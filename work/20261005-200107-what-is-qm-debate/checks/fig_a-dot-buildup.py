import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "a-dot-buildup.png")
rng = np.random.default_rng(12345)
P = lambda x: np.cos(np.pi*x)**2 * np.sinc(x/5)**2   # np.sinc(u) = sin(pi u)/(pi u)
def sample(n):
    xs = []
    while len(xs) < n:
        x = rng.uniform(-6, 6, 4*n); u = rng.uniform(0, 1, 4*n)
        xs.extend(x[u < P(x)])
    return np.array(xs[:n])
counts = [10, 100, 1000, 10000]; sizes = [14, 6, 1.5, 0.25]
plt.rcParams.update({"font.size": 12})
fig, axs = plt.subplots(1, 4, figsize=(11, 4))
for ax, n, s in zip(axs, counts, sizes):
    x = sample(n); y = rng.uniform(0, 1, n)
    ax.set_facecolor("black"); ax.scatter(x, y, s=s, c="white", linewidths=0)
    ax.set_xlim(-6, 6); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"{n:,} electrons")
fig.suptitle("Simulated: electrons arriving one at a time", fontsize=14)
fig.text(0.5, 0.025, "Simulated dots drawn from the two-slit pattern that real single-electron experiments record.\n"
         "Each electron lands as one dot; bands appear only as dots accumulate.", ha="center", fontsize=9.5, wrap=True)
fig.tight_layout(rect=[0, 0.1, 1, 0.95]); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
