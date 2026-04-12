#!/usr/bin/env python3
"""
Speedy Scholars — Daily Morning Brief
Pulls GA4 (7-day traffic + events) + GSC (28-day queries + quick wins)
Usage: python3 scripts/morning_brief.py
"""

import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, DateRange, Metric, Dimension
from google.oauth2 import service_account
from datetime import date, timedelta
import json, os, warnings
warnings.filterwarnings("ignore")

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GA_CREDS_PATH  = os.path.join(BASE, "speedy-scholars-114b292fc6d8.json")
GSC_TOKEN_PATH = os.path.join(BASE, "gsc-oauth-credentials_token.json")
GA_PROPERTY_ID = "521738025"
GSC_SITE       = "https://www.speedyscholars.com/"

TODAY     = date.today().isoformat()
WEEK_AGO  = (date.today() - timedelta(days=7)).isoformat()
MONTH_AGO = (date.today() - timedelta(days=28)).isoformat()


def ga4_client():
    creds = service_account.Credentials.from_service_account_file(
        GA_CREDS_PATH,
        scopes=["https://www.googleapis.com/auth/analytics.readonly"]
    )
    return BetaAnalyticsDataClient(credentials=creds)


def gsc_client():
    with open(GSC_TOKEN_PATH) as f:
        t = json.load(f)
    creds = Credentials(
        token=t["access_token"], refresh_token=t["refresh_token"],
        token_uri="https://oauth2.googleapis.com/token",
        client_id=t["client_id"], client_secret=t["client_secret"],
    )
    return googleapiclient.discovery.build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def run_brief():
    print(f"""
╔══════════════════════════════════════════════════════════╗
║     SPEEDY SCHOLARS — MORNING BRIEF  ({TODAY})      ║
╚══════════════════════════════════════════════════════════╝
""")

    # ── GA4 ──────────────────────────────────────────────────────────────────
    ga = ga4_client()
    PROP = f"properties/{GA_PROPERTY_ID}"

    r = ga.run_report(RunReportRequest(
        property=PROP,
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
        metrics=[
            Metric(name="sessions"), Metric(name="activeUsers"),
            Metric(name="bounceRate"), Metric(name="averageSessionDuration"),
            Metric(name="engagedSessions"),
        ],
    ))
    total_sessions  = sum(int(x.metric_values[0].value) for x in r.rows)
    total_users     = sum(int(x.metric_values[1].value) for x in r.rows)
    avg_bounce      = sum(float(x.metric_values[2].value) for x in r.rows) / max(len(r.rows), 1) * 100
    avg_duration    = sum(float(x.metric_values[3].value) for x in r.rows) / max(len(r.rows), 1)
    engaged         = sum(int(x.metric_values[4].value) for x in r.rows)

    r2 = ga.run_report(RunReportRequest(
        property=PROP,
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
        metrics=[Metric(name="sessions")],
        dimensions=[Dimension(name="sessionDefaultChannelGroup")],
    ))
    sources = {row.dimension_values[0].value: int(row.metric_values[0].value) for row in r2.rows}

    r3 = ga.run_report(RunReportRequest(
        property=PROP,
        date_ranges=[DateRange(start_date="7daysAgo", end_date="today")],
        metrics=[Metric(name="eventCount")],
        dimensions=[Dimension(name="eventName")],
    ))
    events = {row.dimension_values[0].value: int(row.metric_values[0].value) for row in r3.rows}

    print("TRAFFIC  (last 7 days)")
    print(f"   Sessions:         {total_sessions}")
    print(f"   Users:            {total_users}")
    print(f"   Engaged sessions: {engaged}")
    print(f"   Avg bounce:       {avg_bounce:.0f}%")
    print(f"   Avg session len:  {avg_duration:.0f}s")
    print()
    print("   Sources:")
    for k, v in sorted(sources.items(), key=lambda x: -x[1]):
        print(f"     {k:<24} {v}")

    print()
    print("KEY EVENTS  (last 7 days)")
    key_events = ["book_demo_click", "form_start", "user_engagement", "scroll", "page_view"]
    for k in key_events:
        if k in events:
            print(f"   {k:<27} {events[k]}")

    # ── GSC ──────────────────────────────────────────────────────────────────
    gsc = gsc_client()

    queries_resp = gsc.searchanalytics().query(siteUrl=GSC_SITE, body={
        "startDate": MONTH_AGO, "endDate": TODAY,
        "dimensions": ["query"], "rowLimit": 25,
    }).execute()

    pages_resp = gsc.searchanalytics().query(siteUrl=GSC_SITE, body={
        "startDate": MONTH_AGO, "endDate": TODAY,
        "dimensions": ["page"], "rowLimit": 10,
    }).execute()

    queries = queries_resp.get("rows", [])
    quick_wins = [r for r in queries if 4 <= r["position"] <= 15 and r["impressions"] >= 5]

    print()
    print("GSC TOP QUERIES  (last 28 days)")
    for row in sorted(queries, key=lambda x: -x["impressions"])[:10]:
        print(f"   '{row['keys'][0]}'")
        print(f"      clicks: {row['clicks']}  impressions: {row['impressions']}  pos: {row['position']:.1f}")

    print()
    print("QUICK WINS  (pos 4-15, 5+ impressions)")
    if quick_wins:
        for row in sorted(quick_wins, key=lambda x: x["position"])[:6]:
            print(f"   pos {row['position']:.1f}  '{row['keys'][0]}'  ({row['impressions']} impressions)")
    else:
        print("   None yet")

    print()
    print("TOP PAGES  (GSC, last 28 days)")
    for row in sorted(pages_resp.get("rows", []), key=lambda x: -x["impressions"])[:6]:
        path = row["keys"][0].replace("https://www.speedyscholars.com", "")
        print(f"   {path or '/'}")
        print(f"      clicks: {row['clicks']}  impressions: {row['impressions']}  pos: {row['position']:.1f}")

    print()
    print("─" * 58)


if __name__ == "__main__":
    run_brief()
