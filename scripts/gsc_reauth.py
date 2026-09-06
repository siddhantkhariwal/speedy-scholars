#!/usr/bin/env python3
"""
Re-authorise Google Search Console and write a fresh token file.

Run this in YOUR terminal (not through Claude), because it needs to open a
browser window for the Google consent screen:

    pip3 install google-auth-oauthlib
    python3 scripts/gsc_reauth.py

IMPORTANT: if the OAuth consent screen in Google Cloud Console is still in
"Testing" publishing status, Google expires the refresh token after 7 days.
The previous token died after 6.4 days for exactly this reason. Publish the
consent screen ("In production") first, or you will be back here next week.
"""
import json
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENT_SECRETS = os.path.join(BASE, "gsc-oauth-credentials.json")
TOKEN_PATH = os.path.join(BASE, "gsc-oauth-credentials_token.json")
SCOPES = ["https://www.googleapis.com/auth/webmasters"]

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
except ImportError:
    sys.exit("Missing dependency. Run:\n\n    pip3 install google-auth-oauthlib\n")

if not os.path.exists(CLIENT_SECRETS):
    sys.exit(f"Client secrets not found at {CLIENT_SECRETS}")

print("A browser window will open. Sign in with the Google account that owns")
print("Search Console for speedyscholars.com, then click Allow.\n")

flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
# access_type=offline + prompt=consent forces Google to issue a NEW refresh token.
creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")

token = {
    "access_token": creds.token,
    "refresh_token": creds.refresh_token,
    "scope": " ".join(creds.scopes or SCOPES),
    "token_type": "Bearer",
    "expiry_date": int(creds.expiry.timestamp() * 1000) if creds.expiry else None,
}
with open(TOKEN_PATH, "w") as f:
    json.dump(token, f, indent=2)

print(f"\nWrote fresh token to {TOKEN_PATH}")
print(f"refresh_token issued: {bool(creds.refresh_token)}")

rt_days = None
if creds.expiry:
    print(f"access token valid until: {creds.expiry}")
print("\nNext: run /mcp in Claude Code to restart the servers, then ask Claude to retry.")
