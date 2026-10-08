# Claim: fixed-label sieve "fits the first three experiments; the third magnet kills it"
import numpy as np
rng=np.random.default_rng(2); N=100000
z=rng.choice([1,-1],N); x=rng.choice([1,-1],N)    # fixed labels, read off unchanged
print("exp1 distinct outcomes:",sorted(set(z)))           # two spots
upz=z==1; print("exp2 Z then Z: frac up =",np.mean(z[upz]==1))
left=upz&(x==-1); print("exp3 Z then X: frac left =",round(np.mean(x[upz]==-1),3))
print("exp4 sieve prediction Z,X,Z: frac up =",np.mean(z[left]==1)," (observed 0.5)")
ok = set(z)=={1,-1} and np.mean(z[upz]==1)==1 and abs(np.mean(x[upz]==-1)-.5)<.01 and np.mean(z[left]==1)==1
print("PASS" if ok else "FAIL")
