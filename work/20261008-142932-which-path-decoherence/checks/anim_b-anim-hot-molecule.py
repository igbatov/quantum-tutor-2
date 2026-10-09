# Animation 3 (b-anim-hot-molecule), Experiment 3 of final-B.md (2004, hot C70).
# Temperature ramps 1000 K -> 3000 K.
#  Panel A (schematic): one molecule on two paths ~1 um apart, glowing more as T rises,
#    emitting photons; drawn wiggle length/colour encodes wavelength; photon wavelengths are
#    sampled from the ideal black-body photon-number spectrum at the current T; the drawn
#    emission rate is proportional to the total black-body photon rate (~T^3), scaled for display.
#  Panel B (computed): ideal black-body photon-number spectrum n_lambda(T) ~ 2c/lambda^4 /
#    (exp(hc/lambda k T) - 1), log axes, common scale (max at 3000 K = 1), 1 um and 2 um lines.
#  Panel C (illustrative model): V(T) = exp(-K * Int n_lambda(T) (1 - |sinc(2 pi d/lambda)|) dlambda),
#    d = 1 um, K fixed so that V(3000 K) = 0.10. Not a fit to the 2004 data.
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from scipy import constants as C
from scipy.integrate import quad

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "figures")
NAME = "b-anim-hot-molecule"
os.makedirs(FIG, exist_ok=True)

hc_k = C.h * C.c / C.k
d = 1e-6  # path separation (m)


def n_lam(lam, T):
    """Ideal black-body photon number per unit wavelength per time (arbitrary common units)."""
    return 2 * C.c / lam**4 / np.expm1(hc_k / (lam * T))


def overlap(lam):
    x = 2 * np.pi * d / lam
    return np.abs(np.sinc(x / np.pi))  # np.sinc(u) = sin(pi u)/(pi u)


# ---- Panel C model: decoherence exponent integral (integrate in log-lambda for accuracy)
def exponent_integral(T):
    f = lambda u: n_lam(np.exp(u), T) * (1 - overlap(np.exp(u))) * np.exp(u)
    lo, hi = np.log(0.05e-6), np.log(1e-3)
    pts = list(np.linspace(lo, hi, 60))
    tot = 0.0
    for a, b in zip(pts[:-1], pts[1:]):
        tot += quad(f, a, b, limit=200)[0]
    return tot

I3000 = exponent_integral(3000.0)
K = -np.log(0.10) / I3000
Tgrid = np.linspace(1000, 3000, 201)
Igrid = np.array([exponent_integral(T) for T in Tgrid])
Vgrid = np.exp(-K * Igrid)
V = lambda T: np.exp(-K * np.interp(T, Tgrid, Igrid))

# fractions of photons shorter than 2 um and total rate (for caption / panel B text)
def frac_short(T):
    tot = quad(lambda u: n_lam(np.exp(u), T) * np.exp(u), np.log(0.05e-6), np.log(1e-2), limit=400)[0]
    sh = quad(lambda u: n_lam(np.exp(u), T) * np.exp(u), np.log(0.05e-6), np.log(2e-6), limit=400)[0]
    return sh / tot, tot

f1, N1 = frac_short(1000.0)
f2, N2 = frac_short(2000.0)
f3, N3 = frac_short(3000.0)
print(f"K = {K:.4e}  (V(3000) = {V(3000):.3f}, V(1000) = {V(1000):.4f}, V(2000) = {V(2000):.3f})")
print(f"fraction < 2 um: 1000 K {f1:.3f}, 2000 K {f2:.3f}, 3000 K {f3:.3f}")
print(f"total photon rate ratio 3000/1000 = {N3/N1:.1f} (T^3 law -> 27)")
print(f"rate of <2 um photons ratio 3000/1000 = {f3*N3/(f1*N1):.0f}")
print(f"exponent ratio I(3000)/I(1000) = {I3000/Igrid[0]:.0f}")
T_half = np.interp(0.5, Vgrid[::-1], Tgrid[::-1])
print(f"V = 0.5 at T = {T_half:.0f} K")
# signed-sinc comparison (Poisson emission, sign kept) for the notes
def exponent_signed(T):
    f = lambda u: n_lam(np.exp(u), T) * (1 - np.sinc(2 * d / np.exp(u))) * np.exp(u)
    pts = list(np.linspace(np.log(0.05e-6), np.log(1e-3), 60))
    return sum(quad(f, a, b, limit=200)[0] for a, b in zip(pts[:-1], pts[1:]))
Ks = -np.log(0.10) / exponent_signed(3000.0)
print(f"signed-sinc variant with same V(3000)=0.1: V(2000) = {np.exp(-Ks*exponent_signed(2000.0)):.3f}, "
      f"V(1000) = {np.exp(-Ks*exponent_signed(1000.0)):.4f}")

# ---- frames
N_HOLD0, N_RAMP, N_HOLD1 = 8, 72, 14
Ts = np.concatenate([np.full(N_HOLD0, 1000.0), np.linspace(1000, 3000, N_RAMP), np.full(N_HOLD1, 3000.0)])
NF = len(Ts)

