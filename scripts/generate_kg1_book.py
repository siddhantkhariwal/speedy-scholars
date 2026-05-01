#!/usr/bin/env python3
"""
Speedy Scholars — KG-1 Book A Workbook Generator (v3)
Landscape A4, kid-friendly with mascots, big objects, dotted tracing, crosshair boxes.
"""

import os, sys, math, random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from illustrations import *

PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
LOGO_PATH = os.path.join(PROJECT_DIR, "public", "images", "logo3_transparent.png")
OUTPUT_PATH = os.path.join(PROJECT_DIR, "public", "Speedy-Scholars-KG1-Book-A.pdf")

W, H = landscape(A4)
MARGIN = 18 * mm
CW = W - 2 * MARGIN
CH = H - 2 * MARGIN
TF = HexColor("#FAF5EE")
TH = HexColor("#E8DDD0")


def draw_footer(c, pn):
    c.saveState()
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.5)
    c.line(MARGIN, 13 * mm, W - MARGIN, 13 * mm)
    c.setFont("Helvetica", 7); c.setFillColor(BROWN)
    c.drawString(MARGIN, 9 * mm, "Speedy Scholars - KG-1 Book A")
    c.drawRightString(W - MARGIN, 9 * mm, str(pn))
    c.restoreState()
    # Graduation hat mascot on every page (bottom-right area)
    page_mascot(c, pn)

def draw_hdr(c, title, sub=None):
    y = H - 16 * mm
    try:
        c.drawImage(LOGO_PATH, W - MARGIN - 30 * mm, y - 6 * mm, width=28 * mm, height=14 * mm,
                     preserveAspectRatio=True, mask='auto')
    except: pass
    c.setFont("Helvetica-Bold", 15); c.setFillColor(DARKER_BROWN); c.drawString(MARGIN, y, title)
    if sub:
        c.setFont("Helvetica", 9); c.setFillColor(BROWN); c.drawString(MARGIN, y - 13, sub)
    c.setStrokeColor(GOLD); c.setLineWidth(1.2)
    ly = y - (18 if sub else 6)
    c.line(MARGIN, ly, W - MARGIN - 35 * mm, ly)
    return ly - 6

def bg(c):
    c.setFillColor(CREAM); c.rect(0, 0, W, H, stroke=0, fill=1)

def instr(c, x, y, t):
    c.setFont("Helvetica-Oblique", 9); c.setFillColor(BROWN); c.drawString(x, y, t)

def page_mascot(c, pn):
    """Place a graduation-hat mascot consistently on every page."""
    # Bottom-right area, varies slightly per page for visual interest
    random.seed(pn + 500)
    mx = W - MARGIN - random.uniform(8, 15) * mm
    my = 18 * mm + random.uniform(5, 15)
    expr = ["happy", "wink", "thinking", "surprised"][pn % 4]
    draw_bead_bird(c, mx, my, 16, GOLD, "left", expr, hat="graduation")


def draw_calc_table(c, x, y, probs, cols=8, fing=None, table_width=None):
    tw = table_width or (CW * 0.72)
    cw = (tw - 32) / cols; rh = 18; sw = 32  # BIGGER rows and S.No. column
    hf = 9; df = 10  # header font, data font
    if fing:
        c.setFont("Helvetica", 7.5); c.setFillColor(BROWN)
        # Left-aligned, positioned between gold line and first table row
        c.drawString(x, y - 3, fing)
    hy = y - rh
    c.setFillColor(BROWN); c.rect(x, hy, sw, rh, stroke=0, fill=1)
    c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + sw / 2, hy + 5, "S.No.")
    for i in range(cols):
        cx = x + sw + i * cw
        c.setFillColor(BROWN); c.rect(cx, hy, cw, rh, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + cw / 2, hy + 5, str(i + 1))
    for ri, lab in enumerate(["1", "2", "3", "Ans."]):
        ry = hy - (ri + 1) * rh; ia = lab == "Ans."
        c.setFillColor(TH if ia else TF)
        c.rect(x, ry, sw, rh, stroke=0, fill=1)
        c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3)
        c.rect(x, ry, sw, rh, stroke=1, fill=0)
        c.setFillColor(DARKER_BROWN); c.setFont("Helvetica-Bold" if ia else "Helvetica", hf)
        c.drawCentredString(x + sw / 2, ry + 5, lab)
        for i in range(cols):
            cx = x + sw + i * cw
            c.setFillColor(TH if ia else TF); c.rect(cx, ry, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3); c.rect(cx, ry, cw, rh, stroke=1, fill=0)
            if not ia and i < len(probs) and ri < len(probs[i]) and probs[i][ri] is not None:
                v = probs[i][ri]
                c.setFillColor(DARKER_BROWN); c.setFont("Helvetica", df)
                c.drawCentredString(cx + cw / 2, ry + 5, str(v) if ri == 0 else (f"+{v}" if v > 0 else str(v)))
    return hy - 5 * rh - 4


# ══════════════════════════════════════════════════════════════
# PAGES
# ══════════════════════════════════════════════════════════════

