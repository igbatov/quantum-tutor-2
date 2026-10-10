import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-what-this-rules-out.png")
plt.rcParams.update({"font.size": 10})
fig, (axL, axR) = plt.subplots(1, 2, figsize=(9, 4), gridspec_kw={"width_ratios": [1, 1.5]})
th_marks = np.array([0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi])
labels = ["0", "π/4", "π/2", "3π/4", "π"]
circ = np.linspace(0, 2 * np.pi, 400)
axL.plot(np.cos(circ), np.sin(circ), color="0.75", lw=1)
axL.axhline(0, color="0.6", lw=0.6); axL.axvline(0, color="0.6", lw=0.6)
for th, lab in zip(th_marks, labels):
    z = np.exp(-1j * th)
    axL.annotate("", xy=(z.real, z.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", lw=1.4, color="C0"))
    axL.text(1.12 * z.real, 1.12 * z.imag, lab, ha="center", va="center", fontsize=8, color="C0")
    axL.plot(np.cos(th), -1.45, "s", color="C1", ms=6)
    axL.text(np.cos(th), -1.68, lab, ha="center", fontsize=7, color="C1")
axL.plot([-1, 1], [-1.45, -1.45], color="C1", lw=1)
axL.text(0, -1.27, "one real number cos θ: slides through 0", ha="center", fontsize=7.5, color="C1")
axL.text(0, 1.3, "hand e^(−iθ): turns, length stays 1", ha="center", fontsize=7.5, color="C0")
axL.set_xlim(-1.5, 1.5); axL.set_ylim(-1.85, 1.5); axL.set_aspect("equal")
axL.set_xlabel("real part"); axL.set_ylabel("imaginary part")
axL.set_title("θ = Et/ħ at the table's five times", fontsize=9.5)

th = np.linspace(0, 2 * np.pi, 1000)
axR.plot(th, np.ones_like(th), "-", lw=2.4, label="hand: squared length |e^(−iθ)|² = 1")
axR.plot(th, np.cos(th)**2, "--", lw=1.8, label="real number: cos²θ = ½ + ½cos 2θ")
axR.plot(th, np.cos(th), ":", lw=1.4, color="0.4", label="the real number cos θ itself")
axR.plot(th_marks, np.cos(th_marks)**2, "o", color="C1")
axR.set_xticks(np.arange(0, 2 * np.pi + 0.01, np.pi / 2)); axR.set_xticklabels(["0", "π/2", "π", "3π/2", "2π"])
axR.set_xlabel("θ = Et/ħ (one period of the frequency E/h)")
axR.set_ylabel("value / \"chance of up\"")
axR.set_ylim(-1.1, 1.45)
axR.legend(fontsize=7.8, loc="lower left", ncol=1)
axR.set_title("cos²θ hits 0 twice per period; the hand's length never changes", fontsize=9.5)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT))
