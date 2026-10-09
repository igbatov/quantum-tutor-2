"""Animation decoherence-2d: a real 2D Schroedinger simulation of a double slit,
drawn in the style of Dan Schroeder's QuantumScattering2D (black background,
hue = phase of psi, brightness = |psi|).

Model (hbar = m = 1, grid spacing 1):
  - 512 x 512 grid, split-step Fourier (Strang splitting, numpy/scipy FFT), dt = 0.25.
  - Complex absorbing potential (quadratic ramp, 40 cells) on all four edges.
  - Gaussian packet moving down (+y), wavelength 6 cells, toward a wall (6 cells
    thick, V0 = 5 >> E = 0.55) with two slits: width 18, centre separation 72 = 4 x width.
  - Evolve the full packet until the slits are empty (probability in the slit
    channels < 1e-3 of its peak): time t1. Then cut the wave below the wall into
    psi_L (x < 0) and psi_R (x > 0) and evolve each on its own. The full uncut wave
    and the unsplit transmitted wave are evolved too, for the linearity checks.
  - Panel 1 (no record): psi_L + psi_R, hue = phase, brightness = |psi|.
  - Panel 2 (one photon, perfect record, <E_L|E_R> = 0): after t1 the particle is
    entangled, so it has no single wavefunction; drawn as white brightness
    sqrt(|psi_L|^2 + |psi_R|^2) only (same brightness scale as panel 1).
  - Reflected part (above the wall) fades out over 8 frames after t1 (both panels), then is not shown.
  - Screen strips: time-integrated density on the row y_s (near the bottom edge),
    plus dots sampled from the density as it arrives.
Checks printed: norm conservation before absorption, linearity
||(psi_L+psi_R) - psi_trans||, cut leftover vs the uncut full evolution,
visibility near the centre for c = 1 (no record), c = 0 (perfect record), c = 0.5.
"""
import os
import time
import numpy as np
import scipy.fft as sfft
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from matplotlib.patches import Circle

RUN = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(RUN, "figures")
os.makedirs(FIG, exist_ok=True)
CACHE = os.environ.get("DECO2D_CACHE")  # optional cache path for development

# ---------------- grid and potential ----------------
N = 512
dt = 0.25
x1 = np.arange(N) - N / 2 + 0.5          # transverse coordinate, symmetric about 0
y1 = np.arange(N, dtype=float)           # propagation coordinate (row index)
X, Y = np.meshgrid(x1, y1)               # arrays indexed [row=y, col=x]

lam = 6.0
k0 = 2 * np.pi / lam
E0 = k0 ** 2 / 2
V0 = 5.0
wall_top, wall_bot = 200, 206            # rows 200..205
slit_w, slit_sep = 18.0, 72.0
in_slit = (np.abs(np.abs(X) - slit_sep / 2) < slit_w / 2)
wall = (Y >= wall_top) & (Y < wall_bot) & ~in_slit
V = np.where(wall, V0, 0.0)

W = 40                                   # absorbing layer
eta = 0.3
def ramp(d):
    s = np.clip((W - d) / W, 0, 1)
    return s ** 2
dist_edge = np.minimum.reduce([X - x1[0], x1[-1] - X, Y - y1[0], y1[-1] - Y])
cap = eta * ramp(dist_edge)
in_cap = dist_edge < W

kx = 2 * np.pi * sfft.fftfreq(N)
KX, KY = np.meshgrid(kx, kx)
expK = np.exp(-1j * dt * (KX ** 2 + KY ** 2) / 2)
expV = np.exp(-1j * V * dt / 2) * np.exp(-cap * dt / 2)


def step(psi):
    psi = expV * psi
    psi = sfft.ifft2(expK * sfft.fft2(psi, axes=(-2, -1), workers=-1), axes=(-2, -1), workers=-1)
    return expV * psi


# ---------------- initial packet ----------------
y0, sx, sy = 112.0, 50.0, 12.0
psi = np.exp(-X ** 2 / (2 * sx ** 2) - (Y - y0) ** 2 / (2 * sy ** 2) + 1j * k0 * Y)
psi /= np.sqrt(np.sum(np.abs(psi) ** 2))

