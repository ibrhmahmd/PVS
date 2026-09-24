#!/usr/bin/env python3
"""Acceptance checker for issue #1. Run from the site root: python3 check_site.py"""
import os
import re
import sys
from html.parser import HTMLParser

PAGES = {
    "index.html": "home",
    "games.html": "games",
    "heros-journey.html": "heros-journey",
    "studio-lore.html": "studio-lore",
}
EXPECTED_HREF = {
    "home": "index.html",
    "games": "games.html",
    "heros-journey": "heros-journey.html",
    "studio-lore": "studio-lore.html",
    "community": "#newsletter",
    "play-demo": "games.html",
}
SHARED_ASSETS = ["assets/css/site.css", "assets/js/tailwind.config.js", "assets/js/site.js"]
# Invented claims / removed components that must not come back (case-insensitive).
FORBIDDEN = [
    "barnaby", "jax thalas", "project dawn", "beyond the nebula", "claw of destiny", "steamworks",
    "steam deck", "wishlist", "nintendo", "4.9 / 5", "500k", "420k", "98.4", "8-bit on", "scanline",
    "reel-modal", "elena rostova", "sys.ready", "crab game", "comparison-container", "quest-signup-form",
    "elena vance", "kai chen", "mira soren", "leo marchetti", "both are free", "four people",
    "max-w-7xl", "tailwind-config",
]
CRAB_CHAPTERS = ["Kitchen Escape", "Beach Run", "Sea Floor Dodging", "Shrimp Help", "Predator Chase", "Home Sweet Home"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []  # (tag, attrs dict)
        self.text = []  # visible text chunks
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))
        if tag in ("script", "style"):
            self._skip += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip and data.strip():
            self.text.append(data.strip())

    handle_startendtag = handle_starttag


errors = []


def err(page, msg):
    errors.append(f"{page}: {msg}")


def is_local(url):
    return url and not re.match(r"^(https?:|mailto:|tel:|data:|#|javascript:)", url)


