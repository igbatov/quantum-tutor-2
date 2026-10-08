# Figure a-model1: amplitudes from each slit, their sum, and the chance, along a far screen.
# Same ideal set-up as a-one-vs-both: d = 4a, far screen, X = position in stripe spacings.
# Exact far-screen amplitudes (common phase dropped): A_L = s e^{-i pi X}, A_R = s e^{+i pi X}, s = sinc(X/4).
# Plotting convention: all angles measured relative to the left-slit hand (multiply both by e^{+i pi X}),
# so A_L = s (real, positive) and A_R = s e^{2 pi i X}; the right route is X wavelengths longer.
# Top panel shows real parts only (a simplification); clock-hand row shows the full complex values;
# chance uses the full complex sum |A_L + A_R|^2.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-model1.png')
W = 2.6
X = np.linspace(-W, W, 5201)
s = np.sinc(X/4)
AL = s + 0j; AR = s*np.exp(2j*np.pi*X); S = AL + AR
# check the convention changes nothing physical
AL0 = s*np.exp(-1j*np.pi*X); AR0 = s*np.exp(1j*np.pi*X)
assert np.allclose(abs(S)**2, abs(AL0+AR0)**2) and np.allclose(abs(S)**2, 4*s**2*np.cos(np.pi*X)**2)
chance = abs(S)**2; addch = abs(AL)**2 + abs(AR)**2
i0 = np.argmin(abs(X)); ih = np.argmin(abs(X-0.5)); iq = np.argmin(abs(X-0.25))
print(f"bright X=0: A_L={AL[i0].real:.3f}, A_R={AR[i0].real:.3f}, sum={S[i0].real:.3f}, chance={chance[i0]:.3f}, chances added={addch[i0]:.3f}")
print(f"dark X=0.5: A_L={AL[ih].real:.3f}, A_R={AR[ih]:.3f}, |sum|={abs(S[ih]):.1e}, chance={chance[ih]:.1e}, chances added={addch[ih]:.3f}")
print(f"X=0.25: Re sum={S[iq].real:.3f}, (Re sum)^2={S[iq].real**2:.3f}, true chance={chance[iq]:.3f}")
print("max |X| plotted", W, "; s>0 throughout:", bool((s > 0).all()))

plt.rcParams.update({'font.size': 11})
fig = plt.figure(figsize=(8.5, 9.4))
gs = GridSpec(3, 1, height_ratios=[1.0, 0.55, 1.0], hspace=0.75, figure=fig)
ax1 = fig.add_subplot(gs[0]); ax3 = fig.add_subplot(gs[2], sharex=ax1)
# top: real parts
ax1.plot(X, AR.real, color='0.5', lw=1.4, label="from the right slit")
ax1.plot(X, AL.real, 'k--', lw=1.4, label="from the left slit")
ax1.plot(X, S.real, 'k-', lw=2.2, label="sum of the two")
ax1.axhline(0, color='0.7', lw=0.6)
ax1.set_ylim(-1.75, 3.1); ax1.set_yticks([-1, 0, 1, 2])
ax1.set_ylabel("amplitude\n(real part)")
ax1.set_title("Amplitudes (real parts; angles measured from the left-slit hand)", fontsize=11, loc='left')
ax1.legend(loc='upper left', fontsize=9, frameon=False, ncol=3)
ax1.annotate("bright spot: 1 + 1 = 2", xy=(0.02, 2.0), xytext=(0.95, 2.25), fontsize=9,
             arrowprops=dict(arrowstyle='->', lw=0.8))
ax1.annotate("dark spot: about +1 and −1, sum 0", xy=(0.5, -0.97), xytext=(0.8, -1.45), fontsize=9,
             va='center', arrowprops=dict(arrowstyle='->', lw=0.8))
ax1.annotate("", xy=(0.5, 0.0), xytext=(0.8, -1.38), arrowprops=dict(arrowstyle='->', lw=0.8))
ax1.set_xlabel("position on screen (units of the stripe spacing)")
# middle: clock hands at a few spots
xs_hand = [0.0, 0.25, 0.5, 0.75, 1.0]
labels = ["bright", "", "dark", "", "bright"]
sub = gs[1].subgridspec(1, 5, wspace=0.05)
for j, (xv, lab) in enumerate(zip(xs_hand, labels)):
    a = fig.add_subplot(sub[j])
    a.set_aspect('equal'); a.set_xlim(-0.3, 2.3); a.set_ylim(-1.15, 1.15); a.axis('off')
    i = np.argmin(abs(X-xv)); l, r = AL[i], AR[i]; t = l + r
    off = 0.12j if abs(t) < 0.05 else 0       # dark spot: draw right hand slightly apart so it is visible
    if abs(t) > 0.05:
        a.annotate('', xy=(t.real, t.imag), xytext=(0, 0),
                   arrowprops=dict(arrowstyle='-|>', color='tab:blue', lw=4.5, alpha=0.55, mutation_scale=18))
    a.annotate('', xy=(l.real, l.imag), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color='k', lw=1.8, ls='--'))
    a.annotate('', xy=((l+r+off).real, (l+r+off).imag), xytext=((l+off).real, (l+off).imag),
               arrowprops=dict(arrowstyle='-|>', color='0.5', lw=2.0))
    a.plot([0], [0], 'ko', ms=3)
    size = "sum 0" if abs(t) < 0.05 else f"sum {abs(t):.1f}"
    a.set_title(f"X = {xv:g}" + (f" ({lab})" if lab else "") + f"\n{size}", fontsize=9)
fig.canvas.draw(); _bb = a.title.get_window_extent().transformed(fig.transFigure.inverted())
fig.text(0.5, _bb.y1 + 0.012,
         "The same amplitudes as clock hands: left (dashed), right added tip to tail (grey), sum (thick, blue)",
         fontsize=9.5, ha='center')
# bottom: chance
ax3.plot(X, chance, 'k-', lw=2.2, label="chance = (size of the sum)²")
ax3.plot(X, addch, color='tab:blue', ls='--', lw=1.5, label="the two chances added")
ax3.axhline(0, color='0.7', lw=0.6)
ax3.set_ylim(-0.3, 5.7); ax3.set_yticks([0, 1, 2, 3, 4])
ax3.set_ylabel("relative chance")
ax3.set_title("Chance of landing", fontsize=11, loc='left')
ax3.legend(loc='upper left', fontsize=9, frameon=False, ncol=2)
ax3.annotate("bright: 2² = 4", xy=(0.02, 4.0), xytext=(0.95, 4.4), fontsize=9, arrowprops=dict(arrowstyle='->', lw=0.8))
ax3.annotate("dark: 0² = 0", xy=(0.52, 0.02), xytext=(1.7, 3.6), fontsize=9, arrowprops=dict(arrowstyle='->', lw=0.8))
ax3.annotate("chances added:\nabout 2 at both spots", xy=(0.0, 2.0), xytext=(-2.5, 3.6), fontsize=9,
             arrowprops=dict(arrowstyle='->', lw=0.8))
ax3.annotate("", xy=(0.5, addch[ih]), xytext=(-1.45, 3.65), arrowprops=dict(arrowstyle='->', lw=0.8))
ax3.set_xlim(-W, W)
ax3.set_xlabel("position on screen (units of the stripe spacing)")
fig.savefig(out, dpi=150, bbox_inches='tight'); print("saved", os.path.abspath(out))
