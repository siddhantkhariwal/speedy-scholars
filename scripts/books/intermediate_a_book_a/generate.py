#!/usr/bin/env python3
"""
Speedy Scholars — Intermediate A Book A Workbook Generator
4th-level. 47 pages (cover + 46). Speed mastery of 2-digit calculations
plus multiplication tables ×4-×7.
"""

import os, sys, math, random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

_SHARED = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_shared"))
sys.path.insert(0, _SHARED)
from illustrations import *
from chrome import (
    W, H, MARGIN, CW, CH, TF, TH, LOGO_PATH, PUBLIC_DIR,
    bg, instr, draw_hdr, draw_footer, page_mascot, draw_calc_table,
    set_book,
)

# Reuse elementary_b_book_a helpers
_ELEM = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "elementary_b_book_a"))
sys.path.insert(0, _ELEM)
import generate as elem_gen

set_book("Intermediate A Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Intermediate-A-Book-A.pdf")


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
        random.seed(i + 900)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 38); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "INTERMEDIATE A — BOOK A")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "4th Level — Speed Mastery")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 80 * mm, H - 137 * mm, W / 2 + 80 * mm, H - 137 * mm)
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


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1-12: Abacus Calc 8-row 2-digit
    for pn in range(1, 13):
        elem_gen.page_calc_6row(c, pn, "Abacus Calculation",
                                time_limit="10 Mins", num_rows=8)
        c.showPage()

    # p13-19: Mental Arithmetic 5-min limits
    for pn in range(13, 20):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic",
                                time_limit="5 Mins", num_rows=8)
        c.showPage()

    # p20-25: Mental Calc smaller-number variants
    for pn in range(20, 26):
        elem_gen.page_calc_6row(c, pn, "Mental Calculation",
                                time_limit="5 Mins", num_rows=8,
                                start_lo=1, start_hi=9)
        c.showPage()

    # p26-29: Abacus Calc 3-digit
    for pn in range(26, 30):
        elem_gen.page_calc_3digit(c, pn, "Abacus Calculation (3-digit)",
                                  time_limit="10 Mins")
        c.showPage()

    # p30-33: Multiplication tables ×4, ×5, ×6, ×7
    for pn, factor, fn in [(30, 4, draw_apple), (31, 5, draw_strawberry),
                            (32, 6, draw_fish), (33, 7, draw_flower)]:
        elem_gen.page_mult_visual(c, pn, factor, fn=fn)
        c.showPage()

    # p34-39: Mental Arithmetic continued
    for pn in range(34, 40):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic",
                                time_limit="5 Mins", num_rows=8)
        c.showPage()

    # p40-43: Mental Arithmetic 8-min 30-problem (use 3-row × 30-col split)
    for pn in range(40, 44):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic — Sprint",
                                time_limit="8 Mins", num_rows=3,
                                num_cols=30)
        c.showPage()

    # p44-45: Multiplication revision
    for pn in [44, 45]:
        elem_gen.page_mult_revision(c, pn)
        c.showPage()

    # p46: Final Assessment
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Assessment",
                                            "30 Mins",
                                            sub="Section D — Addition & Subtraction (Mental)")
    draw_footer(c, 46); scatter_decorations(c, 46)
    cols_data = elem_gen.gen_calc_data(46, num_cols=20, num_rows=7)
    cur_y = y
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[:10], num_rows=7)
    cur_y -= 12
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[10:], num_rows=7)
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 47 (cover + 46)")


if __name__ == "__main__":
    main()
