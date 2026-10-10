# Claims (flow): V terms cancel; intermediate "(i hbar/2m)(psibar psi'' - psi psibar'')"; derivative identity;
# "J = (i hbar/2m)(psi psibar' - psibar psi') = (hbar/m) Im(psibar psi')"; real psi => "J = 0";
# "the equation gives a real psi an imaginary part at once"; plane wave "J = (hbar k/m)|A|^2"; standing wave J = 0;
# "if psi were real at all times ... H psi = 0".
import sympy as sp, numpy as np
x, t = sp.symbols('x t', real=True); hb, m, k = sp.symbols('hbar m k', positive=True)
u = sp.Function('u', real=True)(x, t); v = sp.Function('v', real=True)(x, t); V = sp.Function('V', real=True)(x)
psi = u + sp.I*v; pb = u - sp.I*v
dpsi = (-(hb**2/(2*m))*sp.diff(psi, x, 2) + V*psi)/(sp.I*hb)
dpb = (-(hb**2/(2*m))*sp.diff(pb, x, 2) + V*pb)/(-sp.I*hb)
lhs = sp.expand(pb*dpsi + psi*dpb)
inter = sp.I*hb/(2*m)*(pb*sp.diff(psi, x, 2) - psi*sp.diff(pb, x, 2))
ok = sp.simplify(lhs - inter) == 0
ok &= sp.simplify(sp.diff(pb*sp.diff(psi, x) - psi*sp.diff(pb, x), x) - (pb*sp.diff(psi, x, 2) - psi*sp.diff(pb, x, 2))) == 0
J = sp.I*hb/(2*m)*(psi*sp.diff(pb, x) - pb*sp.diff(psi, x))
ok &= sp.simplify(lhs + sp.diff(J, x)) == 0
# Im(psibar psi') with psi = u + i v is u v' - v u'
ok &= sp.simplify(sp.expand(J - hb/m*(u*sp.diff(v, x) - v*sp.diff(u, x)))) == 0
ok &= sp.simplify(J.subs(v, 0).doit()) == 0
A = sp.symbols('A'); pw = A*sp.exp(sp.I*k*x)
Jpw = sp.simplify(sp.I*hb/(2*m)*(pw*sp.diff(sp.conjugate(pw), x) - sp.conjugate(pw)*sp.diff(pw, x)))
print("plane-wave J =", Jpw); ok &= sp.simplify(Jpw - hb*k/m*A*sp.conjugate(A)) == 0
sw = sp.cos(k*x); ok &= sp.simplify(sp.I*hb/(2*m)*(sw*sp.diff(sw, x) - sw*sp.diff(sw, x))) == 0
# real Gaussian at t=0 (free): d psi/dt = (i hbar/2m) psi'' is purely imaginary and nonzero
g = sp.exp(-x**2); dg = sp.I*hb/(2*m)*sp.diff(g, x, 2)
ok &= sp.re(sp.expand(dg)) == 0 and sp.simplify(dg) != 0
# real at all times: i hbar psi_t (imaginary) = H psi (real) => both zero. Use real symbols for r_t, r_xx, r.
rt, rxx, r0, Vr = sp.symbols('r_t r_xx r Vr', real=True)
L = sp.I*hb*rt; R = -(hb**2/(2*m))*rxx + Vr*r0
sol = sp.solve([sp.re(L - R), sp.im(L - R)], [rt, rxx], dict=True)
print("real psi at all times forces:", sol)
ok &= sol == [{rt: 0, rxx: 2*m*Vr*r0/hb**2}]   # psi_t = 0 and H psi = 0
print("PASS" if ok else "FAIL")
