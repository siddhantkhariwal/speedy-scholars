"""
Speedy Scholars — Shared Book Chrome
====================================
Brand page furniture used by every book: palette geometry, page background,
header, footer, mascot placement, and the calculation table component.

DO NOT add book-specific logic here. If only one book needs it, put it in
that book's generate.py. If multiple books need it, put it here.

Book scripts use this module via:

    from chrome import *
    set_book("KG-1 Book A")

The set_book() call configures the footer text. Everything else is constant.
"""

import os, sys, random
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white

# Make sibling illustrations.py importable regardless of caller's sys.path
_SHARED_DIR = os.path.dirname(os.path.abspath(__file__))
if _SHARED_DIR not in sys.path:
    sys.path.insert(0, _SHARED_DIR)

from illustrations import (
    BROWN, DARK_BROWN, DARKER_BROWN, GOLD, LIGHT_GOLD, CREAM, WARM_WHITE,
    draw_bead_bird,
)

# ─── Paths ────────────────────────────────────────────────────────────────
# chrome.py lives at: <repo>/scripts/books/_shared/chrome.py
# Repo root is three levels up.
PROJECT_DIR = os.path.abspath(os.path.join(_SHARED_DIR, "..", "..", ".."))
LOGO_PATH = os.path.join(PROJECT_DIR, "public", "images", "logo3_transparent.png")
PUBLIC_DIR = os.path.join(PROJECT_DIR, "public")

# ─── Page geometry (landscape A4) ─────────────────────────────────────────
W, H = landscape(A4)
MARGIN = 18 * mm
CW = W - 2 * MARGIN
CH = H - 2 * MARGIN

# ─── Table fill colors (used by draw_calc_table) ──────────────────────────
TF = HexColor("#FAF5EE")
TH = HexColor("#E8DDD0")

# ─── Per-book footer text ─────────────────────────────────────────────────
_BOOK_NAME = "Speedy Scholars"

def set_book(name):
    """Set the book name shown in the footer. Call once at start of generate.py."""
    global _BOOK_NAME
    _BOOK_NAME = name


# ─── Page background ──────────────────────────────────────────────────────
def bg(c):
    c.setFillColor(CREAM)
    c.rect(0, 0, W, H, stroke=0, fill=1)


# ─── Italic instruction text under a header ───────────────────────────────
def instr(c, x, y, t):
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(BROWN)
    c.drawString(x, y, t)


# ─── Header: title + optional subtitle + gold separator + logo top-right ──
def draw_hdr(c, title, sub=None):
    y = H - 16 * mm
    try:
        c.drawImage(LOGO_PATH, W - MARGIN - 30 * mm, y - 6 * mm, width=28 * mm,
                    height=14 * mm, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setFont("Helvetica-Bold", 15)
    c.setFillColor(DARKER_BROWN)
    c.drawString(MARGIN, y, title)
    if sub:
        c.setFont("Helvetica", 9)
        c.setFillColor(BROWN)
        c.drawString(MARGIN, y - 13, sub)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.2)
    ly = y - (18 if sub else 6)
    c.line(MARGIN, ly, W - MARGIN - 35 * mm, ly)
    return ly - 6


# ─── Mascot: graduation-hat bead-bird, bottom-right, varies by page ───────
def page_mascot(c, pn):
    random.seed(pn + 500)
    mx = W - MARGIN - random.uniform(8, 15) * mm
    my = 18 * mm + random.uniform(5, 15)
    expr = ["happy", "wink", "thinking", "surprised"][pn % 4]
    draw_bead_bird(c, mx, my, 16, GOLD, "left", expr, hat="graduation")


# ─── Footer: gold line + book name (left) + page number (right) + mascot ──
def draw_footer(c, pn):
    c.saveState()
    c.setStrokeColor(LIGHT_GOLD)
    c.setLineWidth(0.5)
    c.line(MARGIN, 13 * mm, W - MARGIN, 13 * mm)
    c.setFont("Helvetica", 7)
    c.setFillColor(BROWN)
    c.drawString(MARGIN, 9 * mm, f"Speedy Scholars - {_BOOK_NAME}")
    c.drawRightString(W - MARGIN, 9 * mm, str(pn))
    c.restoreState()
    page_mascot(c, pn)


# ─── Calculation table component (used by all calc books) ─────────────────
def draw_calc_table(c, x, y, probs, cols=8, fing=None, table_width=None):
    """
    Draw a calculation table with `cols` problem columns and 3 operand rows + Ans row.
    probs: list of column-data, each column is [v1, v2, v3] (None entries skipped).
    fing: optional fingering exercise text printed above the table.
    """
    tw = table_width or (CW * 0.72)
    cw = (tw - 32) / cols
    rh = 18
    sw = 32
    hf = 9
    df = 10
    if fing:
        c.setFont("Helvetica", 7.5)
        c.setFillColor(BROWN)
        c.drawString(x, y - 3, fing)
    hy = y - rh
    c.setFillColor(BROWN)
    c.rect(x, hy, sw, rh, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", hf)
    c.drawCentredString(x + sw / 2, hy + 5, "S.No.")
    for i in range(cols):
        cx = x + sw + i * cw
        c.setFillColor(BROWN)
        c.rect(cx, hy, cw, rh, stroke=0, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", hf)
        c.drawCentredString(cx + cw / 2, hy + 5, str(i + 1))
    for ri, lab in enumerate(["1", "2", "3", "Ans."]):
        ry = hy - (ri + 1) * rh
        ia = lab == "Ans."
        c.setFillColor(TH if ia else TF)
        c.rect(x, ry, sw, rh, stroke=0, fill=1)
        c.setStrokeColor(LIGHT_GOLD)
        c.setLineWidth(0.3)
        c.rect(x, ry, sw, rh, stroke=1, fill=0)
        c.setFillColor(DARKER_BROWN)
        c.setFont("Helvetica-Bold" if ia else "Helvetica", hf)
        c.drawCentredString(x + sw / 2, ry + 5, lab)
        for i in range(cols):
            cx = x + sw + i * cw
            c.setFillColor(TH if ia else TF)
            c.rect(cx, ry, cw, rh, stroke=0, fill=1)
            c.setStrokeColor(LIGHT_GOLD)
            c.setLineWidth(0.3)
            c.rect(cx, ry, cw, rh, stroke=1, fill=0)
            if not ia and i < len(probs) and ri < len(probs[i]) and probs[i][ri] is not None:
                v = probs[i][ri]
                c.setFillColor(DARKER_BROWN)
                c.setFont("Helvetica", df)
                # Abacus convention: positive numbers show as bare digits (no +),
                # only negative numbers show their sign.
                c.drawCentredString(cx + cw / 2, ry + 5, str(v))
    return hy - 5 * rh - 4
