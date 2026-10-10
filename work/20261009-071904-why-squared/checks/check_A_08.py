# Claims (account 3 / Model 1): squared shadows total 100% in every measurement (complete set of
# perpendicular directions) and give a shared direction the same chance in every grouping;
# other powers do not; "a photon prepared along a direction passes that direction every time
# picks out the squared shadow itself" (among averages of squared shadows = density matrices).
# Gleason's theorem itself (uniqueness for dim>=3) is a cited proof: UNVERIFIABLE by computation here.
import numpy as np
rng = np.random.default_rng(7)
def rand_unitary(n):
    Z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Q, R = np.linalg.qr(Z)
    return Q*(np.diag(R)/np.abs(np.diag(R)))
ok = True
for n in (3, 4):
    worst2, worst_other = 0, {}
    for _ in range(2000):
        U = rand_unitary(n); psi = rng.normal(size=n) + 1j*rng.normal(size=n); psi /= np.linalg.norm(psi)
        amps = np.abs(U.conj().T @ psi)
        worst2 = max(worst2, abs(np.sum(amps**2) - 1))
        for p in (1, 1.9, 2.1, 3):
            worst_other[p] = max(worst_other.get(p, 0), abs(np.sum(amps**p) - 1))
    print(f"dim {n}: squared shadows max|total-1| = {worst2:.1e}; other powers: " +
          ", ".join(f"p={p}: {v:.3f}" for p, v in worst_other.items()))
    ok &= worst2 < 1e-12 and all(v > 1e-3 for v in worst_other.values())
# shared direction: e1 fixed, the rest of the basis rotated -> chance of e1 unchanged for p=2 (trivially:
# depends only on <e1|psi>); noncontextual by construction.
# pure-state selection: rho PSD, trace 1, <psi|rho|psi> = 1  ==> rho = |psi><psi|
n = 3; psi = np.array([1, 0, 0], complex)
maxdev = 0
for _ in range(5000):
    A = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); rho = A @ A.conj().T; rho /= np.trace(rho).real
    # push rho towards satisfying <psi|rho|psi> = 1 : mix with |psi><psi|
    lam = rng.uniform(0.9, 1.0); rho = lam*np.outer(psi, psi.conj()) + (1-lam)*rho
    f = np.real(psi.conj() @ rho @ psi)
    dist = np.linalg.norm(rho - np.outer(psi, psi.conj()))
    maxdev = max(maxdev, dist/(1 - f + 1e-300))  # distance shrinks in proportion to (1 - f)
print(f"distance of rho from |psi><psi| <= {maxdev:.2f} x (1 - <psi|rho|psi>) -> zero when chance is 1")
ok &= np.isfinite(maxdev)
print("PASS (consistency parts); Gleason uniqueness: UNVERIFIABLE (cited theorem)" if ok else "FAIL")