# ---- photon sampling (Panel A)
rng = np.random.default_rng(7)
lam_s = np.logspace(np.log10(0.2e-6), np.log10(60e-6), 3000)
_q = [0.0]
def sample_lambda(T):
    # quantile from a golden-ratio sequence (low-discrepancy) so the drawn short/long mix
    # tracks the black-body share closely even with few photons on screen
    w = n_lam(lam_s, T) * lam_s  # density per log-lambda
    cdf = np.cumsum(w); cdf /= cdf[-1]
    _q[0] = (_q[0] + 0.6180339887) % 1.0
    return np.interp(_q[0], cdf, lam_s)

RATE3000 = 1.4  # drawn photons per frame at 3000 K (display scale only)
LIFE = 9        # frames a photon stays on screen
photons = []    # dicts: birth, angle, lam
events = []
for i, T in enumerate(Ts):
    k = rng.poisson(RATE3000 * (T / 3000.0) ** 3)
    for _ in range(k):
        events.append(dict(birth=i, ang=rng.uniform(0, 2 * np.pi), lam=sample_lambda(T)))

ev3 = [e for e in events if Ts[e['birth']] >= 2900]
print('drawn photons at >=2900 K:', len(ev3), 'short share', np.mean([e['lam'] < 2e-6 for e in ev3]))
# ---- figure
plt.rcParams.update({"font.size": 11})
fig = plt.figure(figsize=(10, 6.6), dpi=80)
gs = fig.add_gridspec(2, 2, width_ratios=[1.0, 1.15], hspace=0.55, wspace=0.32,
                      left=0.06, right=0.98, top=0.93, bottom=0.13)
axA = fig.add_subplot(gs[:, 0])
axB = fig.add_subplot(gs[0, 1])
axC = fig.add_subplot(gs[1, 1])

# Panel A static (photon field) + a separate key below it
axA.set_position([0.02, 0.30, 0.42, 0.60])
axA.set_xlim(-5.6, 5.6); axA.set_ylim(-4.6, 4.6); axA.set_aspect("equal"); axA.axis("off")
fig.text(0.03, 0.935, "A  schematic, not to scale", fontsize=12)
yp = 0.5  # half the drawn path separation
xs = np.linspace(-5.6, 5.6, 200)
env = np.clip(1 - (xs / 5.6) ** 2, 0, None) ** 0.5
for s in (+1, -1):
    axA.plot(xs, s * yp * env, color="0.6", lw=1.2, ls="--", zorder=1)
glow = [axA.add_patch(plt.Circle((0, s * yp), 0.38, color="k", zorder=3)) for s in (+1, -1)]
halo = [axA.add_patch(plt.Circle((0, s * yp), 1.1, color="orange", alpha=0.0, lw=0, zorder=2)) for s in (+1, -1)]
Ttxt = fig.text(0.23, 0.885, "", ha="center", fontsize=15, weight="bold")
keyA = fig.add_axes([0.02, 0.06, 0.42, 0.24]); keyA.axis("off"); keyA.set_xlim(0, 1); keyA.set_ylim(0, 1)
keyA.text(0.02, 0.93, "one molecule on two paths (dashed), d ≈ 1 µm, drawn much larger;\n"
          "glow colour schematic", fontsize=9.5, color="0.25", va="top")
def key_wiggle(x0, y0, per, col, lw):
    xx = np.linspace(0, 0.16, 100); keyA.plot(x0 + xx, y0 + 0.05 * np.sin(2 * np.pi * xx / per), color=col, lw=lw)
key_wiggle(0.03, 0.50, 0.04, "navy", 2.2)
keyA.text(0.22, 0.50, "λ < 2 µm: short wiggle, thick;\ncan tell the paths apart", fontsize=9.5, va="center")
key_wiggle(0.03, 0.17, 0.11, "red", 1.2)
keyA.text(0.22, 0.17, "λ > 2 µm: long wiggle, thin;\nrecords little", fontsize=9.5, va="center")
countTxt = fig.text(0.23, 0.845, "", ha="center", fontsize=9.5, color="0.25")
photon_lines = []

def wiggle(ang, lam, age):
    """Wavy segment: drawn period grows with wavelength (log scale), 2.5 periods long."""
    per = 0.22 + 0.40 * np.log10(lam / 0.2e-6)  # 0.2 um -> 0.22, 2 um -> 0.62, 20 um -> 1.02
    L = 2.0 * per
    r0 = 0.5 + 0.30 * age                          # moves outward
    s = np.linspace(0, L, 120)
    amp = 0.13 + 0.10 * per
    r = r0 + s
    off = amp * np.sin(2 * np.pi * s / per)
    ux, uy = np.cos(ang), np.sin(ang)
    return r * ux - off * uy, r * uy + off * ux

