#!/usr/bin/env python3
"""
Speedy Scholars — Higher A Book A Workbook Generator
6th-level. 47 pages. Competition-prep tier with 3-4 digit numbers,
multi-digit multiplication, and division.
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

set_book("Higher A Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Higher-A-Book-A.pdf")


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
        random.seed(i + 1100)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "HIGHER A — BOOK A")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "6th Level — Competition Mastery")
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


def gen_4digit_data(pn, num_cols=20, num_rows=2):
    """2-row format for 4-digit numbers (1000-9999)."""
    random.seed(pn * 29 + 41)
    cols = []
    for cc in range(num_cols):
        a = random.randint(1000, 8000)
        b = random.choice([-1, 1]) * random.randint(500, 3000)
        if a + b < 0:
            b = -b
        cols.append([a, b])
    return cols


def page_4digit_calc(c, pn, title, time_limit="10 Mins"):
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, time_limit)
    draw_footer(c, pn); scatter_decorations(c, pn)
    cols_data = gen_4digit_data(pn, num_cols=24)
    cur_y = y
    for k in range(3):
        block = cols_data[k * 8:(k + 1) * 8]
        cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, block, num_rows=2)
        cur_y -= 12


def page_multidigit_mult(c, pn, title="Multiplication: 3-digit × 1-digit"):
    """3-digit × 1-digit multiplication problems in 3-col grid."""
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, "12 Mins",
                                            sub="Multi-digit multiplication")
    draw_footer(c, pn); scatter_decorations(c, pn)
    random.seed(pn + 200)
    problems = [(random.randint(100, 999), random.randint(2, 9)) for _ in range(30)]
    cols = 3
    col_w = CW / cols
    per_col = 10
    cell_h = (y - 22 * mm - 8) / per_col
    for i, (a, b) in enumerate(problems):
        col = i // per_col; row = i % per_col
        cx = MARGIN + col * col_w + 16
        cy = y - (row + 1) * cell_h + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(cx, cy, col_w - 30, cell_h - 6, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 14, cy + cell_h / 2 - 6, f"{a} × {b}  =")


def page_multidigit_division(c, pn, title="Division: 4-digit ÷ 1-digit"):
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, "12 Mins",
                                            sub="Multi-digit division")
    draw_footer(c, pn); scatter_decorations(c, pn)
    random.seed(pn + 300)
    problems = []
    for _ in range(30):
        dvs = random.randint(2, 9)
        quotient = random.randint(100, 999)
        dividend = dvs * quotient
        problems.append((dividend, dvs))
    cols = 3
    col_w = CW / cols
    per_col = 10
    cell_h = (y - 22 * mm - 8) / per_col
    for i, (a, b) in enumerate(problems):
        col = i // per_col; row = i % per_col
        cx = MARGIN + col * col_w + 16
        cy = y - (row + 1) * cell_h + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(cx, cy, col_w - 30, cell_h - 6, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 14, cy + cell_h / 2 - 6, f"{a} ÷ {b}  =")


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1-12: Multi-row Abacus Calc with 3-digit
    for pn in range(1, 13):
        elem_gen.page_calc_3digit(c, pn, "Abacus Calculation (3-digit)",
                                  time_limit="10 Mins")
        c.showPage()

    # p13-20: Mental Arithmetic sprints
    for pn in range(13, 21):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic — Sprint",
                                time_limit="5 Mins", num_rows=3, num_cols=30)
        c.showPage()

    # p21-29: Multi-digit multiplication
    for pn in range(21, 30):
        page_multidigit_mult(c, pn)
        c.showPage()

    # p30-37: Division (mix of single-digit-divisor and 4-digit dividend)
    for pn in range(30, 38):
        page_multidigit_division(c, pn)
        c.showPage()

    # p38-43: Mixed assessment / revision (4-digit Abacus Calc)
    for pn in range(38, 44):
        page_4digit_calc(c, pn, "Abacus Calculation (4-digit)",
                         time_limit="10 Mins")
        c.showPage()

    # p44-45: Multiplication revision
    for pn in [44, 45]:
        elem_gen.page_mult_revision(c, pn)
        c.showPage()

    # p46: Final Assessment
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Competition Assessment",
                                            "45 Mins",
                                            sub="All operations with up to 4-digit numbers")
    draw_footer(c, 46); scatter_decorations(c, 46)
    cols_data = gen_4digit_data(46, num_cols=16, num_rows=2)
    cur_y = y
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[:8], num_rows=2)
    cur_y -= 14
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Multi-digit Multiplication & Division")
    cur_y -= 18
    random.seed(46)
    for i in range(20):
        op = "×" if i % 2 == 0 else "÷"
        if op == "×":
            a = random.randint(100, 999); b = random.randint(2, 9)
            expr = f"{a} × {b} ="
        else:
            dvs = random.randint(2, 9)
            q = random.randint(100, 999)
            expr = f"{q * dvs} ÷ {dvs} ="
        col = i % 5; row = i // 5
        mx = MARGIN + col * (CW / 5)
        my = cur_y - row * 22
        c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
        c.drawString(mx + 8, my, expr)
    c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 47 (cover + 46)")


if __name__ == "__main__":
    main()
