# Claims (Exp. 1 + figure a-atom-tag): pulses on -> "no stripes, just the smooth pattern,
# the two one-path chances added"; "total number of atoms does not change"; curves of equal area.
import numpy as np
from scipy.integrate import quad
sig = 2.0
E = lambda X: np.exp(-X**2/(2*sig**2))
off = lambda X: E(X)*(1+np.cos(2*np.pi*X))
a_on = quad(E, -np.inf, np.inf)[0]; a_off = quad(off, -60, 60, limit=500)[0]
print(f"area tag-off / area E = {a_off/a_on:.12f} (target 1 for equal areas without rescaling: E*(1+cos) vs E)")
# idealized: each path amplitude sqrt(E/2), relative phase 2piX; tag states A,B orthogonal
X = np.linspace(-30, 30, 20001)
psi1 = np.sqrt(E(X)/2)*np.exp(1j*np.pi*X); psi2 = np.sqrt(E(X)/2)*np.exp(-1j*np.pi*X)
P_notag = np.abs(psi1+psi2)**2
P_tag = np.abs(psi1)**2 + np.abs(psi2)**2       # orthogonal tags: cross term * <A|B> = 0
print("max |P_notag - off| =", np.max(np.abs(P_notag-off(X))))
print("max |P_tag - E| =", np.max(np.abs(P_tag-E(X))))
# smoothness of tag-on over full range: Gaussian has a single maximum, no local minima
d = np.diff(P_tag); sign_changes = np.sum(np.diff(np.sign(d[np.abs(d)>1e-300])) != 0)
print("number of turning points of tag-on curve over [-30,30]:", sign_changes)
ok = abs(a_off/a_on-1) < 1e-9 and np.max(np.abs(P_tag-E(X))) < 1e-12 and sign_changes == 1
print("PASS" if ok else "FAIL")
