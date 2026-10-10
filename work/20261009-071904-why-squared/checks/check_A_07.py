# Claims tested:
#  (a) Account 1 cons: with two exits a non-power "wiggle" rule can still total 1.
#  (b) Account 3: "The wiggle of account 1 dies as soon as a third direction can be swapped in".
#  (c) Intro: "once amplitudes are the shadows of an arrow that can be turned, the square is
#      the only rule under which the two exits always add up"; Account 1: "Closing that gap
#      takes the next two accounts"; Account 2: "a world whose amplitudes add, cancel and can
#      be turned a little at a time has to use the square"; Relate: "the turning argument shows
#      ... has no other option, non-integer powers included".
#  Test: does the two-exit wiggle rule survive account 2's conditions (linear changes, smooth turns)?
import numpy as np, sympy as sp
eps = 0.03
g = lambda x: x + eps*np.sin(2*np.pi*x)          # chance of an exit = g(shadow^2)
x = np.linspace(0, 1, 100001)
print("g monotone:", np.all(np.diff(g(x)) > 0), " g in [0,1]:", g(x).min() >= -1e-15 and g(x).max() <= 1 + 1e-15,
      " g(1)=", g(1.0), "(prepared photon passes its own direction every time)")
# (a) two exits, every arrow angle phi and every splitter angle theta
phi = np.linspace(0, 2*np.pi, 721)
tot = g(np.cos(phi)**2) + g(np.sin(phi)**2)
a_ok = np.max(np.abs(tot - 1)) < 1e-12
print(f"(a) two exits: max|total-1| = {np.max(np.abs(tot-1)):.2e}; max departure from cos^2 = {eps:.2f}")
# Survives smooth turns: apply rotation R(t) (linear, acts on sums part by part) to any arrow
ts = np.linspace(0, 0.2, 50)
worst = 0
for t in ts:
    c, s = np.cos(t), np.sin(t)
    vx, vy = c*np.cos(phi) - s*np.sin(phi), s*np.cos(phi) + c*np.sin(phi)
    worst = max(worst, np.max(np.abs(g(vx**2) + g(vy**2) - 1)))
print(f"    after every small turn: max|total-1| = {worst:.2e}  -> wiggle survives account 2's conditions")
# state set {(a,b): g(a^2)+g(b^2)=1} is exactly the unit circle (so 'possible arrows' unchanged)
rng = np.random.default_rng(3)
pts = rng.uniform(-1.5, 1.5, size=(400000, 2))
on = np.abs(g(pts[:, 0]**2) + g(pts[:, 1]**2) - 1) < 1e-3
r = np.hypot(pts[on, 0], pts[on, 1])
print(f"    points with total=1 have radius in [{r.min():.4f}, {r.max():.4f}] (unit circle)")
survives = worst < 1e-12 and abs(r.min()-1) < 2e-3 and abs(r.max()-1) < 2e-3
# (b) three exits: random orthonormal bases in 3D
devs = []
for _ in range(2000):
    Q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    psi = rng.normal(size=3); psi /= np.linalg.norm(psi)
    devs.append(abs(sum(g((Q[:, i] @ psi)**2) for i in range(3)) - 1))
print(f"(b) three exits: max|total-1| over random bases = {max(devs):.4f}  -> wiggle inconsistent")
X, Y = sp.symbols('x y'); G = sp.Function('g')
expr = G(X) + G(Y) + G(1 - X - Y) - 1
dx, dy = sp.diff(expr, X), sp.diff(expr, Y)
print("    d/dx:", dx, "  d/dy:", dy, " => g'(x)=g'(y)=g'(1-x-y): g' constant, g affine; g(1)=1 and 3g(1/3)=1 => g(x)=x")
b_ok = max(devs) > 1e-3
print("(a) PASS" if a_ok else "(a) FAIL")
print("(b) PASS" if b_ok else "(b) FAIL")
print("(c) FAIL: a non-power rule obeys 'amplitudes add, turn smoothly, two exits total 100%';"
      " turning excludes only other POWERS (incl. non-integer); non-power rules need account 3" if survives else "(c) PASS")
