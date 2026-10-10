# Unit curves |x|^p+|y|^p=1 and the rotated points (cos t, sin t); p-totals computed.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-pnorm-circles.png'
plt.rcParams.update({'font.size': 11})
fig, ax = plt.subplots(figsize=(9.0, 6.4))
t = np.linspace(0, 2*np.pi, 2001)
for p, st, lw in ((1, ':', 1.5), (2, '-', 2.6), (4, '--', 1.3)):
    r = (abs(np.cos(t))**p + abs(np.sin(t))**p)**(-1/p)
    ax.plot(r*np.cos(t), r*np.sin(t), 'k', ls=st, lw=lw)
lab = dict(fontsize=9.5, arrowprops=dict(arrowstyle='->', lw=0.8), bbox=dict(fc='white', ec='none', pad=1))
ff = dict(textcoords='figure fraction')
def onc(p, deg):
    t = np.radians(deg); r = (abs(np.cos(t))**p + abs(np.sin(t))**p)**(-1/p); return (r*np.cos(t), r*np.sin(t))
ax.annotate('p = 1 (diamond, dotted)', xy=onc(1, -40), xytext=(0.745, 0.26), **ff, **lab)
ax.annotate('p = 2 (circle, bold)', xy=onc(2, -50), xytext=(0.745, 0.19), **ff, **lab)
ax.annotate('p = 4 (rounded square, dashed)', xy=onc(4, -60), xytext=(0.745, 0.12), **ff, **lab)
ang = np.radians([0, 15, 30, 45, 60, 75, 90])
ax.plot(np.cos(ang), np.sin(ang), 'ko', ms=6)
ax.annotate('all at exit 1', xy=(1, 0), xytext=(0.30, 0.10), fontsize=9.5, arrowprops=dict(arrowstyle='->', lw=0.8))
ax.annotate('all at exit 2', xy=(0, 1), xytext=(-0.75, 1.07), fontsize=9.5, arrowprops=dict(arrowstyle='->', lw=0.8))
q = np.sqrt(0.5); tot = {p: 2*q**p for p in (1, 2, 4)}
ax.annotate(f'p-totals of (0.707, 0.707):\np=1: 0.707+0.707 = {tot[1]:.2f}\np=2: 0.50+0.50 = {tot[2]:.2f}\np=4: 0.25+0.25 = {tot[4]:.2f}',
            xy=(q, q), xytext=(0.745, 0.40), textcoords='figure fraction', fontsize=9, bbox=dict(fc='white', ec='0.6'),
            arrowprops=dict(arrowstyle='->', lw=0.8))
arc = np.linspace(0.04, np.pi/2-0.04, 100)
ax.plot(0.88*np.cos(arc), 0.88*np.sin(arc), 'k-', lw=0.8)
ax.annotate('', xy=(0.88*np.cos(arc[-1]), 0.88*np.sin(arc[-1])), xytext=(0.88*np.cos(arc[-3]), 0.88*np.sin(arc[-3])),
            arrowprops=dict(arrowstyle='->', lw=0.9))
ax.text(0.5, 1.22, 'arc: rotation by 0° to 90°, a lossless gradual mixer for p = 2. The interferometer U(φ),\n'
        'φ from 0 to π, gives exit amplitudes of sizes (cos φ/2, sin φ/2): the same arc in sizes.',
        fontsize=8.5, ha='center', transform=ax.transData)
ax.set_xlim(-1.15, 1.15); ax.set_ylim(-1.15, 1.15); ax.set_aspect('equal'); ax.grid(alpha=0.3)
ax.set_xlabel('x: amplitude at exit 1 (real, dimensionless)'); ax.set_ylabel('y: amplitude at exit 2 (real, dimensionless)')
fig.subplots_adjust(top=0.86, left=0.04, right=0.72)
fig.savefig(out, dpi=150); print('saved', out)
