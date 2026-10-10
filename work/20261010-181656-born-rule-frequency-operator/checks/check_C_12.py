# Figure-caption claim (c-born-spread): "the right-hand curves are 1 minus the exact deviant weights of the
# previous figure" -- right panel uses eps = 0.05 and 0.01; previous figure (c-parabola-floor) uses eps = 0.1 and 0.05.
# Also check monotonicity of 'chance within eps' in N (lumpy at small N).
import numpy as np
from scipy.stats import binom
prev={0.1,0.05}; here={0.05,0.01}
print("eps in previous figure",prev,"eps here",here,"shared",prev&here)
def within(N,eps):
    m=np.arange(N+1); return binom.pmf(m[np.abs(m/N-0.8)<=eps+1e-12],N,0.8).sum()
def dev(N,eps):
    m=np.arange(N+1); return binom.pmf(m[np.abs(m/N-0.8)>eps+1e-12],N,0.8).sum()
ok_eps05=all(abs(within(N,0.05)+dev(N,0.05)-1)<1e-12 for N in [10,100,1000,10000])
print("eps=0.05: within + deviant = 1:",ok_eps05)
print("eps=0.01, N=10..15 chance within:",[round(within(N,0.01),4) for N in range(10,16)])
print("PASS" if here<=prev else "FAIL")
