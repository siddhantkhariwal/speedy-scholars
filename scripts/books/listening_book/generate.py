#!/usr/bin/env python3
"""
Speedy Scholars — Listening Book Workbook Generator
PORTRAIT A4 (only book in the curriculum not landscape).
50 pages (cover + 49). Teacher reads aloud, student listens and writes
only the answers in the answer grid.

Per-page format:
- Section A: 6 cols × 5 deep
- Section B: 5 cols × 10 deep
- Section C: 4 cols × 15 deep
- Section D: 3 cols × 20 deep
- 18 problems total per page
- 10 answer cells: A, B, C, D, AB, BC, CD, ABC, BCD, ABCD
"""

import os, sys, math, random
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

_SHARED = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared"))
sys.path.insert(0, _SHARED)
from illustrations import *

# Portrait A4 dimensions (210 × 297 mm)
W, H = A4
MARGIN = 14 * mm
CW = W - 2 * MARGIN
CH = H - 2 * MARGIN

# Brand colors (re-imported)
from chrome import LOGO_PATH, PUBLIC_DIR, TF, TH

OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Listening-Book.pdf")
BOOK_SEED = 11000


# ─── PORTRAIT CHROME (header/footer adapted for portrait) ────────────────
def bg(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def draw_hdr_portrait(c, title, time_limit, sub=None):
    y = H - 14 * mm
    try:
        c.drawImage(LOGO_PATH, W - MARGIN - 26 * mm, y - 6 * mm, width=24 * mm,
                    height=12 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y, title)
    if sub:
        c.setFont("Helvetica", 8); c.setFillColor(BROWN)
        c.drawString(MARGIN, y - 11, sub)
    # ORAL / WRITTEN tag top-right (above the logo)
    tag_w = 38 * mm; tag_h = 14
    tag_x = W - MARGIN - 28 * mm - tag_w - 4
    tag_y = y - 2
    c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
    c.roundRect(tag_x, tag_y, tag_w, tag_h, 3, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 8); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(tag_x + tag_w / 2, tag_y + 3, f"ORAL / WRITTEN  •  {time_limit}")
    # Gold underline
    c.setStrokeColor(GOLD); c.setLineWidth(1)
    ly = y - (14 if sub else 4)
    c.line(MARGIN, ly, W - MARGIN - 30 * mm, ly)
    return ly - 4


def draw_footer_portrait(c, pn):
    c.saveState()
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.4)
    c.line(MARGIN, 10 * mm, W - MARGIN, 10 * mm)
    c.setFont("Helvetica", 6.5); c.setFillColor(BROWN)
    c.drawString(MARGIN, 7 * mm, "Speedy Scholars - Listening Book")
    c.drawRightString(W - MARGIN, 7 * mm, str(pn))
    c.restoreState()


# ─── DATA GENERATION ──────────────────────────────────────────────────────
def gen_problem(seed, depth, lo, hi, allow_negative=True, signed_prob=0.4):
    """Generate one problem: a list of `depth` signed numbers."""
    random.seed(seed)
    nums = []
    running = 0
    for i in range(depth):
        if i == 0:
            # Start with a positive number
            v = random.randint(lo, hi)
            nums.append(v)
            running = v
        else:
            # Pick a number with a sign that keeps running >= 0
            attempts = 0
            while True:
                sign = random.choice([1, -1]) if (allow_negative and random.random() < signed_prob) else 1
                mag = random.randint(lo, hi)
                v = sign * mag
                if running + v >= 0:
                    nums.append(v)
                    running += v
                    break
                attempts += 1
                if attempts > 20:
                    # Force a positive number
                    nums.append(mag); running += mag
                    break
    return nums, running


def gen_section(pn, section_letter, num_cols, depth, lo, hi, allow_negative=True):
    """Generate `num_cols` problems for a section. Returns list of (numbers, answer)."""
    section_seed = (pn * 31 + ord(section_letter) * 7 + BOOK_SEED)
    return [gen_problem(section_seed + col * 17, depth, lo, hi,
                        allow_negative=allow_negative)
            for col in range(num_cols)]


