#!/usr/bin/env python3
"""Draw the front page of The Daily Ledger for Wednesday 25 November 2026.

A program-generated newspaper front page (Pillow only, no network, no
randomness) that sums up the day's verified world news. Run it as:

    python3 gen.py [output_path]

Default output is entry.png next to this file.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (26, 26, 26)
NAVY = (27, 42, 74)
RED = (179, 39, 30)
TEAL = (31, 111, 107)
GOLD = (176, 124, 32)
GREY = (90, 86, 78)
LIGHT_LINE = (200, 192, 172)
SEA = (44, 92, 128)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def serif_b(s):
    return font("DejaVuSerif-Bold.ttf", s)


def serif(s):
    return font("DejaVuSerif.ttf", s)


def sans_b(s):
    return font("DejaVuSans-Bold.ttf", s)


def sans(s):
    return font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, max_w, fill=INK, leading=None):
    """Draw wrapped text; return the y just below the last line."""
    x, y = xy
    leading = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, xy, text, color=RED):
    fnt = sans_b(17)
    draw.text(xy, text, font=fnt, fill=color)
    return xy[1] + 24


# ---------------------------------------------------------------- icons
def icon_tanker(draw, x, y, s):
    """Two tankers on a strait, one burning."""
    draw.rectangle([x, y + 34 * s, x + 150 * s, y + 52 * s], fill=NAVY)
    draw.rectangle([x + 8 * s, y + 20 * s, x + 40 * s, y + 34 * s], fill=NAVY)
    draw.rectangle([x + 95 * s, y + 24 * s, x + 118 * s, y + 34 * s], fill=NAVY)
    for i, r in enumerate((16, 12, 9)):
        draw.ellipse(
            [x + 118 * s + i * 6 * s, y + (4 - i * 8) * s,
             x + 118 * s + i * 6 * s + r * 2 * s,
             y + (4 - i * 8) * s + r * 2 * s],
            fill=(120, 120, 115),
        )
    draw.polygon(
        [(x + 128 * s, y + 30 * s), (x + 140 * s, y + 8 * s),
         (x + 152 * s, y + 30 * s)],
        fill=(232, 120, 30),
    )
    for i in range(5):
        wx = x + i * 34 * s
        draw.arc([wx, y + 54 * s, wx + 30 * s, y + 66 * s],
                 0, 180, fill=SEA, width=3)


def icon_rocket(draw, x, y, s):
    draw.polygon([(x + 45 * s, y), (x + 60 * s, y + 34 * s),
                  (x + 30 * s, y + 34 * s)], fill=RED)
    draw.rectangle([x + 30 * s, y + 34 * s, x + 60 * s, y + 96 * s], fill=INK)
    draw.ellipse([x + 38 * s, y + 48 * s, x + 52 * s, y + 62 * s], fill=GOLD)
    draw.polygon([(x + 30 * s, y + 96 * s), (x + 14 * s, y + 118 * s),
                  (x + 30 * s, y + 108 * s)], fill=RED)
    draw.polygon([(x + 60 * s, y + 96 * s), (x + 76 * s, y + 118 * s),
                  (x + 60 * s, y + 108 * s)], fill=RED)
    draw.polygon([(x + 38 * s, y + 108 * s), (x + 45 * s, y + 132 * s),
                  (x + 52 * s, y + 108 * s)], fill=(232, 120, 30))
    for i in range(3):
        draw.ellipse([x + 6 * s + i * 26 * s, y + 128 * s,
                      x + 14 * s + i * 26 * s, y + 136 * s], fill=GOLD)


def icon_chart(draw, x, y, s):
    draw.rectangle([x, y, x + 150 * s, y + 110 * s], fill=(255, 255, 255),
                   outline=LIGHT_LINE, width=2)
    pts = [(x + 12 * s, y + 22 * s), (x + 42 * s, y + 34 * s),
           (x + 72 * s, y + 30 * s), (x + 102 * s, y + 62 * s),
           (x + 132 * s, y + 92 * s)]
    draw.line(pts, fill=RED, width=5, joint="curve")
    draw.polygon([(x + 132 * s, y + 92 * s), (x + 118 * s, y + 88 * s),
                  (x + 128 * s, y + 76 * s)], fill=RED)


def icon_city(draw, x, y, s):
    for i, h in enumerate((70, 95, 60, 85)):
        bx = x + i * 38 * s
        draw.rectangle([bx, y + 110 * s - h * s, bx + 30 * s, y + 110 * s],
                       fill=NAVY)
        draw.rectangle([bx + 8 * s, y + 110 * s - h * s - 8 * s,
                        bx + 22 * s, y + 110 * s - h * s], fill=NAVY)
    draw.polygon([(x + 96 * s, y + 8 * s), (x + 108 * s, y - 14 * s),
                  (x + 120 * s, y + 8 * s)], fill=(232, 120, 30))
    draw.polygon([(x + 100 * s, y + 8 * s), (x + 108 * s, y - 4 * s),
                  (x + 116 * s, y + 8 * s)], fill=GOLD)


def icon_people(draw, x, y, s):
    draw.rectangle([x, y, x + 150 * s, y + 26 * s], fill=TEAL)
    for i in range(3):
        cx = x + 18 * s + i * 44 * s
        draw.ellipse([cx, y + 40 * s, cx + 18 * s, y + 58 * s], fill=INK)
        draw.rectangle([cx + 2 * s, y + 60 * s, cx + 16 * s, y + 96 * s],
                       fill=INK)
        draw.rectangle([cx + 2 * s, y + 96 * s, cx + 7 * s, y + 118 * s],
                       fill=INK)
        draw.rectangle([cx + 11 * s, y + 96 * s, cx + 16 * s, y + 118 * s],
                       fill=INK)


def icon_flags(draw, x, y, s):
    for i, col in enumerate((TEAL, GOLD)):
        px = x + i * 70 * s
        draw.line([(px, y), (px, y + 110 * s)], fill=INK, width=4)
        draw.polygon([(px, y), (px + 58 * s, y + 16 * s), (px, y + 32 * s)],
                     fill=col)
    draw.ellipse([x + 58 * s, y + 46 * s, x + 92 * s, y + 80 * s],
                 outline=NAVY, width=4)


def icon_refinery(draw, x, y, s):
    for i, h in enumerate((95, 70, 110)):
        bx = x + i * 48 * s
        draw.rectangle([bx, y + 118 * s - h * s, bx + 26 * s, y + 118 * s],
                       fill=NAVY)
        draw.polygon([(bx + 4 * s, y + 118 * s - h * s),
                      (bx + 13 * s, y + 118 * s - h * s - 22 * s),
                      (bx + 22 * s, y + 118 * s - h * s)], fill=NAVY)
    draw.ellipse([x + 108 * s, y + 4 * s, x + 140 * s, y + 36 * s],
                 fill=(232, 120, 30))
    draw.ellipse([x + 116 * s, y + 12 * s, x + 132 * s, y + 28 * s],
                 fill=GOLD)


def icon_globe(draw, x, y, s):
    draw.ellipse([x, y, x + 120 * s, y + 120 * s], outline=TEAL, width=5)
    draw.arc([x + 12 * s, y + 18 * s, x + 108 * s, y + 102 * s],
             200, 340, fill=TEAL, width=4)
    draw.arc([x + 30 * s, y + 6 * s, x + 90 * s, y + 114 * s],
             90, 270, fill=TEAL, width=4)
    draw.line([(x, y + 60 * s), (x + 120 * s, y + 60 * s)], fill=TEAL, width=4)
    draw.line([(x + 128 * s, y + 100 * s), (x + 128 * s, y + 20 * s)],
              fill=RED, width=5)
    draw.polygon([(x + 128 * s, y + 12 * s), (x + 118 * s, y + 30 * s),
                  (x + 138 * s, y + 30 * s)], fill=RED)


# ---------------------------------------------------------------- page
def build_page(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([22, 22, W - 23, H - 23], outline=LIGHT_LINE, width=1)

    # masthead
    d.rectangle([22, 22, W - 23, 170], fill=NAVY)
    d.text((512, 40), "THE DAILY LEDGER", font=serif_b(62),
           fill=(247, 242, 231), anchor="ma")
    d.text((512, 112), "WEDNESDAY  25  NOVEMBER  2026",
           font=sans_b(23), fill=GOLD, anchor="ma")
    d.text((512, 146), "One day's world news  ·  verified from reports dated 25 November 2026",
           font=sans(17), fill=(205, 210, 225), anchor="ma")

    # ---- lead: Hormuz
    lx, ly, lw = 40, 192, 560
    y = kicker(d, (lx, ly), "LEAD  ·  MIDDLE EAST")
    y = para(d, (lx, y), "TANKERS ABLAZE IN THE STRAIT OF HORMUZ",
             serif_b(40), lw, leading=46)
    y = para(d, (lx, y + 6),
             "Two oil tankers struck naval mines and caught fire in the "
             "strait, Iran's Revolutionary Guard said. [CLAIM]",
             sans(21), lw, leading=27)
    icon_tanker(d, lx + 200, 430, 0.9)
    d.text((lx, 505), "25 NOV 2026  ·  STRAIT OF HORMUZ",
           font=sans_b(15), fill=GREY)

    # ---- right column
    d.line([(620, 192), (620, 520)], fill=LIGHT_LINE, width=2)
    rx = 640
    y = kicker(d, (rx, 192), "SPACE")
    y = para(d, (rx, y), "Pakistan's first astronaut reaches Tiangong",
             serif_b(27), 344, leading=31)
    y = para(d, (rx, y + 4),
             "Shenzhou-24 docked with Tiangong on Wednesday, carrying "
             "Pakistan's first astronaut.",
             sans(19), 344, leading=24)

    d.line([(rx, 392), (984, 392)], fill=LIGHT_LINE, width=2)
    y = kicker(d, (rx, 404), "MARKETS")
    y = para(d, (rx, y), "KOSPI plunges 6.2% as AI fears hit Asia",
             serif_b(27), 344, leading=31)
    y = para(d, (rx, y + 4),
             "Seoul's benchmark fell 6.16% and the Nikkei 2.78% in a "
             "sharp sell-off in chip stocks.",
             sans(19), 344, leading=24)

    # ---- middle row: Gaza / Colombia / Pacific
    d.line([(40, 580), (984, 580)], fill=INK, width=3)
    cols = [
        (40, "GAZA", "Israeli strike kills Hamas security chief",
         "Abuelouf, Hamas's security chief, was killed with his wife "
         "and children, Gaza medics said.",
         icon_city),
        (368, "COLOMBIA", "All hostages freed in Cartagena siege",
         "Security forces stormed a supermarket after a 17-hour siege, "
         "freeing every hostage. One captor was killed.",
         icon_people),
        (696, "PACIFIC", "Australia signs base ban with Solomons",
         "A treaty signed in Canberra would bar any foreign military or "
         "security base on the Solomon Islands.",
         icon_flags),
    ]
    for cx, kick, head, body, icon in cols:
        y = kicker(d, (cx, 596), kick)
        y = para(d, (cx, y), head, serif_b(24), 272, leading=28)
        y = para(d, (cx, y + 4), body, sans(18), 272, leading=23)

    # ---- bottom row: Ras Tanura / Odesa / Climate
    d.line([(40, 812), (984, 812)], fill=LIGHT_LINE, width=2)
    bottom = [
        (40, "SAUDI ARABIA", "Houthis say they hit Ras Tanura refinery",
         "Yemen's Houthis said they hit the refinery; fires reported. [CLAIM]"),
        (368, "UKRAINE", "Russian strike kills two in Odesa",
         "A night strike killed two and injured three, the governor said."),
        (696, "CLIMATE", "COP31 talks end with no deal",
         "The UN climate talks failed to reach a deal; the Pope voiced concern."),
    ]
    for cx, kick, head, body in bottom:
        y = kicker(d, (cx, 828), kick)
        y = para(d, (cx, y), head, serif_b(22), 272, leading=26)
        y = para(d, (cx, y + 4), body, sans(17), 272, leading=22)

    # ---- footer
    d.text((512, 972),
           "Sources dated 25 Nov 2026: Just Security, Reuters, Yonhap, Dawn, Al Jazeera, AP. [CLAIM] = one party's claim.",
           font=sans(14), fill=GREY, anchor="ma")

    img.save(path, format="PNG", optimize=True)
    return path


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.png")
    build_page(out)
    print("wrote", out, os.path.getsize(out), "bytes")
