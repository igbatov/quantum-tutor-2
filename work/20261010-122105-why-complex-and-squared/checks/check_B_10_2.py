# Claims: Banach-Lamperti "for p != 2 (1 <= p < inf, two or more levels) the only linear maps that keep sum|c_k|^p
# fixed for every state are relabellings ... combined with turning each hand"; "a relabelling ... none moves it
# gradually"; "For p = 2 the length-keeping linear maps are exactly the unitary ones, and every Hermitian equation
# generates a continuous family of them". Numerical evidence on 2x2 complex matrices (not a proof).
import numpy as np
from scipy.optimize import minimize
from scipy.linalg import expm
rng = np.random.default_rng(1)
S = rng.normal(size=(2, 300)) + 1j*rng.normal(size=(2, 300))
def pn(X, p): return (np.abs(X)**p).sum(0)**(1/p)
def loss(z, p):
    M = (z[:4] + 1j*z[4:]).reshape(2, 2); return np.mean((pn(M @ S, p)/pn(S, p) - 1)**2)
def offpattern(M):
    a = np.abs(M); return min(max(a[0,1], a[1,0]), max(a[0,0], a[1,1]))/a.max()
ok = True
for p in [1, 3, 4]:
    found = []
    for _ in range(30):
        r = minimize(loss, rng.normal(size=8), args=(p,), method='BFGS', options={'gtol': 1e-12, 'maxiter': 5000})
        if r.fun < 1e-10: found.append(offpattern((r.x[:4] + 1j*r.x[4:]).reshape(2, 2)))
    print(f"p={p}: {len(found)} isometries; max off-pattern ratio {max(found):.1e}"); ok &= len(found) > 5 and max(found) < 1e-4
    # a one-parameter family through the identity that stays within generalized permutations has constant |entries|:
    # moving chance gradually (|U21|^2 from 0 to between 0 and 1) is impossible
for _ in range(20):
    A = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)); H = A + A.conj().T
    for t in [0.1, 0.7, 2.3]:
        U = expm(-1j*H*t); ok &= np.allclose(U.conj().T @ U, np.eye(2))
r = minimize(loss, rng.normal(size=8), args=(2,), method='BFGS', options={'gtol': 1e-12})
M = (r.x[:4] + 1j*r.x[4:]).reshape(2, 2)
u2 = np.allclose(M.conj().T @ M, np.eye(2), atol=1e-5); print("p=2 search result unitary:", u2, "; off-pattern", round(offpattern(M), 3))
ok &= u2
print("PASS (numerical support)" if ok else "FAIL")
