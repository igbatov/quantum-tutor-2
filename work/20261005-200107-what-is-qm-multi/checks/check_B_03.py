# Claim: "middle of a dark stripe. With only the left slit open, electrons do land there"
# and "Open both ... the spot gets none"
import numpy as np
u_dark = np.array([0.1, 0.3, 0.5, 0.7, 0.9])   # cos(5 pi u) = 0
P1 = np.sinc(u_dark)**2                          # one slit (either), same envelope
P2 = 4*np.sinc(u_dark)**2*np.cos(5*np.pi*u_dark)**2
print("one-slit P at dark spots:", P1)
print("two-slit P at dark spots:", P2)
ok = np.all(P1 > 1e-3) and np.all(np.abs(P2) < 1e-12)
print("PASS" if ok else "FAIL")
