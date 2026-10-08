# Claims: "add the amplitudes ... chance ... size of the total, squared";
# equal routes -> bright; "half a wavelength longer ... cancel"; "whole wavelength longer: bright again"
import sympy as sp
a, dL, lam = sp.symbols('a DeltaL lambda', positive=True)
A1 = a
A2 = a*sp.exp(2*sp.pi*sp.I*dL/lam)
P = sp.simplify(sp.expand(sp.Abs(A1 + A2)**2).rewrite(sp.cos))
P = sp.simplify(sp.expand_complex((A1+A2)*sp.conjugate(A1+A2)))
vals = {name: sp.simplify(P.subs(dL, d)) for name, d in
        [("0", 0), ("lam/2", lam/2), ("lam", lam)]}
print("P(DeltaL) =", P); print(vals)
incoh = 2*a**2
ok = vals["0"] == 4*a**2 and vals["lam/2"] == 0 and vals["lam"] == 4*a**2
# also consistency with figure model: phase difference 8 pi u => u=1/8 is half-wave
print("figure phase at u=1/8 (units of pi):", sp.Rational(8,8))
print("PASS" if ok else "FAIL")
