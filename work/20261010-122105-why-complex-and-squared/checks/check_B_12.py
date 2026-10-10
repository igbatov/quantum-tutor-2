# Claims: Banach/Lamperti "for p != 2 (1 <= p < inf, two or more levels) the only linear maps that
#  keep sum|c_k|^p fixed for every state are relabellings ... combined with turning each hand";
#  "For p = 2 the length-keeping maps are exactly the unitary ones, and the Schrodinger equation
#  generates them".  Numerical evidence (not a proof): search 2x2 complex matrices for p-isometries.
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm
rng = np.random.default_rng(0)
S = rng.normal(size=(2, 300)) + 1j*rng.normal(size=(2, 300))
def pn(X, p): return (np.abs(X)**p).sum(0)**(1/p)
def loss(z, p):
    M = (z[:4] + 1j*z[4:]).reshape(2, 2)
    return np.mean((pn(M @ S, p) / pn(S, p) - 1)**2)
def offpattern(M):
    a = np.abs(M); return min(max(a[0, 1], a[1, 0]), max(a[0, 0], a[1, 1])) / a.max()
ok = True
for p in [1, 3, 4]:
    found = []
    for trial in range(40):
        r = minimize(loss, rng.normal(size=8), args=(p,), method='BFGS', options={'gtol': 1e-12, 'maxiter': 5000})
        if r.fun < 1e-10:
            M = (r.x[:4] + 1j*r.x[4:]).reshape(2, 2); found.append(offpattern(M))
    print(f"p={p}: {len(found)} exact isometries found; max off-pattern ratio {max(found) if found else None:.2e}")
    ok &= len(found) > 0 and max(found) < 1e-4
    # a gradual swap exp(-iHt) with H12 != 0 breaks the p-norm
    Hx = np.array([[0, -1], [-1, 0]])
    U = expm(-1j*Hx*np.pi/4); c = np.array([1, 0])
    print(f"   p={p}: after quarter swap, sum|c|^p = {(np.abs(U @ c)**p).sum():.4f}")
for p in [2]:
    for _ in range(20):
        A = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); H = A + A.conj().T
        U = expm(-1j*H*0.7)
        ok &= np.allclose(U.conj().T @ U, np.eye(2)) and np.allclose(pn(U @ S, 2), pn(S, 2))
    # a p=2 isometry found by search is unitary
    r = minimize(loss, rng.normal(size=8), args=(2,), method='BFGS', options={'gtol': 1e-12})
    M = (r.x[:4] + 1j*r.x[4:]).reshape(2, 2)
    print("p=2 isometry from search unitary?", np.allclose(M.conj().T @ M, np.eye(2), atol=1e-5),
          "off-pattern ratio", round(offpattern(M), 3))
print("PASS (numerical evidence consistent with the theorem)" if ok else "FAIL")
