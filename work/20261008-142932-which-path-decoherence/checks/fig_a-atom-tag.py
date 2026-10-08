import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import FancyArrowPatch, Rectangle
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-atom-tag.png"
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1, 1.25]})
ax = axL; ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
ax.set_title("Set-up (schematic, not to scale)")
ax.annotate("", xy=(4, 8.7), xytext=(4, 9.8), arrowprops=dict(arrowstyle="->", lw=1.5))
ax.text(4.2, 9.5, "falling atoms", fontsize=9)
ax.add_patch(Rectangle((1, 7.6), 8, 0.5, color="orange", alpha=0.5)); ax.text(6.0, 7.75, "splitting light pulse", fontsize=9)
ax.add_patch(Rectangle((1, 4.4), 8, 0.5, color="orange", alpha=0.5)); ax.text(6.0, 4.55, "redirecting light pulse", fontsize=9)
for y, lab in [(8.5, "microwave pulse 1"), (7.05, "microwave pulse 2")]:
    xs = np.linspace(6.2, 7.4, 100); ax.plot(xs, y+0.12*np.sin(2*np.pi*(xs-6.2)/0.3), color="purple")
    ax.text(7.5, y-0.1, lab, fontsize=8, color="purple")
# straight path (solid) and deflected path (dashed)
ax.plot([4, 4], [7.6, 4.4], "k-", lw=2); ax.text(1.3, 6.0, "straight:\ninternal state A", fontsize=8)
ax.plot([4, 5.6], [7.6, 4.9], "k--", lw=2); ax.text(5.8, 6.0, "deflected:\ninternal state B", fontsize=8)
ax.plot([5.6, 4.6], [4.4, 1.6], "k--", lw=2); ax.plot([4, 4.6], [4.4, 1.6], "k-", lw=2)
ax.fill_between([3.4, 5.6], 1.2, 2.0, color="gray", alpha=0.25); ax.text(5.8, 1.5, "parts spread\nand overlap", fontsize=8)
ax.plot([0.8, 9.2], [0.9, 0.9], "k-", lw=1); ax.text(1.0, 0.25, "positions recorded (far below)", fontsize=9)
ax = axR
X = np.linspace(-4, 4, 3000); E = np.exp(-X**2/(2*2.0**2))
ax.plot(X, E*(1+np.cos(2*np.pi*X)), "k-", lw=2, label="microwave pulses off (stripes)")
ax.plot(X, E, "--", color="tab:red", lw=2.2, label="microwave pulses on (tag written)\n= two one-path chances added")
ax.set_xlabel("position X (units of the stripe spacing)"); ax.set_ylabel("relative chance of finding an atom")
ax.set_title("Idealized two-path far-screen pattern (computed)"); ax.set_ylim(0, 2.25); ax.legend(loc="upper right", fontsize=8.5)
ax.text(-3.9, 2.08, "equal areas: same number of atoms", fontsize=8.5)
fig.text(0.01, 0.005, "Right panel: idealized pattern with a smooth Gaussian envelope, not the experiment's data; the real stripes had lower contrast than drawn.\n"
         "Tag-on curve = exactly the two one-path chances added. Only difference between the runs: two microwave pulses, whose photons carry ~1/100,000 of the optical photons' momentum.",
         fontsize=8)
fig.tight_layout(rect=(0, 0.08, 1, 1)); fig.savefig(OUT, dpi=150); print(OUT)
