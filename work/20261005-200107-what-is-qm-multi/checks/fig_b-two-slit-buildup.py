import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "figures", "b-two-slit-buildup.png")
rng = np.random.default_rng(12345)

def P_two(u): return np.sinc(u)**2*np.cos(5*np.pi*u)**2   # np.sinc = sin(pi u)/(pi u)
def P_one(u): return np.sinc(u)**2

def sample(P, n, pmax=1.0):
    out = []
    while len(out) < n:
        u = rng.uniform(-2, 2, 4*n); y = rng.uniform(0, pmax, 4*n)
        out.extend(u[y < P(u)].tolist())
    return np.array(out[:n])

panels = [(sample(P_two, 50), "50 electrons", 18),
          (sample(P_two, 5000), "5,000 electrons: stripes", 1.5),
          (sample(P_one, 5000), "5,000 electrons, which slit recorded:\nno stripes", 1.5)]
plt.rcParams.update({"font.size": 11})
fig, axes = plt.subplots(1, 3, figsize=(10.5, 4), sharey=True)
for ax, (x, title, ms) in zip(axes, panels):
    ax.scatter(x, rng.uniform(0, 1, len(x)), s=ms, c="black", linewidths=0)
    ax.set_xlim(-2, 2); ax.set_ylim(0, 1); ax.set_yticks([])
    ax.set_title(title, fontsize=11)
    ax.set_xlabel("position on screen (u, dimensionless)")
    ax.set_facecolor("white")
fig.tight_layout()
fig.savefig(out, dpi=150)
print("saved", os.path.abspath(out))
