# Checks numbers printed in figure annotations: "faint stripes in the gap (at most 12% of peak)"
# (close, |x| <= 1a) and far "side bands beyond +-4 stripe spacings (under 5% of peak)".
import numpy as np
from scipy.special import fresnel
a, d = 1.0, 4.0
def u(x, c, lL):
    s = np.sqrt(2/lL); S1, C1 = fresnel(s*(c-a/2-x)); S2, C2 = fresnel(s*(c+a/2-x))
    return ((C2-C1) + 1j*(S2-S1))/np.sqrt(2j)
lL = 16/20; x = np.linspace(-5, 5, 400001); Ib = abs(u(x,-2,lL)+u(x,2,lL))**2; Ib /= Ib.max()
g = Ib[abs(x) <= 1].max(); print(f"close gap |x|<=1a max = {g:.4f}", "PASS" if g <= 0.125 else "FAIL")
lL = 16/0.05; x = np.linspace(-640, 640, 400001); Ib = abs(u(x,-2,lL)+u(x,2,lL))**2; Ib /= Ib.max()
s = Ib[abs(x) > 4*lL/d].max(); print(f"far side bands |X|>4 max = {s:.4f}", "PASS" if s < 0.05 else "FAIL")
