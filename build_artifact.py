#!/usr/bin/env python3
"""Combine the three UAG pages into one self-contained artifact page.

Artifacts are single-page and the CSP blocks external hosts, so:
  - the three pages become three <div class="uag-doc"> sections switched by the nav
  - the shared stylesheet is inlined
  - every image becomes a data: URI
  - internal links (buying.html, selling.html#how) become switcher links
"""
import base64, re, pathlib

SRC = pathlib.Path("/Users/pauluncle/Desktop/Claude Projects/CLIENTS/UAG/pages/site")
OUT = pathlib.Path("/private/tmp/claude-501/-Users-pauluncle-Desktop-Claude-Projects/59ef649b-583b-4814-9308-cb1db8cc67c4/scratchpad/uag-preview.html")

PAGES = [("home", "index.html", "Home"),
         ("buying", "buying.html", "Buying"),
         ("selling", "selling.html", "Selling")]

# ---- images as data URIs ----
data_uris = {}
for img in sorted((SRC / "img").glob("*.webp")):
    b64 = base64.b64encode(img.read_bytes()).decode()
    data_uris[f"img/{img.name}"] = f"data:image/webp;base64,{b64}"
print(f"embedded {len(data_uris)} images, {sum(len(v) for v in data_uris.values())/1024/1024:.2f} MB of base64")

css = (SRC / "uag.css").read_text()

FILE_TO_KEY = {f: k for k, f, _ in PAGES}


def body_of(html: str) -> str:
    """Everything inside <div class="uag-page">, minus the review bar and nav."""
    m = re.search(r'<div class="uag-page">(.*)</div>\s*</body>', html, re.S)
    inner = m.group(1)
    inner = re.sub(r'<div class="uag-review">.*?</div>\s*</div>', '', inner, flags=re.S, count=1)
    inner = re.sub(r'<nav class="uag-nav".*?</nav>', '', inner, flags=re.S, count=1)
    return inner.strip()


def rewrite(inner: str) -> str:
    # images -> data URIs
    for k, v in data_uris.items():
        inner = inner.replace(f'src="{k}"', f'src="{v}"')
    # internal page links -> switcher links
    def link(m):
        href = m.group(1)
        file, _, anchor = href.partition('#')
        key = FILE_TO_KEY.get(file)
        if key is None:
            return m.group(0)
        extra = f' data-anchor="{anchor}"' if anchor else ''
        return f'href="#" data-goto="{key}"{extra}'
    inner = re.sub(r'href="((?:index|buying|selling)\.html(?:#[\w-]+)?)"', link, inner)
    # same-page anchors stay as anchors, they work inside the active section
    return inner


sections = []
for key, fname, _label in PAGES:
    inner = rewrite(body_of((SRC / fname).read_text()))
    sections.append(f'<div class="uag-doc" id="doc-{key}" data-doc="{key}">\n{inner}\n</div>')

CUR = ' aria-current="page"'
nav_links = "\n".join(
    '        <a href="#" data-goto="%s"%s>%s</a>' % (k, CUR if k == "home" else "", lab)
    for k, _f, lab in PAGES)

page = f'''<title>Universal Auctions Group: homepage, buying and selling pages</title>
<style>
/* The viewer's theme must not repaint the client's brand. This preview deliberately
   commits to UAG's own single visual world so it matches universalauctionsgroup.com
   exactly and can be pasted straight into Squarespace. */
:root, :root[data-theme="dark"], :root[data-theme="light"] {{ color-scheme: light; }}
html, body {{ margin: 0; padding: 0; background: #fafafa; }}
{css}

/* ---- preview shell, not part of any paste block ---- */
.uag-doc {{ display: none; }}
.uag-doc.is-on {{ display: block; }}
.uag-shell-bar {{
  background: #1c2126; color: #cfd6dc; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px; line-height: 1.5; padding: 12px clamp(20px,5vw,48px);
}}
.uag-shell-in {{ max-width: 1180px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 6px 18px; align-items: baseline; }}
.uag-shell-bar strong {{ color: #fff; font-weight: 600; }}
.uag-shell-tag {{ border: 1px solid #53a8c7; color: #8fd0e6; padding: 2px 8px; font-size: 11px; letter-spacing: .08em; text-transform: uppercase; }}
.uag-shell-nav {{ background: #000; padding: 0 clamp(20px,5vw,48px); position: sticky; top: 0; z-index: 20; }}
.uag-shell-nav-in {{ max-width: 1180px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 4px 26px; align-items: center; }}
.uag-shell-brand {{ color: #fafafa; font-size: 15px; letter-spacing: -.02em; padding: 16px 0; margin-right: auto; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }}
.uag-shell-nav a {{ color: #aeb7bf; text-decoration: none; font-size: 14px; padding: 16px 0; border-bottom: 2px solid transparent; font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; cursor: pointer; }}
.uag-shell-nav a:hover, .uag-shell-nav a:focus-visible {{ color: #fff; }}
.uag-shell-nav a[aria-current="page"] {{ color: #fff; border-bottom-color: #53a8c7; }}
.uag-shell-nav a:focus-visible {{ outline: 2px solid #53a8c7; outline-offset: 2px; }}
@media (max-width: 560px) {{ .uag-shell-brand {{ margin-right: 0; width: 100%; padding-bottom: 4px; }} }}
</style>

<div class="uag-shell-bar">
  <div class="uag-shell-in">
    <span class="uag-shell-tag">Client review build</span>
    <span><strong>Not live.</strong> Three pages: a homepage signpost, a page for buyers and a page for sellers. Use the tabs to move between them.</span>
    <span>Every fact is taken from UAG's own terms and conditions. Two yellow flags mark figures the terms state inconsistently.</span>
  </div>
</div>

<nav class="uag-shell-nav" aria-label="Pages">
  <div class="uag-shell-nav-in">
    <span class="uag-shell-brand">Universal Auctions Group</span>
{nav_links}
    <a href="https://bid.universalauctions.group" data-external="1">View latest stock</a>
  </div>
</nav>

<div class="uag-page">
{"".join(sections)}
</div>

<script>
(function () {{
  var docs = document.querySelectorAll('.uag-doc');
  var tabs = document.querySelectorAll('.uag-shell-nav a[data-goto]');
  function show(key, anchor) {{
    docs.forEach(function (d) {{ d.classList.toggle('is-on', d.dataset.doc === key); }});
    tabs.forEach(function (t) {{
      if (t.dataset.goto === key) {{ t.setAttribute('aria-current', 'page'); }}
      else {{ t.removeAttribute('aria-current'); }}
    }});
    var target = anchor && document.getElementById('doc-' + key).querySelector('#' + anchor);
    if (target) {{ target.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}
    else {{ window.scrollTo({{ top: 0, behavior: 'auto' }}); }}
  }}
  document.addEventListener('click', function (e) {{
    var a = e.target.closest('a');
    if (!a) return;
    if (a.dataset.goto) {{ e.preventDefault(); show(a.dataset.goto, a.dataset.anchor); return; }}
    var href = a.getAttribute('href') || '';
    if (href.charAt(0) === '#' && href.length > 1) {{
      var active = document.querySelector('.uag-doc.is-on');
      var t = active && active.querySelector(href);
      if (t) {{ e.preventDefault(); t.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}
    }}
  }});
  show('home');
}})();
</script>
'''

OUT.write_text(page)
print(f"wrote {OUT}  {OUT.stat().st_size/1024/1024:.2f} MB")
