# Claim: "after 100 photons ... about 4 percentage points around 25%, after 10 000 by about 0.4"
# and scatter table sqrt(0.25*0.75/N) = 0.433, 0.217, 0.043, 0.0043, 0.00043; cos^2 30 = 0.75, sin^2 30 = 0.25
# also "scatters ... by an amount that shrinks as 1/sqrt N" (Monte Carlo of binomial model)
import numpy as np, sympy as sp
ok=True
th=sp.pi/6
ok &= sp.simplify(sp.cos(th)**2-sp.Rational(3,4))==0 and sp.simplify(sp.sin(th)**2-sp.Rational(1,4))==0
table={1:0.433,4:0.217,100:0.043,10000:0.0043,1000000:0.00043}
for N,v in table.items():
    s=np.sqrt(0.25*0.75/N); print(N, s, v); ok &= abs(s-v)/v<0.01
rng=np.random.default_rng(1)
for N in [100,10000]:
    f=rng.binomial(N,0.25,size=20000)/N; print("MC N",N,"sd",f.std(),"mean",f.mean())
    ok &= abs(f.std()-np.sqrt(0.1875/N))/np.sqrt(0.1875/N)<0.03
print("PASS" if ok else "FAIL")
