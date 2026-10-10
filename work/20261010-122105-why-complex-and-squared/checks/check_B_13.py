# Claims: f(x) = x^2 + eps x^2(1-x^2)(2x^2-1): "f(cos)+f(sin) = 1"; "f(0)=0, f(1)=1";
#  "non-negative for |eps| < 1"; "(1-x^2)(2x^2-1) lies between -1 and 1/8";
#  three levels (1,1,1)/sqrt3: "f = 1/3 - 2 eps/27", "total 1 - 2 eps/9".
import sympy as sp
import numpy as np
x, e, th = sp.symbols('x epsilon theta', real=True)
f = lambda y: y**2 + e*y**2*(1 - y**2)*(2*y**2 - 1)
ok = True
ok &= sp.simplify(sp.expand_trig(f(sp.cos(th)) + f(sp.sin(th)) - 1)) == 0
ok &= f(0) == 0 and sp.simplify(f(1) - 1) == 0
g = (1 - x**2)*(2*x**2 - 1)
X = np.linspace(0, 1, 200001); gv = (1 - X**2)*(2*X**2 - 1)
print("range of g on [0,1]:", gv.min(), gv.max()); ok &= abs(gv.min()+1) < 1e-12 and abs(gv.max()-1/8) < 1e-9
for E in np.linspace(-0.999, 0.999, 81):
    ok &= (X**2 + E*X**2*gv >= -1e-15).all()
f3 = sp.simplify(f(1/sp.sqrt(3)))
print("f(1/sqrt3) =", f3, "; total =", sp.simplify(3*f3)); ok &= sp.simplify(f3 - (sp.Rational(1, 3) - 2*e/27)) == 0
ok &= sp.simplify(3*f3 - (1 - 2*e/9)) == 0
print("PASS" if ok else "FAIL")
