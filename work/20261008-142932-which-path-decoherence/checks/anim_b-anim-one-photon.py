"""Animation b-anim-one-photon (Experiment 1, Chapman et al. 1995).

Model (computed, Panels B and C):
  * isotropic emission; one scattered photon multiplies the stripe amplitude by the
    signed overlap c(d) = sin(2*pi*d/lam) / (2*pi*d/lam)   (np.sinc(2 d/lam));
  * the number n of photons per atom is Poisson with mean nbar = 1, each photon
    independent, so the stripes of all arriving atoms have visibility
    F(d) = sum_n P(n) c^n = exp(-nbar (1 - c(d)))  (relative to laser off);
  * sub-groups: n = 0 atoms (fraction e^-1) keep visibility 1; n = 1 atoms
    (fraction e^-1) have signed visibility c(d) (c < 0: shifted by half a stripe).
  * count behind the third grating vs its sideways shift x (in grating periods):
    N(x) / <N> = 1 + V cos(2 pi x), laser-off visibility idealized as 1.
Panel A is schematic, not to scale.
"""
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from matplotlib.animation import FuncAnimation, PillowWriter

here = os.path.dirname(os.path.abspath(__file__))
figdir = os.path.join(here, "..", "figures")
name = "b-anim-one-photon"
plt.rcParams.update({"font.size": 11})

nbar = 1.0
c = lambda r: np.sinc(2 * r)                       # r = d / lambda
F = lambda r: np.exp(-nbar * (1 - c(r)))

# ---- printed checks of the numbers the animation and caption use ----
rr = np.linspace(0, 2, 200001)
Fr = F(rr)
i_min = np.argmin(Fr); r_min, F_min = rr[i_min], Fr[i_min]
m = (rr > 1.0) & (rr < 1.5); i_rev = np.argmax(np.where(m, Fr, -1)); r_rev, F_rev = rr[i_rev], Fr[i_rev]
m2 = (rr > 1.5); i_m2 = np.argmin(np.where(m2, Fr, 9)); r_m2, F_m2 = rr[i_m2], Fr[i_m2]
# Poisson sum check
from scipy.stats import poisson
r_test = np.array([0.3, 0.5, 0.715, 1.23, 1.9])
S = sum(poisson.pmf(n, nbar) * c(r_test) ** n for n in range(60))
assert np.allclose(S, F(r_test), atol=1e-12), (S, F(r_test))
assert np.all(Fr > 0)
print(f"F(0)={F(0.0):.3f}  F(lam/2)={F(0.5):.3f}")
print(f"min of F on [0,2]: d={r_min:.3f} lam, F={F_min:.3f}")
print(f"revival max on [1,1.5]: d={r_rev:.3f} lam, F={F_rev:.3f}")
print(f"second dip on [1.5,2]: d={r_m2:.3f} lam, F={F_m2:.3f}")
print(f"F(2 lam)={F(2.0):.3f}, large-d limit e^-1={np.exp(-1):.3f}")
print(f"most negative c: {c(rr).min():.3f} at d={rr[np.argmin(c(rr))]:.3f} lam")
print("Poisson-sum check PASS; F > 0 everywhere (total pattern never shifted) PASS")

# ---- frames ----
n_sweep, n_hold = 84, 8
d_frames = np.concatenate([np.linspace(0, 2, n_sweep), np.full(n_hold, 2.0)])
n_frames = len(d_frames)

# schematic photon events: a new atom every 6 frames, n ~ Poisson(1)
rng = np.random.default_rng(7)
atom_len = 6
n_atoms = int(np.ceil(n_frames / atom_len))
atom_n = rng.poisson(nbar, n_atoms)
atom_ph = [[(rng.integers(2), rng.uniform(0, 2 * np.pi)) for _ in range(k)] for k in atom_n]
print("photons per schematic atom:", atom_n.tolist())

fig = plt.figure(figsize=(8, 7.2))
gs = fig.add_gridspec(2, 2, height_ratios=[0.85, 1.15], hspace=0.32, wspace=0.3,
                      left=0.08, right=0.97, top=0.90, bottom=0.11)
