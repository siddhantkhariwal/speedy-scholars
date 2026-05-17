#!/usr/bin/env python3
"""
Speedy Scholars — Elementary B Book B Workbook Generator
Sequel to Elementary B Book A. 43 pages (cover + 42).
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

set_book("Elementary B Book B")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Elementary-B-Book-B.pdf")
elem_gen.set_seed_offset(8000)


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
        random.seed(i + 1500)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 36); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "ELEMENTARY B BOOK B")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "3rd Level — Speed Mastery Continued")
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


def page_42(c):
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Assessment", "30 Mins",
                                            sub="All operations — show your mastery")
    draw_footer(c, 42); scatter_decorations(c, 42)
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y - 4, "Section A — Mental Calculation")
    cols_data = elem_gen.gen_calc_data(42, num_cols=24, num_rows=3)
    cur_y = y - 12
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[:12], num_rows=3)
    cur_y -= 6
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[12:], num_rows=3)
    cur_y -= 14
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Section B — Multiplication")
    random.seed(42 + 8000)
    mult_problems = [(random.randint(0, 9), random.randint(0, 9)) for _ in range(20)]
    mp_y = cur_y - 16
    for i, (a, b) in enumerate(mult_problems):
        col = i % 10; row = i // 10
        mx = MARGIN + col * (CW / 10)
        my = mp_y - row * 18
        c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
        c.drawString(mx + 4, my, f"{a}×{b} =")


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()
    # p1-8: Abacus Calc 6-row, 2-digit
    for pn in range(1, 9):
        elem_gen.page_calc_6row(c, pn, "Abacus Calculation")
        c.showPage()
    # p9: Mental Calc 6-row
    elem_gen.page_calc_6row(c, 9, "Mental Calculation"); c.showPage()
    # p10-15: Mixed Mental/Abacus 6-row, shorter time
    for pn in range(10, 16):
        title = "Mental Calculation" if pn % 2 == 0 else "Abacus Calculation"
        elem_gen.page_calc_6row(c, pn, title,
                                time_limit="5 Mins" if pn >= 14 else "10 Mins")
        c.showPage()
    # p16: Multiplication ×6 visual
    elem_gen.page_mult_visual(c, 16, 6, fn=draw_mango); c.showPage()
    # p17: Multiplication test
    elem_gen.page_mult_test(c, 17); c.showPage()
    # p18: ×7 visual
    elem_gen.page_mult_visual(c, 18, 7, fn=draw_strawberry); c.showPage()
    # p19: ×8 visual
    elem_gen.page_mult_visual(c, 19, 8, fn=draw_apple); c.showPage()
    # p20-24: Abacus Calc 3-digit
    for pn in range(20, 25):
        elem_gen.page_calc_3digit(c, pn, "Abacus Calculation (3-digit)")
        c.showPage()
    # p25: Multiplication revision
    elem_gen.page_mult_revision(c, 25); c.showPage()
    # p26: Mental Calc
    elem_gen.page_calc_6row(c, 26, "Mental Calculation"); c.showPage()
    # p27: ×9 visual
    elem_gen.page_mult_visual(c, 27, 9, fn=draw_butterfly); c.showPage()
    # p28-33: Mixed Calc
    for pn in range(28, 34):
        if pn in [30, 33]:
            elem_gen.page_calc_3digit(c, pn, "Abacus Calculation (3-digit)")
        else:
            title = "Mental Calculation" if pn % 2 == 0 else "Abacus Calculation"
            elem_gen.page_calc_6row(c, pn, title)
        c.showPage()
    # p34: ×4 visual (or revisit lower factor)
    elem_gen.page_mult_visual(c, 34, 4, fn=draw_flower); c.showPage()
    # p35: Multiplication test
    elem_gen.page_mult_test(c, 35); c.showPage()
    # p36-41: Mental Calc series with Time Limit: 5 Mins
    for pn in range(36, 42):
        elem_gen.page_calc_6row(c, pn, "Mental Calculation",
                                time_limit="5 Mins")
        c.showPage()
    # p42: Final assessment
    page_42(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 43 (cover + 42)")


if __name__ == "__main__":
    main()
