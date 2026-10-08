# Figure a-model2: sum over paths.
# Left panel: SCHEMATIC (not to scale) geometry: source, two slits, a few routes to one spot.
# Right panels: COMPUTED clock hands for a real 2D geometry (lengths in wavelengths):
#   source on the axis 300 wavelengths before the wall; slits of width a = 4, centres at +-8 (d = 4a = 16);
#   screen L = 2000 wavelengths behind the wall (far screen: d^2/(lambda L) = 0.128).
# Each slit is cut into n = 8 strips; each hand stands for the routes through one strip:
# angle = 2*pi*(length source->strip centre + strip centre->spot)/lambda, all hands of equal length 1/n
# (the 1/distance weighting varies by under 1% here and is left out).
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-model2.png')
lam, Ls, L, a, d, n = 1.0, 300.0, 2000.0, 4.0, 16.0, 8
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
x_bright = 0.0
win = (xx > 0.3*lam*L/d) & (xx < 0.8*lam*L/d)
x_dark = xx[win][np.argmin(Pdisc[win])]; x_dark_fine = xx[win][np.argmin(Pfine[win])]
print(f"stripe spacing lam*L/d = {lam*L/d:.1f}; first dark spot (8 strips) x = {x_dark:.2f}, (400 strips) x = {x_dark_fine:.2f}")
print(f"chance (8 strips): bright {abs(total(0.0))**2:.3f}, dark {abs(total(x_dark))**2:.2e}; "
      f"(400 strips): bright {abs(total(0.0,400))**2:.3f}, dark {abs(total(x_dark_fine,400))**2:.2e}")
r = [np.hypot(Ls, y) + np.hypot(L, x - y) for x in (0, x_dark) for y in (strips(-d/2, n), strips(d/2, n))]
rr = np.concatenate(r); print("route length spread (1/r weighting variation):", round((rr.max()-rr.min())/rr.min()*100, 3), "%")
for x, nm in ((x_bright, "bright"), (x_dark, "dark")):
    h = hands(x); gl, gr = h["left"].sum(), h["right"].sum()
    ang = lambda z: np.degrees(np.angle(z))
    print(f"{nm}: left group |{abs(gl):.3f}|, right group |{abs(gr):.3f}|, angle between groups "
          f"{(ang(gr)-ang(gl)+180)%360-180:.1f} deg; fan of hands within a slit: "
          f"{np.degrees(np.ptp(np.unwrap(np.angle(h['left'])))):.0f} deg (left), "
          f"{np.degrees(np.ptp(np.unwrap(np.angle(h['right'])))):.0f} deg (right)")

plt.rcParams.update({'font.size': 11})
fig = plt.figure(figsize=(11, 4.9))
gs = GridSpec(1, 3, width_ratios=[1.15, 1, 1], wspace=0.25, figure=fig)
# ---- left: schematic geometry ----
ax = fig.add_subplot(gs[0]); ax.set_xlim(-0.3, 10.3); ax.set_ylim(-4.3, 4.3); ax.axis('off')
src = (0.3, 0.0); wall_x = 3.5; scr_x = 9.6; spot = (scr_x, 1.2)
ax.plot(*src, 'ko', ms=7); ax.text(src[0], -0.6, "source", ha='center', va='top', fontsize=9.5)
ys_l = [-1.75, -1.5, -1.25]; ys_r = [1.25, 1.5, 1.75]
for (y0, y1) in ((-4.0, -1.9), (-1.1, 1.1), (1.9, 4.0)):
    ax.plot([wall_x, wall_x], [y0, y1], 'k-', lw=4)
ax.plot([scr_x, scr_x], [-4.0, 4.0], color='0.4', lw=2)
ax.text(scr_x, -4.2, "screen", ha='center', va='top', fontsize=9.5)
ax.text(wall_x, -4.2, "wall", ha='center', va='top', fontsize=9.5)
for y in ys_l:
    ax.plot([src[0], wall_x, spot[0]], [src[1], y, spot[1]], color='k', ls='--', lw=1.0)
for y in ys_r:
    ax.plot([src[0], wall_x, spot[0]], [src[1], y, spot[1]], color='0.5', ls='-', lw=1.2)
ax.plot(*spot, 'ko', ms=7); ax.text(spot[0]-0.15, spot[1]+0.35, "spot", ha='right', fontsize=9.5)
ax.text(4.0, -2.6, "routes through\nthe left slit (dashed)", fontsize=8.5, va='top')
ax.text(4.0, 3.9, "routes through the\nright slit (grey)", fontsize=8.5, va='top')
ax.set_title("A few routes to one spot\n(schematic, not to scale)", fontsize=10.5)
# ---- right: computed clock hands ----
def draw(axp, x, title):
    h = hands(x); z = 0j
    # rotate so the left-slit group total points to the right (overall angle is irrelevant)
    rot = np.exp(-1j*np.angle(h["left"].sum()))
    pts = [0j]
    for name, col, ls in (("left", 'k', '--'), ("right", '0.5', '-')):
        for v in h[name]*rot:
            axp.annotate('', xy=((z+v).real, (z+v).imag), xytext=(z.real, z.imag),
                         arrowprops=dict(arrowstyle='-|>', color=col, lw=1.6, ls=ls, mutation_scale=10))
            z = z + v; pts.append(z)
    gl = h["left"].sum()*rot; gr = h["right"].sum()*rot
    off = -0.13j
    axp.annotate('', xy=((gl+off).real, (gl+off).imag), xytext=(off.real, off.imag),
                 arrowprops=dict(arrowstyle='-|>', color='k', lw=2.6, mutation_scale=14))
    axp.annotate('', xy=((gl+gr+off).real, (gl+gr+off).imag), xytext=((gl+off).real, (gl+off).imag),
                 arrowprops=dict(arrowstyle='-|>', color='0.5', lw=2.6, mutation_scale=14))
    axp.plot([0], [0], 'ko', ms=4)
    axp.set_title(title, fontsize=10.5)
    axp.set_aspect('equal'); axp.axis('off')
    return gl, gr, z
ax2 = fig.add_subplot(gs[1]); gl, gr, z = draw(ax2, x_bright, "Bright spot (middle of screen)")
ax2.set_xlim(-0.15, 2.15); ax2.set_ylim(-0.8, 0.8)
ax2.text(1.0, -0.42, "left group (bold black)  +  right group (bold grey)\nline up: total length "
         f"{abs(z):.2f}, chance {abs(z)**2:.1f}", ha='center', va='top', fontsize=8.5)
ax3 = fig.add_subplot(gs[2]); gl, gr, z = draw(ax3, x_dark, "Dark spot (first dark stripe)")
ax3.set_xlim(-0.2, 1.2); ax3.set_ylim(-0.75, 0.75)
ax3.text(0.5, -0.36, "left group goes out, right group\ncomes straight back: total "
         f"{abs(z):.2f}, chance {abs(z)**2:.0f}", ha='center', va='top', fontsize=8.5)
fig.text(0.70, 0.04, "Thin hands: one per strip of a slit (8 per slit), added tip to tail; dashed black = left slit, grey = right slit.\n"
         "Bold arrows (drawn just below): the total of each group.", ha='center', fontsize=8.5)
fig.savefig(out, dpi=150, bbox_inches='tight'); print("saved", os.path.abspath(out))
