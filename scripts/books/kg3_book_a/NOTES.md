# KG-3 Book A — Book Notes

Sits between KG-2 Book B and KG-4 Book A in the curriculum. 39 pages
(cover + 38), landscape A4.

Reference: UCMAS KG-3 Book A
(`reference-pdfs/KG-3 BOOK-A(1-24).pdf` + `KG-3 BOOK-A(25-38).pdf`).

## What This Book Teaches

The **bridge** book — moves the student from single-digit (KG-2) to fluent
2-digit calculation (KG-4). Three themes:

1. **2-Digit Abacus Calculation** (3-row tables) — start with 2-digit ± 2-digit
2. **Decomposition of 5 / Composition of 10 — revisited in 2-digit context**
   (e.g., 86 + 73 needs both 2-digit work AND the −4 = +1 −5 trick on the
   ones rod)
3. **Mental Calculation** of the same tricks (eyes closed, no physical abacus)

## Page Spine (proposed, 38 content + cover)

| Pages | Topic |
|-------|-------|
| Cover | "KG-3 Book A" |
| 1–2 | Abacus Calculation: 2 Digits, 2 Rows (3-row 30-col tables) |
| 3–4 | Decomposition of 5 (−4) with 2-digit |
| 5 | Decomposition of 5 (+4) revision |
| 6–7 | Revision |
| 8 | Decomposition of 5 (−3) |
| 9–10 | Revision |
| 11 | Decomposition of 5 (−2) |
| 12 | Revision |
| 13 | Decomposition of 5 (−1) |
| 14–17 | Revision (mixed) |
| 18–22 | More 2-digit revision |
| 23 | Mental Calculation Revision (3-row + small written-eqn area at bottom) |
| 24 | Mental Calculation: Decomposition of 10 (+9) |
| 25 | Mental Calculation: Decomposition of 10 (+4) |
| 26–30 | Mental Calc continued (various compositions) |
| 31–34 | Mental Calc Revision |
| 35 | Concept: 8 = 8.2+10 (carrying intro illustrated) |
| 36–37 | Abacus Calc with 2-digit + carry |
| 38 | Final Assessment |

## Build Plan

Reuses helpers from `elementary_b_book_a` (draw_hdr_with_time, _draw_grid,
page_calc_6row) and `kg4_book_a` (gen_calc_data). Same pattern as other
calculation-drilling books but with:
- 30-col tables (10/10/10 splits) instead of 20-col
- Small "written equations" footer area on Mental Calc pages
- Time-limit headers on each page

## Decisions for v1 (overnight pattern)

- Time limits: 10 Mins for Abacus Calc, 5 Mins for Mental Calc
- 2-digit data range: 10-99
- Programmatic data generation with per-book seed offset (7000)
