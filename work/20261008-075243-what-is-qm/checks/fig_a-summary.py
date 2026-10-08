# Figure a-summary: four-step visual of the closing paragraph (schematic layout; the small curves and dots
# are computed from the same ideal far-screen two-slit model as a-one-vs-both: slits 4x further apart than
# wide, X in stripe spacings; both slits P = 4 sinc^2(X/4) cos^2(pi X); perfect which-slit record P = 2 sinc^2(X/4)).
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-summary.png')
rng = np.random.default_rng(7)
X = np.linspace(-6, 6, 60001)
P1 = np.sinc(X/4)**2; Pb = 4*P1*np.cos(np.pi*X)**2; Prec = 2*P1
cdf = np.cumsum(Pb); cdf /= cdf[-1]
xs = np.interp(rng.random(4000), cdf, X); ys = rng.random(4000)
# checks: record curve has no zeros inside |X|<4 (no stripes), both-open curve does (dark stripes)
m = np.abs(X) < 3.5
print(f"min of record curve for |X|<3.5: {Prec[m].min():.3f}  (>0: no dark stripes)")
print(f"min of both-open curve for |X|<3.5: {Pb[m].min():.2e}  (=0: dark stripes)")
print(f"areas equal (same number of electrons): {np.trapezoid(Pb, X):.4f} vs {np.trapezoid(Prec, X):.4f}")

plt.rcParams.update({'font.size': 11})
fig = plt.figure(figsize=(13, 5.0))
gs = fig.add_gridspec(2, 4, height_ratios=[4.2, 0.8], hspace=0.38, wspace=0.32, left=0.03, right=0.985, top=0.835, bottom=0.03)
axs = [fig.add_subplot(gs[0, i]) for i in range(4)]
titles = ["1. Matter and light arrive\nin whole lumps",
          "2. Where each lands can only\nbe given as chances",
          "3. Chances come from amplitudes\nthat add and cancel",
          "4. A record of the route\nstops the cancelling"]
for ax, t in zip(axs, titles):
    ax.set_title(t, fontsize=11.5)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color('0.6')

# 1: a few single dots on a screen
ax = axs[0]
ax.scatter(xs[:12], 0.15+0.7*ys[:12], s=40, c='k', linewidths=0)
ax.set_xlim(-6, 6); ax.set_ylim(0, 1)
ax.set_xlabel("screen: 12 electrons,\neach one whole dot", fontsize=10)

# 2: many dots and the chance curve
ax = axs[1]
ax.scatter(xs, 0.05+0.5*ys, s=0.6, c='k', linewidths=0)
ax.plot(X, 0.58 + 0.33*Pb/Pb.max(), 'k-', lw=1.6)
ax.set_xlim(-6, 6); ax.set_ylim(0, 1)
ax.text(-5.7, 0.975, "chance of\nlanding", ha='left', va='top', fontsize=9)
ax.set_xlabel("4,000 dots follow the chances;\nno single dot is predictable", fontsize=10)

# 3: amplitudes alike vs opposite
ax = axs[2]; ax.set_xlim(0, 10); ax.set_ylim(0, 10)
def arr(a, b, lw=2.2, color='k'):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=14, lw=lw, color=color))
ax.text(5, 9.2, "amplitude from left slit + from right slit", ha='center', fontsize=9)
# bright spot: +1 +1
ax.text(0.4, 7.3, "bright\nspot", fontsize=10, va='center')
arr((2.8, 7.3), (4.6, 7.3)); arr((4.6, 7.3), (6.4, 7.3), color='0.45')
ax.text(6.8, 7.3, "= 2\nchance 4", fontsize=10, va='center')
ax.text(3.7, 6.6, "+1", ha='center', fontsize=9); ax.text(5.5, 6.6, "+1", ha='center', fontsize=9, color='0.35')
# dark spot: +1 -1
ax.text(0.4, 3.6, "dark\nspot", fontsize=10, va='center')
arr((2.8, 3.9), (4.6, 3.9)); arr((4.6, 3.3), (2.8, 3.3), color='0.45')
ax.text(6.8, 3.6, "= 0\nchance 0", fontsize=10, va='center')
ax.text(3.7, 4.35, "+1", ha='center', fontsize=9); ax.text(3.7, 2.55, "−1", ha='center', fontsize=9, color='0.35')
ax.text(5, 1.0, "adding chances instead\nwould give 2 at both spots", ha='center', va='center', fontsize=9, style='italic')

# 4: record vs no record
ax = axs[3]
ax.plot(X, Pb, 'k-', lw=1.8, label="no record:\nstripes")
ax.plot(X, Prec, color='0.4', ls='--', lw=1.8, label="perfect which-slit\nrecord: no stripes")
ax.set_xlim(-6, 6); ax.set_ylim(-0.1, 5.6)
ax.legend(loc='upper center', fontsize=8.5, frameon=False, ncol=2, handlelength=1.6, columnspacing=0.8)
ax.set_xlabel("position on screen (same number\nof electrons in both curves)", fontsize=10)

# arrows between panels
for i in range(3):
    b0 = axs[i].get_position(); b1 = axs[i+1].get_position()
    y = b0.y0 + 0.5*b0.height
    fig.add_artist(FancyArrowPatch((b0.x1+0.004, y), (b1.x0-0.004, y), transform=fig.transFigure,
                                   arrowstyle='-|>', mutation_scale=16, lw=1.6, color='k'))

# bottom note
axn = fig.add_subplot(gs[1, :]); axn.axis('off')
axn.text(0.5, 0.5, "The same amplitude rule, plus one rule for identical particles (two electrons never share one state; "
         "photons can pile into one),\nis the physics behind atoms, chemical bonds, transistors and lasers.",
         ha='center', va='center', fontsize=10.5, transform=axn.transAxes,
         bbox=dict(boxstyle='round,pad=0.6', fc='0.95', ec='0.5'))
fig.suptitle("What quantum mechanics is about, in four steps (schematic; curves computed for the ideal two-slit set-up)",
             fontsize=12.5, y=0.985)
fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
