# Gleason restatement (final-C, Model 3):
#  "the chance must be a weighted average of squared shadows" (Gleason: chance = Tr(rho P))
#  "Add one more fact, that an outcome whose direction is the arrow's own is certain,
#   and the average collapses to the squared shadow of that one arrow"
#  "'every outcome equally likely, whatever the arrow' is such an average, over arrows pointing every way,
#   and it passes the three conditions while ignoring the arrow"
import numpy as np
rng = np.random.default_rng(7)
def rand_state(d):
    v = rng.normal(size=d) + 1j*rng.normal(size=d); return v/np.linalg.norm(v)
def rand_basis(d):
    q, _ = np.linalg.qr(rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d))); return q
ok = True
for d in [3, 4, 6]:
    G = rng.normal(size=(d, d)) + 1j*rng.normal(size=(d, d)); rho = G@G.conj().T; rho /= np.trace(rho).real
    p, V = np.linalg.eigh(rho)
    err = 0; serr = 0
    for _ in range(200):
        Q = rand_basis(d)
        tr = np.array([np.real(Q[:, k].conj()@rho@Q[:, k]) for k in range(d)])
        avg = np.array([np.sum(p*np.abs(V.conj().T@Q[:, k])**2) for k in range(d)])
        err = max(err, np.abs(tr-avg).max()); serr = max(serr, abs(tr.sum()-1))
    # certainty along psi forces rho = |psi><psi|: the largest possible <psi|rho|psi> is the largest weight
    print(f"d={d}: Tr(rho P) vs weighted average of squared shadows: max diff {err:.1e}; sums to 1 within {serr:.1e}; "
          f"weights {np.round(p, 3)}, so the best any direction can reach is {p.max():.3f} < 1")
    ok &= err < 1e-12 and serr < 1e-12 and p.max() < 1
    psi = rand_state(d); rho1 = np.outer(psi, psi.conj())
    e = rand_state(d)
    ok &= abs(np.real(psi.conj()@rho1@psi) - 1) < 1e-12 and abs(np.real(e.conj()@rho1@e) - abs(np.vdot(e, psi))**2) < 1e-12
# uniform average over arrows pointing every way = identity/d, giving 1/d to every outcome whatever the arrow
d = 3; N = 400000
Z = rng.normal(size=(N, d)) + 1j*rng.normal(size=(N, d)); Z /= np.linalg.norm(Z, axis=1, keepdims=True)
rhoU = (Z.T @ Z.conj())/N
print("Haar average of |psi><psi| in d=3:\n", np.round(rhoU, 3))
devU = np.abs(rhoU - np.eye(d)/d).max()
print(f"max deviation from I/3: {devU:.1e} (Monte Carlo, tolerance 5e-3); chance of the outcome along the arrow under this rule: 1/3, not 1")
ok &= devU < 5e-3
print("PASS" if ok else "FAIL")
