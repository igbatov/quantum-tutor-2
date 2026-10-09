"""Animation: decoherence by a scattered photon, with the particle's path waves unchanged.

Model (idealized):
  joint state (|L>|E_L> + |R>|E_R>)/sqrt2, scatterer starts in |E>.
  Screen probability (photon not looked at):
      P(x) = 1/2|psi_L|^2 + 1/2|psi_R|^2 + Re[psi_L* psi_R <E_L|E_R>]
  Far screen: psi_{L,R}(x) = A(x) exp(+/- i pi x / s), s = fringe spacing,
  A(x) = one-slit amplitude envelope, slit separation = 4 x slit width,
  so A(x) = sinc(x / 4s) (first zero at x = 4s).
  Phase 1: one photon emitted isotropically, wavelength lam, path separation d:
      <E_L|E_R> = sin(2 pi d/lam) / (2 pi d/lam),  d/lam from 0 to 0.5 (c from 1 to 0).
  Phase 2: N = 1..5 independent photons, each with overlap 0.6:
      <E_L|E_R> = 0.6^N  (computed as an inner product of N-photon product states).
Checks printed at the end:
  - |psi_L|^2 == |psi_R|^2 in every frame, and both equal their frame-0 values.
  - fringe visibility measured from P(x) (relative to the one-slit sum) == |<E_L|E_R>|.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import Arc
from scipy.optimize import brentq

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(RUN, "figures")
os.makedirs(FIG, exist_ok=True)

plt.rcParams.update({"font.size": 10, "axes.titlesize": 11, "axes.labelsize": 10})

# ---------------- physics ----------------
x = np.linspace(-10, 10, 4001)          # x in units of fringe spacing s
A = np.sinc(x / 4.0)                    # one-slit amplitude envelope, zeros at |x| = 4, 8


def psi_L(x):
    return np.sinc(x / 4.0) * np.exp(+1j * np.pi * x)


def psi_R(x):
    return np.sinc(x / 4.0) * np.exp(-1j * np.pi * x)


def c_one_photon(u):                    # u = d / lambda, isotropic emission
    return np.sinc(2.0 * u)             # = sin(2 pi u)/(2 pi u)


def photon_states(u):
    """Single-photon final states as unit vectors in a 2D real plane with overlap c(u)."""
    c = c_one_photon(u)
    th = np.arccos(c)
    return np.array([1.0, 0.0]), np.array([np.cos(th), np.sin(th)])


def kron_n(v, n):
    out = np.array([1.0])
    for _ in range(n):
        out = np.kron(out, v)
    return out


C2 = 0.6
U2 = brentq(lambda u: c_one_photon(u) - C2, 0.01, 0.49)   # d/lam giving c = 0.6

# ---------------- frame schedule ----------------
frames = []
for _ in range(6):
    frames.append(dict(phase=1, u=0.0, N=1))
for u in np.linspace(0.0, 0.5, 54):
    frames.append(dict(phase=1, u=float(u), N=1))
for _ in range(12):
    frames.append(dict(phase=1, u=0.5, N=1))
for N in range(1, 6):
    for _ in range(7):
        frames.append(dict(phase=2, u=U2, N=N))
for _ in range(8):
    frames.append(dict(phase=2, u=U2, N=5))

for f in frames:
    eL1, eR1 = photon_states(f["u"])
    EL, ER = kron_n(eL1, f["N"]), kron_n(eR1, f["N"])
    f["c"] = float(np.dot(EL, ER))      # <E_L|E_R> from the state vectors
    f["c_formula"] = float(c_one_photon(f["u"]) ** f["N"])

# ---------------- verification ----------------
pL0 = np.abs(psi_L(x)) ** 2
pR0 = np.abs(psi_R(x)) ** 2
central = np.abs(x) < 3.5               # stay away from envelope zeros at |x| = 4
max_LR = max_unchanged = max_vis = max_cform = 0.0
for f in frames:
    pl, pr = psi_L(x), psi_R(x)
    PL, PR = np.abs(pl) ** 2, np.abs(pr) ** 2
    P = 0.5 * PL + 0.5 * PR + np.real(np.conj(pl) * pr * f["c"])
    f["P"], f["PL"], f["PR"] = P, PL, PR
    f["cross"] = np.real(np.conj(pl) * pr * f["c"])
    ratio = P[central] / (0.5 * PL + 0.5 * PR)[central]
    V = (ratio.max() - ratio.min()) / (ratio.max() + ratio.min())
    f["V"] = V
    max_LR = max(max_LR, np.max(np.abs(PL - PR)))
    max_unchanged = max(max_unchanged, np.max(np.abs(PL - pL0)), np.max(np.abs(PR - pR0)))
    max_vis = max(max_vis, abs(V - abs(f["c"])))
    max_cform = max(max_cform, abs(f["c"] - f["c_formula"]))
    assert f["c"] >= -1e-12, "overlap went negative"

TOL = 1e-6
print(f"frames: {len(frames)}")
print(f"max | |psi_L|^2 - |psi_R|^2 | over all frames: {max_LR:.3e}")
print(f"max change of |psi_L|^2, |psi_R|^2 from frame 0: {max_unchanged:.3e}")
print(f"max | visibility(P) - |<E_L|E_R>| | over all frames: {max_vis:.3e}")
print(f"max | <E_L|E_R>(vectors) - c(d/lam)^N (formula) |: {max_cform:.3e}")
print(f"c range: {min(f['c'] for f in frames):.4f} .. {max(f['c'] for f in frames):.4f};"
      f" phase-2 d/lam = {U2:.4f}")
ok = max_LR < TOL and max_unchanged < TOL and max_vis < 1e-3 and max_cform < TOL
print("PASS" if ok else "FAIL")

# ---------------- figure ----------------
fig = plt.figure(figsize=(8.0, 7.6), dpi=100)
gs = fig.add_gridspec(2, 2, width_ratios=[2.15, 1], height_ratios=[1, 1.15],
                      left=0.08, right=0.98, top=0.90, bottom=0.07, wspace=0.18, hspace=0.42)
axA = fig.add_subplot(gs[0, 0])
axB = fig.add_subplot(gs[0, 1])
axC = fig.add_subplot(gs[1, :])
suptitle = fig.suptitle("", fontsize=12, fontweight="bold")

# Panel A
lineL, = axA.plot(x, pL0, color="tab:blue", lw=2.6, label=r"$|\psi_L(x)|^2$")
lineR, = axA.plot(x, pR0, color="tab:orange", lw=1.6, ls=(0, (4, 3)), label=r"$|\psi_R(x)|^2$")
axA.set_xlim(-10, 10)
axA.set_ylim(0, 1.25)
axA.set_xlabel("screen position x / s   (s = fringe spacing)")
axA.set_ylabel(r"density (units of $|\psi_L(0)|^2$)", fontsize=9)
axA.set_title("A. Particle's path waves (unchanged)")
axA.legend(loc="upper right", fontsize=9, frameon=False)
txtA = axA.text(-9.6, 1.12, "", fontsize=8.5, va="center", color="0.25")

# Panel B
axB.set_aspect("equal")
axB.set_xlim(-0.25, 1.45)
axB.set_ylim(-1.05, 1.45)
axB.axis("off")
axB.set_title("B. Scatterer's two final states")
axB.text(0.6, 1.38, "abstract state space, not lab", ha="center", fontsize=8, style="italic",
         color="0.35")
arrL = axB.annotate("", xy=(1, 0), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", lw=2.6, color="tab:blue"))
arrR = axB.annotate("", xy=(1, 0), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="-|>", lw=1.6, color="tab:orange", ls="--"))
labL = axB.text(1.04, -0.07, r"$|E_L\rangle$", fontsize=10, color="tab:blue", va="top")
labR = axB.text(1.04, 0.08, r"$|E_R\rangle$", fontsize=10, color="tab:orange", va="bottom")
arc = Arc((0, 0), 0.5, 0.5, theta1=0, theta2=0, color="0.3", lw=1)
axB.add_patch(arc)
labTh = axB.text(0.3, 0.05, "", fontsize=9)
txtB = axB.text(0.6, -0.36, "", ha="center", fontsize=10, fontweight="bold")
# lab schematic
axB.plot([-0.2, 1.3, 1.3, -0.2, -0.2], [-0.52, -0.52, -1.03, -1.03, -0.52], color="0.6", lw=0.8)
axB.text(0.6, -0.6, "schematic (lab): paths L, R", ha="center", fontsize=7.5, style="italic", color="0.35")
dotL, = axB.plot([0.05], [-0.74], "o", color="tab:blue", ms=7)
dotR, = axB.plot([0.05], [-0.74], "o", color="tab:orange", ms=5)
dline, = axB.plot([0.05, 0.05], [-0.82, -0.82], color="k", lw=1)
axB.plot([0.05, 1.05], [-0.95, -0.95], color="tab:red", lw=2)
axB.text(1.08, -0.95, r"$\lambda$", va="center", fontsize=9, color="tab:red")
txtd = axB.text(1.08, -0.74, "", va="center", fontsize=8)

# Panel C
lineP, = axC.plot(x, frames[0]["P"], color="k", lw=2.2, label=r"$P(x)$")
lineS, = axC.plot(x, 0.5 * pL0 + 0.5 * pR0, color="tab:green", lw=1.6, ls="--",
                  label=r"$\frac{1}{2}|\psi_L|^2+\frac{1}{2}|\psi_R|^2$ (one-slit sum)")
lineX, = axC.plot(x, frames[0]["cross"], color="tab:purple", lw=0.9,
                  label=r"cross term Re$[\psi_L^*\psi_R\langle E_L|E_R\rangle]$")
axC.axhline(0, color="0.6", lw=0.6)
axC.set_xlim(-10, 10)
axC.set_ylim(-1.1, 2.3)
axC.set_xlabel("screen position x / s   (s = fringe spacing)")
axC.set_ylabel(r"density (units of $|\psi_L(0)|^2$)", fontsize=9)
axC.set_title("C. What the screen shows")
axC.legend(loc="lower left", fontsize=8.5, frameon=False, ncol=1)
txtC = axC.text(9.7, 2.1, "", ha="right", va="center", fontsize=11, fontweight="bold")


def update(i):
    f = frames[i]
    c = f["c"]
    th = np.arccos(np.clip(c, -1, 1))
    if f["phase"] == 1:
        suptitle.set_text(f"One photon scatters off the particle:  d/λ = {f['u']:.2f}")
    else:
        suptitle.set_text(f"Several photons, each with overlap 0.6:  N = {f['N']}")
    lineL.set_ydata(f["PL"])
    lineR.set_ydata(f["PR"])
    txtA.set_text("both curves identical every frame;\nno kick, no change")
    ex, ey = np.cos(th), np.sin(th)
    arrR.xy = (ex, ey)
    labR.set_position((ex + 0.04, ey + 0.08))
    arc.theta2 = np.degrees(th)
    labTh.set_text(r"$\theta$" if th > 0.12 else "")
    labTh.set_position((0.3 * np.cos(th / 2) + 0.02, 0.3 * np.sin(th / 2) - 0.04))
    if f["phase"] == 1:
        txtB.set_text(r"$|\langle E_L|E_R\rangle| = \cos\theta$ = " + f"{abs(c):.2f}")
        d = f["u"]
        dotR.set_data([0.05 + d], [-0.74])
        dline.set_data([0.05, 0.05 + d], [-0.82, -0.82])
        txtd.set_text("d")
        txtd.set_position((0.1 + d, -0.82))
    else:
        txtB.set_text(r"$|\langle E_L|E_R\rangle| = 0.6^{%d}$ = " % f["N"] + f"{abs(c):.2f}")
        d = f["u"]
        dotR.set_data([0.05 + d], [-0.74])
        dline.set_data([0.05, 0.05 + d], [-0.82, -0.82])
        txtd.set_text(f"d, {f['N']} photon" + ("s" if f["N"] > 1 else ""))
        txtd.set_position((0.1 + d, -0.82))
    lineP.set_ydata(f["P"])
    lineX.set_ydata(f["cross"])
    txtC.set_text(r"visibility = $|\langle E_L|E_R\rangle|$ = " + f"{abs(c):.2f}")
    return ()


if __name__ == "__main__":
    anim = FuncAnimation(fig, update, frames=len(frames), blit=False)
    gif = os.path.join(FIG, "decoherence-process.gif")
    anim.save(gif, writer=PillowWriter(fps=12), dpi=100)
    print(f"saved {gif}: {os.path.getsize(gif) / 1e6:.2f} MB")
    for name, idx in [("start", 0), ("one-photon-end", 71),
                      ("N3", 72 + 2 * 7 + 3)]:
        update(idx)
        p = os.path.join(FIG, f"decoherence-process-still-{name}.png")
        fig.savefig(p, dpi=100)
        print(f"still {p}: frame {idx}, c = {frames[idx]['c']:.3f}")