def page_cover(c):
    bg(c)
    c.setStrokeColor(GOLD); c.setLineWidth(3)
    c.roundRect(12 * mm, 12 * mm, W - 24 * mm, H - 24 * mm, 8, stroke=1, fill=0)
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(1)
    c.roundRect(15 * mm, 15 * mm, W - 30 * mm, H - 30 * mm, 6, stroke=1, fill=0)
    # Mascots — BIG and visible
    draw_bead_bird(c, 55 * mm, H - 40 * mm, 32, GOLD, "right", "happy", hat="graduation")
    draw_bead_bird(c, W - 55 * mm, H - 40 * mm, 30, BROWN, "left", "wink")
    draw_bead_bird(c, 45 * mm, 50 * mm, 28, LIGHT_GOLD, "right", "surprised")
    draw_bead_bird(c, W - 50 * mm, 55 * mm, 30, GOLD, "left", "happy", action="waving")
    # Stars
    for i in range(15):
        random.seed(i + 200)
        draw_star(c, random.uniform(25 * mm, W - 25 * mm), random.uniform(25 * mm, H - 25 * mm),
                  3 + random.random() * 4, LIGHT_GOLD)
    # Logo
    try:
        c.drawImage(LOGO_PATH, (W - 100 * mm) / 2, H - 90 * mm, width=100 * mm, height=55 * mm,
                     preserveAspectRatio=True, mask='auto')
    except: pass
    c.setFont("Helvetica-Bold", 42); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, H - 115 * mm, "KG-1  BOOK A")
    c.setFont("Helvetica", 16); c.setFillColor(GOLD)
    c.drawCentredString(W / 2, H - 130 * mm, "Abacus Mental Arithmetic")
    c.setStrokeColor(GOLD); c.setLineWidth(2)
    c.line(W / 2 - 70 * mm, H - 137 * mm, W / 2 + 70 * mm, H - 137 * mm)
    # Abacuses — moved up to avoid overlap
    for i, (u, l, lb) in enumerate([(0, 3, "3"), (1, 0, "5"), (0, 4, "4")]):
        draw_abacus(c, W / 2 - 55 * mm + i * 45 * mm, H - 178 * mm, 22 * mm, 30 * mm, u, l, lb)
    # Info
    iw = 180 * mm; iy = 32 * mm
    c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1)
    c.roundRect((W - iw) / 2, iy, iw, 42 * mm, 5, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
    c.drawCentredString(W / 2, iy + 34 * mm, "Student Information")
    for i, f in enumerate(["Name:", "Level:", "Date:"]):
        fy = iy + 22 * mm - i * 10 * mm
        c.setFont("Helvetica-Bold", 10); c.setFillColor(BROWN); c.drawString((W - iw) / 2 + 10, fy, f)
        c.setStrokeColor(LIGHT_GOLD); c.setDash(1, 2)
        c.line((W - iw) / 2 + 35 * mm, fy - 2, (W + iw) / 2 - 10, fy - 2); c.setDash()
    c.setFont("Helvetica", 9); c.setFillColor(BROWN)
    c.drawCentredString(W / 2, 18 * mm, "www.speedyscholars.com")


def page_01(c):
    """Page 1: Description — MULTIPLE progressive abacus diagrams + mascots interacting."""
    bg(c); y = draw_hdr(c, "Description of the Abacus"); draw_footer(c, 1)
    scatter_decorations(c, 1)

    # 5 progressive illustrations: Frame, Beam, Rod, Upper Bead, Lower Bead + Full labeled
    illus = [("Frame", "The outer rectangle"), ("Beam", "Horizontal divider bar"),
             ("Rod", "Vertical bars for beads"), ("Upper Bead", "Value = 5"),
             ("Lower Bead", "Value = 1 each")]

    box_w = CW / 3 - 4 * mm
    box_h = (y - 22 * mm) / 2 - 6 * mm

    for i, (name, desc) in enumerate(illus):
        col = i % 3; row = i // 3
        bx = MARGIN + col * (box_w + 4 * mm)
        by = y - (row + 1) * (box_h + 6 * mm) + 6 * mm

        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
        c.roundRect(bx, by, box_w, box_h, 4, stroke=1, fill=1)

        # Title
        c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + 6, by + box_h - 14, name)
        c.setFont("Helvetica", 7.5); c.setFillColor(BROWN)
        c.drawString(bx + 6, by + box_h - 24, desc)

        # Draw a simplified abacus highlighting this part — BIGGER
        ab_w = box_w * 0.7
        ab_h = box_h - 38
        ab_x = bx + (box_w - ab_w) / 2
        ab_y = by + 10

        # Frame (always visible, highlighted when i==0)
        c.setStrokeColor(DARK_BROWN if i == 0 else LIGHT_GOLD)
        c.setLineWidth(3 if i == 0 else 0.5)
        c.setFillColor(white)
        c.roundRect(ab_x, ab_y, ab_w, ab_h, 3, stroke=1, fill=1)

        beam_y2 = ab_y + ab_h * 0.65
        # Beam
        if i >= 1:
            c.setFillColor(BROWN if i == 1 else HexColor("#D4C4A8"))
            c.setStrokeColor(DARK_BROWN if i == 1 else LIGHT_GOLD)
            c.setLineWidth(2.5 if i == 1 else 0.5)
            c.rect(ab_x, beam_y2 - 3, ab_w, 6, stroke=1, fill=1)

        # Rods
        if i >= 2:
            for ri in range(3):
                rx = ab_x + ab_w / 4 * (ri + 1)
                c.setStrokeColor(DARK_BROWN if i == 2 else LIGHT_BROWN)
                c.setLineWidth(2 if i == 2 else 0.8)
                c.line(rx, ab_y + 4, rx, ab_y + ab_h - 4)

        # Upper bead — BIGGER diamonds
        if i >= 3:
            for ri in range(3):
                rx = ab_x + ab_w / 4 * (ri + 1)
                c.setFillColor(GOLD)
                c.setStrokeColor(DARK_BROWN)
                c.setLineWidth(1.2 if i == 3 else 0.6)
                bsz = ab_w * 0.11  # bead size
                uby = beam_y2 + bsz * 2.2
                # Hexagonal bead
                hw = bsz; hh = bsz * 0.8
                p = c.beginPath()
                p.moveTo(rx - hw, uby); p.lineTo(rx - hw * 0.5, uby + hh)
                p.lineTo(rx + hw * 0.5, uby + hh); p.lineTo(rx + hw, uby)
                p.lineTo(rx + hw * 0.5, uby - hh); p.lineTo(rx - hw * 0.5, uby - hh)
                p.close(); c.drawPath(p, stroke=1, fill=1)

        # Lower beads — BIGGER
        if i >= 4:
            for ri in range(3):
                rx = ab_x + ab_w / 4 * (ri + 1)
                for j in range(4):
                    lby = beam_y2 - 8 - j * (ab_h * 0.1 + 1)
                    c.setFillColor(BROWN if j < 2 else LIGHT_GOLD)
                    c.setStrokeColor(DARK_BROWN); c.setLineWidth(1 if i == 4 else 0.6)
                    c.roundRect(rx - ab_w * 0.08, lby - 4, ab_w * 0.16, 8, 2, stroke=1, fill=1)

        # Mascot bird near/on each illustration
        bird_positions = [
            (bx - 5, by + 15, 14, "right", "happy"),
            (bx + box_w - 8, by + box_h - 28, 13, "left", "wink"),
            (bx + box_w + 3, by + 20, 12, "left", "thinking"),
            (bx - 8, by + box_h - 25, 13, "right", "surprised"),
            (bx + box_w - 5, by + 12, 14, "left", "happy"),
        ]
        bpx, bpy, bps, bpf, bpe = bird_positions[i]
        draw_bead_bird(c, bpx, bpy, bps, [GOLD, LIGHT_GOLD, BROWN, GOLD, LIGHT_GOLD][i], bpf, bpe)

    # 6th box: Full labeled abacus
    bx = MARGIN + 2 * (box_w + 4 * mm)
    by = y - 2 * (box_h + 6 * mm) + 6 * mm

    c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.8)
    c.roundRect(bx, by, box_w, box_h, 4, stroke=1, fill=1)
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(bx + 6, by + box_h - 14, "Complete Abacus")
    c.setFont("Helvetica", 7.5); c.setFillColor(BROWN)
    c.drawString(bx + 6, by + box_h - 24, "All parts together — values 0 to 9")

    # Show 5 mini abacuses for 0-4 — sized to fit inside card with padding
    available_h = box_h - 38  # space below title
    mini_h = min(16 * mm, available_h - 14)  # leave room for label
    mini_w = 10 * mm
    # Center abacuses vertically in available space (below title)
    total_strip_w = 5 * (mini_w + 4) - 4
    start_x = bx + (box_w - total_strip_w) / 2
    my = by + (available_h - mini_h) / 2 + 4  # vertically centered
    for num in range(5):
        mx = start_x + num * (mini_w + 4)
        u = 1 if num >= 5 else 0
        lo = num - 5 if num >= 5 else num
        draw_abacus(c, mx, my, mini_w, mini_h, u, lo, label=num)

    # Mascot with graduation cap
    draw_bead_bird(c, bx + box_w - 15, by + box_h - 28, 16, GOLD, "left", "happy", hat="graduation")


def page_02(c):
    """Page 2: Value of Beads."""
    bg(c); y = draw_hdr(c, "Write the Value of Beads", "Set 1 to 9 on the abacus"); draw_footer(c, 2)
    scatter_decorations(c, 2)
    instr(c, MARGIN, y - 5, "Look at each abacus and write the number it shows in the box below.")
    y -= 14
    draw_bead_bird(c, W - MARGIN - 10 * mm, y + 5, 18, GOLD, "left", "thinking")

    # Calculate available space
    footer_y = 16 * mm
    avail = y - footer_y - 10
    # 3 sections: 2 rows of value reading + 1 row of practice
    section_h = avail / 3

    aw = 20 * mm; ah = min(26 * mm, section_h - 18 * mm)
    sp = CW / 5

    # 2 rows: values 0-4 and 5-9
    for ri, vals in enumerate([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]):
        for ci, v in enumerate(vals):
            ax = MARGIN + ci * sp + (sp - aw) / 2
            ay = y - ri * section_h - ah
            draw_abacus(c, ax, ay, aw, ah, 1 if v >= 5 else 0, v - 5 if v >= 5 else v)
            bs = 12 * mm
            c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(white)
            c.rect(ax + (aw - bs) / 2, ay - bs - 2, bs, bs, stroke=1, fill=1)

    # Practice section — 1 row of 5 (fits on page)
    y2 = y - 2 * section_h - 4
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y2, "Now set these numbers on the abacus:")
    y2 -= 22  # extra space so number labels don't overlap with text above
    prac_ah = min(ah, y2 - footer_y - 16)
    for i, n in enumerate([3, 7, 1, 9, 5]):
        ax = MARGIN + i * sp + (sp - aw) / 2
        ay = y2 - prac_ah
        draw_abacus(c, ax, ay, aw, prac_ah, 0, 0)
        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(ax + aw / 2, ay + prac_ah + 3, str(n))