axA = fig.add_subplot(gs[0, :]); axB = fig.add_subplot(gs[1, 0]); axC = fig.add_subplot(gs[1, 1])

# Panel A (schematic)
xG1, xG2, xG3, yG2 = 1.0, 5.5, 10.0, 1.6
x_l0, x_l1 = 1.0, 3.0                               # laser sweep range (schematic)
def path_y(x):
    return np.where(x <= xG2, yG2 * (x - xG1) / (xG2 - xG1), yG2 * (xG3 - x) / (xG3 - xG2))
axA.set_xlim(-0.3, 11.4); axA.set_ylim(-2.8, 2.7); axA.axis("off")
axA.set_title("A  Set-up (schematic, not to scale)", loc="left", fontsize=11)
axA.plot([-0.2, xG1], [0, 0], color="0.4", lw=2)
axA.text(-0.2, 0.25, "Na atoms", fontsize=9)
xs = np.linspace(xG1, xG3, 400)
axA.plot(xs, path_y(xs), "b-", lw=1.8); axA.plot(xs, -path_y(xs), "b-", lw=1.8)
axA.text(6.9, 1.6, "two paths of one atom's wave", fontsize=9, color="b")
for xg, lab in [(xG1, "G1"), (xG2, "G2"), (xG3, "G3 (mask, slid sideways)")]:
    for y0 in np.arange(-2.2, 2.25, 0.22):
        axA.plot([xg, xg], [y0, y0 + 0.12], "k-", lw=2)
    axA.text(xg, 2.42, lab, ha="center" if xg < 9 else "right", fontsize=9)
axA.add_patch(plt.Rectangle((10.35, -0.5), 0.35, 1.0, fc="0.75", ec="k"))
axA.text(10.52, 0.65, "hot-wire\ncounter", ha="center", fontsize=8)
laser = plt.Rectangle((x_l0 - 0.07, -2.3), 0.14, 4.5, color="orange", alpha=0.45, lw=0); axA.add_patch(laser)
laser_lab = axA.text(x_l0 + 0.12, -2.6, "laser 589 nm", ha="left", fontsize=9, color="darkorange")
d_arrow = axA.annotate("", (x_l0, 0), (x_l0, 0), arrowprops=dict(arrowstyle="<->", lw=1.2))
d_text = axA.text(x_l0 + 0.3, -0.12, "", fontsize=10, zorder=4, bbox=dict(fc="white", ec="none", pad=1, alpha=0.85))
axA.text(5.9, -2.6, "real d at the laser: 0 to ~1.2 µm;\nat G2 the paths are tens of µm apart", fontsize=8, color="0.3")
ph_lines = [axA.plot([], [], "r-", lw=1.2, zorder=1)[0] for _ in range(max(atom_n.max(), 1))]
ph_text = axA.text(-0.3, -1.9, "", fontsize=8.5, color="r")

# Panel B (computed)
xB = np.linspace(0, 2, 400)
axB.set_xlim(0, 2); axB.set_ylim(0, 2.75)
axB.set_xlabel("sideways shift of G3 (grating periods)")
axB.set_ylabel("atoms counted / mean count")
axB.set_title("B  Stripes read at G3 (computed)", loc="left", fontsize=11)
lB0, = axB.plot(xB, 1 + np.cos(2 * np.pi * xB), ":", color="0.55", lw=1.3, label="atoms with 0 photons (37%)")
lB1, = axB.plot(xB, 1 + 0 * xB, "--", color="r", lw=1.3, label="atoms with exactly 1 photon (37%)")
lBt, = axB.plot(xB, 1 + 0 * xB, "k-", lw=2.4, label="all arriving atoms")
axB.legend(loc="upper center", fontsize=7.5, ncol=1, frameon=False, bbox_to_anchor=(0.5, 1.02))
vis_text = axB.text(0.03, 0.06, "", fontsize=9, transform=axB.transAxes)
shift_text = axB.text(0.97, 0.06, "", fontsize=8, color="r", ha="right", transform=axB.transAxes)

