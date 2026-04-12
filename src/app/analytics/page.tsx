"use client";

import { useEffect, useState } from "react";
import Image from "next/image";

// Simple access guard — set NEXT_PUBLIC_ANALYTICS_PASSWORD in .env.local
// Leave it unset in Vercel production to block public access
const ACCESS_PASSWORD = process.env.NEXT_PUBLIC_ANALYTICS_PASSWORD ?? "";

function renderMarkdown(text: string) {
  const lines = text.split("\n");
  const elements: React.ReactNode[] = [];
  let i = 0;

  const inlineFormat = (str: string, key: number): React.ReactNode => {
    const parts = str.split(/(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)/g);
    return (
      <span key={key}>
        {parts.map((p, j) => {
          if (p.startsWith("**") && p.endsWith("**")) return <strong key={j}>{p.slice(2, -2)}</strong>;
          if (p.startsWith("*") && p.endsWith("*")) return <em key={j}>{p.slice(1, -1)}</em>;
          if (p.startsWith("`") && p.endsWith("`")) return <code key={j} style={{ background: "#F5EDE3", borderRadius: 3, padding: "1px 5px", fontSize: 12, fontFamily: "monospace" }}>{p.slice(1, -1)}</code>;
          return p;
        })}
      </span>
    );
  };

  while (i < lines.length) {
    const line = lines[i];

    // Table
    if (line.startsWith("|") && lines[i + 1]?.match(/^\|[-| ]+\|$/)) {
      const headers = line.split("|").filter((c) => c.trim()).map((c) => c.trim());
      i += 2;
      const rows: string[][] = [];
      while (i < lines.length && lines[i].startsWith("|")) {
        rows.push(lines[i].split("|").filter((c) => c.trim()).map((c) => c.trim()));
        i++;
      }
      elements.push(
        <div key={i} style={{ overflowX: "auto", margin: "10px 0" }}>
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12 }}>
            <thead>
              <tr>{headers.map((h, j) => <th key={j} style={{ background: "#F5EDE3", color: "#5A4830", padding: "6px 10px", textAlign: "left", borderBottom: "2px solid #D4B896", fontWeight: 700 }}>{h}</th>)}</tr>
            </thead>
            <tbody>
              {rows.map((row, ri) => (
                <tr key={ri} style={{ background: ri % 2 === 0 ? "#fff" : "#FFF8F0" }}>
                  {row.map((cell, ci) => <td key={ci} style={{ padding: "6px 10px", borderBottom: "1px solid #F5EDE3", color: "#5A4830" }}>{cell}</td>)}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      );
      continue;
    }

    // Heading
    if (line.startsWith("## ")) {
      elements.push(<div key={i} style={{ fontWeight: 700, fontSize: 14, color: "#5A4830", margin: "10px 0 4px" }}>{line.slice(3)}</div>);
    } else if (line.startsWith("# ")) {
      elements.push(<div key={i} style={{ fontWeight: 700, fontSize: 15, color: "#5A4830", margin: "10px 0 4px" }}>{line.slice(2)}</div>);
    }
    // Horizontal rule
    else if (line.match(/^---+$/)) {
      elements.push(<hr key={i} style={{ border: "none", borderTop: "1px solid #D4B896", margin: "10px 0" }} />);
    }
    // Bullet
    else if (line.match(/^[-*] /)) {
      elements.push(
        <div key={i} style={{ display: "flex", gap: 8, margin: "3px 0" }}>
          <span style={{ color: "#C9A86C", flexShrink: 0 }}>•</span>
          <span>{inlineFormat(line.slice(2), i)}</span>
        </div>
      );
    }
    // Empty line
    else if (line.trim() === "") {
      elements.push(<div key={i} style={{ height: 6 }} />);
    }
    // Normal paragraph
    else {
      elements.push(<div key={i} style={{ margin: "2px 0" }}>{inlineFormat(line, i)}</div>);
    }
    i++;
  }
  return elements;
}

interface BriefData {
  generatedAt: string;
  ga4: {
    totalSessions: number;
    totalUsers: number;
    engaged: number;
    avgBounce: number;
    avgDuration: number;
    sources: { name: string; sessions: number }[];
    events: Record<string, number>;
    daily: { date: string; sessions: number }[];
  };
  gsc: {
    queries: { query: string; clicks: number; impressions: number; position: number }[];
    pages: { page: string; clicks: number; impressions: number; position: number }[];
    quickWins: { query: string; clicks: number; impressions: number; position: number }[];
    topQuery: { query: string; clicks: number; impressions: number; position: number };
  };
}

interface ActionItem {
  priority: number;
  category: string;
  action: string;
  why: string;
  effort: "Low" | "Medium" | "High";
  impact: "Low" | "Medium" | "High";
}

const CATEGORY_COLORS: Record<string, string> = {
  SEO: "#8B6F47",
  Conversion: "#5A4830",
  Content: "#6B5335",
  Traffic: "#8B6F47",
  Technical: "#5A4830",
};

const IMPACT_BG: Record<string, string> = {
  High: "#5A4830",
  Medium: "#8B6F47",
  Low: "#D4B896",
};

const IMPACT_COLOR: Record<string, string> = {
  High: "#fff",
  Medium: "#fff",
  Low: "#5A4830",
};

function StatCard({ label, value, sub, accent }: { label: string; value: string | number; sub?: string; accent?: boolean }) {
  return (
    <div style={{
      background: accent ? "#8B6F47" : "#FFF8F0",
      border: `1.5px solid ${accent ? "#8B6F47" : "#D4B896"}`,
      borderRadius: 12,
      padding: "20px 24px",
      display: "flex",
      flexDirection: "column",
      gap: 4,
    }}>
      <span style={{ fontSize: 12, fontWeight: 600, color: accent ? "#D4B896" : "#8B6F47", textTransform: "uppercase", letterSpacing: 1 }}>{label}</span>
      <span style={{ fontSize: 32, fontWeight: 700, color: accent ? "#fff" : "#5A4830", lineHeight: 1.1 }}>{value}</span>
      {sub && <span style={{ fontSize: 12, color: accent ? "#D4B896" : "#8B6F47" }}>{sub}</span>}
    </div>
  );
}

function MiniBar({ value, max, color = "#C9A86C" }: { value: number; max: number; color?: string }) {
  return (
    <div style={{ flex: 1, height: 6, background: "#F5EDE3", borderRadius: 3, overflow: "hidden" }}>
      <div style={{ width: `${Math.min((value / max) * 100, 100)}%`, height: "100%", background: color, borderRadius: 3 }} />
    </div>
  );
}

function Badge({ label, value }: { label: string; value: string }) {
  return (
    <span style={{
      background: IMPACT_BG[value] ?? "#D4B896",
      color: IMPACT_COLOR[value] ?? "#5A4830",
      fontSize: 10,
      fontWeight: 700,
      borderRadius: 4,
      padding: "2px 7px",
      textTransform: "uppercase",
      letterSpacing: 0.5,
    }}>
      {label}: {value}
    </span>
  );
}

export default function AnalyticsDashboard() {
  const [data, setData] = useState<BriefData | null>(null);
  const [actions, setActions] = useState<ActionItem[] | null>(null);
  const [loadingData, setLoadingData] = useState(false);
  const [loadingActions, setLoadingActions] = useState(false);
  const [lastFetched, setLastFetched] = useState<string | null>(null);
  const [chatMessages, setChatMessages] = useState<{ role: "user" | "claude"; text: string }[]>([]);
  const [chatInput, setChatInput] = useState("");
  const [chatLoading, setChatLoading] = useState(false);

  const fetchActions = async (briefData: BriefData) => {
    setLoadingActions(true);
    setActions(null);
    try {
      const res = await fetch("/api/action-items", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ga4: briefData.ga4, gsc: briefData.gsc }),
      });
      const json = await res.json();
      setActions(json.actions ?? []);
    } finally {
      setLoadingActions(false);
    }
  };

  const fetchBrief = async () => {
    setLoadingData(true);
    try {
      const res = await fetch("/api/analytics-brief");
      const json = await res.json();
      setData(json);
      setLastFetched(new Date().toLocaleTimeString());
      fetchActions(json);
    } finally {
      setLoadingData(false);
    }
  };

  const askClaude = async () => {
    if (!chatInput.trim() || !data || chatLoading) return;
    const question = chatInput.trim();
    setChatInput("");
    setChatMessages((prev) => [...prev, { role: "user", text: question }]);
    setChatLoading(true);
    try {
      const res = await fetch("/api/analytics-chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question, briefData: { ga4: data.ga4, gsc: data.gsc } }),
      });
      const json = await res.json();
      setChatMessages((prev) => [...prev, { role: "claude", text: json.answer ?? json.error }]);
    } finally {
      setChatLoading(false);
    }
  };

  const [authed, setAuthed] = useState(!ACCESS_PASSWORD);
  const [pwInput, setPwInput] = useState("");

  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => { if (authed) fetchBrief(); }, [authed]);

  if (!authed) {
    return (
      <div style={{ minHeight: "100vh", background: "#F5EDE3", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Arial, sans-serif" }}>
        <div style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 16, padding: "40px 48px", textAlign: "center", maxWidth: 360 }}>
          <div style={{ color: "#5A4830", fontSize: 20, fontWeight: 700, marginBottom: 8 }}>Analytics</div>
          <div style={{ color: "#8B6F47", fontSize: 13, marginBottom: 24 }}>Enter password to continue</div>
          <input
            type="password"
            value={pwInput}
            onChange={(e) => setPwInput(e.target.value)}
            onKeyDown={(e) => { if (e.key === "Enter" && pwInput === ACCESS_PASSWORD) setAuthed(true); }}
            placeholder="Password"
            style={{ width: "100%", padding: "10px 14px", border: "1.5px solid #D4B896", borderRadius: 8, fontSize: 14, color: "#5A4830", background: "#FFF8F0", outline: "none", marginBottom: 12, boxSizing: "border-box" }}
          />
          <button
            onClick={() => { if (pwInput === ACCESS_PASSWORD) setAuthed(true); }}
            style={{ width: "100%", background: "#8B6F47", color: "#fff", border: "none", borderRadius: 8, padding: "10px", fontSize: 14, fontWeight: 700, cursor: "pointer" }}
          >
            Enter
          </button>
        </div>
      </div>
    );
  }

  const maxImpressions = data ? Math.max(...data.gsc.queries.map((q) => q.impressions), 1) : 1;
  const maxSessions = data ? Math.max(...data.ga4.daily.map((d) => d.sessions), 1) : 1;

  return (
    <div style={{ minHeight: "100vh", background: "#F5EDE3", fontFamily: "Arial, sans-serif" }}>
      {/* Header */}
      <div style={{ background: "#5A4830", padding: "16px 40px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
          <Image src="/images/logo3_transparent.png" alt="Speedy Scholars" width={48} height={24} style={{ filter: "brightness(0) invert(1)" }} />
          <div>
            <div style={{ color: "#C9A86C", fontSize: 11, fontWeight: 600, letterSpacing: 1, textTransform: "uppercase" }}>Speedy Scholars</div>
            <div style={{ color: "#fff", fontSize: 18, fontWeight: 700 }}>Analytics Morning Brief</div>
          </div>
        </div>
        <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
          {lastFetched && <span style={{ color: "#D4B896", fontSize: 12 }}>Updated {lastFetched}</span>}
          <button
            onClick={fetchBrief}
            disabled={loadingData}
            style={{
              background: loadingData ? "#8B6F47" : "#C9A86C",
              color: "#5A4830",
              border: "none",
              borderRadius: 8,
              padding: "8px 20px",
              fontSize: 13,
              fontWeight: 700,
              cursor: loadingData ? "not-allowed" : "pointer",
            }}
          >
            {loadingData ? "Pulling data..." : "Refresh"}
          </button>
        </div>
      </div>

      {loadingData && !data && (
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", height: "60vh" }}>
          <div style={{ textAlign: "center" }}>
            <div style={{ color: "#8B6F47", fontWeight: 600, fontSize: 16 }}>Connecting to GA4 + Search Console...</div>
          </div>
        </div>
      )}

      {data && (
        <div style={{ padding: "32px 40px", maxWidth: 1200, margin: "0 auto" }}>

          {/* Traffic Overview */}
          <h2 style={{ color: "#5A4830", fontSize: 13, fontWeight: 700, textTransform: "uppercase", letterSpacing: 1.5, margin: "0 0 16px" }}>
            Traffic — Last 7 Days (GA4)
          </h2>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(5, 1fr)", gap: 16, marginBottom: 32 }}>
            <StatCard label="Sessions" value={data.ga4.totalSessions} accent />
            <StatCard label="Users" value={data.ga4.totalUsers} />
            <StatCard label="Engaged" value={data.ga4.engaged} sub="sessions with 10s+ engagement" />
            <StatCard label="Avg Bounce" value={`${data.ga4.avgBounce.toFixed(0)}%`} />
            <StatCard label="Avg Session" value={`${data.ga4.avgDuration.toFixed(0)}s`} />
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 24, marginBottom: 32 }}>
            {/* Daily chart */}
            <div style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12, padding: 24 }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#8B6F47", textTransform: "uppercase", letterSpacing: 1, marginBottom: 16 }}>Daily Sessions</div>
              <div style={{ display: "flex", alignItems: "flex-end", gap: 6, height: 80 }}>
                {data.ga4.daily.map((d) => (
                  <div key={d.date} style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", gap: 4 }}>
                    <div style={{ width: "100%", background: "#C9A86C", borderRadius: "3px 3px 0 0", height: `${Math.max((d.sessions / maxSessions) * 72, 4)}px` }} />
                    <span style={{ fontSize: 9, color: "#8B6F47" }}>{d.date.slice(6)}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Sources */}
            <div style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12, padding: 24 }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#8B6F47", textTransform: "uppercase", letterSpacing: 1, marginBottom: 16 }}>Traffic Sources</div>
              <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
                {data.ga4.sources.map((s) => (
                  <div key={s.name} style={{ display: "flex", alignItems: "center", gap: 10 }}>
                    <span style={{ fontSize: 12, color: "#5A4830", width: 120, flexShrink: 0 }}>{s.name}</span>
                    <MiniBar value={s.sessions} max={data.ga4.totalSessions} />
                    <span style={{ fontSize: 13, fontWeight: 700, color: "#5A4830", width: 24, textAlign: "right" }}>{s.sessions}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Key Events */}
            <div style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12, padding: 24 }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#8B6F47", textTransform: "uppercase", letterSpacing: 1, marginBottom: 16 }}>Key Events</div>
              <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                {["book_demo_click", "form_start", "user_engagement", "scroll"].map((ev) => (
                  data.ga4.events[ev] !== undefined && (
                    <div key={ev} style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                      <span style={{ fontSize: 12, color: "#5A4830", fontFamily: "monospace" }}>{ev}</span>
                      <span style={{
                        background: ev === "book_demo_click" ? "#8B6F47" : "#F5EDE3",
                        color: ev === "book_demo_click" ? "#fff" : "#5A4830",
                        fontWeight: 700, fontSize: 13, borderRadius: 6, padding: "2px 10px",
                      }}>{data.ga4.events[ev]}</span>
                    </div>
                  )
                ))}
              </div>
            </div>
          </div>

          {/* Divider */}
          <div style={{ borderTop: "2px solid #C9A86C", margin: "8px 0 32px" }} />

          {/* GSC Section */}
          <h2 style={{ color: "#5A4830", fontSize: 13, fontWeight: 700, textTransform: "uppercase", letterSpacing: 1.5, margin: "0 0 16px" }}>
            Search Console — Last 28 Days
          </h2>

          {data.gsc.topQuery && (
            <div style={{
              background: "#5A4830", borderRadius: 12, padding: "20px 28px", marginBottom: 24,
              display: "flex", alignItems: "center", justifyContent: "space-between",
            }}>
              <div>
                <div style={{ color: "#C9A86C", fontSize: 11, fontWeight: 700, textTransform: "uppercase", letterSpacing: 1, marginBottom: 6 }}>Top Opportunity</div>
                <div style={{ color: "#fff", fontSize: 18, fontWeight: 700, marginBottom: 4 }}>&ldquo;{data.gsc.topQuery.query}&rdquo;</div>
                <div style={{ color: "#D4B896", fontSize: 13 }}>
                  {data.gsc.topQuery.impressions.toLocaleString()} impressions &mdash; position {data.gsc.topQuery.position.toFixed(1)} &mdash; {data.gsc.topQuery.clicks} clicks
                </div>
              </div>
              <div style={{ textAlign: "right" }}>
                <div style={{ color: "#C9A86C", fontSize: 40, fontWeight: 700 }}>{data.gsc.topQuery.impressions.toLocaleString()}</div>
                <div style={{ color: "#D4B896", fontSize: 12 }}>people searched this</div>
                <div style={{ color: "#D4B896", fontSize: 12 }}>we showed up #{data.gsc.topQuery.position.toFixed(1)}</div>
              </div>
            </div>
          )}

          <div style={{ display: "grid", gridTemplateColumns: "1.4fr 1fr", gap: 24, marginBottom: 32 }}>
            <div style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12, padding: 24 }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#8B6F47", textTransform: "uppercase", letterSpacing: 1, marginBottom: 16 }}>Top Search Queries</div>
              <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                {data.gsc.queries.slice(0, 8).map((q) => (
                  <div key={q.query}>
                    <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
                      <span style={{ fontSize: 12, color: "#5A4830", flex: 1, fontStyle: "italic" }}>&ldquo;{q.query}&rdquo;</span>
                      <span style={{ fontSize: 11, color: "#8B6F47", whiteSpace: "nowrap" }}>#{q.position.toFixed(1)}</span>
                    </div>
                    <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                      <MiniBar value={q.impressions} max={maxImpressions} color="#C9A86C" />
                      <span style={{ fontSize: 11, color: "#8B6F47", whiteSpace: "nowrap" }}>{q.impressions.toLocaleString()} impr</span>
                      <span style={{ fontSize: 11, color: q.clicks > 0 ? "#5A4830" : "#C9A86C", fontWeight: 600, whiteSpace: "nowrap" }}>{q.clicks} clicks</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12, padding: 24 }}>
              <div style={{ fontSize: 12, fontWeight: 700, color: "#8B6F47", textTransform: "uppercase", letterSpacing: 1, marginBottom: 4 }}>Quick Wins</div>
              <div style={{ fontSize: 11, color: "#8B6F47", marginBottom: 16 }}>Pos 4-15 with 5+ impressions — one tweak from page 1</div>
              <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                {data.gsc.quickWins.map((q) => (
                  <div key={q.query} style={{ borderLeft: "3px solid #C9A86C", paddingLeft: 12 }}>
                    <div style={{ fontSize: 12, color: "#5A4830", fontWeight: 600, marginBottom: 2 }}>&ldquo;{q.query}&rdquo;</div>
                    <div style={{ display: "flex", gap: 12 }}>
                      <span style={{ fontSize: 11, color: "#8B6F47" }}>pos {q.position.toFixed(1)}</span>
                      <span style={{ fontSize: 11, color: "#8B6F47" }}>{q.impressions.toLocaleString()} impressions</span>
                    </div>
                  </div>
                ))}
              </div>
              <div style={{ marginTop: 24 }}>
                <div style={{ fontSize: 12, fontWeight: 700, color: "#8B6F47", textTransform: "uppercase", letterSpacing: 1, marginBottom: 12 }}>Top Pages</div>
                {data.gsc.pages.slice(0, 4).map((p) => (
                  <div key={p.page} style={{ display: "flex", justifyContent: "space-between", marginBottom: 8, alignItems: "center" }}>
                    <span style={{ fontSize: 12, color: "#5A4830", fontFamily: "monospace" }}>{p.page}</span>
                    <div style={{ display: "flex", gap: 10 }}>
                      <span style={{ fontSize: 11, color: "#8B6F47" }}>{p.impressions.toLocaleString()} impr</span>
                      <span style={{ fontSize: 11, fontWeight: 700, color: "#5A4830" }}>{p.clicks} clicks</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* ── AI ACTION ITEMS ─────────────────────────────────────────── */}
          <div style={{ borderTop: "2px solid #C9A86C", margin: "8px 0 32px" }} />
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 16 }}>
            <div>
              <h2 style={{ color: "#5A4830", fontSize: 13, fontWeight: 700, textTransform: "uppercase", letterSpacing: 1.5, margin: 0 }}>
                Claude&rsquo;s Action Items
              </h2>
              <div style={{ color: "#8B6F47", fontSize: 12, marginTop: 4 }}>
                AI analysis of your data — what to do next, ranked by impact
              </div>
            </div>
            <button
              onClick={() => data && fetchActions(data)}
              disabled={loadingActions}
              style={{
                background: "transparent",
                border: "1.5px solid #C9A86C",
                color: "#8B6F47",
                borderRadius: 8,
                padding: "6px 16px",
                fontSize: 12,
                fontWeight: 700,
                cursor: loadingActions ? "not-allowed" : "pointer",
              }}
            >
              {loadingActions ? "Analysing..." : "Re-analyse"}
            </button>
          </div>

          {loadingActions && (
            <div style={{
              background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12,
              padding: 32, textAlign: "center", marginBottom: 32,
            }}>
              <div style={{ color: "#8B6F47", fontSize: 14, fontWeight: 600, marginBottom: 8 }}>
                Claude is analysing your data...
              </div>
              <div style={{ color: "#8B6F47", fontSize: 12 }}>
                Reading GA4 traffic, Search Console queries, bounce rates, and identifying your highest-leverage moves
              </div>
            </div>
          )}

          {actions && !loadingActions && (
            <div style={{ display: "flex", flexDirection: "column", gap: 16, marginBottom: 32 }}>
              {actions.map((item) => (
                <div key={item.priority} style={{
                  background: "#FFF8F0",
                  border: `1.5px solid ${item.priority === 1 ? "#8B6F47" : "#D4B896"}`,
                  borderLeft: `4px solid ${CATEGORY_COLORS[item.category] ?? "#8B6F47"}`,
                  borderRadius: 12,
                  padding: "20px 24px",
                  display: "grid",
                  gridTemplateColumns: "40px 1fr auto",
                  gap: 16,
                  alignItems: "start",
                }}>
                  {/* Priority number */}
                  <div style={{
                    width: 36, height: 36, borderRadius: "50%",
                    background: item.priority === 1 ? "#5A4830" : "#F5EDE3",
                    border: `2px solid ${item.priority === 1 ? "#5A4830" : "#D4B896"}`,
                    display: "flex", alignItems: "center", justifyContent: "center",
                    color: item.priority === 1 ? "#fff" : "#8B6F47",
                    fontWeight: 700, fontSize: 16, flexShrink: 0,
                  }}>
                    {item.priority}
                  </div>

                  {/* Content */}
                  <div>
                    <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                      <span style={{
                        background: CATEGORY_COLORS[item.category] ?? "#8B6F47",
                        color: "#fff", fontSize: 10, fontWeight: 700,
                        borderRadius: 4, padding: "2px 8px",
                        textTransform: "uppercase", letterSpacing: 0.5,
                      }}>{item.category}</span>
                    </div>
                    <div style={{ fontSize: 15, fontWeight: 700, color: "#5A4830", marginBottom: 6, lineHeight: 1.4 }}>
                      {item.action}
                    </div>
                    <div style={{ fontSize: 13, color: "#8B6F47", lineHeight: 1.5 }}>
                      {item.why}
                    </div>
                  </div>

                  {/* Badges */}
                  <div style={{ display: "flex", flexDirection: "column", gap: 6, alignItems: "flex-end", flexShrink: 0 }}>
                    <Badge label="Impact" value={item.impact} />
                    <Badge label="Effort" value={item.effort} />
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* ── ASK CLAUDE CHAT ─────────────────────────────────────── */}
          <div style={{ borderTop: "2px solid #C9A86C", margin: "8px 0 32px" }} />
          <div style={{ marginBottom: 32 }}>
            <h2 style={{ color: "#5A4830", fontSize: 13, fontWeight: 700, textTransform: "uppercase", letterSpacing: 1.5, margin: "0 0 4px" }}>
              Ask Claude
            </h2>
            <div style={{ color: "#8B6F47", fontSize: 12, marginBottom: 20 }}>
              Ask anything about your data in plain English
            </div>

            {/* Suggested questions */}
            {chatMessages.length === 0 && (
              <div style={{ display: "flex", flexWrap: "wrap", gap: 8, marginBottom: 20 }}>
                {[
                  "What is my top performing page?",
                  "Why am I getting impressions but no clicks?",
                  "Which keyword should I target next?",
                  "How many people tried to book a demo?",
                  "What should I fix first on my site?",
                ].map((q) => (
                  <button
                    key={q}
                    onClick={() => { setChatInput(q); }}
                    style={{
                      background: "#FFF8F0", border: "1.5px solid #D4B896",
                      borderRadius: 20, padding: "6px 14px",
                      fontSize: 12, color: "#8B6F47", cursor: "pointer",
                    }}
                  >
                    {q}
                  </button>
                ))}
              </div>
            )}

            {/* Chat messages */}
            {chatMessages.length > 0 && (
              <div style={{ display: "flex", flexDirection: "column", gap: 12, marginBottom: 16 }}>
                {chatMessages.map((msg, i) => (
                  <div key={i} style={{
                    display: "flex",
                    justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
                  }}>
                    <div style={{
                      maxWidth: "75%",
                      background: msg.role === "user" ? "#8B6F47" : "#FFF8F0",
                      border: msg.role === "claude" ? "1.5px solid #D4B896" : "none",
                      borderRadius: msg.role === "user" ? "16px 16px 4px 16px" : "16px 16px 16px 4px",
                      padding: "12px 16px",
                      fontSize: 13,
                      color: msg.role === "user" ? "#fff" : "#5A4830",
                      lineHeight: 1.6,
                    }}>
                      {msg.role === "claude" && (
                        <div style={{ fontSize: 10, fontWeight: 700, color: "#C9A86C", textTransform: "uppercase", letterSpacing: 1, marginBottom: 8 }}>Claude</div>
                      )}
                      {msg.role === "claude" ? renderMarkdown(msg.text) : msg.text}
                    </div>
                  </div>
                ))}
                {chatLoading && (
                  <div style={{ display: "flex", justifyContent: "flex-start" }}>
                    <div style={{
                      background: "#FFF8F0", border: "1.5px solid #D4B896",
                      borderRadius: "16px 16px 16px 4px", padding: "12px 16px",
                    }}>
                      <div style={{ fontSize: 10, fontWeight: 700, color: "#C9A86C", textTransform: "uppercase", letterSpacing: 1, marginBottom: 6 }}>Claude</div>
                      <div style={{ color: "#8B6F47", fontSize: 13 }}>Thinking...</div>
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Input */}
            <div style={{ display: "flex", gap: 10 }}>
              <input
                type="text"
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && askClaude()}
                placeholder={data ? "Ask about your analytics..." : "Loading data first..."}
                disabled={!data || chatLoading}
                style={{
                  flex: 1, background: "#FFF8F0",
                  border: "1.5px solid #D4B896", borderRadius: 10,
                  padding: "12px 16px", fontSize: 13, color: "#5A4830",
                  outline: "none",
                }}
              />
              <button
                onClick={askClaude}
                disabled={!data || !chatInput.trim() || chatLoading}
                style={{
                  background: (!data || !chatInput.trim() || chatLoading) ? "#D4B896" : "#8B6F47",
                  color: "#fff", border: "none", borderRadius: 10,
                  padding: "12px 24px", fontSize: 13, fontWeight: 700,
                  cursor: (!data || !chatInput.trim() || chatLoading) ? "not-allowed" : "pointer",
                }}
              >
                Ask
              </button>
            </div>
          </div>

          {/* What's Next */}
          <div style={{ borderTop: "2px solid #C9A86C", margin: "8px 0 32px" }} />
          <h2 style={{ color: "#5A4830", fontSize: 13, fontWeight: 700, textTransform: "uppercase", letterSpacing: 1.5, margin: "0 0 16px" }}>
            What&rsquo;s Next
          </h2>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 16, marginBottom: 40 }}>
            {[
              { label: "Now — Live", items: ["GA4 traffic brief", "Search Console queries", "AI action items", "Daily refresh"] },
              { label: "Next — WhatsApp & Ads", items: ["WhatsApp morning brief delivery", "Meta Ads MCP (Instagram campaigns)", "Auto-fix blog title & meta tags", "Lead alerts from Gmail"] },
              { label: "Next — Claude takes action", items: ["Claude opens the PR to fix SEO", "Ad performance briefs when campaigns run", "More MCP integrations as we grow"] },
            ].map((col) => (
              <div key={col.label} style={{ background: "#FFF8F0", border: "1.5px solid #D4B896", borderRadius: 12, padding: 20 }}>
                <div style={{ fontSize: 11, fontWeight: 700, color: "#C9A86C", textTransform: "uppercase", letterSpacing: 1, marginBottom: 12 }}>{col.label}</div>
                {col.items.map((item) => (
                  <div key={item} style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8 }}>
                    <div style={{ width: 6, height: 6, borderRadius: "50%", background: "#C9A86C", flexShrink: 0 }} />
                    <span style={{ fontSize: 13, color: "#5A4830" }}>{item}</span>
                  </div>
                ))}
              </div>
            ))}
          </div>

          <div style={{ textAlign: "center", color: "#8B6F47", fontSize: 12, paddingBottom: 32 }}>
            Powered by Claude Code + MCP &mdash; GA4 &amp; Google Search Console live data
          </div>
        </div>
      )}
    </div>
  );
}
