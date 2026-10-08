# Figure a-rules-out (section "What this rules out"): what each classical picture predicts vs what is seen.
# Panels 1-2: classical balls, Monte Carlo of straight-line flight (nearly parallel beam, small angular
#   spread) through two slits of width a = d/4, screen at L = 4 d. Panel 2 adds edge bounces: balls passing
#   within eps of a slit edge get a random deflection. Each ball uses one slit, so both-open = sum of one-slit.
# Panels 3-4: ideal far-screen wave pattern, d = 4a: I(X) ~ cos^2(pi X) sinc^2(X/4), X in stripe spacings.
#   Panel 3: classical wave, continuous intensity (full and dimmed x0.1: same shape, fainter everywhere).
#   Panel 4: quantum: same pattern built from single dots (random samples), plus one-slit curve.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-rules-out.png')
rng = np.random.default_rng(2024)
plt.rcParams.update({'font.size': 11})

# ---------- classical balls ----------
d, a, L, th0 = 1.0, 0.25, 4.0, 0.02
eps, thb = 0.07, 0.15          # edge zone width, max bounce angle (rad)
def balls(c, n, bounce):
    y = c + a*(rng.random(n) - 0.5)                  # where the ball crosses the slit
    th = th0*(2*rng.random(n) - 1)                   # small spread of the incoming beam
    if bounce:
        near = (np.abs(y - (c - a/2)) < eps) | (np.abs(y - (c + a/2)) < eps)
        th = th + np.where(near, thb*(2*rng.random(n) - 1), 0.0)
    return y + L*np.tan(th)
xb = np.linspace(-2.2, 2.2, 221); xc = 0.5*(xb[1:] + xb[:-1]); w = xb[1] - xb[0]
N = 400000
def dens(x):
    h, _ = np.histogram(x, xb); return h/(N*w)
cls = {}
for bounce in (False, True):
    xl, xr = balls(-d/2, N, bounce), balls(d/2, N, bounce)
    cls[bounce] = (dens(xl), dens(xr), np.concatenate([xl[:400], xr[:400]]))

# ---------- waves ----------
X = np.linspace(-6, 6, 6001)
Ib = np.cos(np.pi*X)**2*np.sinc(X/4)**2          # peak 1
I1 = 0.25*np.sinc(X/4)**2                         # one slit, same units
Xf = np.linspace(-8, 8, 160001); Pf = np.cos(np.pi*Xf)**2*np.sinc(Xf/4)**2
cdf = np.cumsum(Pf); cdf /= cdf[-1]
dots = np.interp(rng.random(3000), cdf, Xf)

fig = plt.figure(figsize=(11, 7.6))
outer = fig.add_gridspec(2, 2, hspace=0.42, wspace=0.16)
def panel(k, title):
    g = outer[k].subgridspec(2, 1, height_ratios=[1, 2.3], hspace=0.08)
    s, p = fig.add_subplot(g[0]), fig.add_subplot(g[1])
    s.set_title(title, fontsize=11.5, loc='left')
    s.set_xticks([]); s.set_yticks([]); s.set_ylim(0, 1)
    p.axhline(0, color='0.7', lw=0.6); p.set_yticks([])
    return s, p

# panel 1: straight-flying balls
for k, bounce, title in [(0, False, "(a) Tiny balls flying straight"), (1, True, "(b) Balls that also bounce off the slit edges")]:
    s, p = panel(k, title)
    dl, dr, sample = cls[bounce]
    M = (dl + dr).max()
    s.scatter(sample, rng.random(sample.size), s=1.2, c='k', linewidths=0)
    s.set_xlim(-2.2, 2.2); s.set_ylabel("screen", fontsize=9)
    p.plot(xc, (dl + dr)/M, 'k-', lw=2.0, label="both slits open")
    p.plot(xc, dl/M, color='0.45', lw=1.0, ls='--', label="one slit open (left or right)")
    p.plot(xc, dr/M, color='0.45', lw=1.0, ls='--')
    for c in (-d/2, d/2):
        p.add_patch(plt.Rectangle((c - a/2, -0.17), a, 0.07, color='k', clip_on=False))
    p.set_xlim(-2.2, 2.2); p.set_ylim(-0.2, 1.55)
    p.set_xlabel("position on screen (units of slit separation d)", fontsize=9.5)
    p.set_ylabel("relative number of hits", fontsize=9.5)
    p.text(1.25, -0.135, "black bars: slits", fontsize=8, va='center')
    if not bounce:
        p.text(2.1, 1.5, "two bands, one behind each slit;\neach band is just that slit's hits", ha='right', va='top', fontsize=8.5)
        p.legend(loc='upper left', fontsize=8, frameon=False)
    else:
        p.text(0, 1.5, "wider bands that can merge; each ball uses one slit,\nso both-open = sum of the one-slit curves:\nopening a slit only adds hits", ha='center', va='top', fontsize=8.5)

