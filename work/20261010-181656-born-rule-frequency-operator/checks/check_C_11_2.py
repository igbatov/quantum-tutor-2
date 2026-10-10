# Caption c-buildup-fraction: "outside the one-standard-deviation band about a third of the time on average
# (this run more often than that beyond N = 1000) and almost always stays inside twice it".
# Caption c-rules-out: "(ii) and (iii) ... each stepping outside the 1-s.d. band for stretches of a few hundred arrivals"
import numpy as np
from scipy.stats import binom
N=np.arange(1,70001); sd=np.sqrt(0.16/N)
outs=[];outs2=[]
for seed in range(400):
    f=np.cumsum(np.random.default_rng(seed).random(70000)<0.8)/N
    outs.append((np.abs(f-0.8)>sd).mean()); outs2.append((np.abs(f-0.8)>2*sd).mean())
# exact: P(|m/N - p| > sd) per N
Nx=np.array([100,1000,10000,70000]); pex=[1-binom.cdf(np.floor(0.8*n+0.4*np.sqrt(n)),n,0.8)+binom.cdf(np.ceil(0.8*n-0.4*np.sqrt(n))-1,n,0.8) for n in Nx]
print("exact P(outside 1 sd) at N=",Nx,np.round(pex,3))
print("mean time-fraction outside 1 sd (all N):",np.mean(outs),"; outside 2 sd:",np.mean(outs2))
# drawn run: replicate figure rng consumption
rng=np.random.default_rng(1989)
for n in [10,100,3000,20000]: rng.random(n); rng.random(n)
f=np.cumsum(rng.random(70000)<0.8)/N
r1=(np.abs(f-0.8)>sd)[999:].mean(); r2=(np.abs(f-0.8)>2*sd)[999:].mean()
print("drawn run, N>=1000: outside 1 sd",r1,"outside 2 sd",r2)
ok= 0.25<np.mean(outs)<0.40 and r1>np.mean(outs) and r2<0.05 and np.mean(outs2)<0.08
# rules-out runs (seeds 11, 29, N<=10000): longest stretch outside 1 sd
Nr=np.arange(1,10001); sdr=np.sqrt(0.16/Nr)
for seed in [11,29]:
    f=np.cumsum(np.random.default_rng(seed).random(10000)<0.8)/Nr; o=np.abs(f-0.8)>sdr
    runs=[];c=0
    for b in o:
        if b: c+=1
        else:
            if c: runs.append(c)
            c=0
    if c: runs.append(c)
    runs=sorted(runs)[::-1]; print("seed",seed,"fraction outside",o.mean().round(3),"longest stretches",runs[:5])
    ok&= len(runs)>0 and runs[0]>=100
print("PASS" if ok else "FAIL")
