import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "a-one-vs-two.png")
plt.rcParams.update({"font.size": 11})
x = np.linspace(-6, 6, 4001); S = np.sinc(x/5)**2
fig, ax = plt.subplots(figsize=(8, 5.6))
ax.plot(x, S, "k--", lw=1, label="one slit open (either one)")
ax.plot(x, 2*S, "k:", lw=1.8, label="two slits, chances simply added (as when the slit is recorded)")
ax.plot(x, 4*S*np.cos(np.pi*x)**2, "C0-", lw=1.8, label="two slits, nothing records the slit: what is seen")
ax.axvline(0.5, color="grey", lw=0.8)
ax.set_xlim(-6, 6); ax.set_ylim(0, 4.2)
ax.set_xlabel("position on the screen (in band spacings)")
ax.set_ylabel("chance of arriving\n(1 unit = one slit alone, at the centre)")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=1, frameon=False, fontsize=10)
# arrow insets in data coordinates, same scale (1 unit arrow = 1.3 x-units)
sc = 1.3; kw = dict(head_width=0.12, head_length=0.18, length_includes_head=True, color="k", lw=1.2)
# bright inset
x0, y0 = -5.6, 3.3
ax.arrow(x0, y0, sc, 0, **kw); ax.arrow(x0+sc, y0, sc, 0, fc="C1", ec="C1", **{k:v for k,v in kw.items() if k!="color"})
ax.plot([x0], [y0], "ko", ms=4)
ax.text(x0+sc, y0-0.35, "bright band: arrows in line,\nwalk 2 long, 2 × 2 = 4 units", ha="center", va="top", fontsize=9)
ax.annotate("", xy=(0, 4.0), xytext=(x0+2*sc+0.1, y0+0.05), arrowprops=dict(arrowstyle="-", color="grey", lw=0.8))
# dark inset
x1, y1 = 3.2, 3.5
ax.arrow(x1, y1, sc, 0, **kw)
ax.arrow(x1+sc, y1-0.18, -sc, 0, fc="C1", ec="C1", **{k:v for k,v in kw.items() if k!="color"})
ax.plot([x1+sc, x1+sc], [y1, y1-0.18], color="k", lw=0.6, ls=":")   # tip of first = tail of second
ax.plot([x1-0.08], [y1-0.09], "ko", ms=5)                              # start = end of the walk
ax.text(x1-0.25, y1-0.09, "start = end", ha="right", va="center", fontsize=8)
ax.text(x1+sc/2+0.2, y1-0.45, "dark band: arrows opposite,\nwalk ends where it began: 0 units\n(one slit alone: about 1)", ha="center", va="top", fontsize=9)
ax.annotate("", xy=(0.5, 0.0), xytext=(x1+sc/2-0.6, y1-1.2), arrowprops=dict(arrowstyle="-", color="grey", lw=0.8))
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
