#!/usr/bin/env python3
"""
Speedy Scholars — Elementary B Book A Workbook Generator
3rd-level workbook. 43 pages (cover + 42). Step up from KG-4:
- 6-row calculation tables (vs 3-row in KG-4)
- 3-digit numbers on Abacus Calc pages (2-row format)
- Multiplication tests with grouped problem sets
- Time-limit headers on each page
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

set_book("Elementary B Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-Elementary-B-Book-A.pdf")


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
        random.seed(i + 800)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 36); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "ELEMENTARY B BOOK A")
    c.setFont("Helvetica", 14); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "3rd Level — Mastery & Speed Drills")
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


# ─── PROGRAMMATIC DATA GEN ────────────────────────────────────────────────
# Per-book seed offset — each importing book sets this before generating so that
# different books with shared helpers don't produce identical page data.
BOOK_SEED_OFFSET = 0

def set_seed_offset(n):
    global BOOK_SEED_OFFSET
    BOOK_SEED_OFFSET = n


def gen_calc_data(pn, num_cols=20, num_rows=6, start_lo=10, start_hi=99, op_max=9):
    random.seed(pn * 17 + 11 + BOOK_SEED_OFFSET)
    cols = []
    for cc in range(num_cols):
        attempts = 0
        while attempts < 50:
            start = random.randint(start_lo, start_hi)
            ops = []
            val = start
            ok = True
            for r in range(num_rows - 1):
                delta = random.choice([-1, 1]) * random.randint(1, op_max)
                if 0 <= val + delta <= start_hi:
                    val += delta
                    ops.append(delta)
                else:
                    delta = -delta
                    if 0 <= val + delta <= start_hi:
                        val += delta
                        ops.append(delta)
                    else:
                        ok = False
                        break
            if ok:
                cols.append([start] + ops)
                break
            attempts += 1
        else:
            cols.append([start_lo] + [1] * (num_rows - 1))
    return cols


def gen_3digit_data(pn, num_cols=24, num_rows=2):
    """2-row format for 3-digit numbers."""
    random.seed(pn * 23 + 19 + BOOK_SEED_OFFSET)
    cols = []
    for cc in range(num_cols):
        a = random.randint(100, 800)
        b = random.choice([-1, 1]) * random.randint(50, 400)
        if a + b < 0:
            b = -b
        cols.append([a, b])
    return cols


# ─── HEADER WITH TIME LIMIT ──────────────────────────────────────────────
def draw_hdr_with_time(c, title, time_limit, sub=None):
    """Draw the standard header plus a time-limit indicator on the right."""
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
    # Time limit badge
    c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
    c.roundRect(W - MARGIN - 95 * mm, y - 4, 30 * mm, 18, 4, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 8); c.setFillColor(DARKER_BROWN)
    c.drawString(W - MARGIN - 93 * mm, y, f"Time Limit: {time_limit}")
    c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    ly = y - (18 if sub else 6)
    c.line(MARGIN, ly, W - MARGIN - 100 * mm, ly)
    # Time field on far right
    c.setFont("Helvetica-Bold", 8); c.setFillColor(BROWN)
    c.drawString(W - MARGIN - 65 * mm, y, "Time:  __________")
    return ly - 6


# ─── 6-ROW CALC GRID PAGE ────────────────────────────────────────────────
def page_calc_6row(c, pn, title, time_limit="10 Mins", num_rows=6,
                   num_cols=24, start_lo=10, start_hi=99):
    bg(c); y = draw_hdr_with_time(c, title, time_limit); draw_footer(c, pn)
    scatter_decorations(c, pn)
    cols_data = gen_calc_data(pn, num_cols=num_cols, num_rows=num_rows,
                              start_lo=start_lo, start_hi=start_hi)
    # 2 sub-tables of (num_cols / 2) columns each
    half = num_cols // 2
    cur_y = y
    for k in range(2):
        block = cols_data[k * half:(k + 1) * half]
        cur_y = _draw_grid(c, MARGIN, cur_y, block, num_rows=num_rows)
        cur_y -= 12


def _draw_grid(c, x, y, table_data, num_rows=6):
    cols = len(table_data)
    rh = 14
    sw = 22
    cw = (CW - sw) / cols
    hf = 8
    hy = y - rh
    c.setFillColor(BROWN); c.rect(x, hy, sw, rh, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + sw / 2, hy + 3, "S.No.")
    for i in range(cols):
        cx = x + sw + i * cw
        c.setFillColor(BROWN); c.rect(cx, hy, cw, rh, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + cw / 2, hy + 3, str(i + 1))

    labels = [str(k + 1) for k in range(num_rows)] + ["Ans."]
    for ri, lab in enumerate(labels):
        ry = hy - (ri + 1) * rh
        is_ans = "Ans" in lab
        c.setFillColor(TH if is_ans else TF)
        c.rect(x, ry, sw, rh, stroke=0, fill=1)
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3)
        c.rect(x, ry, sw, rh, stroke=1, fill=0)
        c.setFillColor(DARKER_BROWN)
        c.setFont("Helvetica-Bold" if is_ans else "Helvetica", hf)
        c.drawCentredString(x + sw / 2, ry + 3, lab)
        for i in range(cols):
            cx = x + sw + i * cw
            c.setFillColor(TH if is_ans else TF)
            c.rect(cx, ry, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3)
            c.rect(cx, ry, cw, rh, stroke=1, fill=0)
            if not is_ans and i < len(table_data) and ri < len(table_data[i]):
                v = table_data[i][ri]
                if v is not None:
                    c.setFillColor(DARKER_BROWN); c.setFont("Helvetica", 8.5)
                    s = str(v)  # no + sign for positive operands (abacus convention)
                    c.drawCentredString(cx + cw / 2, ry + 3, s)
    return hy - (num_rows + 1) * rh - 4


# ─── 3-DIGIT 2-ROW CALC PAGE ─────────────────────────────────────────────
def page_calc_3digit(c, pn, title, time_limit="10 Mins"):
    bg(c); y = draw_hdr_with_time(c, title, time_limit); draw_footer(c, pn)
    scatter_decorations(c, pn)
    cols_data = gen_3digit_data(pn, num_cols=24, num_rows=2)
    half = 8
    cur_y = y
    for k in range(3):
        block = cols_data[k * half:(k + 1) * half]
        cur_y = _draw_grid(c, MARGIN, cur_y, block, num_rows=2)
        cur_y -= 12


# ─── MULTIPLICATION ×N VISUAL PAGE ───────────────────────────────────────
def page_mult_visual(c, pn, factor, fn=draw_apple):
    bg(c); y = draw_hdr_with_time(c, f"Multiplication × {factor}",
                                   "5 Mins",
                                   sub="Solve, then look at the visual groupings"); draw_footer(c, pn)
    scatter_decorations(c, pn)

    # Top: 3 columns of multiplication problems
    col_w = CW / 4
    cell_h = (y - 26 * mm - 8) / 11
    col_data = [list(range(10)),
                list(range(9, -1, -1)),
                list(range(0, 10, 1))]
    random.seed(pn + 60)
    random.shuffle(col_data[2])

    for ci, col in enumerate(col_data):
        cx = MARGIN + ci * col_w + 12
        for ri, k in enumerate(col):
            cy = y - (ri + 1) * cell_h - 6
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
            c.roundRect(cx, cy, col_w - 24, cell_h - 4, 3, stroke=1, fill=1)
            c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
            if ci == 0:
                expr = f"{k} × {factor}  ="
            elif ci == 1:
                expr = f"{factor} × {k}  ="
            else:
                expr = f"{k} × {factor}  =" if ri % 2 == 0 else f"{factor} × {k}  ="
            c.drawString(cx + 10, cy + cell_h / 2 - 6, expr)

    # 4th column: visual grouping (e.g., 4 groups of N apples)
    vx = MARGIN + 3 * col_w + 12
    vw = col_w - 24
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(vx, y - 16, f"× {factor} = groups of {factor}:")
    obj_s = 9
    for groups in [2, 3, 4, 5]:
        gy = y - 32 - (groups - 2) * 32
        c.setFont("Helvetica-Bold", 9); c.setFillColor(BROWN)
        c.drawString(vx, gy + 14, f"{groups} × {factor}:")
        for g in range(groups):
            for k in range(factor):
                ox = vx + 4 + g * (factor * (obj_s + 2) + 6) + k * (obj_s + 2)
                if ox + obj_s < vx + vw:
                    fn(c, ox, gy, size=obj_s)


# ─── MULTIPLICATION TEST WITH GROUPS A/B/C/D ─────────────────────────────
def page_mult_test(c, pn):
    bg(c); y = draw_hdr_with_time(c, "Multiplication: Group Test", "10 Mins",
                                   sub="Solve each group — A, B, C, D"); draw_footer(c, pn)
    scatter_decorations(c, pn)

    groups = ["A", "B", "C", "D"]
    group_problems = {
        "A": [(2,3),(4,5),(1,2),(0,5),(8,3),(7,2),(3,1),(5,2)],
        "B": [(6,5),(2,5),(3,2),(4,5),(9,2),(5,3),(8,3),(2,5)],
        "C": [(1,5),(7,1),(8,2),(3,3),(5,3),(4,1),(4,3),(2,1)],
        "D": [(5,2),(7,3),(6,2),(9,0),(3,5),(8,5),(4,2),(2,4)],
    }

    col_w = CW / 4
    for ci, g in enumerate(groups):
        cx = MARGIN + ci * col_w + 10
        # Balloon-style group label
        c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.2)
        c.circle(cx + col_w / 2 - 5, y - 30, 22, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(cx + col_w / 2 - 5, y - 38, g)
        # String dangling from balloon
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.6)
        c.line(cx + col_w / 2 - 5, y - 52, cx + col_w / 2 - 5, y - 70)
        # 8 problems in the group
        for ri, (a, b) in enumerate(group_problems[g]):
            ry = y - 80 - ri * 26
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
            c.roundRect(cx + 4, ry, col_w - 30, 22, 3, stroke=1, fill=1)
            c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
            c.drawString(cx + 14, ry + 7, f"{a} × {b}  =")


# ─── MULTIPLICATION REVISION (3 plain columns) ───────────────────────────
def page_mult_revision(c, pn):
    bg(c); y = draw_hdr_with_time(c, "Multiplication: Revision", "10 Mins"); draw_footer(c, pn)
    scatter_decorations(c, pn)
    random.seed(pn + 90)
    problems = []
    for _ in range(36):
        a = random.randint(0, 9)
        b = random.randint(1, 6)
        problems.append((a, b))
    cols = 3
    col_w = CW / cols
    per_col = 12
    cell_h = (y - 22 * mm - 8) / per_col
    for i, (a, b) in enumerate(problems[:36]):
        col = i // per_col; row = i % per_col
        cx = MARGIN + col * col_w + 16
        cy = y - (row + 1) * cell_h + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(cx, cy, col_w - 30, cell_h - 4, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 14, cy + cell_h / 2 - 6, f"{a} × {b}  =")


# ─── FINAL ASSESSMENT ─────────────────────────────────────────────────────
def page_42(c):
    bg(c); y = draw_hdr_with_time(c, "Final Assessment", "30 Mins",
                                   sub="All operations — show your mastery"); draw_footer(c, 42)
    scatter_decorations(c, 42)
    # Section A: 24-col × 3-row
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y - 4, "Section A — Mental Calculation")
    cols_data = gen_calc_data(42, num_cols=24, num_rows=3)
    cur_y = y - 12
    cur_y = _draw_grid(c, MARGIN, cur_y, cols_data[:12], num_rows=3)
    cur_y -= 6
    cur_y = _draw_grid(c, MARGIN, cur_y, cols_data[12:], num_rows=3)
    # Section B: Multiplication
    cur_y -= 14
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, cur_y, "Section B — Multiplication")
    random.seed(42)
    mult_problems = [(random.randint(0, 9), random.randint(0, 9)) for _ in range(20)]
    mp_y = cur_y - 16
    for i, (a, b) in enumerate(mult_problems):
        col = i % 10; row = i // 10
        mx = MARGIN + col * (CW / 10)
        my = mp_y - row * 18
        c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
        c.drawString(mx + 4, my, f"{a}×{b} =")


# ─── MAIN ────────────────────────────────────────────────────────────────
def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1-8: Abacus Calc 6-row, 2-digit
    for pn in range(1, 9):
        page_calc_6row(c, pn, "Abacus Calculation")
        c.showPage()
    # p9: Mental Calc 6-row
    page_calc_6row(c, 9, "Mental Calculation"); c.showPage()
    # p10-15: Mixed Mental/Abacus 6-row
    for pn in range(10, 16):
        title = "Mental Calculation" if pn % 2 == 0 else "Abacus Calculation"
        page_calc_6row(c, pn, title, time_limit="5 Mins" if pn >= 14 else "10 Mins")
        c.showPage()
    # p16: Multiplication ×2 visual
    page_mult_visual(c, 16, 2, fn=draw_apple); c.showPage()
    # p17: Multiplication test A/B/C/D
    page_mult_test(c, 17); c.showPage()
    # p18: Multiplication ×3 visual
    page_mult_visual(c, 18, 3, fn=draw_strawberry); c.showPage()
    # p19: Multiplication ×4 visual
    page_mult_visual(c, 19, 4, fn=draw_fish); c.showPage()
    # p20-24: Abacus Calc 3-digit (2-row)
    for pn in range(20, 25):
        page_calc_3digit(c, pn, "Abacus Calculation (3-digit)")
        c.showPage()
    # p25: Multiplication revision
    page_mult_revision(c, 25); c.showPage()
    # p26: Mental Calc 6-row
    page_calc_6row(c, 26, "Mental Calculation"); c.showPage()
    # p27: Multiplication ×5 visual
    page_mult_visual(c, 27, 5, fn=draw_flower); c.showPage()
    # p28-33: Mixed Calc
    for pn in range(28, 34):
        if pn in [30, 33]:
            page_calc_3digit(c, pn, "Abacus Calculation (3-digit)")
        else:
            title = "Mental Calculation" if pn % 2 == 0 else "Abacus Calculation"
            page_calc_6row(c, pn, title)
        c.showPage()
    # p34: Multiplication ×6 visual
    page_mult_visual(c, 34, 6, fn=draw_mango); c.showPage()
    # p35: Multiplication test
    page_mult_test(c, 35); c.showPage()
    # p36-41: Mental Calc series with Time Limit: 5 Mins
    for pn in range(36, 42):
        page_calc_6row(c, pn, "Mental Calculation", time_limit="5 Mins")
        c.showPage()
    # p42: Final assessment
    page_42(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 43 (cover + 42)")


if __name__ == "__main__":
    main()
