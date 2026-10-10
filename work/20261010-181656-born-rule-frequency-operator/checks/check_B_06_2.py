# Claim: "D_eps(N) <= p(1-p)/(N eps^2)"; deviant table (eps=0.05): 100/N, 36/N, Hoeffding 2exp(-2N eps^2)
# 1.21, 0.0135, 3.9e-22, below 1e-2000; "exponential bound is weaker than Chebyshev's at N = 100";
# overtakes (among informative bounds, Chebyshev < 1) "between N=400 and 500 at p=1/2, between 700 and 800 at p=0.1"; exact N=1000 p=1/2 "about 0.0014"
import numpy as np
from scipy.stats import binom
from math import log10, exp
eps=0.05; ok=True
def exact(N,p):
    m=np.arange(N+1); dev=np.abs(m/N-p)>eps+1e-12
    return binom(N,p).pmf(m)[dev].sum()
rows=[]
for N in [100,1000,10**4,10**6]:
    c5=0.25/(N*eps**2); c1=0.09/(N*eps**2); hlog=log10(2)-2*N*eps**2/np.log(10)
    e5=exact(N,0.5); e1=exact(N,0.1)
    print(f"N={N}: Cheb .5 {c5:.4g}; Cheb .1 {c1:.4g}; Hoeffding log10 {hlog:.2f}; exact .5 {e5:.3g}, .1 {e1:.3g}")
    ok&=abs(c5-100/N)<1e-12 and abs(c1-36/N)<1e-12 and e5<=c5 and e1<=c1 and e5<=10**hlog and e1<=10**hlog
    rows.append((N,c5,c1,hlog,e5,e1))
ok&=abs(2*exp(-0.5)-1.21)<0.005 and abs(2*exp(-5)-0.0135)<5e-5 and abs(2*exp(-50)-3.9e-22)<0.05e-22 and rows[-1][3]< -2000
H=lambda N:2*np.exp(-2*N*eps**2)
print("N=100: Hoeffding",H(100),"> Cheb",1.0,"and",0.36); ok&=H(100)>1 and H(100)>0.36
for p,lo,hi in [(0.5,400,500),(0.1,700,800)]:
    Ns=np.arange(1,5000); C=p*(1-p)/(Ns*eps**2)
    # compare only where Chebyshev is informative (<1); below that both bounds exceed 1
    inf=C<1; cross=Ns[inf][np.argmax(H(Ns[inf])<C[inf])]
    sm=Ns[(~inf)&(H(Ns)<C)]; print(f"  (Hoeffding numerically below Chebyshev for N<={sm.max() if sm.size else None}, where both exceed 1)")
    print(f"p={p}: Hoeffding first below Chebyshev at N={cross} (text between {lo} and {hi})"); ok&= lo<cross<=hi
    ok&= all(H(N)<p*(1-p)/(N*eps**2) for N in range(cross,100000,37))
e=exact(1000,0.5); print("exact N=1000 p=.5:",e); ok&=abs(e-0.0014)<0.00015
print("ratio exact/Hoeffding N=1e3,1e4:", rows[1][4]/10**rows[1][3], rows[2][4]/10**rows[2][3])
for N in [10,57,300]:
    for p in [0.1,0.37,0.5]:
        m=np.arange(N+1); w=binom(N,p).pmf(m); dev=np.abs(m/N-p)>eps
        ok&= eps**2*w[dev].sum() <= (w[dev]*(m[dev]/N-p)**2).sum()+1e-15 <= (w*(m/N-p)**2).sum()+2e-15 and abs((w*(m/N-p)**2).sum()-p*(1-p)/N)<1e-12
print("PASS" if ok else "FAIL")
