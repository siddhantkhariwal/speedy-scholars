#!/usr/bin/env python3
"""
Speedy Scholars — Listening Book Workbook Generator
LANDSCAPE A4 (matches all other Speedy Scholars books).
50 pages (cover + 49). Teacher reads aloud, student listens and writes
only the answers in the answer grid.

Per-page format (4 sections side-by-side as horizontal bands):
- Section A: 6 cols × 5 deep   (taller cells, fewer rows)
- Section B: 5 cols × 10 deep
- Section C: 4 cols × 15 deep
- Section D: 3 cols × 20 deep  (shorter cells, more rows)
- 18 problems total per page
- 10 answer cells at bottom: A, B, C, D, AB, BC, CD, ABC, BCD, ABCD
"""

import os, sys, math, random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

_SHARED = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared"))
sys.path.insert(0, _SHARED)
from illustrations import *
from chrome import (W, H, MARGIN, CW, CH, TF, TH, LOGO_PATH, PUBLIC_DIR,
                     bg, instr, draw_hdr, draw_footer, page_mascot,
                     set_book)

set_book("Listening Book")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Listening-Book.pdf")
BOOK_SEED = 11000


# ─── HEADER WITH ORAL/WRITTEN TAG ─────────────────────────────────────────
def draw_hdr_listening(c, title, time_limit, sub=None):
    y = H - 16 * mm
    try:
        c.drawImage(LOGO_PATH, W - MARGIN - 30 * mm, y - 6 * mm, width=28 * mm,
                    height=14 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 15); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y, title)
    if sub:
        c.setFont("Helvetica", 9); c.setFillColor(BROWN)
        c.drawString(MARGIN, y - 13, sub)
    # ORAL / WRITTEN tag top-right (just left of the logo)
    tag_w = 56 * mm; tag_h = 16
    tag_x = W - MARGIN - 32 * mm - tag_w
    tag_y = y - 4
    c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
    c.roundRect(tag_x, tag_y, tag_w, tag_h, 3, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(tag_x + tag_w / 2, tag_y + 4,
                        f"ORAL  /  WRITTEN   •   {time_limit}")
    c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    ly = y - (18 if sub else 6)
    c.line(MARGIN, ly, W - MARGIN - 32 * mm - tag_w - 4, ly)
    return ly - 6


# ─── DATA GENERATION ──────────────────────────────────────────────────────
def gen_problem(seed, depth, lo, hi, allow_negative=True, signed_prob=0.4):
    """Generate one problem: a list of `depth` signed numbers, running sum stays >= 0."""
    random.seed(seed)
    nums = []
    running = 0
    for i in range(depth):
        if i == 0:
            v = random.randint(lo, hi)
            nums.append(v); running = v
        else:
            attempts = 0
            while True:
                sign = random.choice([1, -1]) if (allow_negative and random.random() < signed_prob) else 1
                mag = random.randint(lo, hi)
                v = sign * mag
                if running + v >= 0:
                    nums.append(v); running += v
                    break
                attempts += 1
                if attempts > 20:
                    nums.append(mag); running += mag
                    break
    return nums, running


def gen_section(pn, section_letter, num_cols, depth, lo, hi, allow_negative=True):
    section_seed = (pn * 31 + ord(section_letter) * 7 + BOOK_SEED)
    return [gen_problem(section_seed + col * 17, depth, lo, hi,
                        allow_negative=allow_negative)
            for col in range(num_cols)]


# ─── SECTION TABLE DRAWING (vertical band, fills full band height) ───────
def draw_section_vertical(c, x, y_top, label, columns_data, depth,
                          band_w, band_h):
    """
    Draw one section as a vertical band of `num_cols` problems.
    Each cell is sized so the section fills the full band height
    (deeper sections get shorter cells, shallow sections get taller cells).
    """
    num_cols = len(columns_data)
    col_w = band_w / num_cols
    row_h = band_h / (depth + 1)  # +1 for header row
    hf = 7

    # Header row across the top with the section label spanning all columns
    hy = y_top - row_h
    # Section label band (across full band width)
    c.setFillColor(BROWN); c.rect(x, hy + row_h - 12, band_w, 12, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(x + band_w / 2, hy + row_h - 10, f"Section {label}")
    # Column numbers row below the section label
    sub_h = row_h - 12
    for ci in range(num_cols):
        cx = x + ci * col_w
        c.setFillColor(DARK_BROWN); c.rect(cx, hy, col_w, sub_h, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf - 1)
        c.drawCentredString(cx + col_w / 2, hy + sub_h / 2 - 2, str(ci + 1))

    # Data rows
    for ri in range(depth):
        ry = hy - (ri + 1) * row_h
        for ci, (nums, _ans) in enumerate(columns_data):
            cx = x + ci * col_w
            c.setFillColor(TF if ri % 2 == 0 else WARM_WHITE)
            c.rect(cx, ry, col_w, row_h, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.25)
            c.rect(cx, ry, col_w, row_h, stroke=1, fill=0)
            if ri < len(nums):
                v = nums[ri]
                # Adaptive font size based on cell dimensions
                fs = min(11, max(6, row_h * 0.45))
                c.setFillColor(DARKER_BROWN)
                c.setFont("Helvetica", fs)
                c.drawCentredString(cx + col_w / 2,
                                    ry + row_h / 2 - fs * 0.35, str(v))


# ─── ANSWER GRID (10 cells: A B C D AB BC CD ABC BCD ABCD) ──────────────
def draw_answer_grid(c, x, y, total_w, total_h):
    labels = ["A", "B", "C", "D", "AB", "BC", "CD", "ABC", "BCD", "ABCD"]
    cell_w = total_w / 10
    label_h = total_h * 0.42
    cell_h = total_h - label_h
    # Labels row (gold)
    for i, lab in enumerate(labels):
        cx = x + i * cell_w
        c.setFillColor(BROWN); c.rect(cx, y - label_h, cell_w, label_h, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 10)
        c.drawCentredString(cx + cell_w / 2, y - label_h + 4, lab)
    # Answer cells (empty for student)
    for i in range(10):
        cx = x + i * cell_w
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.7)
        c.rect(cx, y - label_h - cell_h, cell_w, cell_h, stroke=1, fill=1)


# ─── ONE FULL PAGE ────────────────────────────────────────────────────────
def page_listen(c, pn, time_limit, lo, hi, allow_negative=True):
    bg(c)
    y = draw_hdr_listening(c, "Listening Exercise", time_limit,
                           sub="Teacher reads each column • Student listens and writes the answer")
    draw_footer(c, pn)

    # Generate data for sections A, B, C, D
    sec_a = gen_section(pn, "A", 6, 5, lo, hi, allow_negative=allow_negative)
    sec_b = gen_section(pn, "B", 5, 10, lo, hi, allow_negative=allow_negative)
    sec_c = gen_section(pn, "C", 4, 15, lo, hi, allow_negative=allow_negative)
    sec_d = gen_section(pn, "D", 3, 20, lo, hi, allow_negative=allow_negative)

    # Vertical layout: sections side-by-side as horizontal bands across the page
    # Width distribution proportional to column count (A=6, B=5, C=4, D=3) = 18 total
    total_cols = 18
    section_widths = [(6 / total_cols) * CW, (5 / total_cols) * CW,
                       (4 / total_cols) * CW, (3 / total_cols) * CW]

    # Layout: 4 section bands fill the upper area, answer grid sits above the footer.
    # Footer line is at 13mm; reserve ~24mm above that for the answer grid + gap.
    ans_grid_h = 24            # total height of labels + cells
    ans_grid_top = 14 * mm + ans_grid_h + 4   # ~75pt from bottom of page
    band_top = y
    band_bot = ans_grid_top + 8   # 8pt gap between sections and answer grid
    band_h = band_top - band_bot

    # Draw the 4 sections horizontally (side-by-side)
    cur_x = MARGIN
    for label, sec_data, depth, sec_w in [
            ("A", sec_a, 5, section_widths[0]),
            ("B", sec_b, 10, section_widths[1]),
            ("C", sec_c, 15, section_widths[2]),
            ("D", sec_d, 20, section_widths[3])]:
        draw_section_vertical(c, cur_x, band_top, label, sec_data, depth,
                              sec_w, band_h)
        cur_x += sec_w

    # Answer grid above the footer
    draw_answer_grid(c, MARGIN, ans_grid_top, CW, ans_grid_h)


# ─── COVER ────────────────────────────────────────────────────────────────
def page_cover(c):
    bg(c)
    c.setStrokeColor(GOLD); c.setLineWidth(3)
    c.roundRect(12 * mm, 12 * mm, W - 24 * mm, H - 24 * mm, 8, stroke=1, fill=0)
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(1)
    c.roundRect(15 * mm, 15 * mm, W - 30 * mm, H - 30 * mm, 6, stroke=1, fill=0)
    draw_bead_bird(c, 55 * mm, H - 40 * mm, 32, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - 55 * mm, H - 40 * mm, 30, BROWN, "left", "wink", hat="graduation")
    draw_bead_bird(c, 45 * mm, 50 * mm, 28, LIGHT_GOLD, "right", "surprised")
    draw_bead_bird(c, W - 50 * mm, 55 * mm, 30, GOLD, "left", "happy", action="waving")
    for i in range(15):
        random.seed(i + 1800)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "LISTENING  BOOK")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Oral & Written Exercises")
    c.setFont("Helvetica-Oblique", 11); c.setFillColor(BROWN)
    c.drawCentredString(W / 2, H - 144 * mm,
                        "Teacher reads • Student listens • Student writes")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 80 * mm, H - 154 * mm, W / 2 + 80 * mm, H - 154 * mm)

    iw = 180 * mm; iy = 32 * mm
    c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1)
    c.roundRect((W - iw) / 2, iy, iw, 42 * mm, 5, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, iy + 34 * mm, "Student Information")
    for i, f in enumerate(["Name:", "Level:", "Date:"]):
        fy = iy + 22 * mm - i * 10 * mm
        c.setFont("Helvetica-Bold", 10); c.setFillColor(BROWN)
        c.drawString((W - iw) / 2 + 10, fy, f)
        c.setStrokeColor(LIGHT_GOLD); c.setDash(1, 2)
        c.line((W - iw) / 2 + 35 * mm, fy - 2, (W + iw) / 2 - 10, fy - 2); c.setDash()
    c.setFont("Helvetica", 9); c.setFillColor(BROWN)
    c.drawCentredString(W / 2, 18 * mm, "www.speedyscholars.com")


# ─── MAIN ────────────────────────────────────────────────────────────────
def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
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

    # p49: Final mastery (medium difficulty for assessment)
    page_listen(c, 49, "5 Mins", lo=10, hi=99, allow_negative=True)
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 50 (cover + 49) — LANDSCAPE A4")


if __name__ == "__main__":
    main()
