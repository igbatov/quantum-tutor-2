# Claim: "add up the amplitudes for all the ways through the left slit into one combined
# amplitude ... add the two; that is exactly the sum over every way, just sorted by slit."
# Check: (a) summing many points across each slit (Fraunhofer phase), grouped per slit then added,
# reproduces the figures' pattern 4 sinc^2(X/4) cos^2(pi X); (b) grouping equals summing all at once;
# (c) symbolic: exact integral over each slit gives the same formula.
import numpy as np, sympy as sp
d, a = 1.0, 0.25                     # slit spacing (centre to centre) = 4 slit widths
X = np.linspace(-14, 14, 5601)       # screen position in units of stripe spacing (lambda L / d)
def ways(centre, N):                 # N points (midpoint rule) across a slit of width a
    return centre + a*((np.arange(N) + 0.5)/N - 0.5)
ok = True
for N in (10, 100, 1000):
    yL, yR = ways(-d/2, N), ways(+d/2, N)
    amp = lambda ys: np.exp(-2j*np.pi*np.outer(X, ys)/d).sum(axis=1)/N   # phase from path-length difference
    psiL, psiR = amp(yL), amp(yR)
    grouped = psiL + psiR
    rng = np.random.default_rng(0); allpts = rng.permutation(np.concatenate([yL, yR]))
    at_once = amp(allpts)                                                 # every way, unsorted
    ref = 4*np.sinc(X/4)**2*np.cos(np.pi*X)**2
    e_group = np.max(np.abs(grouped - at_once)); e_pat = np.max(np.abs(np.abs(grouped)**2 - ref))
    print(f"N={N:5d} per slit: max|grouped - all-at-once| = {e_group:.1e}; max|P - 4sinc^2cos^2| = {e_pat:.1e}")
    ok &= e_group < 1e-12
ok &= e_pat < 1e-5
# symbolic, continuum of ways
y, x = sp.symbols('y x', real=True)
f = sp.exp(-2*sp.I*sp.pi*x*y)
psiL = sp.integrate(f, (y, -sp.Rational(5,8), -sp.Rational(3,8)))/sp.Rational(1,4)
psiR = sp.integrate(f, (y, sp.Rational(3,8), sp.Rational(5,8)))/sp.Rational(1,4)
whole = sp.integrate(f, (y, -sp.Rational(5,8), -sp.Rational(3,8))) + sp.integrate(f, (y, sp.Rational(3,8), sp.Rational(5,8)))
diff_group = sp.simplify(psiL + psiR - whole/sp.Rational(1,4))
P = sp.simplify(sp.expand_complex((psiL + psiR)*sp.conjugate(psiL + psiR)))
target = 4*(sp.sin(sp.pi*x/4)/(sp.pi*x/4))**2*sp.cos(sp.pi*x)**2
vals = [abs(float((P - target).subs(x, v))) for v in (0.13, 0.5, 1.7, 3.3, 5.72, 9.1)]
print("symbolic: grouped - whole =", diff_group, "; |P - target| at sample points:", max(vals))
ok &= diff_group == 0 and max(vals) < 1e-12
# combined per-slit amplitudes at dark / bright stripes
for xv in (0.5, 1.5, 1.0, 2.0):
    l, r = complex(psiL.subs(x, xv).evalf()), complex(psiR.subs(x, xv).evalf())
    print(f"X={xv}: psiL={l:.4f}, psiR={r:.4f}, psiL/psiR={l/r:.4f}")
print("PASS" if ok else "FAIL")
