# Figure a-buildup: single-particle detections building up two-slit stripes.
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12})
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "figures", "a-buildup.png")
rng = np.random.default_rng(1)
u = np.linspace(-1.5, 1.5, 200001)
P = np.sinc(u)**2*np.cos(4*np.pi*u)**2          # sinc = sin(pi u)/(pi u)
cdf = np.cumsum(P); cdf /= cdf[-1]
fig, axes = plt.subplots(1, 4, figsize=(7, 4), sharey=True)
for ax, N in zip(axes, [10, 100, 1000, 10000]):
    x = np.interp(rng.random(N), cdf, u)           # inverse-CDF sampling from P(u)
    y = rng.random(N)                               # vertical position: visibility only
    ax.scatter(x, y, s=4 if N <= 100 else (1 if N == 1000 else 0.25), c="black", marker=".", linewidths=0)
    ax.set_title(f"N = {N}"); ax.set_xlim(-1.5, 1.5); ax.set_ylim(0, 1)
    ax.set_xticks([-1, 0, 1]); ax.set_yticks([]); ax.set_facecolor("white")
    ax.set_xlabel("screen position u\n(arb. units)", fontsize=10)
fig.suptitle("Two slits, one particle at a time: each lands as a single dot; stripes appear only after many", fontsize=10)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
