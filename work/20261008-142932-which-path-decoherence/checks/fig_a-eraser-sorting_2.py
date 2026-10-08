import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-eraser-sorting.png"
# Range widened from -4..4 to -8..8 so the one-slit side bands (4.7% of the centre) are visible.
XM = 8
S = lambda X: np.sinc(X/4)**2
rng = np.random.default_rng(7)
# rejection-sample 2000 dots from S on [-XM, XM]
pts = []
while len(pts) < 2000:
    x = rng.uniform(-XM, XM, 20000); keep = x[rng.uniform(0, 1, x.size) < S(x)]; pts.extend(keep.tolist())
xd = np.array(pts[:2000]); grp = rng.uniform(0, 1, xd.size) < (1+np.cos(2*np.pi*xd))/2
X = np.linspace(-XM, XM, 4000)
fig, axs = plt.subplots(3, 1, figsize=(8, 7.2), sharex=True)
ax = axs[0]; ax.scatter(xd, rng.uniform(0, 0.3, xd.size), s=2, color="k")
ax.plot(X, 0.35+0.6*S(X), "k--", label="two one-slit chances added")
ax.set_yticks([]); ax.set_title("all pairs (nothing sorted): 2,000 dots, no stripes"); ax.legend(loc="upper right", fontsize=8)
ax.annotate("faint one-slit side bands\n(not two-slit stripes)", xy=(-5.7, 0.38), xytext=(-7.9, 0.75), fontsize=8, arrowprops=dict(arrowstyle="->"))
ax = axs[1]
ax.scatter(xd[grp], rng.uniform(0.55, 0.95, grp.sum()), s=2, color="tab:blue", marker="o", label="partner passed +45°")
ax.scatter(xd[~grp], rng.uniform(0.05, 0.45, (~grp).sum()), s=4, color="tab:orange", marker="x", lw=0.6, label="partner passed −45°")
ax.set_yticks([]); ax.set_title("the same 2,000 dots, sorted by the partner's result (no dot moved)")
ax.legend(loc="upper right", fontsize=8, markerscale=3)
ax = axs[2]
ax.plot(X, S(X)*(1+np.cos(2*np.pi*X))/2, "-", color="tab:blue", lw=1.6, label="+45° group")
ax.plot(X, S(X)*(1-np.cos(2*np.pi*X))/2, "-", color="tab:orange", lw=1.6, dashes=(4, 1.5), label="−45° group")
ax.plot(X, S(X), "k--", lw=1.4, label="sum = two one-slit chances added")
ax.set_ylabel("relative chance"); ax.set_xlabel("position X on the far screen (units of the stripe spacing), d = 4a")
ax.legend(loc="upper right", fontsize=8)
fig.text(0.01, 0.005, "Sorting moves no dot; the two groups' stripes are half a spacing apart and add up to the dashed curve. Where each group sits relative to the\n"
         "untagged stripes: drawn here with the +45° group peaking at X = 0; with the real plate settings both groups sit a quarter spacing off this drawing\n"
         "(separation and sum unchanged; see check_A_07_2). Idealized: perfect plates, polarizer, source; far screen; d = 4a.", fontsize=7.5)
fig.tight_layout(rect=(0, 0.065, 1, 1)); fig.savefig(OUT, dpi=150); print(OUT)
