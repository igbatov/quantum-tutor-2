# Claims (Model 2): "for a free electron the position-dependent part is momentum times distance
#  travelled, so the hand turns once per de Broglie wavelength"; "hands near the classical path
#  line up, the rest cancel".
import sympy as sp
import numpy as np
from scipy.special import fresnel
m, d, T = sp.symbols('m d T', positive=True)
ok = True
v = d/T; p = m*v; E = p**2/(2*m)
S = sp.Rational(1, 2)*m*v**2*T          # action of the classical free path
print("S =", sp.simplify(S), "; p d - E T =", sp.simplify(p*d - E*T))
ok &= sp.simplify(S - (p*d - E*T)) == 0
hb = sp.symbols('hbar', positive=True)
lam = 2*sp.pi*hb/p
print("phase p*lambda/hbar =", sp.simplify(p*lam/hb)); ok &= sp.simplify(p*lam/hb - 2*sp.pi) == 0
# stationary phase: routes deflected through y have extra phase pi*y^2 (units of Fresnel zone);
# sum of e^{i pi y^2/2} over |y|<Y converges to the full sum mostly from |y| < ~1.5
full = (1 + 1j)  # integral_{-inf}^{inf} e^{i pi y^2/2} dy = 1+i
for Y in [0.5, 1.0, 1.5, 3, 10]:
    Sf, Cf = fresnel(Y)
    part = 2*(Cf + 1j*Sf)
    print(f"|y|<{Y}: |partial sum| / |full| = {abs(part)/abs(full):.3f}")
# contribution per unit width of y: |int_y^{y+1} e^{i pi y^2/2} dy| near the classical path vs far away
def chunk(y0):
    S1, C1 = fresnel(y0); S2, C2 = fresnel(y0 + 1)
    return abs((C2 - C1) + 1j*(S2 - S1))
for y0 in [0, 2, 5, 10, 20]:
    print(f"routes with {y0}<y<{y0+1}: |sum of hands| = {chunk(y0):.4f}")
ok &= chunk(5)/chunk(0) < 0.1 and chunk(20) < chunk(10) < chunk(5)
print("PASS" if ok else "FAIL")
