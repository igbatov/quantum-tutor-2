# Animation 2 (b-anim-gas): Experiment 2 of final-B.md (collisional decoherence, C70 + argon, 2003).
#
# Stated model (all computed numbers come from here):
#   * Pressure p in units of p0, the pressure at which the visibility has fallen to 1/e.
#   * Collisions between first and third grating are independent (Poisson), mean mu = k * p.
#   * Illustrative loss model: each collision, with probability f = 1/2, deflects the molecule out of
#     the detected beam; otherwise it passes on.  (f is NOT a measured value.)
#       -> fraction of molecules that still arrive:            T(p) = exp(-f mu)
#       -> collisions suffered by arriving molecules: Poisson, mean (1-f) mu   (Poisson thinning)
#   * Per-collision overlap c = 0 (one collision is a full record; argon wavelength << 1 um separation),
#     so the visibility among arriving molecules is exp(-(1-f) mu (1-c)) = exp(-p/p0) when k = 2/p0.
#     With f = 1/2 the arriving fraction is then also exp(-p/p0).
#   * Pattern read by sliding grating 3: counts(x) = T(p) * [1 + V0 * V(p) * cos(2 pi x / g)],
#     sinusoidal idealization, ideal zero-pressure visibility V0 = 1, grating period g = 1 um.
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from matplotlib.animation import FuncAnimation, PillowWriter

here = os.path.dirname(os.path.abspath(__file__))
figdir = os.path.join(here, "..", "figures")
name = "b-anim-gas"
gif = os.path.join(figdir, name + ".gif")

F_LOSS = 0.5                       # illustrative fraction of collisions that knock the molecule out
K = 1.0 / (1 - F_LOSS)             # mean collisions per p0, so that (1-f) K p0 = 1
G = 1.0                            # grating period, um
V0 = 1.0                           # ideal zero-pressure visibility
def mean_coll(p): return K * p
def transmitted(p): return np.exp(-F_LOSS * mean_coll(p))
def visibility(p): return np.exp(-(1 - F_LOSS) * mean_coll(p) * (1 - 0.0))   # c = 0

# self-checks of the model
ps = np.linspace(0, 3, 31)
assert np.allclose(visibility(ps), np.exp(-ps)) and np.allclose(transmitted(ps), np.exp(-ps))
rng_chk = np.random.default_rng(1)
n = rng_chk.poisson(mean_coll(2.0), 400000); lost = rng_chk.binomial(n, F_LOSS)
arr = lost == 0
mc_T, mc_V = arr.mean(), (n[arr] == 0).mean()   # V among arrivals = fraction with no collision (c = 0)
print(f"MC check p=2p0: T={mc_T:.4f} (model {transmitted(2):.4f}), V={mc_V:.4f} (model {visibility(2):.4f})")
assert abs(mc_T - transmitted(2)) < 3e-3 and abs(mc_V - visibility(2)) < 5e-3

