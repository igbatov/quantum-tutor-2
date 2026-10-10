import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-terms-and-precession.png")
plt.rcParams.update({"font.size": 10})
R = 3.29e15
fig = plt.figure(figsize=(9, 4.6))
gs = GridSpec(2, 2, height_ratios=[3.2, 1], width_ratios=[1.05, 1], hspace=0.55, wspace=0.3)

ax = fig.add_subplot(gs[0, 0])
for n in range(1, 7):
    T = R / n**2
    width = 1.0 - 0.1 * (n - 1)
    ax.hlines(T / 1e15, 0, width, color="k", lw=1.5)
    ax.text(width + 0.03, T / 1e15, f"n={n}", va="center", fontsize=8)
arrows = [(2, 1, 0.2, "Lyman-α\n2.47e15 Hz"), (3, 2, 0.45, "Balmer-α\n4.57e14 Hz"), (4, 2, 0.7, "Balmer-β\n6.17e14 Hz")]
for hi, lo, xpos, lab in arrows:
    y0, y1 = R / hi**2 / 1e15, R / lo**2 / 1e15
    ax.annotate("", xy=(xpos, y1), xytext=(xpos, y0), arrowprops=dict(arrowstyle="<->", lw=1.2))
    ax.text(xpos + 0.02, (y0 + y1) / 2 + (0.2 if lo == 1 else 0.0), lab, fontsize=7.5, va="center")
ax.set_xlim(0, 1.35); ax.set_xticks([])
ax.set_ylabel("term R/n² (10¹⁵ Hz)")
ax.set_title("Hydrogen terms; a line = a difference of two terms", fontsize=9.5)

axf = fig.add_subplot(gs[1, 0])
# all gross-structure lines (Lyman, Balmer, Paschen...) as faint ticks, the three named ones bold
for a in range(1, 6):
    for b in range(a + 1, 60):
        f = R * (1 / a**2 - 1 / b**2)
        if f < 3e15:
            axf.vlines(f / 1e15, 0, 0.5, color="0.7", lw=0.6)
for f in [2.47e15, 4.57e14, 6.17e14]:
    axf.vlines(f / 1e15, 0, 1, color="k", lw=2)
fs = R * (1 / 4 + 1 / 9)
axf.plot(fs / 1e15, 0.5, "x", ms=10, mew=2.5, color="C3")
axf.text(fs / 1e15, 1.15, "sum R(1/4+1/9)=1.19e15 Hz:\nno line here", ha="center", fontsize=7.5, color="C3")
axf.set_xlim(0, 3); axf.set_ylim(0, 2.2); axf.set_yticks([])
axf.set_xlabel("frequency (10¹⁵ Hz); bold = lines named above, grey = other H lines")

axs = fig.add_subplot(gs[:, 1])
t = np.linspace(0, 5, 2000)
axs.plot(t, np.full_like(t, np.cos(np.pi / 3)), "-", lw=2, label="along the field: cos 60° = 0.5 (constant)")
axs.plot(t, np.sin(np.pi / 3) * np.cos(2 * np.pi * t), "--", lw=1.6, label="transverse: 0.866 cos(2πt/T)")
axs.set_xlabel("time t (units of the Larmor period T)")
axs.set_ylabel("spin component (units of its length)")
axs.set_ylim(-1.05, 1.25)
axs.set_title("Spin tipped 60° from a field along z", fontsize=9.5)
axs.legend(fontsize=8, loc="upper right")
fig.savefig(OUT, dpi=150, bbox_inches="tight")
print("saved", os.path.abspath(OUT))
