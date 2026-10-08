# Claims (Exp. 2, d = 4a, far screen): (a) stripes; (b) "no stripes ... two one-slit patterns added,
# a broad central band with faint one-slit side bands further out"; (c) +45 and -45 groups striped,
# "shifted by half a stripe spacing, bright where the first group was dark"; groups "make up the
# pattern of (b)"; "never ... stripes ... whatever is done to the partner"; (d) order irrelevant;
# figure caption: "true gaps at X = +-4 and +-8", side bands "under 5% of the centre";
# with real plates "each group's stripes sit a quarter of a spacing to one side or the other".
import numpy as np
from scipy.signal import argrelextrema
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def qwp(t): return rot(t) @ np.diag([1, 1j]) @ rot(-t)
H = np.array([1, 0]); V = np.array([0, 1]); J1, J2 = qwp(np.pi/4), qwp(-np.pi/4)
X = np.linspace(-12, 12, 48001); S = np.sinc(X/4)**2; amp = np.sqrt(S/2)
psi1 = amp*np.exp(1j*np.pi*X); psi2 = amp*np.exp(-1j*np.pi*X)
def pattern(plates, pv=None, pairs=((V, H), (H, V))):
    P = np.zeros_like(X); basis = [pv] if pv is not None else [H, V]
    for b in basis:
        f = np.zeros((2, X.size), complex)
        for sv, part in pairs:
            cc = np.vdot(b, part)/np.sqrt(2)
            a1 = J1@sv if plates else sv; a2 = J2@sv if plates else sv
            f += cc*(np.outer(a1, psi1)+np.outer(a2, psi2))
        P += np.sum(np.abs(f)**2, 0)
    return P
def vis(P):
    m = np.abs(X) < 3.5; r = P[m]/S[m]; return (r.max()-r.min())/(r.max()+r.min())
p45 = np.array([1, 1])/np.sqrt(2); m45 = np.array([1, -1])/np.sqrt(2)
Pa, Pb, Pp, Pm = pattern(False), pattern(True), pattern(True, p45), pattern(True, m45)
c = np.abs(X) <= 0.5
xa = X[c][np.argmax(Pa[c]/S[c])]; xp = X[c][np.argmax(Pp[c]/S[c])]; xm = X[c][np.argmax(Pm[c]/S[c])]
print(f"contrast (a) {vis(Pa):.3f} (b) {vis(Pb):.3f} (+45) {vis(Pp):.3f} (-45) {vis(Pm):.3f}; partner-H group {vis(pattern(True, H)):.3f}")
print(f"stripe peaks: untagged {xa:+.3f}, +45 group {xp:+.3f}, -45 group {xm:+.3f}")
print(f"max|(+45)+(-45)-(b)| = {np.max(np.abs(Pp+Pm-Pb)):.1e}; max|(b)-S| = {np.max(np.abs(Pb-S)):.1e}")
# bright where the other is dark
print(f"at +45 peak, -45 group / envelope = {np.interp(xp, X, Pm/np.maximum(S,1e-300)):.2e}")
rng = np.random.default_rng(5); worst = 0
for _ in range(50):
    u = rng.normal(size=2)+1j*rng.normal(size=2); u /= np.linalg.norm(u); w = np.array([-np.conj(u[1]), np.conj(u[0])])
    worst = max(worst, np.max(np.abs(pattern(True, u)+pattern(True, w)-Pb)))
print(f"50 random partner bases: worst |sum-(b)| = {worst:.1e}")
A = np.kron(rng.random((2, 2)), np.eye(2)); B = np.kron(np.eye(2), rng.random((2, 2)))
print("commutator slit-op / partner-op:", np.linalg.norm(A@B-B@A))
# (b) shape over the full far screen
Xw = np.linspace(-20, 20, 400001); Sw = np.sinc(Xw/4)**2
mx = argrelextrema(Sw, np.greater)[0]; mn = argrelextrema(Sw, np.less)[0]
print("maxima X:", np.round(Xw[mx], 2), "heights:", np.round(Sw[mx], 4))
print("zeros X:", np.round(Xw[mn], 2), "values:", Sw[mn].max())
side = sorted(Sw[mx])[-2]
ok = vis(Pa) > 0.99 and vis(Pb) < 1e-3 and vis(Pp) > 0.99 and vis(Pm) > 0.99 and abs(abs(xp-xm)-0.5) < 0.01 \
     and abs(abs(xp-xa)-0.25) < 0.01 and abs(abs(xm-xa)-0.25) < 0.01 and np.max(np.abs(Pp+Pm-Pb)) < 1e-12 \
     and worst < 1e-12 and side < 0.05 and np.allclose(np.sort(np.abs(Xw[mn]))[:4], [4, 4, 8, 8], atol=1e-3) and len(mx) > 1
print("PASS" if ok else "FAIL")
