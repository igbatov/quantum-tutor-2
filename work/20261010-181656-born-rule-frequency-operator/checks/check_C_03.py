# Claim: "total maverick weight < p(1-p)/(N eps^2)"; "64/N ... 0.064 at N=1000, 0.0064 at 10^4, 0.0009 at 70000"
# and "exact maverick weight ... roughly 10^-4 at N = 1000 for eps = 0.05"
import numpy as np
from scipy.stats import binom
from mpmath import mp, binomial, mpf
p=0.8; ok=True
for N,claim in [(1000,0.064),(10**4,0.0064),(70000,0.0009)]:
    b=0.16/(N*0.05**2); print("N",N,"bound",b,"claimed",claim); ok&=abs(b-claim)/claim<0.02
def mav(N,eps):
    mp.dps=50; P=mpf(p)
    return sum(binomial(N,m)*P**m*(1-P)**(N-m) for m in range(N+1) if abs(mpf(m)/N-P)>eps+mpf(10)**-30)
def mav_sc(N,eps):
    m=np.arange(N+1); sel=np.abs(m/N-p)>eps+1e-12
    return binom.pmf(m[sel],N,p).sum()
w=mav(1000,mpf('0.05'))
lo=sum(binom.pmf(m,1000,p) for m in range(0,750)); hi=sum(binom.pmf(m,1000,p) for m in range(851,1001))
print("N=1000 eps=0.05 exact maverick weight",float(w)," lower tail m<750:",lo," upper tail m>850:",hi)
print("  (if boundary m=750,850 counted as maverick:",mav_sc(1000,0.05-1e-9),")")
ok&= 0.3e-4 < float(w) < 3e-4
# bound holds for many N, eps
for N in [1,2,3,5,10,20,50,100,1000,10000]:
    for eps in [0.01,0.05,0.1,0.3]:
        ok&= mav_sc(N,eps) < 0.16/(N*eps**2)
print("exact eps=0.05 at N=1e4:",mav_sc(10**4,0.05),"N=70000:",mav_sc(70000,0.05))
print("PASS" if ok else "FAIL")
