#!/usr/bin/env python3
"""
Speedy Scholars — KG-2 Book B Workbook Generator
Sequel to KG-2 Book A. Decomposition of 10 (teen − single-digit) and
Combination of 10 two-step subtraction tricks. 39 pages (cover + 38).
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

set_book("KG-2 Book B")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG2-Book-B.pdf")


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
        random.seed(i + 500)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-2  BOOK B")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Decomposition of 10 & Big/Small Friends")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 90 * mm, H - 137 * mm, W / 2 + 90 * mm, H - 137 * mm)
    for i, (u, l, lb) in enumerate([(1, 3, "8"), (1, 4, "9"), (1, 0, "5")]):
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


# ─── PAGE 1: VISUAL SUBTRACTION CARDS ────────────────────────────────────
def page_01(c):
    bg(c); y = draw_hdr(c, "Combination of Big & Small Friends",
                        "Teen − single rewrites as − 10 + (10 − single)"); draw_footer(c, 1)
    scatter_decorations(c, 1)

    problems = [(13, 8, 5, "13 − 8 : 13 − 10 + 2 = ( )", draw_apple),
                (14, 9, 5, "14 − 9 : 14 − 10 + 1 = ( )", draw_strawberry)]

    avail_h = y - 18 * mm - 8
    card_h = avail_h / 2 - 8
    obj_s = 16

    for i, (a, b, ans, formula, fn) in enumerate(problems):
        cy = y - (i + 1) * (card_h + 8) + 8

        left_w = CW - 110
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(MARGIN, cy, left_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 16, cy + card_h - 20, formula)

        # Top group of `a` objects (single row, all)
        obj_sp = obj_s + 4
        oy = cy + card_h * 0.42
        for j in range(a):
            fn(c, MARGIN + 20 + j * obj_sp, oy, size=obj_s)
        # Red X overlay on the last b objects (visualizing the subtraction)
        c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(1.8)
        x_size = obj_s * 0.45
        for j in range(a - b, a):
            ox = MARGIN + 20 + j * obj_sp
            c.line(ox - x_size, oy - x_size, ox + x_size, oy + x_size)
            c.line(ox - x_size, oy + x_size, ox + x_size, oy - x_size)

        # Right: vertical subtraction
        rs_x = MARGIN + left_w + 12
        rs_w = CW - left_w - 12
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(rs_x, cy, rs_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 26); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 36, str(a))
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 68, f"− {b}")
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(rs_x + 14, cy + card_h - 84, rs_x + rs_w - 14, cy + card_h - 84)
        c.setFillColor(white); c.setStrokeColor(GOLD)
        c.rect(rs_x + rs_w / 2 - 22, cy + 14, 44, 28, stroke=1, fill=1)


# ─── PAGE 2: PYRAMID GRID OF SUBTRACTIONS ────────────────────────────────
def page_02(c):
    bg(c); y = draw_hdr(c, "Decomposition Pyramid",
                        "Solve every subtraction problem in the staircase"); draw_footer(c, 2)
    scatter_decorations(c, 2)

    # Row n = subtraction by n+1, columns expand to right
    # Row 0: 10-1
    # Row 1: 10-2, 11-2
    # Row 8: 10-9, 11-9, ..., 18-9
    rows = 9
    grid_x = MARGIN + 30
    grid_y_top = y - 8
    grid_h = grid_y_top - 22 * mm - 8
    grid_w = CW - 60
    cell_w = grid_w / rows
    cell_h = grid_h / rows

    for r in range(rows):
        for col in range(r + 1):
            a = 10 + col
            b = r + 1
            cx = grid_x + col * cell_w
            cy = grid_y_top - (r + 1) * cell_h
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
            c.roundRect(cx, cy, cell_w - 2, cell_h - 2, 2, stroke=1, fill=1)
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 9.5)
            c.drawCentredString(cx + (cell_w - 2) / 2, cy + (cell_h - 2) / 2 - 3,
                                f"{a}−{b}")

    # Mascots
    draw_bead_bird(c, W - 60 * mm, y - 80, 24, GOLD, "left", "happy", hat="graduation")


# ─── PAGE 9: VISUAL SUBTRACTION CARDS (−6 with mascots) ──────────────────
def page_09(c):
    bg(c); y = draw_hdr(c, "Visual Subtraction",
                        "Subtract 6 from each — what is left?"); draw_footer(c, 9)
    scatter_decorations(c, 9)

    problems = [(11, 6, 5, draw_apple), (13, 6, 7, draw_fish),
                (16, 6, 10, draw_flower), (15, 6, 9, draw_strawberry)]

    avail_h = y - 18 * mm - 8
    cols = 2; rows = 2
    card_w = CW / cols - 8
    card_h = avail_h / rows - 6

    for i, (a, b, _ans, fn) in enumerate(problems):
        col = i % cols; row = i // cols
        bx = MARGIN + col * (card_w + 8)
        by = y - (row + 1) * (card_h + 6) + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(bx, by, card_w, card_h, 4, stroke=1, fill=1)

        # Objects (all a) with last b X'd out
        obj_s = 14
        obj_sp = obj_s + 4
        oy = by + card_h * 0.55
        total_w = a * obj_sp
        start_x = bx + (card_w - total_w) / 2
        for j in range(a):
            fn(c, start_x + j * obj_sp, oy, size=obj_s)
        c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(1.6)
        xs = obj_s * 0.45
        for j in range(a - b, a):
            ox = start_x + j * obj_sp
            c.line(ox - xs, oy - xs, ox + xs, oy + xs)
            c.line(ox - xs, oy + xs, ox + xs, oy - xs)

        # Equation + answer box
        c.setFont("Helvetica-Bold", 16); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + card_w / 2 - 28, by + 18, f"{a} − {b} =")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(bx + card_w / 2 + 32, by + 12, 30, 22, stroke=1, fill=1)


# ─── PAGE 10: VISUAL CARDS (10-6 and 15-6) ───────────────────────────────
def page_10(c):
    bg(c); y = draw_hdr(c, "Visual Subtraction",
                        "Different starting numbers, same trick"); draw_footer(c, 10)
    scatter_decorations(c, 10)

    problems = [(10, 6, 4, "10 − 6 : 10 − 10 + 4 = ( )", draw_apple),
                (15, 6, 9, "15 − 6 : 15 − 10 + 4 = ( )", draw_strawberry)]

    avail_h = y - 18 * mm - 8
    card_h = avail_h / 2 - 8
    obj_s = 16

    for i, (a, b, _ans, formula, fn) in enumerate(problems):
        cy = y - (i + 1) * (card_h + 8) + 8
        left_w = CW - 110
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(MARGIN, cy, left_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 16, cy + card_h - 20, formula)
        obj_sp = obj_s + 4
        oy = cy + card_h * 0.42
        for j in range(a):
            fn(c, MARGIN + 20 + j * obj_sp, oy, size=obj_s)
        c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(1.8)
        xs = obj_s * 0.45
        for j in range(a - b, a):
            ox = MARGIN + 20 + j * obj_sp
            c.line(ox - xs, oy - xs, ox + xs, oy + xs)
            c.line(ox - xs, oy + xs, ox + xs, oy - xs)
        # Right vertical
        rs_x = MARGIN + left_w + 12
        rs_w = CW - left_w - 12
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(rs_x, cy, rs_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 26); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 36, str(a))
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 68, f"− {b}")
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(rs_x + 14, cy + card_h - 84, rs_x + rs_w - 14, cy + card_h - 84)
        c.setFillColor(white); c.setStrokeColor(GOLD)
        c.rect(rs_x + rs_w / 2 - 22, cy + 14, 44, 28, stroke=1, fill=1)


# ─── PAGE 13: VISUAL CARDS (3 small) ─────────────────────────────────────
def page_13(c):
    bg(c); y = draw_hdr(c, "Visual Subtraction Cards",
                        "Three more subtraction tricks"); draw_footer(c, 13)
    scatter_decorations(c, 13)

    problems = [(13, 5, 8, "13 − 5 : 13 − 10 + 5", draw_apple),
                (11, 4, 7, "11 − 4 : 11 − 10 + 6", draw_strawberry),
                (12, 3, 9, "12 − 3 : 12 − 10 + 7", draw_fish)]

    avail_h = y - 18 * mm - 8
    cols = 3
    card_w = CW / cols - 8
    card_h = avail_h - 8
    obj_s = 14

    for i, (a, b, _ans, formula, fn) in enumerate(problems):
        bx = MARGIN + i * (card_w + 8)
        by = 22 * mm + 12
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(bx, by, card_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + 10, by + card_h - 22, formula)

        # Object grid: up to 6 per row, two rows if needed
        obj_sp = obj_s + 4
        per_row = 6
        rows_needed = (a + per_row - 1) // per_row
        for j in range(a):
            r = j // per_row; col = j % per_row
            ox = bx + 14 + col * obj_sp
            oy = by + card_h * 0.55 - r * (obj_s + 4)
            fn(c, ox, oy, size=obj_s)
            if j >= a - b:
                c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(1.4)
                xs = obj_s * 0.4
                c.line(ox - xs, oy - xs, ox + xs, oy + xs)
                c.line(ox - xs, oy + xs, ox + xs, oy - xs)

        # Vertical sum at bottom
        c.setFont("Helvetica-Bold", 18); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + 10, by + 30, str(a))
        c.drawString(bx + 10, by + 14, f"− {b}")
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.8)
        c.line(bx + 10, by + 10, bx + 60, by + 10)


# ─── PAGE 22: MASCOT-TO-HOUSE MATCH (interest page) ──────────────────────
def page_22(c):
    bg(c); y = draw_hdr(c, "Match the Mascot to its House",
                        "Each mascot's problem solves to a house number"); draw_footer(c, 22)
    scatter_decorations(c, 22)

    problems = [(14, 6, 8), (13, 5, 8), (12, 4, 8), (11, 3, 8),
                (15, 7, 8), (16, 8, 8), (17, 9, 8), (10, 2, 8)]
    # Houses with various numbers; some duplicate target answers
    houses = [8, 5, 7, 9, 6, 10, 11, 4]

    avail_h = y - 18 * mm - 8
    left_x = MARGIN + 10
    left_w = CW * 0.45
    right_x = MARGIN + left_w + 30
    right_w = CW - left_w - 30

    # Left: 8 mascots+problems in a 2-col × 4-row grid
    cols = 2; rows = 4
    cell_w = left_w / cols
    cell_h = avail_h / rows
    for i, (a, b, _ans) in enumerate(problems):
        col = i % cols; row = i // cols
        mx = left_x + col * cell_w + cell_w / 2
        my = y - (row + 1) * cell_h + cell_h / 2
        col_choice = [GOLD, BROWN, LIGHT_GOLD, LIGHT_BROWN][i % 4]
        draw_bead_bird(c, mx, my + 14, 20, col_choice, "right",
                       ["happy", "wink", "surprised", "thinking"][i % 4],
                       hat="graduation")
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(mx - 30, my - 18, 60, 18, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(mx, my - 11, f"{a} − {b}")

    # Right: 8 houses in 4×2 grid
    h_cols = 4; h_rows = 2
    h_cell_w = right_w / h_cols
    h_cell_h = avail_h / h_rows
    for i, n in enumerate(houses):
        col = i % h_cols; row = i // h_cols
        hx = right_x + col * h_cell_w + h_cell_w / 2
        hy = y - (row + 1) * h_cell_h + h_cell_h / 2
        hw = 50; hh = 42
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.rect(hx - hw / 2, hy - hh / 2, hw, hh, stroke=1, fill=1)
        # Roof
        c.setFillColor(BROWN)
        p = c.beginPath()
        p.moveTo(hx - hw / 2 - 4, hy + hh / 2)
        p.lineTo(hx, hy + hh / 2 + 18)
        p.lineTo(hx + hw / 2 + 4, hy + hh / 2)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        # Number
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(hx, hy + hh / 2 + 2, str(n))


# ─── PAGE 24: COUNT-AND-WRITE STYLE INTEREST PAGE ────────────────────────
def page_24(c):
    bg(c); y = draw_hdr(c, "Count and Subtract",
                        "Cross out the smaller group and write the difference"); draw_footer(c, 24)
    scatter_decorations(c, 24)

    problems = [(12, 4, 8, draw_apple), (15, 7, 8, draw_strawberry),
                (14, 5, 9, draw_fish), (16, 8, 8, draw_flower),
                (13, 6, 7, draw_butterfly), (11, 2, 9, draw_mango)]

    avail_h = y - 18 * mm - 8
    cols = 3; rows = 2
    card_w = CW / cols - 8
    card_h = avail_h / rows - 6
    obj_s = 12

    for i, (a, b, _ans, fn) in enumerate(problems):
        col = i % cols; row = i // cols
        bx = MARGIN + col * (card_w + 8)
        by = y - (row + 1) * (card_h + 6) + 6
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(bx, by, card_w, card_h, 4, stroke=1, fill=1)

        # Objects: up to 8 per row
        obj_sp = obj_s + 3
        per_row = 8
        for j in range(a):
            r = j // per_row; col2 = j % per_row
            ox = bx + 16 + col2 * obj_sp
            oy = by + card_h * 0.65 - r * (obj_s + 3)
            fn(c, ox, oy, size=obj_s)
            if j >= a - b:
                c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(1.2)
                xs = obj_s * 0.4
                c.line(ox - xs, oy - xs, ox + xs, oy + xs)
                c.line(ox - xs, oy + xs, ox + xs, oy - xs)

        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(bx + card_w / 2 - 18, by + 12, f"{a} − {b} =")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(bx + card_w / 2 + 14, by + 8, 28, 20, stroke=1, fill=1)


# ─── PAGE 36: CARRY-FORWARD INTRO ────────────────────────────────────────
def page_36(c):
    bg(c); y = draw_hdr(c, "Two-Digit Addition: Carrying Forward",
                        "Now let's apply the trick to bigger numbers"); draw_footer(c, 36)
    scatter_decorations(c, 36)

    # Featured mascot with thought bubble
    draw_bead_bird(c, MARGIN + 50, y - 80, 40, GOLD, "right", "thinking", hat="graduation")
    bub_x = MARGIN + 110
    bub_y = y - 60
    c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
    c.roundRect(bub_x, bub_y - 50, 190, 60, 8, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(bub_x + 10, bub_y - 8, "Have you learned how to")
    c.drawString(bub_x + 10, bub_y - 22, "carry-forward a digit?")
    c.drawString(bub_x + 10, bub_y - 36, "Now do it for double digits!")

    # Right: number column showing 100 broken into 99/98/.../91 + 1/2/.../9
    col_x = MARGIN + 320
    col_y = y - 30
    c.setFont("Helvetica-Bold", 13); c.setFillColor(GOLD)
    c.drawCentredString(col_x + 30, col_y, "100")
    # Vertical bracket
    c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
    c.line(col_x, col_y - 6, col_x + 60, col_y - 6)
    rows_data = [(1, 99), (2, 98), (3, 97), (4, 96), (5, 95),
                 (6, 94), (7, 93), (8, 92), (9, 91)]
    for i, (a, b) in enumerate(rows_data):
        ry = col_y - 22 - i * 13
        c.setFont("Helvetica", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(col_x, ry, str(a))
        c.drawString(col_x + 36, ry, str(b))

    # Right side: two worked examples
    ex_x = MARGIN + 460
    c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
    c.drawString(ex_x, y - 30, "29 + 61 = 90")
    # Mini abacus illustration (two-digit)
    draw_abacus(c, ex_x, y - 130, 100, 80, 0, 0)  # blank placeholder
    c.drawString(ex_x, y - 160, "47 + 53 = 100")
    draw_abacus(c, ex_x, y - 260, 100, 80, 0, 0)


# ─── PAGE 38: FINAL ASSESSMENT (4 sections) ──────────────────────────────
def page_38(c):
    bg(c); y = draw_hdr(c, "Final Assessment",
                        "Sections B, C, D — show what you have learned"); draw_footer(c, 38)
    scatter_decorations(c, 38)

    # Time line in top right (just a label)
    c.setFont("Helvetica-Bold", 9); c.setFillColor(BROWN)
    c.drawRightString(W - MARGIN - 30, y - 4, "Time:  _________")

    # Section B: 10-col abacus calc, 3 rows
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y - 16, "Section B — Abacus Calculation")
    y2 = y - 22
    data_b = [[18,-5,-4],[21,4,3],[30,-8,-9],[28,-4,6],[17,6,-7],[25,4,2],[16,5,8],[12,9,-6]]
    y2 = draw_calc_table(c, MARGIN, y2, data_b, len(data_b), None, table_width=CW)

    # Section C: 10-col mental calc
    y2 -= 20
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y2, "Section C — Mental Calculation")
    y2 -= 6
    data_c = [[9,-3,2],[7,-3,5],[4,5,-2],[6,2,-1],[5,-2,8],[8,2,-7],[2,7,-3],[9,-7,5],[3,9,-2],[6,-5,9]]
    y2 = draw_calc_table(c, MARGIN, y2, data_c, len(data_c), None, table_width=CW)

    # Section D: Fill in combination/decomposition (number bonds)
    y2 -= 18
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y2, "Section D — Fill in the Combination & Decomposition Number")
    y2 -= 6
    band_h = y2 - 22 * mm - 8
    bonds = [(10, 8, "?"), (10, "?", 4), (10, 5, "?"), (10, "?", 7),
             (10, 3, "?"), (10, "?", 9), (5, "?", 4), (5, 2, "?"),
             (5, "?", 1), (5, 3, "?")]
    cols = 5
    cell_w = CW / cols
    for i, (total, l, r) in enumerate(bonds):
        col = i % cols; row = i // cols
        cx = MARGIN + col * cell_w + cell_w / 2
        cy = 22 * mm + 8 + (1 - row) * (band_h / 2) - 10
        # Total on top
        c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.8)
        c.circle(cx, cy + 20, 11, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(cx, cy + 17, str(total))
        # Branches
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
        c.line(cx - 4, cy + 12, cx - 16, cy - 6)
        c.line(cx + 4, cy + 12, cx + 16, cy - 6)
        # Left + right child
        for side, val in [(-16, l), (16, r)]:
            c.setFillColor(LIGHT_GOLD if val != "?" else white)
            c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
            c.circle(cx + side, cy - 14, 9, stroke=1, fill=1)
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 10)
            c.drawCentredString(cx + side, cy - 17, str(val))


# ─── CALC PAGE + MENTAL PAGE (same as KG-2 Book A) ───────────────────────
BOTTOM_STRIP_SETS = {
    3:  [(11,"−",9,draw_apple),  (12,"−",9,draw_strawberry),(13,"−",9,draw_fish), (14,"−",9,draw_flower)],
    4:  [(11,"−",8,draw_apple),  (13,"−",7,draw_strawberry),(15,"−",6,draw_fish), (12,"−",9,draw_flower)],
    5:  [(11,"−",8,draw_apple),  (13,"−",8,draw_strawberry),(14,"−",8,draw_fish), (12,"−",8,draw_flower)],
    6:  [(15,"−",7,draw_apple),  (14,"−",6,draw_strawberry),(11,"−",5,draw_fish), (12,"−",4,draw_flower)],
    7:  [(13,"−",4,draw_apple),  (16,"−",9,draw_strawberry),(15,"−",8,draw_fish), (14,"−",7,draw_flower)],
    8:  [(11,"−",7,draw_apple),  (13,"−",7,draw_strawberry),(15,"−",7,draw_fish), (12,"−",7,draw_flower)],
    11: [(10,"−",6,draw_apple),  (12,"−",6,draw_strawberry),(14,"−",6,draw_fish), (15,"−",6,draw_flower)],
    12: [(10,"−",5,draw_apple),  (12,"−",5,draw_strawberry),(11,"−",4,draw_fish), (13,"−",3,draw_flower)],
    14: [(10,"−",5,draw_apple),  (11,"−",5,draw_strawberry),(12,"−",5,draw_fish), (13,"−",5,draw_flower)],
    15: [(10,"−",4,draw_apple),  (11,"−",4,draw_strawberry),(12,"−",4,draw_fish), (13,"−",4,draw_flower)],
    16: [(15,"−",3,draw_apple),  (14,"−",4,draw_strawberry),(13,"−",5,draw_fish), (12,"−",6,draw_flower)],
    17: [(16,"−",7,draw_apple),  (15,"−",8,draw_strawberry),(14,"−",9,draw_fish), (13,"−",4,draw_flower)],
    18: [(10,"−",4,draw_apple),  (11,"−",4,draw_strawberry),(12,"−",4,draw_fish), (13,"−",4,draw_flower)],
    19: [(14,"−",5,draw_apple),  (15,"−",6,draw_strawberry),(13,"−",4,draw_fish), (12,"−",3,draw_flower)],
    20: [(11,"−",2,draw_apple),  (12,"−",3,draw_strawberry),(13,"−",4,draw_fish), (14,"−",5,draw_flower)],
    21: [(15,"−",5,draw_apple),  (16,"−",6,draw_strawberry),(13,"−",3,draw_fish), (14,"−",4,draw_flower)],
    25: [(14,"−",9,draw_apple),  (15,"−",9,draw_strawberry),(16,"−",9,draw_fish), (13,"−",9,draw_flower)],
    26: [(13,"−",8,draw_apple),  (12,"−",7,draw_strawberry),(14,"−",8,draw_fish), (15,"−",8,draw_flower)],
    27: [(13,"−",8,draw_apple),  (14,"−",8,draw_strawberry),(15,"−",8,draw_fish), (16,"−",8,draw_flower)],
    28: [(13,"−",7,draw_apple),  (14,"−",7,draw_strawberry),(15,"−",7,draw_fish), (16,"−",7,draw_flower)],
    29: [(12,"−",7,draw_apple),  (13,"−",7,draw_strawberry),(14,"−",7,draw_fish), (15,"−",7,draw_flower)],
    30: [(12,"−",7,draw_apple),  (13,"−",7,draw_strawberry),(15,"−",7,draw_fish), (16,"−",7,draw_flower)],
    31: [(11,"−",6,draw_apple),  (12,"−",6,draw_strawberry),(13,"−",6,draw_fish), (15,"−",6,draw_flower)],
    32: [(11,"−",6,draw_apple),  (12,"−",6,draw_strawberry),(13,"−",6,draw_fish), (15,"−",6,draw_flower)],
    33: [(13,"−",5,draw_apple),  (14,"−",6,draw_strawberry),(15,"−",7,draw_fish), (12,"−",4,draw_flower)],
    34: [(11,"−",7,draw_apple),  (12,"−",8,draw_strawberry),(13,"−",9,draw_fish), (14,"−",5,draw_flower)],
}


def page_calc(c, pn, title, formula, fingering, tables, mini_diagram=None, wide=False):
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)
    header_parts = []
    if formula: header_parts.append(formula)
    if fingering: header_parts.append(fingering)
    if header_parts:
        c.setFont("Helvetica", 8); c.setFillColor(BROWN)
        c.drawString(MARGIN, y - 2, "    ".join(header_parts))
        y -= 10
    if wide:
        for table_data in tables:
            cols = len(table_data)
            y = draw_calc_table(c, MARGIN, y, table_data, cols, None, table_width=CW)
            y -= 10
        return
    for table_data in tables:
        cols = len(table_data)
        y = draw_calc_table(c, MARGIN, y, table_data, cols, None, table_width=CW)
        y -= 8
    strip_y = 18 * mm
    strip_h = y - strip_y - 4
    if strip_h < 25: strip_h = 25
    strip_set = BOTTOM_STRIP_SETS.get(pn, [(10,"−",5,draw_apple)] * 4)
    num_cards = 4
    card_w = CW / num_cards
    for i in range(num_cards):
        px = MARGIN + i * card_w
        pw = card_w - 4
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(px, strip_y, pw, strip_h, 3, stroke=1, fill=1)
        if mini_diagram and i == num_cards - 1:
            _draw_mini_trick(c, px, strip_y, pw, strip_h, mini_diagram)
            continue
        a, op, b, fn = strip_set[i]
        # For subtraction in strip: draw `a` objects, cross out last `b`
        total_count = a
        obj_s = min(11, strip_h * 0.24, (pw - 30) / max(total_count, 1) - 1)
        obj_s = max(obj_s, 6)
        obj_y = strip_y + strip_h * 0.62
        obj_sp = obj_s + 1.5
        total_w = a * obj_sp
        start_x = px + max(6, (pw - total_w) / 2)
        for j in range(a):
            ox = start_x + j * obj_sp
            try: fn(c, ox, obj_y, size=obj_s)
            except: fn(c, ox, obj_y)
            if j >= a - b and op == "−":
                c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(1)
                xs = obj_s * 0.4
                c.line(ox - xs, obj_y - xs, ox + xs, obj_y + xs)
                c.line(ox - xs, obj_y + xs, ox + xs, obj_y - xs)
        c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
        c.drawString(px + 8, strip_y + 5, f"{a} {op} {b} =")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(px + pw - 14 * mm, strip_y + 2, 12 * mm, 12, stroke=1, fill=1)


def _draw_mini_trick(c, px, py, pw, ph, diag):
    c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(px + pw / 2, py + ph - 12, f"{diag['a']} {diag['op']} {diag['b']}")
    c.setFont("Helvetica", 7.5); c.setFillColor(BROWN)
    c.drawCentredString(px + pw / 2, py + ph - 24, f"= {diag['trick']}")
    c.drawCentredString(px + pw / 2, py + ph - 34, f"= {diag['result']}")
    ab_w = 20; ab_h = min(34, ph - 14)
    ab_x = px + pw - ab_w - 6; ab_y = py + 6
    res = diag['result']
    if res <= 9:
        upper = 1 if res >= 5 else 0
        lower = res - 5 if res >= 5 else res
        draw_abacus(c, ab_x, ab_y, ab_w, ab_h, upper, lower)
    else:
        c.setFont("Helvetica-Bold", 13); c.setFillColor(GOLD)
        c.drawCentredString(ab_x + ab_w / 2, ab_y + ab_h / 2 - 4, str(res))


def page_mental(c, pn, title, table_a, table_b=None, listening=False):
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)
    sidebar_w = 60 if listening else 0
    main_w = CW - sidebar_w - (8 if listening else 0)
    y = _draw_mental_block(c, MARGIN, y, "A", table_a, main_w)
    if table_b:
        y -= 18
        y = _draw_mental_block(c, MARGIN, y, "B", table_b, main_w)
    if listening:
        sb_x = MARGIN + main_w + 8
        sb_top = H - 16 * mm - 8
        sb_bot = 18 * mm + 4
        c.setFillColor(LIGHT_GOLD); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(sb_x, sb_bot, sidebar_w, sb_top - sb_bot, 4, stroke=1, fill=1)
        c.setFillColor(BROWN); c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(sb_x + sidebar_w / 2, sb_top - 18, "Listening")
        c.drawCentredString(sb_x + sidebar_w / 2, sb_top - 30, "Exercise")
        line_h = (sb_top - sb_bot - 50) / 10
        for k in range(10):
            ly = sb_top - 50 - (k + 0.5) * line_h
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 9)
            c.drawString(sb_x + 6, ly - 4, str(k + 1))
            c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.5)
            c.line(sb_x + 18, ly - 6, sb_x + sidebar_w - 6, ly - 6)


def _draw_mental_block(c, x, y, label, table, block_w):
    cols = len(table)
    rh = 18; sw = 24
    cw = (block_w - sw) / cols
    hf = 9
    hy = y - rh
    c.setFillColor(BROWN); c.rect(x, hy, sw, rh, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + sw / 2, hy + 5, "S.No.")
    for i in range(cols):
        cx = x + sw + i * cw
        c.setFillColor(BROWN); c.rect(cx, hy, cw, rh, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + cw / 2, hy + 5, str(i + 1))
    labels = ["1", "2", "3", "Ans.", "Ans."]
    for ri, lab in enumerate(labels):
        ry = hy - (ri + 1) * rh
        is_ans = "Ans" in lab
        c.setFillColor(TH if is_ans else TF)
        c.rect(x, ry, sw, rh, stroke=0, fill=1)
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3)
        c.rect(x, ry, sw, rh, stroke=1, fill=0)
        if ri == 0:
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 13)
            c.drawCentredString(x + sw / 2, ry + 5, label)
        elif is_ans:
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", hf)
            c.drawCentredString(x + sw / 2, ry + 5, "Ans.")
        else:
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica", hf)
            c.drawCentredString(x + sw / 2, ry + 5, str(ri + 1))
        for i in range(cols):
            cx = x + sw + i * cw
            c.setFillColor(TH if is_ans else TF)
            c.rect(cx, ry, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3)
            c.rect(cx, ry, cw, rh, stroke=1, fill=0)
            if not is_ans and i < len(table) and ri < len(table[i]) and table[i][ri] is not None:
                v = table[i][ri]
                c.setFillColor(DARKER_BROWN); c.setFont("Helvetica", 10)
                c.drawCentredString(cx + cw / 2, ry + 5,
                                    str(v))  # abacus convention: no + sign
    return hy - 5 * rh - 4


# ─── CALC PAGE DATA ──────────────────────────────────────────────────────
CALC_PAGES = {
    3: dict(title="Abacus Calculation: Decomposition of 10 (−9)",
            formula="−9 = −10 + 1", fingering="Fingering Ex.: 10−9, 11−9, 12−9",
            tables=[[[10,-9,2],[11,-9,3],[12,-9,4],[13,-9,1],[10,-9,5],[11,-9,2],[12,-9,3],[13,-9,4]],
                    [[14,-9,3],[15,-9,2],[16,-9,1],[17,-9,3],[18,-9,2],[11,-9,4],[12,-9,5],[13,-9,6]],
                    [[14,-9,2],[15,-9,3],[16,-9,4],[17,-9,1]]],
            mini_diag={"a":13,"op":"−","b":9,"trick":"13-10+1","result":4}),
    4: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
            tables=[[[12,-9,3],[13,-9,5],[14,-9,2],[15,-9,4],[16,-9,3],[17,-9,2],[10,-9,4],[11,-9,3]],
                    [[18,-9,1],[12,-9,5],[13,-9,2],[14,-9,3],[15,-9,4],[16,-9,2],[10,-9,3],[11,-9,5]],
                    [[12,-9,4],[13,-9,3],[14,-9,2],[15,-9,1]]], mini_diag=None),
    5: dict(title="Abacus Calculation: Decomposition of 10 (−8)",
            formula="−8 = −10 + 2", fingering="Fingering Ex.: 11−8, 13−8, 15−8, 16−8",
            tables=[[[11,-8,3],[12,-8,4],[13,-8,2],[14,-8,5],[15,-8,3],[16,-8,2],[17,-8,4],[18,-8,1]],
                    [[10,-8,5],[12,-8,3],[14,-8,2],[16,-8,4],[11,-8,6],[13,-8,1],[15,-8,5],[17,-8,3]],
                    [[10,-8,4],[12,-8,2],[14,-8,3],[16,-8,1]]],
            mini_diag={"a":11,"op":"−","b":8,"trick":"11-10+2","result":3}),
    6: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
            tables=[[[12,-9,3],[10,-8,4],[11,-9,2],[14,-8,3],[16,-9,4],[15,-8,2],[13,-9,3],[12,-8,5]],
                    [[17,-9,2],[16,-8,3],[15,-9,4],[14,-8,1],[13,-9,5],[12,-8,4],[11,-9,3],[10,-8,2]],
                    [[18,-9,3],[16,-8,1],[14,-9,4],[12,-8,2]]], mini_diag=None),
    7: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
            tables=[[[11,-8,3],[12,-9,2],[13,-8,4],[14,-9,1],[15,-8,3],[16,-9,4],[17,-8,2],[18,-9,3]],
                    [[10,-9,4],[11,-8,5],[12,-9,3],[13,-8,2],[14,-9,4],[15,-8,1],[16,-9,3],[17,-8,5]],
                    [[10,-8,3],[12,-9,2],[14,-8,4],[16,-9,1]]], mini_diag=None),
    8: dict(title="Abacus Calculation: Decomposition of 10 (−7)",
            formula="−7 = −10 + 3", fingering="Fingering Ex.: 11−7, 15−7, 16−7",
            tables=[[[11,-7,4],[12,-7,3],[13,-7,2],[14,-7,5],[15,-7,3],[16,-7,2],[17,-7,4],[18,-7,1]],
                    [[10,-7,5],[12,-7,3],[14,-7,2],[16,-7,4],[11,-7,6],[13,-7,1],[15,-7,5],[17,-7,3]],
                    [[10,-7,4],[12,-7,2],[14,-7,3],[16,-7,1]]],
            mini_diag={"a":11,"op":"−","b":7,"trick":"11-10+3","result":4}),
    11: dict(title="Abacus Calculation: Decomposition of 10 (−6)",
             formula="−6 = −10 + 4", fingering="Fingering Ex.: 10−6, 15−6, 16−6",
             tables=[[[10,-6,2],[11,-6,4],[12,-6,3],[13,-6,5],[14,-6,1],[15,-6,3],[16,-6,2],[17,-6,4]],
                     [[18,-6,5],[12,-6,3],[13,-6,2],[14,-6,5],[15,-6,1],[16,-6,3],[10,-6,4],[11,-6,2]],
                     [[12,-6,5],[13,-6,4],[14,-6,2],[15,-6,3]]],
             mini_diag={"a":15,"op":"−","b":6,"trick":"15-10+4","result":9}),
    12: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[15,-6,3],[16,-7,4],[17,-8,2],[18,-9,1],[14,-6,5],[13,-7,3],[12,-8,4],[11,-9,2]],
                     [[10,-6,4],[11,-7,3],[12,-8,2],[13,-9,1],[14,-6,5],[15,-7,3],[16,-8,4],[17,-9,2]],
                     [[18,-6,5],[16,-7,3],[14,-8,4],[12,-9,2]]], mini_diag=None),
    14: dict(title="Abacus Calculation: Decomposition of 10 (−5)",
             formula="−5 = −10 + 5", fingering="Fingering Ex.: 10−5, 11−5, 12−5",
             tables=[[[10,-5,3],[11,-5,2],[12,-5,4],[13,-5,1],[14,-5,5],[15,-5,3],[16,-5,2],[17,-5,4]],
                     [[18,-5,3],[10,-5,5],[11,-5,4],[12,-5,3],[13,-5,2],[14,-5,1],[15,-5,5],[16,-5,3]],
                     [[10,-5,4],[12,-5,2],[14,-5,3],[16,-5,1]]],
             mini_diag={"a":13,"op":"−","b":5,"trick":"13-10+5","result":8}),
    18: dict(title="Abacus Calculation: Decomposition of 10 (−4)",
             formula="−4 = −10 + 6", fingering="Fingering Ex.: 10−4, 11−4, 12−4",
             tables=[[[10,-4,3],[11,-4,5],[12,-4,2],[13,-4,4],[14,-4,3],[15,-4,1],[16,-4,5],[17,-4,2]],
                     [[18,-4,4],[10,-4,5],[11,-4,3],[12,-4,2],[13,-4,1],[14,-4,5],[15,-4,3],[16,-4,2]],
                     [[10,-4,4],[12,-4,3],[14,-4,2],[16,-4,1]]],
             mini_diag={"a":13,"op":"−","b":4,"trick":"13-10+6","result":9}),
    25: dict(title="Abacus Calculation: Combination of 10 (−9 two-step)",
             formula="−9 = −10 + 5 − 4", fingering="Fingering Ex.: 14−9",
             tables=[[[14,-9,3],[14,-9,5],[14,-9,2],[14,-9,4],[14,-9,1],[14,-9,3],[14,-9,5],[14,-9,2]],
                     [[14,-9,4],[14,-9,3],[14,-9,2],[14,-9,5],[14,-9,1],[14,-9,4],[14,-9,3],[14,-9,2]],
                     [[14,-9,5],[14,-9,4],[14,-9,2],[14,-9,3]]],
             mini_diag={"a":14,"op":"−","b":9,"trick":"14-10+5-4","result":5}),
    27: dict(title="Abacus Calculation: Combination of 10 (−8 two-step)",
             formula="−8 = −10 + 5 − 3", fingering="Fingering Ex.: 13−8, 14−8",
             tables=[[[13,-8,4],[14,-8,3],[13,-8,5],[14,-8,2],[13,-8,1],[14,-8,4],[13,-8,3],[14,-8,5]],
                     [[14,-8,2],[13,-8,4],[14,-8,1],[13,-8,3],[14,-8,5],[13,-8,2],[14,-8,4],[13,-8,3]],
                     [[13,-8,2],[14,-8,5],[13,-8,4],[14,-8,1]]],
             mini_diag={"a":13,"op":"−","b":8,"trick":"13-10+5-3","result":5}),
    29: dict(title="Abacus Calculation: Combination of 10 (−7 two-step)",
             formula="−7 = −10 + 5 − 2", fingering="Fingering Ex.: 12−7, 13−7",
             tables=[[[12,-7,3],[13,-7,5],[12,-7,4],[13,-7,2],[12,-7,1],[13,-7,4],[12,-7,5],[13,-7,3]],
                     [[13,-7,2],[12,-7,4],[13,-7,1],[12,-7,3],[13,-7,5],[12,-7,2],[13,-7,4],[12,-7,3]],
                     [[12,-7,2],[13,-7,5],[12,-7,4],[13,-7,1]]],
             mini_diag={"a":12,"op":"−","b":7,"trick":"12-10+5-2","result":5}),
    30: dict(title="Abacus Calculation: Combination of 10 (−7 cont.)",
             formula="−7 = −10 + 5 − 2", fingering="Fingering Ex.: 12−7, 13−7",
             tables=[[[12,-7,5],[13,-7,3],[12,-7,2],[13,-7,4],[12,-7,3],[13,-7,5],[12,-7,1],[13,-7,2]],
                     [[13,-7,4],[12,-7,3],[13,-7,1],[12,-7,4],[13,-7,2],[12,-7,5],[13,-7,3],[12,-7,4]],
                     [[12,-7,1],[13,-7,4],[12,-7,5],[13,-7,3]]], mini_diag=None),
    32: dict(title="Abacus Calculation: Combination of 10 (−6 two-step)",
             formula="−6 = −10 + 5 − 1", fingering="Fingering Ex.: 11−6, 12−6",
             tables=[[[11,-6,3],[12,-6,5],[11,-6,4],[12,-6,2],[11,-6,1],[12,-6,4],[11,-6,5],[12,-6,3]],
                     [[12,-6,2],[11,-6,4],[12,-6,1],[11,-6,3],[12,-6,5],[11,-6,2],[12,-6,4],[11,-6,3]],
                     [[11,-6,2],[12,-6,5],[11,-6,4],[12,-6,1]]],
             mini_diag={"a":11,"op":"−","b":6,"trick":"11-10+5-1","result":5}),
}

REV_PAGES = {
    15: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[11,-5,2],[31,-9,4],[20,-4,3],[43,-8,5],[14,-6,2],[35,-7,1],[26,-8,3],[24,-5,4],[41,-9,2],[12,-4,3]],
                     [[13,-7,5],[20,-4,3],[35,-9,2],[14,-5,1],[15,-6,4],[26,-7,3],[18,-9,5],[27,-8,2],[16,-7,1],[19,-9,4]],
                     [[21,-6,3],[24,-7,2],[28,-9,1],[15,-8,5],[16,-7,2],[18,-9,3],[24,-5,1],[14,-7,4],[12,-9,3],[28,-7,2]]], mini_diag=None),
    16: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[12,-5,4],[13,-6,3],[14,-7,2],[15,-8,1],[16,-9,3],[11,-4,5],[12,-5,2],[13,-6,4]],
                     [[14,-7,3],[15,-8,2],[16,-9,4],[11,-4,3],[12,-5,5],[13,-6,1],[14,-7,4],[15,-8,3]],
                     [[16,-9,2],[11,-4,4],[12,-5,3],[13,-6,2]]], mini_diag=None),
    17: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[12,-6,3],[14,-8,2],[16,-9,4],[11,-5,3],[13,-7,2],[15,-9,4],[17,-8,3],[10,-4,5]],
                     [[18,-9,2],[16,-8,4],[14,-7,3],[12,-6,5],[10,-5,2],[11,-4,4],[13,-7,3],[15,-9,2]],
                     [[17,-9,3],[15,-7,2],[13,-5,4],[11,-4,1]]], mini_diag=None),
    19: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[24,-9,3],[15,4,-6],[28,-7,5],[11,5,-9],[19,-6,3],[22,-8,4],[17,5,-3],[14,3,-5]],
                     [[26,-9,4],[18,-8,3],[15,4,-2],[20,-7,5],[13,6,-4],[21,-9,2],[16,3,-5],[22,-7,4]],
                     [[28,-9,3],[16,5,-7],[24,-8,2],[18,-6,3]]], mini_diag=None),
    20: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[26,-9,3],[14,5,-6],[18,-7,4],[22,5,-3],[16,4,-7],[28,-9,5],[15,3,-4],[19,-6,2]],
                     [[24,-8,3],[12,4,-5],[26,-9,2],[15,3,-6],[18,4,-7],[21,-5,3],[23,-9,4],[14,5,-2]],
                     [[20,-8,5],[26,-7,3],[12,5,-4],[28,-9,1]]], mini_diag=None),
    21: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[26,-9,3],[18,5,-6],[24,-7,4],[15,4,-3],[28,-9,2],[17,5,-4],[22,-8,3],[13,4,-6]],
                     [[20,-7,3],[14,5,-2],[26,-9,4],[16,3,-5],[24,-8,2],[18,-6,3],[15,4,-7],[27,-9,5]],
                     [[19,-8,3],[23,5,-7],[14,-3,5],[26,-9,3]]], mini_diag=None),
    23: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[11,-5,3],[24,-9,4],[31,-7,5],[16,4,-6],[19,5,-3],[27,-9,4],[14,3,-5],[28,-8,2]],
                     [[12,-5,4],[24,-9,3],[35,-8,2],[15,4,-6],[16,3,-5],[26,-7,3],[18,-9,5],[27,-8,2]],
                     [[21,-6,3],[28,-7,4],[24,-9,1],[15,-8,5]]], mini_diag=None),
    26: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[14,-9,3],[15,-9,2],[16,-9,4],[14,-9,1],[15,-9,3],[16,-9,5],[14,-9,2],[15,-9,4]],
                     [[13,-8,2],[14,-8,3],[12,-7,4],[13,-7,3],[14,-8,1],[15,-9,5],[16,-9,3],[14,-9,4]],
                     [[15,-9,1],[14,-9,3],[16,-9,2],[13,-8,4]]], mini_diag=None),
    28: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[13,-7,3],[14,-8,2],[15,-9,4],[12,-7,3],[13,-8,5],[14,-9,2],[15,-7,4],[16,-8,1]],
                     [[12,-7,5],[13,-8,3],[14,-9,2],[15,-7,4],[16,-8,3],[13,-9,5],[14,-7,2],[15,-8,3]],
                     [[16,-9,4],[12,-7,1],[14,-8,5],[15,-9,3]]], mini_diag=None),
    31: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[12,-6,4],[11,-6,3],[12,-7,2],[13,-8,5],[14,-9,1],[12,-7,3],[13,-8,4],[14,-9,2]],
                     [[11,-6,5],[12,-7,4],[13,-8,3],[14,-9,2],[11,-6,1],[12,-7,5],[13,-8,4],[14,-9,3]],
                     [[12,-6,2],[13,-7,4],[14,-8,3],[15,-9,2]]], mini_diag=None),
    33: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[12,-6,4],[13,-7,5],[14,-8,3],[15,-9,2],[11,-5,4],[12,-6,3],[13,-7,2],[14,-8,5]],
                     [[15,-9,1],[11,-5,3],[12,-6,4],[13,-7,2],[14,-8,5],[15,-9,3],[11,-5,2],[12,-6,4]],
                     [[13,-7,1],[14,-8,3],[15,-9,5],[12,-6,4]]], mini_diag=None),
    34: dict(title="Abacus Calculation: Revision", formula=None, fingering=None,
             tables=[[[13,-9,3],[12,-8,4],[11,-7,2],[10,-6,5],[15,-9,3],[14,-8,2],[13,-7,4],[12,-6,1]],
                     [[11,-9,5],[10,-8,3],[15,-7,2],[14,-6,4],[13,-9,3],[12,-8,5],[11,-7,4],[10,-6,2]],
                     [[15,-9,1],[14,-8,3],[13,-7,4],[12,-6,5]]], mini_diag=None),
}

MENTAL_CALC = {
    35: dict(title="Mental Calculation",
             a=[[2,3,-1],[5,-3,4],[7,-3,2],[4,2,-3],[6,-2,3],[3,5,-2],[8,-4,2],[2,3,4],[5,-2,1],[7,-5,3]]),
    37: dict(title="Mental Calculation",
             a=[[3,5,-2],[7,-5,2],[2,4,3],[8,-6,2],[5,-2,4],[2,3,5],[8,-6,1],[4,2,-3],[7,-4,1],[5,3,-2]],
             b=[[2,3,2],[7,-5,1],[3,4,-2],[6,3,-5],[2,7,-5],[8,-3,2],[5,2,1],[4,-3,5],[6,2,-4],[5,3,-2]],
             listening=True),
}


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    page_cover(c); c.showPage()
    page_01(c); c.showPage()
    page_02(c); c.showPage()
    for pn in [3, 4, 5, 6, 7, 8]:
        cfg = CALC_PAGES.get(pn) or REV_PAGES.get(pn)
        if cfg is None:
            # generate generic revision page
            cfg = {"title": f"Abacus Calculation: Revision", "formula": None, "fingering": None,
                   "tables": [[[12,-7,3],[13,-8,4],[14,-9,2],[15,-6,5],[11,-5,3],[12,-4,2],[16,-9,4],[17,-8,1]],
                              [[13,-9,2],[14,-8,5],[15,-7,3],[16,-6,4],[12,-5,3],[13,-4,2],[14,-9,1],[15,-8,5]],
                              [[12,-7,2],[14,-8,3],[16,-9,4],[11,-6,1]]],
                   "mini_diag": None}
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    page_09(c); c.showPage()
    page_10(c); c.showPage()
    for pn in [11, 12]:
        cfg = CALC_PAGES.get(pn) or REV_PAGES.get(pn)
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    page_13(c); c.showPage()
    for pn in [14]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    # p15 wide revision
    cfg = REV_PAGES[15]
    page_calc(c, 15, cfg["title"], cfg["formula"], cfg["fingering"], cfg["tables"], None, wide=True)
    c.showPage()
    for pn in [16, 17, 18, 19]:
        cfg = CALC_PAGES.get(pn) or REV_PAGES.get(pn)
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    # p20, p21 wide
    for pn in [20, 21]:
        cfg = REV_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"], cfg["tables"], None, wide=True)
        c.showPage()
    page_22(c); c.showPage()
    # p23 wide
    cfg = REV_PAGES[23]
    page_calc(c, 23, cfg["title"], cfg["formula"], cfg["fingering"], cfg["tables"], None, wide=True)
    c.showPage()
    page_24(c); c.showPage()
    for pn in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]:
        cfg = CALC_PAGES.get(pn) or REV_PAGES.get(pn)
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    cfg = MENTAL_CALC[35]
    page_mental(c, 35, cfg["title"], cfg["a"], cfg.get("b"), cfg.get("listening", False))
    c.showPage()
    page_36(c); c.showPage()
    cfg = MENTAL_CALC[37]
    page_mental(c, 37, cfg["title"], cfg["a"], cfg.get("b"), cfg.get("listening", False))
    c.showPage()
    page_38(c); c.showPage()
    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 39 (cover + 38)")


if __name__ == "__main__":
    main()
