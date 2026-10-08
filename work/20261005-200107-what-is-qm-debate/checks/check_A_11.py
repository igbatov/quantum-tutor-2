# Claim: "the amplitudes change over time in a fully predictable way" (deterministic, norm-preserving evolution)
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(0)
M = rng.normal(size=(6,6)) + 1j*rng.normal(size=(6,6)); H = (M + M.conj().T)/2
psi0 = rng.normal(size=6) + 1j*rng.normal(size=6); psi0 /= np.linalg.norm(psi0)
U = expm(-1j*H*2.7)
p1 = U @ psi0; p2 = U @ psi0
print("unitary:", np.allclose(U.conj().T @ U, np.eye(6)), " norm after:", np.linalg.norm(p1), " repeatable:", np.allclose(p1, p2))
ok = np.allclose(U.conj().T @ U, np.eye(6)) and abs(np.linalg.norm(p1)-1) < 1e-12 and np.allclose(p1, p2)
print("PASS" if ok else "FAIL")
