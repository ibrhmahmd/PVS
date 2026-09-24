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
ACTIVE_TOKENS = ["text-secondary", "bg-surface-container-high", "shadow-[2px_2px_0_0_#4cd7f6]"]


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []  # (tag, attrs dict)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

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
            cls = a.get("class", "")
            missing = [c for c in ACTIVE_TOKENS if c not in cls.split()]
            if missing:
                err(page, f"active link {dp} missing classes {missing}")
    if not active or set(active) != {slug}:
        err(page, f"aria-current links {active}, expected only {slug!r}")
    # mobile menu present
    if not re.search(r'aria-controls="[^"]+"', src) or "aria-expanded" not in src:
        err(page, "no mobile menu toggle with aria-controls/aria-expanded")
    if 'id="newsletter"' not in src:
        err(page, 'footer has no id="newsletter"')

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
