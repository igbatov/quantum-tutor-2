# Claims: "complex quantum mechanics predicts up to 6 sqrt2 approx 8.49"; "real-hand theories cannot
#  score above 7.66" (Renou et al. 2021).
# Check: 6 sqrt2 numerically; the standard strategy (Bob's Bell-state measurement swaps entanglement to
# A-C; Alice measures Z, X, Y; Charlie measures (Z+-X)/sqrt2, (Z+-Y)/sqrt2, (X+-Y)/sqrt2) gives three
# CHSH values of 2 sqrt2 each (Tsirelson-maximal), and uses Y (imaginary entries).
# The real bound 7.66 needs an NPA-type SDP over real models: not reproduced here.
import numpy as np
I2 = np.eye(2); Z = np.diag([1, -1]).astype(complex); Xp = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]])
bell = {'Phi+': np.array([1, 0, 0, 1])/np.sqrt(2), 'Phi-': np.array([1, 0, 0, -1])/np.sqrt(2),
        'Psi+': np.array([0, 1, 1, 0])/np.sqrt(2), 'Psi-': np.array([0, 1, -1, 0])/np.sqrt(2)}
def E(s, A, C): return np.real(np.vdot(s, np.kron(A, C) @ s))
ok = abs(6*np.sqrt(2) - 8.485) < 1e-3
print("6 sqrt2 =", 6*np.sqrt(2))
total_by_b = {}
for b, s in bell.items():
    tot = 0
    for (P, Q) in [(Z, Xp), (Z, Y), (Xp, Y)]:
        best = 0
        for sP in [1, -1]:
            for sQ in [1, -1]:  # Charlie adapts signs to Bell outcome (equivalently relabel outcomes)
                C1 = (sP*P.conj() + sQ*Q.conj())/np.sqrt(2); C2 = (sP*P.conj() - sQ*Q.conj())/np.sqrt(2)
                val = E(s, P, C1) + E(s, Q, C1) + E(s, P, C2) - E(s, Q, C2)
                best = max(best, val)
        tot += best
    total_by_b[b] = tot
print("sum of three CHSH values per Bell outcome:", {k: round(v, 4) for k, v in total_by_b.items()})
ok &= all(abs(v - 6*np.sqrt(2)) < 1e-9 for v in total_by_b.values())
print("6 sqrt2 reached with complex Y; 3 x Tsirelson 2 sqrt2 is the maximum:", "PASS" if ok else "FAIL")
print("7.66 real bound: UNVERIFIABLE here (requires the SDP of Renou et al.)")
