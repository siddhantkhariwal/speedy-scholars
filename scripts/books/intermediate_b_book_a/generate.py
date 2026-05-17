#!/usr/bin/env python3
"""
Speedy Scholars — Intermediate B Book A Workbook Generator
5th-level. 47 pages (cover + 46). Between Intermediate A and Higher A.
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
                     draw_calc_table, set_book)

_ELEM = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "elementary_b_book_a"))
sys.path.insert(0, _ELEM)
import generate as elem_gen

set_book("Intermediate B Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Intermediate-B-Book-A.pdf")
elem_gen.set_seed_offset(9000)


# Inline division helper (avoid import collision)
def page_division(c, pn, divisor):
    bg(c); y = elem_gen.draw_hdr_with_time(c, f"Division ÷ {divisor}",
                                            "10 Mins",
                                            sub=f"Find the quotient for each division by {divisor}")
    draw_footer(c, pn); scatter_decorations(c, pn)
    cols = 3; col_w = CW / cols; per_col = 12
    cell_h = (y - 22 * mm - 8) / per_col
    random.seed(pn + 9100)
    for i in range(36):
        q = random.randint(1, 9)
        dividend = q * divisor
        col = i // per_col; row = i % per_col
        cx = MARGIN + col * col_w + 16
        cy = y - (row + 1) * cell_h + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(cx, cy, col_w - 30, cell_h - 4, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 14, cy + cell_h / 2 - 6, f"{dividend} ÷ {divisor}  =")


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
        random.seed(i + 1600)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 36); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "INTERMEDIATE B BOOK A")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "5th Level — Advanced Multi-Digit Mastery")
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
    # p1-12: Abacus Calc 8-row, 3-digit
    for pn in range(1, 13):
        elem_gen.page_calc_3digit(c, pn, "Abacus Calculation (3-digit)",
                                  time_limit="10 Mins")
        c.showPage()
    # p13-18: Mental Arithmetic 4-row 5-min
    for pn in range(13, 19):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic",
                                time_limit="5 Mins", num_rows=4)
        c.showPage()
    # p19-22: Multiplication ×6-×9
    for pn, factor, fn in [(19, 6, draw_apple), (20, 7, draw_strawberry),
                            (21, 8, draw_fish), (22, 9, draw_flower)]:
        elem_gen.page_mult_visual(c, pn, factor, fn=fn)
        c.showPage()
    # p23-29: Mixed Mental/Abacus
    for pn in range(23, 30):
        if pn % 2 == 0:
            elem_gen.page_calc_3digit(c, pn, "Abacus Calculation (3-digit)")
        else:
            elem_gen.page_calc_6row(c, pn, "Mental Arithmetic",
                                    time_limit="5 Mins", num_rows=4)
        c.showPage()
    # p30-33: Division ÷4, ÷5, ÷6, ÷7
    for pn, dvs in [(30, 4), (31, 5), (32, 6), (33, 7)]:
        page_division(c, pn, dvs)
        c.showPage()
    # p34-37: Mixed
    for pn in range(34, 38):
        title = "Mental Arithmetic" if pn % 2 == 0 else "Abacus Calculation"
        elem_gen.page_calc_6row(c, pn, title,
                                time_limit="5 Mins" if "Mental" in title else "10 Mins",
                                num_rows=4 if "Mental" in title else 6)
        c.showPage()
    # p38-45: Speed sprints
    for pn in range(38, 46):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic — Sprint",
                                time_limit="5 Mins", num_rows=3, num_cols=30)
        c.showPage()
    # p46: Final Assessment
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Assessment", "30 Mins",
                                            sub="3-digit calculations + multiplication + division")
    draw_footer(c, 46); scatter_decorations(c, 46)
    cols_data = elem_gen.gen_calc_data(46, num_cols=20, num_rows=4)
    cur_y = y
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[:10], num_rows=4)
    cur_y -= 14
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Multiplication & Division")
    cur_y -= 16
    random.seed(46 + 9000)
    for i in range(20):
        if i % 2 == 0:
            a = random.randint(10, 99); b = random.randint(2, 9)
            expr = f"{a} × {b} ="
        else:
            dvs = random.randint(2, 9); q = random.randint(10, 99)
            expr = f"{q * dvs} ÷ {dvs} ="
        col = i % 5; row = i // 5
        mx = MARGIN + col * (CW / 5)
        my = cur_y - row * 20
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(mx + 8, my, expr)
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 47 (cover + 46)")


if __name__ == "__main__":
    main()
