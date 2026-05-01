"""
Speedy Scholars — Kid-Friendly Illustration Library v3
Enhanced: bigger objects, dotted tracing, crosshair boxes, tree, better hands.
"""

from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.units import mm
import math

# Brand colours
BROWN        = HexColor("#8B6F47")
DARK_BROWN   = HexColor("#6B5335")
DARKER_BROWN = HexColor("#5A4830")
GOLD         = HexColor("#C9A86C")
LIGHT_GOLD   = HexColor("#D4B896")
CREAM        = HexColor("#F5EDE3")
WARM_WHITE   = HexColor("#FFF8F0")
LIGHT_BROWN  = HexColor("#C4A882")
NAVY         = HexColor("#2C3E50")
SKIN         = HexColor("#FDDCB5")
LEAF_GREEN   = HexColor("#A0875A")  # warm earthy brown (no green on brand)
RED_FRUIT    = HexColor("#CC4444")
ORANGE_BEAK  = HexColor("#E8A040")


# ══════════════════════════════════════════════════════════════
# MASCOT: Bead Bird
# ══════════════════════════════════════════════════════════════

def draw_bead_bird(c, x, y, size=20, color=None, facing="right", expression="happy",
                   has_wings=True, has_feet=True, hat=None, action=None):
    """
    Draw a cute bead-shaped bird mascot.
    action: None, "pointing", "sitting", "waving"
    """
    if color is None:
        color = GOLD
    c.saveState()
    bw = size * 0.7
    bh = size
    d = 1 if facing == "right" else -1

    # Body
    c.setFillColor(color)
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(max(0.6, size * 0.04))
    p = c.beginPath()
    p.moveTo(x, y + bh * 0.5)
    p.curveTo(x + bw * 0.6, y + bh * 0.3, x + bw * 0.6, y - bh * 0.3, x, y - bh * 0.5)
    p.curveTo(x - bw * 0.6, y - bh * 0.3, x - bw * 0.6, y + bh * 0.3, x, y + bh * 0.5)
    c.drawPath(p, stroke=1, fill=1)

    # Highlight
    c.setFillColor(white)
    c.circle(x - bw * 0.2, y + bh * 0.2, size * 0.07, stroke=0, fill=1)

    # Eyes
    ey = y + bh * 0.12
    er = size * 0.08
    for ex_off in [-bw * 0.18, bw * 0.18]:
        c.setFillColor(white)
        c.setStrokeColor(DARKER_BROWN)
        c.setLineWidth(0.5)
        c.circle(x + ex_off, ey, er * 1.4, stroke=1, fill=1)
        c.setFillColor(NAVY)
        po = er * 0.3 * d
        if expression == "wink" and ex_off > 0:
            c.setStrokeColor(NAVY)
            c.setLineWidth(0.8)
            c.arc(x + ex_off - er, ey - er * 0.5, x + ex_off + er, ey + er * 0.5, 0, 180)
        else:
            pr = er * 0.7 if expression != "surprised" else er * 0.9
            c.circle(x + ex_off + po, ey, pr, stroke=0, fill=1)
        # Shine
        c.setFillColor(white)
        c.circle(x + ex_off + po - er * 0.25, ey + er * 0.25, er * 0.25, stroke=0, fill=1)

    # Beak
    beak_x = x + bw * 0.38 * d
    bs = size * 0.13
    c.setFillColor(ORANGE_BEAK)
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(0.5)
    p = c.beginPath()
    p.moveTo(beak_x, y + bs * 0.4)
    p.lineTo(beak_x + bs * 1.3 * d, y)
    p.lineTo(beak_x, y - bs * 0.4)
    p.close()
    c.drawPath(p, stroke=1, fill=1)

    # Mouth
    if expression in ("happy", "wink"):
        c.setStrokeColor(DARK_BROWN)
        c.setLineWidth(0.5)
        sw = bw * 0.18
        c.arc(x - sw, y - bh * 0.15, x + sw, y - bh * 0.05, 200, 140)
    elif expression == "surprised":
        c.setFillColor(DARK_BROWN)
        c.circle(x, y - bh * 0.1, size * 0.035, stroke=0, fill=1)

    # Wings
    if has_wings:
        wy = y - bh * 0.05
        for side in [-1, 1]:
            wx = x + bw * 0.5 * side
            c.setFillColor(color)
            c.setStrokeColor(DARK_BROWN)
            c.setLineWidth(0.4)
            p = c.beginPath()
            p.moveTo(wx, wy)
            wt_x = wx + size * 0.4 * side
            p.curveTo(wx + size * 0.15 * side, wy + size * 0.12, wt_x, wy + size * 0.06, wt_x, wy - size * 0.12)
            p.curveTo(wt_x - size * 0.08 * side, wy - size * 0.1, wx + size * 0.08 * side, wy - size * 0.13, wx, wy - size * 0.08)
            p.close()
            c.drawPath(p, stroke=1, fill=1)
            # If waving, raise one wing
            if action == "waving" and side == d:
                c.setFillColor(color)
                p2 = c.beginPath()
                p2.moveTo(wx, wy + size * 0.1)
                p2.curveTo(wx + size * 0.2 * side, wy + size * 0.35, wt_x, wy + size * 0.4, wt_x, wy + size * 0.2)
                p2.lineTo(wx, wy + size * 0.1)
                p2.close()
                c.drawPath(p2, stroke=1, fill=1)

    # Feet
    if has_feet:
        fy = y - bh * 0.55
        for fx_off in [-bw * 0.15, bw * 0.15]:
            fx = x + fx_off
            c.setStrokeColor(ORANGE_BEAK)
            c.setLineWidth(max(0.8, size * 0.04))
            c.line(fx, fy + size * 0.05, fx, fy - size * 0.08)
            for a in [-25, 0, 25]:
                r = math.radians(a)
                tl = size * 0.06
                c.line(fx, fy - size * 0.08, fx + tl * math.sin(r), fy - size * 0.08 - tl * math.cos(r))

    # Hat
    if hat == "graduation":
        hy = y + bh * 0.45
        hw = bw * 0.9
        c.setFillColor(NAVY)
        c.setStrokeColor(DARKER_BROWN)
        c.setLineWidth(0.5)
        c.rect(x - hw * 0.6, hy + size * 0.05, hw * 1.2, size * 0.04, stroke=1, fill=1)
        c.roundRect(x - hw * 0.35, hy - size * 0.05, hw * 0.7, size * 0.12, 1, stroke=1, fill=1)
        c.setStrokeColor(GOLD)
        c.setLineWidth(0.6)
        c.line(x + hw * 0.5, hy + size * 0.07, x + hw * 0.7, hy - size * 0.02)
        c.setFillColor(GOLD)
        c.circle(x + hw * 0.7, hy - size * 0.03, size * 0.025, stroke=0, fill=1)

    c.restoreState()


