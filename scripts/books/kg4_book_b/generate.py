#!/usr/bin/env python3
"""
Speedy Scholars — KG-4 Book B Workbook Generator
Sequel to KG-4 Book A. Continued Mental + Abacus Calculation drilling with
2-digit numbers and multiplication tables (×2, ×4, ×5). 37 pages (cover + 36).
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

# Reuse KG-4 Book A's calc-grid + multiplication functions by importing them
_KG4A = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "kg4_book_a"))
sys.path.insert(0, _KG4A)
import generate as kg4a_gen

set_book("KG-4 Book B")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG4-Book-B.pdf")


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
        random.seed(i + 700)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-4  BOOK B")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Mental Calculation & Multiplication Continued")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 90 * mm, H - 137 * mm, W / 2 + 90 * mm, H - 137 * mm)
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

    # p1-8: Mental Calculation grids
    for pn in range(1, 9):
        kg4a_gen.page_calc_grid(c, pn, "Mental Calculation")
        c.showPage()

    # p9-14: Abacus Calculation grids
    for pn in range(9, 15):
        kg4a_gen.page_calc_grid(c, pn, "Abacus Calculation")
        c.showPage()

    # p15: Multiplication ×2
    kg4a_gen.page_multiplication(c, 15, 2); c.showPage()

    # p16-22: Abacus Calc with bottom sums on some pages
    for pn in range(16, 23):
        kg4a_gen.page_calc_grid(c, pn, "Abacus Calculation",
                                with_sums=(pn in [17, 20, 22]))
        c.showPage()

    # p23: Multiplication ×4
    kg4a_gen.page_multiplication(c, 23, 4); c.showPage()

    # p24-28: Mental Calculation
    for pn in range(24, 29):
        kg4a_gen.page_calc_grid(c, pn, "Mental Calculation")
        c.showPage()

    # p29: Multiplication ×5
    kg4a_gen.page_multiplication(c, 29, 5); c.showPage()

    # p30-35: Mixed Mental + Abacus
    for pn in range(30, 36):
        title = "Mental Calculation" if pn % 2 == 0 else "Abacus Calculation"
        kg4a_gen.page_calc_grid(c, pn, title)
        c.showPage()

    # p36: Final Assessment
    bg(c); y = draw_hdr(c, "Final Assessment",
                        "Mental + Abacus + Multiplication — all together"); draw_footer(c, 36)
    scatter_decorations(c, 36)
    cols_data = kg4a_gen.gen_calc_data(36, num_cols=20, num_rows=3)
    cur_y = y
    for k in range(2):
        block = cols_data[k * 10:(k + 1) * 10]
        cur_y = kg4a_gen._draw_grid_table(c, MARGIN, cur_y, block)
        cur_y -= 12
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 37 (cover + 36)")


if __name__ == "__main__":
    main()
