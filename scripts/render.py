#!/usr/bin/env python3
"""Render a tutor answer (Markdown + LaTeX) to a standalone HTML page next to it.

Usage: python3 scripts/render.py work/<run-id>/final.md
Writes answer.html next to it (final-A.md becomes answer-A.html). Math is rendered in the browser by MathJax.
"""
import html
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("The 'markdown' package is missing. Run: pip install -r requirements.txt")

MATH = re.compile(
    r"(\$\$[\s\S]+?\$\$|\\\[[\s\S]+?\\\]|\\\([\s\S]+?\\\)|\$(?!\s)[^$\n]+?(?<!\s)\$)"
)

PAGE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<script>
window.MathJax = {{ tex: {{ inlineMath: [['$','$'],['\\\\(','\\\\)']],
  displayMath: [['$$','$$'],['\\\\[','\\\\]']] }} }};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"></script>
<style>
:root {{ --ink:#1A1E3A; --soft:#545A7A; --paper:#F4F6FA; --line:#D9DDEA; --accent:#5B3FD0; }}
@media (prefers-color-scheme: dark) {{ :root {{ --ink:#E7E9F6; --soft:#A3A8C6; --paper:#121429; --line:#2E3254; --accent:#A893FF; }} }}
body {{ margin:0; background:var(--paper); color:var(--ink);
  font:18px/1.68 "Newsreader", Georgia, "Times New Roman", serif; }}
main {{ max-width:70ch; margin:0 auto; padding:40px 20px 80px; }}
h1,h2,h3 {{ line-height:1.3; }}
img {{ max-width:100%; height:auto; border:1px solid var(--line); border-radius:8px; background:#fff; }}
pre, table, mjx-container[display="true"] {{ overflow-x:auto; max-width:100%; }}
code {{ font-size:.88em; }}
table {{ border-collapse:collapse; }} td, th {{ border:1px solid var(--line); padding:4px 8px; }}
blockquote {{ border-left:3px solid var(--line); margin:0; padding-left:14px; color:var(--soft); }}
strong {{ color:var(--accent); }}
</style></head>
<body><main>
{body}
</main></body></html>
"""


def render(md_text: str) -> str:
    maths = []

    def stash(m):
        maths.append(m.group(0))
        return f"@@MATH{len(maths) - 1}@@"

    protected = MATH.sub(stash, md_text)
    body = markdown.markdown(protected, extensions=["tables", "fenced_code", "sane_lists"])
    return re.sub(r"@@MATH(\d+)@@", lambda m: html.escape(maths[int(m.group(1))]), body)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 scripts/render.py work/<run-id>/final.md")
    src = Path(sys.argv[1])
    if not src.is_file():
        sys.exit(f"Not found: {src}")
    text = src.read_text(encoding="utf-8")
    first = next((ln.strip("# ").strip() for ln in text.splitlines() if ln.strip()), "Answer")
    out = src.with_name(src.stem.replace("final", "answer", 1) + ".html")
    out.write_text(PAGE.format(title=html.escape(first[:80]), body=render(text)), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
