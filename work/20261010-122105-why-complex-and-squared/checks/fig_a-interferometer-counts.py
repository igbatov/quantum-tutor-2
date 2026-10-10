# Computes the ideal Mach-Zehnder exit fractions from H P(phi) H acting on (1,0).
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-interferometer-counts.png'
plt.rcParams.update({'font.size': 11})
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
phi = np.linspace(0, 4*np.pi, 801)
amps = np.array([H @ np.diag([np.exp(1j*p), 1]) @ H @ [1, 0] for p in phi])
P1, P2 = abs(amps[:, 0])**2, abs(amps[:, 1])**2
blk = np.array([abs(H @ (np.diag([np.exp(1j*p), 1]) @ H @ [1, 0] * [1, 0]))**2 for p in phi])
fig = plt.figure(figsize=(7.5, 5.5))
ax = fig.add_axes([0.10, 0.17, 0.86, 0.54])
ax.plot(phi, P1, 'k-', lw=2.6, label='exit 1')
ax.plot(phi, P2, 'k-', lw=1.0, label='exit 2')
ax.plot(phi, P1+P2, 'k--', lw=1.4, label='exit 1 + exit 2')
ax.plot(phi, blk[:, 0], 'k:', lw=1.8, label='either exit, arm 2 blocked')
pts = [(0, 1), (np.pi, 0), (2*np.pi, 1), (3*np.pi, 0)]
ax.plot([p for p, _ in pts], [v for _, v in pts], 'o', ms=15, mfc='none', mec='k', mew=1.8)
ax.annotate('hollow circles: the only two values one real\nnumber per arm allows (plate factor +1 or −1)',
            xy=(np.pi, 0.0), xytext=(np.pi*1.25, 0.42), fontsize=9.5,
            arrowprops=dict(arrowstyle='->', lw=0.9), bbox=dict(fc='white', ec='0.6'))
ticks = np.arange(5)*np.pi
ax.set_xticks(ticks); ax.set_xticklabels(['0\n(0)', 'π\n(λ/2)', '2π\n(λ)', '3π\n(3λ/2)', '4π\n(2λ)'])
ax.set_xlim(-0.3, 4*np.pi+0.3); ax.set_ylim(-0.03, 1.05)
ax.set_xlabel('plate phase φ (extra optical path in brackets)')
ax.set_ylabel('fraction of photons')
ax.legend(loc='upper left', bbox_to_anchor=(0.0, 1.47), ncol=2, fontsize=9.5, frameon=False)
ax.grid(alpha=0.3)
# clock-hand diagrams (computed: arm amplitudes after the plate)
for i, ph in enumerate([0, np.pi/2, np.pi]):
    a = fig.add_axes([0.62 + i*0.12, 0.74, 0.11, 0.21]); a.set_aspect('equal'); a.axis('off')
    arms = np.diag([np.exp(1j*ph), 1]) @ H @ [1, 0]
    a.add_patch(plt.Circle((0, 0), 1/np.sqrt(2), fill=False, ls=':', lw=0.6, color='0.5'))
    a.annotate('', xy=(arms[1].real, arms[1].imag), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=1.0, color='k'))
    a.annotate('', xy=(arms[0].real, arms[0].imag), xytext=(0, 0), arrowprops=dict(arrowstyle='->', lw=2.6, color='k'))
    a.set_xlim(-0.85, 0.85); a.set_ylim(-0.85, 0.85)
    p1 = abs((H @ arms)[0])**2
    a.set_title(f'φ = {["0", "π/2", "π"][i]}\nexit 1: {p1:.1f}', fontsize=9)
fig.text(0.62, 0.722, 'thick hand: arm 1 (turned by φ); thin: arm 2', fontsize=8.5)
fig.text(0.10, 0.012, 'Ideal: lossless optics, 50/50 splitters, perfect detectors, one wavelength.', fontsize=8.5, style='italic')
fig.savefig(out, dpi=150); print('saved', out)
