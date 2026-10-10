# Exit amplitudes (z+1)/2 and (z-1)/2 traced in the complex plane as phi goes round; table points marked.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-model-1.png'
plt.rcParams.update({'font.size': 10.5})
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
amp = lambda p: H @ np.diag([np.exp(1j*p), 1]) @ H @ np.array([1, 0])
phi = np.linspace(0, 2*np.pi, 400); A = np.array([amp(p) for p in phi])
fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.plot(A[:, 0].real, A[:, 0].imag, 'k-', lw=2.2, label='exit-1 amplitude (z+1)/2')
ax.plot(A[:, 1].real, A[:, 1].imag, 'k--', lw=1.4, label='exit-2 amplitude (z−1)/2')
off1 = {0: (6, 4), 60: (6, -14), 90: (-6, 8), 120: (4, -18), 180: (6, 4)}
off2 = {0: (-52, 4), 60: (4, -14), 90: (-6, 8), 120: (-60, -4), 180: (-52, -14)}
for d, mk in zip([0, 60, 90, 120, 180], ['o', 's', '^', 'D', 'v']):
    u, v = amp(np.radians(d))
    ax.plot(u.real, u.imag, mk, color='k', ms=7); ax.plot(v.real, v.imag, mk, mfc='white', mec='k', ms=7)
    ax.annotate(f'{d}°: P₁={abs(u)**2:.2f}', (u.real, u.imag), xytext=off1[d], textcoords='offset points', fontsize=8.5)
    ax.annotate(f'P₂={abs(v)**2:.2f}', (v.real, v.imag), xytext=off2[d], textcoords='offset points', fontsize=8.5)
ax.plot(0, 0, 'k+', ms=12)
ax.set_aspect('equal'); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-0.62, 0.68); ax.grid(alpha=0.3)
ax.set_xlabel('real part of amplitude'); ax.set_ylabel('imaginary part')
ax.legend(loc='lower center', fontsize=9, ncol=2)
ax.set_title('Chance = squared distance from the origin (+); the two always sum to 1', fontsize=10)
fig.tight_layout(); fig.savefig(out, dpi=150); print('saved', out)
