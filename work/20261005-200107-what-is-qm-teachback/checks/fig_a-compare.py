# Figure a-compare: one slit vs both slits (route recorded / not recorded).
import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.size": 12})
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "..", "figures", "a-compare.png")
u = np.linspace(-1, 1, 4001)
S = np.sinc(u)**2
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(u, S, color="tab:blue", ls=":", lw=2.2, label="one slit open")
ax.plot(u, 2*S, color="tab:green", ls="--", lw=2, label="both slits open, route recorded")
ax.plot(u, 4*S*np.cos(4*np.pi*u)**2, color="black", ls="-", lw=1.4, label="both slits open, nothing recorded")
u0 = 0.125; s0 = np.sinc(u0)**2
ax.axvline(u0, color="gray", ls="--", lw=1)
ax.plot([u0], [s0], marker="o", ms=8, mfc="white", mec="tab:blue", mew=2, zorder=5)
ax.plot([u0], [0], marker="s", ms=8, color="black", zorder=5)
ax.annotate(f"one slit: {s0:.2f}", (u0, s0), xytext=(0.3, 2.6), fontsize=10,
            arrowprops=dict(arrowstyle="->", color="tab:blue"))
ax.annotate("both, unrecorded: 0", (u0, 0), xytext=(0.38, 2.05), fontsize=10,
            arrowprops=dict(arrowstyle="->", color="black"))
ax.set_xlabel("screen position u (arb. units)")
ax.set_ylabel("relative chance of landing (arb. units)")
ax.set_xlim(-1, 1); ax.set_ylim(0, 4.3)
ax.legend(fontsize=9, loc="upper left")
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
