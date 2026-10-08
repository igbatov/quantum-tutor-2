# Round 4: legends say 'ideal which-slit detector'; title gap list marked incomplete.
# Round 3: legend labels made true as written ("both slits open (ideal set-up)";
# "if chances simply added (also with a which-slit detector)").
# Redrawn (round 2): adds a zoom panel over a wider range so the one-slit side bands
# (about 5% of the central peak, beyond the dark gap at X = +-4) are visible, instead of
# looking like "one broad hump" on the linear main axes.
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "a-one-vs-two.png")
P1f = lambda X: np.sinc(X/4)**2
plt.rcParams.update({"font.size": 12})
fig, (ax, az) = plt.subplots(2, 1, figsize=(7.5, 7.2), gridspec_kw={"height_ratios": [3, 1.6]})
X = np.linspace(-6, 6, 4001); P1 = P1f(X)
ax.plot(X, P1, color="grey", lw=1.2, label="one slit open (either one)")
ax.plot(X, 2*P1, "k--", lw=1.5, label="if chances simply added\n(also with an ideal which-slit detector)")
ax.plot(X, 4*P1*np.cos(np.pi*X)**2, "k-", lw=2.8, label="both slits open (ideal set-up)")
for xd in [-1.5, -0.5, 0.5, 1.5]:
    ax.annotate("", xy=(xd, 0.12), xytext=(xd, 0.75), zorder=5,
                arrowprops=dict(arrowstyle="-|>,head_width=0.35,head_length=0.6", fc="white", ec="black", lw=1.2))
    ax.plot([xd], [P1f(xd)], "o", ms=6, mfc="white", mec="black", zorder=6)
ax.text(2.05, 2.3, "arrows: dark stripes: zero with\nboth slits open (ideal set-up);\ncircles: one slit alone\n(0.95 and 0.62)", fontsize=9.5, ha="left")
ax.set_xlim(-6, 6); ax.set_ylim(0, 4.6)
ax.set_xlabel("position on screen (units of stripe spacing)"); ax.set_ylabel("relative chance of landing here")
ax.legend(loc="upper left", fontsize=8.5, frameon=False)
# zoom panel: wider range, magnified vertical scale
Xw = np.linspace(-14, 14, 8001); Pw = P1f(Xw)
az.plot(Xw, Pw, color="grey", lw=2.0, label="one slit open")
az.plot(Xw, 2*Pw, "k--", lw=1.4, label="chances added\n(ideal which-slit detector)")
az.set_xlim(-14, 14); az.set_ylim(0, 0.25)
az.legend(loc="upper left", fontsize=8.5, frameon=False)
az.set_xlabel("position on screen (units of stripe spacing)"); az.set_ylabel("same, zoomed x18")
for s in (-1, 1):
    az.annotate("one-slit side band\n(about 5% of centre)", xy=(s*5.72, P1f(5.72)), xytext=(s*10.5, 0.115),
                ha="center", fontsize=9, arrowprops=dict(arrowstyle="->", lw=1))
az.text(0, 0.1, "central band\n(off scale)", ha="center", fontsize=9, bbox=dict(fc="white", ec="none"))
az.set_title("wider view, zoomed: dark gaps at \u00b14, \u00b18, \u2026, fainter side bands between them", fontsize=10)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
