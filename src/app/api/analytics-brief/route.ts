import { NextResponse } from "next/server";
import { BetaAnalyticsDataClient } from "@google-analytics/data";
import { google } from "googleapis";
import path from "path";

const GA_CREDS = path.join(process.cwd(), "speedy-scholars-114b292fc6d8.json");
const GA_PROPERTY_ID = "521738025";
const GSC_SITE = "https://www.speedyscholars.com/";
const GSC_TOKEN = path.join(process.cwd(), "gsc-oauth-credentials_token.json");

export async function GET() {
  try {
    // ── GA4 ──────────────────────────────────────────────────────────────
    const gaClient = new BetaAnalyticsDataClient({
      keyFilename: GA_CREDS,
    });

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
    const fs = await import("fs");
    const tokenData = JSON.parse(fs.readFileSync(GSC_TOKEN, "utf-8"));

    const auth = new google.auth.OAuth2(tokenData.client_id, tokenData.client_secret);
    auth.setCredentials({
      access_token: tokenData.access_token,
      refresh_token: tokenData.refresh_token,
    });

    const gsc = google.searchconsole({ version: "v1", auth });
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

    const topQuery = queries.sort((a, b) => b.impressions - a.impressions)[0];

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
