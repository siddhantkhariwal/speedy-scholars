import { NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

export async function POST(req: Request) {
  try {
    const data = await req.json();
    const { ga4, gsc } = data;

    const briefText = `
SPEEDY SCHOLARS — ANALYTICS DATA (as of today)

GA4 — Last 7 Days:
- Sessions: ${ga4.totalSessions}
- Users: ${ga4.totalUsers}
- Engaged sessions: ${ga4.engaged}
- Avg bounce rate: ${ga4.avgBounce.toFixed(0)}%
- Avg session duration: ${ga4.avgDuration.toFixed(0)}s
- Traffic sources: ${ga4.sources.map((s: {name: string; sessions: number}) => `${s.name}: ${s.sessions}`).join(", ")}
- Key events: book_demo_click=${ga4.events["book_demo_click"] ?? 0}, form_start=${ga4.events["form_start"] ?? 0}, user_engagement=${ga4.events["user_engagement"] ?? 0}

Google Search Console — Last 28 Days:
- Top page: /blog/abacus-vs-calculator — ${gsc.pages[0]?.impressions ?? 0} impressions, ${gsc.pages[0]?.clicks ?? 0} clicks, position ${gsc.pages[0]?.position?.toFixed(1)}
- Homepage: / — ${gsc.pages.find((p: {page: string}) => p.page === "/")?.impressions ?? 0} impressions, ${gsc.pages.find((p: {page: string}) => p.page === "/")?.clicks ?? 0} clicks

Top search queries:
${gsc.queries.slice(0, 8).map((q: {query: string; impressions: number; clicks: number; position: number}) =>
  `  "${q.query}" — ${q.impressions} impressions, pos ${q.position.toFixed(1)}, ${q.clicks} clicks`
).join("\n")}

Quick wins (pos 4-15 with 5+ impressions):
${gsc.quickWins.map((q: {query: string; impressions: number; position: number}) =>
  `  "${q.query}" — pos ${q.position.toFixed(1)}, ${q.impressions} impressions`
).join("\n")}

Business context:
- Online abacus tutoring, founder Nidhi Khariwal, 20+ years experience
- Target markets: USA, UK, Australia, NZ, Indian diaspora
- Free 45-min demo booking via Calendly is the main CTA
- Site: speedyscholars.com (Next.js, deployed on Vercel)
- No paid ads running currently
- Only 1 blog post is getting meaningful search impressions
`;

    const message = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 1024,
      messages: [
        {
          role: "user",
          content: `You are a growth analyst for Speedy Scholars, an online abacus tutoring business.
Analyse this analytics data and give exactly 5 prioritised action items.

${briefText}

Format your response as a JSON array of exactly 5 objects, each with:
- "priority": number 1-5 (1 = most urgent)
- "category": one of "SEO", "Conversion", "Content", "Traffic", "Technical"
- "action": the specific thing to do (1 sentence, concrete and actionable)
- "why": why this matters right now, referencing the actual data (1 sentence)
- "effort": "Low" | "Medium" | "High"
- "impact": "Low" | "Medium" | "High"

Return ONLY the JSON array, no other text.`,
        },
      ],
    });

    const raw = message.content[0].type === "text" ? message.content[0].text : "[]";
    const text = raw.replace(/^```json\s*/i, "").replace(/^```\s*/i, "").replace(/```\s*$/i, "").trim();
    const actions = JSON.parse(text);

    return NextResponse.json({ actions });
  } catch (err) {
    console.error(err);
    return NextResponse.json({ error: String(err) }, { status: 500 });
  }
}
