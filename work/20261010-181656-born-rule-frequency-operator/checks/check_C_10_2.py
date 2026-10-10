# Claim: "at the 50 kV used the electrons move at about 0.41 of the speed of light, so successive
# electrons were on average roughly 120 km apart" (roughly a thousand electrons per second)
import numpy as np
from scipy.constants import m_e,c,e
g=1+e*50e3/(m_e*c**2); v=c*np.sqrt(1-1/g**2); d=v/1000/1e3
print("50 kV: v/c=%.4f, spacing at 1000 e/s = %.1f km"%(v/c,d))
# apparatus length ~ 1.5 m: transit time vs mean gap
print("transit time over 1.5 m: %.2e s; mean gap 1e-3 s; P(another electron within transit) ~ %.1e"%(1.5/v,1-np.exp(-1000*1.5/v)))
ok=abs(v/c-0.41)<0.005 and abs(d-120)<=6
print("PASS" if ok else "FAIL")
