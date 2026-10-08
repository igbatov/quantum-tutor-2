# Claim: "about 0.95 at |X| = 0.5 and 0.62 at |X| = 1.5"; dark stripes at X=+-0.5,+-1.5
# and "electrons land there nearly as often as at the hump's peak; with both open, essentially never."
import numpy as np
P1 = lambda X: np.sinc(X/4)**2            # np.sinc(x)=sin(pi x)/(pi x) -> [sin(pi X/4)/(pi X/4)]^2
P2 = lambda X: 4*P1(X)*np.cos(np.pi*X)**2
ok = True
for X, exp in [(0.5, 0.95), (1.5, 0.62)]:
    v = P1(X); ok &= abs(v-exp) < 0.01
    print(f"P1({X}) = {v:.4f} (claimed ~{exp}); two-slit = {P2(X):.2e}")
    ok &= P2(X) < 1e-12 and P2(-X) < 1e-12
# dark stripes are exactly the zeros of cos^2(pi X) in [-2,2]
Xs = np.linspace(-2, 2, 400001)
y = P2(Xs); mins = Xs[1:-1][(y[1:-1] < y[:-2]) & (y[1:-1] < y[2:])]
print("two-slit minima in [-2,2]:", np.round(mins, 4))
ok &= np.allclose(mins, [-1.5, -0.5, 0.5, 1.5], atol=1e-4)
print("one-slit peak P1(0) =", P1(0.0))
print("PASS" if ok else "FAIL")
