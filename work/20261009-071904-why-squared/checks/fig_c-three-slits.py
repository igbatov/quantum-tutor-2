# Figure c-three-slits: ideal far-screen (Fraunhofer) patterns for three slits, width a, spacing d = 4a.
import os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, '..', 'figures', 'c-three-slits.png')
lam, a = 1.0, 1.0; d = 4*a
u = np.linspace(-3, 3, 6001)              # screen position in units of the A+B stripe spacing
s = u*lam/d                               # sin(theta)
env = np.sinc(a*s/lam)                    # single-slit amplitude, 1 at centre
amp = {k: env*np.exp(-2j*np.pi*x*s/lam) for k,x in {'A':-d,'B':0.0,'C':d}.items()}
T = {'A':amp['A'],'B':amp['B'],'C':amp['C'],'A+B':amp['A']+amp['B'],'B+C':amp['B']+amp['C'],
     'A+C':amp['A']+amp['C'],'A+B+C':amp['A']+amp['B']+amp['C']}
def chance(k,p): return np.abs(T[k])**p
def leftover(p):
    return (chance('A+B+C',p)-chance('A+B',p)-chance('B+C',p)-chance('A+C',p)
            +chance('A',p)+chance('B',p)+chance('C',p))
plt.rcParams.update({'font.size': 11})
fig = plt.figure(figsize=(10,11.5))
gs = GridSpec(4, 3, figure=fig, hspace=0.55, wspace=0.12)
ax1 = fig.add_subplot(gs[0,:])
ax1.plot(u, chance('A',2), 'k-', lw=3.5, label='A alone')
ax1.plot(u, chance('B',2), color='tab:orange', ls='--', lw=2.2, label='B alone')
ax1.plot(u, chance('C',2), color='tab:blue', ls=':', lw=2.2, label='C alone')
ax1.set_title('Row 1. One slit open (square rule): the three curves coincide')
ax1.legend(fontsize=9, loc='upper right', ncol=3); ax1.set_ylim(0,1.15)
ax2 = fig.add_subplot(gs[1,:], sharex=ax1)
ax2.plot(u, chance('A+B',2), 'k-', lw=2.2, label='A+B (same as B+C)')
ax2.plot(u, chance('B+C',2), color='tab:orange', ls='--', lw=1.5, label='B+C')
ax2.plot(u, chance('A+C',2), color='tab:blue', ls=':', lw=1.8, label='A+C')
ax2.set_title('Row 2. Two slits open (square rule): A+B = B+C, stripes 1 unit apart; A+C, 1/2 unit apart')
ax2.legend(fontsize=9, loc='upper right', ncol=3); ax2.set_ylim(0,4.9)
ax3 = fig.add_subplot(gs[2,:], sharex=ax1)
ax3.plot(u, chance('A+B+C',2), 'k-', lw=1.8)
ax3.set_title('Row 3. All three open (square rule): tall stripes, faint stripe between, zeros at 1/3 and 2/3')
ax3.annotate('faint stripe\nheight %.2f' % chance('A+B+C',2)[np.argmin(abs(u-0.5))],
             xy=(0.5, 1.05), xytext=(0.5, 2.6), ha='center',
             arrowprops=dict(arrowstyle='->'), fontsize=8.5)
ax3.set_ylim(0,10.5)
for ax in (ax1,ax2,ax3):
    ax.set_ylabel('chance\n(one slit at centre = 1)', fontsize=9.5)
    ax.set_xlim(-3,3); ax.grid(alpha=0.3)
    plt.setp(ax.get_xticklabels(), visible=True)
ax3.set_xlabel('position across the screen (units of the A+B stripe spacing)')
rules = [(2,'chance = size²  (square rule)'),(1,'chance = size  (plain size)'),(3,'chance = size³  (cube)')]
Ls = [leftover(p) for p,_ in rules]
lim = 1.1*max(np.abs(L).max() for L in Ls)
for k,((p,name),L) in enumerate(zip(rules,Ls)):
    ax = fig.add_subplot(gs[3,k])
    ax.axhline(0, color='0.5', lw=0.8)
    ax.plot(u, L, 'k-', lw=1.6)
    if p == 1:
        zs = np.arange(-9,10)/3
        ax.plot(zs, np.zeros_like(zs), 'o', mfc='white', mec='k', ms=4)
    ax.set_ylim(-lim, lim); ax.set_xlim(-3,3); ax.grid(alpha=0.3)
    ax.set_title(name, fontsize=10)
    m = np.abs(L).max()
    ax.text(0.03, 0.96, ('max |leftover| = %.1e' % m) if m < 1e-6 else ('max |leftover| = %.2f' % m),
            transform=ax.transAxes, va='top', fontsize=9, bbox=dict(facecolor='white', edgecolor='0.6'))
    if k == 0: ax.set_ylabel('leftover\n(one slit at centre = 1)', fontsize=9.5)
    else: ax.set_yticklabels([])
    ax.set_xlabel('position (A+B stripe units)', fontsize=9.5)
fig.text(0.5, 0.245, 'Row 4. Leftover = (A+B+C) − (A+B) − (B+C) − (A+C) + A + B + C, under three rules '
         '(open circles: plain-size zeros, every 1/3 unit)', ha='center', fontsize=10.5)
fig.subplots_adjust(left=0.1, right=0.98, top=0.96, bottom=0.05)
fig.savefig(out, dpi=150)
print("saved", os.path.abspath(out), " max leftovers:", [float(np.abs(L).max()) for L in Ls])
