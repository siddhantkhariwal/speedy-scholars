import { NextResponse } from "next/server";
import { BetaAnalyticsDataClient } from "@google-analytics/data";
import { google } from "googleapis";

const GA_PROPERTY_ID = "521738025";
const GSC_SITE = "https://www.speedyscholars.com/";

export async function GET() {
  try {
    // ── GA4 ──────────────────────────────────────────────────────────────
    // Credentials from env var (JSON string) or file path fallback for local dev
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    let gaClientOptions: any = {};
    if (process.env.GA_SERVICE_ACCOUNT_JSON) {
      gaClientOptions = { credentials: JSON.parse(process.env.GA_SERVICE_ACCOUNT_JSON) };
    } else {
      gaClientOptions = { keyFilename: "speedy-scholars-114b292fc6d8.json" };
    }
    const gaClient = new BetaAnalyticsDataClient(gaClientOptions);

    const [overviewResp] = await gaClient.runReport({
      property: `properties/${GA_PROPERTY_ID}`,
      dateRanges: [{ startDate: "7daysAgo", endDate: "today" }],
      metrics: [
        { name: "sessions" },
        { name: "activeUsers" },
        { name: "bounceRate" },
        { name: "averageSessionDuration" },
        { name: "engagedSessions" },
      ],
    });

    const [sourcesResp] = await gaClient.runReport({
      property: `properties/${GA_PROPERTY_ID}`,
      dateRanges: [{ startDate: "7daysAgo", endDate: "today" }],
      metrics: [{ name: "sessions" }],
      dimensions: [{ name: "sessionDefaultChannelGroup" }],
    });

    const [eventsResp] = await gaClient.runReport({
      property: `properties/${GA_PROPERTY_ID}`,
      dateRanges: [{ startDate: "7daysAgo", endDate: "today" }],
      metrics: [{ name: "eventCount" }],
      dimensions: [{ name: "eventName" }],
    });

    const [dailyResp] = await gaClient.runReport({
      property: `properties/${GA_PROPERTY_ID}`,
      dateRanges: [{ startDate: "7daysAgo", endDate: "today" }],
      metrics: [{ name: "sessions" }],
      dimensions: [{ name: "date" }],
    });

    const rows = overviewResp.rows ?? [];
    const totalSessions = rows.reduce((s, r) => s + parseInt(r.metricValues?.[0]?.value ?? "0"), 0);
    const totalUsers = rows.reduce((s, r) => s + parseInt(r.metricValues?.[1]?.value ?? "0"), 0);
    const avgBounce = rows.length
      ? (rows.reduce((s, r) => s + parseFloat(r.metricValues?.[2]?.value ?? "0"), 0) / rows.length) * 100
      : 0;
    const avgDuration = rows.length
      ? rows.reduce((s, r) => s + parseFloat(r.metricValues?.[3]?.value ?? "0"), 0) / rows.length
      : 0;
    const engaged = rows.reduce((s, r) => s + parseInt(r.metricValues?.[4]?.value ?? "0"), 0);

    const sources = (sourcesResp.rows ?? [])
      .map((r) => ({ name: r.dimensionValues?.[0]?.value ?? "", sessions: parseInt(r.metricValues?.[0]?.value ?? "0") }))
      .sort((a, b) => b.sessions - a.sessions);

    const events = Object.fromEntries(
      (eventsResp.rows ?? []).map((r) => [r.dimensionValues?.[0]?.value, parseInt(r.metricValues?.[0]?.value ?? "0")])
    );

    const daily = (dailyResp.rows ?? [])
      .map((r) => ({
        date: r.dimensionValues?.[0]?.value ?? "",
        sessions: parseInt(r.metricValues?.[0]?.value ?? "0"),
      }))
      .sort((a, b) => a.date.localeCompare(b.date));

    // ── GSC ──────────────────────────────────────────────────────────────
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    let gscAuth: any;
    if (process.env.GSC_TOKEN_JSON) {
      const t = JSON.parse(process.env.GSC_TOKEN_JSON);
      const oauth2 = new google.auth.OAuth2(t.client_id, t.client_secret);
      oauth2.setCredentials({ access_token: t.access_token, refresh_token: t.refresh_token });
      gscAuth = oauth2;
    } else {
      const fs = await import("fs");
      const t = JSON.parse(fs.readFileSync("gsc-oauth-credentials_token.json", "utf-8"));
      const oauth2 = new google.auth.OAuth2(t.client_id, t.client_secret);
      oauth2.setCredentials({ access_token: t.access_token, refresh_token: t.refresh_token });
      gscAuth = oauth2;
    }

    const gsc = google.searchconsole({ version: "v1", auth: gscAuth });
    const today = new Date().toISOString().split("T")[0];
    const monthAgo = new Date(Date.now() - 28 * 86400000).toISOString().split("T")[0];

    const [queriesRes, pagesRes] = await Promise.all([
      gsc.searchanalytics.query({
        siteUrl: GSC_SITE,
        requestBody: { startDate: monthAgo, endDate: today, dimensions: ["query"], rowLimit: 25 },
      }),
      gsc.searchanalytics.query({
        siteUrl: GSC_SITE,
        requestBody: { startDate: monthAgo, endDate: today, dimensions: ["page"], rowLimit: 10 },
      }),
    ]);

    const queries = (queriesRes.data.rows ?? []).map((r) => ({
      query: r.keys?.[0] ?? "",
      clicks: r.clicks ?? 0,
      impressions: r.impressions ?? 0,
      position: r.position ?? 0,
    }));

    const pages = (pagesRes.data.rows ?? [])
      .map((r) => ({
        page: (r.keys?.[0] ?? "").replace("https://www.speedyscholars.com", "") || "/",
        clicks: r.clicks ?? 0,
        impressions: r.impressions ?? 0,
        position: r.position ?? 0,
      }))
      .sort((a, b) => b.impressions - a.impressions);

    const quickWins = queries
      .filter((q) => q.position >= 4 && q.position <= 15 && q.impressions >= 5)
      .sort((a, b) => b.impressions - a.impressions)
      .slice(0, 6);

    const topQuery = [...queries].sort((a, b) => b.impressions - a.impressions)[0];

    return NextResponse.json({
      generatedAt: new Date().toISOString(),
      ga4: { totalSessions, totalUsers, engaged, avgBounce, avgDuration, sources, events, daily },
      gsc: { queries: queries.slice(0, 12), pages, quickWins, topQuery },
    });
  } catch (err) {
    console.error(err);
    return NextResponse.json({ error: String(err) }, { status: 500 });
  }
}
