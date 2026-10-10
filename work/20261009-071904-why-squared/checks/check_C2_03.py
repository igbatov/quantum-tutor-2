# Figure captions vs computed data (final-C).
#  c-three-slits: "A+B and B+C are identical, with stripes one unit apart"; "A+C ... half a unit apart";
#  "each reaches 4 at the centre"; "9 at the centre"; faint stripe "about 1 near the centre, lower further out";
#  "zeros a third and two thirds of the way"; square leftover "zero at every point"; cube "6 at the centre,
#  swinging between positive and negative"; plain size "never negative" (zeros: check_C2_02).
#  c-square-of-a-sum: "(9, 4 and 1)", "(6, 3 and 2, each twice)", dashed A+B block, "six dark boxes, each a.b.c = 6".
import numpy as np, itertools, sympy as sp
u = np.linspace(-3, 3, 60001); s = u/4
env = np.sinc(s); w = np.exp(2j*np.pi*u)
A, B, C = env/w, env, env*w
P = lambda z, p=2: np.abs(z)**p
ok = True
ok &= np.max(np.abs(P(A)-P(B))) < 1e-12 and np.max(np.abs(P(C)-P(B))) < 1e-12
ok &= np.max(np.abs(P(A+B)-P(B+C))) < 1e-12
def minima(y):
    i = np.where((y[1:-1] < y[:-2]) & (y[1:-1] < y[2:]) & (y[1:-1] < 1e-3))[0]+1
    return u[i]
mAB, mAC, mABC = minima(P(A+B)), minima(P(A+C)), minima(P(A+B+C))
print("A+B zero spacing:", np.round(np.diff(mAB), 3)[:3], " A+C zero spacing:", np.round(np.diff(mAC), 3)[:3])
print("A+B peaks spacing ~1, A+C ~0.5; centre values:", P(A+B)[30000], P(A+C)[30000], P(A+B+C)[30000])
ok &= np.allclose(np.diff(mAB), 1, atol=2e-3) and np.allclose(np.diff(mAC), 0.5, atol=2e-3)
ok &= abs(P(A+B)[30000]-4) < 1e-9 and abs(P(A+C)[30000]-4) < 1e-9 and abs(P(A+B+C)[30000]-9) < 1e-9
fr = np.mod(mABC, 1); print("A+B+C zeros, fractional positions:", sorted(set(np.round(fr, 3))))
ok &= set(np.round(fr, 2)) <= {0.33, 0.67}
for x in [0.5, 1.5, 2.5]:
    print(f"faint stripe height at u={x}: {P(A+B+C)[np.argmin(abs(u-x))]:.3f}")
f = [P(A+B+C)[np.argmin(abs(u-x))] for x in [0.5, 1.5, 2.5]]
ok &= 0.85 < f[0] < 1.05 and f[0] > f[1] > f[2]
L = lambda p: P(A+B+C,p)-P(A+B,p)-P(B+C,p)-P(A+C,p)+P(A,p)+P(B,p)+P(C,p)
print("square leftover max:", np.abs(L(2)).max(), " plain min:", L(1).min(), " cube centre:", L(3)[30000], " cube min/max:", L(3).min(), L(3).max())
ok &= np.abs(L(2)).max() < 1e-12 and L(1).min() > -1e-12 and abs(L(3)[30000]-6) < 1e-9 and L(3).min() < -1
# square-of-a-sum figure numbers
a, b, c = 3, 2, 1
diag = [a*a, b*b, c*c]; rect = [a*b, a*c, b*c]
print("diagonal", diag, "rectangles", rect, "total", sum(diag)+2*sum(rect), "A+B block", (a+b)**2, "=", a*a+2*a*b+b*b)
ok &= diag == [9, 4, 1] and rect == [6, 3, 2] and sum(diag)+2*sum(rect) == 36 and (a+b)**2 == a*a+2*a*b+b*b
# boxes of the 3x3x3 cut whose three edges are a, b, c in some order
boxes = [t for t in itertools.product('abc', repeat=3) if sorted(t) == ['a', 'b', 'c']]
print("boxes with edges a,b,c:", len(boxes), "each", a*b*c, "; total volume", 6**3)
ok &= len(boxes) == 6 and a*b*c == 6
# no single-slit or pair run contains the abc term: (x+y)^3 and x^3 have no abc monomial
x, y, z = sp.symbols('a b c')
runs = [x**3, y**3, z**3, (x+y)**3, (y+z)**3, (x+z)**3]
print("abc coefficient in (a+b+c)^3:", sp.Poly(sp.expand((x+y+z)**3), x, y, z).coeff_monomial(x*y*z),
      "; in single/pair runs:", [sp.Poly(sp.expand(r), x, y, z).coeff_monomial(x*y*z) for r in runs])
ok &= all(sp.Poly(sp.expand(r), x, y, z).coeff_monomial(x*y*z) == 0 for r in runs)
print("PASS" if ok else "FAIL")
