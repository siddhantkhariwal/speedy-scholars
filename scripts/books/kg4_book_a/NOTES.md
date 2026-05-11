# KG-4 Book A — Book Notes

Fifth Speedy Scholars workbook. 39 pages (cover + 38), landscape A4. The
calculation-drilling book — heavily focused on Mental Calculation and
Abacus Calculation with 2-digit numbers, plus an introduction to
multiplication tables.

Reference: UCMAS KG-4 Book A
(`public/ucmas-books/KG-4 BOOK A 1-24.pdf` + `KG-4 BOOK-A (25-38).pdf`).

---

## What This Book Teaches

After KG-2 Book B introduced 2-digit carrying, KG-4 Book A drills it. Three
themes:

1. **Mental Calculation with 2-digit numbers** — bulk of the book. Each page
   is a 20-column grid where each column is a 3-step problem like `28 / +7 / −2`.
2. **Abacus Calculation with multi-row sums** — pages where the bottom half
   shows 4-line vertical additions of 2-digit numbers (e.g., `26 + 73 + 51 + 80`).
3. **Multiplication intro** — tables of ×0, ×1, ×3 etc. with the addition
   equivalent shown on the right (e.g., `3 + 3 = 3×2`).

---

## Page Spine (38 content + cover)

| Page | Topic |
|------|-------|
| Cover | "KG-4 Book A" |
| 1–11 | Mental Calculation grids (20 col × 3 row, 2-digit numbers) |
| 12 | Abacus Calculation + bottom 4-line sums |
| 13–17 | Mixed Mental/Abacus Calc |
| 18 | Multiplication ×0 and ×1 |
| 19 | Multiplication ×1 with addition equivalents |
| 20–24 | Abacus Calc + 4-line sums at bottom |
| 25–27 | Mental Calculation continued |
| 28 | Multiplication ×3 with addition equivalents |
| 29–31 | Abacus Calculation |
| 32–37 | Mental Calculation |
| 38 | Final mental-calc assessment |

---

## Page Types Built

- `page_calc_grid` — 20-col × 3-row table of 2-digit calculations
- `page_with_sums` — calc grid + 6 multi-row addition problems at bottom
- `page_multiplication` — 3 columns of ×N tables + addition equivalents

## Data Strategy

Problem data is **programmatically generated** with a deterministic seed per
page. Each cell: pick a 2-digit start (10-99), pick op2 (±1..±9 or ±2-digit),
pick op3, ensure intermediate and final results stay positive and ≤ 99.

Not every problem is independently hand-verified — this is a drilling book,
problems should be plausible and unique per page, not curated.

## Overnight Authorization

All design decisions made for v1.
