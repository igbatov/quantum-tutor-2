# Claim: "real-amplitude theories cannot exceed about 7.66 while complex quantum mechanics
# allows up to 6 sqrt2 ~ 8.49" (Renou et al. network test).
# Part 1 (computable): build the swapping network (two Phi+ sources, Bob Bell measurement,
# Alice Z,X,Y; Charlie (Z+-X)/rt2,(Z+-Y)/rt2,(X+-Y)/rt2 up to outcome relabelling) and compute
# the score = average over Bob's outcome of three CHSH sums with Pauli-frame sign correction.
# Part 2: the 7.66 real bound needs an NPA-type SDP hierarchy -> UNVERIFIABLE here.
import numpy as np
I = np.eye(2); X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
k = lambda *a: np.kron(a[0], k(*a[1:])) if len(a) > 1 else a[0]
phi = np.array([1, 0, 0, 1])/np.sqrt(2)
psi = np.kron(phi, phi)  # order A, B1, B2, C
bell = [np.array(v)/np.sqrt(2) for v in ([1, 0, 0, 1], [1, 0, 0, -1], [0, 1, 1, 0], [0, 1, -1, 0])]
paulis = [I, Z, X, X @ Z]
A = [Z, X, Y]
T = 0; pb = []
for b, B in enumerate(bell):
    proj = np.kron(np.kron(I, np.outer(B, B.conj())), I)
    st = proj @ psi; p = np.vdot(st, st).real; pb.append(p)
    # reduce to A,C by contracting B1B2 with <B|
    M = st.reshape(2, 4, 2); ac = np.einsum('j,ijk->ik', B.conj(), M).reshape(4); ac /= np.linalg.norm(ac)
    # Pauli frame on Alice: find sigma with (sigma x I)|Phi+> ~ ac
    sig = max(paulis, key=lambda s: abs(np.vdot(np.kron(s, I) @ phi, ac)))
    Ab = [sig @ a @ sig.conj().T for a in A]      # = +- A_x
    E = lambda a, c: np.vdot(ac, np.kron(a, c) @ ac).real
    tot = 0
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        Cp = (A[i] + A[j]).T/np.sqrt(2); Cm = (A[i] - A[j]).T/np.sqrt(2)  # transpose = outcome relabel for Y
        tot += E(Ab[i], Cp) + E(Ab[j], Cp) + E(Ab[i], Cm) - E(Ab[j], Cm)
    T += p*tot
# Tsirelson check for each CHSH operator
ts = []
for (i, j) in [(0, 1), (0, 2), (1, 2)]:
    best = 0
    rng = np.random.default_rng(0)
    from scipy.optimize import minimize
    def neg(par):
        n1 = par[:3]/np.linalg.norm(par[:3]); n2 = par[3:]/np.linalg.norm(par[3:])
        C1 = sum(c*s for c, s in zip(n1, (X, Y, Z))); C2 = sum(c*s for c, s in zip(n2, (X, Y, Z)))
        Op = np.kron(A[i], C1 + C2) + np.kron(A[j], C1 - C2)
        return -np.linalg.eigvalsh(Op).max()
    for _ in range(20):
        r = minimize(neg, rng.normal(size=6)); best = max(best, -r.fun)
    ts.append(best)
print('p(b) =', np.round(pb, 4), ' complex-QM score =', round(T, 6), ' 6*sqrt2 =', round(6*np.sqrt(2), 6))
print('max of each CHSH operator =', np.round(ts, 6), '(2 sqrt2 =', round(2*np.sqrt(2), 6), ')')
ok = abs(T - 6*np.sqrt(2)) < 1e-9 and all(abs(t - 2*np.sqrt(2)) < 1e-6 for t in ts) and abs(6*np.sqrt(2) - 8.49) < 0.005
print('PASS (6 sqrt2 = 8.49 reached and is the max)' if ok else 'FAIL')
print('UNVERIFIABLE: real-QM bound ~7.66 (requires NPA SDP hierarchy; literature value 7.6605)')
