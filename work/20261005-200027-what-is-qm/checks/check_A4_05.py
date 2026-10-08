# Figure-label / text consistency after the "routes -> ways, combined per slit" rewrite.
# Text: grey = one slit, dashed = chances added / which-slit detector, bold = both open; new paragraph
# points to "(bottom panel)" for "dark gaps" and "much fainter side bands".
import re, os, numpy as np
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.join(here, "..")
txt = open(os.path.join(root, "final-A.md")).read(); fig = open(os.path.join(here, "fig_a-one-vs-two.py")).read()
labels = re.findall(r'label="([^"]+)"', fig); texts = re.findall(r'(?:text|annotate|set_title)\("([^"]+)"', fig)
print("labels:", labels); print("texts:", texts)
checks = {
 "no leftover 'route' wording in text or figure": "route" not in txt.lower() and "route" not in fig.lower(),
 "grey = one slit": 'color="grey"' in fig and "one slit open" in labels[0],
 "dashed = chances added / which-slit": '"k--"' in fig and "which-slit detector" in labels[1],
 "bold = both open": 'lw=2.8, label="both slits open' in fig,
 "bottom panel exists and shows dark gaps + side bands": "dark gaps" in fig and "side band" in fig and "(bottom panel)" in txt,
 "bottom panel range covers first two gaps and side bands": "np.linspace(-14, 14" in fig,
 "central band visible as 'wide bright band' in top panel (|X|<4 within -6..6)": "ax.set_xlim(-6, 6)" in fig,
 "figure file exists": os.path.exists(os.path.join(root, "figures", "a-one-vs-two.png")) and os.path.exists(os.path.join(root, "figures", "a-buildup.png")),
}
for k, v in checks.items(): print(("ok  " if v else "BAD ") + k)
print("PASS" if all(checks.values()) else "FAIL")
