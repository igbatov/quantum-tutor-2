# Claims: "Routes that can be told apart add their chances, not their amplitudes";
# "records far too gentle ... erase the stripes too. What matters is that a record exists"
# Model: psi = (psi1|d1> + psi2|d2>)/sqrt2 ; d's are marker states that do not touch the spatial amplitude.
import numpy as np
u = np.linspace(-1, 1, 4001)
env = np.sinc(u)
psi1 = env*np.exp(+1j*4*np.pi*u)   # route 1 (no momentum kick applied to either route)
psi2 = env*np.exp(-1j*4*np.pi*u)
def screen(overlap):
    # P(u) = |psi1|^2 + |psi2|^2 + 2 Re(overlap * conj(psi1) psi2)
    return np.abs(psi1)**2 + np.abs(psi2)**2 + 2*np.real(overlap*np.conj(psi1)*psi2)
P_none = screen(1.0)    # no record (identical marker states)
P_rec = screen(0.0)     # orthogonal marker states (perfect record)
sumchances = np.abs(psi1)**2 + np.abs(psi2)**2
vis = lambda P: (P.max()-P[np.argmin(np.abs(u-0.125))])/(P.max()+P[np.argmin(np.abs(u-0.125))])
print("max |P_rec - sum of chances| =", np.max(np.abs(P_rec - sumchances)))
print("P_none at u=0.125:", P_none[np.argmin(np.abs(u-0.125))], " P_rec there:", P_rec[np.argmin(np.abs(u-0.125))])
for g in [1.0, 0.5, 0.0]:
    print(f"marker overlap {g}: fringe visibility near centre = {vis(screen(g)):.3f}")
ok = np.max(np.abs(P_rec - sumchances)) < 1e-12 and P_none[np.argmin(np.abs(u-0.125))] < 1e-12
print("PASS" if ok else "FAIL")
