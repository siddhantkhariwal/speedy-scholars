# Speedy Scholars — Claude Code Instructions

## What This Project Is
Online abacus tutoring business website. LIVE at https://www.speedyscholars.com
Founder & instructor: Nidhi Khariwal (20+ years, 2000+ students worldwide).
Built with Next.js 14 App Router, deployed on Vercel, auto-deploys on push to `main`.

---

## Tech Stack
- **Framework:** Next.js 14.2.13 (App Router, TypeScript)
- **Styling:** Tailwind CSS — no separate CSS files, inline styles only for brand colours
- **Animations:** Framer Motion (only on "use client" pages)
- **Icons:** Lucide React
- **Booking:** Calendly embed (iframe modal)
- **Analytics:** Google Analytics 4 — ID: G-KYY9RC30T9
- **Currency:** Custom CurrencyContext with auto-detection via ipapi.co
- **Deployment:** Vercel (GitHub auto-deploy on push to main)

---

## Brand Guidelines — Never Deviate From These

### Colours
```
Primary brown:   #8B6F47
Dark brown:      #6B5335
Darker brown:    #5A4830
Gold accent:     #C9A86C
Light gold:      #D4B896
Cream bg:        #F5EDE3
Warm white:      #FFF8F0
```

### Rules
- **No emojis** anywhere in website pages (docs/markdown files are fine)
- **No green** — the old about page used #556B2F olive green, that's been replaced. Never use green on any page.
- Font: Arial / Geist Sans (system default via Next.js)
- Tone: Professional, warm, trustworthy, educational — never salesy or gimmicky

---

## Key Business Facts (Use These for Content)
- Founder: **Nidhi Khariwal**, based in Jaipur, India
- Experience: **20+ years** teaching abacus
- Students: **2,000+** worldwide
- Competition winners: **50+**
- Awards: **15+**
- Languages: English and Hindi
- Target markets: USA, UK, Australia, NZ, Indian diaspora
- Phone: +91 9352646671
- Email: nidhikhariwal2012@gmail.com
- WhatsApp: +919352646671

### Pricing (multi-currency)
| Tier | INR | USD | GBP | AUD |
|------|-----|-----|-----|-----|
| Free Demo (45 min) | FREE | FREE | FREE | FREE |
| Pay-As-You-Go | ₹1,600 | $20 | £15 | A$30 |
| 10-Class Pack | ₹12,500 | $150 | £120 | A$230 |

---

## Important Business Context
- We run a **UCMAS franchise in Jaipur** — Speedy Scholars must remain a **separate online-only brand**. Never reference Jaipur location on the website or suggest Google Business Profile with a physical address.
- The UCMAS franchise has its own Google Business Profile — Speedy Scholars should NOT be connected to it.
- Speedy Scholars is online-only, global, and must not reveal the Jaipur connection publicly.

---

## Project Structure
```
src/
├── app/
│   ├── page.tsx              # Home page ("use client") — main landing page
│   ├── layout.tsx            # Root layout — metadata, GA4, fonts
│   ├── sitemap.ts            # Dynamic sitemap — update when adding pages
│   ├── analytics/
│   │   └── page.tsx          # Analytics dashboard ("use client") — password-protected
│   ├── api/
│   │   ├── analytics-brief/  # GA4 + GSC data API (reads from env vars)
│   │   ├── action-items/     # Claude AI action items from analytics data
│   │   └── analytics-chat/   # Claude chat endpoint for /analytics page
│   ├── about/
│   │   ├── page.tsx          # About page ("use client", Framer Motion)
│   │   └── layout.tsx        # About metadata (server component)
│   ├── contact/
│   │   ├── page.tsx          # Contact form ("use client")
│   │   └── layout.tsx        # Contact metadata (server component)
│   ├── blog/
│   │   ├── page.tsx          # Blog listing (server component)
│   │   └── [slug]/page.tsx   # Individual posts (server component)
│   ├── resources/
│   │   └── page.tsx          # Resources page (server component)
│   ├── privacy/page.tsx
│   └── terms/page.tsx
├── components/
│   ├── StructuredData.tsx    # All JSON-LD schemas — add new ones here
│   ├── GoogleAnalytics.tsx   # GA4 script injection
│   ├── Providers.tsx         # CurrencyProvider wrapper
│   └── ui/                   # Shadcn components
├── contexts/
│   └── CurrencyContext.tsx   # Multi-currency support + selector
└── lib/
    ├── blog.ts               # ALL blog data lives here — add new posts here
    └── utils.ts              # cn() helper

scripts/
├── generate_kg1_book.py      # KG-1 Book A PDF generator (ReportLab)
├── illustrations.py          # Shared illustration library for all books
├── morning_brief.py          # Terminal analytics brief (GA4 + GSC)
└── BOOK_DESIGN_GUIDE.md      # Design rules for all future books
```

---

## Adding a New Blog Post
Only edit `src/lib/blog.ts` — add a new entry to the `blogPosts` array:
```typescript
{
  title: "...",
  slug: "url-slug-here",          // becomes /blog/url-slug-here
  date: "2026-MM-DD",
  excerpt: "...",                  // shown on listing page
  author: "Nidhi Khariwal",
  authorTitle: "Founder & Lead Instructor, Speedy Scholars",
  readTime: "X min read",
  tags: ["tag1", "tag2"],
  metaTitle: "... | Speedy Scholars",
  metaDescription: "...",          // 150-160 chars
  coverImage: "/images/...",       // must exist in public/images/
  content: `...`,                  // markdown-like, rendered by renderContent()
}
```
Then update `src/app/sitemap.ts` — it auto-pulls slugs from blog.ts so no change needed there.

