# Figure-caption claims (c-buildup-fraction / c-rules-out): running fraction "settles inside the narrowing band"
# 0.8 +/- sqrt(0.16/N) (a ONE-standard-deviation band). Test: how often is the running fraction outside it?
import numpy as np
outs=[];late=[]
for seed in range(200):
    rng=np.random.default_rng(seed); x=rng.random(70000)<0.8; N=np.arange(1,70001); f=np.cumsum(x)/N
    o=np.abs(f-0.8)>np.sqrt(0.16/N); outs.append(o[1000:].mean()); late.append(o[-1])
print("mean fraction of N in [1000,70000] where running fraction is outside the 1-SD band:",np.mean(outs))
print("fraction of sequences outside the band at N=70000:",np.mean(late))
print("fraction of sequences that are inside for every N>=1000:",np.mean(np.array(outs)==0))
print("FAIL" if np.mean(outs)>0.1 else "PASS")