titles = set()
for page, slug in PAGES.items():
    if not os.path.isfile(page):
        err(page, "missing")
        continue
    src = open(page, encoding="utf-8").read()
    p = Collector()
    p.feed(src)
    ids = {a.get("id") for _, a in p.tags if a.get("id")}

    if "googleusercontent" in src:
        err(page, "still references googleusercontent")
    font_links = [a for t, a in p.tags if t == "link" and "fonts.googleapis.com/css" in (a.get("href") or "")]
    if len(font_links) != 1:
        err(page, f"expected 1 Google Fonts stylesheet link, found {len(font_links)}")

    m = re.search(r"<title>([^<]+)</title>", src)
    if not m:
        err(page, "no <title>")
    elif m.group(1) in titles:
        err(page, f"duplicate title {m.group(1)!r}")
    else:
        titles.add(m.group(1))
    if not any(t == "meta" and a.get("name") == "description" and a.get("content") for t, a in p.tags):
        err(page, "no meta description")
    if not any(t == "link" and "icon" in (a.get("rel") or "") for t, a in p.tags):
        err(page, "no favicon link")

    # local refs resolve, in-page anchors resolve
    for t, a in p.tags:
        for attr in ("src", "href"):
            v = a.get(attr)
            if not v:
                continue
            if is_local(v):
                path = v.split("#")[0].split("?")[0]
                if path and not os.path.exists(path):
                    err(page, f"<{t} {attr}={v!r}> does not exist")
                frag = v.split("#", 1)[1] if "#" in v else None
                if frag and path in PAGES:
                    target = open(path, encoding="utf-8").read()
                    if f'id="{frag}"' not in target:
                        err(page, f"{v!r}: #{frag} not found in {path}")
            elif v.startswith("#") and len(v) > 1 and v[1:] not in ids:
                err(page, f"anchor {v!r} has no matching id")

    # nav: every data-path link resolves; exactly the right one is active
    nav_links = [a for t, a in p.tags if t == "a" and a.get("data-path")]
    if not nav_links:
        err(page, "no data-path nav links found")
    active = []
    for a in nav_links:
        dp, href = a["data-path"], a.get("href")
        if dp in EXPECTED_HREF and href != EXPECTED_HREF[dp]:
            err(page, f"data-path={dp} href={href!r}, expected {EXPECTED_HREF[dp]!r}")
        if a.get("aria-current") == "page":
            active.append(dp)
    if not active or set(active) != {slug}:
        err(page, f"aria-current links {active}, expected only {slug!r}")
    # mobile menu present
    if not re.search(r'aria-controls="[^"]+"', src) or "aria-expanded" not in src:
        err(page, "no mobile menu toggle with aria-controls/aria-expanded")
    if 'id="newsletter"' not in src:
        err(page, 'footer has no id="newsletter"')

    # shared assets linked, no inline copies
    for asset in SHARED_ASSETS:
        if asset not in src:
            err(page, f"does not reference {asset}")
    if re.search(r"<style[\s>]", src):
        err(page, "has an inline <style> block (move it to assets/css/site.css)")
    inline_js = [m for m in re.findall(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", src, re.S) if m.strip()]
    if inline_js:
        err(page, f"has {len(inline_js)} inline <script> block(s) (move to assets/js/)")
    low = src.lower()
    for bad in FORBIDDEN:
        if bad in low:
            err(page, f"contains forbidden {bad!r}")
    labels = [t for t in p.text if " // " in t]
    if labels:
        err(page, f"decorative '//' labels remain: {labels[:3]}")

# JS files: refs resolve, no forbidden content
js_files = [os.path.join("assets/js", f) for f in os.listdir("assets/js")] if os.path.isdir("assets/js") else []
for js in js_files:
    body = open(js, encoding="utf-8").read()
    for ref in re.findall(r"""['"](assets/[^'"]+)['"]""", body):
        if not os.path.exists(ref):
            errors.append(f"{js}: {ref!r} does not exist")
    for bad in FORBIDDEN[:-2]:
        if bad in body.lower():
            errors.append(f"{js}: contains forbidden {bad!r}")

# real game content present
games = open("games.html", encoding="utf-8").read() if os.path.isfile("games.html") else ""
journey_js = open("heros-journey.html", encoding="utf-8").read() if os.path.isfile("heros-journey.html") else ""
if os.path.exists("assets/js/heros-journey.js"):
    errors.append("assets/js/heros-journey.js should be deleted (Story Spine page is static)")
for phrase in ("Once upon a time", "One day", "Because of that", "Until finally", "And ever since then"):
    if phrase.lower() not in journey_js.lower():
        errors.append(f"heros-journey.html: missing Story Spine phrase {phrase!r}")
for gone in ("game-btn-", "stage-buttons", "stage-prev", "planet-panel", "<svg", "?game="):
    if gone in journey_js:
        errors.append(f"heros-journey.html: removed component still present ({gone!r})")
for anchor in ("crab-quest", "space-x"):
    if f'id="{anchor}"' not in journey_js:
        errors.append(f'heros-journey.html: missing section id="{anchor}"')
# games page uses the same Story Spine beats as the journey page
games_low = games.lower()
for stale in ("call to adventure", "crossing the threshold", "meeting the mentor", "return with the elixir", "the game loop", "real planet facts"):
    if stale in games_low:
        errors.append(f"games.html: stale label {stale!r} (use the Story Spine beats)")
for phrase in ("one day", "because of that", "until finally", "and ever since then"):
    if phrase not in games_low:
        errors.append(f"games.html: missing Story Spine phrase {phrase!r}")
# every screenshot is click-to-enlarge
for page in PAGES:
    if os.path.isfile(page):
        for tag in re.findall(r"<img\b[^>]*assets/img/[^\"]*/screens/[^>]*>", open(page, encoding="utf-8").read()):
            if "data-lightbox" not in tag:
                errors.append(f"{page}: screenshot without data-lightbox: {tag[:90]}")
if "data-lightbox" not in (open("assets/js/site.js", encoding="utf-8").read() if os.path.isfile("assets/js/site.js") else ""):
    errors.append("assets/js/site.js: no lightbox handling for [data-lightbox]")
for anchor in ("crab-quest", "space-x"):
    if f'id="{anchor}"' not in games:
        errors.append(f'games.html: missing id="{anchor}"')
for chapter in CRAB_CHAPTERS:
    if chapter not in games:
        errors.append(f"games.html: missing Crab Quest chapter {chapter!r}")
    if chapter not in journey_js:
        errors.append(f"heros-journey.html: missing Crab Quest chapter {chapter!r}")
for planet in ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"):
    if planet not in journey_js and planet not in games:
        errors.append(f"Space X planet {planet} not presented anywhere")

# real team + real screenshots in use; user media archived, not served
lore = open("studio-lore.html", encoding="utf-8").read() if os.path.isfile("studio-lore.html") else ""
for name in ("Mariam", "Salah", "Sleem"):
    if name not in lore:
        errors.append(f"studio-lore.html: team member {name} missing")
for shot in ["assets/img/crab-quest/screens/start.jpg"] + [f"assets/img/crab-quest/screens/chapter-{i}.jpg" for i in range(1, 7)] + ["assets/img/space-x/screens/gameplay.jpg"]:
    if not os.path.isfile(shot):
        errors.append(f"missing screenshot {shot}")
for stray in ("assets/game-screens", "assets/team"):
    if os.path.exists(stray):
        errors.append(f"{stray} should be moved to design/source-media/")

# every image in assets/img is referenced somewhere
corpus = "".join(open(f, encoding="utf-8").read() for f in list(PAGES) + js_files + ["assets/css/site.css"] if os.path.isfile(f))
for root, _, files in os.walk("assets/img"):
    for f in files:
        path = os.path.join(root, f)
        if path not in corpus:
            errors.append(f"unreferenced image {path} (delete it)")

# no leftover stitch dirs at root
for d in os.listdir("."):
    if d.startswith("pixel_verse_studios_") or d in ("bauhaus", "neo_arcade_narrative") or d.startswith("charming_16_bit"):
        errors.append(f"leftover Stitch dir at root: {d}")
if os.path.isdir("assets/img"):
    imgs = os.listdir("assets/img")
    if not imgs:
        errors.append("assets/img is empty")
else:
    errors.append("assets/img missing")

if errors:
    print("FAIL")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print(f"OK: {len(PAGES)} pages pass all checks")