def page_03_04(c, pn):
    """Pages 3-4: Numbers with hands, dots, dotted tracing, crosshair boxes."""
    bg(c)
    nums = range(1, 6) if pn == 3 else range(6, 11)
    y = draw_hdr(c, "Understand Numbers", "Numbers 1 to 5" if pn == 3 else "Numbers 6 to 10")
    draw_footer(c, pn); scatter_decorations(c, pn)

    # Column widths — balanced to prevent overlaps
    # Total CW ~285mm, distribute proportionally
    cws = [30 * mm, 30 * mm, 28 * mm, 28 * mm, 28 * mm, 28 * mm]
    prac_w = CW - sum(cws)
    cws.append(max(prac_w, 50 * mm))
    hdrs = ["Abacus", "Hand", "Dots", "Number", "Trace", "Trace", "Practice"]

    hx = MARGIN
    for h, w in zip(hdrs, cws):
        c.setFillColor(BROWN); c.rect(hx, y - 13, w, 13, stroke=0, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", 7); c.drawCentredString(hx + w / 2, y - 10, h)
        hx += w
    y -= 15
    rh = (y - 22 * mm) / 5  # extra footer clearance so row 5 doesn't clip

    for idx, num in enumerate(nums):
        ry = y - (idx + 1) * rh
        if idx % 2 == 0:
            c.setFillColor(TF); c.rect(MARGIN, ry, CW, rh, stroke=0, fill=1)
        hx = MARGIN
        for w in cws:
            c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.3); c.rect(hx, ry, w, rh, stroke=1, fill=0)
            hx += w

        cx = MARGIN
        # Col 1: Abacus
        u = 1 if num >= 5 else 0; lo = num % 5 if num != 5 and num != 10 else (0 if num == 5 else 4)
        if num == 5: u = 1; lo = 0
        if num == 10: u = 1; lo = 4  # show as 9 since single rod
        aw2 = cws[0] * 0.65; ah2 = rh * 0.78
        draw_abacus(c, cx + (cws[0] - aw2) / 2, ry + (rh - ah2) / 2, aw2, ah2, u, lo)
        cx += cws[0]

        # Col 2: Hand
        draw_hand(c, cx + cws[1] / 2, ry + rh * 0.45, rh * 0.7, min(num, 5))
        if num > 5:
            c.setFont("Helvetica", 6); c.setFillColor(BROWN)
            c.drawCentredString(cx + cws[1] / 2, ry + 3, f"5+{num - 5}" if num < 10 else "5+5")
        cx += cws[1]

        # Col 3: Dots
        for j in range(num):
            dc, dr = j % (3 if num <= 5 else 5), j // (3 if num <= 5 else 5)
            c.setFillColor(BROWN); c.circle(cx + 6 + dc * 7, ry + rh - 10 - dr * 7, 2.8, stroke=0, fill=1)
        cx += cws[2]

        # Col 4: Big number
        c.setFont("Helvetica-Bold", 26); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(cx + cws[3] / 2, ry + rh * 0.3, str(num))
        cx += cws[3]

        # Col 5: Dotted trace
        draw_dotted_number(c, cx + cws[4] / 2, ry + rh * 0.3, num, 26)
        cx += cws[4]

        # Col 6: Dotted trace 2 (lighter)
        draw_dotted_number(c, cx + cws[5] / 2, ry + rh * 0.3, num, 26)
        cx += cws[5]

        # Col 7: Crosshair practice boxes
        bs = min(rh * 0.5, 15 * mm)
        for b in range(min(3, int(cws[6] / (bs + 3)))):
            draw_crosshair_box(c, cx + 3 + b * (bs + 3), ry + (rh - bs) / 2, bs)


def page_05(c):
    """Page 5: Hidden numbers — numbers overlap to form a dense puzzle."""
    bg(c); y = draw_hdr(c, "Write the Numbers You Can Identify"); draw_footer(c, 5)
    scatter_decorations(c, 5)
    instr(c, MARGIN, y - 5, "How many numbers can you find hidden in the picture? Write them in the boxes!")
    y -= 16

    # Large central puzzle area — numbers overlapping densely
    puzzle_x = MARGIN + 30 * mm
    puzzle_y = 40 * mm
    puzzle_w = CW - 60 * mm
    puzzle_h = y - puzzle_y - 10

    # Light background for puzzle area
    c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(1.5)
    c.roundRect(puzzle_x, puzzle_y, puzzle_w, puzzle_h, 8, stroke=1, fill=1)

    # Dense overlapping numbers — each at specific positions forming a visual puzzle
    # Numbers are drawn at varying sizes, rotations, and colors to be "hidden"
    random.seed(77)
    positions = []
    for num in range(10):
        # Each number placed 2-3 times at different sizes/angles
        for rep in range(3):
            nx = puzzle_x + 15 + random.random() * (puzzle_w - 30)
            ny = puzzle_y + 15 + random.random() * (puzzle_h - 30)
            fs = random.randint(22, 55)
            rot = random.randint(-45, 45)
            # Mix of colors: some very similar to background (harder to find)
            colors = [DARKER_BROWN, BROWN, DARK_BROWN, GOLD, LIGHT_BROWN,
                      HexColor("#D4C4A8"), HexColor("#B8A080"), HexColor("#9E8868")]
            col = colors[random.randint(0, len(colors) - 1)]
            positions.append((num, nx, ny, fs, rot, col))

    # Sort by font size (draw big ones first, small on top)
    positions.sort(key=lambda p: -p[3])
    for num, nx, ny, fs, rot, col in positions:
        c.saveState()
        c.translate(nx, ny); c.rotate(rot)
        c.setFont("Helvetica-Bold", fs)
        c.setFillColor(col)
        c.drawCentredString(0, 0, str(num))
        c.restoreState()

    # Birds sitting on top of puzzle
    draw_bird(c, puzzle_x + 20, puzzle_y + puzzle_h + 5, 14, GOLD)
    draw_bird(c, puzzle_x + puzzle_w - 25, puzzle_y + puzzle_h + 5, 12, LIGHT_GOLD, "left")
    draw_bead_bird(c, MARGIN + 8 * mm, puzzle_y + puzzle_h / 2, 18, GOLD, "right", "surprised", action="waving")

    # Answer boxes
    y2 = puzzle_y - 8
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y2, "Write the numbers you found:")
    y2 -= 3
    bsz = 14 * mm; bsp = CW / 10
    for i in range(10):
        bx = MARGIN + i * bsp + (bsp - bsz) / 2
        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(white)
        c.rect(bx, y2 - bsz, bsz, bsz, stroke=1, fill=1)


