# Claim: "Over the whole screen, two slits give twice the hits of one"
# Compared to: ONE slit open (the text's unit). Cross term integrates to zero; ratio = 2.
import sympy as sp, numpy as np
from scipy.integrate import quad
u = sp.symbols('u', real=True)
# Two-slit far field: |sinc(u)(e^{i5pi u}+e^{-i5pi u})|^2 = 4 sinc^2 cos^2(5 pi u)
sinc2 = (sp.sin(sp.pi*u)/(sp.pi*u))**2
I1 = sp.integrate(sinc2, (u, -sp.oo, sp.oo))
cross = sp.integrate(sinc2*sp.cos(10*sp.pi*u), (u, -sp.oo, sp.oo))  # FT of sinc^2 is triangle, zero at f=5
I2 = 2*I1 + 2*cross
print("integral one slit:", sp.nsimplify(I1), " cross term:", sp.simplify(cross), " two slits:", sp.simplify(I2))
# numeric cross-check over a wide finite screen
f1 = lambda x: np.sinc(x)**2
f2 = lambda x: 4*np.sinc(x)**2*np.cos(5*np.pi*x)**2
L = 200
n1 = quad(f1, -L, L, limit=5000)[0]; n2 = quad(f2, -L, L, limit=5000)[0]
print(f"numeric on [-{L},{L}]: one={n1:.6f} two={n2:.6f} ratio={n2/n1:.6f}")
ok = sp.simplify(I2/I1 - 2) == 0 and abs(n2/n1 - 2) < 1e-3
# Redistribution: total equals incoherent sum (which-slit) total
print("two-slit total equals sum of two one-slit totals:", sp.simplify(I2 - 2*I1) == 0)
print("PASS" if ok else "FAIL")
