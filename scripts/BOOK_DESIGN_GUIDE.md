# Speedy Scholars — Abacus Book Design Guide

Learnings from designing KG-1 Book A across 10+ iterations. Use this for all future books (KG-1 Book B, KG-2, Level 1, etc.).

---

## Tech Stack

- **Generator:** Python + ReportLab (`reportlab` library)
- **Image processing:** Pillow (PIL) for logo transparency, PyMuPDF for PDF review
- **Format:** Landscape A4 (841.89 x 595.28 pts)
- **Output:** Print-ready PDF in `public/` directory

### Key Files
```
scripts/
  illustrations.py         # All drawing functions: mascots, objects, abacus, hands, decorations
  generate_kg1_book.py     # Page-by-page generator for KG-1 Book A
  BOOK_DESIGN_GUIDE.md     # This file — design learnings for future books
```

---

## Brand Rules (Never Change)

| Element | Value |
|---------|-------|
| Primary brown | #8B6F47 |
| Dark brown | #6B5335 |
| Darker brown | #5A4830 |
| Gold accent | #C9A86C |
| Light gold | #D4B896 |
| Cream bg | #F5EDE3 |
| Warm white | #FFF8F0 |
| **No green** | Old UCMAS uses green — we use brown/gold |
| **No emojis** | Not in books or website |
| Font | Helvetica (ReportLab default) |
| Logo | `public/images/logo3_transparent.png` (white bg removed) |

---

## Page Layout Standards

### Landscape A4
- Page size: 841.89 x 595.28 points
- Margins: 18mm all sides
- Content width: ~285mm
- Content height: ~173mm (between header and footer)

### Header (every page)
- Title: Helvetica-Bold 15pt, darker brown
- Subtitle: Helvetica 9pt, brown
- Gold line separator below
- Logo: 28x14mm top-right
- Fingering exercise text: right-aligned above first table

### Footer (every page)
- Gold line at 13mm from bottom
- "Speedy Scholars - KG-1 Book A" left, page number right
- **Graduation-hat mascot** automatically placed bottom-right (varies position per page)

### Student Info (cover page)
- Fields: Name, **Level** (not "Class" — abacus uses levels), Date
- Dotted lines for writing

---

## Illustration Guidelines

### Object Sizes (learned through iteration)
| Context | Minimum Size | Notes |
|---------|-------------|-------|
| Count and Write cards | 28px | Objects must be clearly recognizable |
| Visual add/sub cards | 24px | Both groups visible with operator between |
| Bottom strip (calc pages) | 13px | Constrained by strip height |
| Page 29 count & write | 22px | Fruits/objects need detail |

### Object Padding from Card Borders
**Critical lesson:** Objects stuck to borders or overflowing was the #1 recurring issue.
- Left padding from card edge: **20px minimum**
- Top padding from card top: **25-28px minimum** (accounting for object height)
- Objects should never touch or cross card borders
- Use `bx + 20 + (j % cols) * spacing` pattern

### Available Object Drawing Functions
```python
draw_apple(c, x, y, size)        # Red apple with leaf
draw_fish(c, x, y, size, color)  # Fish with tail and eye
draw_flower(c, x, y, size)       # 5-petal flower with stem
draw_bird(c, x, y, size, color)  # Simple bird
draw_bone(c, x, y, size, angle)  # Cartoon bone
draw_butterfly(c, x, y, size)    # 4-wing butterfly
draw_strawberry(c, x, y, size)   # Red strawberry with seeds
draw_cherry(c, x, y, size)       # Two cherries on stem
draw_mango(c, x, y, size)        # Kidney-shaped mango
draw_banana(c, x, y, size)       # Curved banana — renders poorly at <16px, avoid in small spaces
draw_pineapple(c, x, y, size)    # Pineapple — complex, avoid in small spaces
draw_star(c, x, y, size, color)  # 5-pointed star
```

### Objects to AVOID in Small Spaces
- `draw_banana` — barely visible below 16px
- `draw_pineapple` — looks like a blob below 18px
- `draw_bone` — knobs need 18px+ to be recognizable

### Objects That Work Best
- `draw_apple` — clear at any size
- `draw_fish` — distinctive shape
- `draw_flower` — colorful and recognizable
- `draw_cherry` — works well at 14px+
- `draw_strawberry` — good detail even small

---

## Abacus Drawing

### Bead Shapes
- **Upper bead:** Hexagonal (6-sided polygon) — distinctive, not diamond or capsule
- **Lower beads:** Rounded rectangles (capsule-ish)
- Both use GOLD for active, LIGHT_GOLD for inactive

### Abacus Sizing
| Context | Width | Height |
|---------|-------|--------|
| Full-page reference | 80-100mm | 95mm |
| Number understanding (pages 3-4) | 65% of column width | 78% of row height |
| Practice (page 2) | 20mm | 26mm (dynamic) |
| Composition of 5 | 22mm | dynamic |
| Mini (page 1 Complete card) | 10mm | 16mm max |

### Value Mapping
```python
upper = 1 if value >= 5 else 0
lower = value - 5 if value >= 5 else value
# Special: value 10 → upper=1, lower=4 (single rod can't truly show 10)
```

---

## Mascot System

### Bead Bird Mascot
The main character is a bead-shaped bird with eyes, wings, beak, and feet.
```python
draw_bead_bird(c, x, y, size, color, facing, expression, hat, action)
```

### Parameters
- `size`: 12-38 (12 for tiny decorative, 24-38 for featured)
- `expression`: "happy", "wink", "surprised", "thinking"
- `hat`: None or "graduation" — **use graduation hat on ALL pages**
- `action`: None or "waving"
- `facing`: "left" or "right"