def page_06_07(c, pn):
    """Pages 6-7: Count objects (BIG) + write + abacus."""
    bg(c); y = draw_hdr(c, "Count and Write"); draw_footer(c, pn)
    scatter_decorations(c, pn)
    instr(c, MARGIN, y - 5, "Count the objects, write the number, then show it on the abacus.")
    y -= 14
    draw_bead_bird(c, W - MARGIN - 10 * mm, y + 6, 16, GOLD, "left", "happy")

    if pn == 6:
        items = [(1, draw_bird), (3, draw_fish), (2, draw_flower),
                 (4, draw_apple), (5, draw_star), (2, draw_butterfly)]
    else:
        items = [(5, draw_strawberry), (3, draw_mango), (6, draw_cherry),
                 (4, draw_pineapple), (7, draw_bone), (3, draw_banana)]

    bw = CW / 3 - 6 * mm; bh = (y - 20 * mm) / 2 - 4 * mm
    obj_size = 28  # BIGGER objects for kids

    for i, (count, fn) in enumerate(items):
        col, row = i % 3, i // 3
        bx = MARGIN + col * (bw + 6 * mm)
        by = y - (row + 1) * (bh + 4 * mm) + 4 * mm
        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(WARM_WHITE)
        c.roundRect(bx, by, bw, bh, 4, stroke=1, fill=1)

        # Draw objects BIG — scale up for fewer objects, centered in left portion
        actual_size = obj_size if count >= 4 else int(obj_size * 1.4)  # bigger when fewer
        sp = actual_size + 8  # more spacing between objects
        max_cols = min(count, 4)
        obj_area_w = bw * 0.55  # left portion of card (right has =, box, abacus)
        total_obj_w = max_cols * sp
        obj_start_x = bx + max(28, (obj_area_w - total_obj_w) / 2 + 10)
        for j in range(count):
            ox = obj_start_x + (j % max_cols) * sp
            oy = by + bh - 25 - (j // max_cols) * sp
            try:
                if fn == draw_star: fn(c, ox, oy, size=actual_size * 0.4, color=GOLD, filled=True)
                elif fn == draw_bone: fn(c, ox, oy, size=actual_size, angle=random.randint(-10, 10))
                elif fn == draw_bird: fn(c, ox, oy, size=actual_size, color=GOLD)
                elif fn == draw_fish: fn(c, ox, oy, size=actual_size, color=GOLD)
                elif fn == draw_butterfly: fn(c, ox, oy, size=actual_size, color=GOLD)
                else: fn(c, ox, oy, size=actual_size)
            except: fn(c, ox, oy)

        # = and answer box
        eqx = bx + bw * 0.6; eqy = by + bh * 0.5
        c.setFont("Helvetica-Bold", 18); c.setFillColor(BROWN); c.drawCentredString(eqx, eqy, "=")
        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(white)
        c.rect(eqx + 12, eqy - 6, 14 * mm, 14 * mm, stroke=1, fill=1)

        # Mini abacus with arrows
        draw_abacus(c, bx + bw - 22 * mm, by + 6, 17 * mm, 24 * mm, 0, 0, show_arrows=True)


def page_08_09(c, pn):
    """Pages 8-9: Match the Following."""
    bg(c); y = draw_hdr(c, "Match the Following"); draw_footer(c, pn)
    scatter_decorations(c, pn)
    nums = list(range(1, 6)) if pn == 8 else [6, 7, 8, 9, 10]
    instr(c, MARGIN, y - 5, "Draw lines to match each number with its dot pattern and abacus.")
    y -= 16

    c1x = MARGIN + 25 * mm; c2x = W / 2 - 10 * mm; c3x = W - MARGIN - 55 * mm
    random.seed(pn + 100)
    do = nums.copy(); ao = nums.copy(); random.shuffle(do); random.shuffle(ao)
    rs = (y - 22 * mm) / 5

    c.setFont("Helvetica-Bold", 10); c.setFillColor(BROWN)
    c.drawCentredString(c1x, y, "Number"); c.drawCentredString(c2x + 10, y, "Dots")
    c.drawCentredString(c3x + 14 * mm, y, "Abacus"); y -= 8

    for i in range(5):
        ry = y - (i + 0.5) * rs
        # Number (tab shape)
        bs = 20 * mm
        c.setStrokeColor(GOLD); c.setLineWidth(1.2); c.setFillColor(WARM_WHITE)
        c.roundRect(c1x - bs / 2, ry - bs / 2, bs, bs, 4, stroke=1, fill=1)
        c.setFont("Helvetica-Bold", 24); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(c1x, ry - 8, str(nums[i]))

        # Dots (scrambled, in cloud-ish bubble)
        dv = do[i]
        bubble_w = 40 * mm; bubble_h = 20 * mm
        c.setFillColor(WARM_WHITE); c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.8)
        c.roundRect(c2x - 5, ry - bubble_h / 2, bubble_w, bubble_h, 8, stroke=1, fill=1)
        dot_sp = 7 if dv <= 5 else 6
        dot_r = 3 if dv <= 5 else 2.5
        for j in range(dv):
            c.setFillColor(DARKER_BROWN)
            c.circle(c2x + 5 + (j % 5) * dot_sp, ry + 4 - (j // 5) * dot_sp, dot_r, stroke=0, fill=1)

        # Abacus (scrambled)
        av = ao[i]; u = 1 if av >= 5 else 0; lo = av - 5 if av >= 5 else av
        if av == 10: u, lo = 1, 4
        draw_abacus(c, c3x, ry - 14 * mm, 24 * mm, 28 * mm, u, lo)

        # Connection dots
        c.setFillColor(BROWN)
        c.circle(c1x + bs / 2 + 3, ry, 2.5, stroke=0, fill=1)
        c.circle(c2x - 8, ry, 2.5, stroke=0, fill=1)
        c.circle(c2x + bubble_w, ry, 2.5, stroke=0, fill=1)
        c.circle(c3x - 3, ry, 2.5, stroke=0, fill=1)

    draw_bead_bird(c, W - MARGIN - 8 * mm, y - rs * 2, 16, GOLD, "left", "wink")


def page_calc(c, pn, title, data):
    """Calculation page: FULL WIDTH tables + bottom illustration strip."""
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)

    # Draw fingering exercise text between header and first table (if present)
    first_fing = data[0][0] if data and data[0][0] else None
    if first_fing:
        c.setFont("Helvetica", 7); c.setFillColor(BROWN)
        c.drawString(MARGIN, y - 2, first_fing)
        y -= 10  # extra space for the fingering line

    # Tables use FULL page width — fingering handled above, not passed to draw_calc_table
    for ti, (fing, probs) in enumerate(data):
        cols = len(probs)
        y = draw_calc_table(c, MARGIN, y, probs, cols, None, table_width=CW)
        y -= 8

    # Bottom illustration strip — horizontal row of picture problems
    # Shows BOTH groups: a objects OP b objects = ___
    strip_y = 18 * mm  # just above footer
    strip_h = y - strip_y - 4
    if strip_h < 25: strip_h = 25  # minimum

    # Unique strip sets per page — no repeats across calc pages
    all_problem_sets = {
        10: [(3, "+", 2, draw_apple),      (5, "-", 3, draw_cherry),     (4, "+", 1, draw_flower),    (5, "-", 4, draw_fish)],
        11: [(2, "+", 4, draw_cherry),     (5, "-", 2, draw_apple),      (3, "+", 2, draw_strawberry),(4, "-", 3, draw_fish)],
        13: [(1, "+", 5, draw_flower),     (4, "-", 2, draw_cherry),     (2, "+", 3, draw_apple),     (5, "-", 1, draw_strawberry)],
        15: [(3, "+", 3, draw_apple),      (5, "-", 4, draw_fish),       (1, "+", 4, draw_cherry),    (4, "-", 2, draw_flower)],
        16: [(4, "+", 2, draw_fish),       (5, "-", 3, draw_apple),      (2, "+", 3, draw_cherry),    (3, "-", 1, draw_strawberry)],
        17: [(3, "+", 1, draw_strawberry), (4, "-", 1, draw_cherry),     (2, "+", 4, draw_apple),     (5, "-", 2, draw_flower)],
        19: [(4, "+", 1, draw_cherry),     (5, "-", 2, draw_strawberry), (1, "+", 3, draw_fish),      (4, "-", 3, draw_apple)],
        20: [(2, "+", 2, draw_apple),      (4, "-", 3, draw_fish),       (3, "+", 3, draw_cherry),    (5, "-", 4, draw_flower)],
        21: [(5, "+", 1, draw_flower),     (3, "-", 2, draw_apple),      (4, "+", 2, draw_cherry),    (5, "-", 3, draw_strawberry)],
        22: [(1, "+", 4, draw_strawberry), (5, "-", 1, draw_cherry),     (3, "+", 2, draw_fish),      (4, "-", 2, draw_apple)],
        25: [(2, "+", 3, draw_fish),       (5, "-", 3, draw_flower),     (4, "+", 1, draw_strawberry),(3, "-", 2, draw_cherry)],
        27: [(4, "+", 2, draw_apple),      (5, "-", 4, draw_strawberry), (2, "+", 4, draw_fish),      (4, "-", 1, draw_cherry)],
        28: [(3, "+", 3, draw_cherry),     (5, "-", 2, draw_fish),       (1, "+", 5, draw_apple),     (4, "-", 3, draw_flower)],
        30: [(2, "+", 2, draw_flower),     (4, "-", 2, draw_strawberry), (3, "+", 1, draw_cherry),    (5, "-", 3, draw_apple)],
        31: [(5, "+", 1, draw_strawberry), (3, "-", 1, draw_apple),      (2, "+", 3, draw_flower),    (4, "-", 2, draw_cherry)],
        32: [(1, "+", 3, draw_cherry),     (4, "-", 1, draw_flower),     (3, "+", 2, draw_apple),     (5, "-", 2, draw_strawberry)],
        33: [(4, "+", 2, draw_strawberry), (5, "-", 3, draw_cherry),     (2, "+", 2, draw_fish),      (3, "-", 1, draw_flower)],
    }
    # Fallback to a default set if page not found
    mini_set = all_problem_sets.get(pn, [(3, "+", 2, draw_apple), (4, "-", 1, draw_cherry), (2, "+", 3, draw_fish), (5, "-", 2, draw_flower)])
    num_probs = len(mini_set)
    prob_w = CW / num_probs

    for i, (a, op, b, fn) in enumerate(mini_set):
        px = MARGIN + i * prob_w
        pw = prob_w - 4

        # Card background
        c.setFillColor(WARM_WHITE); c.setStrokeColor(GOLD); c.setLineWidth(0.5)
        c.roundRect(px, strip_y, pw, strip_h, 3, stroke=1, fill=1)

        obj_s = min(13, strip_h * 0.28)
        obj_y = strip_y + strip_h * 0.58  # centered vertically with padding

        # Center objects + operator horizontally with clear padding around operator
        obj_sp = obj_s + 3
        op_pad = 14  # padding on EACH side of the operator
        op_w = 8     # approximate operator glyph width
        total_w = a * obj_sp + op_pad + op_w + op_pad + b * obj_sp
        start_x = px + max(8, (pw - total_w) / 2)

        # Draw FIRST group (a objects)
        for j in range(a):
            ox = start_x + j * obj_sp
            try: fn(c, ox, obj_y, size=obj_s)
            except: fn(c, ox, obj_y)

        # Operator — centered between the two groups with equal padding
        op_cx = start_x + a * obj_sp + op_pad + op_w / 2
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(op_cx, obj_y - 4, op)

        # Draw SECOND group (b objects)
        b_start = op_cx + op_w / 2 + op_pad
        for j in range(b):
            ox = b_start + j * obj_sp
            try: fn(c, ox, obj_y, size=obj_s)
            except: fn(c, ox, obj_y)

        # Expression + answer box at bottom of card
        c.setFont("Helvetica-Bold", 9); c.setFillColor(DARKER_BROWN)
        c.drawString(px + 10, strip_y + 5, f"{a} {op} {b} =")

        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(px + pw - 14 * mm, strip_y + 2, 12 * mm, 12, stroke=1, fill=1)

    # (mascot added automatically by draw_footer via page_mascot)


def page_visual(c, pn, title, problems):
    """Visual add/sub with BIG objects."""
    bg(c); y = draw_hdr(c, title); draw_footer(c, pn)
    scatter_decorations(c, pn)
    instr(c, MARGIN, y - 5, "Count the objects and write the answer.")
    y -= 14

    fns = [draw_bone, draw_fish, draw_apple, draw_flower, draw_strawberry, draw_cherry]
    bw = CW / 3 - 5 * mm; bh = (y - 20 * mm) / 2 - 5 * mm
    obj_s = 24  # BIGGER objects

    for i, (a, op, b) in enumerate(problems[:6]):
        col, row = i % 3, i // 3
        bx = MARGIN + col * (bw + 5 * mm)
        by = y - (row + 1) * (bh + 5 * mm) + 5 * mm
        fn = fns[i % len(fns)]

        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(WARM_WHITE)
        c.roundRect(bx, by, bw, bh, 4, stroke=1, fill=1)

        # Background band for objects (upper portion)
        c.setFillColor(HexColor("#F0E8DA"))
        c.roundRect(bx + 2, by + bh * 0.3, bw - 4, bh * 0.65, 3, stroke=0, fill=1)

        def _draw_obj(fn, ox, oy, s, col=None):
            try:
                if fn == draw_bone: fn(c, ox, oy, size=s, angle=0)
                elif fn == draw_fish: fn(c, ox, oy, size=s, color=col or GOLD)
                elif fn == draw_cherry: fn(c, ox, oy, size=s)
                else: fn(c, ox, oy, size=s)
            except: fn(c, ox, oy)

        # Horizontal split layout: [Group A] [operator] [Group B]
        # Each side gets ~42% of card width, operator sits centered between
        max_count = max(a, b)
        # Pick object size based on the busiest side; sp = obj + breathing room
        if max_count <= 4:
            obj_size = 22
        elif max_count <= 6:
            obj_size = 18
        else:
            obj_size = 15
        sp = obj_size + 6
        cols = 3 if max_count <= 6 else 4  # columns per side before wrapping

        # Vertical center of object zone (upper 65% of card)
        zone_y_top = by + bh * 0.92
        zone_y_bot = by + bh * 0.32
        zone_cy = (zone_y_top + zone_y_bot) / 2

        def _layout_group(side_x_center, count):
            """Return list of (x, y) positions for `count` objects centered around side_x_center."""
            positions = []
            rows = (count + cols - 1) // cols if count > 0 else 0
            for j in range(count):
                row_i = j // cols
                col_i = j % cols
                # Items in this specific row (last row may have fewer)
                items_in_row = min(cols, count - row_i * cols)
                row_w = (items_in_row - 1) * sp
                row_start_x = side_x_center - row_w / 2
                ox = row_start_x + col_i * sp
                # Stack rows from top down, centered vertically around zone_cy
                total_h = (rows - 1) * sp if rows > 0 else 0
                row_top_y = zone_cy + total_h / 2
                oy = row_top_y - row_i * sp
                positions.append((ox, oy))
            return positions

        left_cx = bx + bw * 0.25
        right_cx = bx + bw * 0.75
        op_x = bx + bw * 0.5

        # Group A — left side
        for ox, oy in _layout_group(left_cx, a):
            _draw_obj(fn, ox, oy, obj_size)

        # Operator — centered between groups, vertically aligned with object zone
        c.setFont("Helvetica-Bold", 28); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(op_x, zone_cy - 8, op)

        # Group B — right side
        b_positions = _layout_group(right_cx, b)
        for ox, oy in b_positions:
            color = HexColor("#CC8866") if op == "-" else LIGHT_GOLD
            _draw_obj(fn, ox, oy, obj_size, color)

        # For subtraction: overlay X on group B (these are being taken away)
        if op == "-":
            c.setStrokeColor(HexColor("#CC3333")); c.setLineWidth(2)
            sz = obj_size * 0.5
            for ox, oy in b_positions:
                c.line(ox - sz, oy - sz, ox + sz, oy + sz)
                c.line(ox - sz, oy + sz, ox + sz, oy - sz)

        # Expression
        c.setFont("Helvetica-Bold", 15); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + 6, by + 8, f"{a}  {op}  {b}  =")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(bx + bw - 22 * mm, by + 4, 16 * mm, 16, stroke=1, fill=1)


