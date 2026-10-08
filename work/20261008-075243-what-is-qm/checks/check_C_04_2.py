# Claims: fitting patterns "can, at any one moment, be taken as simply positive or negative";
# "the clock hands of a fitting pattern do all turn together, at a rate set by its energy".
import sympy as sp
from sympy.physics.hydrogen import R_nl, E_nl
r, th, ph, t = sp.symbols('r theta phi t', positive=True)
hb = m = 1  # atomic units, Z = 1
def H(f):
    lap = sp.diff(r**2*sp.diff(f, r), r)/r**2 + sp.diff(sp.sin(th)*sp.diff(f, th), th)/(r**2*sp.sin(th)) + sp.diff(f, ph, 2)/(r**2*sp.sin(th)**2)
    return -lap/2 - f/r
ok = True
# real basis: 1s, 2p_z, 2p_x (= real combination of m=+-1), 3d_xy-type
cases = {
 '1s':  (R_nl(1, 0, r, 1), 1),
 '2p_z': (R_nl(2, 1, r, 1)*sp.cos(th), 2),
 '2p_x': (R_nl(2, 1, r, 1)*sp.sin(th)*sp.cos(ph), 2),
 '3d_xy': (R_nl(3, 2, r, 1)*sp.sin(th)**2*sp.sin(2*ph), 3),
}
for name, (psi, n) in cases.items():
    E = E_nl(n, 1)
    res = sp.simplify(H(psi) - E*psi)
    Psi = psi*sp.exp(-sp.I*E*t)
    tdse = sp.simplify(sp.I*sp.diff(Psi, t) - H(Psi))
    real = sp.simplify(sp.im(psi.subs({r: sp.Rational(3, 2), th: sp.Rational(1, 3), ph: sp.Rational(2, 7)}))) == 0
    print(f"{name}: H psi - E psi = {res}; TDSE residual = {tdse}; real-valued: {real}; E = {E}")
    ok &= res == 0 and tdse == 0 and real
# all points share the single phase factor exp(-iEt): ratio of Psi at two points is time-independent
psi = cases['2p_x'][0]; E = E_nl(2, 1); Psi = psi*sp.exp(-sp.I*E*t)
ratio = sp.simplify(Psi.subs({r: 1, th: 1, ph: 0})/Psi.subs({r: 2, th: 2, ph: 1}))
print("ratio of amplitudes at two points (2p_x):", ratio, "time-dependent:", ratio.has(t)); ok &= not ratio.has(t)
# note: the m=+1 eigenstate R21 sin(th) e^{i phi} is NOT real at one moment; real choice needs combining m=+-1
print("PASS" if ok else "FAIL")
