# Tip-to-tail addition of the two route-group hands A2 (fixed) and A1 (turned by phi) at exit 1.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-model-2.png'
plt.rcParams.update({'font.size': 10.5})
a = (1/np.sqrt(2))**2   # two splitters, each shrinks by 1/sqrt2
degs = [0, 60, 90, 120, 180]
fig, axs = plt.subplots(1, 5, figsize=(10, 2.55))
for ax, d in zip(axs, degs):
    A2 = a; A1 = a*np.exp(1j*np.radians(d)); tot = A2 + A1
    kw = dict(arrowprops=dict(arrowstyle='->', lw=2.2))
    ax.annotate('', xy=(A2.real, A2.imag), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=1.2))
    ax.annotate('', xy=(tot.real, tot.imag), xytext=(A2.real, A2.imag), **kw)
    if abs(tot) > 1e-9:
        ax.annotate('', xy=(tot.real, tot.imag), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=1.2, ls='--'))
    ax.set_xlim(-0.1, 1.1); ax.set_ylim(-0.1, 0.6); ax.set_aspect('equal'); ax.grid(alpha=0.3)
    ax.set_title(f'φ = {d}°\nlength {abs(tot):.3f}, squared {abs(tot)**2:.2f}', fontsize=9.5)
    ax.set_xlabel('real part'); ax.tick_params(labelsize=8)
axs[0].set_ylabel('imaginary part')
fig.text(0.5, 0.005, 'thin: A₂ (arm 2, fixed, length 1/2)   thick: A₁ (arm 1, length 1/2, turned by φ)   dashed: total',
         ha='center', fontsize=9)
fig.tight_layout(rect=(0, 0.07, 1, 1)); fig.savefig(out, dpi=150); print('saved', out)
