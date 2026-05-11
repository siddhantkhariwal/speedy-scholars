# KG-4 Book B — Book Notes (DRAFT — awaiting morning sign-off)

Sequel to KG-4 Book A. **Not yet built** — generator pending sign-off on spine.

Reference: UCMAS KG-4 Book B (`public/ucmas-books/KG-4 Book B.pdf`).
Reference is **36 content pages** (single PDF, unsplit).

---

## What This Book Teaches

Continuation of calculation drilling started in KG-4 Book A. Same format
(Mental Calc + Abacus Calc grids with 2-digit numbers), more practice volume,
and likely deeper multiplication coverage (×2, ×4, ×5+).

The reference is structurally near-identical to KG-4 Book A — 20-column
3-row grids dominate, with occasional 4-line addition columns and
multiplication tables.

---

## Page Spine (proposed, 36 content + cover = 37 PDF pages)

| Pages | Topic |
|-------|-------|
| Cover | "KG-4 Book B" |
| 1–8 | Mental Calculation (20 col × 3 row) |
| 9–14 | Abacus Calculation (20 col × 3 row) |
| 15 | Multiplication × 2 |
| 16–22 | Abacus Calculation with bottom 4-line sums (some pages) |
| 23 | Multiplication × 4 |
| 24–28 | Mental Calculation |
| 29 | Multiplication × 5 |
| 30–35 | Mental + Abacus Calculation mixed |
| 36 | Final Assessment |

---

## Build Plan

Reuse 90% of KG-4 Book A's `generate.py`:
- `page_cover` (change title to "KG-4 BOOK B")
- `page_calc_grid` (unchanged)
- `page_multiplication` (unchanged, different factor)
- `gen_calc_data` (different page-seed offset so problems are fresh)
- Different `main()` page sequence

Estimated build time post-signoff: 20-30 min.

## Open Questions

- **Confirm sequence and multiplication factors** (I guessed ×2, ×4, ×5 — UCMAS
  may have different mix; need to inspect more carefully).
- **Add an interest page?** UCMAS KG-4 B may have a non-calc page I haven't
  spotted at low DPI; let me know after you skim the reference.
