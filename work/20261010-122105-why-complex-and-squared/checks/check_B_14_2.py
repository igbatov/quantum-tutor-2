# Claim: Stueckelberg: "any such theory can be rewritten with twice as many real amplitudes plus one fixed operator that
# plays the role of i, and for a single system the two descriptions are the same theory".
# Check: c = a + i b -> (a, b); H = Hr + i Hi -> real generator; J = [[0,-1],[1,0]] (x) I commutes with it, J^2 = -1;
# the real evolution reproduces every |c_k|^2 = a_k^2 + b_k^2 and transition chance.
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(3); n = 3; ok = True
for _ in range(20):
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n)); H = A + A.conj().T
    c0 = rng.normal(size=n) + 1j*rng.normal(size=n); c0 /= np.linalg.norm(c0)
    Hr, Hi = H.real, H.imag
    # i dc/dt = H c  ->  d/dt (a, b) = [[Hi, Hr], [-Hr, Hi]] (a, b)
    G = np.block([[Hi, Hr], [-Hr, Hi]]); Jm = np.kron(np.array([[0,-1],[1,0]]), np.eye(n))
    ok &= np.allclose(G @ Jm, Jm @ G) and np.allclose(Jm @ Jm, -np.eye(2*n)) and np.allclose(G.T, -G)
    t = rng.uniform(0, 3); c = expm(-1j*H*t) @ c0; ab = expm(G*t) @ np.concatenate([c0.real, c0.imag])
    ok &= np.allclose(ab[:n] + 1j*ab[n:], c) and np.allclose(ab[:n]**2 + ab[n:]**2, np.abs(c)**2)
    phi = rng.normal(size=n) + 1j*rng.normal(size=n); phi /= np.linalg.norm(phi)
    pr = np.concatenate([phi.real, phi.imag])   # |<phi|c>|^2 = (pr.ab)^2 + (pr.J ab)^2
    ok &= np.isclose(abs(np.vdot(phi, c))**2, (pr @ ab)**2 + (pr @ Jm @ ab)**2)
print("PASS" if ok else "FAIL")
