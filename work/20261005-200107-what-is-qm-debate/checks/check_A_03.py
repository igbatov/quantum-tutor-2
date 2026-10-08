# Claim: "a second slit could only add hits" if chances add; "at ... dark bands, opening the second slit drops hits almost to zero"
# Figure model: one slit S(x)=sinc^2(x/5); two slits 4 S cos^2(pi x). Dark band at x=0.5.
import numpy as np
S = lambda x: np.sinc(x/5)**2
x = np.linspace(-6, 6, 12001)
added = 2*S(x); interf = 4*S(x)*np.cos(np.pi*x)**2
print("adding chances never decreases: min(2S - S) =", (added - S(x)).min())
xd = 0.5
print("at x=0.5: one slit =", S(xd), " two slits (interference) =", 4*S(xd)*np.cos(np.pi*xd)**2)
# 'at every bright band solid is twice dotted'
xb = np.arange(-5, 6)  # integer x = bright band centres (avoid x=+-5 envelope zero)
xb = xb[np.abs(xb) != 5]
ratio = (4*S(xb)*np.cos(np.pi*xb)**2)/(2*S(xb))
print("bright band ratio solid/dotted:", ratio)
ok = (added - S(x)).min() >= -1e-12 and 4*S(xd)*np.cos(np.pi*xd)**2 < 1e-12 and abs(S(xd)-1) < 0.05 and np.allclose(ratio, 2)
print("PASS" if ok else "FAIL")
