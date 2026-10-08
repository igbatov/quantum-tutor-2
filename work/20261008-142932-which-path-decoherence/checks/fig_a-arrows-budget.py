import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-arrows-budget.png"
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.8))
th = np.radians(60); A = np.array([1, 0]); B = np.array([np.cos(th), np.sin(th)])
for v, lab, off in [(A, "tag after left slit", (0.02, -0.09)), (B, "tag after right slit", (-0.25, 0.05))]:
    a1.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", lw=2.2, color="k"))
    a1.text(v[0]+off[0], v[1]+off[1], lab, fontsize=9)
h = (A+B)/np.linalg.norm(A+B); a1.plot([0, 1.15*h[0]], [0, 1.15*h[1]], "k--", lw=1.2)
a1.text(1.15*h[0]-0.1, 1.15*h[1]+0.04, "halfway direction\n(erasing measures along this)", fontsize=8.5)
proj = B[0]*A
a1.plot([B[0], B[0]], [0, B[1]], ":", color="tab:red", lw=2)
a1.plot([0, proj[0]], [0, 0], color="tab:blue", lw=6, alpha=0.5, solid_capstyle="butt")
a1.text(0.0, -0.17, "overlap = cos θ = stripe strength = 0.5", color="tab:blue", fontsize=9)
a1.text(B[0]+0.03, 0.12, "sin θ = telling-apart\npower ≈ 0.87", color="tab:red", fontsize=9)
t = np.linspace(0, th, 50); a1.plot(0.2*np.cos(t), 0.2*np.sin(t), "k-", lw=1); a1.text(0.22, 0.07, "θ = 60°")
a1.set_xlim(-0.1, 1.45); a1.set_ylim(-0.25, 1.05); a1.set_aspect("equal"); a1.axis("off")
a1.set_title("The tag's two end states (abstract state space)")
t = np.linspace(0, np.pi/2, 300); a2.plot(np.cos(t), np.sin(t), "k-", lw=2.5, label="ideal tag: V² + D² = 1")
a2.fill_between(np.cos(t), 0, np.sin(t), color="gray", alpha=0.2, hatch="//", edgecolor="gray", label="allowed for imperfect tags (V² + D² < 1)")
for (x, y, lab, dx, dy) in [(1, 0, "θ = 0:\nno record", 0.03, 0.04), (0.5, np.sqrt(3)/2, "θ = 60°: last time's middle panel", 0.03, 0.05), (0, 1, "θ = 90°: perfect record", 0.03, 0.03)]:
    a2.plot(x, y, "ko", ms=7); a2.text(x+dx, y+dy, lab, fontsize=8.5)
a2.set_xlim(0, 1.35); a2.set_ylim(0, 1.35); a2.set_aspect("equal")
a2.set_xlabel("stripe strength V (contrast, 0 to 1)"); a2.set_ylabel("telling-apart power D (0 to 1)")
a2.legend(loc="upper right", fontsize=7.5, bbox_to_anchor=(1.0, 1.0)); a2.set_title("The budget")
fig.text(0.01, 0.005, "Equality holds for an ideal tag (a definite tag state per slit, equal chances for the two slits); real tags fall on or inside the quarter circle;\n"
         "the 1998 atom data fell on or inside it. θ is the angle between the tag's two end states in its abstract state space, not an angle in the laboratory.", fontsize=8)
fig.tight_layout(rect=(0, 0.07, 1, 1)); fig.savefig(OUT, dpi=150); print(OUT)
