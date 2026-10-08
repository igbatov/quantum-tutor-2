# Claim: "linked in ways no plan agreed in advance ... could produce, yet never ... sends a message"
# CHSH for singlet: 2*sqrt(2) > 2 (local-hidden-variable bound); Bob's marginals independent of Alice's setting.
import numpy as np, itertools
X = np.array([[0,1],[1,0]]); Z = np.array([[1,0],[0,-1]])
psi = np.array([0,1,-1,0])/np.sqrt(2); rho = np.outer(psi, psi.conj())
def obs(t): return np.cos(t)*Z + np.sin(t)*X
def E(a,b): return np.real(psi.conj() @ np.kron(obs(a), obs(b)) @ psi)
a, a2, b, b2 = 0, np.pi/2, np.pi/4, 3*np.pi/4
S = abs(E(a,b) - E(a,b2) + E(a2,b) + E(a2,b2))
print(f"quantum CHSH S = {S:.6f}, 2*sqrt2 = {2*np.sqrt(2):.6f}")
# best deterministic local strategy
best = max(abs(A1*B1 - A1*B2 + A2*B1 + A2*B2) for A1,A2,B1,B2 in itertools.product([1,-1],repeat=4))
print(f"max over local pre-agreed plans = {best}")
# no-signalling: Bob's outcome probabilities for each Alice setting
I = np.eye(2); ok_ns = True
for tb in [b, b2]:
    Pb = (I + obs(tb))/2
    for ta in [a, a2]:
        pb = sum(np.real(np.trace(rho @ np.kron((I+s*obs(ta))/2, Pb))) for s in (1,-1))
        ok_ns &= abs(pb-0.5) < 1e-12
print(f"Bob's marginals independent of Alice's setting: {ok_ns}")
# joint state not a product: Schmidt rank 2
sv = np.linalg.svd(psi.reshape(2,2), compute_uv=False)
print(f"Schmidt coefficients {sv} (rank 2 -> cannot split into one wave per particle)")
ok = abs(S-2*np.sqrt(2)) < 1e-9 and best == 2 and ok_ns and np.sum(sv > 1e-12) == 2
print("PASS" if ok else "FAIL")
