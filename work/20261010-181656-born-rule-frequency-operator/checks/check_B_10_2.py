# Claims in figure captions and the exercise: b-opening minima "0.045, 0.009, 0.0009" (N=2,10,100);
# b-counter-readings "0.0036 at 3/4 and 0.0001 at 1", spreads "0.25 ... 0.15"; b-model-2 "N x w_6 = 0.0014",
# spreads 0.095, 0.030, 0.009; b-how-they-relate "0.25, 0.10, 0.036, 0.012"; Check yourself N=2, c1=1/sqrt2
import numpy as np
from math import comb
ok=True
mins=[0.09/N for N in (2,10,100)]; print("opening minima",mins); ok&=np.allclose(mins,[0.045,0.009,0.0009])
w4=[comb(4,m)*.1**m*.9**(4-m) for m in range(5)]; print("N=4 p=.1 w",np.round(w4,4)); ok&=abs(w4[3]-0.0036)<1e-12 and abs(w4[4]-1e-4)<1e-12
s=[np.sqrt(p*(1-p)/4) for p in (.5,.1)]; print("spreads N=4",s); ok&=np.allclose(s,[0.25,0.15])
w6=10*comb(10,6)*.1**6*.9**4; print("N*w_6 (N=10)",w6); ok&=abs(w6-0.0014)<5e-5
# largest beyond 0.5 for N=10 (m=6..10) and for N=100,1000 smaller
for N in (10,100,1000):
    v=max(N*comb(N,m)*.1**m*.9**(N-m) for m in range(N+1) if m/N>0.5); print(f"N={N}: max N*w_m beyond 0.5 = {v:.3g}"); ok&=v<=w6+1e-12
sp=[np.sqrt(.09/N) for N in (10,100,1000)]; print("spreads",np.round(sp,3)); ok&=np.allclose(sp,[0.095,0.030,0.009],atol=6e-4)
fq=[1/(3**q+1) for q in (1,2,3,4)]; print("f_q",np.round(fq,3)); ok&=np.allclose(fq,[0.25,0.10,0.036,0.012],atol=6e-4)
# f_q agrees for all q at p=0,1/2,1
for p in (0,.5,1): ok&=len(set(round(np.sqrt(p)**q/(np.sqrt(1-p)**q+np.sqrt(p)**q),12) for q in (1,2,3,4)))==1
# exercise
psi=np.full(4,.5); F=np.diag([0,.5,.5,1]); lams=np.linspace(0,1,100001)
r=[np.sum(((np.diag(F)-l)*psi)**2) for l in lams]; i=int(np.argmin(r)); print("exercise: lam*",lams[i],"min",r[i]); ok&=abs(lams[i]-.5)<1e-9 and abs(r[i]-1/8)<1e-12
print("PASS" if ok else "FAIL")
