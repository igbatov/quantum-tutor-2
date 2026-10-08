# Figure a-interpretations: four panels, one per view (Copenhagen-style, many-worlds, pilot-wave,
# objective collapse). Pilot-wave panel is COMPUTED: Bohmian trajectories for two Gaussian-shaped slit
# openings, paraxial (1D transverse position x, distance from slits z = v*t plays the role of time),
# free Schroedinger evolution (hbar = m = 1), guidance law dx/dt = Im(psi_x / psi).
# The other three panels are schematic. Checks printed: no trajectory crosses the centre line; final
# positions follow |psi|^2 (KS distance); trajectories bunch into the bright stripes.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib.patches import FancyArrowPatch, Ellipse
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-interpretations.png')

# ---------------- pilot-wave computation ----------------
sig, x0s, T = 0.25, (-2.0, 2.0), 6.0          # Gaussian slit openings: rms width 0.25, centres +-2 (d = 4)
d = x0s[1] - x0s[0]
def psi_and_dpsi(x, t):
    s = 1 + 1j*t/(2*sig**2)
    p = np.zeros_like(x, dtype=complex); dp = np.zeros_like(x, dtype=complex)
    for c in x0s:
        g = (2*np.pi*sig**2)**-0.25 / np.sqrt(s) * np.exp(-(x-c)**2/(4*sig**2*s))
        p += g; dp += -(x-c)/(2*sig**2*s)*g
    return p, dp
def vel(x, t):
    p, dp = psi_and_dpsi(x, t); return np.imag(dp/p)
def run(xstart, dt=2.5e-4):
    n = int(round(T/dt)); x = xstart.astype(float).copy(); ts = [0.0]; xs = [x.copy()]
    for k in range(n):
        t = k*dt
        k1 = vel(x, t); k2 = vel(x+dt/2*k1, t+dt/2); k3 = vel(x+dt/2*k2, t+dt/2); k4 = vel(x+dt*k3, t+dt)
        x = x + dt/6*(k1+2*k2+2*k3+k4)
        if (k+1) % 40 == 0: ts.append((k+1)*dt); xs.append(x.copy())
    return np.array(ts), np.array(xs)

# trajectories to draw: equal-probability starting points in each opening
nd = 18
q = norm.ppf((np.arange(nd)+0.5)/nd)
start_draw = np.concatenate([x0s[0]+sig*q, x0s[1]+sig*q])
ts, xs = run(start_draw)

# --- checks (many trajectories) ---
nc = 1500
qc = norm.ppf((np.arange(nc)+0.5)/nc)
start_chk = np.concatenate([x0s[0]+sig*qc, x0s[1]+sig*qc])
_, xc = run(start_chk, dt=2.5e-4)
crossed = np.sum(np.sign(xc[-1]) != np.sign(start_chk)) + np.sum(np.any(np.sign(xc) != np.sign(start_chk), axis=0))
xg = np.linspace(-60, 60, 120001); Pf = abs(psi_and_dpsi(xg, T)[0])**2
cdf = np.cumsum(Pf); cdf /= cdf[-1]
fin = np.sort(xc[-1]); emp = (np.arange(len(fin))+0.5)/len(fin)
ks = np.max(np.abs(np.interp(fin, xg, cdf) - emp))
# bright-stripe bunching: fraction of final positions in the brighter half of each stripe period
spacing = 2*np.pi*T/d * (1 + (2*sig**2/T)**2)   # exact fringe spacing for Gaussian beams: phase diff = x*d*t/(4 sig^4 |s|^2)
ph = np.mod(xc[-1]/spacing + 0.5, 1.0)           # bright stripe centres at integer multiples of spacing
in_bright = np.mean(np.abs(ph-0.5) < 0.25)
print(f"trajectories crossing centre line: {crossed} (of {len(start_chk)})")
print(f"KS distance final positions vs |psi|^2: {ks:.4f}")
print(f"fringe spacing {spacing:.3f}; fraction of arrivals in the bright half of each stripe period: {in_bright:.3f} (uniform would be 0.5)")
P_at_nodes = abs(psi_and_dpsi(np.array([spacing/2, 1.5*spacing]), T)[0])**2 / Pf.max()
print(f"|psi|^2 at first two dark lines / peak: {P_at_nodes}")
phg = np.mod(xg/spacing + 0.5, 1.0); exp_bright = np.sum(Pf[np.abs(phg-0.5) < 0.25])/np.sum(Pf)
print(f"|psi|^2 weight in bright halves: {exp_bright:.3f} (cos^2 fringes give 1/2+1/pi = {0.5+1/np.pi:.3f})")
print("PASS" if (crossed == 0 and ks < 0.01 and abs(in_bright-exp_bright) < 0.01 and in_bright > 0.75) else "FAIL")
grw_years = 1/1e-16/(365.25*24*3600)
print(f"GRW original rate 1e-16 /s per particle -> once per {grw_years:.2e} years")