# ══════════════════════════════════════════════════════════════
# DECORATIVE
# ══════════════════════════════════════════════════════════════

def draw_star(c, x, y, size=8, color=None, filled=True):
    if color is None: color = GOLD
    c.saveState()
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.4)
    p = c.beginPath()
    for i in range(5):
        a1 = math.radians(90 + i * 72)
        p.lineTo(x + size * math.cos(a1), y + size * math.sin(a1)) if i else p.moveTo(x + size * math.cos(a1), y + size * math.sin(a1))
        a2 = math.radians(90 + i * 72 + 36)
        p.lineTo(x + size * 0.4 * math.cos(a2), y + size * 0.4 * math.sin(a2))
    p.close()
    c.drawPath(p, stroke=1, fill=filled)
    c.restoreState()

def draw_sparkle(c, x, y, size=5, color=None):
    if color is None: color = GOLD
    c.saveState(); c.setStrokeColor(color); c.setLineWidth(0.8)
    c.line(x, y - size, x, y + size); c.line(x - size, y, x + size, y)
    d = size * 0.6
    c.line(x - d, y - d, x + d, y + d); c.line(x - d, y + d, x + d, y - d)
    c.restoreState()

def draw_cloud(c, x, y, width=30, height=15, color=None):
    if color is None: color = WARM_WHITE
    c.saveState(); c.setFillColor(color); c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.5)
    r = height * 0.5
    for dx, dy, s in [(0, 0, 1), (0.25, 0.3, 1.1), (0.55, 0.1, 0.9), (0.35, -0.2, 0.8), (0.7, -0.1, 0.7)]:
        c.circle(x + width * dx, y + r * dy, r * s, stroke=1, fill=1)
    c.restoreState()


