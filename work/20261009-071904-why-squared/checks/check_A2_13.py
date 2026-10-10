# Claim (2): "The same curve, with the angle between two polarizers ..., is seen in the joint counts
# of entangled photon pairs" (state (HH + VV)/sqrt2, polarizers at a and b).
import sympy as sp
a, b = sp.symbols('a b', real=True)
H, V = sp.Matrix([1, 0]), sp.Matrix([0, 1])
psi = (sp.kronecker_product(H, H) + sp.kronecker_product(V, V))/sp.sqrt(2)
pol = lambda x: sp.Matrix([sp.cos(x), sp.sin(x)])
amp = (sp.kronecker_product(pol(a), pol(b)).T*psi)[0]
Ppp = sp.simplify(amp**2); PA = sp.Rational(1, 2)
cond = sp.simplify(Ppp/PA)
print("P(both pass) =", Ppp, "; P(pass | partner passed) =", cond)
ok = sp.simplify(cond - sp.cos(a - b)**2) == 0
print("joint counts follow cos²(a-b) (scaled by 1/2):", ok)
print("PASS" if ok else "FAIL")
