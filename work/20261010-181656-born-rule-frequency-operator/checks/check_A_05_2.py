# Claim: F_N diagonal, readings multiples of 1/N (diag 0,1/2,1/2,1 at N=2); p=0.1, N=4 not a reading;
# eigenvectors supported on one m; "Psi_N is not a sure-bet list at any finite N" for 0<p<1;
# F_N = (1/N) sum P^(k), P^(k)^2 = P^(k)
import numpy as np, itertools
ok=True
def build(N):
    strs=list(itertools.product([0,1],repeat=N))
    P=[np.diag([s[k] for s in strs]).astype(float) for k in range(N)]
    F=np.diag([sum(s)/N for s in strs]); return strs,P,F
strs,P,F=build(2); print(np.diag(F)); ok&= np.allclose(np.diag(F),[0,.5,.5,1])
for N in [2,3,4,5]:
    strs,P,F=build(N); ok&= np.allclose(F,sum(P)/N) and all(np.allclose(Pk@Pk,Pk) for Pk in P)
    ev=set(np.round(np.diag(F),12)); ok&= ev==set(np.round(np.arange(N+1)/N,12))
_,_,F4=build(4); print("N=4 readings",sorted(set(np.diag(F4))),"0.1 in?",any(abs(np.diag(F4)-0.1)<1e-12)); ok&= not any(abs(np.diag(F4)-0.1)<1e-12)
for p in [0.1,0.25,0.5,0.9]:
    for N in [1,2,3,6]:
        strs,P,F=build(N); c0,c1=np.sqrt(1-p),np.sqrt(p)
        psi=np.array([np.prod([c1 if x else c0 for x in s]) for s in strs])
        lam=psi@F@psi; r=np.linalg.norm(F@psi-lam*psi); ok&= r>1e-6  # not eigenvector
print("PASS" if ok else "FAIL")
