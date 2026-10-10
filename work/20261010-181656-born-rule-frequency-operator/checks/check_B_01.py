# Claim: "has squared length (lambda - p)^2 + p(1-p)/N, shortest at lambda = p"
# plus <P_k>=p, <F_N>=p, <F_N^2>=p^2+p(1-p)/N; numbers p=0.1: 0.045 (N=2), 0.0009 (N=100), 0.000009 (N=1e4)
import itertools, numpy as np, sympy as sp
ok = True
# symbolic: exact for N=1..6 via explicit lists
p, lam = sp.symbols('p lam', positive=True)
c0, c1 = sp.sqrt(1-p), sp.sqrt(p)
for N in range(1, 7):
    R2 = 0; mean = 0; sq = 0; norm = 0
    for s in itertools.product([0,1], repeat=N):
        m = sum(s); amp = c0**(N-m)*c1**m
        R2 += amp**2*(sp.Rational(m, N)-lam)**2
        mean += amp**2*sp.Rational(m, N); sq += amp**2*sp.Rational(m, N)**2; norm += amp**2
    d1 = sp.simplify(sp.expand(R2 - ((lam-p)**2 + p*(1-p)/N)))
    d2 = sp.simplify(sp.expand(mean - p)); d3 = sp.simplify(sp.expand(sq - (p**2+p*(1-p)/N))); d4 = sp.simplify(sp.expand(norm-1))
    print(f"N={N}: R2-formula={d1}, <F>-p={d2}, <F^2>-formula={d3}, norm-1={d4}")
    ok &= (d1 == 0 and d2 == 0 and d3 == 0 and d4 == 0)
# per-ion <P_k>=p and <P_j P_k>=p^2, N=4 numeric with p=0.1
N=4; pv=0.1
strings=list(itertools.product([0,1],repeat=N))
amp=np.array([np.sqrt(1-pv)**(N-sum(s))*np.sqrt(pv)**sum(s) for s in strings])
Pk=[np.array([s[k] for s in strings]) for k in range(N)]
for k in range(N): ok &= abs(np.sum(amp**2*Pk[k])-pv)<1e-12
ok &= abs(np.sum(amp**2*Pk[0]*Pk[1])-pv**2)<1e-12
# numbers
for N, want in [(2,0.045),(100,0.0009),(10**4,0.000009)]:
    v=0.1*0.9/N; print(f"p=0.1 N={N}: p(1-p)/N={v:.3g} (text {want})"); ok &= abs(v-want)<1e-12
# minimum location
print("argmin over lambda:", sp.solve(sp.diff((lam-p)**2+p*(1-p)/sp.Symbol('N'),lam),lam))
print("PASS" if ok else "FAIL")
