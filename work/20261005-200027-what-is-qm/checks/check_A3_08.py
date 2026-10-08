# Figure/caption consistency for figures/a-one-vs-two.png vs final-A.md caption:
# "identical slits spaced four slit-widths apart"; "magnified about 18 times"; legend labels true as written;
# arrows at dark stripes; circles at 95% / 62%.
import re, numpy as np, os
here = os.path.dirname(os.path.abspath(__file__)); s = open(os.path.join(here, "fig_a-one-vs-two.py")).read()
labels = re.findall(r'label="([^"]+)"', s); print("legend labels:", labels)
ylim_main = float(re.search(r'ax.set_ylim\(0, ([\d.]+)\)', s).group(1)); ylim_zoom = float(re.search(r'az.set_ylim\(0, ([\d.]+)\)', s).group(1))
print(f"magnification {ylim_main/ylim_zoom:.1f}")
P1 = lambda X: np.sinc(X/4)**2
zeros_env = [k*4 for k in (1, 2)]; print("envelope zeros (d = 4a):", zeros_env, P1(np.array(zeros_env)))
arrows = [float(v) for v in re.search(r'for xd in \[([^\]]+)\]', s).group(1).split(",")]
print("arrow positions", arrows, "two-slit value there", [f"{4*P1(a)*np.cos(np.pi*a)**2:.0e}" for a in arrows], "circles", np.round(P1(np.array(arrows)), 3))
ok = ("both slits open (ideal set-up)" in labels and any("if chances simply added" in l for l in labels)
      and not any("actually seen" in l or "one slit or the other" in l for l in labels)
      and 17 <= ylim_main/ylim_zoom <= 19 and os.path.exists(os.path.join(here, "..", "figures", "a-one-vs-two.png")))
print("PASS" if ok else "FAIL")