ys = 455                                  # screen row
XC = 24                                   # extra side margin hidden (keeps the GIF < 5 MB)
cropy = slice(W, N - W)                   # displayed region (absorbing layer hidden)
cropx = slice(W + XC, N - W - XC)
nf = 13                                   # steps per frame (frame interval 3.25)
chan = (Y >= wall_top) & (Y < wall_bot) & in_slit
below = Y >= wall_bot


def run_sim():
    t0 = time.time()
    p = psi.copy()
    frames = []                           # list of (t, kind, data...)
    norm0 = np.sum(np.abs(p) ** 2)
    norm_dev, cap_prob = 0.0, 0.0
    pchan_peak, t = 0.0, 0.0
    nstep = 0
    while True:
        if nstep % nf == 0:
            pc = np.sum(np.abs(p[chan]) ** 2)
            pchan_peak = max(pchan_peak, pc)
            frames.append(dict(t=t, kind="pre", full=p[cropy, cropx].astype(np.complex64)))
            if pchan_peak > 0.01 and pc < 1e-3 * pchan_peak:
                break
        p = step(p)
        t += dt
        nstep += 1
        n = np.sum(np.abs(p) ** 2)
        norm_dev = max(norm_dev, abs(n / norm0 - 1))
        cap_prob = max(cap_prob, np.sum(np.abs(p[in_cap]) ** 2))
    t1 = t
    frames[-1]["kind"] = "split"
    trans = np.where(below, p, 0)
    L = np.where(X < 0, trans, 0)
    R = np.where(X > 0, trans, 0)
    P_trans = np.sum(np.abs(trans) ** 2)
    P_refl_t1 = np.sum(np.abs(p[~below]) ** 2)
    P_cut_line = np.sum(np.abs(trans[:, (np.abs(x1) < 5)]) ** 2) / P_trans
    print(f"[sim] t1 = {t1:.2f}, steps {nstep}, {time.time()-t0:.1f}s")
    S = np.stack([p, trans, L, R])        # full uncut, unsplit transmitted, L, R
    acc = {k: np.zeros(N) for k in ("nr", "rec", "half")}
    lin_err, cut_left = 0.0, 0.0
    post_steps = 0
    max_post = int(360 / dt)
    while True:
        if post_steps % nf == 0:
            f, tr, l, r = S
            lr = l + r
            frames.append(dict(t=t, kind="post",
                               lr=lr[cropy, cropx].astype(np.complex64),
                               rec=np.sqrt(np.abs(l[cropy, cropx]) ** 2 + np.abs(r[cropy, cropx]) ** 2).astype(np.float32),
                               full_amp=np.abs(f[cropy, cropx]).astype(np.float32),
                               acc_nr=acc["nr"].copy(), acc_rec=acc["rec"].copy()))
            lin_err = max(lin_err, np.sqrt(np.sum(np.abs(lr - tr) ** 2) / np.sum(np.abs(tr) ** 2)))
            nb = np.sqrt(np.sum(np.abs(lr[below]) ** 2))
            if nb > 0:
                cut_left = max(cut_left, np.sqrt(np.sum(np.abs((f - lr)[below]) ** 2)) / nb)
            remaining = np.sum(np.abs(lr[(Y >= wall_bot) & (Y < ys)]) ** 2) / P_trans
            if post_steps >= max_post or (post_steps > 0 and remaining < 0.02):
                break
        S = step(S)
        t += dt
        post_steps += 1
        l, r = S[2][ys], S[3][ys]
        acc["nr"] += np.abs(l + r) ** 2 * dt
        acc["rec"] += (np.abs(l) ** 2 + np.abs(r) ** 2) * dt
        acc["half"] += (np.abs(l) ** 2 + np.abs(r) ** 2 + 2 * 0.5 * np.real(np.conj(l) * r)) * dt
    print(f"[sim] end t = {t:.2f}, {len(frames)} frames, {time.time()-t0:.1f}s, remaining {remaining:.3f}")
    stats = dict(t1=t1, norm_dev=norm_dev, cap_prob=cap_prob, lin_err=lin_err, cut_left=cut_left,
                 P_trans=P_trans, P_refl_t1=P_refl_t1, P_cut_line=P_cut_line,
                 arrived_frac=np.sum(acc["nr"] * k0) / P_trans)  # flux ~ k0 * density
    return frames, acc, stats


