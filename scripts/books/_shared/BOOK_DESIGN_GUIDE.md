# Speedy Scholars — Universal Book Design Guide

These rules apply to **every** Speedy Scholars workbook (KG-1 through Higher A).
Book-specific decisions (curriculum sequence, page-by-page layout, problem-data
ranges, illustration choices) live in each book's own `NOTES.md`.

If a rule applies to *only one* book, it does **not** belong here — move it.

---

## Tech Stack

- **Generator:** Python + ReportLab (`reportlab` library)
- **Drawing primitives:** `_shared/illustrations.py`
- **Brand page furniture:** `_shared/chrome.py` (palette, geometry, header, footer, mascot, calc table)
- **Image processing:** Pillow (PIL), PyMuPDF for review
- **Format:** Landscape A4 (841.89 x 595.28 pts)
- **Output:** one PDF per book in `public/`

### Folder structure

```
scripts/books/
  _shared/
    chrome.py              # brand page furniture — edit affects every book
    illustrations.py       # drawing primitives — additive, don't break existing
    BOOK_DESIGN_GUIDE.md   # this file
  <book_id>/
    generate.py            # the book — runs standalone
    NOTES.md               # this book's decisions
```

Each book is launched with `python3 scripts/books/<book_id>/generate.py`.
Output goes to `public/Speedy-Scholars-<book-name>.pdf`.

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

`LEAF_GREEN` in illustrations.py is `#A0875A` (warm brown), NOT green —
the name is a historical artifact, the colour is correct.

---

## Page Layout Standards

### Landscape A4
- Page size: 841.89 x 595.28 points (defined in chrome.py as `W, H`)
- Margins: 18mm all sides (`MARGIN`)
- Content width: `CW = W - 2*MARGIN`
- Content height: `CH = H - 2*MARGIN`

### Header (every page) — `draw_hdr(c, title, sub=None)`
- Title: Helvetica-Bold 15pt, darker brown
- Subtitle: Helvetica 9pt, brown (optional)
- Gold line separator below (1.2pt)
- Logo: 28x14mm top-right
- Returns the y-cursor below the header line

### Footer (every page) — `draw_footer(c, pn)`
- Gold line at 13mm from bottom
- "Speedy Scholars - <Book Name>" left, page number right
- **Graduation-hat mascot** automatically placed bottom-right (varies position per page)
- Set the book name once at top of `generate.py` via `set_book("KG-1 Book A")`

### Student Info (cover page)
- Fields: Name, **Level** (not "Class" — abacus uses levels), Date
- Dotted lines for writing

---

## Illustration Guidelines

### Object Sizes
| Context | Minimum Size | Notes |
|---------|-------------|-------|
| Count and Write cards | 28px | Objects must be clearly recognizable |
| Visual add/sub cards | 24px | Both groups visible with operator between |
| Bottom strip (calc pages) | 13px | Constrained by strip height |
| Small "count it" grids | 22px | Detail still readable |

### Object Padding from Card Borders
**Critical rule.** Objects stuck to borders or overflowing was the #1 recurring
issue across iterations.
- Left padding from card edge: **20px minimum**
- Top padding from card top: **25-28px minimum** (accounting for object height)
- Objects must never touch or cross card borders
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

### Objects That Work Best at Small Sizes
- `draw_apple` — clear at any size
- `draw_fish` — distinctive shape
- `draw_flower` — colorful and recognizable
- `draw_cherry` — works well at 14px+
- `draw_strawberry` — good detail even small

---

## Abacus Drawing

### Bead Shapes (NEVER change)
- **Upper bead:** Hexagonal (6-sided polygon) — distinctive, not diamond or capsule
- **Lower beads:** Rounded rectangles (capsule-ish)
- Both use GOLD for active, LIGHT_GOLD for inactive

### Value Mapping
```python
upper = 1 if value >= 5 else 0
lower = value - 5 if value >= 5 else value
# Special: value 10 → upper=1, lower=4 (single rod can't truly show 10)
```

