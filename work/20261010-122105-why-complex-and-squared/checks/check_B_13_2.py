# Claims: "complex quantum mechanics predicts up to 6 sqrt2 ~ 8.49" (caption "3 x 2 sqrt2"); "real-hand theories cannot
# score above 7.66" (Renou et al.; needs their SDP, not reproduced).
import numpy as np
Z = np.diag([1, -1]).astype(complex); Xp = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]])
bell = [np.array(v)/np.sqrt(2) for v in ([1,0,0,1], [1,0,0,-1], [0,1,1,0], [0,1,-1,0])]
E = lambda s, A, C: np.real(np.vdot(s, np.kron(A, C) @ s))
ok = abs(6*np.sqrt(2) - 8.49) < 0.005 and abs(3*2*np.sqrt(2) - 6*np.sqrt(2)) < 1e-12
for s in bell:
    tot = 0
    for P, Q in [(Z, Xp), (Z, Y), (Xp, Y)]:
        best = max(E(s,P,(a*P.conj()+b*Q.conj())/np.sqrt(2)) + E(s,Q,(a*P.conj()+b*Q.conj())/np.sqrt(2))
                   + E(s,P,(a*P.conj()-b*Q.conj())/np.sqrt(2)) - E(s,Q,(a*P.conj()-b*Q.conj())/np.sqrt(2))
                   for a in (1,-1) for b in (1,-1))
        tot += best
    print("score for this Bell outcome:", round(tot, 6)); ok &= abs(tot - 6*np.sqrt(2)) < 1e-9
print("6 sqrt2:", "PASS" if ok else "FAIL")
print("7.66: UNVERIFIABLE (requires the real-model SDP of Renou et al.)")
