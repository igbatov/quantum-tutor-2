import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "a-buildup.png")
P = lambda X: np.sinc(X/4)**2*np.cos(np.pi*X)**2   # max 1 at X=0
rng = np.random.default_rng(12345)
def sample(n):
    xs = []
    while len(xs) < n:
        X = rng.uniform(-6, 6, 4*n); keep = X[rng.uniform(0, 1, X.size) < P(X)]; xs.extend(keep.tolist())
    return np.array(xs[:n])
N = 10000; X = sample(N); Y = rng.uniform(0, 1, N)
plt.rcParams.update({"font.size": 12})
fig, axes = plt.subplots(1, 4, figsize=(12, 4), sharey=True)
for ax, n, s in zip(axes, [10, 100, 1000, 10000], [14, 6, 1.5, 0.25]):
    ax.scatter(X[:n], Y[:n], s=s, c="black", marker="o", linewidths=0)
    ax.set_xlim(-6, 6); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"{n:,} electrons"); ax.set_xlabel("position on screen"); ax.set_facecolor("white")
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
