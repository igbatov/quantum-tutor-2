# Claims (final-B): "V = |sin(2πd/λ)/(2πd/λ)|"; "first zero at d = λ/2"; "revival near 0.72λ reaches about 0.22";
# "between λ/2 and λ the overlap is negative"; "at least about three-quarters" removed for λ/d < 2;
# "λ/d = 20 (overlap about 0.98)"; light band λ/d > 10 "records almost nothing"; Check-yourself 20 µm photon.
import numpy as np, sympy as sp
from scipy.optimize import brentq, minimize_scalar
k, d, th = sp.symbols('k d theta', positive=True)
avg = sp.simplify(sp.integrate(sp.exp(sp.I*k*d*sp.cos(th))*sp.sin(th), (th, 0, sp.pi))/2)
iso_ok = sp.simplify(avg.rewrite(sp.sin) - sp.sin(k*d)/(k*d)) == 0
s = lambda r: np.sinc(2*r)              # r = d/λ ; np.sinc(x)=sin(pi x)/(pi x)
z = brentq(s, 0.4, 0.6)
m = minimize_scalar(s, bounds=(0.5, 1.0), method='bounded')
r = np.linspace(1e-6, 0.5-1e-6, 100001); pos_below = np.all(s(r) > 0)
rn = np.linspace(0.5+1e-6, 1-1e-6, 100001); neg_between = np.all(s(rn) < 0)
rr = np.linspace(0.5, 50, 2000001); maxabs = np.abs(s(rr)).max()   # λ/d < 2  <=>  d/λ > 0.5
o20, o10 = s(1/20), s(1/10)
print(f"isotropic average = sin(kd)/(kd): {iso_ok}")
print(f"first zero d/λ = {z:.5f}; V>0 on (0, λ/2): {pos_below}; overlap<0 on (λ/2, λ): {neg_between}")
print(f"revival max at d/λ = {m.x:.4f}, |V| = {abs(m.fun):.4f}")
print(f"max |overlap| for λ/d<2: {maxabs:.4f} -> removes at least {1-maxabs:.3f}")
print(f"overlap λ/d=20: {o20:.4f} (fade {1-o20:.3%}); λ/d=10: {o10:.4f} (fade {1-o10:.3%})")
ok = iso_ok and abs(z-0.5)<1e-6 and pos_below and neg_between and abs(m.x-0.72)<0.01 and abs(abs(m.fun)-0.22)<0.01 \
     and 1-maxabs >= 0.75 and abs(o20-0.98)<0.01 and o10 > 0.93
print("PASS" if ok else "FAIL")
