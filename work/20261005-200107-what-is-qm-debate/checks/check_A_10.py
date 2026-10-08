# Claims: "correlated in ways no answers agreed in advance ... could reproduce"; "no message can be sent this way"
import numpy as np, itertools
Z = np.array([[1,0],[0,-1]]); X = np.array([[0,1],[1,0]])
psi = np.array([1,0,0,1])/np.sqrt(2)  # Bell state
E = lambda A, B: psi @ np.kron(A, B) @ psi
A0, A1 = Z, X
B0, B1 = (Z+X)/np.sqrt(2), (Z-X)/np.sqrt(2)
S_q = E(A0,B0)+E(A0,B1)+E(A1,B0)-E(A1,B1)
S_lhv = max(a0*b0+a0*b1+a1*b0-a1*b1 for a0,a1,b0,b1 in itertools.product([1,-1], repeat=4))
print("quantum CHSH =", S_q, " (2*sqrt2 =", 2*np.sqrt(2), "); best pre-agreed answers =", S_lhv)
# No signalling: Bob's outcome probabilities independent of Alice's measurement choice
rho = np.outer(psi, psi)
def bob_marginal(Aobs):
    w, v = np.linalg.eigh(Aobs); out = np.zeros((2,2))
    for i in range(2):
        P = np.kron(np.outer(v[:,i], v[:,i]), np.eye(2)); r = P @ rho @ P
        out += r.reshape(2,2,2,2).trace(axis1=0, axis2=2)
    return out
m0, m1 = bob_marginal(A0), bob_marginal(A1)
print("Bob's state, Alice measures Z:\n", m0.round(6), "\nAlice measures X:\n", m1.round(6))
ok = abs(S_q - 2*np.sqrt(2)) < 1e-12 and S_lhv == 2 and np.allclose(m0, m1)
print("PASS" if ok else "FAIL")