def page_23(c):
    """Page 23: Composition of 5 with TREE and mascot."""
    bg(c); y = draw_hdr(c, "Composition of 5", "Understanding how numbers make 5"); draw_footer(c, 23)
    scatter_decorations(c, 23)
    instr(c, MARGIN, y - 5, "5 can be split into two parts in different ways!")
    y -= 18

    # Left side: Apple groups showing splits
    splits_x = MARGIN
    splits_w = W * 0.35

    # Big "5" at top
    c.setFont("Helvetica-Bold", 60); c.setFillColor(GOLD)
    c.drawCentredString(splits_x + splits_w / 2, y - 30, "5")

    # Apple group splits
    pairs = [(4, 1), (2, 3), (1, 4), (3, 2)]
    sy = y - 60
    for i, (a, b) in enumerate(pairs):
        gy = sy - i * 28

        # Tree branch notation: 5 → a & b
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(splits_x, gy, f"{a} & {b}")

        # Draw apple groups
        for j in range(a):
            draw_apple(c, splits_x + 45 + j * 16, gy + 3, size=12)
        for j in range(b):
            draw_apple(c, splits_x + 45 + a * 16 + 10 + j * 16, gy + 3, size=12)

        c.setFont("Helvetica-Bold", 12); c.setFillColor(GOLD)
        c.drawString(splits_x + 45 + (a + b) * 16 + 14, gy, "= 5")

    # Summary
    sy2 = sy - len(pairs) * 28 - 15
    for i, (a, b) in enumerate(pairs):
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        c.drawString(splits_x, sy2 - i * 16, f"{a} & {b}  ——  5")

    # Center: Mascot pointing — BIG
    draw_bead_bird(c, W * 0.4, y - 80, 38, GOLD, "right", "happy", hat="graduation", action="waving")

    # Right side: Apple Tree!
    tree_x = W * 0.52; tree_w = W * 0.42; tree_h = y - 25 * mm
    draw_apple_tree(c, tree_x, 22 * mm, tree_w, tree_h, [1, 2, 3, 4, 5])

    # Practice at bottom
    py = 30 * mm
    c.setFont("Helvetica-Bold", 10); c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, py, "Fill in the missing number:")
    py -= 16
    for i, ex in enumerate(["4 + ___ = 5", "___ + 3 = 5", "1 + ___ = 5", "___ + 2 = 5", "3 + ___ = 5", "___ + 4 = 5"]):
        c.setFont("Helvetica-Bold", 12); c.setFillColor(DARKER_BROWN)
        c.drawString(MARGIN + (i % 3) * (CW / 3), py - (i // 3) * 18, ex)


def page_24(c):
    """Page 24: Composition on abacus with mascot characters."""
    bg(c); y = draw_hdr(c, "Composition of 5", "Showing combinations on the abacus"); draw_footer(c, 24)
    scatter_decorations(c, 24)
    instr(c, MARGIN, y - 5, "See how we make 5 on the abacus!")
    y -= 16

    combos = [(2, 3, "2 + 3 = 5"), (4, 1, "4 + 1 = 5"), (1, 4, "1 + 4 = 5"), (3, 2, "3 + 2 = 5")]
    bw = CW / 2 - 5 * mm; bh = (y - 22 * mm) / 2 - 5 * mm

    for i, (a, b, expr) in enumerate(combos):
        col, row = i % 2, i // 2
        bx = MARGIN + col * (bw + 10 * mm)
        by = y - (row + 1) * (bh + 5 * mm) + 5 * mm

        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(WARM_WHITE)
        c.roundRect(bx, by, bw, bh, 4, stroke=1, fill=1)

        c.setFont("Helvetica-Bold", 14); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(bx + bw / 2, by + bh - 16, expr)

        # Mascot character acting it out
        draw_bead_bird(c, bx + 18, by + bh * 0.45, 18, GOLD, "right", ["happy", "wink", "surprised", "happy"][i])

        # Two abacuses
        aw, ah = 22 * mm, bh - 38
        aby = by + 10
        ax1 = bx + bw * 0.35
        ua = 1 if a >= 5 else 0; la = a - 5 if a >= 5 else a
        draw_abacus(c, ax1, aby, aw, ah, ua, la, label=a, show_arrows=True)

        # Arrow
        arx = ax1 + aw + 4 * mm; ary = aby + ah / 2
        c.setStrokeColor(GOLD); c.setLineWidth(1.5)
        c.line(arx, ary, arx + 14 * mm, ary)
        c.line(arx + 12 * mm, ary + 3, arx + 14 * mm, ary)
        c.line(arx + 12 * mm, ary - 3, arx + 14 * mm, ary)
        c.setFont("Helvetica-Bold", 9); c.setFillColor(BROWN)
        c.drawCentredString(arx + 7 * mm, ary + 8, f"+{b}")

        # Result
        draw_abacus(c, ax1 + aw + 20 * mm, aby, aw, ah, 1, 0, label=5)


def page_29(c):
    """Page 29: Count & Write with BIG fruit illustrations."""
    bg(c); y = draw_hdr(c, "Count and Write"); draw_footer(c, 29)
    scatter_decorations(c, 29)
    instr(c, MARGIN, y - 5, "Count the objects on each side, then write the addition and answer.")
    y -= 14

    problems = [(4, 2), (3, 2), (2, 3), (4, 1), (2, 4), (3, 4)]
    fns = [draw_strawberry, draw_apple, draw_mango, draw_cherry, draw_flower, draw_fish]
    bw = CW / 3 - 5 * mm; bh = (y - 20 * mm) / 2 - 5 * mm; os2 = 22  # bigger

    for i, (a, b) in enumerate(problems):
        col, row = i % 3, i // 3
        bx = MARGIN + col * (bw + 5 * mm)
        by = y - (row + 1) * (bh + 5 * mm) + 5 * mm
        fn = fns[i]

        c.setStrokeColor(GOLD); c.setLineWidth(0.8); c.setFillColor(WARM_WHITE)
        c.roundRect(bx, by, bw, bh, 4, stroke=1, fill=1)
        # Background band
        c.setFillColor(HexColor("#F0E8DA"))
        c.roundRect(bx + 2, by + bh * 0.3, bw - 4, bh * 0.65, 3, stroke=0, fill=1)

        # Horizontal split: [Group A] [+] [Group B], vertically centered in object zone
        sp = os2 + 6
        cols = 3
        zone_cy = by + bh * 0.62
        left_cx = bx + bw * 0.25
        right_cx = bx + bw * 0.75

        def _layout(cx, count):
            positions = []
            rows = (count + cols - 1) // cols if count > 0 else 0
            total_h = (rows - 1) * sp if rows > 0 else 0
            for j in range(count):
                row_i = j // cols
                col_i = j % cols
                items_in_row = min(cols, count - row_i * cols)
                row_w = (items_in_row - 1) * sp
                ox = cx - row_w / 2 + col_i * sp
                oy = zone_cy + total_h / 2 - row_i * sp
                positions.append((ox, oy))
            return positions

        for ox, oy in _layout(left_cx, a):
            try: fn(c, ox, oy, size=os2)
            except: fn(c, ox, oy)

        c.setFont("Helvetica-Bold", 28); c.setFillColor(DARKER_BROWN)
        c.drawCentredString(bx + bw * 0.5, zone_cy - 8, "+")

        for ox, oy in _layout(right_cx, b):
            try: fn(c, ox, oy, size=os2)
            except: fn(c, ox, oy)

        c.setFont("Helvetica-Bold", 13); c.setFillColor(DARKER_BROWN)
        c.drawString(bx + 6, by + 7, f"{a}  +  {b}  =")
        c.setStrokeColor(GOLD); c.setFillColor(white)
        c.rect(bx + bw - 20 * mm, by + 4, 14 * mm, 14, stroke=1, fill=1)


def page_34(c):
    """Page 34: BIG train filling the page."""
    bg(c); y = draw_hdr(c, "Abacus Calculation: Revision", "All Aboard the Speedy Scholars Express!")
    draw_footer(c, 34)
    instr(c, MARGIN, y - 5, "Solve each problem — write answers in the wheel circles!")
    y -= 12

    # Train fills most of the page — lower track to avoid title overlap
    track_y = 45 * mm
    c.setStrokeColor(BROWN); c.setLineWidth(2.5)
    c.line(MARGIN - 5 * mm, track_y, W - MARGIN + 5 * mm, track_y)
    c.setLineWidth(1)
    for tx in range(int(MARGIN - 5 * mm), int(W - MARGIN + 5 * mm), 10):
        c.line(tx, track_y - 4, tx, track_y + 4)

    # Engine — sized to fit below header
    ew = 50 * mm
    max_engine_top = y - 8  # leave gap below gold line
    eh = max_engine_top - track_y - 8 - 25 * mm  # leave room for chimney+smoke
    ex = MARGIN
    c.setFillColor(DARKER_BROWN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(2)
    c.roundRect(ex, track_y + 8, ew, eh, 5, stroke=1, fill=1)
    # Chimney — shorter
    chimney_h = 15 * mm
    c.setFillColor(BROWN); c.rect(ex + 8, track_y + 8 + eh, 12 * mm, chimney_h, stroke=1, fill=1)
    # Smoke — positioned above chimney
    smoke_base = track_y + 8 + eh + chimney_h
    draw_cloud(c, ex + 10, smoke_base + 4, 22, 10)
    draw_cloud(c, ex + 3, smoke_base + 12, 15, 8)
    # Wheels
    wr = 10
    c.setFillColor(GOLD); c.setStrokeColor(DARK_BROWN); c.setLineWidth(1.5)
    c.circle(ex + 16, track_y, wr, stroke=1, fill=1)
    c.circle(ex + ew - 16, track_y, wr, stroke=1, fill=1)
    # Label
    c.setFillColor(white); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(ex + ew / 2, track_y + eh / 2 + 12, "SPEEDY")
    c.drawCentredString(ex + ew / 2, track_y + eh / 2, "SCHOLARS")
    # Driver mascot
    draw_bead_bird(c, ex + ew / 2, track_y + eh - 10, 18, GOLD, "right", "happy", hat="graduation")

    # Carriages — BIG
    probs = [[3, 4, 2], [1, 3, 4], [2, 2, 1], [4, 1, 4], [2, 3, 2], [1, 2, 3]]
    cw2 = 35 * mm; ch2 = eh - 8; car_x = ex + ew + 10 * mm

    for i, prob in enumerate(probs):
        cx = car_x + i * (cw2 + 8 * mm)
        if cx + cw2 > W - MARGIN: break
        cy = track_y + 8

        c.setFillColor(WARM_WHITE); c.setStrokeColor(BROWN); c.setLineWidth(1.2)
        c.roundRect(cx, cy, cw2, ch2, 4, stroke=1, fill=1)

        # Bead bird mascots riding on top
        if i % 2 == 0:
            draw_bead_bird(c, cx + cw2 / 2, cy + ch2 + 10, 13,
                            [GOLD, BROWN, LIGHT_GOLD][i % 3], "right",
                            ["happy", "wink", "surprised"][i % 3])

        # Problem text
        c.setFont("Helvetica-Bold", 11); c.setFillColor(DARKER_BROWN)
        for j, v in enumerate(prob):
            t = str(v) if j == 0 else (f"+{v}" if v > 0 else str(v))
            c.drawCentredString(cx + cw2 / 2, cy + ch2 - 14 - j * 14, t)

        # Wheel with answer circle
        c.setFillColor(LIGHT_GOLD); c.setStrokeColor(BROWN); c.setLineWidth(1.5)
        c.circle(cx + cw2 / 2, track_y, 10, stroke=1, fill=1)
        # Ans label
        c.setFont("Helvetica", 6); c.setFillColor(BROWN)
        c.drawCentredString(cx + cw2 / 2, track_y - 3, "Ans")


# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=landscape(A4))
    c.setTitle("Speedy Scholars - KG-1 Book A")
    c.setAuthor("Speedy Scholars")

    page_cover(c); c.showPage()
    page_01(c); c.showPage()
    page_02(c); c.showPage()
    page_03_04(c, 3); c.showPage()
    page_03_04(c, 4); c.showPage()
    page_05(c); c.showPage()
    page_06_07(c, 6); c.showPage()
    page_06_07(c, 7); c.showPage()
    page_08_09(c, 8); c.showPage()
    page_08_09(c, 9); c.showPage()

    # Pages 10-11: Calculation with picture problems on side
    for pn, title, data in [
        (10, "Abacus Calculation: 1 Digit 3 Rows", [
            ("Fingering Ex: 1-1, 2-1, 3-1, 4-1, 2-2, 3-2", [[1,1,-1],[2,-1,1],[3,-1,-1],[4,-2,1],[1,2,-1],[3,-2,2],[4,-1,-2],[2,1,-2]]),
            (None, [[1,3,-2],[2,-1,3],[4,-3,1],[3,-1,2],[2,2,-3],[4,-2,-1],[1,4,-3],[3,1,-3]]),
            (None, [[4,-1,-2],[2,1,-3],[3,-2,1],[1,2,-3]]),
        ]),
        (11, "Direct Addition & Subtraction", [
            ("Fingering Ex: 1+2, 2+1, 3+1, 5+1, 2+2, 5+2", [[1,2,-1],[2,1,-2],[3,1,-3],[4,-2,1],[1,4,-2],[2,3,-4],[3,2,-1],[4,-3,2]]),
            (None, [[2,-1,3],[4,-1,-2],[3,1,-2],[2,2,-3],[4,-2,1],[1,3,-1],[3,-1,2],[4,-3,1]]),
            (None, [[1,2,1],[3,-2,2],[2,1,-3],[4,-1,1]]),
        ]),
    ]:
        page_calc(c, pn, title, data); c.showPage()

    # Page 12: Visual
    page_visual(c, 12, "Direct Addition & Subtraction", [(5,"+",3),(8,"-",3),(7,"-",5),(4,"+",5),(5,"+",4),(9,"-",6)])
    c.showPage()

    # Page 13: +5 combinations
    page_calc(c, 13, "Abacus Calculation: 1 Digit 3 Rows", [
        ("Fingering Ex: 1+5, 2+5, 3+5, 4+5, 5-5, 6-5", [[1,6,-2],[2,5,-3],[3,5,-4],[4,5,-6],[1,7,-5],[2,6,-1],[3,5,-1],[4,5,-2]]),
        (None, [[7,-5,3],[4,-3,6],[5,-2,4],[6,-1,-3],[8,-5,1],[7,-3,-2],[5,3,-6],[9,-5,-1]]),
        (None, [[1,5,-3],[7,-2,1],[3,5,-6],[8,-5,2]]),
    ]); c.showPage()

    # Page 14: Visual addition
    page_visual(c, 14, "Direct Addition", [(2,"+",6),(1,"+",8),(2,"+",7),(7,"+",1),(3,"+",5),(4,"+",4)])
    c.showPage()

    # Page 15: +6, +7, +8
    page_calc(c, 15, "Abacus Calculation: 1 Digit 3 Rows", [
        ("Fingering Ex: 1+6, 2+6, 3+6, 1+7, 2+7, 1+8", [[1,6,-5],[2,7,-2],[3,-5,7],[4,-2,5],[1,7,-2],[5,-3,1],[6,-2,-3],[7,-5,1]]),
        (None, [[1,5,3],[2,8,-6],[3,-5,6],[4,-3,5],[8,-6,3],[7,-5,4],[6,-3,1],[9,-1,-8]]),
        (None, [[1,7,-5],[2,8,-3],[7,-5,1],[6,-5,1]]),
    ]); c.showPage()

    # Page 16: Mixed practice
    page_calc(c, 16, "Abacus Calculation: 1 Digit 3 Rows", [
        (None, [[3,4,-5],[7,-2,4],[5,-3,6],[2,7,-5],[1,9,-7],[4,-2,5],[6,-3,-2],[8,-5,3]]),
        (None, [[4,6,-7],[9,-4,1],[2,-1,8],[5,3,-6],[7,-3,5],[8,-6,4],[3,6,-5],[1,8,-7]]),
        (None, [[6,-2,1],[9,-7,2],[4,5,-3],[7,-1,-5]]),
    ]); c.showPage()

    # Page 17: More mixed
    page_calc(c, 17, "Abacus Calculation: 1 Digit 3 Rows", [
        (None, [[4,-1,-2],[8,1,-7],[6,-2,5],[3,-3,9],[7,-5,2],[1,8,-6],[5,4,-7],[2,-1,6]]),
        (None, [[8,-6,7],[6,-1,-3],[3,7,-4],[9,-2,-5],[4,5,-8],[7,-3,1],[2,6,-5],[5,-4,3]]),
        (None, [[9,-2,1],[7,-1,-5],[4,-3,5],[8,-5,-2]]),
    ]); c.showPage()

    # Page 18: Visual subtraction
    page_visual(c, 18, "Direct Subtraction", [(8,"-",6),(8,"-",7),(9,"-",6),(9,"-",7),(7,"-",6),(9,"-",8)])
    c.showPage()

    # Page 19: 6-6, 7-6, 8-6, 9-6
    page_calc(c, 19, "Abacus Calculation: 1 Digit 3 Rows", [
        ("Fingering Ex: 6-6, 7-6, 8-6, 9-6", [[7,-6,1],[8,-6,3],[9,-6,-2],[6,-6,7],[5,3,-6],[4,6,-8],[3,-2,8],[2,7,-6]]),
        (None, [[6,1,-6],[7,-3,5],[8,-6,4],[9,-6,-1],[6,3,-7],[5,-4,8],[4,6,-9],[3,7,-6]]),
        (None, [[7,-6,6],[9,-6,3],[8,-6,-1],[6,-6,4]]),
    ]); c.showPage()

    # Page 20: 7-7, 8-7, 9-7, 8-8, 9-8, 9-9
    page_calc(c, 20, "Abacus Calculation: 1 Digit 3 Rows", [
        ("Fingering Ex: 7-7, 8-7, 9-7, 8-8, 9-8, 9-9", [[7,-7,9],[8,-7,4],[9,-7,-1],[8,-8,5],[9,-8,3],[9,-9,8],[7,-7,6],[8,-8,9]]),
        (None, [[9,-9,7],[7,-7,8],[8,-8,6],[9,-7,4],[8,-7,6],[9,-9,5],[7,-6,8],[8,-7,-1]]),
        (None, [[9,-8,7],[7,-7,9],[8,-8,5],[9,-9,8]]),
    ]); c.showPage()

    # Page 21: 8-8, 9-8
    page_calc(c, 21, "Abacus Calculation: 1 Digit 3 Rows", [
        ("Fingering Ex: 8-8, 9-8", [[1,9,-8],[7,-8,9],[8,-8,5],[4,-8,9],[9,-8,3],[2,8,-9],[6,-8,7],[3,-8,8]]),
        (None, [[9,-8,4],[7,2,-8],[8,-7,4],[5,-8,9],[3,6,-8],[1,8,-7],[4,-3,8],[9,-8,6]]),
        (None, [[8,-8,7],[9,-8,4],[7,-8,9],[8,-8,1]]),
    ]); c.showPage()

    # Page 22: 9-9, 8-8, mixed
    page_calc(c, 22, "Abacus Calculation: 1 Digit 3 Rows", [
        ("Fingering Ex: 8-8, 9-8, 9-9", [[9,-9,7],[8,-8,9],[7,-7,6],[9,-8,4],[8,-7,3],[7,-6,5],[9,-9,1],[8,-8,2]]),
        (None, [[9,-7,4],[8,-8,9],[7,-6,8],[9,-9,7],[8,-7,6],[9,-8,3],[7,-6,5],[8,-6,-1]]),
        (None, [[9,-7,4],[8,-8,9],[7,-6,8],[9,-9,7]]),
    ]); c.showPage()

    # Pages 23-24
    page_23(c); c.showPage()
    page_24(c); c.showPage()

    # Page 25: Composition +4
    page_calc(c, 25, "Abacus Calculation: Composition of 5 (+4)", [
        ("+4=+5-1 | Fingering: 1+4, 2+4, 3+4, 4+4", [[1,4,-3],[2,4,-5],[3,4,-6],[4,4,-7],[1,4,2],[2,4,-1],[3,4,-5],[4,4,-3]]),
        (None, [[2,4,-3],[1,4,-5],[3,4,1],[4,4,-6],[1,4,-4],[2,4,-5],[3,4,-2],[4,4,-1]]),
        (None, [[1,4,-3],[4,4,-5],[2,4,-6],[3,4,1]]),
    ]); c.showPage()

    # Page 26: Revision
    page_calc(c, 26, "Abacus Calculation: Revision", [
        (None, [[1,3,-2],[2,6,-5],[3,-1,4],[7,-5,2],[4,2,-3],[5,-2,4],[8,-6,3],[1,-5,9]]),
        (None, [[2,4,-3],[7,-5,6],[1,3,5],[4,-2,6],[8,-3,1],[5,4,-7],[9,-6,2],[7,2,-8]]),
        (None, [[3,4,-5],[2,-1,7],[6,3,-8],[5,2,-4]]),
    ]); c.showPage()

    # Page 27: Composition +3
    page_calc(c, 27, "Abacus Calculation: Composition of 5 (+3)", [
        ("+3=+5-2 | Fingering: 2+3, 3+3, 4+3", [[2,3,-4],[3,3,-5],[4,3,-6],[2,3,1],[3,3,-1],[4,3,-5],[2,3,-3],[3,3,-4]]),
        (None, [[4,3,-2],[2,3,-5],[3,3,1],[4,3,-7],[2,3,-4],[3,3,-6],[4,3,-3],[2,3,-1]]),
        (None, [[3,3,-5],[4,3,-4],[2,3,-3],[3,3,2]]),
    ]); c.showPage()

    # Page 28: Revision
    page_calc(c, 28, "Abacus Calculation: Revision", [
        (None, [[3,4,-5],[2,6,-3],[4,-2,5],[7,-3,1],[5,3,-6],[8,-5,2],[1,4,-3],[6,-4,3]]),
        (None, [[2,3,-4],[4,-3,6],[5,-5,3],[7,-2,-4],[1,6,-5],[8,-3,-4],[3,5,-7],[9,-7,2]]),
        (None, [[4,3,-5],[6,-2,3],[5,-3,2],[7,-5,4]]),
    ]); c.showPage()

    # Page 29: Count & Write
    page_29(c); c.showPage()

    # Page 30: Composition +2
    page_calc(c, 30, "Abacus Calculation: Composition of 5 (+2)", [
        ("+2=+5-3 | Fingering: 3+2, 4+2", [[3,2,-4],[4,2,-5],[3,2,-3],[4,2,-6],[3,2,1],[4,2,-4],[3,2,-2],[4,2,-1]]),
        (None, [[3,2,-5],[4,2,-3],[3,2,2],[4,2,-6],[3,2,-4],[4,2,-1],[3,-2,4],[4,2,-7]]),
        (None, [[3,2,-4],[4,2,-6],[3,2,-5],[4,2,1]]),
    ]); c.showPage()

    # Page 31: Revision
    page_calc(c, 31, "Abacus Calculation: Revision", [
        (None, [[2,8,-3],[4,3,-5],[5,2,-6],[7,-3,1],[3,4,-2],[6,-5,4],[1,7,-3],[8,-4,-2]]),
        (None, [[4,2,-3],[3,5,-7],[6,-4,2],[9,-5,-3],[2,7,-1],[5,-3,4],[8,-2,-5],[1,4,3]]),
        (None, [[4,3,-2],[7,-5,3],[5,2,-4],[3,4,-6]]),
    ]); c.showPage()

    # Page 32: Composition +1
    page_calc(c, 32, "Abacus Calculation: Composition of 5 (+1)", [
        ("+1=+5-4 | Fingering: 4+1", [[4,1,-3],[4,1,-5],[4,1,2],[4,1,-4],[4,1,-2],[4,1,-6],[4,1,3],[4,1,-1]]),
        (None, [[4,1,-5],[4,1,6],[4,1,-3],[4,1,-5],[4,1,-2],[4,1,-4],[4,1,2],[4,1,-5]]),
        (None, [[4,1,-3],[4,1,-5],[4,1,-4],[4,1,2]]),
    ]); c.showPage()

    # Page 33: Big Revision (wider tables)
    page_calc(c, 33, "Abacus Calculation: Revision", [
        (None, [[3,-4,6],[7,-2,3],[5,-5,4],[8,-6,3],[2,4,-5],[6,-3,1],[9,-7,3],[4,5,-8],[1,7,-3],[3,6,-5]]),
        (None, [[5,4,-7],[8,-3,2],[6,-5,4],[3,7,-9],[4,-2,5],[7,-6,8],[2,5,-3],[9,-4,-3],[1,8,-6],[5,-2,4]]),
        (None, [[4,6,-8],[7,-5,3],[2,4,-3],[8,-3,1],[5,-4,6],[3,7,-8],[6,-2,4],[9,-5,-2],[1,3,-4],[4,5,-7]]),
    ]); c.showPage()

    # Page 34: Train
    page_34(c); c.showPage()

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"Total pages: 35 (cover + 34)")

if __name__ == "__main__":
    main()
