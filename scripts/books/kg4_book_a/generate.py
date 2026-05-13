#!/usr/bin/env python3
"""
Speedy Scholars — KG-4 Book A Workbook Generator
Calculation-drilling book: Mental Calc + Abacus Calc with 2-digit numbers
and an intro to multiplication tables. 39 pages (cover + 38).
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

set_book("KG-4 Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG4-Book-A.pdf")


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
        random.seed(i + 600)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-4  BOOK A")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Mental Calculation & Multiplication Intro")
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


# ─── PROGRAMMATIC DATA GEN ────────────────────────────────────────────────
# Per-book seed offset (set by importing books)
BOOK_SEED_OFFSET = 0

def set_seed_offset(n):
    global BOOK_SEED_OFFSET
    BOOK_SEED_OFFSET = n


def gen_calc_data(pn, num_cols=20, num_rows=3, start_lo=10, start_hi=99,
                  op_max=9, op_2digit=False):
    """Generate num_cols columns × num_rows operations, deterministic per page."""
    random.seed(pn * 13 + 7 + BOOK_SEED_OFFSET)
    cols = []
    for c in range(num_cols):
        attempts = 0
        while attempts < 50:
            start = random.randint(start_lo, start_hi)
            ops = []
            val = start
            ok = True
            for r in range(num_rows - 1):
                if op_2digit:
                    delta = random.choice([-1, 1]) * random.randint(10, 49)
                else:
                    delta = random.choice([-1, 1]) * random.randint(1, op_max)
                if 0 <= val + delta <= 99:
                    val += delta
                    ops.append(delta)
                else:
                    delta = -delta
                    if 0 <= val + delta <= 99:
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
            cols.append([start_lo, 1, 1][:num_rows])
    return cols


def gen_sums_data(pn, num_problems=6, num_lines=4, val_lo=10, val_hi=99):
    """Generate multi-line sums for the bottom of certain pages."""
    random.seed(pn * 19 + 23 + BOOK_SEED_OFFSET)
    problems = []
    for p in range(num_problems):
        vals = []
        for _ in range(num_lines):
            vals.append(random.randint(val_lo, val_hi))
        # Optional: random sign per term (after first)
        signs = ["+"] + [random.choice(["+", "+", "+", "−"]) for _ in range(num_lines - 1)]
        problems.append(list(zip(signs, vals)))
    return problems


# ─── PAGE: 20-COLUMN CALC GRID ───────────────────────────────────────────
def page_calc_grid(c, pn, title, num_rows=3, with_sums=False, op_2digit=False):
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)

    # 2 stacked tables of 10 cols each + optionally 1 more row of 10 cols
    rows_to_show = 2  # 2 sub-tables stacked, each with 10 columns
    cols_per_table = 10
    tables = []
    cols_data = gen_calc_data(pn, num_cols=cols_per_table * rows_to_show,
                              num_rows=num_rows, op_2digit=op_2digit)
    for k in range(rows_to_show):
        tables.append(cols_data[k * cols_per_table:(k + 1) * cols_per_table])

    cur_y = y
    block_h = 70 if not with_sums else 60
    for ti, table_data in enumerate(tables):
        cur_y = _draw_grid_table(c, MARGIN, cur_y, table_data, num_rows=num_rows)
        cur_y -= 12

    # Sometimes a 3rd row of 10 cols
    if rows_to_show * cols_per_table < 20:
        third = cols_data[20:30]
        cur_y = _draw_grid_table(c, MARGIN, cur_y, third, num_rows=num_rows)
        cur_y -= 12

    if with_sums:
        # 6 multi-line sums in two columns of 3
        sums = gen_sums_data(pn, num_problems=6, num_lines=4)
        sums_y_top = cur_y - 6
        sums_y_bot = 22 * mm + 8
        col_w = CW / 2
        for i, terms in enumerate(sums):
            col = i % 2; row = i // 2
            sx = MARGIN + col * col_w + 20
            sy = sums_y_top - (row + 1) * ((sums_y_top - sums_y_bot) / 3) + 14
            c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
            c.drawString(sx - 14, sy, f"{i+1}.")
            line_text = "  ".join(f"{s if s == '−' else '+'} {v}" if k > 0 else str(v)
                                  for k, (s, v) in enumerate(terms)) + "  ="
            # Just print as single line for simplicity
            c.setFont("Helvetica", 11); c.setFillColor(DARKER_BROWN)
            c.drawString(sx, sy, " ".join(str(v) if k == 0 else f"{s}{v}"
                                          for k, (s, v) in enumerate(terms)) + " =")
            # Answer line
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.6)
            c.line(sx + 160, sy - 2, sx + 220, sy - 2)


def _draw_grid_table(c, x, y, table_data, num_rows=3):
    """Draw a 10-col table with given rows. Returns y below table."""
    cols = len(table_data)
    rh = 16; sw = 26
    cw = (CW - sw) / cols
    hf = 9
    hy = y - rh
    c.setFillColor(BROWN); c.rect(x, hy, sw, rh, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + sw / 2, hy + 4, "S.No.")
    for i in range(cols):
        cx = x + sw + i * cw
        c.setFillColor(BROWN); c.rect(cx, hy, cw, rh, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + cw / 2, hy + 4, str(i + 1))

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
        c.drawCentredString(x + sw / 2, ry + 4, lab)
        for i in range(cols):
            cx = x + sw + i * cw
            c.setFillColor(TH if is_ans else TF)
            c.rect(cx, ry, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3)
            c.rect(cx, ry, cw, rh, stroke=1, fill=0)
            if not is_ans and i < len(table_data) and ri < len(table_data[i]):
                v = table_data[i][ri]
                if v is not None:
                    c.setFillColor(DARKER_BROWN); c.setFont("Helvetica", 10)
                    s = str(v)  # no + sign for positive operands (abacus convention)
                    c.drawCentredString(cx + cw / 2, ry + 4, s)
    return hy - (num_rows + 1) * rh - 4


# ─── PAGE: MULTIPLICATION TABLE ──────────────────────────────────────────
def page_multiplication(c, pn, factor, with_addition_equivalents=True):
    bg(c); y = draw_hdr(c, f"Multiplication × {factor}",
                        "Each multiplication is repeated addition"); draw_footer(c, pn)
    scatter_decorations(c, pn)

    # Three columns of multiplications
    # Col 1: 0×N, 1×N, ..., 9×N
    # Col 2: 9×N, 8×N, ..., 0×N (shuffled or reversed)
    # Col 3: 7×N, 2×N, 0×N, ... (random shuffle)
    col_data = [list(range(10)), list(range(9, -1, -1))]
    random.seed(pn + 50)
    third = list(range(10)); random.shuffle(third)
    col_data.append(third)

    col_w = CW / 4
    cell_h = (y - 26 * mm - 8) / 10

    for ci, col in enumerate(col_data):
        cx = MARGIN + ci * col_w + 16
        for ri, k in enumerate(col):
            cy = y - (ri + 1) * cell_h
            # Outline cell
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
            c.roundRect(cx, cy, col_w - 30, cell_h - 6, 3, stroke=1, fill=1)
            c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
            # Alternate ordering
            if ci == 0:
                expr = f"{k} × {factor}  ="
            elif ci == 1:
                expr = f"{factor} × {k}  ="
            else:
                expr = f"{k} × {factor}  =" if ri % 2 == 0 else f"{factor} × {k}  ="
            c.drawString(cx + 10, cy + cell_h / 2 - 6, expr)

    # 4th column: addition equivalents
    if with_addition_equivalents:
        ax = MARGIN + 3 * col_w + 16
        # Show equivalents like "3+3+3 = 3×3" — connect the dots
        equivs = [(f"{factor}+{factor} =", f"{factor}×2"),
                  (f"{factor}+{factor}+{factor} =", f"{factor}×3"),
                  (f"{factor}+{factor}+{factor}+{factor} =", f"{factor}×4"),
                  (f"{factor}+{factor}+{factor}+{factor}+{factor} =", f"{factor}×5"),
                  (f"{factor}×6", f"{factor}+{factor}+{factor}+{factor}+{factor}+{factor} =")]
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(ax, y - 16, "Addition equivalents:")
        for ri, (a, b) in enumerate(equivs):
            cy = y - 32 - ri * (cell_h * 1.6)
            c.setFont("Helvetica", 10); c.setFillColor(BROWN)
            c.drawString(ax, cy, a)
            c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
            c.drawString(ax, cy - 14, b)


# ─── PAGE: FINAL ASSESSMENT ──────────────────────────────────────────────
def page_38(c):
    bg(c); y = draw_hdr(c, "Final Mental Calculation Assessment",
                        "Last test — show what you've mastered"); draw_footer(c, 38)
    scatter_decorations(c, 38)
    # Same as regular calc grid but framed
    cols_data = gen_calc_data(38, num_cols=20, num_rows=3)
    cur_y = y
    for k in range(2):
        block = cols_data[k * 10:(k + 1) * 10]
        cur_y = _draw_grid_table(c, MARGIN, cur_y, block)
        cur_y -= 12


# ─── MAIN ────────────────────────────────────────────────────────────────
def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()

    # p1-11: Mental Calculation grids
    for pn in range(1, 12):
        title = "Mental Calculation" if pn % 2 == 1 else "Abacus Calculation"
        page_calc_grid(c, pn, title)
        c.showPage()

    # p12: Abacus Calc with bottom sums
    page_calc_grid(c, 12, "Abacus Calculation", with_sums=True)
    c.showPage()

    # p13-17: Mixed
    for pn in [13, 14, 15, 16, 17]:
        title = "Mental Calculation" if pn % 2 == 1 else "Abacus Calculation"
        page_calc_grid(c, pn, title)
        c.showPage()

    # p18, 19: Multiplication × 0 / × 1
    page_multiplication(c, 18, 0); c.showPage()
    page_multiplication(c, 19, 1); c.showPage()

    # p20-24: Abacus Calc + sums
    for pn in [20, 21, 22, 23, 24]:
        page_calc_grid(c, pn, "Abacus Calculation", with_sums=(pn in [21, 24]))
        c.showPage()

    # p25-27: Mental Calc
    for pn in [25, 26, 27]:
        page_calc_grid(c, pn, "Mental Calculation")
        c.showPage()

    # p28: Multiplication × 3
    page_multiplication(c, 28, 3); c.showPage()

    # p29-31: Abacus Calc
    for pn in [29, 30, 31]:
        page_calc_grid(c, pn, "Abacus Calculation", with_sums=(pn == 30))
        c.showPage()

    # p32-37: Mental Calc
    for pn in [32, 33, 34, 35, 36, 37]:
        page_calc_grid(c, pn, "Mental Calculation")
        c.showPage()

    # p38: Final assessment
    page_38(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 39 (cover + 38)")


if __name__ == "__main__":
    main()