# ---------------- figure ----------------
plt.rcParams.update({'font.size': 11})
fig, axs = plt.subplots(2, 2, figsize=(12, 8.6))
def blank(ax):
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color('0.6')
def arrow(ax, a, b, **kw):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=14, color=kw.get('color', 'k'), lw=kw.get('lw', 1.4),
                                 connectionstyle=kw.get('cs', 'arc3')))
def box(ax, x, y, txt, fs=10, fc='white', ec='k', ls='-'):
    ax.text(x, y, txt, ha='center', va='center', fontsize=fs,
            bbox=dict(boxstyle='round,pad=0.45', fc=fc, ec=ec, ls=ls, lw=1.1))
def screen(ax, x, y0, y1, w=0.35):
    ax.add_patch(plt.Rectangle((x, y0), w, y1-y0, fc='0.92', ec='k', lw=1.0))

# (a) Copenhagen-style
ax = axs[0, 0]; blank(ax)
ax.set_title("Copenhagen-style  (schematic)", fontsize=12)
box(ax, 1.65, 6.0, "wave function\n= a tool for\npredicting")
arrow(ax, (3.15, 6.0), (3.85, 6.0))
xx = np.linspace(-2.2, 2.2, 400); pp = np.cos(np.pi*xx)**2*np.sinc(xx/4)**2
ax.fill_between(4.0 + 2.2*(xx+2.2)/4.4, 5.4, 5.4+1.3*pp, color='0.7', lw=0)
ax.plot([4.0, 6.2], [5.4, 5.4], color='k', lw=0.8)
ax.text(5.1, 7.25, "chances for\neach spot", fontsize=10, ha='center')
arrow(ax, (6.45, 6.0), (7.35, 6.0))
screen(ax, 7.55, 3.6, 8.4)
ax.plot([7.725], [6.4], 'ko', ms=7)
ax.text(8.15, 6.4, "result:\none dot", fontsize=10, va='center')
ax.text(5.0, 2.0, "\"Which slit?\" has no answer the theory gives.\nA record changes what can be predicted.",
        fontsize=9.5, ha='center', va='center', style='italic')
# (b) Many-worlds
ax = axs[0, 1]; blank(ax)
ax.set_title("Many-worlds  (schematic)", fontsize=12)
box(ax, 1.55, 5.0, "electron\nreaches\nscreen", fs=9.5)
ys = [8.8, 7.1, 5.4, 3.7, 2.0]; dots = [0.25, 0.4, 0.5, 0.62, 0.75]
for yb, fx in zip(ys, dots):
    arrow(ax, (2.85, 5.0), (5.15, yb), cs='arc3,rad=0.0', color='0.35', lw=1.1)
    ax.add_patch(plt.Rectangle((5.3, yb-0.55), 2.2, 1.1, fc='0.92', ec='k', lw=0.9))
    ax.plot([5.3 + 2.2*fx], [yb], 'ko', ms=6)
