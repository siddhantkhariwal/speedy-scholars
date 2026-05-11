# KG-1 Book A — Book Notes

The very first Speedy Scholars workbook. 35 pages (cover + 34 content pages),
landscape A4. Reference: UCMAS KG-1 Book A (`public/KG-1 BOOK A Page (1-25).pdf` +
`public/KG-1 book-A (26-34).pdf`).

Generator: `generate.py` in this folder. Universal rules in
`../_shared/BOOK_DESIGN_GUIDE.md`.

---

## Curriculum Spine (page → topic)

| Page | Topic | Notes |
|------|-------|-------|
| Cover | Title, Student Info, mascots | Name / Level / Date |
| 1 | Description of the Abacus | 6 cards: Frame, Beam, Rod, Upper Bead, Lower Bead, Complete |
| 2 | Write the Value of Beads | 10 abacus cards 1–9 + "set these numbers" |
| 3 | Understand Numbers 1–5 | Abacus / Hand / Dots / Number / Trace / Trace / Practice |
| 4 | Understand Numbers 6–10 | Same 7-column layout |
| 5 | Hidden Numbers Puzzle | Replaces UCMAS truck — scattered numbers + answer boxes |
| 6 | Count and Write | 6 cards 3×2, objects + abacus |
| 7 | Count and Write | 6 cards 3×2, different object set |
| 8 | Match the Following | Number ↔ Dots ↔ Abacus |
| 9 | Match the Following | Continued |
| 10 | Direct Add/Sub | Tables, ±1 through ±2 |
| 11 | Direct Add/Sub | Tables, ±1 through ±4 |
| 12 | Visual Add/Sub | 6 cards 3×2 with both groups + operator |
| 13 | Direct Add/Sub | +5 combinations |
| 14 | Visual Add/Sub | +5 visual |
| 15 | Direct Add/Sub | +6, +7, +8 |
| 16 | Direct Add/Sub | Mixed +6 to +8 |
| 17 | Direct Add/Sub | -1 to -5 |
| 18 | Visual Add/Sub | Subtraction visuals (red X overlay) |
| 19 | Direct Add/Sub | -6 |
| 20 | Direct Add/Sub | -7 |
| 21 | Direct Add/Sub | -8 |
| 22 | Direct Add/Sub | -9 |
| 23 | Composition of 5 | Apple splits + number bond + apple tree + fill-ins |
| 24 | Composition +4 calc | Tables only |
| 25 | Composition +4 calc | Continued |
| 26 | Direct Add/Sub Revision | Mixed |
| 27 | Composition +3 calc | |
| 28 | Direct Add/Sub Revision | |
| 29 | Count and Write (revision) | Bigger objects (22px) |
| 30 | Composition +2 calc | |
| 31 | Revision | Mixed all topics |
| 32 | Composition +1 calc | |
| 33 | Big Revision | Wider 10-col tables |
| 34 | Train Revision | "Speedy Scholars Express", 4 carriages with answer wheels |

---

## Page-Specific Decisions

### Pages 3–4 (Understand Numbers)
- 7-column table: Abacus | Hand | Dots | Number | Trace | Trace | Practice
- Column widths must be **balanced**: 30/30/28/28/28/28mm + remainder for Practice
- Dots column needs 28mm minimum (20mm caused overflow into Hand column)
- Use `draw_dotted_number()` for tracing columns
- Use `draw_crosshair_box()` for practice boxes (+ guides inside)
- Hand illustrations: `draw_hand(c, x, y, size, fingers_up)` — show 5+n for 6–10

### Page 5 (Hidden Numbers)
- **Do NOT** use a truck illustration — UCMAS does, but it's too rigid for our brand
- Use a **dense overlapping number puzzle** in a bordered area
- Numbers 0–9 each appear 3× at varying sizes (22–55pt), rotations (-45 to +45), colors
- Some colors close to background (harder to find) for challenge
- Answer boxes: 10 boxes in a row below the puzzle

### Pages 6–7 (Count and Write)
- 6 cards in 3×2 grid
- Each card: objects + "=" + answer box + empty abacus with arrows
- For cards with 1–2 objects, scale objects 1.4× bigger
- Vary objects across the two pages:
  - p6: birds, fish, flowers, apples, stars, butterflies
  - p7: strawberries, mangos, cherries, etc.

### Pages 12, 14, 18 (Visual Add/Sub)
- 6 cards in 3×2 grid
- Warm background band (`#F0E8DA`) behind object area
- Operator: 26pt bold
- Subtraction: draw ALL objects, then overlay red X marks (2px, `#CC3333`) on the first b objects
- X mark size: `obj_s * 0.45` for proper coverage

### Page 23 (Composition of 5)
- Three sections: apple group splits (left), mascot + abacus (center), apple tree (right)
- Tree: `draw_apple_tree()` with numbered red apples
- Mascot: 38px with graduation hat, waving
- Practice exercises at bottom: "4 + ___ = 5" style

### Page 34 (Train Revision)
- Engine: 50mm wide, height dynamically calculated to fit below header
- Chimney: 15mm tall
- Smoke: clouds above chimney
- Carriages: 35mm wide, answer circles in wheels
- **Ensure engine + chimney + smoke does NOT overlap title** — calculate `max_engine_top = y - 8`

---

## Bottom Strip — Unique Problem Data

Every calculation page has a bottom strip of 4 illustrated problems showing both
groups. To prevent reuse, problem sets are keyed by page number (not `pn % N`).
See `BOTTOM_STRIP_SETS` in `generate.py`.

---

## Object-Size Decisions for This Book

| Page context | Size | Why |
|--------------|------|-----|
| Count and Write cards (p6, p7) | 28px | KG-1 readers need bold, easy-to-count objects |
| Visual add/sub cards (p12, p14, p18) | 24px | Two groups must fit with operator between |
| Bottom strip (all calc pages) | 13px max | Strip is short |
| Page 29 count-and-write | 22px | Fits 8 cards in a 4×2 grid |
| Page 23 apple splits | 14px | 4 rows × 5 apples |

---

## Iteration History (Approximate)

- v1: Wrong bead shape (diamonds), green palette, hardcoded margins → bad
- v2: Fixed bead to hexagon, switched to brown palette, but objects overflowed cards
- v3 (current): 20px padding rule, unique problem data, mascot on every page,
  bottom strip with both groups, train finale on p34

If a future change to chrome.py affects this book's visuals, regenerate and diff
against `public/Speedy-Scholars-KG1-Book-A.pdf` page-by-page.