# ══════════════════════════════════════════════════════════════
# OBJECTS — All drawn BIG and charming
# ══════════════════════════════════════════════════════════════

def draw_apple(c, x, y, size=20):
    c.saveState()
    r = size * 0.42
    c.setFillColor(RED_FRUIT); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)
    c.circle(x - r * 0.25, y, r, stroke=1, fill=1)
    c.circle(x + r * 0.25, y, r, stroke=1, fill=1)
    # Stem
    c.setStrokeColor(DARK_BROWN); c.setLineWidth(1.2)
    c.line(x, y + r * 0.7, x + size * 0.04, y + r * 1.4)
    # Leaf
    c.setFillColor(LEAF_GREEN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.3)
    p = c.beginPath()
    p.moveTo(x + size * 0.04, y + r * 1.2)
    p.curveTo(x + size * 0.22, y + r * 1.6, x + size * 0.3, y + r * 1.1, x + size * 0.04, y + r * 0.9)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    # Highlight
    c.setFillColor(white); c.circle(x - r * 0.35, y + r * 0.35, size * 0.07, stroke=0, fill=1)
    c.restoreState()

def draw_fish(c, x, y, size=22, color=None):
    if color is None: color = GOLD
    c.saveState()
    bw, bh = size * 0.5, size * 0.3
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)
    c.ellipse(x - bw, y - bh, x + bw * 0.7, y + bh, stroke=1, fill=1)
    # Tail
    p = c.beginPath()
    p.moveTo(x + bw * 0.55, y + bh * 0.3)
    p.lineTo(x + bw, y + bh * 0.9)
    p.lineTo(x + bw, y - bh * 0.9)
    p.lineTo(x + bw * 0.55, y - bh * 0.3)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    # Eye
    c.setFillColor(white); c.circle(x - bw * 0.35, y + bh * 0.15, size * 0.08, stroke=1, fill=1)
    c.setFillColor(NAVY); c.circle(x - bw * 0.38, y + bh * 0.15, size * 0.04, stroke=0, fill=1)
    # Fin
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN)
    p2 = c.beginPath()
    p2.moveTo(x - bw * 0.1, y + bh * 0.8)
    p2.curveTo(x, y + bh * 1.3, x + bw * 0.2, y + bh * 1.1, x + bw * 0.1, y + bh * 0.7)
    p2.close(); c.drawPath(p2, stroke=1, fill=1)
    # Scales (subtle)
    c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.2)
    for i in range(3):
        sx = x - bw * 0.2 + i * bw * 0.25
        c.arc(sx - bh * 0.2, y - bh * 0.3, sx + bh * 0.2, y + bh * 0.1, 30, 120)
    c.restoreState()

def draw_flower(c, x, y, size=18, color=None):
    if color is None: color = GOLD
    c.saveState()
    pr = size * 0.28
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.4)
    for i in range(5):
        a = math.radians(90 + i * 72)
        c.circle(x + size * 0.22 * math.cos(a), y + size * 0.22 * math.sin(a), pr, stroke=1, fill=1)
    c.setFillColor(ORANGE_BEAK); c.circle(x, y, pr * 0.7, stroke=1, fill=1)
    # Stem
    c.setStrokeColor(LEAF_GREEN); c.setLineWidth(1.2)
    c.line(x, y - size * 0.32, x, y - size * 0.85)
    # Leaf
    c.setFillColor(LEAF_GREEN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.3)
    p = c.beginPath()
    p.moveTo(x, y - size * 0.5)
    p.curveTo(x + size * 0.2, y - size * 0.4, x + size * 0.25, y - size * 0.6, x, y - size * 0.65)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    c.restoreState()

