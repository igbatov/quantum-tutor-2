# Claims (Model 3): "d|c1|^2/dt = (2/hbar) Im(H12 conj(c1) c2)"; "d|c2|^2/dt = -(2/hbar) Im(...)";
#  "d/dt(|c1|^2+|c2|^2) = 0"; "-i Gamma would make |c1|^2 decay as e^{-2 Gamma t/hbar}";
#  ammonia solution "c1 = cos(At/hbar), c2 = i sin(At/hbar)"; "A real c2 = sin(At/hbar) fails";
#  table of cos^p+sin^p; "2(1/sqrt2)^p = 2^{1-p/2}"; "any power below 2 overshoots, any power
#  above 2 undershoots, worst at pi/4".
import sympy as sp
import numpy as np
hb, A, t, G, E = sp.symbols('hbar A t Gamma E', positive=True)
H11, H22 = sp.symbols('H11 H22', real=True)
x1, y1, x2, y2, hr, hi = sp.symbols('x1 y1 x2 y2 hr hi', real=True)
c1 = x1 + sp.I*y1; c2 = x2 + sp.I*y2; H12 = hr + sp.I*hi; H21 = sp.conjugate(H12)
d1 = (H11*c1 + H12*c2)/(sp.I*hb); d2 = (H21*c1 + H22*c2)/(sp.I*hb)
r1 = sp.expand(sp.conjugate(c1)*d1 + c1*sp.conjugate(d1))
r2 = sp.expand(sp.conjugate(c2)*d2 + c2*sp.conjugate(d2))
z = sp.expand(H12*sp.conjugate(c1)*c2)
ok = True
ok &= sp.simplify(r1 - 2/hb*sp.im(z)) == 0
ok &= sp.simplify(r2 + 2/hb*sp.im(z)) == 0
ok &= sp.simplify(r1 + r2) == 0
print("rates and conservation:", ok)
cd = sp.exp(-sp.I*(E - sp.I*G)*t/hb)
dec = sp.simplify(sp.expand_complex(cd*sp.conjugate(cd)))
print("|c1|^2 with -i Gamma:", dec); ok &= sp.simplify(dec - sp.exp(-2*G*t/hb)) == 0
a1 = sp.cos(A*t/hb); a2 = sp.I*sp.sin(A*t/hb)
ok &= sp.simplify(sp.I*hb*sp.diff(a1, t) - (-A*a2)) == 0
ok &= sp.simplify(sp.I*hb*sp.diff(a2, t) - (-A*a1)) == 0
b2 = sp.sin(A*t/hb)
fails = sp.simplify(sp.I*hb*sp.diff(a1, t) - (-A*b2)) != 0
print("ammonia solution ok:", ok, "; real c2 fails:", fails); ok &= fails
th = np.array([0, np.pi/8, np.pi/4, 3*np.pi/8, np.pi/2])
table = {1: [1, 1.307, 1.414, 1.307, 1], 2: [1]*5, 3: [1, .845, .707, .845, 1], 4: [1, .75, .5, .75, 1]}
for p, row in table.items():
    val = np.cos(th)**p + np.sin(th)**p
    print(p, np.round(val, 3)); ok &= np.allclose(val, row, atol=6e-4)
p = sp.symbols('p', positive=True)
ok &= sp.simplify(2*(1/sp.sqrt(2))**p - 2**(1 - p/2)) == 0
TH = np.linspace(1e-6, np.pi/2 - 1e-6, 20001)
for P in np.r_[np.linspace(0.1, 1.99, 40), np.linspace(2.01, 12, 40)]:
    f = np.cos(TH)**P + np.sin(TH)**P
    over = (f > 1).all() if P < 2 else (f < 1).all()
    worst = abs(TH[np.argmax(np.abs(f - 1))] - np.pi/4) < 1e-3
    if not (over and worst):
        ok = False; print("violates at p =", P)
print("over/undershoot & worst at pi/4 for p in (0,2) and (2,12]:", ok)
print("PASS" if ok else "FAIL")
