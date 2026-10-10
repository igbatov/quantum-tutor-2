import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "a-pythagoras.png")
plt.rcParams.update({"font.size": 11})
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1, 1.25]})
t = np.radians(30); c, s = np.cos(t), np.sin(t)
axL.add_patch(Polygon([[0, 0], [c, 0], [c, s]], closed=True, fc="0.88", ec="none"))
axL.annotate("", xy=(c, s), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=2.5, color="k"))
axL.text(0.36, 0.30, "arrow, length 1", rotation=30, fontsize=10)
axL.plot([c, c], [0, s], "k--", lw=1.2); axL.plot([0, c], [s, s], "k--", lw=1.2)
axL.plot([0, c], [0, 0], "k-", lw=6, solid_capstyle="butt"); axL.plot([0, 0], [0, s], "k-", lw=6, solid_capstyle="butt")
axL.text(c/2, -0.07, f"shadow {c:.2f}", ha="center", va="top")
axL.text(-0.04, s/2, f"shadow {s:.2f}", ha="right", va="center", rotation=90)
axL.text(0.5, 0.86, "0.866² + 0.500² = 0.750 + 0.250 = 1.000\n(Pythagoras)", ha="center", fontsize=9.5)
axL.text(0.5, 0.70, f"plain sizes: 0.87 + 0.50 = {c+s:.2f}\ncubes: {c**3:.3f} + {s**3:.3f} = {c**3+s**3:.3f}",
         ha="center", fontsize=9.5)
axL.set_xlim(-0.15, 1.05); axL.set_ylim(-0.15, 1.0); axL.set_aspect("equal")
axL.set_xlabel("pass direction"); axL.set_ylabel("reflect direction", labelpad=14)
axL.set_title("Arrow at 30° and its two shadows", fontsize=11)
th = np.linspace(0, 90, 901); r = np.radians(th)
styles = {1: ("k-.", 1.6, "p = 1 (plain size)"), 2: ("k-", 3.0, "p = 2 (square)"),
          3: ("k:", 2.0, "p = 3 (cube)"), 4: ("k--", 1.4, "p = 4")}
for p, (ls, lw, lab) in styles.items():
    axR.plot(th, np.cos(r)**p + np.sin(r)**p, ls, lw=lw, label=lab)
axR.axhline(1, color="0.5", lw=6, alpha=0.35, zorder=0, label="every photon accounted for")
for p in (1, 3, 4):
    v = 2*np.cos(np.radians(45))**p
    axR.plot(45, v, "ko", ms=5); axR.annotate(f"{v:.2f}", (45, v), textcoords="offset points", xytext=(6, 4 if p == 1 else -14))
axR.set_xlim(0, 90); axR.set_ylim(0, 1.5); axR.set_xticks(range(0, 91, 15))
axR.set_xlabel("splitter angle θ (degrees)"); axR.set_ylabel("total chance of the two exits")
axR.set_title("(cos θ)^p + (sin θ)^p", fontsize=11)
axR.legend(loc="lower center", fontsize=9, ncol=2, framealpha=0.95)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
