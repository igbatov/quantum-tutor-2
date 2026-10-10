import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-model-2-sum-over-paths.png")
plt.rcParams.update({"font.size": 10})
# Routes from source to detector, both a distance D from a middle plane; the route through height y
# has length 2 sqrt(D^2 + y^2) ~ 2D + y^2/D; extra phase 2 pi (y^2/D)/lambda. Use units where
# the extra phase is (pi/2) u^2 with u = y sqrt(4/(lambda D)) (Fresnel variable).
u = np.linspace(-6, 6, 2401)
du = u[1] - u[0]
phase = 0.5 * np.pi * u**2
hands = np.exp(1j * phase) * du
path = np.concatenate([[0], np.cumsum(hands)])
fig, (axL, axR) = plt.subplots(1, 2, figsize=(9.5, 4.2), gridspec_kw={"width_ratios": [1.2, 1]})
axL.plot(u, np.cos(phase), lw=0.9, color="0.3")
axL.axvspan(-1, 1, color="C0", alpha=0.18)
axL.text(0, 1.15, "near the classical\n(straight) route", ha="center", fontsize=8, color="C0")
axL.set_xlabel("route's height y at the middle plane (Fresnel units)")
axL.set_ylabel("real part of the route's hand")
axL.set_ylim(-1.2, 1.45)
axL.set_title("Each route's hand turns by (extra path)/λ × 2π", fontsize=9.5)

mid = (np.abs(u) <= 1)
sel = np.concatenate([[False], mid])
axR.plot(path.real, path.imag, color="0.55", lw=1, label="hands added tip to tail, y from -6 to +6")
axR.plot(path.real[sel], path.imag[sel], color="C0", lw=3, label="routes with |y| ≤ 1")
axR.annotate("", xy=(path[-1].real, path[-1].imag), xytext=(path[0].real, path[0].imag),
             arrowprops=dict(arrowstyle="->", lw=1.8, color="C3"))
axR.text(0.45, 0.62, "total", color="C3", fontsize=9)
axR.set_aspect("equal")
axR.set_xlabel("real part"); axR.set_ylabel("imaginary part")
axR.set_title("Far routes curl up and cancel", fontsize=9.5)
axR.legend(fontsize=7.5, loc="lower right")
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT), "; |total| =", abs(path[-1]), "; ideal |1+i| =", np.sqrt(2))
