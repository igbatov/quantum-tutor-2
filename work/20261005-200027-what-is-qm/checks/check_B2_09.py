# Claim: "after an ideal measurement that leaves the system intact, its arrow points along the answer it gave"
# Ideal (projective, Lueders) measurement: post-state = P_k psi/|P_k psi|; it lies in answer k's subspace,
# and repeating the measurement gives answer k with certainty. Test random 4-dim observables incl. degenerate.
import numpy as np
rng = np.random.default_rng(3); worst = 0
for _ in range(2000):
    Q, _r = np.linalg.qr(rng.normal(size=(4,4)) + 1j*rng.normal(size=(4,4)))
    vals = rng.choice([[1,2,3,4],[1,1,2,3],[1,1,2,2]])            # some answers degenerate
    psi = rng.normal(size=4)+1j*rng.normal(size=4); psi /= np.linalg.norm(psi)
    for e in set(vals):
        cols = Q[:, np.array(vals) == e]; Pk = cols @ cols.conj().T
        p = np.real(psi.conj() @ Pk @ psi)
        if p < 1e-9: continue
        post = Pk @ psi / np.sqrt(p)
        worst = max(worst, abs(np.real(post.conj() @ Pk @ post) - 1), np.linalg.norm(Pk @ post - post))
print("max deviation from 'repeat gives same answer with certainty / post-state in answer subspace':", worst)
print("PASS" if worst < 1e-10 else "FAIL")
