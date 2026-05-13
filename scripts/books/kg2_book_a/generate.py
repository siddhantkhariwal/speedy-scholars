#!/usr/bin/env python3
"""
Speedy Scholars — KG-2 Book A Workbook Generator
Sequel to KG-1 Book B. Advanced Composition of 10 (revisits +1..+9 with
two-digit results and new +8/+9 two-step formulas) followed by Mental
Calculation (visualizing the abacus).

Page furniture lives in scripts/books/_shared/chrome.py.
Book-specific decisions documented in NOTES.md.
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

set_book("KG-2 Book A")
OUTPUT_PATH = os.path.join(PUBLIC_DIR, "Speedy-Scholars-KG2-Book-A.pdf")


# ─── COVER ───────────────────────────────────────────────────────────────
def page_cover(c):
    bg(c)
    c.setStrokeColor(GOLD); c.setLineWidth(3)
    c.roundRect(12 * mm, 12 * mm, W - 24 * mm, H - 24 * mm, 8, stroke=1, fill=0)
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(1)
    c.roundRect(15 * mm, 15 * mm, W - 30 * mm, H - 30 * mm, 6, stroke=1, fill=0)
    # Mascots
    draw_bead_bird(c, 55 * mm, H - 40 * mm, 32, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - 55 * mm, H - 40 * mm, 30, BROWN, "left", "wink", hat="graduation")
    draw_bead_bird(c, 45 * mm, 50 * mm, 28, LIGHT_GOLD, "right", "surprised")
    draw_bead_bird(c, W - 50 * mm, 55 * mm, 30, GOLD, "left", "happy", action="waving")
    for i in range(15):
        random.seed(i + 400)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm),
                  random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm,
                    height=55 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-2  BOOK A")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Composition of 10 Advanced & Mental Calculation")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 90 * mm, H - 137 * mm, W / 2 + 90 * mm, H - 137 * mm)
    for i, (u, l, lb) in enumerate([(1, 2, "7"), (1, 3, "8"), (1, 4, "9")]):
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


# ─── PAGE 1: VISUAL COMPOSITION OF 10 ────────────────────────────────────
# Three cards: each shows the formula text + two object groups + vertical sum + result box
def page_01(c):
    bg(c); y = draw_hdr(c, "Composition of 10",
                        "Each problem rewrites as a two-step trick"); draw_footer(c, 1)
    scatter_decorations(c, 1)

    problems = [(7, 5, 12, "7+5 : 7−5+10 = 12", draw_apple),
                (9, 4, 13, "9+4 : 9−6+10 = 13", draw_flower),
                (8, 3, 11, "8+3 : 8−7+10 = 11", draw_strawberry)]

    avail_h = y - 18 * mm - 4
    card_h = avail_h / 3 - 8
    obj_s = 13

    for i, (a, b, ans, formula, fn) in enumerate(problems):
        cy = y - (i + 1) * (card_h + 8) + 8

        # Main card (object groups + formula text below)
        main_w = CW - 100
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(MARGIN, cy, main_w, card_h, 4, stroke=1, fill=1)

        # Object area (top portion)
        obj_y = cy + card_h * 0.62
        obj_sp = obj_s + 4
        a_start = MARGIN + 20
        for j in range(a):
            fn(c, a_start + j * obj_sp, obj_y, size=obj_s)
        # Plus sign
        plus_x = MARGIN + 20 + a * obj_sp + 14
        c.setFont("Helvetica-Bold", 16); c.setFillColor(DARKER_BROWN)
        c.drawString(plus_x, obj_y - 5, "+")
        # b group
        b_start = plus_x + 22
        for j in range(b):
            fn(c, b_start + j * obj_sp, obj_y, size=obj_s)

        # Formula text below the objects
        c.setFont("Helvetica-Bold", 13); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 20, cy + 16, formula)

        # Right side: vertical sum
        rs_x = MARGIN + main_w + 12
        rs_w = CW - main_w - 12
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(rs_x, cy, rs_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 22); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 30, str(a))
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 56, str(b))  # no + sign
        # Underline + answer box
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(rs_x + 12, cy + card_h - 68, rs_x + rs_w - 12, cy + card_h - 68)
        c.setFillColor(white); c.setStrokeColor(GOLD)
        c.rect(rs_x + rs_w / 2 - 16, cy + 12, 32, 24, stroke=1, fill=1)


# ─── PAGE 2: BANNER MASCOTS WITH 3-OP MIXED PROBLEMS ──────────────────────
def page_02(c):
    bg(c); y = draw_hdr(c, "Three-Step Problems",
                        "Speedy mascots fly high — solve each problem"); draw_footer(c, 2)
    scatter_decorations(c, 2)

    problems = ["7 − 3 + 6 =", "9 + 7 − 4 =", "9 + 6 − 1 =",
                "6 − 3 + 8 =", "8 − 4 + 9 =", "5 + 6 − 3 =",
                "7 − 2 + 4 =", "6 + 8 − 5 ="]

    # 2 rows × 4 columns of mascot+banner pairs filling the available area
    avail_top = y - 20
    avail_bot = 22 * mm + 16
    avail_h = avail_top - avail_bot

    rows = 2
    cols_n = 4
    cell_w = CW / cols_n
    cell_h = avail_h / rows

    for i, prob in enumerate(problems):
        col = i % cols_n
        row = i // cols_n
        cx = MARGIN + (col + 0.5) * cell_w
        cy = avail_top - (row + 0.5) * cell_h

        # Cloud puffs (light gold) behind the banner — bigger now
        c.setFillColor(LIGHT_GOLD); c.setStrokeColor(LIGHT_GOLD)
        for dx, dy, dr in [(-44, 4, 18), (-18, 14, 22), (12, 14, 22), (40, 4, 18),
                            (-30, -8, 16), (28, -8, 16)]:
            c.circle(cx + dx, cy + dy, dr, stroke=0, fill=1)
        # Banner
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.4)
        c.roundRect(cx - 62, cy - 16, 124, 32, 5, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 15); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(cx, cy - 4, prob)
        # Mascot — bigger and sitting on top of the cloud
        expr = ["happy", "wink", "surprised", "thinking"][i % 4]
        face = "left" if i % 2 == 0 else "right"
        draw_bead_bird(c, cx + (28 if face == "left" else -28), cy + 40, 30,
                       GOLD if i % 2 == 0 else BROWN, face, expr,
                       hat="graduation")


# ─── PAGE 8: MATCH BIRDS IN A RING ──────────────────────────────────────
def page_08(c):
    bg(c); y = draw_hdr(c, "Match the Birds to Form 10",
                        "Draw a line between each pair of mascots that sums to 10"); draw_footer(c, 8)
    scatter_decorations(c, 8)

    # Center coordinates
    cx = W / 2
    cy = (y + 22 * mm) / 2 - 5
    radius = min((y - 22 * mm) / 2 - 20, CW / 2 - 80)

    # Center medallion: Speedy Scholars badge
    c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.5)
    c.circle(cx, cy, 40, stroke=1, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(cx, cy + 4, "Speedy")
    c.drawCentredString(cx, cy - 8, "Scholars")

    # 10 mascots positioned in a ring (digits 1-9 plus 5 duplicate, in random-but-fixed order)
    digits = [1, 4, 7, 9, 2, 8, 5, 3, 6, 5]
    colors = [GOLD, BROWN, LIGHT_GOLD, GOLD, LIGHT_BROWN, BROWN, GOLD, LIGHT_GOLD, GOLD, BROWN]
    for i, (dig, col) in enumerate(zip(digits, colors)):
        ang = 2 * math.pi * i / len(digits) + math.pi / 2  # start at top
        mx = cx + radius * math.cos(ang)
        my = cy + radius * math.sin(ang)
        # Mascot
        draw_bead_bird(c, mx, my, 26, col, "right" if math.cos(ang) >= 0 else "left",
                       ["happy", "wink", "surprised", "thinking"][i % 4],
                       hat="graduation")
        # Number badge
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.circle(mx + 18 * (1 if math.cos(ang) >= 0 else -1), my - 18, 11,
                 stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 13)
        c.drawCentredString(mx + 18 * (1 if math.cos(ang) >= 0 else -1), my - 22, str(dig))


# ─── PAGE 13: VISUAL CARDS (2 BIG) ───────────────────────────────────────
def page_13(c):
    bg(c); y = draw_hdr(c, "Composition of 10",
                        "Each visual problem rewrites to a 10-trick"); draw_footer(c, 13)
    scatter_decorations(c, 13)

    problems = [(7, 6, 13, "7 + 6 : 7 − 4 + 10 = ( 13 )", draw_apple),
                (7, 7, 14, "7 + 7 : 7 − 3 + 10 = ( 14 )", draw_strawberry)]

    avail_h = y - 18 * mm - 8
    card_h = avail_h / 2 - 6
    obj_s = 16

    for i, (a, b, ans, formula, fn) in enumerate(problems):
        cy = y - (i + 1) * (card_h + 6) + 6

        # Left: object area + formula
        left_w = CW - 110
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(MARGIN, cy, left_w, card_h, 4, stroke=1, fill=1)

        # Formula at top
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 16, cy + card_h - 22, formula.replace(str(ans), "____"))

        # Single-row layout: a objects + plus + b objects
        obj_sp = obj_s + 4
        ay = cy + card_h * 0.42
        a_start = MARGIN + 24
        for j in range(a):
            fn(c, a_start + j * obj_sp, ay, size=obj_s)
        plus_x = a_start + a * obj_sp + 10
        c.setFont("Helvetica-Bold", 18); c.setFillColor(DARKER_BROWN)
        c.drawString(plus_x, ay - 6, "+")
        b_start = plus_x + 22
        for j in range(b):
            fn(c, b_start + j * obj_sp, ay, size=obj_s)

        # Right: vertical sum
        rs_x = MARGIN + left_w + 12
        rs_w = CW - left_w - 12
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(rs_x, cy, rs_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 26); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 36, str(a))
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 68, str(b))  # no + sign
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(rs_x + 14, cy + card_h - 84, rs_x + rs_w - 14, cy + card_h - 84)
        c.setFillColor(white); c.setStrokeColor(GOLD)
        c.rect(rs_x + rs_w / 2 - 22, cy + 14, 44, 28, stroke=1, fill=1)


# ─── PAGE 15: JIGSAW PUZZLE ──────────────────────────────────────────────
def page_15(c):
    bg(c); y = draw_hdr(c, "Abacus Calculation",
                        "Solve every piece of the puzzle and write the answer in the circle"); draw_footer(c, 15)
    scatter_decorations(c, 15)

    # Build a 4×3 tessellation of warm-toned regions, each with a problem + circle
    panel_x = MARGIN + 20
    panel_top = y - 12
    panel_h = panel_top - 22 * mm - 20
    panel_w = CW - 40

    cols, rows = 4, 3
    cell_w = panel_w / cols
    cell_h = panel_h / rows

    problems = [
        ("3 + 8 + 1", 12), ("5 − 2 + 7", 10), ("6 − 4 + 8", 10), ("7 + 2 − 3", 6),
        ("4 + 9 − 5", 8),  ("3 + 6 − 2", 7),  ("8 − 3 + 5", 10), ("9 + 1 − 4", 6),
        ("5 + 4 − 2", 7),  ("7 − 5 + 9", 11), ("2 + 7 + 3", 12), ("6 + 4 − 8", 2),
    ]

    fills = [WARM_WHITE, LIGHT_GOLD, CREAM, LIGHT_GOLD, WARM_WHITE, LIGHT_GOLD,
             CREAM, LIGHT_GOLD, WARM_WHITE, LIGHT_GOLD, CREAM, WARM_WHITE]

    for i, ((prob, _ans), fill) in enumerate(zip(problems, fills)):
        col = i % cols; row = i // cols
        cx = panel_x + col * cell_w
        cy = panel_top - (row + 1) * cell_h

        # Quad cell with diagonal accent
        c.setFillColor(fill); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.rect(cx, cy, cell_w, cell_h, stroke=1, fill=1)
        # Tile diagonal accent
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.4)
        c.line(cx, cy + cell_h, cx + cell_w * 0.5, cy + cell_h * 0.5)

        # Problem text
        c.setFont("Helvetica-Bold", 13); c.setFillColor(DARKER_BROWN)
        c.drawString(cx + 10, cy + cell_h / 2 - 6, prob)

        # Answer circle on the right
        c.setFillColor(white); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.circle(cx + cell_w - 22, cy + cell_h / 2, 14, stroke=1, fill=1)

    # Mascots peeking out at bottom corners
    draw_bead_bird(c, MARGIN + 30, 26 * mm, 22, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - MARGIN - 30, 26 * mm, 22, BROWN, "left", "wink", hat="graduation")


# ─── PAGE 18: THE LITTLE CINEMA ───────────────────────────────────────────
def page_18(c):
    bg(c); y = draw_hdr(c, "The Little Cinema",
                        "Solve each problem and lead each mascot to its numbered seat"); draw_footer(c, 18)
    scatter_decorations(c, 18)

    # 9 chairs with numbers in top half
    chair_numbers = [15, 4, 12, 6, 16, 7, 5, 17, 11]
    chair_y_top = y - 18
    chair_y_bot = y - 80
    chair_w = CW / 9 - 6
    chair_h = chair_y_top - chair_y_bot

    for i, n in enumerate(chair_numbers):
        cx = MARGIN + i * (CW / 9) + 3
        # Chair: backrest + seat (simplified)
        c.setFillColor(BROWN); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        # Backrest
        c.rect(cx + chair_w * 0.15, chair_y_bot + chair_h * 0.2,
               chair_w * 0.7, chair_h * 0.55, stroke=1, fill=1)
        # Seat (gold)
        c.setFillColor(GOLD)
        c.rect(cx + chair_w * 0.05, chair_y_bot + chair_h * 0.1,
               chair_w * 0.9, chair_h * 0.2, stroke=1, fill=1)
        # Legs
        c.line(cx + chair_w * 0.15, chair_y_bot + chair_h * 0.1,
               cx + chair_w * 0.15, chair_y_bot)
        c.line(cx + chair_w * 0.85, chair_y_bot + chair_h * 0.1,
               cx + chair_w * 0.85, chair_y_bot)
        # Number badge on backrest
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN)
        c.rect(cx + chair_w * 0.3, chair_y_bot + chair_h * 0.5,
               chair_w * 0.4, chair_h * 0.22, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(cx + chair_w / 2,
                            chair_y_bot + chair_h * 0.56, str(n))

    # 9 mascot+problem pairs at bottom
    problems = ["1+3+8", "2+6−4", "6+2+8", "7−5+9", "3+5+9",
                "2+5+8", "6−2+1", "8−6+4", "3+1+3"]
    band_y_top = chair_y_bot - 8
    band_y_bot = 22 * mm + 8
    band_h = band_y_top - band_y_bot
    mascot_w = CW / 9

    for i, prob in enumerate(problems):
        mx = MARGIN + i * mascot_w + mascot_w / 2
        # Mascot
        draw_bead_bird(c, mx, band_y_bot + band_h * 0.62, 18,
                       [GOLD, BROWN, LIGHT_GOLD][i % 3],
                       "right" if i % 2 == 0 else "left",
                       ["happy", "wink", "surprised", "thinking"][i % 4],
                       hat="graduation")
        # Problem text below
        c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(mx, band_y_bot + 4, prob)


# ─── PAGE 22: VISUAL CARDS (5+8 and 5+9) ──────────────────────────────────
def page_22(c):
    bg(c); y = draw_hdr(c, "Composition of 10 — Bigger Sums",
                        "Two new tricks: +8 and +9 with starts of 5+"); draw_footer(c, 22)
    scatter_decorations(c, 22)

    problems = [(5, 8, 13, "5 + 8 = 5 − 2 + 10", draw_fish),
                (5, 9, 14, "5 + 9 = 5 − 1 + 10", draw_apple)]

    avail_h = y - 18 * mm - 8
    card_h = avail_h / 2 - 6
    obj_s = 18

    for i, (a, b, ans, formula, fn) in enumerate(problems):
        cy = y - (i + 1) * (card_h + 8) + 8

        left_w = CW - 110
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(MARGIN, cy, left_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + 16, cy + card_h - 20, formula)

        # Single row of a + b objects (a=5, b up to 9, total 13-14)
        obj_sp = obj_s + 4
        ay = cy + card_h * 0.42
        for j in range(a):
            fn(c, MARGIN + 16 + j * obj_sp, ay, size=obj_s)
        plus_x = MARGIN + 16 + a * obj_sp + 12
        c.setFont("Helvetica-Bold", 20); c.setFillColor(DARKER_BROWN)
        c.drawString(plus_x, ay - 6, "+")
        b_start = plus_x + 22
        for j in range(b):
            fn(c, b_start + j * obj_sp, ay, size=obj_s)

        # Right: vertical sum
        rs_x = MARGIN + left_w + 12
        rs_w = CW - left_w - 12
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(rs_x, cy, rs_w, card_h, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 26); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 36, str(a))
        c.drawCentredString(rs_x + rs_w / 2, cy + card_h - 68, str(b))  # no + sign
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(rs_x + 14, cy + card_h - 84, rs_x + rs_w - 14, cy + card_h - 84)
        c.setFillColor(white); c.setStrokeColor(GOLD)
        c.rect(rs_x + rs_w / 2 - 22, cy + 14, 44, 28, stroke=1, fill=1)


# ─── PAGE 23: RABBITS TO HOUSES ───────────────────────────────────────────
def page_23(c):
    bg(c); y = draw_hdr(c, "Match the Mascot to its House",
                        "Solve each problem and draw a line to the matching house"); draw_footer(c, 23)
    scatter_decorations(c, 23)

    # Left: 8 mascots with problems
    problems = [(8, 8, 16), (2, 9, 11), (1, 9, 10), (8, 6, 14),
                (6, 5, 11), (7, 9, 16), (5, 9, 14), (6, 4, 10)]

    avail_h = y - 18 * mm - 8
    mascot_zone_w = CW * 0.4
    house_zone_x = MARGIN + mascot_zone_w + 40
    house_zone_w = CW - mascot_zone_w - 40

    cols = 2; rows = 4
    cell_w = mascot_zone_w / cols
    cell_h = avail_h / rows

    for i, (a, b, _ans) in enumerate(problems):
        col = i % cols; row = i // cols
        mx = MARGIN + col * cell_w + cell_w / 2
        my = y - (row + 1) * cell_h + cell_h / 2 - 4
        # Mascot
        col_choice = [GOLD, BROWN, LIGHT_GOLD, LIGHT_BROWN][i % 4]
        draw_bead_bird(c, mx, my + 16, 22, col_choice, "right",
                       ["happy", "wink", "surprised", "thinking"][i % 4],
                       hat="graduation")
        # Problem badge below
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(mx - 30, my - 18, 60, 18, 3, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(mx, my - 11, f"{a} + {b}")

    # Right: 4 houses with numbers
    houses = [16, 14, 11, 10]
    h_cols = 2; h_rows = 2
    h_cell_w = house_zone_w / h_cols
    h_cell_h = avail_h / h_rows
    for i, n in enumerate(houses):
        col = i % h_cols; row = i // h_cols
        hx = house_zone_x + col * h_cell_w + h_cell_w / 2
        hy = y - (row + 1) * h_cell_h + h_cell_h / 2

        # House body
        hw = 70; hh = 60
        c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1.2)
        c.rect(hx - hw / 2, hy - hh / 2, hw, hh, stroke=1, fill=1)
        # Roof (triangle)
        c.setFillColor(BROWN)
        p = c.beginPath()
        p.moveTo(hx - hw / 2 - 6, hy + hh / 2)
        p.lineTo(hx, hy + hh / 2 + 26)
        p.lineTo(hx + hw / 2 + 6, hy + hh / 2)
        p.close()
        c.drawPath(p, stroke=1, fill=1)
        # Door
        c.setFillColor(BROWN)
        c.rect(hx - 8, hy - hh / 2, 16, 30, stroke=1, fill=1)
        # Number on roof
        c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(hx, hy + hh / 2 + 6, str(n))


# ─── PAGE 28: HOW TO CALCULATE WHEN SUM > 9 ───────────────────────────────
def page_28(c):
    bg(c); y = draw_hdr(c, "How to Calculate When the Sum is More Than 9",
                        "Every digit 6, 7, 8, 9 is made of 5 plus a part"); draw_footer(c, 28)
    scatter_decorations(c, 28)

    # Mascot with thought bubble on left
    draw_bead_bird(c, MARGIN + 60, y - 80, 36, GOLD, "right", "thinking",
                   hat="graduation")
    # Thought bubble
    bub_x = MARGIN + 110
    bub_y = y - 50
    c.setFillColor(WARM_WHITE); c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
    c.roundRect(bub_x, bub_y - 40, 160, 56, 8, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(bub_x + 10, bub_y - 6, "How to calculate")
    c.drawString(bub_x + 10, bub_y - 18, "when the sum is")
    c.drawString(bub_x + 10, bub_y - 30, "more than 9?")

    # Right side: examples
    ex_x = MARGIN + 300
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(ex_x, y - 30, "Examples:")
    for i, ex in enumerate(["5 + 6 = ?", "5 + 7 = ?", "5 + 8 = ?", "5 + 9 = ?"]):
        c.setFont("Helvetica", 12); c.setFillColor(BROWN)
        c.drawString(ex_x + (i % 2) * 100, y - 50 - (i // 2) * 18, ex)

    # Composition trees: 6,7,8,9 each split into 5 + remainder
    tree_y = y - 130
    tree_xs = [MARGIN + 80, MARGIN + 200, MARGIN + 320, MARGIN + 440]
    splits = [(6, 5, 1), (7, 5, 2), (8, 5, 3), (9, 5, 4)]
    for tx, (n, l, r) in zip(tree_xs, splits):
        # n at top
        c.setFillColor(GOLD); c.setStrokeColor(DARKER_BROWN)
        c.circle(tx, tree_y, 14, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 14)
        c.drawCentredString(tx, tree_y - 4, str(n))
        # Branches
        c.setStrokeColor(DARKER_BROWN); c.setLineWidth(1)
        c.line(tx - 6, tree_y - 14, tx - 18, tree_y - 36)
        c.line(tx + 6, tree_y - 14, tx + 18, tree_y - 36)
        # Children
        c.setFillColor(LIGHT_GOLD); c.setStrokeColor(DARKER_BROWN)
        c.circle(tx - 22, tree_y - 46, 11, stroke=1, fill=1)
        c.circle(tx + 22, tree_y - 46, 11, stroke=1, fill=1)
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold", 12)
        c.drawCentredString(tx - 22, tree_y - 50, str(l))
        c.drawCentredString(tx + 22, tree_y - 50, str(r))

    # Bottom: rule statements
    rule_y = 30 * mm + 10
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, rule_y + 60, "Adding 6, 7, 8 and 9:")
    rules = ["+ 6 = + 1 − 5 + 10",
             "+ 7 = + 2 − 5 + 10",
             "+ 8 = + 3 − 5 + 10",
             "+ 9 = + 4 − 5 + 10"]
    for i, rule in enumerate(rules):
        c.setFont("Helvetica", 12); c.setFillColor(BROWN)
        c.drawString(MARGIN + (i % 2) * 280, rule_y + 40 - (i // 2) * 18, rule)


# ─── PAGE 29: PROCESS OF MENTAL ARITHMETIC ───────────────────────────────
def page_29(c):
    bg(c); y = draw_hdr(c, "The Process of Mental Arithmetic",
                        "Picture the abacus in your mind — no fingers needed"); draw_footer(c, 29)
    scatter_decorations(c, 29)

    # 5 steps across the page
    steps = [("Close your eyes", "happy", None),
             ("Imagine the abacus", "thinking", "frame"),
             ("Imagine the beam", "thinking", "beam"),
             ("Imagine the rods", "thinking", "rods"),
             ("Imagine the beads", "surprised", "full")]

    step_w = CW / 5
    step_y_top = y - 12
    step_y_bot = step_y_top - 130

    for i, (label, expr, stage) in enumerate(steps):
        sx = MARGIN + i * step_w + step_w / 2
        # Mascot
        draw_bead_bird(c, sx, step_y_top - 30, 26, GOLD, "right", expr,
                       hat="graduation")
        # Mini abacus or placeholder below
        ab_w = 40; ab_h = 50
        ab_x = sx - ab_w / 2
        ab_y = step_y_top - 90
        if stage is None:
            # Just a closed-eye blank box
            c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
            c.roundRect(ab_x, ab_y, ab_w, ab_h, 4, stroke=1, fill=1)
            c.setFont("Helvetica", 24); c.setFillColor(GOLD)
            c.drawCentredString(sx, ab_y + ab_h / 2 - 8, "z")
        elif stage == "frame":
            c.setStrokeColor(DARK_BROWN); c.setLineWidth(2); c.setFillColor(white)
            c.rect(ab_x, ab_y, ab_w, ab_h, stroke=1, fill=1)
        elif stage == "beam":
            c.setStrokeColor(DARK_BROWN); c.setLineWidth(2); c.setFillColor(white)
            c.rect(ab_x, ab_y, ab_w, ab_h, stroke=1, fill=1)
            c.setStrokeColor(BROWN); c.setLineWidth(2)
            c.line(ab_x, ab_y + ab_h * 0.6, ab_x + ab_w, ab_y + ab_h * 0.6)
        elif stage == "rods":
            c.setStrokeColor(DARK_BROWN); c.setLineWidth(2); c.setFillColor(white)
            c.rect(ab_x, ab_y, ab_w, ab_h, stroke=1, fill=1)
            c.setStrokeColor(BROWN); c.setLineWidth(2)
            c.line(ab_x, ab_y + ab_h * 0.6, ab_x + ab_w, ab_y + ab_h * 0.6)
            for k in range(3):
                rx = ab_x + (k + 1) * ab_w / 4
                c.line(rx, ab_y, rx, ab_y + ab_h)
        elif stage == "full":
            draw_abacus(c, ab_x, ab_y, ab_w, ab_h, 1, 2)
        # Label
        c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(sx, step_y_bot - 4, label)

    # Bottom: two practice examples
    ex_y_top = step_y_bot - 14
    ex_y_bot = 22 * mm + 8
    ex_h = ex_y_top - ex_y_bot

    for col, (start, ops, label) in enumerate([
            (1, ["+2", "+5"], "1 + 2 + 5 = ?"),
            (4, ["−1", "+3"], "4 − 1 + 3 = ?")]):
        bx = MARGIN + col * (CW / 2) + 20
        bw = CW / 2 - 40
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.6)
        c.roundRect(bx, ex_y_bot + 4, bw, ex_h - 8, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + 12, ex_y_top - 18, label)
        # Vertical sum on the right
        c.setFont("Helvetica-Bold", 18)
        c.drawString(bx + bw - 60, ex_y_top - 26, str(start))
        for k, op in enumerate(ops):
            c.drawString(bx + bw - 60, ex_y_top - 26 - (k + 1) * 22, op)


# ─── EXTENDED CALC PAGE (supports 10-col wide layout) ────────────────────
BOTTOM_STRIP_SETS = {
    # Composition of 10 phase — addition emphasized
    3:  [(4, "+", 6, draw_apple),   (9, "+", 4, draw_strawberry), (8, "+", 4, draw_fish),   (7, "+", 4, draw_flower)],
    4:  [(5, "+", 4, draw_strawberry),(6, "+", 4, draw_apple),    (7, "+", 4, draw_fish),   (9, "−", 4, draw_flower)],
    5:  [(7, "+", 3, draw_apple),   (8, "+", 3, draw_strawberry), (9, "+", 3, draw_fish),   (6, "+", 4, draw_flower)],
    9:  [(8, "+", 2, draw_apple),   (9, "+", 2, draw_strawberry), (7, "+", 3, draw_fish),   (6, "+", 4, draw_flower)],
    10: [(9, "+", 1, draw_flower),  (8, "+", 2, draw_apple),      (7, "+", 3, draw_strawberry),(6, "+", 4, draw_fish)],
    11: [(9, "+", 1, draw_apple),   (8, "+", 1, draw_fish),       (7, "+", 1, draw_flower), (9, "+", 2, draw_strawberry)],
    12: [(6, "+", 5, draw_strawberry),(7, "+", 5, draw_apple),    (8, "+", 5, draw_fish),   (9, "+", 5, draw_flower)],
    14: [(5, "+", 6, draw_apple),   (6, "+", 6, draw_strawberry), (7, "+", 6, draw_fish),   (8, "+", 6, draw_flower)],
    16: [(5, "+", 6, draw_strawberry),(6, "+", 6, draw_apple),    (7, "+", 6, draw_fish),   (4, "+", 6, draw_flower)],
    17: [(8, "+", 5, draw_apple),   (9, "+", 5, draw_strawberry), (5, "+", 5, draw_fish),   (7, "+", 5, draw_flower)],
    19: [(5, "+", 7, draw_strawberry),(6, "+", 7, draw_apple),    (7, "+", 7, draw_fish),   (4, "+", 7, draw_flower)],
    20: [(8, "+", 4, draw_apple),   (7, "+", 5, draw_strawberry), (6, "+", 6, draw_fish),   (9, "+", 2, draw_flower)],
    21: [(5, "+", 8, draw_strawberry),(6, "+", 8, draw_apple),    (4, "+", 8, draw_fish),   (5, "+", 9, draw_flower)],
    24: [(5, "+", 8, draw_apple),   (6, "+", 8, draw_strawberry), (5, "+", 8, draw_fish),   (6, "+", 8, draw_flower)],
    25: [(7, "+", 6, draw_strawberry),(8, "+", 5, draw_apple),    (5, "+", 8, draw_fish),   (6, "+", 8, draw_flower)],
    26: [(5, "+", 9, draw_apple),   (6, "+", 8, draw_strawberry), (7, "+", 7, draw_fish),   (8, "+", 6, draw_flower)],
}


def page_calc(c, pn, title, formula, fingering, tables, mini_diagram=None,
              wide=False):
    """Calc page. If wide=True, three 10-col single-row tables stacked, no strip."""
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
        # Three 10-col tables, no bottom strip
        for table_data in tables:
            cols = len(table_data)
            y = draw_calc_table(c, MARGIN, y, table_data, cols, None, table_width=CW)
            y -= 10
        return

    # Standard layout: 3 tables + bottom strip
    for table_data in tables:
        cols = len(table_data)
        y = draw_calc_table(c, MARGIN, y, table_data, cols, None, table_width=CW)
        y -= 8

    strip_y = 18 * mm
    strip_h = y - strip_y - 4
    if strip_h < 25: strip_h = 25
    strip_set = BOTTOM_STRIP_SETS.get(pn, [(5, "+", 4, draw_apple)] * 4)
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
    c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
    expr = f"{diag['a']} {diag['op']} {diag['b']}"
    c.drawCentredString(px + pw / 2, py + ph - 12, expr)
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


# ─── MENTAL CALCULATION PAGE ─────────────────────────────────────────────
def page_mental(c, pn, title, table_a, table_b=None, listening=False):
    """Mental calculation page. Two 10-col blocks (A, B), optional Listening
    Exercise sidebar with 10 numbered lines."""
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)

    sidebar_w = 60 if listening else 0
    main_w = CW - sidebar_w - (8 if listening else 0)

    # Block A
    y = _draw_mental_block(c, MARGIN, y, "A", table_a, main_w)

    # Block B
    if table_b:
        y -= 18
        y = _draw_mental_block(c, MARGIN, y, "B", table_b, main_w)

    # Listening sidebar on the right
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
    """Single mental-calc block: 'A' or 'B' on left, 10-col table to its right."""
    cols = len(table)
    rh = 18; sw = 24
    cw = (block_w - sw) / cols
    hf = 9

    # Header row
    hy = y - rh
    c.setFillColor(BROWN); c.rect(x, hy, sw, rh, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + sw / 2, hy + 5, "S.No.")
    for i in range(cols):
        cx = x + sw + i * cw
        c.setFillColor(BROWN); c.rect(cx, hy, cw, rh, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + cw / 2, hy + 5, str(i + 1))

    # 3 operand rows + 2 ANS rows
    labels = ["1", "2", "3", "Ans.", "Ans."]
    for ri, lab in enumerate(labels):
        ry = hy - (ri + 1) * rh
        is_ans = "Ans" in lab
        # S.No. column shows the block label on the first non-header row, then numbers
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
    3: dict(
        title="Abacus Calculation: Composition of 10 (+4)",
        formula="+4 = −6 + 10",
        fingering="Fingering Ex.: 6+4, 7+4, 8+4, 9+4",
        tables=[
            [[7,4,-1],[6,4,-3],[8,4,-2],[9,4,-1],[6,4,-2],[7,4,-3],[8,4,-1],[9,4,-2]],
            [[6,4,-1],[7,4,-2],[8,4,-3],[9,4,-1],[6,4,-2],[7,4,-1],[8,4,-2],[9,4,-3]],
            [[7,4,-1],[8,4,-2],[9,4,-3],[6,4,-1]],
        ],
        mini_diag={"a":7,"op":"+","b":4,"trick":"7-6+10","result":11},
    ),
    4: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[3,5,-2],[7,4,-1],[9,-3,5],[2,6,4],[6,8,-3],[8,-2,4],[4,5,-1],[2,6,-3]],
            [[5,-1,4],[7,-3,8],[4,3,-5],[5,2,-4],[9,-2,3],[7,-4,2],[6,-3,4],[5,3,-2]],
            [[7,3,-4],[3,6,2],[4,7,-1],[7,3,4]],
        ],
        mini_diag=None,
    ),
    5: dict(
        title="Abacus Calculation: Composition of 10 (+3)",
        formula="+3 = −7 + 10",
        fingering="Fingering Ex.: 7+3, 8+3, 9+3",
        tables=[
            [[8,3,-1],[7,3,-2],[9,3,-3],[7,3,-1],[8,3,-2],[9,3,-1],[7,3,-3],[8,3,-2]],
            [[9,3,-2],[7,3,-1],[8,3,-3],[9,3,-2],[7,3,-3],[8,3,-1],[9,3,-2],[7,3,-1]],
            [[8,3,-2],[9,3,-1],[7,3,-3],[8,3,-2]],
        ],
        mini_diag={"a":8,"op":"+","b":3,"trick":"8-7+10","result":11},
    ),
    9: dict(
        title="Abacus Calculation: Composition of 10 (+2)",
        formula="+2 = −8 + 10",
        fingering="Fingering Ex.: 8+2, 9+2",
        tables=[
            [[8,2,-1],[9,2,-2],[8,2,-3],[9,2,-1],[8,2,-2],[9,2,-1],[8,2,-3],[9,2,-2]],
            [[8,2,-3],[9,2,-1],[8,2,-2],[9,2,-3],[8,2,-1],[9,2,-2],[8,2,-3],[9,2,-1]],
            [[9,2,-3],[8,2,-1],[9,2,-2],[8,2,-3]],
        ],
        mini_diag={"a":8,"op":"+","b":2,"trick":"8-8+10","result":10},
    ),
    10: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,4,-3],[7,3,-2],[8,2,-1],[9,1,-3],[6,4,-2],[7,3,-1],[8,2,-3],[9,4,-2]],
            [[3,7,-2],[4,6,-1],[5,5,-3],[6,4,-2],[7,3,-1],[8,2,-3],[9,1,-2],[5,4,-3]],
            [[6,3,-1],[7,2,-3],[8,4,-2],[9,3,-1]],
        ],
        mini_diag=None,
    ),
    11: dict(
        title="Abacus Calculation: Composition of 10 (+1)",
        formula="+1 = −9 + 10",
        fingering="Fingering Ex.: 9+1",
        tables=[
            [[9,1,-2],[9,1,-3],[9,1,-1],[9,1,-2],[9,1,-3],[9,1,-1],[9,1,-2],[9,1,-3]],
            [[9,1,-1],[9,1,-2],[9,1,-3],[9,1,-1],[9,1,-2],[9,1,-3],[9,1,-1],[9,1,-2]],
            [[9,1,-3],[9,1,-1],[9,1,-2],[9,1,-3]],
        ],
        mini_diag={"a":9,"op":"+","b":1,"trick":"9-9+10","result":10},
    ),
    12: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[9,1,-3],[8,2,-1],[7,3,-2],[6,4,-1],[5,5,-3],[9,2,-1],[8,3,-2],[7,4,-3]],
            [[6,5,-1],[5,6,-2],[4,7,-3],[3,8,-2],[2,9,-1],[9,1,-2],[8,2,-3],[7,3,-1]],
            [[6,4,-2],[5,5,-3],[4,6,-1],[3,7,-2]],
        ],
        mini_diag=None,
    ),
    14: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,6,-2],[6,5,-1],[7,4,-3],[8,3,-2],[9,2,-1],[5,5,-3],[6,6,-2],[7,7,-3]],
            [[8,5,-2],[9,6,-3],[5,7,-1],[6,8,-2],[7,9,-3],[8,4,-1],[9,3,-2],[5,5,-3]],
            [[6,7,-1],[7,8,-2],[8,9,-3],[9,5,-1]],
        ],
        mini_diag=None,
    ),
    16: dict(
        title="Abacus Calculation: Composition of 10 (+6)",
        formula="+6 = −4 + 10",
        fingering="Fingering Ex.: 5+6, 6+6, 7+6",
        tables=[
            [[5,6,-2],[6,6,-3],[7,6,-1],[5,6,-3],[6,6,-2],[7,6,-1],[5,6,-3],[6,6,-1]],
            [[7,6,-2],[5,6,-1],[6,6,-3],[7,6,-2],[5,6,-3],[6,6,-1],[7,6,-2],[5,6,-3]],
            [[6,6,-1],[7,6,-2],[5,6,-3],[6,6,-2]],
        ],
        mini_diag={"a":5,"op":"+","b":6,"trick":"5-4+10","result":11},
    ),
    17: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,7,-2],[6,6,-3],[7,5,-1],[8,4,-2],[9,3,-1],[5,8,-2],[6,7,-3],[7,6,-1]],
            [[5,5,-3],[6,4,-2],[7,3,-1],[8,2,-3],[9,1,-2],[5,6,-1],[6,5,-2],[7,4,-3]],
            [[8,3,-1],[9,2,-2],[5,7,-3],[6,6,-1]],
        ],
        mini_diag=None,
    ),
    19: dict(
        title="Abacus Calculation: Composition of 10 (+7)",
        formula="+7 = −3 + 10",
        fingering="Fingering Ex.: 5+7, 6+7, 7+7",
        tables=[
            [[5,7,-2],[6,7,-3],[7,7,-1],[5,7,-3],[6,7,-2],[7,7,-1],[5,7,-3],[6,7,-2]],
            [[7,7,-1],[5,7,-2],[6,7,-3],[7,7,-1],[5,7,-3],[6,7,-2],[7,7,-1],[5,7,-2]],
            [[6,7,-3],[7,7,-1],[5,7,-2],[6,7,-3]],
        ],
        mini_diag={"a":5,"op":"+","b":7,"trick":"5-3+10","result":12},
    ),
    20: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,8,-1],[6,7,-2],[7,6,-3],[8,5,-1],[9,4,-2],[5,7,-3],[6,8,-1],[7,5,-2]],
            [[8,6,-3],[9,7,-1],[5,5,-2],[6,6,-3],[7,7,-1],[8,3,-2],[9,2,-3],[5,9,-1]],
            [[6,8,-2],[7,5,-3],[8,4,-1],[9,1,-2]],
        ],
        mini_diag=None,
    ),
    21: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,6,-2],[6,7,-3],[7,5,-1],[8,4,-2],[9,3,-1],[5,5,-2],[6,6,-3],[7,7,-1]],
            [[8,5,-3],[9,6,-2],[5,7,-1],[6,8,-3],[7,9,-2],[8,4,-1],[9,3,-3],[5,5,-2]],
            [[6,7,-1],[7,6,-2],[8,5,-3],[9,4,-1]],
        ],
        mini_diag=None,
    ),
    24: dict(
        title="Abacus Calculation: Composition of 10 (+8)",
        formula="+8 = +3 − 5 + 10",
        fingering="Fingering Ex.: 5+8, 6+8",
        tables=[
            [[5,8,-2],[6,8,-3],[5,8,-1],[6,8,-2],[5,8,-3],[6,8,-1],[5,8,-2],[6,8,-3]],
            [[5,8,-1],[6,8,-2],[5,8,-3],[6,8,-1],[5,8,-2],[6,8,-3],[5,8,-1],[6,8,-2]],
            [[5,8,-3],[6,8,-1],[5,8,-2],[6,8,-3]],
        ],
        mini_diag={"a":5,"op":"+","b":8,"trick":"5+3-5+10","result":13},
    ),
    25: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[5,8,-3],[6,8,-1],[5,7,-2],[6,7,-3],[5,6,-1],[6,6,-2],[5,5,-3],[6,5,-1]],
            [[7,8,-2],[8,7,-3],[9,6,-1],[5,5,-2],[6,4,-3],[7,3,-1],[8,2,-2],[9,1,-3]],
            [[5,8,-1],[6,7,-2],[7,5,-3],[8,4,-1]],
        ],
        mini_diag=None,
    ),
    26: dict(
        title="Abacus Calculation: Composition of 10 (+9)",
        formula="+9 = +4 − 5 + 10",
        fingering="Fingering Ex.: 5+9",
        tables=[
            [[5,9,-2],[5,9,-3],[5,9,-1],[5,9,-2],[5,9,-3],[5,9,-1],[5,9,-2],[5,9,-3]],
            [[5,9,-1],[5,9,-2],[5,9,-3],[5,9,-1],[5,9,-2],[5,9,-3],[5,9,-1],[5,9,-2]],
            [[5,9,-3],[5,9,-1],[5,9,-2],[5,9,-3]],
        ],
        mini_diag={"a":5,"op":"+","b":9,"trick":"5+4-5+10","result":14},
    ),
}

# Wide revision pages (10-col, no bottom strip)
WIDE_CALC_PAGES = {
    6: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[2,7,-5],[6,-3,7],[7,-1,3],[3,5,6],[6,-2,4],[8,5,-3],[5,3,-6],[6,2,-4],[6,3,-5],[2,7,-3]],
            [[3,-1,5],[5,-4,7],[5,-2,4],[5,3,-4],[5,8,-3],[1,3,8],[2,4,3],[3,5,-2],[4,6,-5],[5,7,-6]],
            [[1,6,2],[6,8,-7],[7,-2,8],[5,6,-3],[7,8,-3],[3,6,2],[2,7,5],[3,-2,8],[4,5,-3],[6,4,-2]],
        ],
        mini_diag=None,
    ),
    7: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[3,6,-2],[4,-2,5],[7,5,-3],[8,-3,5],[6,8,-4],[5,-2,3],[1,4,2],[6,7,-5],[2,7,8],[3,8,-2]],
            [[2,-1,5],[6,-3,7],[4,8,-4],[5,5,-3],[7,-3,5],[8,4,-1],[2,3,-1],[6,-2,5],[8,-4,7],[3,4,8]],
            [[1,4,2],[2,6,8],[6,4,-3],[4,-1,3],[5,6,-2],[3,7,-4],[2,8,5],[4,5,-2],[3,-2,7],[5,7,-3]],
        ],
        mini_diag=None,
    ),
    27: dict(
        title="Abacus Calculation: Revision",
        formula=None, fingering=None,
        tables=[
            [[1,5,2],[6,7,-4],[7,5,3],[3,6,5],[6,8,-3],[5,7,-6],[7,5,-2],[6,3,5],[8,4,-3],[3,6,2]],
            [[1,-1,4],[6,-3,5],[5,8,-2],[5,4,-3],[7,-2,6],[6,8,-4],[5,7,-3],[4,8,-2],[3,9,-1],[2,5,7]],
            [[4,5,-3],[7,-2,8],[6,5,-3],[5,4,-2],[7,3,8],[3,7,-2],[2,5,3],[6,4,-3],[5,6,-2],[7,8,-3]],
        ],
        mini_diag=None,
    ),
}


# ─── MENTAL CALC DATA (pages 30-34) ──────────────────────────────────────
MENTAL_CALC = {
    30: dict(
        title="Mental Calculation",
        a=[[1,1,2],[1,2,None],[3,1,-2],[2,-1,-1],[3,-1,-3],[4,-1,-1],[2,-2,-2],[4,-2,1],[1,2,-1],[3,-2,1]],
    ),
    31: dict(
        title="Mental Calculation",
        a=[[7,-6,5],[8,1,-5],[7,-5,2],[9,-3,4],[4,-2,-1],[3,6,-7],[2,4,1],[4,9,-2],[8,-1,5],[7,-5,2]],
        b=[[6,3,-7],[2,2,5],[4,3,2],[8,-6,8],[6,-5,3],[4,2,-3],[2,6,-5],[8,-4,-2],[2,-1,1],[8,-7,2]],
        listening=True,
    ),
    32: dict(
        title="Mental Calculation",
        a=[[7,-6,5],[8,1,-5],[2,7,-7],[4,-3,3],[8,5,-7],[5,3,-5],[1,4,5],[6,5,-7],[9,-2,-6],[7,-5,2]],
        b=[[6,3,-7],[8,-3,2],[7,-4,3],[3,4,-6],[6,-5,7],[5,2,-5],[1,6,-5],[7,-5,-2],[4,3,-4],[6,-2,2]],
        listening=True,
    ),
    33: dict(
        title="Mental Calculation",
        a=[[2,2,5],[5,3,-2],[3,-2,6],[5,3,-8],[8,5,-7],[3,-8,5],[5,1,-2],[4,4,-3],[7,-6,8],[4,5,-7]],
        b=[[5,2,1],[2,5,-5],[6,5,-5],[5,4,-2],[7,-3,5],[4,2,-3],[6,6,-5],[9,-5,-2],[8,-7,1],[3,4,6]],
        listening=True,
    ),
    34: dict(
        title="Mental Calculation",
        a=[[1,6,4],[6,-5,-2],[4,-2,3],[9,-7,2],[2,7,-7],[1,5,2],[3,1,6],[5,4,-6],[8,-2,-6],[7,-6,2]],
        b=[[7,1,-6],[3,5,-4],[9,-4,3],[8,-6,2],[3,5,-7],[2,2,5],[3,6,-5],[8,-6,1],[4,-2,1],[6,-2,3]],
        listening=True,
    ),
}


def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))

    page_cover(c); c.showPage()

    # p1-4
    page_01(c); c.showPage()
    page_02(c); c.showPage()
    for pn in [3, 4, 5]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    # p6, p7 — wide revision
    for pn in [6, 7]:
        cfg = WIDE_CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], None, wide=True)
        c.showPage()
    page_08(c); c.showPage()
    for pn in [9, 10, 11, 12]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    page_13(c); c.showPage()
    for pn in [14]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    page_15(c); c.showPage()
    for pn in [16, 17]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    page_18(c); c.showPage()
    for pn in [19, 20, 21]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    page_22(c); c.showPage()
    page_23(c); c.showPage()
    for pn in [24, 25, 26]:
        cfg = CALC_PAGES[pn]
        page_calc(c, pn, cfg["title"], cfg["formula"], cfg["fingering"],
                  cfg["tables"], cfg.get("mini_diag"))
        c.showPage()
    # p27 wide
    cfg = WIDE_CALC_PAGES[27]
    page_calc(c, 27, cfg["title"], cfg["formula"], cfg["fingering"],
              cfg["tables"], None, wide=True)
    c.showPage()
    page_28(c); c.showPage()
    page_29(c); c.showPage()
    # Mental Calculation pages
    for pn in [30, 31, 32, 33, 34]:
        cfg = MENTAL_CALC[pn]
        page_mental(c, pn, cfg["title"], cfg["a"], cfg.get("b"),
                    cfg.get("listening", False))
        c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print("Total pages: 35 (cover + 34)")


if __name__ == "__main__":
    main()