def draw_bird(c, x, y, size=18, color=None, facing="right"):
    if color is None: color = LIGHT_GOLD
    c.saveState()
    d = 1 if facing == "right" else -1
    # Body
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
    c.circle(x, y, size * 0.35, stroke=1, fill=1)
    # Head
    hx = x + size * 0.28 * d; hy = y + size * 0.25
    c.circle(hx, hy, size * 0.22, stroke=1, fill=1)
    # Eye
    c.setFillColor(NAVY); c.circle(hx + size * 0.08 * d, hy + size * 0.05, size * 0.04, stroke=0, fill=1)
    # Beak
    c.setFillColor(ORANGE_BEAK); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.4)
    p = c.beginPath()
    p.moveTo(hx + size * 0.14 * d, hy + size * 0.02)
    p.lineTo(hx + size * 0.28 * d, hy)
    p.lineTo(hx + size * 0.14 * d, hy - size * 0.04)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    # Tail
    c.setFillColor(color)
    tx = x - size * 0.3 * d
    p2 = c.beginPath()
    p2.moveTo(x - size * 0.2 * d, y)
    p2.lineTo(tx, y + size * 0.15); p2.lineTo(tx - size * 0.08 * d, y)
    p2.lineTo(tx, y - size * 0.1); p2.close()
    c.drawPath(p2, stroke=1, fill=1)
    # Wing
    c.setFillColor(BROWN)
    c.ellipse(x - size * 0.15, y - size * 0.05, x + size * 0.08, y + size * 0.15, stroke=1, fill=1)
    c.restoreState()

def draw_bone(c, x, y, size=20, angle=0):
    c.saveState(); c.translate(x, y); c.rotate(angle)
    c.setFillColor(WARM_WHITE); c.setStrokeColor(DARK_BROWN); c.setLineWidth(max(0.6, size * 0.03))
    sw, sh = size * 0.5, size * 0.2
    c.rect(-sw / 2, -sh / 2, sw, sh, stroke=1, fill=1)
    # Knobs — bigger and more visible
    kr = size * 0.18
    for sx in [-sw / 2, sw / 2]:
        for sy in [-kr * 0.55, kr * 0.55]:
            c.circle(sx, sy, kr, stroke=1, fill=1)
    # Center dot for detail
    c.setFillColor(HexColor("#E8DDD0"))
    c.circle(0, 0, size * 0.04, stroke=0, fill=1)
    c.restoreState()

def draw_butterfly(c, x, y, size=16, color=None):
    if color is None: color = GOLD
    c.saveState()
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.4)
    ww, wh = size * 0.35, size * 0.42
    for sx, sy in [(-1, 1), (1, 1), (-1, -1), (1, -1)]:
        wx = x + ww * 0.5 * sx; wy = y + wh * 0.35 * sy
        c.ellipse(wx - ww * 0.5, wy - wh * 0.4, wx + ww * 0.5, wy + wh * 0.4, stroke=1, fill=1)
    c.setFillColor(DARKER_BROWN)
    c.rect(x - size * 0.04, y - size * 0.32, size * 0.08, size * 0.64, stroke=0, fill=1)
    c.setStrokeColor(DARKER_BROWN); c.setLineWidth(0.5)
    c.line(x, y + size * 0.32, x - size * 0.15, y + size * 0.48)
    c.line(x, y + size * 0.32, x + size * 0.15, y + size * 0.48)
    c.setFillColor(DARKER_BROWN)
    c.circle(x - size * 0.15, y + size * 0.48, 1.2, stroke=0, fill=1)
    c.circle(x + size * 0.15, y + size * 0.48, 1.2, stroke=0, fill=1)
    c.restoreState()

