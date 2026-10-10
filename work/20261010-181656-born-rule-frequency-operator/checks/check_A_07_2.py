# Claim: deviant bound p(1-p)/(N eps^2) = 75/N for p=1/4, eps=0.05: 0.075, 0.0075, 7.5e-5;
# "exact deviant length is far smaller, falling exponentially in N"; typical part >= 1-75/N; never zero at finite N
import numpy as np
from scipy.stats import binom
from scipy.special import logsumexp
ok=True; p=0.25
def logdev(N,eps):
    m=np.arange(N+1); lw=binom.logpmf(m,N,p); mask=np.abs(m/N-p)>eps+1e-12
    return logsumexp(lw[mask]) if mask.any() else -np.inf
print("bound const",p*(1-p)/0.05**2); ok&= abs(p*(1-p)/0.05**2-75)<1e-9
for N,b in [(1000,0.075),(10**4,0.0075),(10**6,7.5e-5)]:
    ld=logdev(N,0.05); print(N,"bound",75/N,"exact",np.exp(ld),"log10",ld/np.log(10)); ok&= abs(75/N-b)<1e-12 and np.exp(ld)<0.05*b
# exponential decay: -log(dev)/N tends to a constant (rate)
rates=[-logdev(N,0.05)/N for N in [10**4,10**5,10**6]]; print("rates",rates); ok&= rates[-1]>0 and abs(rates[-1]-rates[-2])/rates[-1]<0.05
# never zero at finite N (eps<max(p,1-p)): m=N always deviant with weight p^N>0
ok&= all(np.isfinite(logdev(N,0.05)) for N in [10,100,10**5])
print("PASS" if ok else "FAIL")
