# Figure a-three-distances: two slits (width a, centres at -2a and +2a, so d = 4a) seen on screens
# at three distances, chosen by Fresnel number N = d^2/(lambda L). Exact 1D scalar paraxial (Fresnel)
# propagation of a monochromatic plane wave through the slits, via Fresnel integrals.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.special import fresnel
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-three-distances.png')
a, d = 1.0, 4.0
def u(x, c, lL):
    s = np.sqrt(2/lL); S1, C1 = fresnel(s*(c-a/2-x)); S2, C2 = fresnel(s*(c+a/2-x))
    return ((C2-C1) + 1j*(S2-S1))/np.sqrt(2j)
PANELS = [("Close screen", 20.0, 5.0), ("Middle distance", 3.0, 14.0), ("Far screen", 0.05, 640.0)]
plt.rcParams.update({'font.size': 11})
fig, axs = plt.subplots(3, 1, figsize=(8, 10))
for k, (ax, (title, N, W)) in enumerate(zip(axs, PANELS)):
    lL = d*d/N; x = np.linspace(-W, W, 40001)
    uL, uR = u(x, -d/2, lL), u(x, d/2, lL)
    Ib, IL = abs(uL+uR)**2, abs(uL)**2; M = Ib.max()
    ax.plot(x, Ib/M, 'k-', lw=2.0, label="both slits open")
    ax.plot(x, IL/M, color='0.45', lw=1.0, label="left slit only", zorder=3)
    ax.axhline(0, color='0.7', lw=0.6)
    ax.set_xlim(-W, W); ax.set_ylim(-0.2, 1.12)
    ax.set_yticks([0, 0.5, 1])
    ax.set_title(f"{title}:  N = d²/(λL) = {N:g}   (stripe spacing λL/d = {lL/d:.2g} a)", fontsize=11)
    ax.set_ylabel("relative chance")
    if k < 2:
        for c in (-d/2, d/2):
            ax.add_patch(plt.Rectangle((c-a/2, -0.16), a, 0.07, color='k', clip_on=False))
        ax.text(d/2+a/2+0.03*W, -0.125, "slits", va='center', fontsize=9)
        ax.set_xlabel(f"position on screen x (units of slit width a; shown: ±{W:g} a)")
    else:
        ax.plot([-d/2, d/2], [-0.125, -0.125], 'k|', ms=9, mew=2)
        ax.annotate("both slits are here (4 a apart,\ntoo close to separate at this scale)", xy=(0, -0.125),
                    xytext=(0.30*W, -0.125), va='center', fontsize=8.5, arrowprops=dict(arrowstyle='->', lw=0.8))
        ax.set_xlabel(f"position on screen x (units of slit width a; shown: ±{W:g} a)")
        top = ax.secondary_xaxis('top', functions=(lambda v: v*d/lL, lambda X: X*lL/d))
        top.set_xlabel("same position in stripe spacings (range of the one-slit vs both-slits figure)", fontsize=9.5)
        top.tick_params(labelsize=9)
    if k == 0:
        ax.legend(loc='upper center', fontsize=9, frameon=False, ncol=2)
        ax.annotate("ripples on each band", xy=(-2.3, 0.97), xytext=(-4.8, 0.85), fontsize=8.5,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
        ax.annotate("faint stripes in the gap\n(at most 12% of peak)", xy=(0.0, 0.09), xytext=(0.0, 0.42), fontsize=8.5,
                    ha='center', arrowprops=dict(arrowstyle='->', lw=0.8))
    if k == 1:
        ax.annotate("full stripes where\nthe bands overlap", xy=(0.66, 0.05), xytext=(4.5, 0.85), fontsize=8.5,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
        ax.annotate("stripes again at the\nfaint outer edges", xy=(6.0, 0.12), xytext=(8.0, 0.42), fontsize=8.5,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
        ax.annotate("weak stripes where\nmainly one band reaches", xy=(-3.4, 0.36), xytext=(-13.5, 0.75), fontsize=8.5,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
    if k == 2:
        ax.annotate("faint side bands beyond ±4 stripe\nspacings (under 5% of peak)", xy=(-480, 0.05), xytext=(-620, 0.5), fontsize=8.5,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