---

## "use client" vs Server Components
- Pages with `useState`, `useEffect`, `onClick`, Framer Motion = **must have "use client"**
- Pages with "use client" **cannot export `generateMetadata`** — create a `layout.tsx` sibling instead (see about/layout.tsx and contact/layout.tsx as examples)
- Blog and resources pages are server components — no "use client", no event handlers in JSX

---

## GA4 Event Tracking
Book Demo button clicks are tracked via `openCalendly(location)` in page.tsx.
Location labels in use: `navbar`, `mobile_menu`, `hero`, `instructor_section`,
`pricing_free_demo`, `pricing_10class`, `pricing_payg`, `cta_section`

GA4 Property ID: `521738025`
Service account credentials: `speedy-scholars-114b292fc6d8.json` (gitignored — never commit)

---

## Analytics Dashboard (/analytics)

Password-protected page with live GA4 + GSC data, Claude AI action items, and a chat interface.

### Credentials (all in .env.local — never commit)
- `GA_SERVICE_ACCOUNT_JSON` — full service account JSON as single-line string
- `GSC_TOKEN_JSON` — OAuth token JSON from `gsc-oauth-credentials_token.json`
- `ANTHROPIC_API_KEY` — for action items + chat
- `NEXT_PUBLIC_ANALYTICS_PASSWORD` — local access password (set to `speedy123` in .env.local, NOT set on Vercel = blocked publicly)

### GSC OAuth files (gitignored)
- `gsc-oauth-credentials.json` — OAuth client credentials
- `gsc-oauth-credentials_token.json` — saved OAuth token (refresh token inside, auto-refreshes)

### MCP servers (registered in Claude Code)
- `google-analytics` — `npx mcp-google-analytics` with GA_SERVICE_ACCOUNT_JSON + GA_PROPERTY_ID
- `gsc` — `npx mcp-gsc@latest` with GOOGLE_GSC_CREDENTIALS_PATH

---

## Book Design System

KG-1 Book A: 35-page landscape A4 PDF. Generator: `scripts/generate_kg1_book.py`.
Full design rules: `scripts/BOOK_DESIGN_GUIDE.md`
Output: `public/Speedy-Scholars-KG1-Book-A.pdf`

### Key rules (never break these)
- Upper abacus beads: **hexagonal** (6-sided polygon)
- Mascot: graduation-hat bead bird on **every page** via `draw_footer()`
- Logo: `public/images/logo3_transparent.png` (white bg removed)
- Use **"Level"** not "Class" — abacus terminology
- Object padding from card borders: **20px minimum**
- Every calc page must have **unique problem data**
- Bottom strip shows **both groups** (a objects + operator + b objects)

### Future books planned
KG-1 Book B, KG-2 Book A/B, Level 1 Book A/B — reuse `illustrations.py`

---

## ESLint Rules That Bite
- No `any` type — use `eslint-disable-next-line` with a comment explaining why if unavoidable
- No unused variables — remove them or prefix with `_` (but `_` alone is also flagged, use `catch { }` not `catch (_) { }`)
- No unescaped JSX text — use `&apos;` for `'` and `&quot;` for `"`
- No `Function` type — type it properly

Always run `npm run build` before committing. Build must pass clean.

---

## Common Commands
```bash
npm run dev      # Local dev server at localhost:3000
npm run build    # Production build — must pass before pushing
npm run lint     # ESLint check
git push origin main  # Triggers Vercel auto-deploy
```

---

## Platforms We're On (Tutoring Marketplaces)
| Platform | Status | Notes |
|----------|--------|-------|
| Superprof | ✅ Listed | Already active |
| Preply | 🔲 Todo | Top priority — USA/UK/AU reach |
| TutorOcean | 🔲 Todo | Has abacus category |
| Classgap | 🔲 Todo | UK/Europe |
| TeacherOn | 🔲 Todo | Global, free |
| UrbanPro | 🔲 Todo | Indian diaspora |
| Fiverr | 🔲 Todo | Low competition niche |
| Wyzant | ❌ Ineligible | US residency + SSN required |
| Tutor.com | ❌ Ineligible | US only |
| Varsity Tutors | ❌ Ineligible | US only |

---

## Logo
- All pages use `public/images/logo3_transparent.png` (white background removed)
- Old logo backed up as `public/images/logo-old-backup.png`
- Favicons regenerated from new logo (Apr 2026)

---

## What NOT to Do
- Do not modify `src/contexts/CurrencyContext.tsx` without understanding the full auto-detection logic
- Do not add new pages without updating `src/app/sitemap.ts`
- Do not use green colours (`#556B2F` or similar) — replaced with brown palette
- Do not commit `*.json` credential files (gitignored)
- Do not push without a passing `npm run build`
- Do not use `href="#"` for footer/nav links — always use real routes
- Do not add emojis to website pages
- Do not reference Jaipur or UCMAS on the public website
