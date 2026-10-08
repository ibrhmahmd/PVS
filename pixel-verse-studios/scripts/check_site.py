#!/usr/bin/env python3
"""Checks the site for mistakes. Run it from the site folder: python3 scripts/check_site.py"""
import os
import re
import sys

# Each page and the nav link (data-path) that should be marked as the current page.
PAGES = {
    "index.html": "home",
    "games.html": "games",
    "heros-journey.html": "heros-journey",
    "studio-lore.html": "studio-lore",
}

# Where each nav link (data-path) must point.
NAV_TARGETS = {
    "home": "index.html",
    "games": "games.html",
    "heros-journey": "heros-journey.html",
    "studio-lore": "studio-lore.html",
    "play-demo": "games.html",
}

# These game facts are real. They must stay on the pages.
CRAB_CHAPTERS = ["Kitchen Escape", "Beach Run", "Sea Floor Dodging", "Shrimp Help", "Predator Chase", "Home Sweet Home"]
PLANETS = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
STORY_SPINE = ["Once upon a time", "One day", "Because of that", "Until finally", "And ever since then"]

# Made-up things that must never come back.
INVENTED = ["claw of destiny", "steam deck", "wishlist", "project dawn", "beyond the nebula"]

# Things from the old Tailwind setup that must stay gone.
OLD_STUFF = ["tailwind", "max-w-7xl", "googleusercontent"]

problems = []


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def complain(where, message):
    problems.append(where + ": " + message)


titles = []
for page, current in PAGES.items():
    if not os.path.isfile(page):
        complain(page, "file is missing")
        continue
    html = read(page)

    # Title and description
    found = re.search(r"<title>([^<]+)</title>", html)
    if not found:
        complain(page, "no <title>")
    elif found.group(1) in titles:
        complain(page, "same <title> as another page")
    else:
        titles.append(found.group(1))
    if 'name="description"' not in html:
        complain(page, "no meta description")

    # The three shared files
    for shared in ["assets/css/styles.css", "assets/js/site.js"]:
        if shared not in html:
            complain(page, "does not use " + shared)
    if "<style" in html:
        complain(page, "has a <style> block (put it in assets/css/styles.css)")
    if re.search(r"<script(?![^>]*src=)", html):
        complain(page, "has an inline <script> (put it in assets/js/site.js)")

    # Every local file or page that is linked must exist
    for link in re.findall(r'(?:src|href)="([^"]+)"', html):
        if link.startswith(("http", "#", "mailto:")):
            continue
        path = link.split("#")[0]
        if path and not os.path.exists(path):
            complain(page, link + " does not exist")
        if "#" in link and path in PAGES:
            anchor = link.split("#")[1]
            if 'id="' + anchor + '"' not in read(path):
                complain(page, link + ": no element with id " + anchor)

    # Nav links point to the right pages, and only this page is marked as current
    marked = []
    for tag in re.findall(r"<a [^>]*data-path=[^>]*>", html):
        slug = re.search(r'data-path="([^"]+)"', tag).group(1)
        href = re.search(r'href="([^"]+)"', tag).group(1)
        if NAV_TARGETS.get(slug) != href:
            complain(page, "nav link " + slug + " points to " + href)
        if 'aria-current="page"' in tag:
            marked.append(slug)
    if marked != [current]:
        complain(page, "pages marked as current: " + str(marked) + ", expected only " + current)

    # Every screenshot can be enlarged
    for tag in re.findall(r"<img[^>]*/screens/[^>]*>", html):
        if "data-lightbox" not in tag:
            complain(page, "screenshot without data-lightbox: " + tag[:80])

    # Things that must stay gone
    lower = html.lower()
    for bad in INVENTED + OLD_STUFF:
        if bad in lower:
            complain(page, "contains " + repr(bad))

# Real game content is on the pages
games = read("games.html") if os.path.isfile("games.html") else ""
journey = read("heros-journey.html") if os.path.isfile("heros-journey.html") else ""
for chapter in CRAB_CHAPTERS:
    if chapter not in games or chapter not in journey:
        complain("games/heros-journey", "Crab Quest chapter missing: " + chapter)
for planet in PLANETS:
    if planet not in games:
        complain("games.html", "planet missing: " + planet)
for phrase in STORY_SPINE:
    if phrase.lower() not in journey.lower():
        complain("heros-journey.html", "Story Spine phrase missing: " + phrase)
for page_text, name in [(games, "games.html"), (journey, "heros-journey.html")]:
    for section in ["crab-quest", "space-x"]:
        if 'id="' + section + '"' not in page_text:
            complain(name, "no section with id " + section)

# Every picture in assets/img is used by some page, and the old build files are gone
all_pages = "".join(read(p) for p in PAGES if os.path.isfile(p))
for folder, _, files in os.walk("assets/img"):
    for name in files:
        path = os.path.join(folder, name)
        if path not in all_pages:
            complain(path, "picture is not used by any page (delete it)")
for old in ["tailwind.config.js", "assets/css/tailwind.css", "assets/css/site.css", "assets/js/studio-lore.js", "bin"]:
    if os.path.exists(old):
        complain(old, "old file should be deleted")

if problems:
    print("PROBLEMS FOUND")
    for problem in problems:
        print("  -", problem)
    sys.exit(1)
print("OK: all " + str(len(PAGES)) + " pages pass")
