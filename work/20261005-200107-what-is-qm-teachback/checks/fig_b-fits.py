import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 12
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'b-fits.png')
x = np.linspace(0, 1, 500)
fig, ax = plt.subplots(figsize=(7, 4.6))
offsets = {1: 7.5, 2: 5.0, 3: 2.5}
labels = {1: 'pattern 1: one hump', 2: 'pattern 2: two humps', 3: 'pattern 3: three humps'}
for n, off in offsets.items():
    y = np.sin(n*np.pi*x)
    ax.plot(x, off + y, color='black', lw=2.2)
    ax.plot(x, off - y, color='gray', lw=0.8, alpha=0.6)
    ax.text(1.06, off, labels[n], va='center', fontsize=11)
off = 0.0
y = np.sin(2.5*np.pi*x)
ax.plot(x, off + y, 'r--', lw=2)
ax.plot([1], [off + y[-1]], marker='x', color='red', ms=14, mew=3)
ax.text(1.06, off + 0.2, "doesn't fit\n(end is not at rest)", va='center', color='red', fontsize=11)
# clamps
for off in list(offsets.values()) + [0.0]:
    for xe in (0, 1):
        ax.add_patch(plt.Rectangle((xe - 0.025, off - 0.35), 0.05, 0.7, color='#333333', zorder=5))
ax.set_xlim(-0.08, 1.55); ax.set_ylim(-1.5, 9)
ax.axis('off')
ax.set_title('Only whole numbers of half-waves fit between fixed ends\n(more humps = higher note; for an electron, higher energy)', fontsize=12)
fig.tight_layout(); fig.savefig(out, dpi=150); print('saved', os.path.abspath(out))
