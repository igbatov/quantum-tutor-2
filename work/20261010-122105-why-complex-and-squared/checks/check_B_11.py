# Claim: "H21 = conj(H12), which is the condition that the two energies of the coupled system
#  come out real".  Test: is it necessary? Counterexample with real diagonal, real eigenvalues,
#  H21 != conj(H12); then check whether |c1|^2+|c2|^2 is conserved.
import numpy as np
from scipy.linalg import expm
H = np.array([[0.0, 1.0], [4.0, 0.0]])
ev = np.linalg.eigvals(H)
print("eigenvalues of [[0,1],[4,0]]:", ev, "(real)")
c0 = np.array([1.0, 0.0], complex)
norms = [np.linalg.norm(expm(-1j*H*t) @ c0)**2 for t in np.linspace(0, 3, 7)]
print("|c1|^2+|c2|^2 over time:", np.round(norms, 3))
necessary = False   # real energies obtained without Hermiticity
# Correct statement: Hermitian <=> real eigenvalues AND orthogonal eigenvectors (stationary states mutually exclusive)
rng = np.random.default_rng(1)
good = True
for _ in range(200):
    Q, _r = np.linalg.qr(rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)))
    D = np.diag(rng.normal(size=2))
    Hh = Q @ D @ Q.conj().T
    good &= np.allclose(Hh, Hh.conj().T)
V = np.linalg.eig(H)[1]
print("eigenvectors of counterexample orthogonal?", abs(np.vdot(V[:, 0], V[:, 1])) < 1e-12)
print("real-eigenvalues + orthonormal eigenvectors => Hermitian (200 random):", good)
print("Claim 'H21 = conj H12 is THE condition for real energies':", "PASS" if necessary else
      "FAIL (sufficient, not necessary; norm not conserved in counterexample)")
