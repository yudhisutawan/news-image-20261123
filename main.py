#!/usr/bin/env python3
"""The World Today — front page for Monday 23 November 2026.

A one-page newspaper front page, 1024x1024, built with Pillow only.
48 stories: 2 leads, 1 banner, 15 tiles, 30 briefs.
Run:  python3 main.py   -> writes entry.png next to this file.
"""

import os

from PIL import Image, ImageDraw, ImageFont

PAGE = 1024
MARGIN = 28
PAPER = (247, 243, 234)
INK = (22, 28, 44)
NAVY = (27, 42, 74)
NAVY_DARK = (18, 30, 56)
RED = (178, 28, 28)
GREY = (96, 96, 92)
RULE = (180, 172, 156)
BLUE = (38, 84, 138)
GREEN = (34, 110, 72)
AMBER = (166, 110, 16)
PURPLE = (104, 64, 140)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    """Load a DejaVu face; fall back to Pillow's default bitmap font."""
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except OSError:
        return ImageFont.load_default()


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)

CAT_COLORS = {
    "W": RED,
    "B": BLUE,
    "T": PURPLE,
    "SC": GREEN,
    "S": AMBER,
    "C": (150, 60, 110),
}

LEADS = [
    {
        "kicker": "CLIMATE SUMMIT",
        "headline": "COP31 talks collapse as fossil-fuel phase-out dropped from draft",
        "body": (
            "Negotiators in Belem walked out of the final plenary after the "
            "chair removed any mention of phasing out oil, gas and coal from "
            "the summit text. Small island states called the draft a betrayal, "
            "while major producers said the language was never agreed. Talks "
            "will resume in Bonn in March, but delegates warned the 1.5C goal "
            "is now out of reach without faster cuts this decade."
        ),
        "chart": "bars",
        "chart_title": "Pledges vs the 1.5C pathway (Gt CO2e, 2030)",
    },
    {
        "kicker": "ENERGY",
        "headline": "Tanker seized near Hormuz; oil jumps $4 in a day",
        "body": (
            "A crude carrier was boarded by armed speedboats in the Strait of "
            "Hormuz early on Sunday, sending Brent crude up more than $4 to "
            "above $82 a barrel. Insurers raised war-risk premiums for Gulf "
            "transits and several shipping lines rerouted around the Cape of "
            "Good Hope. Governments urged restraint, warning that a prolonged "
            "closure would push petrol prices sharply higher worldwide."
        ),
        "chart": "line",
        "chart_title": "Brent crude, $ per barrel (last 10 days)",
    },
]

BANNER = {
    "kicker": "DEFENCE",
    "headline": "NATO approves 300,000-strong rapid-reaction force after Baltic exercise",
    "sub": (
        "Alliance ministers sign off the biggest readiness overhaul since the "
        "Cold War; new units on high alert from January."
    ),
}

TILES = [
    ("W", "EU leaders agree 50bn euro Ukraine aid package after late-night summit",
     "Funds to be released in tranches tied to reform milestones."),
    ("B", "Markets rally as Fed signals December rate cut is on the table",
     "Stocks hit a record high; the dollar slips against the euro."),
    ("T", "Chipmaker unveils 2nm AI processor, claims 40% efficiency gain",
     "First devices using the chip are expected next autumn."),
    ("SC", "Astronomers spot Earth-sized planet in a nearby star's habitable zone",
     "The world orbits a red dwarf just 11 light-years away."),
    ("S", "Title race tightens as leaders draw in derby thriller",
     "A late equaliser leaves two points between the top three."),
    ("C", "Blockbuster sequel breaks opening-weekend box office record",
     "Biggest crowds since before the pandemic."),
    ("W", "Sudan ceasefire talks resume in Jeddah after month-long pause",
     "Mediators hope for a humanitarian corridor within days."),
    ("B", "Oil steadies near $78 as traders weigh Hormuz disruption risk",
     "Analysts say stockpiles should cushion a short stoppage."),
    ("T", "Regulators probe social platform over teen safety failures",
     "Watchdog demands data on how harmful content is ranked."),
    ("SC", "Antarctic ice shelf calving tracked by new satellite array",
     "The berg, twice the size of London, is drifting north."),
    ("S", "Sprinter breaks 100m season best at Diamond League finale",
     "The 22-year-old clocked 9.81 seconds into a headwind."),
    ("C", "Museum unveils restored Renaissance masterpiece after a decade",
     "Conservators removed centuries of varnish and overpaint."),
    ("W", "Japan unveils stimulus plan to shield households from price rises",
     "Cash handouts and energy subsidies lead the package."),
    ("B", "Electric car sales pass petrol for first time in October",
     "One in three new cars sold was fully electric."),
    ("T", "Quantum computer solves logistics problem in minutes, team says",
     "Researchers say the result still needs independent checks."),
]