def draw_strawberry(c, x, y, size=18):
    c.saveState()
    r = size * 0.4
    c.setFillColor(RED_FRUIT); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
    p = c.beginPath()
    p.moveTo(x - r, y + r * 0.5)
    p.curveTo(x - r, y + r * 1.3, x + r, y + r * 1.3, x + r, y + r * 0.5)
    p.lineTo(x, y - r * 0.9); p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setFillColor(HexColor("#FFCC00"))
    for sx, sy in [(-0.15, 0.3), (0.15, 0.3), (0, 0.05), (-0.2, -0.15), (0.2, -0.15)]:
        c.circle(x + r * sx, y + r * sy, 0.9, stroke=0, fill=1)
    c.setFillColor(LEAF_GREEN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.3)
    for a in [-30, 0, 30]:
        rad = math.radians(a)
        lx = x + size * 0.12 * math.sin(rad); ly = y + r * 0.75
        c.ellipse(lx - size * 0.08, ly - size * 0.02, lx + size * 0.08, ly + size * 0.12, stroke=1, fill=1)
    c.restoreState()

def draw_pineapple(c, x, y, size=22):
    c.saveState()
    bw, bh = size * 0.38, size * 0.5
    c.setFillColor(ORANGE_BEAK); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
    c.ellipse(x - bw, y - bh, x + bw, y + bh * 0.5, stroke=1, fill=1)
    c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.25)
    for i in range(-2, 3):
        off = i * bw * 0.35
        c.line(x + off - bw * 0.25, y - bh * 0.6, x + off + bw * 0.25, y + bh * 0.25)
        c.line(x + off + bw * 0.25, y - bh * 0.6, x + off - bw * 0.25, y + bh * 0.25)
    c.setFillColor(LEAF_GREEN)
    for a in [-20, -10, 0, 10, 20]:
        rad = math.radians(a)
        lx = x + size * 0.15 * math.sin(rad)
        c.ellipse(lx - size * 0.05, y + bh * 0.3, lx + size * 0.05, y + bh * 0.3 + size * 0.3, stroke=1, fill=1)
    c.restoreState()

def draw_balloon(c, x, y, size=20, color=None):
    if color is None: color = GOLD
    c.saveState()
    r = size * 0.38
    c.setFillColor(color); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
    c.ellipse(x - r, y, x + r, y + r * 2.2, stroke=1, fill=1)
    p = c.beginPath()
    p.moveTo(x - size * 0.04, y + size * 0.02)
    p.lineTo(x, y - size * 0.04); p.lineTo(x + size * 0.04, y + size * 0.02); p.close()
    c.drawPath(p, stroke=1, fill=1)
    c.setStrokeColor(BROWN); c.setLineWidth(0.4)
    c.line(x, y - size * 0.04, x + size * 0.05, y - size * 0.4)
    c.setFillColor(white); c.circle(x - r * 0.3, y + r * 1.5, size * 0.05, stroke=0, fill=1)
    c.restoreState()

def draw_mango(c, x, y, size=20):
    """Mango — kidney/teardrop shape."""
    c.saveState()
    c.setFillColor(HexColor("#F4B942")); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)
    r = size * 0.4
    p = c.beginPath()
    p.moveTo(x, y + r * 1.1)
    p.curveTo(x + r * 1.1, y + r * 0.8, x + r * 1.1, y - r * 0.5, x, y - r * 0.9)
    p.curveTo(x - r * 0.8, y - r * 0.3, x - r * 0.8, y + r * 0.6, x, y + r * 1.1)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    # Blush
    c.setFillColor(HexColor("#E88030"))
    c.circle(x + r * 0.2, y + r * 0.3, r * 0.4, stroke=0, fill=1)
    # Stem
    c.setStrokeColor(LEAF_GREEN); c.setLineWidth(1)
    c.line(x, y + r * 1.0, x - size * 0.06, y + r * 1.3)
    c.restoreState()

