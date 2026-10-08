import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-dots-buildup.png')
rng = np.random.default_rng(12345)
X = np.linspace(-8, 8, 160001); P = np.cos(np.pi*X)**2*np.sinc(X/4)**2
cdf = np.cumsum(P); cdf /= cdf[-1]
N = 10000
xs = np.interp(rng.random(N), cdf, X); ys = rng.random(N)
fig, axs = plt.subplots(1, 4, figsize=(11, 3.8), sharey=True)
for ax, n, s in zip(axs, (10, 100, 1000, 10000), (14, 6, 1.6, 0.35)):
    ax.scatter(xs[:n], ys[:n], s=s, c='k', marker='o', linewidths=0)
    ax.set_xlim(-8, 8); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"{n:,} electrons", fontsize=12); ax.set_xlabel("position on screen", fontsize=11)
    ax.set_facecolor('white')
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
