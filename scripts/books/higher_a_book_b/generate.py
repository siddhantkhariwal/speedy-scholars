#!/usr/bin/env python3
"""
Speedy Scholars — Higher A Book B Workbook Generator
The final book. 47 pages. Top-tier competition prep with the largest numbers
in the curriculum (4-digit) and all four operations mixed.
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


# Inline helpers from higher_a_book_a (avoiding module-name collision)
def gen_4digit_data(pn, num_cols=20, num_rows=2):
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
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, "12 Mins",
                                            sub="Multi-digit multiplication")
    draw_footer(c, pn); scatter_decorations(c, pn)
    random.seed(pn + 200)
    problems = [(random.randint(100, 999), random.randint(2, 9)) for _ in range(30)]
    cols = 3; col_w = CW / cols; per_col = 10
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
        dvs = random.randint(2, 9); quotient = random.randint(100, 999)
        problems.append((dvs * quotient, dvs))
    cols = 3; col_w = CW / cols; per_col = 10
    cell_h = (y - 22 * mm - 8) / per_col
    for i, (a, b) in enumerate(problems):
        col = i // per_col; row = i % per_col
        cx = MARGIN + col * col_w + 16
        cy = y - (row + 1) * cell_h + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(cx, cy, col_w - 30, cell_h - 6, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 14, cy + cell_h / 2 - 6, f"{a} ÷ {b}  =")

set_book("Higher A Book B")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Higher-A-Book-B.pdf")


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
        random.seed(i + 1200)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "HIGHER A — BOOK B")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Final Mastery — Competition Tier")
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


def page_mixed_ops(c, pn, title="Mixed Operations"):
    """Mixed grid of ±/×/÷ problems."""
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, "15 Mins",
                                            sub="All four operations on each row")
    draw_footer(c, pn); scatter_decorations(c, pn)
    random.seed(pn + 400)
    problems = []
    for _ in range(36):
        kind = random.choice(["add", "sub", "mul", "div"])
        if kind == "add":
            a = random.randint(100, 999); b = random.randint(100, 999)
            problems.append(f"{a} + {b} =")
        elif kind == "sub":
            a = random.randint(500, 999); b = random.randint(100, a - 1)
            problems.append(f"{a} − {b} =")
        elif kind == "mul":
            a = random.randint(10, 99); b = random.randint(2, 9)
            problems.append(f"{a} × {b} =")
        else:
            dvs = random.randint(2, 9)
            q = random.randint(10, 99)
            problems.append(f"{q * dvs} ÷ {dvs} =")
    cols = 3
    col_w = CW / cols
    per_col = 12
    cell_h = (y - 22 * mm - 8) / per_col
    for i, expr in enumerate(problems):
        col = i // per_col; row = i % per_col
        cx = MARGIN + col * col_w + 16
        cy = y - (row + 1) * cell_h + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(cx, cy, col_w - 30, cell_h - 4, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 14, cy + cell_h / 2 - 6, expr)


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1-15: 4-digit Abacus + Mental Calc
    for pn in range(1, 16):
        if pn % 3 == 0:
            elem_gen.page_calc_6row(c, pn, "Mental Arithmetic — Sprint",
                                    time_limit="5 Mins", num_rows=3, num_cols=30)
        else:
            page_4digit_calc(c, pn,
                                       "Abacus Calculation (4-digit)" if pn % 2 == 0 else "Mental Calculation (4-digit)",
                                       time_limit="10 Mins")
        c.showPage()

    # p16-22: Multi-digit multiplication + division
    for pn in range(16, 23):
        if pn % 2 == 0:
            page_multidigit_mult(c, pn)
        else:
            page_multidigit_division(c, pn)
        c.showPage()

    # p23-30: Speed Mental Arithmetic sprints
    for pn in range(23, 31):
        elem_gen.page_calc_6row(c, pn, "Mental Arithmetic — Speed Sprint",
                                time_limit="5 Mins", num_rows=3, num_cols=30)
        c.showPage()

    # p31-40: Mixed operation drills
    for pn in range(31, 41):
        page_mixed_ops(c, pn)
        c.showPage()

    # p41-45: Competition simulation (mixed-op heavier)
    for pn in range(41, 46):
        page_mixed_ops(c, pn, title=f"Competition Simulation #{pn - 40}")
        c.showPage()

    # p46: Final mastery assessment
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Mastery Assessment",
                                            "60 Mins",
                                            sub="Complete the four-operation challenge")
    draw_footer(c, 46); scatter_decorations(c, 46)
    # Section A: 4-digit Abacus Calc
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y - 4, "Section A — Abacus Calculation (4-digit)")
    cols_data = gen_4digit_data(46, num_cols=10, num_rows=2)
    cur_y = y - 12
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data, num_rows=2)
    cur_y -= 14

    # Section B: Mixed ops
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Section B — Mixed Operations")
    cur_y -= 16
    random.seed(46)
    for i in range(25):
        kind = random.choice(["mul", "div", "add", "sub"])
        if kind == "mul":
            expr = f"{random.randint(10, 99)} × {random.randint(2, 9)} ="
        elif kind == "div":
            dvs = random.randint(2, 9); q = random.randint(10, 99)
            expr = f"{q * dvs} ÷ {dvs} ="
        elif kind == "add":
            expr = f"{random.randint(100, 999)} + {random.randint(100, 999)} ="
        else:
            a = random.randint(500, 999); b = random.randint(100, a - 1)
            expr = f"{a} − {b} ="
        col = i % 5; row = i // 5
        mx = MARGIN + col * (CW / 5)
        my = cur_y - row * 20
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(mx + 8, my, expr)

    # Footer message
    c.setFont("Helvetica-Oblique", 10); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, 22 * mm + 4,
                        "Congratulations — you've completed the Speedy Scholars curriculum!")

    c.showPage()
    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 47 (cover + 46)")


if __name__ == "__main__":
    main()
