# Claim: "renaming each amplitude as its own square root ... look like a fourth-power rule;
# but renamed amplitudes no longer add"
# Also figure caption arithmetic "0.87² + 0.50² = 0.75 + 0.25 = 1.00"
import sympy as sp
a1, a2 = sp.symbols('a1 a2', positive=True)
b = sp.sqrt(a1)
print("square rule in renamed variable b = sqrt(a): a^2 =", sp.simplify((b**2)**2), "= b^4")
# addition: amplitudes a1 + a2 add; renamed: sqrt(a1+a2) vs sqrt(a1)+sqrt(a2)
diff = (sp.sqrt(a1 + a2) - (sp.sqrt(a1) + sp.sqrt(a2))).subs({a1: sp.Rational(1, 2), a2: sp.Rational(1, 2)})
print("renamed sum mismatch at a1=a2=1/2:", sp.nsimplify(diff), "=", float(diff))
ok = sp.simplify((b**2)**2 - a1**2) == 0 and abs(float(diff)) > 0.1
print("0.87^2 + 0.50^2 with the rounded numbers =", 0.87**2 + 0.50**2, "; exact cos30^2 =", float(sp.cos(sp.pi/6)**2))
print("PASS" if ok else "FAIL")
