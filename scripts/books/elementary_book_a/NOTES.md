# Elementary Book A — Book Notes (DRAFT — awaiting morning sign-off)

UCMAS calls this "ELEMENTARY B (3rd Level) BOOK A". For Speedy Scholars we
shorten to "Elementary Book A". **Not yet built.**

Reference: UCMAS
(`public/ucmas-books/ELEMENTARY BOOK-A(1-24) (1).pdf` +
`public/ucmas-books/ELEMENTARY -B BOOK-A (25-42) (1).pdf`).
Total content = 24 + 18 = **42 content pages** (cover + 42 = 43 PDF pages).

---

## What This Book Teaches

Step up from KG-4. Three structural changes:

1. **6-row calc tables** instead of 3-row. Each column has 6 operations
   (start + 5 operations) and an ANS row at the bottom. The student processes
   a 6-step chain of additions/subtractions per problem.
2. **Larger numbers** — both 2-digit and 3-digit, including 4-line vertical
   sums of 3-digit numbers.
3. **Multiplication is featured** — multiple pages (×2 through ×9), each
   with visual illustrations (e.g., balloons grouped for ×2, ×3 etc.)

Time limits appear on each page ("Time Limit: 10 Mins" header), signaling the
shift to performance / competition prep.

---

## Page Spine (proposed, 42 content + cover = 43 PDF pages)

| Pages | Topic |
|-------|-------|
| Cover | "Elementary Book A" |
| 1–10 | Abacus Calculation (20 col × 6 row, time-limited) |
| 11 | Mental Calculation (20 col × 6 row) |
| 12–18 | Abacus Calculation + Mental Calculation alternating |
| 19 | Multiplication × 2 with balloon visuals |
| 20–25 | Abacus + Mental Calculation continued |
| 26 | Multiplication × 3 visuals |
| 27–32 | Abacus + Mental Calculation |
| 33 | Multiplication × 4 |
| 34 | Multiplication × 5 |
| 35 | Multiplication with mixed visuals |
| 36–41 | Final calc + assessment sequences |
| 42 | Comprehensive final assessment |

---

## Build Plan

New page types needed beyond what we have:
- `page_calc_grid_6row` — 6-row table version (KG-4's was 3-row)
- `page_calc_3digit` — handles 3-digit numbers (column widths need to adjust)
- `page_multiplication_visual` — multiplication table card + balloon/object
  visual showing repeated addition (e.g., 4 groups of 3 balloons)
- `page_assessment_final` — multi-section grand finale

Reuse from existing: `page_cover`, `gen_calc_data` (extend to 3-digit mode),
chrome.

Estimated build time post-signoff: 60-90 min (denser content, more new
page types).

## Open Questions

- **Naming**: I'm calling it "Elementary Book A" — UCMAS calls it "Elementary B
  Book A" (3rd level). Do you prefer the longer UCMAS name? Or even rename
  the level itself?
- **Time-limit headers**: UCMAS shows "Time Limit: 10 Mins" on each page.
  Keep that?
- **Multiplication visuals**: UCMAS uses kid drawings (balloons, animals).
  Our brand version → use our object library (apples grouped, mascots
  grouped). OK?
- **42 pages vs flexed** — the page count is big. If we hit visual issues at
  some slot, can I drop the page count by 1-2 to recover layout?

After you sign off, I'll build.
