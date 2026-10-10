import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.linalg import expm

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-rabi-norms.png")
plt.rcParams.update({"font.size": 10})
# Ammonia-type matrix, A = hbar = 1: integrate the equation itself rather than writing cos/sin by hand
H = np.array([[0, -1], [-1, 0]], dtype=complex)
th = np.linspace(0, 2 * np.pi, 1201)
C = np.array([expm(-1j * H * s) @ np.array([1, 0]) for s in th])
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 5.6), sharex=True)
ax1.plot(th, np.abs(C[:, 0])**2, "-", lw=2, label="|c₁|² (level 1)")
ax1.plot(th, np.abs(C[:, 1])**2, "--", lw=2, label="|c₂|² (level 2)")
ax1.set_ylabel("chance"); ax1.legend(fontsize=8, loc="upper right", ncol=2); ax1.set_ylim(-0.05, 1.25)
ax1.set_title("Chance moves back and forth between the two levels", fontsize=10)
ax2.axhspan(0.98, 1.02, color="0.85")
ax2.text(0.05, 1.04, "every molecule accounted for (total = 1)", fontsize=8, color="0.3")
styles = {1: ("-.", "p = 1 (rises to 1.414)"), 2: ("-", "p = 2 (flat at 1)"),
          3: (":", "p = 3 (dips to 0.707)"), 4: ("--", "p = 4 (dips to 0.5)")}
for p, (ls, lab) in styles.items():
    ax2.plot(th, (np.abs(C)**p).sum(1), ls, lw=2 if p == 2 else 1.5, label=lab)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(0, 2 * np.pi + 0.01, np.pi / 2))
ax2.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
ax2.set_xlabel("θ = At/ħ")
ax2.set_ylabel("|c₁|ᵖ + |c₂|ᵖ")
ax2.legend(fontsize=8, loc="lower right", ncol=2)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT))
