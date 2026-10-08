# Claims: pulses on -> "the broad band of the two one-path chances added (exactly that, in the ideal
# case)"; figure a-atom-tag: "The two curves enclose the same area".
import numpy as np
from scipy.integrate import quad
sig = 2.0; E = lambda X: np.exp(-X**2/(2*sig**2))
X = np.linspace(-30, 30, 60001)
p1 = np.sqrt(E(X)/2)*np.exp(1j*np.pi*X); p2 = np.sqrt(E(X)/2)*np.exp(-1j*np.pi*X)
off = np.abs(p1+p2)**2; on = np.abs(p1)**2+np.abs(p2)**2   # orthogonal tags
a_off = np.trapezoid(off, X); a_on = np.trapezoid(on, X)
print(f"area ratio off/on = {a_off/a_on:.10f}; max|on - E| = {np.max(np.abs(on-E(X))):.1e}")
print(f"contrast with tag: {(on.max()-on.min())/(on.max()+on.min()):.3f} (envelope only, no 2-path stripes)")
ok = abs(a_off/a_on-1) < 1e-8 and np.max(np.abs(on-E(X))) < 1e-12
print("PASS" if ok else "FAIL")
