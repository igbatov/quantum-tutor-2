import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out = os.path.join(os.path.dirname(__file__), "..", "figures", "b-recorders-multiply.png")
plt.rcParams.update({"font.size": 10})
u = np.linspace(-3, 3, 2001); env = np.sinc(u/4)**2
fig, ax = plt.subplots(4, 1, figsize=(7, 7.5), sharex=True)
for k, a in enumerate(ax):
    V = 0.7**k
    a.plot(u, env*(1+V*np.cos(2*np.pi*u))/2, "k-", lw=2, label="seen")
    a.plot(u, env/2, "k--", lw=1.2, label="two one-path chances added")
    a.set_ylim(0, 1.1); a.set_yticks([0, 0.5, 1])
    a.text(-2.95, 0.85, f"{k} scattering event{'s' if k != 1 else ''}:  V = {V:.2f}", fontsize=10, bbox=dict(fc="white", ec="none"))
    a.set_ylabel("chance\n(rel.)")
ax[0].legend(fontsize=8, loc="upper right")
ax[-1].set_xlabel("screen position (stripe spacings), far screen, slit spacing = 4 × slit width")
fig.text(0.01, 0.005, "Overlap 0.7 per event (real, positive); a complex overlap would also shift the stripes (not shown). Total arrivals equal in every panel.", fontsize=8)
fig.tight_layout(rect=(0, 0.03, 1, 1)); fig.savefig(out, dpi=150); print("saved", out)
