#!/usr/bin/env python3
"""Builds every PDF/PNG/PPTX in docs/ from the sources next to this file.

    python3 docs/build.py [documentation|poster|slides|all]

Needs: google-chrome, pdftoppm, and `pip install markdown qrcode python-pptx pillow`.
The QR code points at SITE_URL (the only thing to change when the real address is known).
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

import markdown
import qrcode
import qrcode.image.svg

DOCS = Path(__file__).resolve().parent
SITE_URL = "https://pixelversestudios.itch.io/"   # TODO: replace with the studio website address
CHROME = shutil.which("google-chrome") or shutil.which("chromium")


def chrome_pdf(html: Path, pdf: Path):
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
         "--virtual-time-budget=15000", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf}", html.as_uri()],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def make_qr():
    out = DOCS / "assets" / "brand" / "qr-site.svg"
    img = qrcode.make(SITE_URL, image_factory=qrcode.image.svg.SvgPathImage, box_size=10, border=1)
    img.save(str(out))
    qrcode.make(SITE_URL, box_size=12, border=1).save(str(DOCS / "assets" / "brand" / "qr-site.png"))   # for the slides
    return out


def build_documentation():
    src = DOCS / "documentation"
    body = markdown.markdown((src / "pvs-documentation.md").read_text(encoding="utf-8"),
                             extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
    body = re.sub(r"<h2>(.*?)</h2>", r'<h2 class="sec">\1</h2>', body)
    team = "".join(
        f'<figure><img src="../assets/team/{f}.jpg"><figcaption>{n}</figcaption></figure>'
        for f, n in [("mariam", "Mariam Alaa"), ("selim", "Selim Loai"), ("mohamed", "Mohamed Loai"),
                     ("medhat", "Medhat Ali"), ("salah", "Salah Mohamed")])
    cover = f"""
<section class="cover">
  <img class="mark" src="../assets/brand/logo.png">
  <p class="kicker">AFFIAT · Afro-Asian Forum for Innovation and Technology · Aswan Finals 2026 · Games</p>
  <img class="partners" src="../assets/brand/partners.png" alt="AFFIAT and Techno Future Kafr El Sheikh" style="display: block; height: 26mm; width: auto; margin: 5mm 0; background: #fff; padding: 2.5mm 4mm; border-radius: 3mm;">
  <h1>Pixel Verse Studios</h1>
  <p class="tag">Game Technical Documentation</p>
  <p class="lead">Crab Quest and Space X: Journey to Jupiter. Two 16-bit games that teach real science.</p>
  <div class="team">{team}</div>
</section>"""
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Pixel Verse Studios: Documentation</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="doc.css"></head><body>{cover}<main>{body}</main></body></html>"""
    page = src / "pvs-documentation.html"
    page.write_text(html, encoding="utf-8")
    chrome_pdf(page, src / "pvs-documentation.pdf")
    print("documentation ->", src / "pvs-documentation.pdf")


def build_poster():
    make_qr()
    src = DOCS / "poster"
    chrome_pdf(src / "poster.html", src / "pvs-poster-1000x2000mm.pdf")
    # A small preview, like the reference poster has.
    subprocess.run(["pdftoppm", "-png", "-singlefile", "-scale-to-x", "1900", "-scale-to-y", "-1",
                    str(src / "pvs-poster-1000x2000mm.pdf"), str(src / "preview")], check=True)
    print("poster ->", src / "pvs-poster-1000x2000mm.pdf")


def build_slides():
    src = DOCS / "presentation"
    make_qr()
    subprocess.run([sys.executable, str(src / "deck.py")], check=True)      # writes slides.html and the .pptx
    chrome_pdf(src / "slides.html", src / "pvs-presentation.pdf")
    print("slides ->", src)


if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("documentation", "all"):
        build_documentation()
    if what in ("poster", "all"):
        build_poster()
    if what in ("slides", "all"):
        build_slides()
