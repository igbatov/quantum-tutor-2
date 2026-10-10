import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.linalg import expm

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-how-they-relate.png")
plt.rcParams.update({"font.size": 10})
# Left: one hand turning at E/hbar (the i). Right: the two-level state's lengths (|c1|, |c2|) under the
# ammonia equation, against the curves |c1|^p + |c2|^p = 1 for p = 1, 2, 3, 4 (the 2).
fig, (axL, axR) = plt.subplots(1, 2, figsize=(9, 4.3))
t = np.linspace(0, 2 * np.pi, 400)
z = np.exp(-1j * t)
axL.plot(z.real, z.imag, color="C0", lw=2)
for s in np.linspace(0, 2 * np.pi, 8, endpoint=False):
    w = np.exp(-1j * s)
    axL.annotate("", xy=(w.real, w.imag), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="0.45", lw=1))
axL.annotate("", xy=(np.cos(-0.6), np.sin(-0.6)), xytext=(np.cos(-0.2), np.sin(-0.2)),
             arrowprops=dict(arrowstyle="->", color="C3", lw=2))
axL.text(1.12, -0.55, "turns\nclockwise\nat E/ħ", color="C3", fontsize=8)
axL.set_aspect("equal"); axL.set_xlim(-1.4, 1.6); axL.set_ylim(-1.3, 1.3)
axL.set_xlabel("real part"); axL.set_ylabel("imaginary part")
axL.set_title("The i: a hand e^(−iEt/ħ) keeps its length", fontsize=9.5)

H = np.array([[0, -1], [-1, 0]], complex)
th = np.linspace(0, np.pi / 2, 300)
C = np.array([expm(-1j * H * s) @ np.array([1, 0]) for s in th])
a1, a2 = np.abs(C[:, 0]), np.abs(C[:, 1])
x = np.linspace(0, 1, 600)
for p, ls in [(1, "-."), (3, ":"), (4, "--")]:
    axR.plot(x, (1 - x**p)**(1 / p), ls, color="0.4", lw=1.3)
    xx = {1: 0.35, 3: 0.93, 4: 0.97}[p]; yy = {1: 0.65, 3: 0.58, 4: 0.72}[p]
    axR.text(xx + 0.02, yy, f"p={p}", fontsize=8, color="0.3")
axR.plot(a1, a2, "-", color="C0", lw=3.5, alpha=0.6, label="state's lengths (|c₁|, |c₂|) as time runs")
axR.plot(x, np.sqrt(1 - x**2), "-", color="k", lw=1, label="|c₁|² + |c₂|² = 1 (p = 2)")
axR.set_aspect("equal"); axR.set_xlim(0, 1.15); axR.set_ylim(0, 1.15)
axR.set_xlabel("|c₁|"); axR.set_ylabel("|c₂|")
axR.set_title("The 2: the motion stays on the p = 2 curve only", fontsize=9.5)
axR.legend(fontsize=7.5, loc="upper right")
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT), "; max deviation of |c1|^2+|c2|^2 from 1:", np.abs(a1**2 + a2**2 - 1).max())