frames, acc, stats = run_sim()
if CACHE:
    np.savez(CACHE, **acc)

# ---------------- checks ----------------
xs = x1


def visibility(P, half_window):
    m = np.abs(xs) < half_window
    return (P[m].max() - P[m].min()) / (P[m].max() + P[m].min())


fringe = lam * (ys - wall_bot) / slit_sep          # rough far-field spacing estimate
hw = 1.2 * fringe
V_nr, V_rec, V_half = (visibility(acc[k], hw) for k in ("nr", "rec", "half"))
print("=== checks ===")
print(f"norm drift before t1 (no absorption yet): max |N(t)/N(0) - 1| = {stats['norm_dev']:.2e}"
      f"  (prob. inside absorbing layer <= {stats['cap_prob']:.1e})")
print(f"t1 = {stats['t1']:.2f}; transmitted {stats['P_trans']:.3f}, reflected {stats['P_refl_t1']:.3f};"
      f" fraction of transmitted prob within |x|<5 of the cut line: {stats['P_cut_line']:.2e}")
print(f"linearity: max_t ||(psi_L+psi_R) - psi_trans|| / ||psi_trans|| = {stats['lin_err']:.2e}")
print(f"cut leftover: max_t ||(psi_full - (psi_L+psi_R)) below wall|| / ||psi_L+psi_R below wall|| = {stats['cut_left']:.2e}")
print(f"visibility on screen row y={ys}, |x| < {hw:.1f}: no record {V_nr:.3f}, perfect record {V_rec:.3f}, c=0.5 {V_half:.3f}")
vis = (np.abs(xs) <= x1[N - W - XC - 1])
for key in ("nr", "rec"):
    P = acc[key][vis]
    mx = np.sum((P[1:-1] > P[:-2]) & (P[1:-1] > P[2:]) & (P[1:-1] > 0.05 * P.max()))
    mn = np.sum((P[1:-1] < P[:-2]) & (P[1:-1] < P[2:]) & (P[1:-1] > 0.05 * P.max()))
    print(f"screen curve '{key}': {mx} local maxima, {mn} local minima (above 5% of its max, shown range)")
print(f"fraction of transmitted probability that crossed the screen row (flux est.): {stats['arrived_frac']:.2f}")
ok = (stats['norm_dev'] < 1e-6 and stats['lin_err'] < 1e-10 and V_nr > 0.9 and V_rec < 0.1)
print("PASS" if ok else "FAIL")

# ---------------- rendering ----------------
nfr = len(frames)
i_split = next(i for i, f in enumerate(frames) if f["kind"] == "split")
ncropx = N - 2 * W - 2 * XC
yc = y1[cropy]
wall_c = wall[cropy, cropx]
above_c = (yc < wall_bot)[:, None] * np.ones((1, ncropx), bool)
below_c = ~above_c

# brightness scale: same for both panels in a frame, smoothed in time
A_tr = np.zeros(nfr)
A_all = np.zeros(nfr)
for i, f in enumerate(frames):
    if f["kind"] == "post":
        A_tr[i] = np.abs(f["lr"][below_c]).max()
        A_all[i] = f["full_amp"].max()
    else:
        a = np.abs(f["full"])
        A_tr[i] = a[below_c].max()
        A_all[i] = a.max()
A_raw = np.maximum(A_tr, 0.8 * A_all * (np.arange(nfr) <= i_split))
A_raw = np.maximum(A_raw, 1e-12)
# after t1 the scale never grows (fading waves stay faded), but it stops shrinking once
# the main part of the wave reaches the screen row (peak arrival rate)
arr = np.array([f["acc_nr"].sum() if f["kind"] == "post" else 0.0 for f in frames])
i_peak = int(np.argmax(np.diff(arr))) + 1
A_raw[i_split:] = np.minimum.accumulate(A_raw[i_split:])
A_raw[i_peak:] = A_raw[i_peak]
la = np.log(A_raw)
ker = np.ones(5) / 5
A_ref = np.exp(np.convolve(np.pad(la, 2, mode="edge"), ker, mode="valid"))
A_ref *= 0.85                              # let the brightest parts saturate a little


