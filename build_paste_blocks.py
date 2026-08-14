#!/usr/bin/env python3
"""Build per-section Squarespace Code Block paste files from a page.

Each output block is self-contained: minified uag.css in a <style> tag, the
section markup wrapped in <div class="uag-page">, and every image resized to
its rendered width and embedded as a base64 webp data URI. Internal page
links are rewritten to the planned Squarespace slugs.

Usage: python3 build_paste_blocks.py index.html
Writes: paste/<page>/<nn>-<name>.html  (plus a SIZES report on stdout)
"""
import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image

HERE = Path(__file__).parent
LINK_MAP = {
    "buying.html": "/buying",
    "why-sell-with-uag.html": "/why-sell-with-uag",
    "sell-with-us.html": "/sell-with-us",
    "asset-disposal.html": "/asset-disposal",
}
# Max pixel width per image, chosen from the rendered column width (~2x for
# sharp screens). Anything not listed uses 900.
WIDTHS = {
    "img/cat-plant.webp": 700, "img/cat-commercial.webp": 700,
    "img/cat-vans.webp": 700, "img/cat-agri.webp": 700,
    "img/cat-catering.webp": 700, "img/cat-insolvency.webp": 700,
    "img/cat-workshop.webp": 700, "img/cat-mixed.webp": 700,
}
QUALITY = 65


def data_uri(src: str) -> str:
    path = HERE / src
    img = Image.open(path)
    max_w = WIDTHS.get(src, 900)
    if img.width > max_w:
        img = img.resize((max_w, round(img.height * max_w / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "WEBP", quality=QUALITY, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def minify_css(css: str) -> str:
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    css = re.sub(r"\s+", " ", css)
    css = re.sub(r" ?([{};:,>]) ?", r"\1", css)
    return css.strip()


def main(page_file: str) -> None:
    html = (HERE / page_file).read_text()
    css = minify_css((HERE / "uag.css").read_text())
    out_dir = HERE / "paste" / Path(page_file).stem
    out_dir.mkdir(parents=True, exist_ok=True)

    # Split on the banner comments: <!-- ===== 1. NAME ===== -->; pages without
    # banners fall back to plain <section> extraction, named by section id.
    parts = re.split(r"<!-- =+ ([\w .,]+?) =+ -->", html)
    blocks = []  # (name, markup)
    for i in range(1, len(parts) - 1, 2):
        name = parts[i].strip().rstrip(".")
        body = parts[i + 1]
        m = re.search(r"<section.*?</section>", body, flags=re.S)
        if m:
            blocks.append((name, m.group(0)))
    if not blocks:
        for m in re.finditer(r"<section.*?</section>", html, flags=re.S):
            sec = m.group(0)
            mid = re.search(r'id="([\w-]+)"', sec)
            blocks.append((mid.group(1) if mid else "section", sec))

    report = []
    for n, (name, markup) in enumerate(blocks, 1):
        for rel, slug in LINK_MAP.items():
            markup = markup.replace(f'href="{rel}', f'href="{slug}')
        markup = re.sub(
            r'src="(img/[^"]+)"',
            lambda m: f'src="{data_uri(m.group(1))}"',
            markup,
        )
        slug_name = re.sub(r"[^a-z]+", "-", name.lower()).strip("-")
        out = (
            f"<!-- UAG page block {n}: {name}. One Squarespace Code Block, "
            f"Mode HTML, Display Source OFF. -->\n"
            f"<style>{css}</style>\n"
            f'<div class="uag-page">\n{markup}\n</div>'
        )
        f = out_dir / f"{n:02d}-{slug_name}.html"
        f.write_text(out)
        report.append((f.name, len(out)))

    for fname, size in report:
        print(f"{size/1024:7.0f} KB  {fname}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "index.html")
