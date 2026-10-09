import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-leaked-tag.png"
N = np.arange(0, 61)
fig, ax = plt.subplots(figsize=(7.5, 4.6))
ax.semilogy(N, 0.9**N, "k-o", ms=3, label="per-particle overlap p = 0.9")
ax.semilogy(N, 0.5**N, "--s", color="tab:red", ms=3, label="per-particle overlap p = 0.5")
ax.axhline(0.01, color="gray", lw=0.8); ax.text(42, 0.012, "stripes 1% strong", color="gray")
ax.plot(50, 0.9**50, "o", ms=10, mfc="none", mec="tab:blue", mew=2)
ax.annotate(f"N = 50: {0.9**50:.3f}", xy=(50, 0.9**50), xytext=(30, 1e-4), arrowprops=dict(arrowstyle="->"))
ax.set_ylim(1e-6, 1.5); ax.set_xlim(0, 60)
ax.set_xlabel("N, particles that have each scattered off the molecule\n(independently, same overlap p)"); ax.set_ylabel("stripe strength = p^N")
ax.legend(loc="upper right")
fig.text(0.01, 0.005, "Model: overlaps multiply (each particle same overlap p, particles independent). \nA gas atom whose wavelength is far shorter than the path separation has p near 0 (one collision suffices);\n"
         "very long-wavelength light has p near 1. \nSorting the stripes back out would need every one of the N particles measured along its own halfway direction.", fontsize=7.8)
fig.tight_layout(rect=(0, 0.14, 1, 1)); fig.savefig(OUT, dpi=150); print(OUT)
