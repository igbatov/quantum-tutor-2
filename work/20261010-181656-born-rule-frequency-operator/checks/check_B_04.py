# Claim: projection noise "variance ... Np(1-p) ... 100 ions at p=1/2 is 25, sd 5 ... p=0.1 is 9, sd 3";
# "ions at different places ... see slightly different fields, which lowers the scatter a little";
# "error bars of size sqrt(p(1-p)/M)"; figure maxima 0.158, 0.050, 0.0158
import numpy as np
from scipy.stats import binom
ok=True
for p,v,s in [(0.5,25,5),(0.1,9,3)]:
    var=binom(100,p).var(); print(f"p={p}: var={var}, sd={np.sqrt(var)}"); ok&=abs(var-v)<1e-9 and abs(np.sqrt(var)-s)<1e-9
for p in [0,1]: ok&=binom(100,p).var()==0
ps=np.linspace(0,1,1001); vv=ps*(1-ps); ok&=ps[np.argmax(vv)]==0.5
for N,want in [(10,0.158),(100,0.050),(1000,0.0158)]:
    m=np.sqrt(0.25/N); print(f"N={N} max sd of fraction {m:.4f} (text {want})"); ok&=abs(m-want)<6e-4*max(1,want/0.05)
# inhomogeneous p_i with same mean: Poisson-binomial variance sum p_i(1-p_i) <= N pbar(1-pbar)
rng=np.random.default_rng(0)
worst=-1
for _ in range(2000):
    pbar=rng.uniform(0.05,0.95); pi=np.clip(pbar+rng.normal(0,0.03,100),0,1); pi+=pbar-pi.mean()
    pi=np.clip(pi,0,1); diff=np.sum(pi*(1-pi))-100*pi.mean()*(1-pi.mean()); worst=max(worst,diff)
print("max of [sum p_i(1-p_i) - N pbar(1-pbar)] over trials:",worst, "(<=0 means lowered)"); ok&=worst<=1e-9
# Rabi frequency error bar = sd of mean of M Bernoulli
M=500;p=0.3; print("sd of fraction over M runs:",binom(M,p).std()/M,"vs",np.sqrt(p*(1-p)/M)); ok&=abs(binom(M,p).std()/M-np.sqrt(p*(1-p)/M))<1e-12
print("PASS" if ok else "FAIL")