VMIN = 0.05


def phase_rgb(z, scale):
    h = (np.angle(z) + np.pi) / (2 * np.pi)
    v = np.clip(np.abs(z) / scale, 0, 1)
    v[v < VMIN] = 0                        # very faint tails drawn black (keeps the GIF small)
    return hsv_to_rgb(np.dstack([h, np.ones_like(h), v]))


def grey_rgb(a, scale):
    v = np.clip(a / scale, 0, 1)
    v[v < VMIN] = 0
    return np.dstack([v, v, v])


WALL_RGB = np.array([0.6, 0.6, 0.6])
FADE = 8                                   # frames over which the reflected part fades out after t1


def render(i):
    f = frames[i]
    s = A_ref[i]
    if f["kind"] != "post":
        img = phase_rgb(f["full"], s)
        left, right = img, img.copy()
    else:
        dim = max(0.0, 0.5 * (1 - (i - i_split) / FADE))
        refl_grey = grey_rgb(f["full_amp"], s) * dim
        left = phase_rgb(f["lr"], s)
        right = grey_rgb(f["rec"], s)
        refl = refl_grey
        left[above_c] = refl[above_c]
        right[above_c] = refl[above_c]
    for im in (left, right):
        im[wall_c] = WALL_RGB
    return np.clip(left, 0, 1), np.clip(right, 0, 1)


# hits: dots drawn from the density as it arrives on the screen row
rng = np.random.default_rng(7)
N_HITS = 2500
tot_nr = acc["nr"].sum()
hits = {"nr": [], "rec": []}
hit_x = {"nr": np.zeros(0), "rec": np.zeros(0)}
hit_y = {"nr": np.zeros(0), "rec": np.zeros(0)}
carry = {"nr": 0.0, "rec": 0.0}
prev = {"nr": np.zeros(N), "rec": np.zeros(N)}
hits_per_frame = []
for i, f in enumerate(frames):
    if f["kind"] == "post":
        for key, a in (("nr", f["acc_nr"]), ("rec", f["acc_rec"])):
            d = np.clip(a - prev[key], 0, None)
            prev[key] = a
            want = N_HITS * d.sum() / tot_nr + carry[key]
            n = int(want)
            carry[key] = want - n
            if n > 0:
                xs_new = rng.choice(xs, size=n, p=d / d.sum()) + rng.uniform(-0.5, 0.5, n)
                hit_x[key] = np.concatenate([hit_x[key], xs_new])
                hit_y[key] = np.concatenate([hit_y[key], rng.uniform(0.04, 0.40, n)])
    hits_per_frame.append((len(hit_x["nr"]), len(hit_x["rec"])))
# last frame: flush remaining density (final accumulation) so totals match
for key in ("nr", "rec"):
    d = np.clip(acc[key] - prev[key], 0, None)
    n = int(N_HITS * d.sum() / tot_nr + carry[key])
    if n > 0:
        hit_x[key] = np.concatenate([hit_x[key], rng.choice(xs, size=n, p=d / d.sum()) + rng.uniform(-0.5, 0.5, n)])
        hit_y[key] = np.concatenate([hit_y[key], rng.uniform(0.04, 0.40, n)])
final_counts = (len(hit_x["nr"]), len(hit_x["rec"]))

HOLD = 30
seq = list(range(nfr)) + [nfr - 1] * HOLD
P_scale = acc["nr"].max()

plt.rcParams.update({"font.size": 10})
FW, FH = 860, 680                         # figure size in pixels (dpi 100)
PH = N - 2 * W                             # panel size in pixels = simulation cells shown (1:1)
PW = N - 2 * W - 2 * XC
fig = plt.figure(figsize=(FW / 100, FH / 100), dpi=100, facecolor="black")
def px(x0, y0, w, h):
    return [x0 / FW, y0 / FH, w / FW, h / FH]
