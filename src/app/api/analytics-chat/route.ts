import { NextResponse } from "next/server";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

export async function POST(req: Request) {
  try {
    const { question, briefData } = await req.json();
    const { ga4, gsc } = briefData;

    const context = `
You are the analytics assistant for Speedy Scholars, an online abacus tutoring business run by Nidhi Khariwal.
Answer the founder's questions about their website data. Be specific — use the actual numbers.
Never say "I don't have access to" — you have all the data below.
Rules: no emojis, no H1/H2 headings, no horizontal rules. Use plain paragraphs, bullet points, or a table if needed. Keep it concise — 3-5 sentences or a short list. End with one clear recommendation.

LIVE DATA:

GA4 — Last 7 Days:
- Sessions: ${ga4.totalSessions}, Users: ${ga4.totalUsers}, Engaged: ${ga4.engaged}
- Avg bounce: ${ga4.avgBounce.toFixed(0)}%, Avg session: ${ga4.avgDuration.toFixed(0)}s
- Sources: ${ga4.sources.map((s: {name: string; sessions: number}) => `${s.name} (${s.sessions})`).join(", ")}
- Events: book_demo_click=${ga4.events["book_demo_click"] ?? 0}, form_start=${ga4.events["form_start"] ?? 0}, user_engagement=${ga4.events["user_engagement"] ?? 0}, scroll=${ga4.events["scroll"] ?? 0}
- Daily sessions: ${ga4.daily.map((d: {date: string; sessions: number}) => `${d.date.slice(4)}: ${d.sessions}`).join(", ")}

GSC — Last 28 Days:
- Top page: /blog/abacus-vs-calculator — ${gsc.pages[0]?.impressions ?? 0} impressions, ${gsc.pages[0]?.clicks ?? 0} clicks, pos ${gsc.pages[0]?.position?.toFixed(1)}
- Homepage: ${gsc.pages.find((p: {page: string}) => p.page === "/")?.impressions ?? 0} impressions, ${gsc.pages.find((p: {page: string}) => p.page === "/")?.clicks ?? 0} clicks
- Top queries: ${gsc.queries.slice(0, 6).map((q: {query: string; impressions: number; clicks: number; position: number}) => `"${q.query}" (${q.impressions} impr, pos ${q.position.toFixed(1)})`).join("; ")}
- Quick wins (pos 4-15): ${gsc.quickWins.map((q: {query: string; impressions: number; position: number}) => `"${q.query}" pos ${q.position.toFixed(1)}, ${q.impressions} impr`).join("; ")}

Business context:
- Free 45-min demo booking is the main CTA
- No paid ads running
- Target: USA, UK, Australia, NZ, Indian diaspora
- Only 1 blog post getting meaningful organic traffic so far
`;

    const message = await client.messages.create({
      model: "claude-sonnet-4-6",
      max_tokens: 512,
      messages: [
        { role: "user", content: context + "\n\nFounder's question: " + question },
      ],
    });

    const answer = message.content[0].type === "text" ? message.content[0].text : "Sorry, I couldn't process that.";
    return NextResponse.json({ answer });
  } catch (err) {
    console.error(err);
    return NextResponse.json({ error: String(err) }, { status: 500 });
  }
}