# timeline: pressure steps 0, 0.5, ..., 3.0 p0, 12 frames each
STEPS = np.arange(0, 3.01, 0.5)
FPS, PER = 12, 12
NF = len(STEPS) * PER
p_of = lambda i: STEPS[min(i // PER, len(STEPS) - 1)]

# ---------- schematic particle simulation (panel A) ----------
rng = np.random.default_rng(7)
XG = [2.0, 5.0, 8.0]               # grating positions (schematic, not to scale)
X0, X1, YB = 0.6, 9.6, 0.9         # source, detector, beam half-height
VX = 0.25                          # schematic speed per frame
NGAS_PER_P0 = 30
gas = rng.uniform([0.2, -1.9], [9.8, 1.9], size=(NGAS_PER_P0 * 3 + 5, 2))
frames_inside = (XG[2] - XG[0]) / VX
mols = []                          # dict(x, y, vx, vy, state) state: 0 clean, 1 hit-still-in-beam, 2 knocked out

def spawn():
    mols.append(dict(x=X0, y=rng.uniform(-0.7, 0.7), vx=VX, vy=0.0, state=0))

# pre-run the beam so it is full at frame 0
pre = [];
def step_particles(p):
    flashes = []
    q = mean_coll(p) / frames_inside                     # collision chance per frame inside G1..G3
    for _ in range(rng.poisson(1.1)): spawn()
    for m in mols:
        if m["state"] < 2 and XG[0] <= m["x"] <= XG[2] and rng.random() < q:
            flashes.append((m["x"], m["y"]))
            if rng.random() < F_LOSS:
                m["state"] = 2; ang = rng.choice([-1, 1]) * rng.uniform(0.35, 0.7)
                m["vx"], m["vy"] = VX * np.cos(ang), VX * np.sin(ang)
            else:
                m["state"] = 1
        m["x"] += m["vx"]; m["y"] += m["vy"]
    mols[:] = [m for m in mols if m["x"] < X1 and abs(m["y"]) < 2.0]
    return flashes

for _ in range(40): step_particles(0.0)
sim = []                           # precompute every frame
flash_hist = []
for i in range(NF):
    p = p_of(i)
    fl = step_particles(p)
    flash_hist.append(fl)
    gas += rng.normal(0, 0.04, gas.shape); gas[:, 0] = np.clip(gas[:, 0], 0.2, 9.8); gas[:, 1] = np.clip(gas[:, 1], -1.9, 1.9)
    ng = int(round(NGAS_PER_P0 * p))
    sim.append(dict(mols=[(m["x"], m["y"], m["state"]) for m in mols], gas=gas[:ng].copy(),
                    flashes=fl + (flash_hist[-2] if len(flash_hist) > 1 else [])))

# ---------- figure ----------
plt.rcParams.update({"font.size": 10})
fig = plt.figure(figsize=(8, 6.8), facecolor="white")
gsp = fig.add_gridspec(2, 2, height_ratios=[1.0, 1], hspace=0.42, wspace=0.36,
                       left=0.11, right=0.98, top=0.95, bottom=0.15)
axA = fig.add_subplot(gsp[0, :]); axB = fig.add_subplot(gsp[1, 0]); axC = fig.add_subplot(gsp[1, 1])

# panel A static parts
axA.set_xlim(0, 10); axA.set_ylim(-2.05, 2.05); axA.set_xticks([]); axA.set_yticks([])
axA.set_title("A  schematic, not to scale: C70 molecules through a three-grating Talbot–Lau interferometer",
              fontsize=9.5, loc="left")
for k, xg in enumerate(XG):
    for yy in np.arange(-1.6, 1.6, 0.2):
        axA.plot([xg, xg], [yy, yy + 0.12], color="0.25", lw=2.2, solid_capstyle="butt")
    axA.text(xg, -2.0, ["grating 1", "grating 2", "grating 3\n(slid sideways)"][k], ha="center", va="bottom", fontsize=8)
axA.add_patch(plt.Rectangle((0.05, -0.9), 0.45, 1.8, fc="0.85", ec="k")); axA.text(0.27, 0, "oven", rotation=90, ha="center", va="center", fontsize=8)
axA.add_patch(plt.Rectangle((9.6, -0.9), 0.3, 1.8, fc="0.85", ec="k")); axA.text(9.75, 0, "detector", rotation=90, ha="center", va="center", fontsize=8)
gas_sc = axA.scatter([], [], s=5, color="0.55", zorder=1)
m0 = axA.scatter([], [], s=26, color="k", zorder=3)
m1 = axA.scatter([], [], s=26, facecolors="white", edgecolors="k", linewidths=1.2, zorder=3)
m2 = axA.scatter([], [], s=26, marker="x", color="0.45", linewidths=1.2, zorder=3)
fl_sc = axA.scatter([], [], s=150, marker="*", color="#e69500", edgecolors="k", linewidths=0.4, zorder=4)
ptxt = axA.text(0.12, 1.75, "", fontsize=9.5, fontweight="bold", va="center", zorder=6,
                 bbox=dict(fc="white", ec="none", pad=1.5))
from matplotlib.lines import Line2D
leg = [Line2D([], [], ls="", marker="o", color="0.55", ms=3, label="argon atom (number drawn ∝ p)"),
       Line2D([], [], ls="", marker="o", color="k", ms=5, label="no collision yet"),
       Line2D([], [], ls="", marker="o", mfc="white", mec="k", ms=5, label="hit, still in beam: its stripes gone"),
       Line2D([], [], ls="", marker="x", color="0.45", ms=5, label="hit, knocked out of beam"),
       Line2D([], [], ls="", marker="*", color="#e69500", mec="k", ms=9, label="collision")]
axA.legend(handles=leg, loc="lower center", bbox_to_anchor=(0.5, -0.17), ncol=5, fontsize=7, frameon=False,
           handletextpad=0.3, columnspacing=0.8)

# panel B
x = np.linspace(0, 3 * G, 400)
counts = lambda p: transmitted(p) * (1 + V0 * visibility(p) * np.cos(2 * np.pi * x / G))
axB.plot(x, counts(0), ls="--", color="0.6", lw=1.2, label="p = 0")
lineB, = axB.plot([], [], "k-", lw=2, label="current p")
lineB2, = axB.plot([], [], "k-.", lw=1, label="current p, ÷ arriving fraction")
axB.set_xlim(0, 3 * G); axB.set_ylim(0, 3.05)
axB.set_xlabel("shift of grating 3 (µm)"); axB.set_ylabel("molecules counted\n(relative to p = 0 mean)")
axB.set_title("B  computed: stripes read at grating 3", fontsize=9.5, loc="left")
axB.legend(fontsize=7.5, loc="upper right", frameon=False, handlelength=2.2, borderaxespad=0.2)
btxt = axB.text(0.04, 3.0, "", fontsize=7.5, va="top")

# panel C
pp = np.linspace(0, 3.2, 200)
axC.semilogy(pp, visibility(pp), "k-", lw=1.5)
axC.set_xlim(0, 3.2); axC.set_ylim(0.03, 1.3)
axC.set_yticks([0.05, 0.1, 0.2, 0.5, 1]); axC.set_yticklabels(["0.05", "0.1", "0.2", "0.5", "1"])
axC.axhline(np.exp(-1), ls=":", color="k", lw=1); axC.text(2.25, np.exp(-1) * 1.08, "1/e", fontsize=9)
axC.set_xlabel("gas pressure p / p₀"); axC.set_ylabel("visibility / zero-pressure value\n(log scale)")
axC.set_title("C  computed: V = exp(−p/p₀), a straight line", fontsize=9.5, loc="left")
visited, = axC.plot([], [], "o", mfc="white", mec="k", ms=5)
mark, = axC.plot([], [], "o", color="#c0392b", ms=9, mec="k")

fig.text(0.01, 0.008, "Illustrative model: independent collisions, one collision = full record (overlap 0); half of collisions knock the "
         "molecule out\n(assumed, not measured), so the arriving count also falls as exp(−p/p₀). Ideal stripes (V = 1 at p = 0), sinusoidal. "
         "No data drawn.", fontsize=7.2, color="0.25")

def draw(i):
    p = p_of(i); s = sim[i]
    gas_sc.set_offsets(s["gas"] if len(s["gas"]) else np.empty((0, 2)))
    for sc, st in [(m0, 0), (m1, 1), (m2, 2)]:
        pts = [(a, b) for a, b, c in s["mols"] if c == st]
        sc.set_offsets(np.array(pts) if pts else np.empty((0, 2)))
    fl_sc.set_offsets(np.array(s["flashes"]) if s["flashes"] else np.empty((0, 2)))
    ptxt.set_text(f"pressure p = {p:.1f} p₀      mean collisions per molecule between gratings 1 and 3: {mean_coll(p):.0f}")
    lineB.set_data(x, counts(p)); lineB2.set_data(x, counts(p) / transmitted(p))
    btxt.set_text(f"visibility / V(0) = {visibility(p):.2f}\narriving fraction\n= {transmitted(p):.2f} (illustrative)")
    seen = STEPS[STEPS <= p + 1e-9]
    visited.set_data(seen, visibility(seen)); mark.set_data([p], [visibility(p)])
    return []

anim = FuncAnimation(fig, draw, frames=NF, blit=False)
anim.save(gif, writer=PillowWriter(fps=FPS), dpi=100)
print("saved", gif, os.path.getsize(gif) / 1e6, "MB,", NF, "frames")
for k, i in enumerate([PER * 0 + 6, PER * 2 + 6, NF - 3], start=1):
    draw(i); out = os.path.join(figdir, f"{name}-still-{k}.png"); fig.savefig(out, dpi=100); print("saved", out)
