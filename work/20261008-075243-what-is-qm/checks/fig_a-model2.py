# Figure a-model2: sum over paths.
# Left panel: SCHEMATIC (not to scale) geometry: source, two slits, a few routes to one spot.
# Right panels: COMPUTED clock hands for a real 2D geometry (lengths in wavelengths):
#   source on the axis 1e5 wavelengths before the wall; slits of width a = 4, centres at +-8 (d = 4a = 16);
#   screen L = 1e5 wavelengths behind the wall (far on both sides: d^2/(lambda L) = 0.00256),
#   i.e. the same ideal set-up as figures a-one-vs-both and a-model1.
# Each slit is cut into n = 8 strips; each hand stands for the routes through one strip:
# angle = 2*pi*(length source->strip centre + strip centre->spot)/lambda, all hands of equal length 1/n
# (the 1/distance weighting varies by under 1% here and is left out).
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-model2.png')
lam, Ls, L, a, d, n = 1.0, 1e5, 1e5, 4.0, 16.0, 8
k = 2*np.pi/lam
def strips(c, m): return c - a/2 + (np.arange(m) + 0.5)*a/m
def hands(x, m=n):
    out = {}
    for name, c in (("left", -d/2), ("right", d/2)):
        y = strips(c, m); ell = np.hypot(Ls, y) + np.hypot(L, x - y)
        out[name] = np.exp(1j*k*ell)/m
    return out
def total(x, m=n):
    h = hands(x, m); return h["left"].sum() + h["right"].sum()
# fine (near-continuous) pattern to locate bright centre and first dark spot
xx = np.linspace(0, 1.2*lam*L/d, 6001)
Pfine = np.array([abs(total(x, 400))**2 for x in xx])
Pdisc = np.array([abs(total(x))**2 for x in xx])
x_peak = xx[(xx > 0.8*lam*L/d)][np.argmax(Pdisc[xx > 0.8*lam*L/d])]; print(f'side bright peak at x = {x_peak:.1f}, chance {abs(total(x_peak))**2:.3f}')
x_bright = lam*L/d   # exactly one stripe spacing out: the two groups line up exactly
print(f'first side bright stripe x = {x_bright:.1f} (stripe spacing {lam*L/d:.1f})')
win = (xx > 0.3*lam*L/d) & (xx < 0.8*lam*L/d)
x_dark = xx[win][np.argmin(Pdisc[win])]; x_dark_fine = xx[win][np.argmin(Pfine[win])]
print(f"stripe spacing lam*L/d = {lam*L/d:.1f}; first dark spot (8 strips) x = {x_dark:.2f}, (400 strips) x = {x_dark_fine:.2f}")
print(f"chance (8 strips): centre {abs(total(0.0))**2:.3f}, side bright {abs(total(x_bright))**2:.3f}, dark {abs(total(x_dark))**2:.2e}; "
      f"(400 strips): centre {abs(total(0.0,400))**2:.3f}, dark {abs(total(x_dark_fine,400))**2:.2e}")
r = [np.hypot(Ls, y) + np.hypot(L, x - y) for x in (0, x_bright, x_dark) for y in (strips(-d/2, n), strips(d/2, n))]
rr = np.concatenate(r); print("route length spread (1/r weighting variation):", round((rr.max()-rr.min())/rr.min()*100, 3), "%")
for x, nm in ((x_bright, "bright"), (x_dark, "dark")):
    h = hands(x); gl, gr = h["left"].sum(), h["right"].sum()
    ang = lambda z: np.degrees(np.angle(z))
    print(f"{nm}: left group |{abs(gl):.3f}|, right group |{abs(gr):.3f}|, angle between groups "
          f"{(ang(gr)-ang(gl)+180)%360-180:.1f} deg; fan of hands within a slit: "
          f"{np.degrees(np.ptp(np.unwrap(np.angle(h['left'])))):.0f} deg (left), "
          f"{np.degrees(np.ptp(np.unwrap(np.angle(h['right'])))):.0f} deg (right)")

plt.rcParams.update({'font.size': 11})
fig = plt.figure(figsize=(12, 5.2))
gs = GridSpec(1, 3, width_ratios=[0.8, 1.2, 1.0], wspace=0.08, figure=fig)
# ---- left: schematic geometry (beam travels upward; left slit on the left) ----
ax = fig.add_subplot(gs[0]); ax.set_xlim(-4.6, 4.6); ax.set_ylim(-0.9, 10.6); ax.axis('off')
src = (0.0, 0.3); wall_y = 3.6; scr_y = 9.6; spot = (1.6, scr_y)
for (x0, x1) in ((-4.0, -2.4), (-0.6, 0.6), (2.4, 4.0)):
    ax.plot([x0, x1], [wall_y, wall_y], 'k-', lw=4)