ext = [x1[W + XC] - 0.5, x1[N - W - XC - 1] + 0.5, y1[N - W - 1] + 0.5, y1[W] - 0.5]
axL = fig.add_axes(px(30, 132, PW, PH))
axR = fig.add_axes(px(FW - 30 - PW, 132, PW, PH))
sL = fig.add_axes(px(30, 10, PW, 112))
sR = fig.add_axes(px(FW - 30 - PW, 10, PW, 112))
wheel = fig.add_axes(px(6, FH - 84, 76, 76))
for a in (axL, axR, sL, sR):
    a.set_facecolor("black")
    a.set_xticks([]); a.set_yticks([])
    for sp in a.spines.values():
        sp.set_color("0.4")

# phase colour wheel
g = np.linspace(-1, 1, 101)
GX, GY = np.meshgrid(g, g)
r = np.hypot(GX, GY)
wimg = hsv_to_rgb(np.dstack([(np.arctan2(GY, GX) + np.pi) / (2 * np.pi), np.ones_like(r), np.clip(r, 0, 1)]))
wimg[r > 1] = 0
wheel.imshow(wimg, origin="lower", extent=[-1, 1, -1, 1])
wheel.set_axis_off()
wheel.text(1.15, 0.0, "hue = phase\nbrightness = |ψ|", color="white", fontsize=8, va="center", ha="left",
           transform=wheel.transData)

fig.text(0.5, 1 - 22 / FH, "Double slit, 2D Schrödinger simulation", color="white", ha="center", fontsize=13,
         weight="bold")
fig.text(0.5, 1 - 48 / FH, "right panel: one photon scatters at the slits and records the path",
         color="0.85", ha="center", fontsize=9)
axL.set_title("1. No record", color="white", fontsize=11)
axR.set_title("2. Photon scattered at the slits\n(perfect record, ⟨E_L|E_R⟩ = 0)", color="white", fontsize=10)

L0, R0 = render(0)
imL = axL.imshow(L0, extent=ext, interpolation="nearest")
imR = axR.imshow(R0, extent=ext, interpolation="nearest")
for a in (axL, axR):
    a.axhline(ys, color="0.55", lw=0.8, ls=(0, (3, 3)))
    a.text(ext[1] - 4, ys - 4, "screen row", color="0.7", fontsize=7.5, ha="right", va="bottom")
    a.set_xlim(ext[0], ext[1]); a.set_ylim(ext[2], ext[3])
tlab = axL.text(ext[0] + 6, ext[3] + 6, "", color="white", fontsize=8, va="top")
note = axR.text(0, 75, "", color="white", fontsize=8.5, ha="center", va="center",
                bbox=dict(facecolor="black", edgecolor="0.5", alpha=0.75, boxstyle="round,pad=0.3"))
refl_note = axL.text(ext[0] + 6, wall_top - 6, "", color="0.75", fontsize=7.5, va="bottom")
photon_lab = axR.text(0, wall_top - 40, "", color="yellow", fontsize=8.5, ha="center", va="bottom")
rings = [Circle((sgn * slit_sep / 2, wall_bot), 1, fill=False, ec="yellow", lw=1.4, ls="--", visible=False)
         for sgn in (-1, 1)]
for c in rings:
    axR.add_patch(c)

for a, key, lab in ((sL, "nr", "|ψ_L+ψ_R|²"), (sR, "rec", "|ψ_L|²+|ψ_R|²")):
    a.set_xlim(ext[0], ext[1]); a.set_ylim(0, 1.0)
    a.text(ext[0] + 5, 0.93, f"screen: {lab} summed over time; dots = single hits", color="0.85",
           fontsize=7.5, va="top")
lineL, = sL.plot([], [], color="white", lw=1.4)
lineR, = sR.plot([], [], color="white", lw=1.4)
dotL = sL.scatter([], [], s=1.2, c="white", lw=0)
dotR = sR.scatter([], [], s=1.2, c="white", lw=0)
cntL = sL.text(ext[1] - 5, 0.93, "", color="0.85", fontsize=7.5, va="top", ha="right")
cntR = sR.text(ext[1] - 5, 0.93, "", color="0.85", fontsize=7.5, va="top", ha="right")


