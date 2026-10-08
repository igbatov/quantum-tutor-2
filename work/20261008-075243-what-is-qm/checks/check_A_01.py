# Claim: "alike, the total is 2 and the chance 4; opposite ... total is 0"
# and "Adding chances instead would give 2 either way."
import sympy as sp
a1, a2 = sp.Integer(1), sp.Integer(1)
alike = (a1 + a2)**2; opp = (a1 - a2)**2; chances = a1**2 + a2**2
# complex "clock hand" version: |e^{i0}+e^{i phi}|^2 = 2+2cos(phi)
phi = sp.symbols('phi', real=True)
gen = sp.simplify(sp.expand(sp.Abs(1 + sp.exp(sp.I*phi))**2).rewrite(sp.cos))
ok = alike == 4 and opp == 0 and chances == 2 and sp.simplify(gen - (2+2*sp.cos(phi))) == 0
print("alike", alike, "opposite", opp, "chances added", chances, "general |1+e^{i phi}|^2 =", gen)
print("PASS" if ok else "FAIL")
