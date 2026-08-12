#!/usr/bin/env python3
"""
Generate the Open Graph / social-share image for Speedy Scholars.

Output: public/images/og-image.jpg  (1200x630, the standard OG size)

Brand: purple/gold owl rebrand. Re-run whenever the headline stats or the
free-demo duration change so social shares never go stale.

    python3 scripts/generate_og_image.py
"""
import os
from PIL import Image, ImageDraw, ImageFont

# ---- Brand palette (see CLAUDE.md) ----
CREAM       = (248, 245, 249)   # #F8F5F9  background
PURPLE      = (90, 42, 114)     # #5A2A72  primary
PURPLE_DARK = (50, 23, 63)      # #32173F  emphasis text
GOLD        = (249, 174, 39)    # #F9AE27  accent (wordmark, underline)
GOLD_DARK   = (202, 132, 6)     # #CA8406  gold text on light (readable)
WHITE       = (255, 255, 255)

W, H = 1200, 630
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWL_PATH = os.path.join(ROOT, "public", "images", "mascot-owl.png")
OUT_PATH = os.path.join(ROOT, "public", "images", "og-image.jpg")

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size):
    return ImageFont.truetype(FONT_BOLD, size)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Owl on the right, vertically centred
    owl = Image.open(OWL_PATH).convert("RGBA")
    owl_h = 470
    owl = owl.resize((owl_h, owl_h), Image.LANCZOS)
    img.paste(owl, (W - owl_h - 25, (H - owl_h) // 2), owl)

    left = 62

    # Wordmark: "Speedy " (gold) + "Scholars" (purple)
    wf = font(52)
    d.text((left, 52), "Speedy ", font=wf, fill=GOLD)
    speedy_w = d.textlength("Speedy ", font=wf)
    d.text((left + speedy_w, 52), "Scholars", font=wf, fill=PURPLE)

    # Headline
    hf = font(84)
    d.text((left, 170), "Online Abacus", font=hf, fill=PURPLE)
    d.text((left, 262), "Classes for Kids", font=hf, fill=PURPLE)

    # Gold underline bar
    d.rectangle([left + 2, 368, left + 2 + 372, 368 + 9], fill=GOLD)

    # Stats line
    sf = font(31)
    d.text((left, 404), "20+ years experience   •   2,000+ students",
           font=sf, fill=PURPLE_DARK)

    # Free demo line (gold-dark for readability on cream)
    df = font(29)
    d.text((left, 450), "Free 30-minute demo class", font=df, fill=GOLD_DARK)

    # URL pill
    pf = font(27)
    url = "speedyscholars.com"
    tw = d.textlength(url, font=pf)
    px0, py0 = left, 512
    pad_x, pad_y = 26, 16
    d.rounded_rectangle(
        [px0, py0, px0 + tw + pad_x * 2, py0 + 27 + pad_y * 2],
        radius=32, fill=PURPLE,
    )
    d.text((px0 + pad_x, py0 + pad_y), url, font=pf, fill=WHITE)

    # Thin purple accent strip along the bottom
    d.rectangle([0, H - 8, W, H], fill=PURPLE)

    img.save(OUT_PATH, "JPEG", quality=90)
    print(f"Wrote {OUT_PATH} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
