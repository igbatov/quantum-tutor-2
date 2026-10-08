# Claim: "All pass a vertical filter, none pass a horizontal one, and half pass at 45°"
import numpy as np
def pol(deg):
    t=np.radians(deg); return np.array([np.sin(t), np.cos(t)])  # angle from vertical; (x, y)
V=pol(0)
res={a: abs(pol(a)@V)**2 for a in (0,90,45)}
print(res)
ok = abs(res[0]-1)<1e-12 and abs(res[90])<1e-12 and abs(res[45]-0.5)<1e-12
# "Whenever a photon's arrow and a filter are 45° apart, half pass"
ok2 = all(abs(abs(pol(a)@pol(a+45))**2-0.5)<1e-12 for a in np.linspace(0,180,37))
print("general 45-deg separation gives 1/2:", ok2)
print("PASS" if ok and ok2 else "FAIL")