def draw_banana(c, x, y, size=20):
    """Simple banana."""
    c.saveState()
    c.setFillColor(HexColor("#F7E34A")); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)
    p = c.beginPath()
    p.moveTo(x - size * 0.35, y - size * 0.15)
    p.curveTo(x - size * 0.1, y + size * 0.35, x + size * 0.2, y + size * 0.35, x + size * 0.35, y + size * 0.1)
    p.curveTo(x + size * 0.15, y + size * 0.2, x - size * 0.05, y + size * 0.15, x - size * 0.25, y - size * 0.05)
    p.close(); c.drawPath(p, stroke=1, fill=1)
    c.restoreState()

def draw_cherry(c, x, y, size=16):
    """Two cherries."""
    c.saveState()
    r = size * 0.22
    c.setFillColor(HexColor("#CC2233")); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
    c.circle(x - r * 0.8, y, r, stroke=1, fill=1)
    c.circle(x + r * 0.8, y, r, stroke=1, fill=1)
    # Highlights
    c.setFillColor(white)
    c.circle(x - r * 1.0, y + r * 0.3, r * 0.2, stroke=0, fill=1)
    c.circle(x + r * 0.6, y + r * 0.3, r * 0.2, stroke=0, fill=1)
    # Stems
    c.setStrokeColor(LEAF_GREEN); c.setLineWidth(0.8)
    c.line(x - r * 0.8, y + r * 0.8, x, y + size * 0.45)
    c.line(x + r * 0.8, y + r * 0.8, x, y + size * 0.45)
    c.restoreState()


# ══════════════════════════════════════════════════════════════
# HAND — More realistic
# ══════════════════════════════════════════════════════════════

