# Claim: "shadow on the vertical is about 0.866, which squared is 0.75"
# Claim: "shadow on the horizontal is 0.5 ... 0.25"; "These always add to 100%" (Pythagoras)
import sympy as sp
th = sp.symbols('theta', real=True)
sv, sh = sp.cos(sp.pi/6), sp.sin(sp.pi/6)
ok = abs(float(sv) - 0.866) < 5e-4 and sp.simplify(sv**2 - sp.Rational(3,4)) == 0 \
     and sh == sp.Rational(1,2) and sp.simplify(sh**2 - sp.Rational(1,4)) == 0
always = sp.simplify(sp.cos(th)**2 + sp.sin(th)**2 - 1) == 0
print("cos30 =", float(sv), " cos^2 =", sv**2, " sin30 =", sh, " sin^2 =", sh**2)
print("cos^2+sin^2 == 1 for all theta:", always)
print("PASS" if ok and always else "FAIL")
