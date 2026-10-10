# Claims: "for such p, |a+b|^p < |a|^p + |b|^p whenever a and b are both nonzero" (0<p<1),
# "an output that draws on two inputs always loses p-total"; p=1 with non-negative amplitudes allows gradual mixing but nothing cancels.
import numpy as np
rng=np.random.default_rng(1); ok=True
for p in (0.2,0.5,0.9):
    a=rng.normal(size=10**5)+1j*rng.normal(size=10**5); b=rng.normal(size=10**5)+1j*rng.normal(size=10**5)
    if not np.all(np.abs(a+b)**p < np.abs(a)**p+np.abs(b)**p): ok=False
    # any 2x2 complex matrix whose columns have p-total 1 and which mixes: some vector loses p-total
    worst=0
    for _ in range(2000):
        M=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        M=M/ (np.sum(np.abs(M)**p,axis=0)**(1/p))
        x=np.array([1,0.3*np.exp(1j*rng.uniform(0,6.3))]); xin=np.sum(np.abs(x)**p); xout=np.sum(np.abs(M@x)**p)
        if xout>=xin-1e-12: ok=False
        worst=max(worst,xout-xin)
    print(f'p={p}: strict subadditivity holds; mixing maps always lose p-total (max out-in = {worst:.3f})')
# p=1 stochastic matrix: gradual mixer on non-negative vectors, keeps 1-total, but no cancelling
S=lambda e: np.array([[1-e,e],[e,1-e]])
for e in (0.1,0.3,0.5):
    v=S(e)@np.array([1.,0]); print(f'p=1 stochastic eps={e}: out {v}, total {v.sum()}')
    if abs(v.sum()-1)>1e-15: ok=False
# two arms each giving 1/4 to exit 1 -> 1/2, never 0
print('p=1 nonneg: exit 1 from two routes of 1/4 each =',0.25+0.25)
print('PASS' if ok else 'FAIL')
