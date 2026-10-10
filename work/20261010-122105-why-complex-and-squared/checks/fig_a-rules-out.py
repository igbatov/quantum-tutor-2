# Exit-1 fraction vs phi predicted by each picture (left) and the two-detector coincidence ratio
# alpha = P(both)/(P1 P2) at a single splitter (right): classical intensity gives alpha >= 1 by
# Cauchy-Schwarz (computed for steady and fluctuating pulses), one photon gives 0.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-rules-out.png'
plt.rcParams.update({'font.size': 10.5})
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
phi = np.linspace(0, 2*np.pi, 400)
qm = np.array([abs((H @ np.diag([np.exp(1j*p), 1]) @ H @ [1, 0])[0])**2 for p in phi])
balls = 0.5*0.5 + 0.5*0.5; chances = 0.25 + 0.25
fig, (a, b) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw=dict(width_ratios=[2.2, 1]))
a.plot(phi, qm, 'k-', lw=2.4, label='complex pair per arm (quantum) = classical wave energy fraction')
a.plot(phi, np.full_like(phi, balls), 'k--', lw=1.4, label='tiny balls; chances only (both 1/2 at every tilt)')
rr = [(0, 1), (np.pi, 0), (2*np.pi, 1)]
a.plot([p for p, _ in rr], [v for _, v in rr], 's', ms=10, mfc='none', mec='k', mew=1.6, label='one real number per arm: only these settings')
a.set_xticks(np.arange(5)*np.pi/2); a.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
a.set_xlabel('plate phase φ (rad)'); a.set_ylabel('fraction of photons at exit 1'); a.set_ylim(-0.05, 1.45)
a.legend(fontsize=8.3, loc='upper center'); a.grid(alpha=0.3); a.set_title('(b) the smooth sweep', fontsize=10)
rng = np.random.default_rng(0)
def alpha_classical(I):
    p1 = p2 = I/2*1e-3  # weak detection, each detector sees half the intensity
    return np.mean(p1*p2)/(np.mean(p1)*np.mean(p2))
steady = alpha_classical(np.ones(200000)); fluct = alpha_classical(rng.exponential(size=200000))
vals = [steady, fluct, 0.0]
b.bar([0, 1, 2], vals, color=['white', 'white', 'k'], edgecolor='k', hatch='', width=0.6)
b.axhline(1, color='k', ls=':', lw=1); b.text(2.35, 1.03, 'classical\nminimum', fontsize=8, ha='right')
b.set_xticks([0, 1, 2]); b.set_xticklabels(['steady\nclassical\npulse', 'fluctuating\nclassical\npulse', 'one\nphoton\n(ideal)'], fontsize=8.5)
for i, v in enumerate(vals): b.text(i, v+0.04, f'{v:.2f}', ha='center', fontsize=9)
b.set_ylabel('coincidences / (P₁ P₂)'); b.set_ylim(0, 2.4); b.set_title('(a) whole arrivals', fontsize=10)
fig.tight_layout(); fig.savefig(out, dpi=150); print('saved', out, vals)
