# Claim: "shadow on the vertical is about 0.866 ... 0.75"; "horizontal is 0.5 ... 0.25";
# "At every angle the two chances add up to 100%"
import sympy as sp
th = sp.symbols('theta', real=True)
cv, sh = sp.cos(sp.pi/6), sp.sin(sp.pi/6)
print("cos30 =", float(cv), " cos^2 =", sp.nsimplify(cv**2), " sin30 =", sh, " sin^2 =", sh**2)
ok = abs(float(cv)-0.866) < 5e-4 and cv**2 == sp.Rational(3,4) and sh == sp.Rational(1,2) and sh**2 == sp.Rational(1,4)
s = sp.simplify(sp.cos(th)**2 + sp.sin(th)**2 - 1); print("cos^2+sin^2-1 simplifies to", s)
ok &= (s == 0)
print("PASS" if ok else "FAIL")