def curve(a):
    return 0.45 + 0.4 * a / P_scale


def update(j):
    i = seq[j]
    f = frames[i]
    Li, Ri = render(i)
    imL.set_data(Li); imR.set_data(Ri)
    tlab.set_text(f"t = {f['t']:.0f}  (ħ = m = 1)")
    post = f["kind"] == "post"
    if post:
        note.set_text("after the photon: the particle alone has no single phase\n"
                      "(entangled with the photon), so only density is drawn (white)")
        refl_note.set_text("reflected part: fading out" if i - i_split < FADE else "reflected part: not shown")
        k = i - i_split
        for c in rings:
            c.set_visible(1 <= k <= 12)
            c.set_radius(8 + 9 * k)
            c.set_alpha(max(0.0, 1 - k / 13))
        photon_lab.set_text("photon leaves from L or R (schematic)" if 1 <= k <= 14 else "")
        last = j >= nfr - 1
        a_nr = acc["nr"] if last else f["acc_nr"]
        a_rec = acc["rec"] if last else f["acc_rec"]
        lineL.set_data(xs, curve(a_nr)); lineR.set_data(xs, curve(a_rec))
        nL, nR = final_counts if last else hits_per_frame[i]
    else:
        note.set_text("" if i < i_split else "")
        refl_note.set_text("")
        for c in rings:
            c.set_visible(False)
        photon_lab.set_text("")
        lineL.set_data([], []); lineR.set_data([], [])
        nL, nR = 0, 0
    dotL.set_offsets(np.c_[hit_x["nr"][:nL], hit_y["nr"][:nL]] if nL else np.zeros((0, 2)))
    dotR.set_offsets(np.c_[hit_x["rec"][:nR], hit_y["rec"][:nR]] if nR else np.zeros((0, 2)))
    cntL.set_text(f"{nL} hits"); cntR.set_text(f"{nR} hits")
    return []


still_frames = {"start": i_split - 14, "photon": i_split + 6, "end": len(seq) - 1}
for name, j in still_frames.items():
    update(j)
    fig.savefig(os.path.join(FIG, f"decoherence-2d-still-{name}.png"), dpi=100, facecolor="black")

# GIF: render each frame with matplotlib, then one global palette and no dithering
# (dithering noise on the black background would make the file several times larger)
from PIL import Image
def grab(j):
    update(j)
    fig.canvas.draw()
    return np.asarray(fig.canvas.buffer_rgba())[..., :3].copy()
rgb = [grab(j) for j in range(nfr)]
# fixed palette: 48 greys, 24 hues x 7 brightness levels, 8 yellows (photon ring)
pal_cols = [(g, g, g) for g in np.linspace(0, 255, 48).astype(int)]
for v in np.linspace(1 / 7, 1, 7):
    for h in np.arange(24) / 24:
        pal_cols.append(tuple((255 * hsv_to_rgb([h, 1.0, v])).astype(int)))
pal_cols += [(int(255 * v), int(255 * v), 0) for v in np.linspace(0.3, 1, 8)]
flat = [c for col in pal_cols for c in col]
flat += [0] * (768 - len(flat))
pal = Image.new("P", (1, 1))
pal.putpalette(flat)
pimgs = [Image.fromarray(a).quantize(palette=pal, dither=Image.Dither.NONE) for a in rgb]
durations = [int(1000 / 15)] * (nfr - 1) + [int(1000 / 15) * (HOLD + 1)]
out = os.path.join(FIG, "decoherence-2d.gif")
pimgs[0].save(out, save_all=True, append_images=pimgs[1:], duration=durations, loop=0, optimize=False)
print(f"saved {out}: {os.path.getsize(out)/1e6:.2f} MB, {nfr} frames at 15 fps, last frame held {HOLD/15:.0f} s extra, {FW}x{FH} px")
print(f"hits: no record {final_counts[0]}, perfect record {final_counts[1]}")