### Abacus Sizing (rough guide — book-specific sizes go in each NOTES.md)
| Context | Width | Height |
|---------|-------|--------|
| Full-page reference | 80-100mm | 95mm |
| Numbers-row table | ~65% of column width | ~78% of row height |
| Practice grid cells | 20mm | 26mm (dynamic) |
| Composition exercises | 22mm | dynamic |
| Mini (inline) | 10mm | 16mm max |

---

## Mascot System

### Bead Bird Mascot
The main character is a bead-shaped bird with eyes, wings, beak, and feet.
```python
draw_bead_bird(c, x, y, size, color, facing, expression, hat, action)
```

### Parameters
- `size`: 12–38 (12 for tiny decorative, 24–38 for featured)
- `expression`: "happy", "wink", "surprised", "thinking"
- `hat`: None or "graduation" — **use graduation hat on ALL pages**
- `action`: None or "waving"
- `facing`: "left" or "right"

### Placement Rules
- **Every page** gets a graduation-hat mascot — `draw_footer()` handles this via `page_mascot()`
- Cover pages: 4 large mascots (28–32px) in corners
- Concept pages: large mascot (28–38px) acting out the concept

---

## Calculation Table — `draw_calc_table()`

Shared across every calc-heavy book. Defined in `chrome.py`.

### Standard Dimensions
- Row height: **18px**
- S.No. column width: **32px**
- Data column width: calculated from `(table_width - 32) / num_cols`
- Header font: 9pt bold white on brown
- Data font: 10pt regular
- Use **full page width** — no side panels

### Standard Layout: 3 Tables per Page
1. Table 1: 8 columns, with optional fingering exercise text above
2. Table 2: 8 columns
3. Table 3: 4 columns (fewer, wider problems)
4. **Bottom strip**: 4 illustration-based problems in horizontal cards

### Bottom Strip Rules
- Horizontal row of 4 cards at the bottom of every calc page
- Each card shows **BOTH groups**: `a objects [operator] b objects = ___`
- Object size: 13px max (constrained by strip height)
- Padding: 10px from card edges

---

## Unique Problem Data — One Rule

Every calculation page **MUST have unique problem data**. Early versions of KG-1
reused the same numbers across 20+ pages. Use a page-keyed dict for bottom-strip
data, never `pn % N`. Page-specific data ranges live in each book's NOTES.md.

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
11. **Don't use `pn % N` for bottom strip sets** — use a page-keyed dict so every page is unique
12. **Don't use `drawRightString` for fingering exercise text** — it overlaps the logo. Use `drawString(x, y+5, fing)` (left-aligned) instead
13. **Don't duplicate chrome.py code in a book script** — if you find yourself defining `draw_hdr`/`draw_footer`/palette in a book, you're doing it wrong. Edit chrome.py.

---

## Self-Review Loop Process

After generating, run this review loop:

```python
import pymupdf
doc = pymupdf.open("public/Speedy-Scholars-<book>.pdf")
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

## Books Planned

| Book | Status | Folder |
|------|--------|--------|
| KG-1 Book A | ✅ Done | `kg1_book_a/` |
| KG-1 Book B | 🔲 Next | `kg1_book_b/` |
| KG-2 Book A | 🔲 | `kg2_book_a/` |
| KG-2 Book B | 🔲 | `kg2_book_b/` |
| KG-4 Book A | 🔲 | `kg4_book_a/` |
| KG-4 Book B | 🔲 | `kg4_book_b/` |
| Elementary Book A | 🔲 | `elementary_book_a/` |
| Elementary Book B | 🔲 | `elementary_book_b/` |
| Intermediate A Book A | 🔲 | `intermediate_a_book_a/` |
| Intermediate A Book B | 🔲 | `intermediate_a_book_b/` |
| Higher A Book A | 🔲 | `higher_a_book_a/` |
| Higher A Book B | 🔲 | `higher_a_book_b/` |

For each new book:
1. Create `scripts/books/<book_id>/` folder
2. Start `generate.py` from a copy of `kg1_book_a/generate.py`
3. Change `set_book("...")` and `OUTPUT_PATH`
4. Edit page functions for this book's curriculum
5. Write `NOTES.md` documenting this book's specific decisions
6. Run the self-review loop