### Placement Rules
- **Every page** gets a graduation-hat mascot via `draw_footer()` → `page_mascot()`
- Cover page: 4 large mascots (28-32px) in corners
- Page 1: mascots near each abacus card (13-14px)
- Composition pages: large mascot (28-38px) acting out the concept
- Train page: mascot as driver

---

## Calculation Table Design

### Table Dimensions
- Row height: **18px** (increased from 13.5 in early versions)
- S.No. column width: 32px
- Data column width: calculated from `(table_width - 32) / num_cols`
- Header font: 9pt bold white on brown
- Data font: 10pt regular
- Use **full page width** — no side panels

### Standard Layout: 3 Tables per Page
1. Table 1: 8 columns, with fingering exercise text above
2. Table 2: 8 columns
3. Table 3: 4 columns (fewer problems)
4. **Bottom strip**: 4 illustration-based problems in horizontal cards

### Bottom Strip Rules
- Horizontal row of 4 cards at the bottom of every calc page
- Each card shows **BOTH groups**: `a objects [operator] b objects = ___`
- Object size: 13px max (constrained by strip height)
- Padding: 10px from card edges
- Different problem sets rotate across pages (6 sets cycling by page number)
- **MUST show both a and b groups** — early versions only showed group a

### Unique Problem Data
Every calculation page **MUST have unique problem data**. Early versions reused the same data on 20+ pages. Each page should match its curriculum stage:
- Pages 10-11: Basic ±1 through ±4
- Page 13: +5 combinations
- Page 15: +6, +7, +8
- Pages 19-22: -6 through -9
- Pages 25, 27, 30, 32: Composition of 5 (+4, +3, +2, +1)
- Revision pages: mixed review

---

## Page-Specific Learnings

### Pages 3-4 (Understand Numbers)
- Column widths must be **balanced**: 30/30/28/28/28/28mm + remainder for Practice
- Dots column needs 28mm minimum (20mm caused overflow into Hand column)
- Use `draw_dotted_number()` for tracing columns
- Use `draw_crosshair_box()` for practice boxes (+ guides inside)
- Hand illustrations: `draw_hand(c, x, y, size, fingers_up)` — show 5+n for 6-10

### Page 5 (Hidden Numbers)
- **DO NOT** use a truck illustration — it's too rigid
- Use a **dense overlapping number puzzle** in a bordered area
- Numbers 0-9 each appear 3x at varying sizes (22-55pt), rotations (-45 to +45), and colors
- Some colors close to background (harder to find) for challenge
- Answer boxes: 10 boxes in a row below the puzzle

### Pages 6-7 (Count and Write)
- 6 cards in 3x2 grid
- Each card: objects + "=" + answer box + empty abacus with arrows
- For cards with 1-2 objects, scale objects 1.4x bigger
- Use varied objects across the two pages (birds, fish, flowers, apples, stars, butterflies on p6; strawberries, mangos, cherries, etc. on p7)

### Pages 12, 14, 18 (Visual Add/Sub)
- 6 cards in 3x2 grid
- Warm background band (`#F0E8DA`) behind object area
- Operator: 26pt bold
- Subtraction: draw ALL objects, then overlay red X marks (2px, `#CC3333`) on the first b objects
- X mark size: `obj_s * 0.45` for proper coverage

### Page 23 (Composition of 5)
- Three sections: apple group splits (left), mascot (center), apple tree (right)
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

## Common Mistakes to Avoid

1. **Don't use diamond beads** — use hexagonal upper beads, rounded lower beads
2. **Don't hardcode page heights** — calculate dynamically from available space
3. **Don't reuse same problem data** across pages
4. **Don't put objects at `bx + 5`** — minimum 20px padding from card borders
5. **Don't use "Class"** — use "Level" (abacus terminology)
6. **Don't use green** — brown/gold palette only
7. **Don't forget both groups in addition/subtraction illustrations** — show a AND b objects
8. **Don't use banana/pineapple in small spaces** — they're unrecognizable below 16px
9. **Logo must use transparent version** — `logo3_transparent.png`
10. **Test every page visually** — extract as PNG and review (PyMuPDF: `page.get_pixmap(dpi=150)`)

---

## Self-Review Loop Process

After generating, run this review loop:
```python
import pymupdf
doc = pymupdf.open("output.pdf")
for i in range(len(doc)):
    doc[i].get_pixmap(dpi=150).save(f"/tmp/review/p{i:02d}.png")
```
Then check each page for:
- [ ] Objects not overflowing card borders
- [ ] No text cut off at page edges
- [ ] Bottom strip shows both object groups
- [ ] Mascot visible on every page
- [ ] Abacus beads are hexagonal (upper) and rounded (lower)
- [ ] No duplicate problem data across pages
- [ ] Logo has no white background box

---

## Future Books to Create

| Book | Level | Content |
|------|-------|---------|
| KG-1 Book B | KG-1 | Composition of 5 continued, subtraction compositions |
| KG-2 Book A | KG-2 | 2-digit numbers, larger addition/subtraction |
| KG-2 Book B | KG-2 | Advanced 2-digit, introduction to multiplication concepts |
| Level 1 Book A | Level 1 | Formal abacus calculations, speed drills |
| Level 1 Book B | Level 1 | Competition prep, timed exercises |

For each new book:
1. Copy `generate_kg1_book.py` as template
2. Reuse `illustrations.py` (shared library)
3. Update page content, problem data, and difficulty
4. Follow all guidelines in this document
5. Run the self-review loop
