# Claim: "D_eps(N) <= p(1-p)/(N eps^2)"; deviant table (eps=0.05): 100/N, 36/N, Hoeffding 2exp(-2N eps^2)
# values 1.21, 0.0135, 3.9e-22, below 1e-2000; "exact value at N=1000, p=1/2 is about 0.0014";
# "Every column goes to zero ..., the exact value fastest"; label "sharper bound ... (Hoeffding 1963)"
import numpy as np
from scipy.stats import binom
from math import log10, exp
eps=0.05; ok=True
def exact(N,p):
    m=np.arange(N+1); dev=np.abs(m/N-p)>eps+1e-12
    return binom(N,p).pmf(m)[dev].sum()
rows=[]
for N in [100,1000,10**4,10**6]:
    c5=0.25/(N*eps**2); c1=0.09/(N*eps**2); h=2*exp(-2*N*eps**2) if N<10**5 else None
    hlog=log10(2)-2*N*eps**2/np.log(10)
    e5=exact(N,0.5); e1=exact(N,0.1)
    print(f"N={N}: Cheb p=.5 {c5:.4g} (100/N={100/N:.4g}); Cheb p=.1 {c1:.4g} (36/N={36/N:.4g}); Hoeffding log10={hlog:.2f} val={h}; exact p=.5 {e5:.3g}, p=.1 {e1:.3g}")
    ok&=abs(c5-100/N)<1e-12 and abs(c1-36/N)<1e-12 and e5<=c5 and e1<=c1 and e5<=10**hlog and e1<=10**hlog
    rows.append((N,c5,c1,hlog,e5,e1))
ok&=abs(2*exp(-0.5)-1.21)<0.005 and abs(2*exp(-5)-0.0135)<5e-5 and abs(2*exp(-50)-3.9e-22)<0.05e-22
ok&=rows[-1][3]< -2000
e=exact(1000,0.5); print("exact N=1000 p=.5:",e); ok&=abs(e-0.0014)<0.00015
# "exact value fastest": compare decay of exact vs bounds between N=1000 and 10^4
print("ratio exact/Hoeffding N=1e3,1e4:", rows[1][4]/10**rows[1][3], rows[2][4]/10**rows[2][3])
# Chebyshev chain with eps^2 D <= sum w (m/N-p)^2 numerically
for N in [10,57,300]:
    for p in [0.1,0.37,0.5]:
        m=np.arange(N+1); w=binom(N,p).pmf(m); dev=np.abs(m/N-p)>eps
        ok&= eps**2*w[dev].sum() <= (w[dev]*(m[dev]/N-p)**2).sum()+1e-15 <= (w*(m/N-p)**2).sum()+2e-15 and abs((w*(m/N-p)**2).sum()-p*(1-p)/N)<1e-12
# "sharper": Hoeffding vs Chebyshev at each N
for N,c5,c1,hlog,_,_ in rows:
    print(f"N={N}: Hoeffding sharper than Chebyshev? p=.5: {10**hlog<c5}, p=.1: {10**hlog<c1}")
print("table arithmetic and bounds: PASS" if ok else "FAIL")
print("label 'sharper bound': FAIL at N=100 (1.21 > 1 and > 0.36); sharper from N=1000 on")