def draw_hand(c, x, y, size=30, fingers_up=5):
    c.saveState()
    pw, ph = size * 0.42, size * 0.3
    fw, fh = size * 0.085, size * 0.28
    gap = pw / 5

    # Palm
    c.setFillColor(SKIN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)
    c.roundRect(x - pw / 2, y - ph / 2, pw, ph, 4, stroke=1, fill=1)
    # Wrist
    ww = pw * 0.55
    c.roundRect(x - ww / 2, y - ph / 2 - size * 0.1, ww, size * 0.12, 2, stroke=1, fill=1)

    # Fingers 1-4
    for i in range(4):
        fx = x - pw / 2 + gap * (i + 0.8)
        fy = y + ph / 2
        h = fh * (0.95 if i in [1, 2] else 0.82)
        is_up = (i + 1) <= fingers_up
        if is_up:
            c.setFillColor(SKIN)
            c.roundRect(fx - fw / 2, fy, fw, h, fw / 2, stroke=1, fill=1)
            # Nail
            c.setFillColor(HexColor("#F5C8A8"))
            c.roundRect(fx - fw * 0.35, fy + h - fw * 0.55, fw * 0.7, fw * 0.45, 2, stroke=0, fill=1)
            # Knuckle lines
            c.setStrokeColor(HexColor("#E0B090")); c.setLineWidth(0.3)
            c.line(fx - fw * 0.3, fy + h * 0.35, fx + fw * 0.3, fy + h * 0.35)
            c.line(fx - fw * 0.3, fy + h * 0.6, fx + fw * 0.3, fy + h * 0.6)
        else:
            c.setFillColor(HexColor("#EECDA5"))
            c.roundRect(fx - fw / 2, fy, fw, fh * 0.12, fw / 2, stroke=1, fill=1)
        c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)

    # Thumb
    c.setFillColor(SKIN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
    tx, ty = x - pw / 2 - size * 0.05, y + ph * 0.1
    if fingers_up >= 5:
        c.saveState(); c.translate(tx, ty); c.rotate(30)
        c.roundRect(-fw / 2, 0, fw * 1.1, fh * 0.65, fw / 2, stroke=1, fill=1)
        c.restoreState()
    else:
        c.setFillColor(HexColor("#EECDA5"))
        c.ellipse(tx - fw * 0.5, ty - fw * 0.3, tx + fw * 0.8, ty + fw * 0.5, stroke=1, fill=1)
    c.restoreState()


# ══════════════════════════════════════════════════════════════
# ABACUS
# ══════════════════════════════════════════════════════════════

def draw_abacus(c, x, y, width, height, upper=0, lower=0, label=None, show_arrows=False):
    c.saveState()
    c.setStrokeColor(DARK_BROWN); c.setFillColor(WARM_WHITE); c.setLineWidth(1.2)
    c.roundRect(x, y, width, height, 3, stroke=1, fill=1)
    beam_y = y + height * 0.65
    c.setFillColor(BROWN); c.rect(x, beam_y - 1.5, width, 3, stroke=0, fill=1)
    rod_x = x + width / 2
    c.setStrokeColor(LIGHT_BROWN); c.setLineWidth(0.8)
    c.line(rod_x, y + 2, rod_x, y + height - 2)

    bw = width * 0.38; bh_u = height * 0.1
    uby = beam_y + bh_u * 1.5 if upper > 0 else y + height - bh_u * 2
    # Upper bead — HEXAGONAL shape
    c.setFillColor(GOLD); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.6)
    hw = bw / 2; hh = bh_u  # half-width and half-height of hexagon
    p = c.beginPath()
    p.moveTo(rod_x - hw, uby)              # left middle
    p.lineTo(rod_x - hw * 0.5, uby + hh)   # top-left
    p.lineTo(rod_x + hw * 0.5, uby + hh)   # top-right
    p.lineTo(rod_x + hw, uby)              # right middle
    p.lineTo(rod_x + hw * 0.5, uby - hh)   # bottom-right
    p.lineTo(rod_x - hw * 0.5, uby - hh)   # bottom-left
    p.close()
    c.drawPath(p, stroke=1, fill=1)

    lt = beam_y - 3; lb = y + 3; sp = (lt - lb) / 4.5
    for i in range(4):
        bcy = lt - (i + 0.5) * sp if i < lower else lb + (3 - i + 0.5) * sp
        c.setFillColor(BROWN if i < lower else LIGHT_GOLD)
        c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
        c.roundRect(rod_x - bw * 0.4, bcy - sp * 0.27, bw * 0.8, sp * 0.55, 2, stroke=1, fill=1)

    if label is not None:
        c.setFont("Helvetica-Bold", min(10, width * 0.4))
        c.setFillColor(DARKER_BROWN)
        c.drawCentredString(x + width / 2, y - 11, str(label))

    if show_arrows:
        c.setStrokeColor(HexColor("#CC6644")); c.setLineWidth(1)
        ax = x + width + 3
        if upper > 0:
            c.line(ax, y + height - 5, ax, beam_y + 8)
            c.line(ax - 2, beam_y + 12, ax, beam_y + 8); c.line(ax + 2, beam_y + 12, ax, beam_y + 8)
        if lower > 0:
            c.line(ax, y + 5, ax, beam_y - 8)
            c.line(ax - 2, beam_y - 12, ax, beam_y - 8); c.line(ax + 2, beam_y - 12, ax, beam_y - 8)
    c.restoreState()


# ══════════════════════════════════════════════════════════════
# NEW: Dotted tracing number
# ══════════════════════════════════════════════════════════════

def draw_dotted_number(c, x, y, num, size=28):
    """Draw a number as dashed outline for tracing."""
    c.saveState()
    c.setFont("Helvetica-Bold", size)
    c.setFillColor(HexColor("#E0D0C0"))  # very light, almost invisible solid
    c.drawCentredString(x, y, str(num))
    # Overlay with dashed version
    c.setDash(1.5, 2.5)
    c.setStrokeColor(BROWN)
    c.setLineWidth(0.4)
    # Draw guiding dashes around the number using textpath is not available,
    # so we use the light solid + dashed underline as visual cue
    text_w = c.stringWidth(str(num), "Helvetica-Bold", size)
    c.line(x - text_w / 2, y - 1, x + text_w / 2, y - 1)
    c.setDash()
    c.restoreState()