# ─── SECTION TABLE DRAWING ────────────────────────────────────────────────
def draw_section(c, x, y, label, columns_data, depth, total_w, total_h):
    """Draw one section (A/B/C/D) with `len(columns_data)` columns of `depth` rows."""
    num_cols = len(columns_data)
    # Left label column + column headers
    label_w = 14
    col_w = (total_w - label_w) / num_cols
    row_h = total_h / (depth + 1)  # +1 for header row
    hf = 6

    # Header row (column numbers)
    hy = y - row_h
    c.setFillColor(BROWN); c.rect(x, hy, label_w, row_h, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + label_w / 2, hy + row_h / 2 - 2, label)
    for ci in range(num_cols):
        cx = x + label_w + ci * col_w
        c.setFillColor(BROWN); c.rect(cx, hy, col_w, row_h, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + col_w / 2, hy + row_h / 2 - 2, str(ci + 1))

    # Data rows
    for ri in range(depth):
        ry = hy - (ri + 1) * row_h
        # Row number label
        c.setFillColor(LIGHT_GOLD if ri % 2 == 0 else TF)
        c.rect(x, ry, label_w, row_h, stroke=0, fill=1)
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.2)
        c.rect(x, ry, label_w, row_h, stroke=1, fill=0)
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica", hf - 1)
        c.drawCentredString(x + label_w / 2, ry + row_h / 2 - 2, str(ri + 1))

        for ci, (nums, _ans) in enumerate(columns_data):
            cx = x + label_w + ci * col_w
            c.setFillColor(TF if ri % 2 == 0 else LIGHT_GOLD)
            c.rect(cx, ry, col_w, row_h, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.2)
            c.rect(cx, ry, col_w, row_h, stroke=1, fill=0)
            if ri < len(nums):
                v = nums[ri]
                c.setFillColor(DARKER_BROWN)
                c.setFont("Helvetica", min(8, row_h * 0.5))
                c.drawCentredString(cx + col_w / 2, ry + row_h / 2 - 2.5, str(v))

    return y - total_h


