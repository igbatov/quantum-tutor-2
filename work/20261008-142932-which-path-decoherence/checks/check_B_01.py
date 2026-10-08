# Claims: isotropic overlap V = |sin(2*pi*d/lam)/(2*pi*d/lam)|; "first zero at d = lambda/2";
# "weak revival near d ~ 0.72 lambda (height about 0.22)"; "V stays above 0 for d < lambda/2";
# "lambda/d = 20 (overlap about 0.98)"; Check-yourself photon of 20 um at 1 um separation.
import sympy as sp, numpy as np
from scipy.optimize import brentq, minimize_scalar
k, d, th, ph = sp.symbols('k d theta phi', positive=True)
# photon emitted isotropically; outgoing waves from the two paths differ by phase exp(i k n.d)
integrand = sp.exp(sp.I*k*d*sp.cos(th))*sp.sin(th)/(4*sp.pi)
ov = sp.simplify(sp.integrate(sp.integrate(integrand, (th, 0, sp.pi)), (ph, 0, 2*sp.pi)))
ov = sp.simplify(sp.expand_complex(ov.rewrite(sp.sin)))
ok1 = sp.simplify(ov - sp.sin(k*d)/(k*d)) == 0
print("overlap =", ov, "| equals sin(kd)/(kd):", ok1)
f = lambda r: np.sinc(2*r)  # np.sinc(x)=sin(pi x)/(pi x); x = 2 d/lam
z = brentq(f, 0.4, 0.6)
res = minimize_scalar(lambda r: -abs(f(r)), bounds=(0.5, 1.0), method='bounded')
r = np.linspace(1e-6, 0.5-1e-6, 10001)
pos = np.all(np.abs(f(r)) > 0)
v20 = f(1/20)
print(f"first zero d/lam = {z:.4f}; revival at d/lam = {res.x:.4f}, height {abs(f(res.x)):.4f}")
print(f"V>0 on (0, lam/2): {pos}; overlap at lam/d=20: {v20:.4f}; at lam/d=10: {f(0.1):.4f}")
print(f"max |overlap| for lam/d<2 (d/lam>0.5): {abs(f(res.x)):.3f}")
ok = ok1 and abs(z-0.5)<1e-6 and abs(res.x-0.72)<0.01 and abs(abs(f(res.x))-0.22)<0.01 and pos and abs(v20-0.98)<0.01
print("PASS" if ok else "FAIL")
