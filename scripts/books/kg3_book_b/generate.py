#!/usr/bin/env python3
"""
Speedy Scholars — KG-3 Book B Workbook Generator
Sequel to KG-3 Book A. Combination of 5 (+4, +3, +2, +1) and intro to
Composition of 10 (mental). 39 pages (cover + 38).
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

set_book("KG-3 Book B")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG3-Book-B.pdf")

elem_gen.set_seed_offset(7500)


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
        random.seed(i + 1400)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-3  BOOK B")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Combinations & Big-Friends of 10")
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


# ─── CONCEPT PAGE: SMALL FRIENDS OF 5 ────────────────────────────────────
def page_small_friends(c, pn):
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Small Friends of 5",
                                            "5 Mins",
                                            sub="Each pair makes 5. Write the missing partner.")
    draw_footer(c, pn); scatter_decorations(c, pn)

    # 4 partner pairs that make 5 (excluding 0+5)
    pairs = [(1, 4), (2, 3), (3, 2), (4, 1)]

    # Two-column layout: left = visual mushroom pairs, right = number bonds
    # Visual side
    for i, (a, b) in enumerate(pairs):
        ry = y - 30 - i * 70
        # Featured number "5" in circle on left
        c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.circle(MARGIN + 50, ry - 8, 22, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(MARGIN + 50, ry - 15, "5")
        # Branch lines
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(MARGIN + 65, ry - 20, MARGIN + 110, ry - 38)
        c.line(MARGIN + 65, ry - 0, MARGIN + 110, ry + 18)
        # Number bond children
        for k, (val, side_y) in enumerate([(a, ry + 18), (b, ry - 38)]):
            c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN)
            c.roundRect(MARGIN + 110, side_y - 12, 32, 24, 3, stroke=1, fill=1)
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 16)
            c.drawCentredString(MARGIN + 126, side_y - 5, str(val))

        # Right side: fill-in equation
        c.setFont("Helvetica-Bold", 18); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 200, ry - 10, f"{a} + ___ = 5")
        c.drawString(MARGIN + 360, ry - 10, f"___ + {b} = 5")

    # Right side big table summarizing all 4 partner-of-5 pairs
    tbl_x = W - MARGIN - 220
    tbl_y = y - 30
    c.setFont("Helvetica-Bold", 12); c.setFillColor(BROWN)
    c.drawString(tbl_x, tbl_y + 6, "All pairs of 5:")
    rh = 28
    for i, (a, b) in enumerate(pairs + [(0, 5), (5, 0)]):
        ry = tbl_y - 16 - i * rh
        c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
        c.roundRect(tbl_x, ry, 90, rh - 4, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(tbl_x + 45, ry + 8, f"{a} + {b} = 5")


# ─── CONCEPT PAGE: BIG FRIENDS OF 10 ─────────────────────────────────────
def page_big_friends(c, pn):
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Big Friends of 10",
                                            "5 Mins",
                                            sub="Each pair makes 10. Write the missing partner.")
    draw_footer(c, pn); scatter_decorations(c, pn)

    # 9 partner pairs of 10
    pairs = [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5),
             (6, 4), (7, 3), (8, 2), (9, 1)]

    # 3-column grid of pairs
    cols = 3
    rows = 3
    avail_h = y - 26 * mm - 8
    col_w = CW / cols
    cell_h = avail_h / rows

    for i, (a, b) in enumerate(pairs):
        col = i % cols
        row = i // cols
        cx = MARGIN + col * col_w + col_w / 2
        cy = y - (row + 1) * cell_h + cell_h / 2

        # "10" on top
        c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.circle(cx, cy + 30, 18, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(cx, cy + 23, "10")
        # Lines
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(cx - 12, cy + 18, cx - 32, cy)
        c.line(cx + 12, cy + 18, cx + 32, cy)
        # Children
        for k, (val, side_x) in enumerate([(a, cx - 32), (b, cx + 32)]):
            c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN)
            c.roundRect(side_x - 16, cy - 14, 32, 24, 3, stroke=1, fill=1)
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 14)
            c.drawCentredString(side_x, cy - 6, str(val))
        # Equation underneath
        c.setFont("Helvetica-Bold", 11); c.setFillColor(BROWN)
        c.drawCentredString(cx, cy - 30, f"{a} + {b} = 10")


# ─── 30-COL CALC (reuse pattern from KG-3 A) ──────────────────────────────
def page_calc_30col(c, pn, title, time_limit="10 Mins", num_rows=3,
                    start_lo=10, start_hi=99, sub=None):
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, time_limit, sub=sub)
    draw_footer(c, pn); scatter_decorations(c, pn)
    cols_data = elem_gen.gen_calc_data(pn, num_cols=30, num_rows=num_rows,
                                       start_lo=start_lo, start_hi=start_hi)
    cur_y = y
    for k in range(3):
        block = cols_data[k * 10:(k + 1) * 10]
        cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, block, num_rows=num_rows)
        cur_y -= 10


def page_mental_with_eqs(c, pn, title, time_limit="5 Mins", num_rows=3,
                          start_lo=1, start_hi=9, sub=None):
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, time_limit, sub=sub)
    draw_footer(c, pn); scatter_decorations(c, pn)
    cols_data = elem_gen.gen_calc_data(pn, num_cols=20, num_rows=num_rows,
                                       start_lo=start_lo, start_hi=start_hi)
    cur_y = y
    for k in range(2):
        block = cols_data[k * 10:(k + 1) * 10]
        cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, block, num_rows=num_rows)
        cur_y -= 10

    random.seed(pn * 37 + 7500)
    eqs = []
    for _ in range(6):
        a = random.randint(start_lo, start_hi)
        b = random.choice([-1, 1]) * random.randint(1, 9)
        c2 = random.choice([-1, 1]) * random.randint(1, 9)
        eq_str = str(a)
        if b > 0: eq_str += f" + {b}"
        else: eq_str += f" − {abs(b)}"
        if c2 > 0: eq_str += f" + {c2}"
        else: eq_str += f" − {abs(c2)}"
        eq_str += " ="
        eqs.append(eq_str)

    eq_y_top = cur_y - 6
    eq_y_bot = 22 * mm + 8
    eq_h = eq_y_top - eq_y_bot
    if eq_h > 60:
        c.setFont("Helvetica-Bold", 9); c.setFillColor(BROWN)
        c.drawString(MARGIN, eq_y_top - 4, "Written practice:")
        col_w = CW / 3
        per_col = 2
        for i, eq in enumerate(eqs):
            col = i // per_col; row = i % per_col
            ex = MARGIN + col * col_w + 12
            ey = eq_y_top - 22 - row * 22
            c.setFont("Helvetica", 11); c.setFillColor(DARKER_BROWN)
            c.drawString(ex, ey, eq)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.5)
            c.line(ex + 110, ey - 2, ex + 160, ey - 2)


def page_38(c):
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Assessment", "30 Mins",
                                            sub="Sections A & B — all you've learned")
    draw_footer(c, 38); scatter_decorations(c, 38)
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y - 4, "Section A — Abacus Calculation (2-digit)")
    cols_data = elem_gen.gen_calc_data(38, num_cols=20, num_rows=3,
                                       start_lo=10, start_hi=99)
    cur_y = y - 12
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[:10], num_rows=3)
    cur_y -= 12
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Section B — Mental Calculation (single digit)")
    cur_y -= 4
    cols_b = elem_gen.gen_calc_data(38 + 100, num_cols=20, num_rows=4,
                                    start_lo=1, start_hi=9)
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_b[:10], num_rows=4)


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1: Small Friends concept
    page_small_friends(c, 1); c.showPage()

    # p2-3: Combination of 5 (+4)
    for pn in [2, 3]:
        page_calc_30col(c, pn, "Abacus Calculation: Combination of 5 (+4)",
                        time_limit="10 Mins",
                        sub="+4 = −1 + 5  (applied on the ones rod)")
        c.showPage()

    # p4-5: Revision
    for pn in [4, 5]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p6: Combination of 5 (+3)
    page_calc_30col(c, 6, "Abacus Calculation: Combination of 5 (+3)",
                    time_limit="10 Mins", sub="+3 = −2 + 5")
    c.showPage()

    # p7-8: Revision
    for pn in [7, 8]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p9: Combination of 5 (+2)
    page_calc_30col(c, 9, "Abacus Calculation: Combination of 5 (+2)",
                    time_limit="10 Mins", sub="+2 = −3 + 5")
    c.showPage()

    # p10-11: Revision
    for pn in [10, 11]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p12: Combination of 5 (+1)
    page_calc_30col(c, 12, "Abacus Calculation: Combination of 5 (+1)",
                    time_limit="10 Mins", sub="+1 = −4 + 5")
    c.showPage()

    # p13-14: Mental Calc revision
    for pn in [13, 14]:
        page_mental_with_eqs(c, pn, "Mental Calculation: Revision",
                             time_limit="5 Mins")
        c.showPage()

    # p15: Big Friends concept
    page_big_friends(c, 15); c.showPage()

    # p16-22: Mental Calc Combinations of 10 (+9..+1)
    factors = [(16, 9), (17, 8), (18, 7), (19, 6), (20, 5), (21, 4), (22, 1)]
    tricks = {9: "−1 + 10", 8: "−2 + 10", 7: "−3 + 10", 6: "−4 + 10",
              5: "−5 + 10", 4: "−6 + 10", 1: "−9 + 10"}
    for pn, f in factors:
        page_mental_with_eqs(c, pn,
                             f"Mental Calculation: Combination of 10 (+{f})",
                             time_limit="5 Mins",
                             sub=f"+{f} = {tricks[f]}")
        c.showPage()

    # p23-30: Mental Calc continued revision
    for pn in range(23, 31):
        page_mental_with_eqs(c, pn, "Mental Calculation: Revision",
                             time_limit="5 Mins")
        c.showPage()

    # p31-37: 2-digit Abacus Calc revision
    for pn in range(31, 38):
        page_calc_30col(c, pn, "Abacus Calculation: Revision (2-digit)",
                        time_limit="10 Mins")
        c.showPage()

    # p38: Final Assessment
    page_38(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 39 (cover + 38)")


if __name__ == "__main__":
    main()
