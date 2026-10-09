import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out = os.path.join(os.path.dirname(__file__), "..", "figures", "b-rules-out.png")
plt.rcParams.update({"font.size": 10})
u = np.linspace(-3, 3, 2001)
env = np.sinc(u/4)**2
I = lambda V, s=0.0, amp=1.0: amp*env*(1+V*np.cos(2*np.pi*(u-s)))/2
fig, ax = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
ax[0].plot(u, I(1), "k-", lw=1.8, label="full strength"); ax[0].plot(u, I(1, amp=0.25), "k--", lw=1.8, label="quarter strength")
ax[0].set_title("(a) damped classical wave:\ndimmer, dark stripes still reach zero"); ax[0].legend(fontsize=8, loc="upper right")
for V, ls, lab in [(1, "-", "d = 0: V = 1"), (0.64, "-.", "d = λ/4: V = 0.64"), (0, ":", "d = λ/2: V = 0")]:
    ax[1].plot(u, I(np.sinc(2*{1: 0, 0.64: 0.25, 0: 0.5}[V])), ls=ls, color="k", lw=1.8, label=lab)
ax[1].plot(u, env/2, color="r", ls="--", lw=1, label="one-path chances added")
ax[1].set_title("(b) model: one photon scattered"); ax[1].legend(fontsize=8, loc="upper right")
rng = np.random.default_rng(3)
for s in rng.uniform(-0.25, 0.25, 5):
    ax[2].plot(u, I(1, s), color="0.7", lw=0.8)
avg = np.mean([I(1, s) for s in np.linspace(-0.25, 0.25, 2001)], axis=0)
ax[2].plot(u, avg, "k-", lw=2.2, label="average of shifted patterns\nV = sin(π/2)/(π/2) ≈ 0.64")
ax[2].plot([], [], color="0.7", lw=0.8, label="five random shifts (±0.25 spacing)")
ax[2].set_title("(c) random kicks, d = λ/4"); ax[2].legend(fontsize=8, loc="upper right")
for a in ax: a.set_xlabel("screen position (stripe spacings)"); a.set_xlim(-3, 3); a.set_ylim(0, 1.6)
ax[0].set_ylabel("arrival chance (relative)")
fig.text(0.01, 0.005, "(a) fails: atom count unchanged while stripes fade.  (c) = (b) middle for photon scattering; kick-free tags (1998) tell them apart.", fontsize=8)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(out, dpi=150); print("saved", out)
