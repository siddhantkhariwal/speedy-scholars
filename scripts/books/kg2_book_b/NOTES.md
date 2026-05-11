# KG-2 Book B — Book Notes

Fourth Speedy Scholars workbook. Sequel to KG-2 Book A. 39 pages (cover + 38),
landscape A4. **Larger than other KG books** — UCMAS reference is 38 content
pages (24 + 14).

Reference: UCMAS KG-2 Book B
(`public/ucmas-books/KG 2 BOOK B (1-24).pdf` + `KG 2 BOOK B(25-38).pdf`).

---

## What This Book Teaches

The **subtraction counterpart** of KG-2 Book A. Two themes:

1. **Decomposition of 10** (p1-21). Teen-minus-single-digit subtraction using
   `−n = −10 + (10−n)`:
   - `−9 = −10 + 1`
   - `−8 = −10 + 2`
   - `−7 = −10 + 3`
   - `−6 = −10 + 4`
   - `−5 = −10 + 5`
   - `−4 = −10 + 6`

2. **Big/Small Friends Decomposition** (p22-34). Two-step subtractions where
   single-rod borrow isn't enough:
   - `−9 = −10 + 5 − 4`
   - `−8 = −10 + 5 − 3`
   - `−7 = −10 + 5 − 2`
   - `−6 = −10 + 5 − 1`

3. **Mental Calculation + Two-Digit Carry Intro** (p35-38). Visualized
   subtraction, then a peek into carry-forward for two-digit addition
   (29+61=90, 47+53=100) and a comprehensive final assessment.

---

## Page Spine (mirrors UCMAS slot-for-slot, 38 content + cover)

| Page | UCMAS Topic | Plan |
|------|-------------|------|
| Cover | — | "KG-2 Book B" / Student Info |
| 1 | Combination of Big & Small Friends (visual) | 2 cards: `13−8 : 13−10+2 = ( )` + `14−9 : 14−10+1 = ( )` with object groups |
| 2 | Pyramid grid of subtractions | Tall staircase: row n = subtractions by n, e.g. row 1=10-1; row 2=10-2 11-2; ... row 9 = 10-9, 11-9, ..., 18-9 |
| 3 | Calc Decomp of 10 (−9) | Formula `−9 = −10 + 1`, fingering 10−9, 11−9, 12−9 + mini diag |
| 4 | Revision | 8/8/4 tables |
| 5 | Calc Decomp of 10 (−8) | Formula `−8 = −10 + 2`, fingering 11−8, 15−8, 16−8 + mini diag |
| 6 | Revision | 8/8/4 |
| 7 | Revision | 8/8/4 |
| 8 | Calc Decomp of 10 (−7) | Formula `−7 = −10 + 3`, fingering 11−7, 15−7, 16−7 + mini diag |
| 9 | Visual cards (−6 with mascots) | 2 cards |
| 10 | Visual cards (10−6, 15−6) | 2 cards |
| 11 | Calc Decomp of 10 (−6) | Formula `−6 = −10 + 4`, fingering 10−6, 15−6 + mini diag |
| 12 | Revision | 8/8/4 |
| 13 | Visual cards (13−5, 11−4, 12−3) | 3 cards |
| 14 | Calc Decomp of 10 (−5) | Formula `−5 = −10 + 5`, fingering 10−5, 11−5, 12−5 + mini diag |
| 15 | Revision | wide |
| 16 | Revision | 8/8/4 |
| 17 | Revision | 8/8/4 |
| 18 | Calc Decomp of 10 (−4) | Formula `−4 = −10 + 6`, fingering 10−4, 11−4, 12−4 + mini diag |
| 19 | Revision | 8/8/4 |
| 20 | Revision | wide |
| 21 | Revision | wide |
| 22 | Special interest (animals/houses or similar) | Match-mascots-to-numbered-houses puzzle |
| 23 | Revision | wide |
| 24 | Special interest (jigsaw or count) | A jigsaw-style or count-and-write |
| 25 | Calc Combination of 10 (−9 with two-step) | Formula `−9 = −10 + 5 − 4`, fingering 14−9 + mini diag |
| 26 | Revision | 8/8/4 |
| 27 | Calc Combination of 10 (−8 two-step) | Formula `−8 = −10 + 5 − 3` + mini diag |
| 28 | Revision | 8/8/4 |
| 29 | Calc Combination of 10 (−7 two-step) | Formula `−7 = −10 + 5 − 2` + mini diag |
| 30 | Calc Combination of 10 (−7 alt) | Continuation page same formula |
| 31 | Revision | 8/8/4 |
| 32 | Calc Combination of 10 (−6 two-step) | Formula `−6 = −10 + 5 − 1` + mini diag |
| 33 | Revision | 8/8/4 |
| 34 | Revision | 8/8/4 |
| 35 | Mental Calculation | wide 10-col blocks (no listening sidebar this time) |
| 36 | Carry-forward intro | Featured mascot with thought bubble: "Now let's learn double digits". Show 29+61=90 and 47+53=100 with paired abacuses |
| 37 | Mental Calculation A/B | with listening sidebar |
| 38 | FINAL ASSESSMENT — Sections B/C/D | Section B: Abacus Calc 8/8/4 / Section C: Mental Calc / Section D: Fill in Combination & Decomposition number bonds |

---

## Notes on Implementation

- Reuses `page_calc`, `page_mental` from KG-2 Book A pattern (the same component
  patterns, not yet promoted to `_shared/`).
- New page types: `page_pyramid`, `page_visual_cards_sub`, `page_carry_intro`,
  `page_assessment`.

## Overnight Authorization

All page-specific design decisions made for v1.
