# Check-yourself: vertical light -> 45 -> horizontal -> 45; expected answer 1/8 of light leaving vertical filter
import numpy as np
def v(d): t=np.radians(d); return np.array([np.sin(t),np.cos(t)])
p=1.0; cur=v(0)
for a in (45,90,45):
    p*=abs(v(a)@cur)**2; cur=v(a)
print("fraction =",p)
print("PASS (answer 1/8 is well-defined)" if abs(p-1/8)<1e-12 else "FAIL")
