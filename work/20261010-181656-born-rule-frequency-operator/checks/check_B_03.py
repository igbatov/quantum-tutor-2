# Claim: "Its eigenvalues ... 0, 1/N, ..., 1"; eigenvectors = lists on one m; N=4 binomials 1,4,6,4,1;
# "sum w_m = 1"; "Psi_N ... not an eigenvector ... at any finite N"; F_2 matrix; P.P=P
import itertools, numpy as np
from math import comb
ok=True
P=np.diag([0,1]); ok&=np.array_equal(P@P,P)
for N in [2,3,4,6]:
    strings=list(itertools.product([0,1],repeat=N))
    F=np.diag([sum(s)/N for s in strings])
    ev=sorted(set(np.round(np.diag(F),12)))
    ok&=np.allclose(ev,[m/N for m in range(N+1)])
    # multiplicity of each eigenvalue = C(N,m)
    mult=[int(np.sum(np.isclose(np.diag(F),m/N))) for m in range(N+1)]
    ok&= mult==[comb(N,m) for m in range(N+1)]
    for p in [0.1,0.5,0.73]:
        amp=np.array([np.sqrt(1-p)**(N-sum(s))*np.sqrt(p)**sum(s) for s in strings])
        w=[sum(amp[i]**2 for i,s in enumerate(strings) if sum(s)==m) for m in range(N+1)]
        ok&=np.allclose(w,[comb(N,m)*p**m*(1-p)**(N-m) for m in range(N+1)]) and abs(sum(w)-1)<1e-12
        # not eigenvector: min over lam of |(F-lam)psi|^2 >0
        lam=amp@F@amp; r=(F-lam*np.eye(len(amp)))@amp; ok&= r@r>1e-6
    print(f"N={N}: eigenvalues {ev}, multiplicities {mult}")
print("N=4 binomials:",[comb(4,m) for m in range(5)]); ok&=[comb(4,m) for m in range(5)]==[1,4,6,4,1]
print("p=0.1 not among N=4 readings:", 0.1 not in [m/4 for m in range(5)])
strings=list(itertools.product([0,1],repeat=2))
P1=np.diag([s[0] for s in strings]); P2=np.diag([s[1] for s in strings])
print("P1 diag",np.diag(P1),"P2 diag",np.diag(P2)); ok&=list(np.diag(P1))==[0,0,1,1] and list(np.diag(P2))==[0,1,0,1]
print("PASS" if ok else "FAIL")