BRIEFS = [
    "UN chief calls for emergency Security Council session on Hormuz.",
    "UK inflation eases to 3.1% as food prices fall for a second month.",
    "Space agency confirms crewed Moon flyby still on track for 2027.",
    "World Cup hosts unveil final stadium with 18 months to spare.",
    "Striking dockworkers reach deal after three weeks of disruption.",
    "Heatwave grips southern Europe as November records tumble.",
    "Central bank holds rates, hints at cuts early next year.",
    "Rare snow leopard filmed with cubs in the Himalayas.",
    "Film festival winner to open in cinemas worldwide in January.",
    "Cyber-attack hits hospital network; patient care unaffected.",
    "New high-speed rail line cuts capital journey to 47 minutes.",
    "Drought emergency declared in three East African states.",
    "Tech giant fined 900m euros over app store rules.",
    "Tennis world No. 1 withdraws from season finale with injury.",
    "Pope calls for ceasefire in Christmas message preview.",
    "Record 40,000 runners complete city marathon in the rain.",
    "Scientists grow mini-livers in lab in transplant breakthrough.",
    "Airline orders 60 new jets in biggest deal of the year.",
    "Opera house reopens after two-year restoration project.",
    "Gold hits record high as investors seek safe havens.",
    "Volcano eruption forces evacuation of 2,000 islanders.",
    "Chess prodigy, 16, beats world champion in rapid match.",
    "New malaria vaccine rolls out to 12 more countries.",
    "Fashion week opens with tribute to late design legend.",
    "Flood defences tested as river levels rise after storms.",
    "Study links short sleep to faster memory decline in old age.",
    "Historic treaty on ocean protection ratified by 60 nations.",
    "Football club sacks manager after five straight defeats.",
    "Solar power now cheapest source of new electricity in 90% of world.",
    "Novel wins year's biggest literary prize in surprise upset.",
]


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines that fit `width`."""
    lines, current = [], ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def para(draw, x, y, text, fnt, width, fill=INK, leading=None, max_lines=None):
    """Draw wrapped text; returns the y just below the last line."""
    leading = leading or int(fnt.size * 1.35)
    lines = wrap(draw, text, fnt, width)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_bars(draw, x, y, w, h):
    """Mini bar chart: pledges vs the 1.5C pathway."""
    vals = [("2024", 52), ("2026", 50), ("2030 pledge", 42), ("2030 1.5C", 28)]
    top, bottom = y + 6, y + h - 16
    vmax = 60.0
    slot = w // len(vals)
    for i, (label, v) in enumerate(vals):
        bh = int((bottom - top) * v / vmax)
        bx = x + i * slot + 14
        bw = slot - 28
        color = RED if "1.5C" in label else NAVY
        draw.rectangle([bx, bottom - bh, bx + bw, bottom], fill=color)
        # value inside the bar (white) so it never collides with the title
        draw.text((bx + bw // 2, bottom - bh + 2), str(v),
                  font=SANS_B(10), fill=(255, 255, 255), anchor="ma")
        draw.text((bx + bw // 2, bottom + 3), label,
                  font=SANS(9), fill=GREY, anchor="ma")


def draw_line(draw, x, y, w, h):
    """Mini line chart: Brent crude over the last ten days."""
    prices = [74, 75, 74, 76, 75, 77, 78, 78, 80, 82]
    top, bottom = y + 10, y + h - 16
    lo, hi = 72.0, 84.0
    pts = []
    for i, p in enumerate(prices):
        px = x + 12 + i * (w - 24) // (len(prices) - 1)
        py = bottom - (p - lo) / (hi - lo) * (bottom - top)
        pts.append((px, py))
    draw.rectangle([x, y, x + w, y + h], outline=RULE, width=1)
    for gy in (74, 78, 82):
        gyy = bottom - (gy - lo) / (hi - lo) * (bottom - top)
        draw.line([(x + 4, gyy), (x + w - 4, gyy)], fill=(225, 220, 208), width=1)
        draw.text((x + 6, gyy - 11), f"${gy}", font=SANS(8), fill=GREY)
    draw.line(pts, fill=RED, width=2)
    for px, py in pts:
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)
    draw.text((x + w - 4, y + 2), "$82", font=SANS_B(11), fill=RED, anchor="ra")


def build_page():
    img = Image.new("RGB", (PAGE, PAGE), PAPER)
    d = ImageDraw.Draw(img)
    x0, x1 = MARGIN, PAGE - MARGIN
    width = x1 - x0

    # ---- Masthead -------------------------------------------------------
    d.text((x0, 14), "THE WORLD TODAY", font=SERIF_B(46), fill=NAVY)
    d.text((x1, 22), "MONDAY 23 NOVEMBER 2026", font=SANS_B(15), fill=INK, anchor="ra")
    d.text((x1, 44), "ONE PAGE  ·  48 STORIES", font=SANS(11), fill=GREY, anchor="ra")
    d.line([(x0, 78), (x1, 78)], fill=RED, width=3)
    d.line([(x0, 83), (x1, 83)], fill=RULE, width=1)

    # ---- Strapline ------------------------------------------------------
    strap = "THE WORLD IN ONE PAGE  ·  48 STORIES  ·  WORLD  ·  BUSINESS  ·  TECH  ·  SCIENCE  ·  SPORT  ·  CULTURE"
    d.text((PAGE // 2, 92), strap, font=SANS_B(12), fill=NAVY, anchor="ma")
    d.line([(x0, 110), (x1, 110)], fill=RULE, width=1)

    # ---- Two leads ------------------------------------------------------
    col_w = (width - 16) // 2
    lead_top, lead_h = 118, 210
    for i, lead in enumerate(LEADS):
        lx = x0 + i * (col_w + 16)
        d.text((lx, lead_top), lead["kicker"], font=SANS_B(11), fill=RED)
        y = lead_top + 17
        y = para(d, lx, y, lead["headline"], SANS_B(18), col_w, NAVY, 23)
        y = para(d, lx, y + 4, lead["body"], SANS(11), col_w, INK, 14, max_lines=5)
        chart_y = lead_top + lead_h - 52
        d.text((lx, chart_y - 13), lead["chart_title"], font=SANS_B(10), fill=GREY)
        if lead["chart"] == "bars":
            draw_bars(d, lx, chart_y, col_w, 50)
        else:
            draw_line(d, lx, chart_y, col_w, 50)
        d.line([(lx, lead_top + lead_h), (lx + col_w, lead_top + lead_h)],
               fill=RULE, width=1)
    d.line([(x0 + col_w + 8, lead_top), (x0 + col_w + 8, lead_top + lead_h)],
           fill=RULE, width=1)

    # ---- Banner ---------------------------------------------------------
    by = lead_top + lead_h + 8
    d.rectangle([x0, by, x1, by + 54], fill=NAVY_DARK)
    d.text((x0 + 14, by + 6), BANNER["kicker"], font=SANS_B(11), fill=(240, 200, 90))
    d.text((x0 + 14, by + 20), BANNER["headline"], font=SANS_B(15), fill=(255, 255, 255))
    d.text((x0 + 14, by + 39), BANNER["sub"], font=SANS(11), fill=(200, 208, 224))

    # ---- Tile grid: 3 x 5 ----------------------------------------------
    ty = by + 54 + 10
    gap = 8
    tile_w = (width - 2 * gap) // 3
    tile_h = 62
    for idx, (cat, head, sub) in enumerate(TILES):
        row, col = divmod(idx, 3)
        tx = x0 + col * (tile_w + gap)
        tyy = ty + row * (tile_h + gap)
        d.rectangle([tx, tyy, tx + tile_w, tyy + tile_h], outline=RULE, width=1)
        badge = CAT_COLORS[cat]
        d.rectangle([tx + 6, tyy + 6, tx + 30, tyy + 22], fill=badge)
        d.text((tx + 18, tyy + 14), cat, font=SANS_B(10), fill=(255, 255, 255), anchor="mm")
        para(d, tx + 36, tyy + 5, head, SANS_B(11), tile_w - 42, NAVY, 14, max_lines=2)
        para(d, tx + 6, tyy + 44, sub, SANS(10), tile_w - 12, GREY, 13, max_lines=1)

    # ---- In brief -------------------------------------------------------
    iy = ty + 5 * tile_h + 4 * gap + 8
    d.text((x0, iy), "IN BRIEF", font=SANS_B(13), fill=NAVY)
    d.line([(x0 + 78, iy + 8), (x1, iy + 8)], fill=RED, width=2)
    byy = iy + 20
    brief_col_w = (width - 16) // 2
    for i, item in enumerate(BRIEFS):
        col = i // 15
        row = i % 15
        bx = x0 + col * (brief_col_w + 16)
        yy = byy + row * 12.5
        d.text((bx, yy), "•  " + item, font=SANS(10), fill=INK)

    # ---- Footer ---------------------------------------------------------
    fy = byy + 15 * 12.5 + 6
    d.line([(x0, fy), (x1, fy)], fill=RULE, width=1)
    d.text((PAGE // 2, fy + 6),
           "THE WORLD TODAY — MONDAY 23 NOVEMBER 2026  ·  48 STORIES  ·  ALL TIMES AS REPORTED ON THE DAY",
           font=SANS(10), fill=GREY, anchor="ma")
    return img


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    page = build_page()
    page.save(os.path.join(here, "entry.png"))
    outdir = "/output"
    if os.path.isdir(outdir):
        page.save(os.path.join(outdir, "entry.png"))
    print("wrote entry.png (1024x1024, 48 stories)")


if __name__ == "__main__":
    main()
