# Schematic Mach-Zehnder with amplitudes computed from H and P(phi) at every stage.
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from pathlib import Path
out = Path(__file__).resolve().parent.parent/'figures'/'a-setup.png'
plt.rcParams.update({'font.size': 10.5})
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
phi = np.pi/3; z = np.exp(1j*phi)
s0 = np.array([1, 0]); s1 = H @ s0; s2 = np.diag([z, 1]) @ s1; s3 = H @ s2
assert np.allclose(s1, [1/np.sqrt(2)]*2) and np.allclose(s3, [(z+1)/2, (z-1)/2])
fig, ax = plt.subplots(figsize=(7.5, 4.6)); ax.set_aspect('equal'); ax.axis('off')
bs = lambda x, y: ax.plot([x-0.25, x+0.25], [y-0.25, y+0.25], color='0.3', lw=4, alpha=0.6)
mir = lambda x, y: ax.plot([x-0.25, x+0.25], [y-0.25, y+0.25], 'k', lw=5)
ax.annotate('', xy=(0, 0), xytext=(-1.6, 0), arrowprops=dict(arrowstyle='->', lw=1.5))
ax.add_patch(plt.Rectangle((-2.3, -0.25), 0.7, 0.5, fc='white', ec='k')); ax.text(-1.95, 0, 'heralded\nsource', ha='center', va='center', fontsize=8)
ax.plot([0, 3], [0, 0], 'k', lw=1.5); ax.plot([0, 0], [0, 2], 'k--', lw=1.5)
ax.plot([3, 3], [0, 2], 'k', lw=1.5); ax.plot([0, 3], [2, 2], 'k--', lw=1.5)
bs(0, 0); bs(3, 2); mir(3, 0); mir(0, 2)
ax.add_patch(plt.Rectangle((1.35, -0.3), 0.18, 0.6, angle=0, fc='0.85', ec='k', hatch='///'))
ax.annotate('tiltable glass plate:\nturns arm-1 hand by φ', xy=(1.45, -0.3), xytext=(0.9, -1.2), fontsize=9, ha='center', arrowprops=dict(arrowstyle='->', lw=0.8))
ax.plot([3, 4.3], [2, 2], 'k', lw=1.5); ax.plot([3, 3], [2, 3.0], 'k', lw=1.5)
ax.add_patch(plt.Rectangle((4.3, 1.75), 0.35, 0.5, fc='k')); ax.add_patch(plt.Rectangle((2.75, 3.0), 0.5, 0.35, fc='k'))
ax.text(4.75, 2, 'exit 1\namplitude (z+1)/2\nchance cos²(φ/2)', va='center', fontsize=9)
ax.text(3.35, 3.2, 'exit 2: amplitude (z−1)/2, chance sin²(φ/2)', va='center', fontsize=9)
ax.text(0.15, 0.5, 'BS 1 (H)', fontsize=9); ax.text(2.0, 2.45, 'BS 2 (H)', fontsize=9)
ax.text(3.25, -0.35, 'mirror', fontsize=9); ax.text(-0.95, 2.25, 'mirror', fontsize=9)
ax.text(1.9, 0.15, 'arm 1: z/√2', fontsize=9); ax.text(-0.95, 1.0, 'arm 2:\n1/√2', fontsize=9)
ax.text(-2.3, -1.65, f'Computed example, φ = 60°: arm chances {abs(s2[0])**2:.2f} and {abs(s2[1])**2:.2f}; '
        f'exit 1 {abs(s3[0])**2:.2f}, exit 2 {abs(s3[1])**2:.2f}.  z = e^(iφ).  Ideal lossless optics, equal arms.', fontsize=8.5)
ax.set_xlim(-2.4, 6.6); ax.set_ylim(-1.8, 3.5)
fig.savefig(out, dpi=150, bbox_inches='tight'); print('saved', out)
