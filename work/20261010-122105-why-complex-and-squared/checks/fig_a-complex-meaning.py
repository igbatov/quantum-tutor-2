# Left: J (quarter-wave delay) as a real 2x2 matrix acting on a hand; J^2 = -1.
# Right: network score: complex QM value computed (6 sqrt2) vs the literature real-amplitude bound.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-complex-meaning.png'
plt.rcParams.update({'font.size': 10.5})
J = np.array([[0, -1], [1, 0]]); v0 = np.array([0.8, 0.35]); v1 = J @ v0; v2 = J @ v1
assert np.allclose(v2, -v0)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw=dict(width_ratios=[1.2, 1]))
for v, st, lab in [(v0, '-', 'hand (x, y)'), (v1, '--', 'after quarter-wave delay: J(x,y) = (−y, x)'), (v2, ':', 'after half-wave delay: J²(x,y) = (−x, −y)')]:
    a.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=2, ls=st))
    a.plot([], [], 'k', ls=st, lw=2, label=lab)
a.add_patch(plt.Circle((0, 0), np.linalg.norm(v0), fill=False, ls=':', color='0.6'))
a.set_aspect('equal'); a.set_xlim(-1.1, 1.1); a.set_ylim(-1.1, 1.1); a.grid(alpha=0.3)
a.set_xlabel('x (first real number of the pair)'); a.set_ylabel('y (second real number)')
a.legend(fontsize=8, loc='lower left'); a.set_title('i as a laboratory operation: J² = −1', fontsize=10)
vals = [7.66, 6*np.sqrt(2)]
b.bar([0, 1], vals, color=['white', '0.3'], edgecolor='k', hatch='//', width=0.55)
for i, v in enumerate(vals): b.text(i, v+0.2, f'{v:.2f}', ha='center')
b.set_xticks([0, 1]); b.set_xticklabels(['real amplitudes\n+ product rule\n(bound, Renou 2021)', 'complex QM\n6√2 (computed)'], fontsize=8.5)
b.set_ylim(0, 9.8); b.set_ylabel('network Bell score (dimensionless)')
b.set_title('Two independent sources, three parties', fontsize=10)
fig.tight_layout(); fig.savefig(out, dpi=150); print('saved', out)