# Panel B static
lam_um = np.logspace(np.log10(0.3), 1, 500)
ref = n_lam(lam_um * 1e-6, 3000).max()
axB.loglog(lam_um, n_lam(lam_um * 1e-6, 1000) / ref, color="0.75", lw=1, ls=":")
axB.loglog(lam_um, n_lam(lam_um * 1e-6, 3000) / ref, color="0.75", lw=1, ls=":")
axB.text(9.5, 1.2e-3, "1000 K (dotted)", fontsize=8.5, color="0.45", ha="right")
axB.text(9.5, 3.5e-2 * 1.0, "3000 K (dotted)", fontsize=8.5, color="0.45", ha="right")
axB.axvline(1, color="b", lw=1); axB.axvline(2, color="r", lw=1.2)
axB.text(1.04, 2e-7, "1 µm\n(path sep.)", color="b", fontsize=8.5)
axB.text(2.08, 2e-7, "2 µm", color="r", fontsize=8.5)
axB.set_xlim(0.3, 10); axB.set_ylim(1e-7, 3)
axB.set_xlabel("wavelength (µm)")
axB.set_ylabel("photons per unit λ per time\n(relative, common scale)", fontsize=10)
axB.set_title("B  ideal black-body photon spectrum (computed)", fontsize=11, loc="left")
lineB, = axB.loglog([], [], "k-", lw=2.2)
fillB = [None]
fracTxt = axB.text(3.0, 2e-7, "", fontsize=9)

# Panel C static
axC.plot(Tgrid, Vgrid, "k-", lw=2)
axC.set_xlim(950, 3050); axC.set_ylim(0, 1.08)
axC.set_xlabel("molecule temperature T (K)"); axC.set_ylabel("stripe visibility V")
axC.set_title("C  visibility, illustrative model (d = 1 µm)", fontsize=11, loc="left")
axC.text(1000, 0.08, "scale K set to match the qualitative result\n(V ≈ 1 at 1000 K, V = 0.1 at 3000 K);\n"
         "not a fit to the 2004 data", fontsize=8.5, color="0.25", va="bottom")
axC.grid(alpha=0.3)
markC, = axC.plot([], [], "o", ms=10, mfc="white", mec="k", mew=2)
vTxt = axC.text(2100, 0.88, "", fontsize=10)

fig.text(0.01, 0.012, "Model: V = exp(−K ∫ n_λ(T) (1 − |sin(2πd/λ)/(2πd/λ)|) dλ), ideal black body, isotropic emission. "
         "Drawn photon numbers in A are scaled for display.", fontsize=8.5, color="0.2")

def glow_color(T):
    # schematic: dull red at 1000 K -> orange -> pale yellow at 3000 K
    t = (T - 1000) / 2000
    c0, c1, c2 = np.array([0.45, 0.05, 0.0]), np.array([1.0, 0.45, 0.05]), np.array([1.0, 0.92, 0.6])
    return tuple(c0 + (c1 - c0) * 2 * t) if t < 0.5 else tuple(c1 + (c2 - c1) * (2 * t - 1))

def update(i):
    T = Ts[i]
    Ttxt.set_text(f"T = {T:,.0f} K")
    col = glow_color(T)
    for g in glow:
        g.set_color(col)
    for h in halo:
        h.set_alpha(0.08 + 0.42 * ((T - 1000) / 2000) ** 1.5)
        h.set_radius(0.6 + 0.5 * (T - 1000) / 2000)
    for ln in photon_lines:
        ln.remove()
    photon_lines.clear()
    live = [e for e in events if 0 <= i - e["birth"] < LIFE]
    for e in live:
        x, y = wiggle(e["ang"], e["lam"], i - e["birth"])
        short = e["lam"] < 2e-6
        ln, = axA.plot(x, y, color="navy" if short else "red", lw=2.2 if short else 1.2, zorder=4)
        photon_lines.append(ln)
    countTxt.set_text(f"drawn photon rate ∝ T³ (×{(T/1000)**3:.0f} vs 1000 K)")
    nb = n_lam(lam_um * 1e-6, T) / ref
    lineB.set_data(lam_um, nb)
    if fillB[0] is not None:
        fillB[0].remove()
    m = lam_um <= 2
    fillB[0] = axB.fill_between(lam_um[m], 1e-7, np.maximum(nb[m], 1e-7), color="0.6", alpha=0.45, hatch="//", lw=0)
    fs, _ = frac_short(T)
    fracTxt.set_text(f"hatched (λ < 2 µm):\n{100*fs:.0f}% of photons")
    v = V(T)
    markC.set_data([T], [v])
    vTxt.set_text(f"V = {v:.2f}")
    return []

anim = FuncAnimation(fig, update, frames=NF, blit=False)
gif = os.path.join(FIG, NAME + ".gif")
anim.save(gif, writer=PillowWriter(fps=12))
print("saved", gif, os.path.getsize(gif) / 1e6, "MB,", NF, "frames")

for k, fi in enumerate([4, 8 + N_RAMP // 2, NF - 3], start=1):
    update(fi)
    p = os.path.join(FIG, f"{NAME}-still-{k}.png")
    fig.savefig(p, dpi=80)
    print("still", k, "frame", fi, "T =", Ts[fi], p)
