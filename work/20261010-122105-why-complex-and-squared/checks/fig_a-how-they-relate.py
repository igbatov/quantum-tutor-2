# Left: p-total |u|^p + |v|^p of the interferometer output U(phi)(1,0) for p = 1, 2, 3, 4.
# Right: definite-energy state: the hand e^{-iEt/hbar} turns (Re, Im oscillate) at frequency E/h
# while |psi|^2 stays fixed.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-how-they-relate.png'
plt.rcParams.update({'font.size': 10.5})
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
phi = np.linspace(0, 2*np.pi, 400)
A = np.array([H @ np.diag([np.exp(1j*p), 1]) @ H @ [1, 0] for p in phi])
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.0))
for p, st, lw in ((1, ':', 1.6), (2, '-', 2.6), (3, '-.', 1.2), (4, '--', 1.4)):
    a.plot(phi, np.sum(abs(A)**p, axis=1), 'k', ls=st, lw=lw, label=f'p = {p}')
a.set_xticks(np.arange(5)*np.pi/2); a.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
a.set_xlabel('plate phase φ (rad)'); a.set_ylabel('|amp₁|^p + |amp₂|^p')
a.set_title('Same device, one photon in: only p = 2 keeps the total at 1', fontsize=10); a.legend(fontsize=9); a.grid(alpha=0.3)
t = np.linspace(0, 2, 400)       # time in units of h/E (one full turn per unit)
psi = np.exp(-1j*2*np.pi*t)
b.plot(t, psi.real, 'k-', lw=1.4, label='real part of the hand')
b.plot(t, psi.imag, 'k--', lw=1.4, label='imaginary part')
b.plot(t, abs(psi)**2, 'k-', lw=2.8, label='squared length |ψ|²')
b.set_xlabel('time t (units of h/E)'); b.set_ylabel('value (dimensionless)'); b.set_ylim(-1.2, 1.75)
b.set_title('Definite energy E: the hand turns at frequency E/h,\nthe chance never changes', fontsize=10)
b.legend(fontsize=8.5, loc='upper center', ncol=3); b.grid(alpha=0.3)
fig.tight_layout(); fig.savefig(out, dpi=150); print('saved', out)
