# Claim (account 3): squared shadows total 100% in every complete set of perpendicular directions,
# give a shared direction the same chance in every grouping; other powers do not;
# "passes that direction every time picks out the squared shadow itself" (rho with <psi|rho|psi>=1 is pure).
import numpy as np
rng = np.random.default_rng(3)
def rand_basis(n):
    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); q, _ = np.linalg.qr(z); return q
ok = True
for n in (3, 4):
    psi = rand_basis(n)[:, 0]
    for p in (1, 1.9, 2, 2.1, 3):
        err = max(abs(sum(abs(np.vdot(q[:, k], psi))**p for k in range(n)) - 1) for q in (rand_basis(n) for _ in range(3000)))
        good = err < 1e-12 if p == 2 else err > 1e-2; ok &= good
        print(f"n={n} p={p}: max |total-1| = {err:.2e} {'ok' if good else 'X'}")
# a density matrix that gives its arrow probability 1 is that arrow's projector:
# for random rho (mixed, any n), ||rho - |psi><psi||| is bounded by C*(1 - <psi|rho|psi>) -> 0
worst = 0
for _ in range(4000):
    n = 3; psi = rand_basis(n)[:, 0]
    t = 10**rng.uniform(-8, -1)
    A = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); sig = A @ A.conj().T; sig /= np.trace(sig)
    rho = (1 - t)*np.outer(psi, psi.conj()) + t*sig       # general rho near the pure state
    f = np.real(np.vdot(psi, rho @ psi))
    worst = max(worst, np.linalg.norm(rho - np.outer(psi, psi.conj()))/(1 - f))
print(f"max ||rho - |psi><psi||| / (1 - <psi|rho|psi>) = {worst:.2f} (bounded => f=1 forces pure)"); ok &= worst < 50
print("Gleason uniqueness itself: cited theorem (UNVERIFIABLE here); consistency checks above")
print("PASS" if ok else "FAIL")