def draw_crosshair_box(c, x, y, size):
    """Draw a practice box with crosshair guidelines."""
    c.saveState()
    c.setStrokeColor(LIGHT_GOLD); c.setLineWidth(0.5)
    c.rect(x, y, size, size, stroke=1, fill=0)
    # Crosshair
    c.setDash(1, 2); c.setStrokeColor(HexColor("#E8DDD0")); c.setLineWidth(0.3)
    c.line(x + size / 2, y, x + size / 2, y + size)  # vertical
    c.line(x, y + size / 2, x + size, y + size / 2)  # horizontal
    c.setDash()
    c.restoreState()


# ══════════════════════════════════════════════════════════════
# NEW: Apple tree for composition of 5
# ══════════════════════════════════════════════════════════════

def draw_apple_tree(c, x, y, width, height, apple_numbers=None):
    """Draw a tree with numbered apples on branches."""
    if apple_numbers is None:
        apple_numbers = [1, 2, 3, 4, 5]
    c.saveState()
    # Trunk
    tw = width * 0.15
    c.setFillColor(BROWN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(1)
    c.rect(x + width / 2 - tw / 2, y, tw, height * 0.4, stroke=1, fill=1)
    # Canopy (big fluffy cloud shape)
    c.setFillColor(LEAF_GREEN); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.8)
    cx, cy = x + width / 2, y + height * 0.65
    rw, rh = width * 0.45, height * 0.35
    c.circle(cx, cy, rh, stroke=1, fill=1)
    c.circle(cx - rw * 0.5, cy - rh * 0.2, rh * 0.75, stroke=1, fill=1)
    c.circle(cx + rw * 0.5, cy - rh * 0.2, rh * 0.75, stroke=1, fill=1)
    c.circle(cx - rw * 0.3, cy + rh * 0.4, rh * 0.6, stroke=1, fill=1)
    c.circle(cx + rw * 0.3, cy + rh * 0.4, rh * 0.6, stroke=1, fill=1)

    # Apples with numbers
    positions = [
        (cx - rw * 0.3, cy + rh * 0.15),
        (cx + rw * 0.35, cy + rh * 0.1),
        (cx - rw * 0.1, cy - rh * 0.25),
        (cx + rw * 0.15, cy + rh * 0.45),
        (cx - rw * 0.4, cy - rh * 0.05),
    ]
    for i, num in enumerate(apple_numbers[:len(positions)]):
        ax, ay = positions[i]
        ar = min(width, height) * 0.08
        c.setFillColor(RED_FRUIT); c.setStrokeColor(DARK_BROWN); c.setLineWidth(0.5)
        c.circle(ax, ay, ar, stroke=1, fill=1)
        c.setFillColor(white); c.setFont("Helvetica-Bold", ar * 1.2)
        c.drawCentredString(ax, ay - ar * 0.35, str(num))
    c.restoreState()


def scatter_decorations(c, seed=0, count=8):
    """Scatter small doodles in margins."""
    import random
    random.seed(seed)
    for _ in range(count):
        ex = random.choice([random.uniform(5, 18 * mm - 5), random.uniform(841.89 - 18 * mm + 5, 841.89 - 5)])
        ey = random.uniform(20 * mm, 595.28 - 20 * mm)
        ch = random.randint(0, 3)
        if ch == 0: draw_star(c, ex, ey, size=3 + random.random() * 3, color=LIGHT_GOLD)
        elif ch == 1: draw_sparkle(c, ex, ey, size=2 + random.random() * 2, color=GOLD)
        elif ch == 2:
            c.setFillColor(LIGHT_GOLD); c.circle(ex, ey, 1.5, stroke=0, fill=1)
        else: draw_butterfly(c, ex, ey, size=6, color=LIGHT_GOLD)
