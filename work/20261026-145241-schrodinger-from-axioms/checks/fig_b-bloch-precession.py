import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.linalg import expm
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-bloch-precession.png")
sx = np.array([[0,1],[1,0]], complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1,-1]).astype(complex)
U = lambda ang: expm(-1j*ang/2*sz)             # H=(hbar w/2) sz for time t: angle = w t
psi0 = np.array([1, 1], complex)/np.sqrt(2)    # theta = 90 deg, phi = 0 (along +x)
bloch = lambda p: (np.vdot(p, sx@p).real, np.vdot(p, sy@p).real)
def arc(p_start, ang_deg, n=200):
    return np.array([bloch(U(np.radians(a))@p_start) for a in np.linspace(0, ang_deg, n)])
a1 = arc(psi0, 70); mid = U(np.radians(70))@psi0; a2 = arc(mid, 50)
a12 = arc(psi0, 120)
end_two = bloch(U(np.radians(50))@mid); end_one = bloch(U(np.radians(120))@psi0)
assert np.allclose(end_two, end_one)
plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots(figsize=(7, 4))
th = np.linspace(0, 2*np.pi, 400); ax.plot(np.cos(th), np.sin(th), color="0.75", lw=1)
ax.axhline(0, color="0.85", lw=0.8); ax.axvline(0, color="0.85", lw=0.8)
ax.plot(a1[:,0], a1[:,1], "-", color="tab:blue", lw=5, label="rotation 1: 0° → 70°")
ax.plot(a2[:,0], a2[:,1], "-", color="tab:orange", lw=5, label="rotation 2: 70° → 120°")
r = 1.12; ax.plot(r*a12[:,0], r*a12[:,1], "k--", lw=2, label="one rotation: 0° → 120° (drawn just outside)")
for (px, py), lab in [((1, 0), "start φ=0°"), (bloch(mid), "70°")]:
    ax.annotate("", (px, py), (0, 0), arrowprops=dict(arrowstyle="->", color="0.4", lw=1.5))
    ax.text(1.2*px, 1.2*py, lab, ha="center", va="center", fontsize=10)
ax.annotate("", end_one, (0, 0), arrowprops=dict(arrowstyle="->", color="k", lw=2))
ax.plot(*end_two, "o", ms=13, mfc="white", mec="tab:orange", mew=2.5)
ax.plot(*end_one, "x", ms=10, color="k", mew=2.5)
ax.text(end_one[0]-0.15, end_one[1]+0.22, "120°: both endpoints\ncoincide (○ and ×)", ha="right", fontsize=10)
ax.text(0.03, -0.12, "z (out of page)", fontsize=9, color="0.4")
ax.set_xlabel(r"$\langle\sigma_x\rangle$ (dimensionless)"); ax.set_ylabel(r"$\langle\sigma_y\rangle$ (dimensionless)")
ax.set_aspect("equal"); ax.set_xlim(-2.6, 1.6); ax.set_ylim(-1.35, 1.45)
ax.legend(loc="lower left", fontsize=9, framealpha=0.95)
ax.set_title(r"Bloch equator, top view; $H=\frac{\hbar\omega}{2}\sigma_z$, angle $\varphi=\omega t$", fontsize=12)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
