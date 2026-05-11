#!/usr/bin/env python3
"""
Speedy Scholars — KG-1 Book B Workbook Generator
Landscape A4. Sequel to Book A: teaches Decomposition of 5 (−1 to −4) and
Composition of 10 (+5 to +9).

Page furniture (palette, header, footer, mascot, calc table) lives in
scripts/books/_shared/chrome.py. Drawing primitives live in
scripts/books/_shared/illustrations.py.

Book-specific decisions for this book are documented in NOTES.md.
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

set_book("KG-1 Book B")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG1-Book-B.pdf")


# ─────────────────────────────────────────────────────────────────────────
# COVER
# ─────────────────────────────────────────────────────────────────────────
def page_cover(c):
    bg(c)
    c.setStrokeColor(GOLD); c.setLineWidth(3)
    c.roundRect(12 * mm, 12 * mm, W - 24 * mm, H - 24 * mm, 8, stroke=1, fill=0)
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(1)
    c.roundRect(15 * mm, 15 * mm, W - 30 * mm, H - 30 * mm, 6, stroke=1, fill=0)
    # Mascots
    draw_bead_bird(c, 55 * mm, H - 40 * mm, 32, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - 55 * mm, H - 40 * mm, 30, BROWN, "left", "wink")
    draw_bead_bird(c, 45 * mm, 50 * mm, 28, LIGHT_GOLD, "right", "surprised")
    draw_bead_bird(c, W - 50 * mm, 55 * mm, 30, GOLD, "left", "happy", action="waving")
    # Stars
    for i in range(15):
        random.seed(i + 300)  # different seed than Book A
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    # Logo
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-1  BOOK B")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Decomposition of 5 & Composition of 10")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 70 * mm, H - 137 * mm, W / 2 + 70 * mm, H - 137 * mm)
    # Three abacuses showing 5, 7, 10
    for i, (u, l, lb) in enumerate([(1, 0, "5"), (1, 2, "7"), (1, 4, "9")]):
        draw_abacus(c, W / 2 - 55 * mm + i * 45 * mm, H - 178 * mm, 22 * mm,
                    30 * mm, u, l, lb)
    # Info card
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


# ─────────────────────────────────────────────────────────────────────────
# OBJECT REGISTRY (for concept pages — vary across the book)
# ─────────────────────────────────────────────────────────────────────────
OBJECT_FNS = [draw_apple, draw_fish, draw_flower, draw_strawberry, draw_strawberry,
              draw_butterfly, draw_mango]


# ─────────────────────────────────────────────────────────────────────────
# PAGE 1 — Composition of 5 (visual rows)
# Four rows: ( ) [a-objects] [b-objects] ( ) = 5
# Student writes both counts in the parens.
# ─────────────────────────────────────────────────────────────────────────
def page_01(c):
    bg(c); y = draw_hdr(c, "Composition of 5",
                        "Count the objects in each group and write the numbers"); draw_footer(c, 1)
    scatter_decorations(c, 1)

    pairs = [(1, 4, draw_apple), (2, 3, draw_strawberry),
             (3, 2, draw_strawberry), (4, 1, draw_fish)]

    available_h = y - 18 * mm - 8
    row_h = available_h / 4
    obj_s = 22

    for ri, (a, b, fn) in enumerate(pairs):
        ry = y - (ri + 1) * row_h + 8

        # Card background
        c.setFillColor(WARM_WHITE); c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.6)
        c.roundRect(MARGIN, ry, CW, row_h - 10, 4, stroke=1, fill=1)

        cy = ry + (row_h - 10) / 2

        # Left paren + answer box (count of a)
        c.setFont("Helvetica-Bold", 22); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 12, cy - 6, "(")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(MARGIN + 24, cy - 8, 18, 18, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 46, cy - 6, ")")

        # a objects (group 1)
        obj_sp = obj_s + 6
        a_start = MARGIN + 75
        for j in range(a):
            fn(c, a_start + j * obj_sp, cy, size=obj_s)

        # b objects (group 2)
        b_start = MARGIN + CW / 2 + 30
        for j in range(b):
            fn(c, b_start + j * obj_sp, cy, size=obj_s)

        # Right paren + answer box (count of b)
        right_x = MARGIN + CW - 80
        c.setFont("Helvetica-Bold", 22); c.setFillColor(DARKER_BROWN)
        c.drawString(right_x, cy - 6, "(")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(right_x + 12, cy - 8, 18, 18, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN)
        c.drawString(right_x + 34, cy - 6, ")")

        # "= 5"
        c.setFont("Helvetica-Bold", 22); c.setFillColor(GOLD)
        c.drawString(right_x + 50, cy - 6, "= 5")


# ─────────────────────────────────────────────────────────────────────────
# PAGE 2 — Composition of 5 (number bond + fill-ins)
# Tree showing 5 splitting into pairs; featured mascot; fill-in equations.
# ─────────────────────────────────────────────────────────────────────────
def page_02(c):
    bg(c); y = draw_hdr(c, "Composition of 5",
                        "5 is made of two parts — fill in the missing number"); draw_footer(c, 2)
    scatter_decorations(c, 2)

    # Left: mascot
    draw_bead_bird(c, MARGIN + 50, y - 70, 38, GOLD, "right", "happy",
                   hat="graduation", action="waving")

    # Center: number bond tree (the "5" splitting)
    center_x = W / 2 - 30
    top_y = y - 30
    # "5" in a circle at top
    c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.2)
    c.circle(center_x, top_y, 20, stroke=1, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(center_x, top_y - 7, "5")
    # Lines to two children
    c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
    c.line(center_x - 8, top_y - 18, center_x - 38, top_y - 60)
    c.line(center_x + 8, top_y - 18, center_x + 38, top_y - 60)
    # Two child boxes
    for cx, val in [(center_x - 45, "?"), (center_x + 30, "?")]:
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1)
        c.roundRect(cx, top_y - 90, 30, 30, 4, stroke=1, fill=1)
        c.setFillColor(BROWN); c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(cx + 15, top_y - 80, val)

    c.setFont("Helvetica-Oblique", 8); c.setFillColor(BROWN)
    c.drawCentredString(center_x, top_y - 105, "Split 5 into two parts")

    # Right: the four splits as visual "a + b = 5" with apples
    splits = [(1, 4), (2, 3), (3, 2), (4, 1)]
    rx = W - MARGIN - 200
    ry_start = y - 30
    line_h = 26
    obj_s = 12

    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(rx, ry_start + 6, "The four ways:")

    for i, (a, b) in enumerate(splits):
        ly = ry_start - (i + 1) * line_h
        # a apples
        for j in range(a):
            draw_apple(c, rx + 8 + j * (obj_s + 3), ly, size=obj_s)
        # "+" between
        c.setFont("Helvetica-Bold", 13); c.setFillColor(DARKER_BROWN)
        c.drawString(rx + 8 + 4 * (obj_s + 3) + 4, ly - 4, "+")
        # b apples
        bx = rx + 8 + 4 * (obj_s + 3) + 18
        for j in range(b):
            draw_apple(c, bx + j * (obj_s + 3), ly, size=obj_s)
        # "= 5"
        c.setFont("Helvetica-Bold", 13); c.setFillColor(GOLD)
        c.drawString(bx + 4 * (obj_s + 3) + 6, ly - 4, "= 5")

    # Middle band: featured abacus + caption (fills the previously empty space)
    band_y = y - 200
    ab_x = W / 2 - 18
    ab_y = band_y - 50
    draw_abacus(c, ab_x, ab_y, 36, 56, 1, 0, label="5")
    c.setFont("Helvetica-Oblique", 10); c.setFillColor(BROWN)
    c.drawCentredString(W / 2, band_y - 64, "On the abacus, 5 is just one upper bead")

    # A wider strip of "the four ways" callouts — to the left of the abacus
    call_x = MARGIN + 30
    call_y = band_y - 18
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(call_x, call_y, "Together, two parts make five.")
    c.setFont("Helvetica-Oblique", 9); c.setFillColor(BROWN)
    c.drawString(call_x, call_y - 14, "Practice splitting 5 into 1+4, 2+3, 3+2, 4+1.")

    # Bottom: fill-in equations (moved closer to footer)
    eq_y = 26 * mm
    c.setFont("Helvetica-Bold", 11); c.setFillColor(BROWN)
    c.drawString(MARGIN, eq_y + 16, "Fill in the missing number:")
    equations = ["4 + ___ = 5", "___ + 3 = 5", "2 + ___ = 5",
                 "___ + 1 = 5", "3 + ___ = 5", "___ + 4 = 5"]
    eq_w = CW / 6
    for i, eq in enumerate(equations):
        c.setFont("Helvetica", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + i * eq_w + 8, eq_y, eq)


# ─────────────────────────────────────────────────────────────────────────
# PAGE 3 — Decomposition of 5 (visual subtraction)
# 6 cards 3×2: ALL objects shown, red X overlay on the right group.
# ─────────────────────────────────────────────────────────────────────────
def page_03(c):
    bg(c); y = draw_hdr(c, "Decomposition of 5",
                        "Cross out the objects to subtract — what is left?"); draw_footer(c, 3)
    scatter_decorations(c, 3)

    problems = [(8, 4, draw_apple), (5, 2, draw_fish), (7, 3, draw_strawberry),
                (5, 1, draw_flower), (6, 4, draw_strawberry), (6, 2, draw_butterfly)]

    cols = 3; rows = 2
    avail_h = y - 18 * mm - 8
    card_w = CW / cols - 6
    card_h = avail_h / rows - 6

    for i, (a, b, fn) in enumerate(problems):
        col = i % cols; row = i // cols
        bx = MARGIN + col * (card_w + 6)
        by = y - (row + 1) * (card_h + 6) + 6

        # Card
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(bx, by, card_w, card_h, 4, stroke=1, fill=1)

        # Object area
        obj_s = 22
        obj_sp = obj_s + 6
        total_w = a * obj_sp
        start_x = bx + (card_w - total_w) / 2
        obj_y = by + card_h * 0.62
        for j in range(a):
            fn(c, start_x + j * obj_sp, obj_y, size=obj_s)
        # Red X on the LAST b objects (representing -b)
        c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(2)
        x_size = obj_s * 0.5
        for j in range(a - b, a):
            cx = start_x + j * obj_sp
            c.line(cx - x_size, obj_y - x_size, cx + x_size, obj_y + x_size)
            c.line(cx - x_size, obj_y + x_size, cx + x_size, obj_y - x_size)

        # Equation
        c.setFont("Helvetica-Bold", 16); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(bx + card_w / 2 - 18, by + 14, f"{a} - {b} =")
        # Answer box
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(bx + card_w / 2 + 20, by + 10, 22, 18, stroke=1, fill=1)


# ─────────────────────────────────────────────────────────────────────────
# PAGE 4 — Subtraction Cart (mascot-driven, staircase panel)
# Mascot drives a cart with hex beads as wheels; problem panel on its side
# shows the −1, −2, −3, −4 staircase pyramid.
# ─────────────────────────────────────────────────────────────────────────
def page_04(c):
    bg(c); y = draw_hdr(c, "Decomposition of 5",
                        "Climb the subtraction ladder with our Speedy mascot!"); draw_footer(c, 4)
    scatter_decorations(c, 4)

    # Cart on left (bigger, focal element)
    cart_w = 200
    cart_h = 140
    cart_x = MARGIN + 10
    cart_y = (22 * mm + 10 + (y - 20) - cart_h) / 2  # vertically centered in content area

    # Cart body
    c.setFillColor(BROWN); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.5)
    c.roundRect(cart_x, cart_y, cart_w, cart_h, 8, stroke=1, fill=1)
    # Cart label
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(cart_x + cart_w / 2, cart_y + cart_h / 2 + 12, "SPEEDY")
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(cart_x + cart_w / 2, cart_y + cart_h / 2 - 10, "CART")
    c.setFont("Helvetica-Oblique", 10); c.setFillColor(LIGHT_GOLD)
    c.drawCentredString(cart_x + cart_w / 2, cart_y + cart_h / 2 - 26, "Decomposition of 5")

    # Wheels (hex beads, bigger)
    for wx in [cart_x + 30, cart_x + cart_w - 30]:
        c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.2)
        p = c.beginPath()
        r = 16
        for k in range(6):
            ang = math.pi / 3 * k - math.pi / 6
            px = wx + r * math.cos(ang); py = cart_y - 6 + r * math.sin(ang)
            if k == 0: p.moveTo(px, py)
            else: p.lineTo(px, py)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        # Wheel hub
        c.setFillColor(DARKER_BROWN)
        c.circle(wx, cart_y - 6, 3, stroke=0, fill=1)

    # Chimney with smoke (top-right of cart)
    chim_x = cart_x + cart_w - 35
    chim_y = cart_y + cart_h
    c.setFillColor(DARKER_BROWN)
    c.rect(chim_x, chim_y, 12, 18, stroke=0, fill=1)
    # Smoke puffs
    c.setFillColor(LIGHT_GOLD); c.setStrokeColor(LIGHT_GOLD)
    for sx, sy, sr in [(chim_x + 6, chim_y + 24, 6),
                       (chim_x + 18, chim_y + 32, 7),
                       (chim_x + 32, chim_y + 40, 6),
                       (chim_x + 22, chim_y + 46, 5)]:
        c.circle(sx, sy, sr, stroke=0, fill=1)

    # Mascot driver — sitting on top of cart, peeking up
    draw_bead_bird(c, cart_x + 50, cart_y + cart_h + 18, 28,
                   GOLD, "right", "happy", hat="graduation")

    # Right: staircase pyramid of subtraction problems
    panel_x = cart_x + cart_w + 25
    panel_w = W - MARGIN - panel_x
    panel_y_top = y - 10
    panel_h = panel_y_top - (22 * mm + 14)
    panel_y_bot = panel_y_top - panel_h

    # Staircase: row k shows problems with start = 5+k, all minus 1..k+1
    # Row 0: 5-1
    # Row 1: 6-2, 5-2
    # Row 2: 7-3, 6-3, 5-3
    # Row 3: 8-4, 7-4, 6-4, 5-4
    rows_data = [
        [(5, 1)],
        [(6, 2), (5, 2)],
        [(7, 3), (6, 3), (5, 3)],
        [(8, 4), (7, 4), (6, 4), (5, 4)],
    ]
    row_h = panel_h / 4
    cell_w = panel_w / 4

    for ri, row in enumerate(rows_data):
        ry = panel_y_top - (ri + 1) * row_h + 4
        for ci, (a, b) in enumerate(row):
            cx = panel_x + ci * cell_w
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
            c.roundRect(cx, ry, cell_w - 4, row_h - 4, 3, stroke=1, fill=1)
            c.setFont("Helvetica-Bold", 16); c.setFillColor(DARKER_BROWN)
            c.drawCentredString(cx + (cell_w - 4) / 2, ry + (row_h - 4) / 2 - 5,
                                f"{a} - {b}")
            # Answer line
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(1)
            c.line(cx + 14, ry + 8, cx + cell_w - 18, ry + 8)


# ─────────────────────────────────────────────────────────────────────────
# CALC PAGE — three tables + bottom strip (with optional mini-diagram card)
# data: list of 3 tuples (fing_or_None, table_data)
# formula: top-left of header (e.g. "−4 = +1 − 5"); set None for revision pages
# fingering: text after formula (e.g. "Fingering Ex: 5−4, 6−4, 7−4, 8−4")
# mini_diagram: dict like {"a":4,"op":"+","b":9,"trick":"4-1+10"} or None
# ─────────────────────────────────────────────────────────────────────────

BOTTOM_STRIP_SETS = {
    # Decomp-of-5 phase (pages 5-15): subtraction emphasized
    5:  [(8, "-", 4, draw_apple),   (5, "-", 4, draw_strawberry),   (7, "-", 4, draw_fish),   (6, "-", 4, draw_flower)],
    6:  [(5, "-", 3, draw_strawberry),  (7, "-", 2, draw_apple),    (4, "+", 1, draw_strawberry), (6, "-", 4, draw_fish)],
    7:  [(7, "-", 3, draw_fish),    (5, "-", 3, draw_apple),    (6, "-", 3, draw_strawberry), (4, "+", 1, draw_flower)],
    8:  [(6, "-", 2, draw_apple),   (5, "-", 4, draw_strawberry),(7, "-", 3, draw_strawberry),(4, "+", 3, draw_fish)],
    10: [(6, "-", 2, draw_strawberry),(5,"-", 2, draw_apple),   (7, "-", 2, draw_flower), (4, "-", 2, draw_strawberry)],
    11: [(5, "-", 1, draw_fish),    (6, "-", 3, draw_apple),    (3, "+", 2, draw_strawberry), (7, "-", 4, draw_strawberry)],
    12: [(5, "-", 1, draw_strawberry),  (6, "-", 1, draw_apple),    (7, "-", 1, draw_flower), (4, "-", 1, draw_fish)],
    13: [(5, "-", 4, draw_apple),   (7, "-", 3, draw_strawberry),   (6, "-", 2, draw_strawberry),(4,"+", 2, draw_flower)],
    14: [(6, "-", 4, draw_flower),  (5, "-", 2, draw_fish),     (7, "-", 1, draw_apple),  (3, "+", 1, draw_strawberry)],
    15: [(8, "-", 4, draw_strawberry),  (5, "-", 3, draw_apple),    (6, "-", 1, draw_fish),   (4, "+", 2, draw_strawberry)],
    # Comp-of-10 phase (pages 19+): addition emphasized
    19: [(4, "+", 9, draw_apple),   (3, "+", 9, draw_strawberry),   (6, "+", 4, draw_fish),   (8, "-", 3, draw_flower)],
    20: [(5, "+", 4, draw_strawberry),(2,"+", 9, draw_apple),   (7, "-", 3, draw_strawberry), (6, "-", 4, draw_fish)],
    21: [(4, "+", 8, draw_strawberry),  (3, "+", 8, draw_apple),    (5, "+", 4, draw_flower), (7, "-", 2, draw_strawberry)],
    22: [(6, "+", 4, draw_fish),    (5, "+", 8, draw_apple),    (8, "-", 4, draw_strawberry), (3, "+", 9, draw_flower)],
    23: [(4, "+", 7, draw_flower),  (3, "+", 7, draw_apple),    (8, "+", 7, draw_strawberry), (6, "-", 3, draw_fish)],
    24: [(5, "+", 7, draw_apple),   (4, "+", 9, draw_strawberry),(7,"-", 4, draw_strawberry), (6, "+", 4, draw_fish)],
    27: [(3, "+", 8, draw_strawberry),(5,"+", 7, draw_flower),  (6, "+", 4, draw_apple),  (8, "-", 3, draw_strawberry)],
    28: [(4, "+", 6, draw_strawberry),  (9, "+", 6, draw_apple),    (5, "+", 8, draw_fish),   (7, "-", 4, draw_flower)],
    29: [(8, "+", 6, draw_fish),    (5, "+", 6, draw_strawberry),   (7, "+", 4, draw_apple),  (6, "-", 2, draw_strawberry)],
    30: [(4, "+", 7, draw_apple),   (6, "+", 6, draw_flower),   (8, "+", 5, draw_strawberry), (7, "-", 3, draw_fish)],
    31: [(5, "+", 5, draw_strawberry),  (7, "+", 5, draw_apple),    (8, "+", 5, draw_strawberry),(9,"+", 5, draw_fish)],
    32: [(6, "+", 5, draw_fish),    (8, "+", 5, draw_apple),    (9, "+", 4, draw_strawberry), (7, "+", 6, draw_flower)],
}


def page_calc(c, pn, title, formula, fingering, tables, mini_diagram=None):
    """
    Standard calc page: three tables + bottom strip (4 cards).
    If mini_diagram is given, the LAST strip card is replaced with the trick diagram.
    """
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)

    # Formula + fingering text just below header
    header_parts = []
    if formula:
        header_parts.append(formula)
    if fingering:
        header_parts.append(fingering)
    if header_parts:
        c.setFont("Helvetica", 8); c.setFillColor(BROWN)
        c.drawString(MARGIN, y - 2, "    ".join(header_parts))
        y -= 10

    # Three tables, full page width
    for table_data in tables:
        cols = len(table_data)
        y = draw_calc_table(c, MARGIN, y, table_data, cols, None, table_width=CW)
        y -= 8

    # Bottom strip
    strip_y = 18 * mm
    strip_h = y - strip_y - 4
    if strip_h < 25:
        strip_h = 25

    strip_set = BOTTOM_STRIP_SETS.get(pn, BOTTOM_STRIP_SETS[5])
    num_cards = 4
    card_w = CW / num_cards

    for i in range(num_cards):
        px = MARGIN + i * card_w
        pw = card_w - 4

        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(px, strip_y, pw, strip_h, 3, stroke=1, fill=1)

        # If this is the last card AND we have a mini-diagram, draw the diagram
        if mini_diagram and i == num_cards - 1:
            _draw_mini_trick(c, px, strip_y, pw, strip_h, mini_diagram)
            continue

        a, op, b, fn = strip_set[i]
        # Scale object size down so high-count problems (e.g. 8+4) fit inside the card
        total_count = a + b
        obj_s = min(13, strip_h * 0.28, (pw - 60) / max(total_count, 1) - 1)
        obj_s = max(obj_s, 7)
        obj_y = strip_y + strip_h * 0.58
        obj_sp = obj_s + 2
        op_pad = max(8, obj_s); op_w = 8
        total_w = a * obj_sp + op_pad + op_w + op_pad + b * obj_sp
        start_x = px + max(6, (pw - total_w) / 2)

        for j in range(a):
            ox = start_x + j * obj_sp
            try: fn(c, ox, obj_y, size=obj_s)
            except: fn(c, ox, obj_y)

        op_cx = start_x + a * obj_sp + op_pad + op_w / 2
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(op_cx, obj_y - 4, op)

        b_start = op_cx + op_w / 2 + op_pad
        for j in range(b):
            ox = b_start + j * obj_sp
            try: fn(c, ox, obj_y, size=obj_s)
            except: fn(c, ox, obj_y)

        c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
        c.drawString(px + 10, strip_y + 5, f"{a} {op} {b} =")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(px + pw - 14 * mm, strip_y + 2, 12 * mm, 12, stroke=1, fill=1)


def _draw_mini_trick(c, px, py, pw, ph, diag):
    """Draw the 'trick' diagram: e.g. 4+9 = 4-1+10 = 12 with 2 small abacuses."""
    # Title line
    c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
    expr = f"{diag['a']} {diag['op']} {diag['b']}"
    c.drawCentredString(px + pw / 2, py + ph - 12, expr)
    # Trick text
    c.setFont("Helvetica", 7.5); c.setFillColor(BROWN)
    c.drawCentredString(px + pw / 2, py + ph - 24, f"= {diag['trick']}")
    c.drawCentredString(px + pw / 2, py + ph - 34, f"= {diag['result']}")
    # Tiny abacus on the right showing the result
    ab_w = 20
    ab_h = min(34, ph - 14)
    ab_x = px + pw - ab_w - 6
    ab_y = py + 6
    res = diag['result']
    if res <= 9:
        upper = 1 if res >= 5 else 0
        lower = res - 5 if res >= 5 else res
        draw_abacus(c, ab_x, ab_y, ab_w, ab_h, upper, lower)
    else:
        # For 10+, just show "10" digit
        c.setFont("Helvetica-Bold", 11); c.setFillColor(GOLD)
        c.drawCentredString(ab_x + ab_w / 2, ab_y + ab_h / 2 - 4, str(res))


# ─────────────────────────────────────────────────────────────────────────
# PAGE 9 — Revision 5: Look for the Answer
# Colored answer balloons on top, vertical subtraction stacks below.
# Student matches each stack to a balloon.
# ─────────────────────────────────────────────────────────────────────────
def page_09(c):
    bg(c); y = draw_hdr(c, "Revision: Look for the Answer",
                        "Solve each subtraction stack and find the matching balloon"); draw_footer(c, 9)
    scatter_decorations(c, 9)

    # Mascot on left, arms up (use "surprised" expression)
    draw_bead_bird(c, MARGIN + 35, y - 60, 32, GOLD, "right", "surprised", hat="graduation")

    # 8 balloons in a row (gives answers 1..8)
    balloon_y = y - 38
    balloons = [4, 9, 5, 3, 6, 7, 8, 2]
    balloon_colors = [GOLD, BROWN, LIGHT_GOLD, GOLD, LIGHT_BROWN, GOLD, LIGHT_GOLD, BROWN]
    balloon_start_x = MARGIN + 90
    bal_w = (W - MARGIN - balloon_start_x) / 8

    for i, (val, col) in enumerate(zip(balloons, balloon_colors)):
        bx = balloon_start_x + i * bal_w + bal_w / 2
        # Balloon body
        c.setFillColor(col); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.8)
        c.circle(bx, balloon_y, 14, stroke=1, fill=1)
        # String
        c.setLineWidth(0.5)
        c.line(bx, balloon_y - 14, bx, balloon_y - 28)
        # Value
        c.setFillColor(white); c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(bx, balloon_y - 4, str(val))

    # 7 vertical subtraction stacks below
    stacks = [
        (7, -3, -2),   # = 2
        (8, -4, +3),   # = 7
        (7, +1, -4),   # = 4
        (6, -3, +5),   # = 8
        (7, -4, +2),   # = 5
        (7, -3, +5),   # = 9
        (9, -2, -4),   # = 3
    ]
    # Box geometry: each stack is a vertical card from y=22mm+8 (bottom) up to y - 90 (top)
    box_bottom = 22 * mm + 8
    box_top = y - 90
    box_h = box_top - box_bottom
    stack_w = CW / 7

    # 4 horizontal slots inside each box: start value, op2, op3, answer underline
    slot_h = box_h / 4

    for i, (a, op2, op3) in enumerate(stacks):
        sx = MARGIN + i * stack_w + stack_w / 2
        box_x = sx - stack_w / 2 + 6
        box_w = stack_w - 12

        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(box_x, box_bottom, box_w, box_h, 4, stroke=1, fill=1)

        c.setFont("Helvetica-Bold", 22); c.setFillColor(DARKER_BROWN)
        # Slot k counted from top. Slot 0 = start, slot 1 = op2, slot 2 = op3, slot 3 = answer
        for ri, v in enumerate([a, op2, op3]):
            slot_center_y = box_top - (ri + 0.5) * slot_h - 4
            label = str(v) if ri == 0 else (f"+{v}" if v > 0 else str(v))
            c.drawCentredString(sx, slot_center_y, label)
        # Answer underline in slot 3
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        line_y = box_bottom + slot_h * 0.5
        c.line(sx - 16, line_y, sx + 16, line_y)


# ─────────────────────────────────────────────────────────────────────────
# PAGE 16 — Composition of 10 (visual rows)
# 10 rows: ( ) [a-objects] [b-objects] ( ) = 10
# ─────────────────────────────────────────────────────────────────────────
def page_16(c):
    bg(c); y = draw_hdr(c, "Composition of 10",
                        "Count the objects and write both numbers — they make 10"); draw_footer(c, 16)
    scatter_decorations(c, 16)

    pairs = [(1, 9, draw_apple),    (2, 8, draw_strawberry),  (3, 7, draw_fish),
             (4, 6, draw_flower),   (5, 5, draw_butterfly),(6, 4, draw_strawberry),
             (7, 3, draw_apple),    (8, 2, draw_mango),   (9, 1, draw_strawberry),
             (4, 6, draw_fish)]

    avail_h = y - 18 * mm - 4
    row_h = avail_h / 10
    obj_s = 10

    for ri, (a, b, fn) in enumerate(pairs):
        ry = y - (ri + 1) * row_h + 2
        cy = ry + row_h / 2

        # Left paren + box
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 4, cy - 4, "(")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(MARGIN + 12, cy - 7, 14, 14, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 28, cy - 4, ")")

        # a objects
        obj_sp = obj_s + 3
        a_start = MARGIN + 46
        for j in range(a):
            fn(c, a_start + j * obj_sp, cy, size=obj_s)
        # b objects
        b_start = MARGIN + CW * 0.55
        for j in range(b):
            fn(c, b_start + j * obj_sp, cy, size=obj_s)

        # Right paren + box
        rx = W - MARGIN - 70
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(rx, cy - 4, "(")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(rx + 8, cy - 7, 14, 14, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN)
        c.drawString(rx + 24, cy - 4, ")")
        c.setFont("Helvetica-Bold", 12); c.setFillColor(GOLD)
        c.drawString(rx + 36, cy - 4, "= 10")


# ─────────────────────────────────────────────────────────────────────────
# PAGE 17 — Composition of 10 (number-pair grid with bead columns)
# 9 cards: each shows pre-filled "10" on top, two operand circles, and a
# vertical abacus column. Some operands are blank for the student to fill.
# ─────────────────────────────────────────────────────────────────────────
def page_17(c):
    bg(c); y = draw_hdr(c, "Composition of 10",
                        "Fill in the missing partner and look at the beads"); draw_footer(c, 17)
    scatter_decorations(c, 17)

    # 9 pairs that make 10: (1,9), (2,8), (3,7), (4,6), (5,5), (6,4), (7,3), (8,2), (9,1)
    # Each card: a pair, with one operand visible and the other blank (alternating which side is hidden)
    pairs = [(1, 9, "left"), (2, 8, "right"), (3, 7, "left"), (4, 6, "right"),
             (5, 5, "left"), (6, 4, "right"), (7, 3, "left"), (8, 2, "right"),
             (9, 1, "left")]

    cols = 3; rows = 3
    avail_h = y - 18 * mm - 8
    card_w = CW / cols - 6
    card_h = avail_h / rows - 6

    for i, (a, b, hidden) in enumerate(pairs):
        col = i % cols; row = i // cols
        bx = MARGIN + col * (card_w + 6)
        by = y - (row + 1) * (card_h + 6) + 6

        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(bx, by, card_w, card_h, 4, stroke=1, fill=1)

        # "10" badge top-center
        c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.8)
        c.roundRect(bx + card_w / 2 - 14, by + card_h - 22, 28, 18, 3, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(bx + card_w / 2, by + card_h - 16, "10")

        # Two operand circles below, connected by a "+"
        left_cx = bx + card_w * 0.32
        right_cx = bx + card_w * 0.68
        op_y = by + card_h - 50
        for cx, val, is_hidden in [(left_cx, a, hidden == "left"),
                                    (right_cx, b, hidden == "right")]:
            if is_hidden:
                c.setFillColor(white); c.setStrokeColor(GOLD); c.setLineWidth(1)
            else:
                c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.8)
            c.circle(cx, op_y, 12, stroke=1, fill=1)
            if not is_hidden:
                c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 13)
                c.drawCentredString(cx, op_y - 4, str(val))
            else:
                c.setFillColor(BROWN); c.setFont("Helvetica-Bold", 13)
                c.drawCentredString(cx, op_y - 4, "?")

        # "+" between
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 14)
        c.drawCentredString((left_cx + right_cx) / 2, op_y - 4, "+")

        # Mini abacus showing the LEFT operand value
        ab_w = 18
        ab_h = min(40, card_h - 80)
        ab_x = bx + card_w / 2 - ab_w / 2
        ab_y = by + 8
        upper = 1 if a >= 5 else 0
        lower = a - 5 if a >= 5 else a
        draw_abacus(c, ab_x, ab_y, ab_w, ab_h, upper, lower)


# ─────────────────────────────────────────────────────────────────────────
# PAGE 18 — "I can do it!" subtraction card grid
# 3 rows × 3 cards. Each card: 10–19 number on top, subtract single digit.
# ─────────────────────────────────────────────────────────────────────────
def page_18(c):
    bg(c); y = draw_hdr(c, "I Can Do It!",
                        "Subtract the smaller number from the bigger one"); draw_footer(c, 18)
    scatter_decorations(c, 18)

    # Two mascots flanking the grid
    draw_bead_bird(c, MARGIN + 22, y - 60, 26, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - MARGIN - 22, y - 60, 26, BROWN, "left", "wink", hat="graduation")

    # 3×3 cards, centered
    grid_w = CW - 100  # leave space for side mascots
    grid_x = MARGIN + 50
    grid_y_top = y - 30
    grid_h = grid_y_top - 22 * mm - 8

    cols = 3; rows = 3
    card_w = grid_w / cols - 8
    card_h = grid_h / rows - 8

    problems = [(10, 1), (12, 8), (13, 7),
                (14, 6), (15, 5), (16, 4),
                (17, 3), (18, 2), (19, 1)]

    for i, (a, b) in enumerate(problems):
        col = i % cols; row = i // cols
        cx = grid_x + col * (card_w + 8)
        cy = grid_y_top - (row + 1) * (card_h + 8) + 8

        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(cx, cy, card_w, card_h, 4, stroke=1, fill=1)

        # a on top
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 22)
        c.drawCentredString(cx + card_w / 2, cy + card_h - 28, str(a))
        # -b
        c.drawCentredString(cx + card_w / 2, cy + card_h - 50, f"- {b}")
        # Bottom line
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(cx + 16, cy + 18, cx + card_w - 16, cy + 18)


# ─────────────────────────────────────────────────────────────────────────
# PAGE 25 — Composition of 10 revision: staircase pyramid
# Triangular grid where each row n contains pairs that sum to 10: 9+1, 8+2 9+2,
# 7+3 8+3 9+3, ... up to 9 wide.
# ─────────────────────────────────────────────────────────────────────────
def page_25(c):
    bg(c); y = draw_hdr(c, "Composition of 10: Revision",
                        "Solve every box on the staircase"); draw_footer(c, 25)
    scatter_decorations(c, 25)

    # Mascots flanking
    draw_bead_bird(c, MARGIN + 22, y - 60, 28, GOLD, "right", "happy", hat="graduation",
                   action="waving")
    draw_bead_bird(c, W - MARGIN - 22, y - 220, 28, BROWN, "left", "wink", hat="graduation")

    # Staircase: row r (r from 0 to 8), row r has (r+1) columns
    # Row 0: 9+1
    # Row 1: 8+2, 9+2
    # Row 2: 7+3, 8+3, 9+3
    # ...
    # Row 8: 1+9, 2+9, 3+9, ..., 9+9
    rows = 9
    grid_x = MARGIN + 60
    grid_y_top = y - 12
    grid_h = grid_y_top - 22 * mm - 8
    grid_w = CW - 120
    cell_w = grid_w / rows
    cell_h = grid_h / rows

    for r in range(rows):
        for col in range(r + 1):
            a = 9 - r + col
            b = r + 1
            cx = grid_x + col * cell_w
            cy = grid_y_top - (r + 1) * cell_h
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
            c.roundRect(cx, cy, cell_w - 2, cell_h - 2, 2, stroke=1, fill=1)
            c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 8.5)
            c.drawCentredString(cx + (cell_w - 2) / 2, cy + (cell_h - 2) / 2 - 3,
                                f"{a}+{b}")


# ─────────────────────────────────────────────────────────────────────────
# PAGE 26 — Match the Following
# 4 problem boxes on top, 4 visual-group boxes middle, 4 rewrite boxes bottom.
# Student draws lines to match (top↔middle = same problem, middle↔bottom = rewrite).
# ─────────────────────────────────────────────────────────────────────────
def page_26(c):
    bg(c); y = draw_hdr(c, "Match the Following",
                        "Match each problem with its picture and its trick form"); draw_footer(c, 26)
    scatter_decorations(c, 26)

    problems = [
        (3, 9, "3-1+10", draw_apple),
        (4, 9, "4-1+10", draw_strawberry),
        (3, 8, "3-2+10", draw_fish),
        (4, 7, "4-3+10", draw_flower),
    ]

    avail_h = y - 18 * mm - 8
    band_h = avail_h / 3
    band_top_y = y - 8

    col_w = CW / 4

    for i, (a, b, trick, fn) in enumerate(problems):
        cx_center = MARGIN + (i + 0.5) * col_w

        # Top: problem box
        top_box_y = band_top_y - band_h + 30
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(cx_center - 50, top_box_y, 100, 32, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 18); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(cx_center, top_box_y + 12, f"{a} + {b}")
        # Anchor dot
        c.setFillColor(GOLD)
        c.circle(cx_center, top_box_y - 6, 3, stroke=0, fill=1)

        # Middle: visual group box (a objects, "+", b objects)
        mid_box_y = band_top_y - 2 * band_h + 30
        mid_h = band_h - 16
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(cx_center - 55, mid_box_y, 110, mid_h, 4, stroke=1, fill=1)
        # Objects packed inside
        obj_s = 10
        per_row = 4
        all_obj = [fn] * a + ["op"] + [fn] * b
        # Pack in 3 rows
        ipx = cx_center - 50
        ipy = mid_box_y + mid_h - 18
        for ki, item in enumerate(all_obj):
            ox = ipx + (ki % per_row) * (obj_s + 4)
            oy = ipy - (ki // per_row) * (obj_s + 4)
            if item == "op":
                c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
                c.drawCentredString(ox, oy - 3, "+")
            else:
                item(c, ox, oy, size=obj_s)
        # Anchor dots top and bottom
        c.setFillColor(GOLD)
        c.circle(cx_center, mid_box_y + mid_h + 6, 3, stroke=0, fill=1)
        c.circle(cx_center, mid_box_y - 6, 3, stroke=0, fill=1)

        # Bottom: rewrite box
        bot_box_y = 24 * mm
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(cx_center - 55, bot_box_y, 110, 32, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 15); c.setFillColor(BROWN)
        c.drawCentredString(cx_center, bot_box_y + 12, trick)
        # Anchor dot
        c.setFillColor(GOLD)
        c.circle(cx_center, bot_box_y + 38, 3, stroke=0, fill=1)


# ─────────────────────────────────────────────────────────────────────────
# PAGE 33 — Color-the-Region Puzzle
# 4×5 grid of cells, each with an addition problem. Student solves and
# colors the cell according to the answer (color key below).
# Brown/gold variant palette per sign-off.
# ─────────────────────────────────────────────────────────────────────────
def page_33(c):
    bg(c); y = draw_hdr(c, "Color the Answer Puzzle",
                        "Solve each problem, then color the box by its answer"); draw_footer(c, 33)
    scatter_decorations(c, 33)

    # Mascot holding a brush, left side
    draw_bead_bird(c, MARGIN + 30, y - 70, 28, GOLD, "right", "thinking", hat="graduation")
    # Tiny brush
    c.setStrokeColor(DARKER_BROWN); c.setLineWidth(2)
    c.line(MARGIN + 45, y - 80, MARGIN + 60, y - 95)
    c.setFillColor(BROWN)
    c.circle(MARGIN + 62, y - 96, 3, stroke=0, fill=1)

    # Problems — each maps to one of 5 answer values: 10, 11, 12, 13, 14
    # Grid: 4 rows × 5 cols = 20 cells
    problems_raw = [
        # row 1 — all 10s
        (1, 9), (2, 8), (3, 7), (4, 6), (5, 5),
        # row 2 — all 11s
        (2, 9), (3, 8), (4, 7), (5, 6), (6, 5),
        # row 3 — mix of 12, 13
        (3, 9), (4, 8), (5, 7), (6, 6), (7, 6),  # last two = 12, 13
        # row 4 — mix of 13, 14
        (4, 9), (5, 8), (6, 7), (5, 9), (6, 8),
    ]
    # Shuffle deterministically so colors are scattered
    random.seed(123)
    problems = problems_raw[:]
    random.shuffle(problems)

    grid_x = MARGIN + 90
    grid_y_top = y - 18
    grid_h = (grid_y_top - 22 * mm - 60)  # leave room for color key
    grid_w = CW - 110
    cols = 5; rows = 4
    cell_w = grid_w / cols
    cell_h = grid_h / rows

    answer_to_color = {
        10: WARM_WHITE,
        11: LIGHT_GOLD,
        12: GOLD,
        13: LIGHT_BROWN,
        14: BROWN,
    }
    # Cells display answer label in lighter ink (so coloring is the activity)
    for i, (a, b) in enumerate(problems):
        col = i % cols; row = i // cols
        cx = grid_x + col * cell_w
        cy = grid_y_top - (row + 1) * cell_h
        # Empty/white-ish cell so kid can color
        c.setFillColor(white); c.setStrokeColor(GOLD); c.setLineWidth(0.7)
        c.roundRect(cx, cy, cell_w - 3, cell_h - 3, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 13); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(cx + (cell_w - 3) / 2, cy + (cell_h - 3) / 2 - 4,
                            f"{a} + {b}")

    # Color key at bottom
    key_y = 22 * mm
    key_w = 70
    c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, key_y + 14, "Color key:")
    key_start_x = MARGIN + 70
    for i, ans in enumerate([10, 11, 12, 13, 14]):
        kx = key_start_x + i * (key_w + 10)
        c.setFillColor(answer_to_color[ans]); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.6)
        c.roundRect(kx, key_y, 24, 18, 2, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(kx + 30, key_y + 4, f"= {ans}")


# ─────────────────────────────────────────────────────────────────────────
# PAGE 34 — Composition of 10 (final visual review)
# 10 rows of paired counts that make 10 — like page 16 but final assessment.
# ─────────────────────────────────────────────────────────────────────────
def page_34(c):
    bg(c); y = draw_hdr(c, "Composition of 10: Final Review",
                        "You have made it to the end — count carefully!"); draw_footer(c, 34)
    scatter_decorations(c, 34)

    pairs = [(2, 8, draw_butterfly), (3, 7, draw_apple),  (4, 6, draw_strawberry),
             (5, 5, draw_flower),    (6, 4, draw_mango),  (7, 3, draw_strawberry),
             (8, 2, draw_fish),      (9, 1, draw_butterfly),(1, 9, draw_strawberry),
             (5, 5, draw_apple)]

    avail_h = y - 18 * mm - 4
    row_h = avail_h / 10
    obj_s = 10

    for ri, (a, b, fn) in enumerate(pairs):
        ry = y - (ri + 1) * row_h + 2
        cy = ry + row_h / 2

        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 4, cy - 4, "(")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(MARGIN + 12, cy - 7, 14, 14, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN); c.drawString(MARGIN + 28, cy - 4, ")")

        obj_sp = obj_s + 3
        a_start = MARGIN + 46
        for j in range(a):
            fn(c, a_start + j * obj_sp, cy, size=obj_s)
        b_start = MARGIN + CW * 0.55
        for j in range(b):
            fn(c, b_start + j * obj_sp, cy, size=obj_s)

        rx = W - MARGIN - 70
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(rx, cy - 4, "(")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(rx + 8, cy - 7, 14, 14, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN); c.drawString(rx + 24, cy - 4, ")")
        c.setFont("Helvetica-Bold", 12); c.setFillColor(GOLD)
        c.drawString(rx + 36, cy - 4, "= 10")


# ─────────────────────────────────────────────────────────────────────────
# CALC PAGE DATA — every calc page gets a (title, formula, fingering, tables, mini_diag) entry
# 3 tables per page: cols 8, 8, 4
# Each column = [start_value, op1, op2] — Ans row computed by the student
# All data is unique per page (verified during review)
# ─────────────────────────────────────────────────────────────────────────

CALC_PAGES = {
    # ── Decomposition of 5 phase ────────────────────────────────────────
    5: dict(
        title="Abacus Calculation: Decomposition of 5 (−4)",
        formula="−4 = +1 − 5",
        fingering="Fingering Ex.: 5−4, 6−4, 7−4, 8−4",
        tables=[
            [[4,8,-1],[8,-4,3],[9,-4,2],[7,-4,1],[5,4,-1],[8,-4,-1],[6,-4,3],[4,5,-4]],
            [[4,5,-4],[6,2,-4],[7,-4,2],[8,-4,-1],[5,4,-4],[7,-4,3],[6,-4,4],[8,-4,1]],
            [[5,-4,2],[7,-4,3],[6,3,-4],[8,-4,-1]],
        ],
        mini_diag={"a":7,"op":"-","b":4,"trick":"7+1-5","result":3},
    ),
    6: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[8,-4,2],[5,3,-4],[7,-4,1],[6,-4,3],[5,4,-4],[8,-4,-2],[7,-4,2],[9,-4,3]],
            [[6,-4,2],[5,2,-4],[7,-4,-1],[8,-4,1],[6,3,-4],[5,-4,4],[7,-4,2],[8,-4,-2]],
            [[5,4,-4],[7,-4,3],[6,-4,2],[8,-4,1]],
        ],
        mini_diag=None,
    ),
    7: dict(
        title="Abacus Calculation: Decomposition of 5 (−3)",
        formula="−3 = +2 − 5",
        fingering="Fingering Ex.: 5−3, 6−3, 7−3",
        tables=[
            [[5,-3,2],[7,-3,1],[6,-3,3],[5,3,-3],[7,-3,-1],[6,-3,2],[5,-3,4],[6,3,-3]],
            [[7,-3,2],[5,-3,3],[6,2,-3],[7,-3,-1],[5,-3,4],[6,-3,3],[7,-3,1],[5,-3,2]],
            [[6,-3,4],[7,-3,2],[5,-3,3],[6,-3,2]],
        ],
        mini_diag={"a":6,"op":"-","b":3,"trick":"6+2-5","result":3},
    ),
    8: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[7,-3,-2],[5,-3,4],[6,2,-3],[8,-4,3],[5,4,-3],[7,-3,-1],[6,-4,3],[5,3,-3]],
            [[6,-3,1],[5,-3,2],[7,-4,2],[6,-3,-1],[8,-3,2],[5,2,-3],[7,-3,3],[6,-3,4]],
            [[7,-3,2],[5,3,-3],[6,-3,1],[8,-4,3]],
        ],
        mini_diag=None,
    ),
    10: dict(
        title="Abacus Calculation: Decomposition of 5 (−2)",
        formula="−2 = +3 − 5",
        fingering="Fingering Ex.: 5−2, 6−2",
        tables=[
            [[5,-2,3],[6,-2,1],[5,3,-2],[6,-2,-1],[5,-2,4],[6,2,-2],[5,-2,1],[6,-2,3]],
            [[6,-2,2],[5,-2,4],[6,-2,1],[5,2,-2],[6,-2,-1],[5,-2,3],[6,-2,2],[5,4,-2]],
            [[5,-2,4],[6,-2,1],[5,3,-2],[6,-2,-1]],
        ],
        mini_diag={"a":6,"op":"-","b":2,"trick":"6+3-5","result":4},
    ),
    11: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,-2,3],[7,-3,2],[6,-2,-1],[8,-4,2],[5,3,-3],[7,-2,-3],[6,-4,2],[5,2,-2]],
            [[6,-3,1],[8,-2,-3],[5,-2,3],[7,-3,-1],[5,2,-4],[6,-2,1],[7,-4,3],[5,-3,2]],
            [[6,2,-3],[5,-2,1],[7,-3,2],[6,-4,3]],
        ],
        mini_diag=None,
    ),
    12: dict(
        title="Abacus Calculation: Decomposition of 5 (−1)",
        formula="−1 = +4 − 5",
        fingering="Fingering Ex.: 5−1",
        tables=[
            [[5,-1,4],[5,2,-1],[5,-1,3],[5,1,-1],[5,-1,2],[5,3,-1],[5,-1,1],[5,4,-1]],
            [[5,-1,4],[5,3,-1],[5,-1,1],[5,2,-1],[5,4,-1],[5,-1,3],[5,-1,2],[5,1,-1]],
            [[5,-1,4],[5,-1,2],[5,3,-1],[5,1,-1]],
        ],
        mini_diag={"a":5,"op":"-","b":1,"trick":"5+4-5","result":4},
    ),
    13: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,-1,3],[6,-2,2],[7,-3,1],[8,-4,2],[5,-1,2],[6,-3,2],[7,-2,1],[8,-3,2]],
            [[5,2,-1],[6,-2,3],[7,-1,-3],[5,3,-2],[6,1,-3],[7,-4,3],[8,-3,1],[5,2,-3]],
            [[6,-1,2],[7,-3,1],[8,-4,3],[5,-2,1]],
        ],
        mini_diag=None,
    ),
    14: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[7,-3,2],[8,-4,1],[5,-1,3],[6,-2,1],[7,-2,-1],[5,3,-4],[6,-3,2],[8,-1,-3]],
            [[5,-1,4],[6,-4,3],[7,-2,-3],[5,2,-3],[6,-1,-2],[8,-3,1],[7,-4,2],[5,4,-3]],
            [[8,-4,3],[5,-3,1],[6,-2,2],[7,-1,3]],
        ],
        mini_diag=None,
    ),
    15: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[6,-1,-2],[5,3,-4],[7,-2,1],[8,-3,2],[6,-2,3],[5,4,-3],[7,-3,1],[8,-1,-2]],
            [[5,2,-3],[7,-4,3],[6,-3,2],[8,-2,-3],[5,-1,2],[6,-4,3],[7,-2,1],[8,-3,2]],
            [[5,-1,3],[7,-3,2],[6,-2,1],[8,-4,3]],
        ],
        mini_diag=None,
    ),
    # ── Composition of 10 phase ────────────────────────────────────────
    19: dict(
        title="Abacus Calculation: Composition of 10 (+9)",
        formula="+9 = −1 + 10",
        fingering="Fingering Ex.: 1+9, 2+9, 3+9, 4+9, 6+9, 7+9, 8+9, 9+9",
        tables=[
            [[1,9,-3],[2,9,-4],[3,9,-2],[4,9,-3],[6,9,-4],[7,9,-3],[8,9,-2],[9,9,-3]],
            [[2,9,-1],[3,9,-4],[4,9,-2],[6,9,-3],[7,9,-4],[1,9,-2],[8,9,-3],[9,9,-4]],
            [[3,9,-2],[6,9,-4],[8,9,-3],[9,9,-2]],
        ],
        mini_diag={"a":3,"op":"+","b":9,"trick":"3-1+10","result":12},
    ),
    20: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[2,9,-3],[3,-1,9],[4,9,-2],[5,-2,9],[6,9,-3],[7,9,-4],[8,-3,9],[2,-1,9]],
            [[5,9,-4],[3,9,-2],[6,-4,9],[4,9,-3],[2,-1,9],[7,-3,9],[5,9,-1],[6,9,-2]],
            [[3,9,-1],[4,-2,9],[7,9,-3],[8,9,-4]],
        ],
        mini_diag=None,
    ),
    21: dict(
        title="Abacus Calculation: Composition of 10 (+8)",
        formula="+8 = −2 + 10",
        fingering="Fingering Ex.: 2+8, 3+8, 4+8, 6+8, 7+8, 8+8, 9+8",
        tables=[
            [[2,8,-3],[3,8,-2],[4,8,-1],[6,8,-3],[7,8,-2],[8,8,-1],[9,8,-3],[2,8,-4]],
            [[3,8,-3],[4,8,-2],[5,8,-1],[6,8,-4],[7,8,-3],[8,8,-2],[9,8,-1],[3,8,-2]],
            [[4,8,-3],[6,8,-2],[7,8,-3],[9,8,-4]],
        ],
        mini_diag={"a":4,"op":"+","b":8,"trick":"4-2+10","result":12},
    ),
    22: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[3,8,-2],[4,9,-3],[5,8,-1],[6,9,-2],[7,8,-3],[8,9,-2],[2,8,-1],[5,9,-4]],
            [[4,-1,8],[5,9,-2],[6,8,-1],[7,-2,9],[3,8,-2],[8,-1,9],[5,8,-3],[6,9,-4]],
            [[3,9,-2],[4,8,-1],[6,8,-3],[7,9,-2]],
        ],
        mini_diag=None,
    ),
    23: dict(
        title="Abacus Calculation: Composition of 10 (+7)",
        formula="+7 = −3 + 10",
        fingering="Fingering Ex.: 3+7, 4+7, 8+7, 9+7",
        tables=[
            [[3,7,-2],[4,7,-3],[8,7,-1],[9,7,-2],[3,7,-1],[4,7,-2],[8,7,-3],[9,7,-1]],
            [[4,7,-1],[3,7,-3],[8,7,-2],[9,7,-3],[3,7,-2],[4,7,-1],[8,7,-2],[9,7,-2]],
            [[3,7,-3],[4,7,-2],[8,7,-3],[9,7,-1]],
        ],
        mini_diag={"a":4,"op":"+","b":7,"trick":"4-3+10","result":11},
    ),
    24: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[3,7,-2],[4,8,-3],[5,9,-4],[6,7,-2],[7,8,-3],[8,7,-1],[9,8,-4],[3,9,-3]],
            [[4,7,-2],[5,8,-3],[6,9,-1],[7,7,-3],[8,8,-2],[9,7,-1],[3,8,-2],[4,9,-3]],
            [[5,7,-3],[6,8,-2],[7,9,-3],[8,7,-1]],
        ],
        mini_diag=None,
    ),
    27: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[2,9,-3],[3,8,-2],[4,7,-1],[5,8,-3],[6,9,-2],[7,8,-3],[8,9,-1],[9,8,-2]],
            [[3,7,-2],[4,9,-3],[5,8,-2],[6,7,-1],[7,9,-3],[8,8,-2],[9,7,-3],[3,9,-1]],
            [[4,8,-2],[5,7,-1],[6,9,-3],[7,8,-2]],
        ],
        mini_diag=None,
    ),
    28: dict(
        title="Abacus Calculation: Composition of 10 (+6)",
        formula="+6 = −4 + 10",
        fingering="Fingering Ex.: 4+6, 9+6",
        tables=[
            [[4,6,-2],[9,6,-3],[4,6,-1],[9,6,-2],[4,6,-3],[9,6,-1],[4,6,-2],[9,6,-3]],
            [[9,6,-2],[4,6,-3],[9,6,-1],[4,6,-2],[9,6,-3],[4,6,-1],[9,6,-2],[4,6,-3]],
            [[4,6,-1],[9,6,-3],[4,6,-2],[9,6,-1]],
        ],
        mini_diag={"a":4,"op":"+","b":6,"trick":"4-4+10","result":10},
    ),
    29: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[3,7,-2],[4,8,-3],[5,9,-1],[6,6,-2],[7,7,-3],[8,8,-1],[9,9,-2],[3,6,-1]],
            [[4,7,-3],[5,8,-2],[6,9,-1],[7,6,-3],[8,7,-2],[9,8,-3],[3,9,-2],[4,6,-1]],
            [[5,7,-2],[6,8,-3],[7,9,-1],[8,6,-2]],
        ],
        mini_diag=None,
    ),
    30: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[4,9,-3],[5,8,-2],[6,7,-1],[7,6,-3],[8,9,-2],[9,8,-3],[3,7,-1],[4,6,-2]],
            [[5,9,-3],[6,8,-2],[7,7,-1],[8,6,-3],[9,9,-2],[3,8,-1],[4,7,-3],[5,6,-2]],
            [[6,9,-2],[7,8,-3],[8,7,-1],[9,6,-2]],
        ],
        mini_diag=None,
    ),
    31: dict(
        title="Abacus Calculation: Composition of 10 (+5)",
        formula="+5 = −5 + 10",
        fingering="Fingering Ex.: 5+5, 6+5, 7+5, 8+5, 9+5",
        tables=[
            [[5,5,-2],[6,5,-3],[7,5,-1],[8,5,-2],[9,5,-3],[5,5,-1],[6,5,-2],[7,5,-3]],
            [[8,5,-1],[9,5,-2],[5,5,-3],[6,5,-1],[7,5,-2],[8,5,-3],[9,5,-1],[5,5,-2]],
            [[6,5,-3],[7,5,-1],[8,5,-2],[9,5,-3]],
        ],
        mini_diag={"a":7,"op":"+","b":5,"trick":"7-5+10","result":12},
    ),
    32: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,6,-2],[6,7,-3],[7,8,-1],[8,9,-2],[5,5,-3],[6,6,-1],[7,7,-2],[8,8,-3]],
            [[9,5,-2],[5,9,-3],[6,8,-1],[7,7,-2],[8,6,-3],[9,5,-1],[5,8,-2],[6,7,-3]],
            [[7,9,-1],[8,8,-2],[9,7,-3],[5,6,-1]],
        ],
        mini_diag=None,
    ),
}


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))

    # Cover
    page_cover(c); c.showPage()

    # Concept and calc pages in order
    page_01(c); c.showPage()
    page_02(c); c.showPage()
    page_03(c); c.showPage()
    page_04(c); c.showPage()

    # Calc pages 5-15 (with page 9 being the special "Look for the Answer")
    for pn in [5, 6, 7, 8]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()

    page_09(c); c.showPage()

    for pn in [10, 11, 12, 13, 14, 15]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()

    page_16(c); c.showPage()
    page_17(c); c.showPage()
    page_18(c); c.showPage()

    for pn in [19, 20, 21, 22, 23, 24]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()

    page_25(c); c.showPage()
    page_26(c); c.showPage()

    for pn in [27, 28, 29, 30, 31, 32]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()

    page_33(c); c.showPage()
    page_34(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"Total pages: 35 (cover + 34)")


if __name__ == "__main__":
    main()
