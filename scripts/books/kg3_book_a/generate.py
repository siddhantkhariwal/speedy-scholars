#!/usr/bin/env python3
"""
Speedy Scholars — KG-3 Book A Workbook Generator
Bridge book between KG-2 (single-digit) and KG-4 (2-digit fluency).
39 pages (cover + 38).
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

set_book("KG-3 Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG3-Book-A.pdf")

# Unique seed offset so problems differ from other books
elem_gen.set_seed_offset(7000)


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
        random.seed(i + 1300)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-3  BOOK A")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Bridge to Two-Digit Mastery")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 80 * mm, H - 137 * mm, W / 2 + 80 * mm, H - 137 * mm)
    for i, (u, l, lb) in enumerate([(1, 2, "7"), (1, 4, "9"), (0, 3, "3")]):
        draw_abacus(c, W / 2 - 55 * mm + i * 45 * mm, H - 178 * mm, 22 * mm,
                    30 * mm, u, l, lb)
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


# ─── 30-COL CALC PAGE (3 sub-tables of 10 each) ──────────────────────────
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


# ─── MENTAL CALC PAGE WITH SMALL WRITTEN EQS AT BOTTOM ───────────────────
def page_mental_with_eqs(c, pn, title, time_limit="5 Mins", num_rows=3,
                          start_lo=1, start_hi=9, sub=None):
    """Mental Calc grid (20-col × num_rows) + 6 small written equations at bottom."""
    bg(c); y = elem_gen.draw_hdr_with_time(c, title, time_limit, sub=sub)
    draw_footer(c, pn); scatter_decorations(c, pn)
    cols_data = elem_gen.gen_calc_data(pn, num_cols=20, num_rows=num_rows,
                                       start_lo=start_lo, start_hi=start_hi)
    cur_y = y
    for k in range(2):
        block = cols_data[k * 10:(k + 1) * 10]
        cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, block, num_rows=num_rows)
        cur_y -= 10

    # Small written-equation area at bottom
    random.seed(pn * 31 + 7000)
    eqs = []
    for _ in range(6):
        a = random.randint(start_lo, start_hi)
        b = random.choice([-1, 1]) * random.randint(1, 9)
        c2 = random.choice([-1, 1]) * random.randint(1, 9)
        eq_str = f"{a}"
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


# ─── CARRY-FORWARD CONCEPT PAGE ──────────────────────────────────────────
def page_carry_concept(c, pn):
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Carrying Forward — Two Digits",
                                            "10 Mins",
                                            sub="When the ones rod overflows, carry to the tens rod")
    draw_footer(c, pn); scatter_decorations(c, pn)

    # Mascot with thought bubble
    draw_bead_bird(c, MARGIN + 50, y - 70, 36, GOLD, "right", "thinking",
                   hat="graduation")
    bub_x = MARGIN + 110
    bub_y = y - 60
    c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
    c.roundRect(bub_x, bub_y - 50, 200, 60, 8, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(bub_x + 12, bub_y - 8, "When 8 + 5 overflows the ones rod,")
    c.drawString(bub_x + 12, bub_y - 22, "we use: 8 = 8 + 2 + 10")
    c.drawString(bub_x + 12, bub_y - 36, "Carry the 1 to the tens place.")

    # Right column: pattern table
    col_x = MARGIN + 340
    col_y = y - 20
    c.setFont("Helvetica-Bold", 12); c.setFillColor(GOLD)
    c.drawString(col_x, col_y, "Pattern: a + b where a + b > 9")
    rows = [("98 + 1", "= 99"), ("98 + 2", "= 100"), ("98 + 3", "= 101"),
            ("98 + 4", "= 102"), ("99 + 5", "= 104"), ("99 + 6", "= 105"),
            ("99 + 7", "= 106"), ("99 + 8", "= 107"), ("99 + 9", "= 108")]
    for i, (lhs, rhs) in enumerate(rows):
        ry = col_y - 24 - i * 16
        c.setFont("Helvetica", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(col_x, ry, lhs)
        c.setFont("Helvetica-Bold", 11); c.setFillColor(BROWN)
        c.drawString(col_x + 80, ry, rhs)

    # Bottom: practice problems
    practice_y = 30 * mm
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, practice_y + 30, "Try these:")
    practice = ["98 + 7 =", "99 + 8 =", "97 + 9 =", "96 + 4 ="]
    for i, eq in enumerate(practice):
        c.setFont("Helvetica", 13); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + i * (CW / 4) + 10, practice_y, eq)
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.5)
        c.line(MARGIN + i * (CW / 4) + 80, practice_y - 2,
               MARGIN + i * (CW / 4) + 120, practice_y - 2)


# ─── FINAL ASSESSMENT ─────────────────────────────────────────────────────
def page_38(c):
    bg(c); y = elem_gen.draw_hdr_with_time(c, "Final Assessment", "30 Mins",
                                            sub="Section A: Abacus / Section B: Mental")
    draw_footer(c, 38); scatter_decorations(c, 38)
    # Section A — 2-digit Abacus Calc
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y - 4, "Section A — Abacus Calculation (2-digit)")
    cols_data = elem_gen.gen_calc_data(38, num_cols=20, num_rows=3,
                                       start_lo=10, start_hi=99)
    cur_y = y - 12
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_data[:10], num_rows=3)
    cur_y -= 12

    # Section B — Mental Calc (single digit, 4 rows)
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Section B — Mental Calculation (single digit)")
    cur_y -= 4
    cols_b = elem_gen.gen_calc_data(38 + 100, num_cols=20, num_rows=4,
                                    start_lo=1, start_hi=9)
    cur_y = elem_gen._draw_grid(c, MARGIN, cur_y, cols_b[:10], num_rows=4)


# ─── MAIN ────────────────────────────────────────────────────────────────
def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1-2: 2-digit Abacus Calc (intro)
    for pn in [1, 2]:
        page_calc_30col(c, pn, "Abacus Calculation: 2 Digits, 2 Rows",
                        time_limit="10 Mins")
        c.showPage()

    # p3-4: Decomposition of 5 (-4) with 2-digit
    for pn in [3, 4]:
        page_calc_30col(c, pn, "Abacus Calculation: Decomposition of 5 (−4)",
                        time_limit="10 Mins",
                        sub="−4 = +1 − 5  (applied on the ones rod)")
        c.showPage()

    # p5: Decomp of 5 (+4) revision
    page_calc_30col(c, 5, "Abacus Calculation: Decomposition of 5 (+4)",
                    time_limit="10 Mins")
    c.showPage()

    # p6-7: Revision
    for pn in [6, 7]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p8: Decomp -3
    page_calc_30col(c, 8, "Abacus Calculation: Decomposition of 5 (−3)",
                    time_limit="10 Mins",
                    sub="−3 = +2 − 5  (applied on the ones rod)")
    c.showPage()

    # p9-10: Revision
    for pn in [9, 10]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p11: Decomp -2
    page_calc_30col(c, 11, "Abacus Calculation: Decomposition of 5 (−2)",
                    time_limit="10 Mins",
                    sub="−2 = +3 − 5  (applied on the ones rod)")
    c.showPage()

    # p12: Revision
    page_calc_30col(c, 12, "Abacus Calculation: Revision", time_limit="10 Mins")
    c.showPage()

    # p13: Decomp -1
    page_calc_30col(c, 13, "Abacus Calculation: Decomposition of 5 (−1)",
                    time_limit="10 Mins",
                    sub="−1 = +4 − 5  (applied on the ones rod)")
    c.showPage()

    # p14-17: Revision (mixed 2-digit)
    for pn in [14, 15, 16, 17]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p18-22: More 2-digit revision
    for pn in [18, 19, 20, 21, 22]:
        page_calc_30col(c, pn, "Abacus Calculation: Revision",
                        time_limit="10 Mins")
        c.showPage()

    # p23: Mental Calc Revision (with written equations footer)
    page_mental_with_eqs(c, 23, "Mental Calculation: Revision",
                         time_limit="5 Mins")
    c.showPage()

    # p24: Mental Calc Decomposition of 10 (+9)
    page_mental_with_eqs(c, 24, "Mental Calculation: Decomposition of 10 (+9)",
                         time_limit="5 Mins",
                         sub="+9 = −1 + 10")
    c.showPage()

    # p25: Mental Calc Decomp +4
    page_mental_with_eqs(c, 25, "Mental Calculation: Decomposition of 10 (+4)",
                         time_limit="5 Mins",
                         sub="+4 = −6 + 10")
    c.showPage()

    # p26-30: Mental Calc continued
    titles = ["Mental Calculation: Decomposition of 10 (+8)",
             "Mental Calculation: Decomposition of 10 (+7)",
             "Mental Calculation: Decomposition of 10 (+6)",
             "Mental Calculation: Decomposition of 10 (+5)",
             "Mental Calculation: Revision"]
    subs = ["+8 = −2 + 10", "+7 = −3 + 10", "+6 = −4 + 10", "+5 = −5 + 10", None]
    for pn, t, s in zip([26, 27, 28, 29, 30], titles, subs):
        page_mental_with_eqs(c, pn, t, time_limit="5 Mins", sub=s)
        c.showPage()

    # p31-34: Mental Calc Revision
    for pn in [31, 32, 33, 34]:
        page_mental_with_eqs(c, pn, "Mental Calculation: Revision",
                             time_limit="5 Mins")
        c.showPage()

    # p35: Concept page (carry-forward intro)
    page_carry_concept(c, 35)
    c.showPage()

    # p36-37: Abacus Calc with 2-digit + carry
    for pn in [36, 37]:
        page_calc_30col(c, pn, "Abacus Calculation: 2-Digit + Carry",
                        time_limit="10 Mins")
        c.showPage()

    # p38: Final Assessment
    page_38(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 39 (cover + 38)")


if __name__ == "__main__":
    main()
