# Figure a-setup: side-view schematic of the two-slit experiment (section "The set-up").
# Schematic geometry, not to scale. The dots on the screen are a real random sample from the
# far-screen pattern used in the other A figures (slit separation d = 4 x slit width a):
#   P(X) ~ cos^2(pi X) * sinc^2(X/4), X in units of the stripe spacing.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-setup.png')
plt.rcParams.update({'font.size': 11})
fig, ax = plt.subplots(figsize=(9, 4.6))
ax.set_xlim(-0.3, 10.6); ax.set_ylim(-2.75, 3.0); ax.set_aspect('equal'); ax.axis('off')

# source
ax.add_patch(FancyBboxPatch((0.25, -0.45), 1.0, 0.9, boxstyle='round,pad=0.05', fc='0.85', ec='k', lw=1.2))
ax.text(0.75, 0, "electron\nsource", ha='center', va='center', fontsize=9.5)
ax.annotate('', xy=(2.35, 0), xytext=(1.4, 0), arrowprops=dict(arrowstyle='-|>', color='k', lw=1.2))
ax.text(1.85, -0.15, "one at\na time", ha='center', va='top', fontsize=8.5)

# wall with two slits (drawn with d = 4a: slit width a = 0.25, centres at +-0.5)
xw, tw, a, d = 2.6, 0.18, 0.25, 1.0
edges = [-2.2, -d/2 - a/2, -d/2 + a/2, d/2 - a/2, d/2 + a/2, 2.2]
for y0, y1 in [(edges[0], edges[1]), (edges[2], edges[3]), (edges[4], edges[5])]:
    ax.add_patch(Rectangle((xw, y0), tw, y1 - y0, fc='0.25', ec='k', lw=0.8))
ax.text(xw + tw/2, 2.35, "wall with\ntwo narrow slits", ha='center', va='bottom', fontsize=9.5)

# slit width label (upper slit)
xl = xw - 0.12
ax.annotate('', xy=(xl, d/2 + a/2), xytext=(xl, d/2 - a/2), arrowprops=dict(arrowstyle='<->', lw=0.9, shrinkA=0, shrinkB=0))
ax.annotate("slit width a", xy=(xl - 0.03, d/2), xytext=(1.0, 1.35), ha='center', va='center', fontsize=9,
            arrowprops=dict(arrowstyle='-', lw=0.6, color='0.4'))
# slit separation label (centre to centre), to the right of the wall
xr = xw + tw + 0.15
ax.annotate('', xy=(xr, d/2), xytext=(xr, -d/2), arrowprops=dict(arrowstyle='<->', lw=0.9, shrinkA=0, shrinkB=0))
ax.plot([xw + tw, xr + 0.05], [d/2, d/2], color='0.5', lw=0.6, ls=':')
ax.plot([xw + tw, xr + 0.05], [-d/2, -d/2], color='0.5', lw=0.6, ls=':')
ax.text(xr + 0.08, -0.05, "slit separation d\n(centre to centre)", ha='left', va='center', fontsize=9)

# distance with a break
yb = -1.75
ax.plot([xw + tw, 5.3], [yb, yb], color='0.3', lw=1.0)
ax.plot([5.75, 8.6], [yb, yb], color='0.3', lw=1.0)
for xs in (5.3, 5.75):
    ax.plot([xs - 0.08, xs + 0.08], [yb - 0.16, yb + 0.16], color='0.3', lw=1.2)
ax.annotate('', xy=(8.6, yb), xytext=(8.45, yb), arrowprops=dict(arrowstyle='-|>', color='0.3', lw=1.0))
ax.text(5.5, yb - 0.25, "screen far away (not to scale)", ha='center', va='top', fontsize=9.5)

# screen and dots: sample from the far-screen pattern over the part the drawn screen covers (+-5 stripe spacings)
xs_scr = 8.7
ax.add_patch(Rectangle((xs_scr, -2.2), 0.14, 4.4, fc='0.9', ec='k', lw=1.0))
ax.text(xs_scr + 0.07, 2.35, "screen", ha='center', va='bottom', fontsize=9.5)
rng = np.random.default_rng(7)
X = np.linspace(-5, 5, 100001); P = np.cos(np.pi*X)**2*np.sinc(X/4)**2
cdf = np.cumsum(P); cdf /= cdf[-1]
n = 14
Xs = np.interp(rng.random(n), cdf, X)
ys = Xs * (2.1/5)                       # +-5 stripe spacings -> drawn screen height
ax.scatter(xs_scr + 0.07 + rng.uniform(-0.035, 0.035, n), ys, s=14, c='k', zorder=5)
ax.annotate("each electron:\none dot", xy=(xs_scr + 0.12, ys[np.argmax(ys)]), xytext=(9.05, 1.55),
            fontsize=8.5, ha='left', va='center', arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(9.0, -0.05, f"first {n}\nelectrons", ha='left', va='center', fontsize=8.5, color='0.3')

ax.set_title("The two-slit set-up, seen from the side (schematic)", fontsize=12)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
