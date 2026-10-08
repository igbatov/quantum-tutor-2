# Claim: "As it fell, the frequency of its light would rise smoothly."
# Classical Coulomb circular orbit: omega^2 = k e^2/(m r^3) -> omega ∝ r^(-3/2), monotonic as r decreases
import sympy as sp
r,k,e,m = sp.symbols('r k e m', positive=True)
omega = sp.sqrt(k*e**2/(m*r**3))
d = sp.simplify(sp.diff(omega, r))
print("d omega/dr =", d)
print("PASS" if sp.ask(sp.Q.negative(d), sp.Q.positive(r)&sp.Q.positive(k)&sp.Q.positive(e)&sp.Q.positive(m)) else "FAIL")
