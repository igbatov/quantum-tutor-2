# Figure captions: a-weights-concentrate "weight only 0.42" at N=4, spreads 0.217,0.108,0.054,0.027;
# a-deviant-length "every curve falls toward zero as N grows" -- test monotonicity of exact curves over integer N
import numpy as np
from scipy.stats import binom
from scipy.special import logsumexp
ok=True; p=0.25
w1=binom.pmf(1,4,p); print("w(1/4) at N=4",w1); ok&= abs(w1-0.42)<0.005
for N,s in zip([4,16,64,256],[0.217,0.108,0.054,0.027]):
    v=np.sqrt(p*(1-p)/N); print(N,v); ok&= abs(v-s)<6e-4
def dev(N,eps):
    m=np.arange(N+1); lw=binom.logpmf(m,N,p); mask=np.abs(m/N-p)>eps+1e-12
    return np.exp(logsumexp(lw[mask]))
mono=True
for eps in [0.05,0.1]:
    Ns=np.arange(10,401); d=np.array([dev(N,eps) for N in Ns])
    rises=np.where(np.diff(d)>0)[0]
    print("eps",eps,"number of N in 10..400 where exact deviant length rises at N->N+1:",len(rises),"examples",[(Ns[i],round(d[i],4),round(d[i+1],4)) for i in rises[:4]])
    print("   max relative rise",np.max(d[1:]/d[:-1]))
    mono&= len(rises)==0
print("caption numbers:", "PASS" if ok else "FAIL")
print("'every curve falls toward zero as N grows' strictly monotone:", "PASS" if mono else "FAIL (overall trend to zero holds, but exact curves zigzag)")