# Panel C (computed)
rC = np.linspace(0, 2, 1001)
axC.axhline(0, color="0.7", lw=0.8)
axC.axhline(np.exp(-1), color="0.6", lw=0.8, ls=":")
axC.text(1.02, 0.27, "e⁻¹ = share of atoms\nwith no photon", fontsize=7.5, ha="left", va="top", color="0.4")
axC.plot(rC, c(rC), "--", color="r", lw=1.1, label="exactly 1 photon: c(d)")
axC.plot(rC, F(rC), "k-", lw=2.2, label="mean 1 photon (Poisson)")
axC.plot(r_min, F_min, "s", mfc="white", mec="k", ms=6)
axC.annotate(f"lowest {F_min:.2f}\nat d ≈ {r_min:.2f}λ", (r_min, F_min), (0.03, 0.06),
             fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
axC.annotate(f"partial revival\n{F_rev:.2f} at {r_rev:.2f}λ", (r_rev, F_rev), (1.15, 0.7),
             fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
axC.set_xlim(0, 2); axC.set_ylim(-0.3, 1.05)
axC.set_xlabel("path separation at scattering, d / λ")
axC.set_ylabel("visibility / visibility, laser off")
axC.set_title("C  Visibility vs d (computed)", loc="left", fontsize=11)
axC.legend(loc="upper right", fontsize=7.5, frameon=False)
mk, = axC.plot([], [], "o", color="k", mfc="orange", ms=10, zorder=5)
vline = axC.axvline(0, color="orange", lw=1)

fig.suptitle("Experiment 1 (1995): each atom scatters on average one photon; nobody detects it", fontsize=11, y=0.985)
fig.text(0.01, 0.01, "Model: isotropic emission, Poisson photon number (mean 1), laser-off visibility set to 1. "
         "Only d/λ matters.", fontsize=8, color="0.3")

def wavy(x0, y0, ang, L=1.3, k=5, amp=0.07):
    s = np.linspace(0, L, 80)
    u, v = np.cos(ang), np.sin(ang)
    w = amp * np.sin(2 * np.pi * k * s / L) * np.minimum(1, s / 0.15)
    return x0 + s * u - w * v, y0 + s * v + w * u

def update(i):
    r = d_frames[i]
    xl = x_l0 + (x_l1 - x_l0) * r / 2
    yl = float(path_y(np.array(xl)))
    laser.set_x(xl - 0.07)
    laser_lab.set_x(xl + 0.12)
    d_arrow.xy = (xl + 0.18, yl); d_arrow.set_position((xl + 0.18, -yl))
    d_text.set_x(xl + 0.3); d_text.set_text(f"d = {r:.2f} λ")
    a = min(i // atom_len, n_atoms - 1)
    for ln in ph_lines:
        ln.set_data([], [])
    for j, (which, ang) in enumerate(atom_ph[a]):
        y0 = yl if which == 0 else -yl
        ln = ph_lines[j]; ln.set_data(*wavy(xl, y0, ang))
    k = atom_n[a]
    ph_text.set_text(f"this atom:\n{k} photon{'s' if k != 1 else ''}\n(undetected)")
    cv, Fv = c(r), F(r)
    lB1.set_ydata(1 + cv * np.cos(2 * np.pi * xB))
    lBt.set_ydata(1 + Fv * np.cos(2 * np.pi * xB))
    vis_text.set_text(f"visibility, all atoms: {Fv:.2f}")
    shift_text.set_text("1-photon stripes shifted\nby half a period (c < 0)" if cv < -0.02 else "")
    mk.set_data([r], [Fv]); vline.set_xdata([r, r])
    return []

anim = FuncAnimation(fig, update, frames=n_frames, blit=False)
out = os.path.join(figdir, f"{name}.gif")
anim.save(out, writer=PillowWriter(fps=12), dpi=100)
print("saved", out, os.path.getsize(out) / 1e6, "MB", n_frames, "frames")

# stills at d = 0.25, ~0.72 (minimum), ~1.23 (revival)
for s, rt in enumerate([0.25, r_min, r_rev], 1):
    i = int(np.argmin(np.abs(d_frames[:n_sweep] - rt)))
    update(i)
    p = os.path.join(figdir, f"{name}-still-{s}.png")
    fig.savefig(p, dpi=100); print("still", p, f"d={d_frames[i]:.3f}")