ax.plot([-4.0, 4.0], [scr_y, scr_y], color='0.4', lw=2)
ax.text(4.1, scr_y, "screen", va='center', fontsize=9.5)
ax.text(4.1, wall_y, "wall", va='center', fontsize=9.5)
for x in (-2.0, -1.5, -1.0):
    ax.plot([src[0], x, spot[0]], [src[1], wall_y, spot[1]], color='k', lw=1.1)
for x in (1.0, 1.5, 2.0):
    ax.plot([src[0], x, spot[0]], [src[1], wall_y, spot[1]], color='0.55', ls='--', lw=1.2)
ax.plot(*src, 'ko', ms=7); ax.text(src[0], src[1]-0.35, "source", ha='center', va='top', fontsize=9.5)
ax.plot(*spot, 'ko', ms=7); ax.text(spot[0], spot[1]+0.3, "spot", ha='center', va='bottom', fontsize=9.5)
ax.text(-2.5, wall_y-0.3, "left slit", ha='right', va='top', fontsize=9)
ax.text(2.5, wall_y-0.3, "right slit", ha='left', va='top', fontsize=9)
ax.text(-4.4, 6.6, "routes via\nleft slit\n(black)", fontsize=8.5, va='center')
ax.text(2.55, 6.6, "routes via\nright slit\n(grey,\ndashed)", fontsize=8.5, va='center')
ax.set_title("A few routes to one spot\n(schematic, not to scale)", fontsize=10.5)
# ---- right: computed clock hands ----
def draw(axp, x, title):
    h = hands(x); z = 0j
    rot = np.exp(-1j*np.angle(h["left"].sum()))   # overall angle is irrelevant: left group total points right
    for name, col in (("left", 'k'), ("right", '0.55')):
        for v in h[name]*rot:
            axp.annotate('', xy=((z+v).real, (z+v).imag), xytext=(z.real, z.imag),
                         arrowprops=dict(arrowstyle='-|>', color=col, lw=1.5, mutation_scale=11,
                                         shrinkA=0, shrinkB=0))
            z = z + v
    gl = h["left"].sum()*rot; gr = h["right"].sum()*rot
    off = -0.16j
    axp.annotate('', xy=((gl+off).real, (gl+off).imag), xytext=(off.real, off.imag),
                 arrowprops=dict(arrowstyle='-|>', color='k', lw=3.2, mutation_scale=16, shrinkA=0, shrinkB=0))
    off2 = off - (0.09j if abs(gl+gr) < 0.05 else 0)   # dark spot: right total drawn a little lower so both show
    axp.annotate('', xy=((gl+gr+off2).real, (gl+gr+off2).imag), xytext=((gl+off2).real, (gl+off2).imag),
                 arrowprops=dict(arrowstyle='-|>', color='0.55', lw=3.2, mutation_scale=16, shrinkA=0, shrinkB=0,
                                 ls='--'))
    axp.plot([0], [0], 'ko', ms=4)
    axp.set_title(title, fontsize=10.5)
    axp.set_aspect('equal'); axp.axis('off')
    return gl, gr, z
ax2 = fig.add_subplot(gs[1]); gl, gr, z = draw(ax2, x_bright, "Bright spot (one stripe spacing out)")
ax2.set_xlim(-0.08, 1.9); ax2.set_ylim(-0.75, 0.55)
ax2.text(0.9, -0.3, "each slit's hands fan out, but the two group\ntotals (bold) point the same way:\n"
         f"total {abs(z):.1f}, chance {abs(z)**2:.1f}", ha='center', va='top', fontsize=9)
ax3 = fig.add_subplot(gs[2]); gl, gr, z = draw(ax3, x_dark, "Dark spot (first dark stripe)")
ax3.set_xlim(-0.12, 1.12); ax3.set_ylim(-0.75, 0.55)
ax3.text(0.5, -0.3, "left group goes out,\nright group comes straight back:\n"
         f"total {abs(z):.0f}, chance {abs(z)**2:.0f}", ha='center', va='top', fontsize=9)
fig.text(0.66, 0.06, "Thin arrows: one hand per strip of a slit (8 per slit), added tip to tail; black = left slit, grey = right slit.\n"
         "Bold arrows, drawn just below: each slit's group total (left solid black, right dashed grey).",
         ha='center', fontsize=9)
fig.savefig(out, dpi=150, bbox_inches='tight'); print("saved", os.path.abspath(out))