# ─── ANSWER GRID (10 cells) ───────────────────────────────────────────────
def draw_answer_grid(c, x, y, total_w, total_h):
    """Draw the 10-cell answer grid: A B C D AB BC CD ABC BCD ABCD."""
    labels = ["A", "B", "C", "D", "AB", "BC", "CD", "ABC", "BCD", "ABCD"]
    cell_w = total_w / 10
    cell_h = total_h * 0.5
    label_h = total_h * 0.3

    # Labels row
    for i, lab in enumerate(labels):
        cx = x + i * cell_w
        c.setFillColor(BROWN); c.rect(cx, y - label_h, cell_w, label_h, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(cx + cell_w / 2, y - label_h + 3, lab)

    # Answer cells (empty for student)
    for i in range(10):
        cx = x + i * cell_w
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
        c.rect(cx, y - label_h - cell_h, cell_w, cell_h, stroke=1, fill=1)


# ─── ONE FULL PAGE ────────────────────────────────────────────────────────
def page_listen(c, pn, time_limit, lo, hi, allow_negative=True):
    bg(c)
    y = draw_hdr_portrait(c, "Listening Exercise", time_limit,
                          sub="Teacher reads each column • Student listens and writes the answer")
    draw_footer_portrait(c, pn)

    # Generate data for sections A, B, C, D
    sec_a = gen_section(pn, "A", 6, 5, lo, hi, allow_negative=allow_negative)
    sec_b = gen_section(pn, "B", 5, 10, lo, hi, allow_negative=allow_negative)
    sec_c = gen_section(pn, "C", 4, 15, lo, hi, allow_negative=allow_negative)
    sec_d = gen_section(pn, "D", 3, 20, lo, hi, allow_negative=allow_negative)

    # Layout heights (total height ~ y - 30mm available)
    avail = y - 18 * mm  # leave 18mm for answer grid
    # Distribute heights proportionally to depths: 5+10+15+20 = 50
    # Plus 1 header row per section = 4 header rows extra
    total_units = 5 + 10 + 15 + 20 + 4
    unit_h = avail / total_units
    section_heights = [(5 + 1) * unit_h, (10 + 1) * unit_h,
                        (15 + 1) * unit_h, (20 + 1) * unit_h]

    # Draw sections
    cur_y = y
    for sec_label, sec_data, depth, sec_h in [
            ("A", sec_a, 5, section_heights[0]),
            ("B", sec_b, 10, section_heights[1]),
            ("C", sec_c, 15, section_heights[2]),
            ("D", sec_d, 20, section_heights[3])]:
        cur_y = draw_section(c, MARGIN, cur_y, sec_label, sec_data, depth,
                             CW, sec_h)
        cur_y -= 2  # small gap

    # Answer grid at bottom
    ans_y = 14 * mm + 16
    draw_answer_grid(c, MARGIN, ans_y, CW, 14)


# ─── COVER ────────────────────────────────────────────────────────────────
def page_cover(c):
    bg(c)
    c.setStrokeColor(GOLD); c.setLineWidth(3)
    c.roundRect(10 * mm, 10 * mm, W - 20 * mm, H - 20 * mm, 8, stroke=1, fill=0)
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(1)
    c.roundRect(13 * mm, 13 * mm, W - 26 * mm, H - 26 * mm, 6, stroke=1, fill=0)
    draw_bead_bird(c, 30 * mm, H - 30 * mm, 28, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - 30 * mm, H - 30 * mm, 26, BROWN, "left", "wink", hat="graduation")
    draw_bead_bird(c, 30 * mm, 40 * mm, 24, LIGHT_GOLD, "right", "surprised")
    draw_bead_bird(c, W - 30 * mm, 40 * mm, 26, GOLD, "left", "happy", action="waving")
    for i in range(12):
        random.seed(i + 1800)
        draw_star(c, random.uniform(20 * mm, W - 20 * mm),
                  random.uniform(20 * mm, H - 20 * mm),
                  3 + random.random() * 3, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 80 * mm) / 2, H - 95 * mm, width=80 * mm,
                    height=45 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 32); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 125 * mm, "LISTENING BOOK")
    c.setFont("Helvetica", 13); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 138 * mm, "Oral & Written Exercises")
    c.setFont("Helvetica-Oblique", 10); c.setFillColor(BROWN)
    c.drawCentredString(W / 2, H - 152 * mm,
                        "Teacher reads • Student listens • Student writes")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 65 * mm, H - 162 * mm, W / 2 + 65 * mm, H - 162 * mm)

    iw = 140 * mm; iy = H - 230 * mm
    c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1)
    c.roundRect((W - iw) / 2, iy, iw, 50 * mm, 5, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, iy + 42 * mm, "Student Information")
    for i, f in enumerate(["Name:", "Level:", "Date:"]):
        fy = iy + 30 * mm - i * 12 * mm
        c.setFont("Helvetica-Bold", 10); c.setFillColor(BROWN)
        c.drawString((W - iw) / 2 + 8, fy, f)
        c.setStrokeColor(LIGHT_GOLD); c.setDash(1, 2)
        c.line((W - iw) / 2 + 30 * mm, fy - 2, (W + iw) / 2 - 8, fy - 2); c.setDash()
    c.setFont("Helvetica", 9); c.setFillColor(BROWN)
    c.drawCentredString(W / 2, 18 * mm, "www.speedyscholars.com")


# ─── MAIN ────────────────────────────────────────────────────────────────
def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=A4)  # PORTRAIT
    page_cover(c); c.showPage()

    # p1-10: Beginner — single digit, mostly +
    for pn in range(1, 11):
        page_listen(c, pn, "8 Mins", lo=1, hi=9, allow_negative=False)
        c.showPage()

    # p11-20: Intermediate — single-digit mixed signs
    for pn in range(11, 21):
        page_listen(c, pn, "6 Mins", lo=1, hi=9, allow_negative=True)
        c.showPage()

    # p21-30: Advanced — 2-digit
    for pn in range(21, 31):
        page_listen(c, pn, "5 Mins", lo=10, hi=99, allow_negative=True)
        c.showPage()

    # p31-40: Speed — 2-digit, tighter time
    for pn in range(31, 41):
        page_listen(c, pn, "4 Mins", lo=10, hi=99, allow_negative=True)
        c.showPage()

    # p41-48: Expert — 3-digit
    for pn in range(41, 49):
        page_listen(c, pn, "3 Mins", lo=100, hi=999, allow_negative=True)
        c.showPage()

    # p49: Final mastery (mixed difficulties — use 2-digit medium time)
    page_listen(c, 49, "5 Mins", lo=10, hi=99, allow_negative=True)
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 50 (cover + 49) — PORTRAIT A4")


if __name__ == "__main__":
    main()
