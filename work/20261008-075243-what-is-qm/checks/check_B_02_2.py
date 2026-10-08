# Claims: "pushes would take every value between the two extremes ... one continuous band" (text);
# caption: "fill one continuous band evenly"; "an empty gap exactly where the classical band is as full as anywhere"
import numpy as np, sympy as sp
ok=True
th=sp.symbols('theta')
pdf=sp.simplify((sp.sin(th)/2)/sp.sin(th)); print("pdf of cos(theta) for isotropic directions:",pdf)
ok &= pdf==sp.Rational(1,2)
rng=np.random.default_rng(0); v=rng.normal(size=(400000,3)); v/=np.linalg.norm(v,axis=1)[:,None]
h,_=np.histogram(v[:,2],bins=20,range=(-1,1),density=True)
centre=h[9:11].mean()
print(f"classical density: min {h.min():.3f} max {h.max():.3f}, centre {centre:.3f}")
ok &= h.min()>0.47 and h.max()<0.53 and abs(centre-0.5)<0.03
# idealized quantum panel as drawn: gaussians sd 0.08 at +-1; density at 0 relative to peak
s=0.08; rel=np.exp(-1/(2*s**2))
print(f"idealized quantum density at centre / peak = {rel:.1e} (empty gap)")
ok &= rel<1e-30
print("PASS" if ok else "FAIL")
