# Claim: "roughly a thousand electrons per second ... tens-of-kilovolt energies ... successive electrons were
# on average well over a hundred kilometres apart"; "a sizeable fraction of light speed"
import numpy as np
from scipy.constants import m_e,c,e
for kV in [10,30,50,100]:
    g=1+e*kV*1e3/(m_e*c**2); v=c*np.sqrt(1-1/g**2); print(kV,"kV: v/c=%.3f spacing at 1000/s = %.0f km"%(v/c,v/1000/1e3))
g=1+e*50e3/(m_e*c**2); v=c*np.sqrt(1-1/g**2); d=v/1000/1e3
print("Tonomura used 50 kV: spacing %.0f km"%d)
print("PASS" if d>100 else "FAIL")
