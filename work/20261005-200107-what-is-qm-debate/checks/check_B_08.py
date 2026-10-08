# Claim: "At a dark stripe, opening the second slit *lowers* the number of hits"
#        "adds the amplitudes ... then turns the total into a chance by squaring its size"
import numpy as np
lam = 1.0; d = 5.0; D = 1000.0
y = np.linspace(-300, 300, 20001)
r1 = np.sqrt(D**2 + (y-d/2)**2); r2 = np.sqrt(D**2 + (y+d/2)**2)
a1 = np.exp(2j*np.pi*r1/lam)/np.sqrt(2); a2 = np.exp(2j*np.pi*r2/lam)/np.sqrt(2)
one = abs(a1)**2
both = abs(a1+a2)**2
idx = np.argmin(both[np.abs(y) < 150] if False else both)
print(f"at dark stripe y={y[idx]:.2f}: one slit P={one[idx]:.3f}, both slits P={both[idx]:.2e}")
print(f"sum-of-chances would give {abs(a1[idx])**2+abs(a2[idx])**2:.3f}")
ok = both[idx] < one[idx]*1e-3
print("PASS" if ok else "FAIL")