# panel 3: classical wave
s, p = panel(2, "(c) A classical wave (like water)")
s.imshow(np.tile(Ib, (2, 1)), extent=(-6, 6, 0.5, 1), aspect='auto', cmap='Greys', vmin=0, vmax=1)
s.imshow(np.tile(0.1*Ib, (2, 1)), extent=(-6, 6, 0, 0.5), aspect='auto', cmap='Greys', vmin=0, vmax=1)
s.axhline(0.5, color='0.5', lw=0.6); s.set_xlim(-6, 6)
s.text(6.15, 0.75, "full", fontsize=8, va='center'); s.text(6.15, 0.25, "dimmed", fontsize=8, va='center')
p.plot(X, Ib, 'k-', lw=2.0, label="full source")
p.plot(X, 0.1*Ib, 'k--', lw=1.2, label="source dimmed 10×")
p.set_xlim(-6, 6); p.set_ylim(-0.05, 1.42)
p.set_xlabel("position on screen (units of the stripe spacing)", fontsize=9.5)
p.set_ylabel("intensity", fontsize=9.5)
p.legend(loc='upper left', fontsize=8, frameon=False)
p.text(5.8, 1.37, "stripes, but the energy arrives\ncontinuously, spread over the\nwhole pattern; dimmed: same\nshape, fainter, never one dot", ha='right', va='top', fontsize=8.5)

# panel 4: what is seen
s, p = panel(3, "(d) What is seen with electrons")
s.scatter(dots[:30], 0.57 + 0.36*rng.random(30), s=6, c='k', linewidths=0)
s.scatter(dots, 0.5*rng.random(3000), s=0.6, c='k', linewidths=0)
s.axhline(0.5, color='0.5', lw=0.6); s.set_xlim(-6, 6)
s.text(6.15, 0.75, "30", fontsize=8, va='center'); s.text(6.15, 0.25, "3,000", fontsize=8, va='center')
s.text(6.15, 1.0, "electrons:", fontsize=8, va='bottom')
p.plot(X, Ib, 'k-', lw=2.0, label="both slits open")
p.plot(X, I1, color='0.45', lw=1.0, label="one slit open")
p.set_xlim(-6, 6); p.set_ylim(-0.05, 1.42)
p.set_xlabel("position on screen (units of the stripe spacing)", fontsize=9.5)
p.set_ylabel("relative chance", fontsize=9.5)
p.legend(loc='upper left', fontsize=8, frameon=False)
p.text(5.8, 1.37, "whole dots, one at a time,\nbuilding stripes; at the dark\nstripes near the middle, one slit\ngives hits, two slits give none", ha='right', va='top', fontsize=8.5)

fig.savefig(out, dpi=150, bbox_inches='tight'); print("saved", os.path.abspath(out))
# sanity numbers
for bounce in (False, True):
    dl, dr, _ = cls[bounce]; tot = dl + dr; M = tot.max()
    print("bounce" if bounce else "straight", "min of both-open between bands / peak:", round(tot[np.abs(xc) < 0.05].min()/M, 3),
          " both >= each one-slit everywhere:", bool(np.all(tot >= dl) and np.all(tot >= dr)))
print("wave min/peak at dark stripe X=0.5:", np.cos(np.pi*0.5)**2, " one-slit there:", round(0.25*np.sinc(0.5/4)**2, 3))