ax.text(7.75, 4.6, "every branch\nhas one dot,\nin a different\nplace", fontsize=9.5, va='center')
ax.annotate("we are in one\nbranch and see\none dot", xy=(7.5, 8.8), xytext=(7.75, 7.8), fontsize=9.5, va='center',
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.text(4.2, 0.45, "electron and screen form one joint state with a branch\nfor each spot; nothing collapses, all branches remain", fontsize=9.5, ha='center', style='italic')

# (c) Pilot-wave (computed)
ax = axs[1, 0]
ax.set_title("Pilot-wave  (computed paths)", fontsize=12)
for i in range(xs.shape[1]):
    ax.plot(ts, xs[:, i], color='k', lw=0.7)
ax.axhline(0, color='0.45', ls='--', lw=1.0)
# wall with two openings at z = 0
W = 34
for (y0, y1) in [(-W, -2.5), (-1.5, 1.5), (2.5, W)]:
    ax.add_patch(plt.Rectangle((-0.12, y0), 0.12, y1-y0, color='k', clip_on=True))
# screen pattern at z = T, drawn sideways
P = Pf/Pf.max()
ax.fill_betweenx(xg, T+0.05, T+0.05+1.1*P, color='0.7', lw=0)
ax.plot([T+0.05, T+0.05], [-W, W], color='k', lw=1.0)
ax.text(T+0.6, 25, "chance at\nthe screen", fontsize=9, ha='center')
ins = ax.inset_axes([0.07, 0.60, 0.29, 0.30])
for i in range(xs.shape[1]):
    ins.plot(ts, xs[:, i], color='k', lw=0.6)
ins.axhline(0, color='0.45', ls='--', lw=0.9)
for (y0, y1) in [(-9, -2.5), (-1.5, 1.5), (2.5, 9)]:
    ins.add_patch(plt.Rectangle((-0.03, y0), 0.03, y1-y0, color='k'))
ins.set_xlim(-0.05, 0.8); ins.set_ylim(-7, 7); ins.tick_params(labelsize=7.5)
ins.set_yticks([]); ins.set_xticks([]); ins.set_title("zoom: first 0.8 units", fontsize=8.5, pad=2)
ax.annotate("paths bunch\ninto bright stripes", xy=(T-0.05, spacing), xytext=(3.0, 25), fontsize=9,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate("each path goes through one slit,\non a bent line, and never crosses\nthe dashed centre line", xy=(1.0, -5.5), xytext=(1.2, -27), fontsize=9,
            arrowprops=dict(arrowstyle='->', lw=0.8))
ax.set_xlim(-0.3, T+1.3); ax.set_ylim(-W, W)
ax.set_xlabel("distance from the slits (arbitrary units)")
ax.set_ylabel("position across (slit spacing = 4)")

# (d) Objective collapse
ax = axs[1, 1]; blank(ax)
ax.set_title("Objective collapse  (schematic)", fontsize=12)
for (y0, y1) in [(2.0, 4.4), (4.8, 5.2), (5.6, 8.0)]:
    ax.add_patch(plt.Rectangle((0.6, y0), 0.25, y1-y0, color='k'))
for r in (0.8, 1.6, 2.4, 3.2, 4.0, 4.8, 5.6):
    for yc in (4.6, 5.4):
        tmax = min(1.0, np.arcsin(min(1.0, 2.4/r)))
        th = np.linspace(-tmax, tmax, 100)
        ax.plot(0.85 + r*np.cos(th), yc + r*np.sin(th), color='0.6', lw=0.9)
ax.text(3.6, 9.0, "the ripple is real and stays spread out:\none electron almost never localizes in flight",
        fontsize=9.3, ha='center', va='center')
screen(ax, 7.0, 2.0, 8.0, w=0.5)
ax.plot([7.25], [6.2], 'ko', ms=8)
ax.text(7.75, 6.2, "localized\nhere", fontsize=9.5, ha='left', va='center')
ax.text(7.75, 3.4, "screen: huge\nnumbers of\nparticles set\nmoving", fontsize=9, ha='left', va='center')
ax.text(3.6, 0.95, "with that many particles involved, the random\nlocalization happens almost at once \u2192 one dot",
        fontsize=9, ha='center', va='center', style='italic')
fig.tight_layout(h_pad=1.8, w_pad=1.5); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
