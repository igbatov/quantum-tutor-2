import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figures', 'c-string-fits.png')
plt.rcParams.update({'font.size': 10})
fig = plt.figure(figsize=(9, 5.2))
gs = fig.add_gridspec(4, 2, width_ratios=[1.15, 1], hspace=0.55, wspace=0.25, left=0.04, right=0.98, top=0.9, bottom=0.2)
x = np.linspace(0, 1, 400)
labels = {1: 'fits: 1 half-wave', 2: 'fits: 2 half-waves', 3: 'fits: 3 half-waves'}
for i, n in enumerate([1, 2, 3, 2.5]):
    ax = fig.add_subplot(gs[i, 0])
    y = np.sin(n*np.pi*x)
    if n != 2.5:
        ax.plot(x, -y, color='0.75', lw=1.2, ls='--')
        ax.plot(x, y, 'k-', lw=2)
        ax.set_title(labels[n], fontsize=10, loc='left')
    else:
        ax.plot(x, y, color='red', lw=2, ls='-.')
        ax.plot([1], [np.sin(n*np.pi)], 'x', color='red', ms=14, mew=3)
        ax.set_title('2.5 half-waves: does not end at the fixed point, not allowed', fontsize=10, loc='left', color='darkred')
    ax.plot([0, 1], [0, 0], 'ko', ms=7)
    ax.axhline(0, color='0.85', lw=0.6, zorder=0)
    ax.set_xlim(-0.05, 1.08); ax.set_ylim(-1.35, 1.35)
    ax.set_yticks([]); ax.set_xticks([0, 0.5, 1] if i == 3 else [])
    if i == 3: ax.set_xlabel('position along string (string length = 1)')
    for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
# right panel
for j, (Ls, lab) in enumerate([(1.0, 'string length 1: wavelength 2'), (0.5, 'string length 0.5: wavelength 1, bends more sharply')]):
    ax = fig.add_subplot(gs[2*j:2*j+2, 1]) if j == 0 else fig.add_subplot(gs[2:4, 1])
    xs = np.linspace(0, Ls, 300)
    ax.plot(xs, np.sin(np.pi*xs/Ls), 'k-', lw=2)
    ax.plot([0, Ls], [0, 0], 'ko', ms=7)
    ax.axhline(0, color='0.85', lw=0.6, zorder=0)
    ax.set_xlim(-0.05, 1.08); ax.set_ylim(-0.2, 1.3); ax.set_yticks([])
    ax.set_title(lab, fontsize=10, loc='left')
    if j == 1: ax.set_xlabel('position (same scale in both rows)')
    else: ax.set_xticklabels([])
    for s in ('top', 'right', 'left'): ax.spines[s].set_visible(False)
    if j == 1:
        ax.text(0.58, 0.55, 'half the wavelength:\nhigher note for sound;\nfor an electron wave,\n4x the energy of motion', fontsize=9.5, va='center')
fig.suptitle('Only whole numbers of half-waves fit between fixed ends; less room means sharper bends', fontsize=11.5)
fig.text(0.5, 0.015, 'Analogy with a guitar string only: an electron\'s pattern is three-dimensional, and nothing material is vibrating.\n'
         'Grey dashed curves: the same pattern at the opposite moment of the swing.', ha='center', fontsize=9.5, style='italic')
fig.set_size_inches(9, 5.2)
fig.savefig(out, dpi=150)
print('saved', os.path.abspath(out))
