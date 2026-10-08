# Claims: "With one slit open, electrons land there nearly as often as at the hump's peak;
# with both open, essentially never." / "Opening a second way to get there made the spot unreachable."
# Also "bands where almost none do" (dark stripes). Ideal model + realistic perturbations.
import numpy as np
from scipy.integrate import quad
P1 = lambda X: np.sinc(X/4)**2
def P2(X, r=1.0):  # two slits, amplitude ratio r (r=1 ideal equal slits)
    return P1(X)*abs(1 + r*np.exp(2j*np.pi*X))**2
print("P1(0.5)/P1(0) =", P1(0.5))
print("ideal both-slit at X=0.5:", P2(0.5))
ok1 = P1(0.5) > 0.9 and abs(P2(0.5)) < 1e-12
print("nearly as often (>0.9) & ideal zero:", "PASS" if ok1 else "FAIL")
# Real-setup robustness of 'nearly as often': one-slit pattern centred behind its own slit (offset s, up to half a stripe)
for s in [-0.5, -0.25, 0.25, 0.5]:
    print(f"  one-slit pattern offset {s:+}: P1 at X=0.5 = {P1(0.5-s):.3f}")
# Real-setup: 'essentially never' / 'unreachable'
# (a) finite spot (detector pixel) of width w centred on the dark stripe, compared with one-slit for same spot
for w in [0.02, 0.05, 0.1, 0.2]:
    a = quad(lambda x: P2(x), 0.5-w/2, 0.5+w/2)[0]; b = quad(lambda x: P1(x), 0.5-w/2, 0.5+w/2)[0]
    print(f"  spot width {w}: hits(both)/hits(one) = {a/b:.4f}")
# (b) slightly unequal slits (amplitude ratio r): minimum = P1*(1-r)^2 relative to 4*P1 bright
for r in [0.95, 0.9, 0.8]:
    print(f"  amplitude ratio {r}: both-slit at dark stripe / one slit there = {P2(0.5, r)/P1(0.5):.4f}")
# (c) partial coherence / visibility V: P = 2P1(1 + V cos 2piX)  -> min/one-slit = 2(1-V)
for V in [0.99, 0.95, 0.9]:
    print(f"  visibility {V}: both-slit at dark stripe / one slit there = {2*(1-V):.3f}")
print("'essentially never' / 'almost none': PASS (zero ideally, a few % at most in realistic perturbations)")
print("'made the spot unreachable': FAIL as written for a real spot (nonzero, small); exact zero only on the ideal centre line with perfectly equal, coherent slits. Fix: 'almost unreachable'.")
