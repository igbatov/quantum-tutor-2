# Claims (spin worked): amplitude for +x "= cos(omega t/2)", chance "cos^2(wt/2) = 1/2(1+cos wt)";
#  -x amplitude "(c+ - c-)/sqrt2 = -i sin(wt/2)"; "the two add to 1"; "|c+|^2 = 1/2, constant".
#  Check yourself: chance of +y "1/2(1 + sin wt)"; first time along +y.
import sympy as sp
w, t = sp.symbols('omega t', positive=True)
ok = True
cp = sp.exp(-sp.I*w*t/2)/sp.sqrt(2); cm = sp.exp(sp.I*w*t/2)/sp.sqrt(2)
def z(e): return sp.simplify(sp.expand_complex(sp.expand(e))) == 0
ok &= z(cp*sp.conjugate(cp) - sp.Rational(1, 2))
ax = (cp + cm)/sp.sqrt(2); amx = (cp - cm)/sp.sqrt(2)
ok &= z(ax - sp.cos(w*t/2)); ok &= z(amx + sp.I*sp.sin(w*t/2))
ok &= z(sp.cos(w*t/2)**2 - (1 + sp.cos(w*t))/2)
ok &= z(ax*sp.conjugate(ax) + amx*sp.conjugate(amx) - 1)
ay = sp.conjugate(1/sp.sqrt(2))*cp + sp.conjugate(sp.I/sp.sqrt(2))*cm
py = sp.simplify(sp.expand_complex(ay*sp.conjugate(ay)))
print("P(+y) =", py); ok &= z(py - (1 + sp.sin(w*t))/2)
t1 = sp.solve(sp.Eq(sp.sin(w*t), 1), t)
print("first time P(+y)=1: t =", t1, " (= T/4 with T = 2 pi/omega, for omega > 0)")
print("PASS" if ok else "FAIL")
