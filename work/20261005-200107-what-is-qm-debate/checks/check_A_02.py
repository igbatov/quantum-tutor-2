# Claim: "Averaged across the bands, the chance comes back to 2 units: interference only moves probability around."
# Model: two unit arrows with relative phase phi; phase advances uniformly along the screen.
import sympy as sp
phi = sp.symbols('phi', real=True)
P = sp.simplify(sp.Abs(1 + sp.exp(sp.I*phi))**2)
avg = sp.simplify(sp.integrate(sp.expand_complex(P), (phi, 0, 2*sp.pi)) / (2*sp.pi))
print("P(phi) =", sp.simplify(sp.expand_complex(P)), " average over a band period =", avg)
# Also with the figure envelope: integral of 4 S cos^2(pi x) vs 2 S over -6..6
import numpy as np
from scipy.integrate import quad
S = lambda x: np.sinc(x/5)**2      # numpy sinc = sin(pi u)/(pi u)
I2 = quad(lambda x: 4*S(x)*np.cos(np.pi*x)**2, -6, 6, limit=400)[0]
Iadd = quad(lambda x: 2*S(x), -6, 6, limit=400)[0]
print("area solid =", I2, " area dotted =", Iadd, " rel diff =", abs(I2-Iadd)/Iadd)
ok = avg == 2 and abs(I2-Iadd)/Iadd < 0.02
print("PASS" if ok else "FAIL")
