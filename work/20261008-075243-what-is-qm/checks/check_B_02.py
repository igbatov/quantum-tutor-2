# Claim: "the push would take every value between the two extremes, giving one continuous band"
# Also figure: classical panel uses deflection uniform on [-1,1].
import numpy as np, sympy as sp
ok=True
# isotropic orientation: pdf of u=cos(theta) is (1/2)sin th dth / |du| = 1/2 uniform
th=sp.symbols('theta'); u=sp.symbols('u')
pdf=sp.simplify((sp.sin(th)/2)/sp.sin(th)); print("pdf of cos(theta) for isotropic directions:",pdf)
ok &= pdf==sp.Rational(1,2)
rng=np.random.default_rng(0); v=rng.normal(size=(200000,3)); v/=np.linalg.norm(v,axis=1)[:,None]
h,_=np.histogram(v[:,2],bins=20,range=(-1,1),density=True)
print("histogram min/max density:",h.min().round(3),h.max().round(3))
ok &= h.min()>0.45 and h.max()<0.55   # continuous, flat, nonzero at centre
# quantum: only +-1 -> centre bin empty
print("quantum deflections: {-1,+1} only; centre (|d|<0.5) fraction = 0")
print("PASS" if ok else "FAIL")
