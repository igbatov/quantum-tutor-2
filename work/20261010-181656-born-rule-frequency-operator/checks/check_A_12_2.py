# Figure captions: a-weights-concentrate "weight only 0.42", spreads 0.217..0.027;
# a-deviant-length (revised): "bounds ... exceed 1 for N below 75 and 19"; "exact ... zigzag at small N";
# "continue down to about 1e-280 and 1e-1077 at N = 1e5"; "At no N is any of them zero"
import numpy as np
from scipy.stats import binom
from scipy.special import logsumexp
ok=True; p=0.25
w1=binom.pmf(1,4,p); print("w(1/4) at N=4",w1); ok&= abs(w1-0.42)<0.005
for N,s in zip([4,16,64,256],[0.217,0.108,0.054,0.027]):
    v=np.sqrt(p*(1-p)/N); print(N,v); ok&= abs(v-s)<6e-4
def logdev(N,eps):
    m=np.arange(N+1); lw=binom.logpmf(m,N,p); mask=np.abs(m/N-p)>eps+1e-12
    return logsumexp(lw[mask])
for eps,thr in [(0.05,75),(0.1,19)]:
    b=lambda N: p*(1-p)/(N*eps**2)
    Nstar=min(N for N in range(1,1000) if b(N)<=1); print("eps",eps,"bound <=1 from N =",Nstar)
    ok&= Nstar in (thr, thr) or (eps==0.1 and Nstar==19)
    Ns=np.arange(10,401); d=np.array([logdev(N,eps) for N in Ns]); rises=int(np.sum(np.diff(d)>0))
    print("  rises N->N+1 in 10..400:",rises); ok&= rises>0
    l5=logdev(100000,eps)/np.log(10); print("  log10 exact at N=1e5:",l5)
    ok&= np.isfinite(l5)
    exp=-280 if eps==0.05 else -1077
    ok&= abs(l5-exp)<3
    # nonzero: all-R string always deviant
    ok&= abs(1-p)>eps
print("PASS" if ok else "FAIL")
