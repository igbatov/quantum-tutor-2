# Claims: "a qubit is exactly one of these globes"; "two-answer magnetism in the hydrogen nuclei ... MRI"
import numpy as np, sympy as sp
rng=np.random.default_rng(3); ok=True
sig=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
for _ in range(1000):
    v=rng.normal(size=2)+1j*rng.normal(size=2); v/=np.linalg.norm(v)
    r=np.real([v.conj()@s@v for s in sig]); ok&=abs(np.linalg.norm(r)-1)<1e-12
    th=np.arccos(r[2]); ph=np.arctan2(r[1],r[0])
    w=np.array([np.cos(th/2),np.exp(1j*ph)*np.sin(th/2)])
    ok&=abs(abs(np.vdot(w,v))-1)<1e-10        # same state up to global phase
print("every pure qubit state <-> unique point on unit sphere (up to global phase):",ok)
I=sp.Rational(1,2); print("proton spin I=1/2 -> 2I+1 =",2*I+1,"orientations in a field"); ok&= 2*I+1==2
print("PASS" if ok else "FAIL")
