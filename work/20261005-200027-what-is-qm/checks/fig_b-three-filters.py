import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "b-three-filters.png")
def counts(N, filters_from_vertical):  # photons already vertical; ideal filters
    n, s, res = N, 0.0, [N]
    for a in filters_from_vertical:
        n *= np.cos(np.radians(a - s))**2; s = a; res.append(round(n, 6))
    return res
row1 = counts(100, [90]); row2 = counts(100, [45, 90])
plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots(figsize=(7.5, 4.4))
H = 1.4  # bar height scale for 100
def filt(x, y, ang, label):
    ax.add_patch(Rectangle((x-0.3, y-0.3), 0.6, 0.6, fc="0.92", ec="k", lw=1.3))
    a = np.radians(ang); dx, dy = 0.27*np.sin(a), 0.27*np.cos(a)
    ax.plot([x-dx, x+dx], [y-dy, y+dy], "k-", lw=2.5)
    ax.text(x, y-0.42, label, ha="center", va="top", fontsize=9.5)
def bar(x, y0, n):
    h = H*n/100
    ax.add_patch(Rectangle((x-0.22, y0), 0.44, max(h, 0.0), fc="0.35", ec="k"))
    ax.plot([x-0.3, x+0.3], [y0, y0], "k-", lw=1)
    ax.text(x, y0+h+0.06, f"{n:g}", ha="center", va="bottom", fontsize=12, weight="bold")
for (title, y, fl, cs) in [("two filters", 2.6, [(0,"vertical"),(90,"horizontal")], row1),
                           ("three filters", 0.0, [(0,"vertical"),(45,"45°"),(90,"horizontal")], row2)]:
    ax.text(-0.6, y+1.15, title, fontsize=12, style="italic")
    x = 0.0
    for i, (ang, lab) in enumerate(fl):
        filt(x, y+0.3, ang, lab + " filter")
        bar(x+1.0, y, cs[i]); x += 2.0
ax.annotate("", xy=(7.0, 0.3), xytext=(-0.6, 0.3), arrowprops=dict(arrowstyle="-", color="none"))
ax.text(6.4, 3.3, "light travels\nleft to right →", fontsize=9.5, ha="right", color="0.3")
ax.set_xlim(-0.7, 6.5); ax.set_ylim(-0.6, 4.3); ax.axis("off")
ax.set_title("Adding a filter lets more light through\n(expected photon counts, ideal filters; bar height ∝ count)", fontsize=12)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out), row1, row2)
