# Claims: "exactly the sum over every way, just sorted by slit" and "A way's amplitude depends on its
# length ... cancel (completely in an ideal set-up, almost completely in a real one)".
# Check with exact path lengths (no far-field approximation): source on axis, each way = source -> point
# in slit -> screen spot; amplitude ~ exp(i k (r1 + r2)) / sqrt(r1 r2) (2D Huygens). Finite distances.
import numpy as np
lam = 1.0; k = 2*np.pi/lam; d = 100*lam; a = d/4
Ls, L = 2e5*lam, 2e5*lam                                     # source and screen distances
N = 2000
yL = -d/2 + a*((np.arange(N)+0.5)/N - 0.5); yR = -yL[::-1]
fringe = lam*L/d
xs = np.linspace(-6, 6, 2401)*fringe
def amp(ys):
    r1 = np.sqrt(Ls**2 + ys**2)[None, :]
    r2 = np.sqrt(L**2 + (xs[:, None] - ys[None, :])**2)
    return (np.exp(1j*k*(r1 + r2))/np.sqrt(r1*r2)).sum(axis=1)
psiL, psiR = amp(yL), amp(yR); allw = amp(np.concatenate([yL, yR]))
eg = np.max(np.abs(psiL + psiR - allw))/np.max(np.abs(allw))
P = np.abs(psiL + psiR)**2; P /= P.max()
X = xs/fringe; ideal = np.sinc(X/4)**2*np.cos(np.pi*X)**2
print(f"grouped vs all-at-once (exact path lengths): rel diff {eg:.1e}")
print(f"max deviation from ideal Fraunhofer pattern: {np.max(np.abs(P - ideal)):.1e}")
for x0 in (0.5, 1.5):
    m = np.abs(X - x0) < 0.2; i = np.argmin(P[m])
    print(f"dark stripe near X={x0}: min {P[m][i]:.1e} at X={X[m][i]:.4f}")
# a 'real' set-up: slightly unequal slits (90% amplitude) -> nonzero but small minimum
P2 = np.abs(psiL + 0.9*psiR)**2; P2 /= P2.max(); m = np.abs(X - 0.5) < 0.2
print(f"with unequal slits (0.9): dark-stripe min {P2[m].min():.1e} of peak (almost, not completely)")
ok = eg < 1e-10 and np.max(np.abs(P - ideal)) < 0.02 and P2[m].min() > 1e-4
print("PASS" if ok else "FAIL")
