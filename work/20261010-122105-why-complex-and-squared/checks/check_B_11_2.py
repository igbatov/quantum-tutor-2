# Claims: f(x) = x^2 + eps x^2(1-x^2)(2x^2-1): "f(cos) + f(sin) = 1"; "f(0)=0, f(1)=1"; "non-negative for |eps|<1"
# with the factor "between -1 and 1/8"; three levels "1/3 - 2 eps/27", total "1 - 2 eps/9";
# Gleason: "adding that a state prepared in a level is found in it with certainty leaves the squared shadow itself".
import sympy as sp, numpy as np
x, th, e = sp.symbols('x theta epsilon', real=True)
f = lambda y: y**2 + e*y**2*(1-y**2)*(2*y**2-1)
ok = sp.simplify(sp.expand_trig(f(sp.cos(th)) + f(sp.sin(th)) - 1)) == 0
C, S = sp.symbols('C S'); ok &= sp.simplify((C*S*(2*C-1) + S*C*(2*S-1)).subs(S, 1-C)) == 0
ok &= f(0) == 0 and sp.simplify(f(1) - 1) == 0
g = (1-x**2)*(2*x**2-1); xs = np.linspace(0, 1, 100001); gv = sp.lambdify(x, g)(xs)
print("factor range on [0,1]:", gv.min(), gv.max()); ok &= abs(gv.min()+1) < 1e-12 and abs(gv.max()-1/8) < 1e-9
for ev in np.linspace(-0.999, 0.999, 41):
    ok &= np.all(xs**2*(1 + ev*gv) >= -1e-15)
f3 = sp.simplify(f(1/sp.sqrt(3))); print("f(1/sqrt3) =", f3)
ok &= sp.simplify(f3 - (sp.Rational(1,3) - 2*e/27)) == 0 and sp.simplify(3*f3 - (1 - 2*e/9)) == 0
# Gleason rider: rho >= 0, tr rho = 1, <psi|rho|psi> = 1  =>  rho = |psi><psi|
rng = np.random.default_rng(0); psi = np.array([1, 0, 0], complex)
for _ in range(200):
    B = rng.normal(size=(3,3)) + 1j*rng.normal(size=(3,3)); rho = B @ B.conj().T; rho /= np.trace(rho).real
    # mix toward psi and check that p(psi)=1 occurs only for the pure projector
    for lam in [0.5, 0.9, 0.999]:
        r = lam*np.outer(psi, psi.conj()) + (1-lam)*rho
        ok &= np.vdot(psi, r @ psi).real < 1 - 1e-12 or np.allclose(r, np.outer(psi, psi.conj()))
print("PASS" if ok else "FAIL")
