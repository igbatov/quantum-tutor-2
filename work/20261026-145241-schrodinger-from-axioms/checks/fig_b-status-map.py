# §5 figure: assumptions -> theorems -> equation, status shown by box style (not colour alone).
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-status-map.png")
fig, ax = plt.subplots(figsize=(8, 4.6)); ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
sty = {"A": dict(boxstyle="square,pad=0.3", fc="#e8eef8", ec="k", lw=1.2, ls="-"),
       "T": dict(boxstyle="round,pad=0.3", fc="#eaf5e6", ec="k", lw=2.2, ls="-"),
       "C": dict(boxstyle="round,pad=0.3", fc="#f6f6f6", ec="k", lw=1.2, ls="--"),
       "V": dict(boxstyle="sawtooth,pad=0.3", fc="#fff4e0", ec="k", lw=1.0),
       "R": dict(boxstyle="round,pad=0.45", fc="#fff8c8", ec="k", lw=2.5)}
def box(x, y, s, k, fs=8.5):
    ax.text(x, y, s, ha="center", va="center", fontsize=fs, bbox=sty[k]); return (x, y)
def arr(p, q, dx0=0.0, dx1=0.0, dy0=0.0, dy1=0.0):
    ax.annotate("", (q[0]+dx1, q[1]+dy1), (p[0]+dx0, p[1]+dy0), arrowprops=dict(arrowstyle="->", lw=1.1, color="0.25"))
ax.text(1.3, 9.7, "assumptions", ha="center", fontsize=10, weight="bold")
ax.text(5.0, 9.7, "theorems", ha="center", fontsize=10, weight="bold")
ax.text(8.6, 9.7, "result", ha="center", fontsize=10, weight="bold")
a1 = box(1.3, 8.7, "A1 linearity\nA2 unitarity", "A")
a3 = box(1.3, 7.2, "A3 composition\n+ time-translation inv.", "A")
a4 = box(1.3, 5.9, "A4 continuity", "A")
g1 = box(1.3, 4.6, "G1 Galilei ops are\nunitary groups (+Wigner)", "A")
gk = box(1.3, 3.2, "Galilean kinematics\n(G2, G4 group law)", "A")
sp_ = box(1.3, 1.9, "spinless (G6)", "A")
vx = box(1.3, 0.7, "local potential V(x)", "A")
s12 = box(5.0, 8.4, "Steps 1–2: dU/dt = AU,\nU = exp(At)  (2×2 shown)", "T")
s3 = box(5.0, 7.0, "Step 3: H = iħA Hermitian\n⇔ U unitary", "T")
st = box(5.0, 5.7, "Stone: infinite dimensions\n(cited)", "C")
kp = box(5.0, 4.4, "[K,P] = iħM,  φ = Mav/ħ\n(2nd order shown; Bargmann cited)", "T")
kh = box(5.0, 3.0, "X = K/M,  [K,H] = iħP\nd⟨X⟩/dt = ⟨P⟩/M", "T")
h0 = box(5.0, 1.7, "H = P²/2M + V(X)\n(Stone–von Neumann cited)", "T")
hb = box(8.6, 7.7, "ħ: unit convention\n+ experiment", "V")
r1 = box(8.6, 5.9, "iħ dψ/dt = Hψ", "R", 10)
r2 = box(8.6, 2.6, "iħ ∂ψ/∂t =\n−(ħ²/2M) ∂²ψ/∂x²\n+ V(x) ψ", "R", 10)
for p in (a1, a3, a4): arr(p, s12, 1.15, -1.25)
arr(a1, s3, 1.15, -1.25); arr(s12, s3, dy0=-0.5, dy1=0.5); arr(s3, st, dy0=-0.5, dy1=0.5)
arr(s3, r1, 1.1, -0.9); arr(hb, r1, dy0=-0.5, dy1=0.4); arr(st, r1, 1.15, -0.9)
arr(g1, kp, 1.25, -1.6); arr(gk, kp, 1.25, -1.6); arr(gk, kh, 1.25, -1.35)
arr(kp, kh, dy0=-0.5, dy1=0.5); arr(kh, h0, dy0=-0.5, dy1=0.5); arr(sp_, h0, 0.8, -1.4); arr(vx, h0, 1.0, -1.4)
arr(h0, r2, 1.3, -1.0); arr(r1, r2, dy0=-0.4, dy1=0.95)
from matplotlib.patches import Patch
hs = [Patch(fc=sty[k]["fc"], ec="k", lw=sty[k]["lw"], ls=sty[k].get("ls", "-"), label=l) for k, l in
      [("A", "assumption (square, thin)"), ("T", "theorem shown here (round, thick)"),
       ("C", "theorem cited (dashed)"), ("V", "convention (zigzag)")]]
ax.legend(handles=hs, loc="lower right", fontsize=7.5, framealpha=1, bbox_to_anchor=(1.0, -0.02))
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
