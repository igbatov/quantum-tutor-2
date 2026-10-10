# Claim: "only the 2-norm is kept fixed by continuous lossless change" (Banach-Lamperti), tested for real rotations
# in 2D: q-norm of R(t)v constant in t for all v only at q=2
import numpy as np
ok=True; t=np.linspace(0,2*np.pi,2001)
for q in [1,1.5,2,3,4]:
    n=(np.abs(np.cos(t))**q+np.abs(np.sin(t))**q)**(1/q); spread=n.max()-n.min(); print(q,spread)
    ok&= (spread<1e-12) if q==2 else (spread>1e-3)
print("PASS" if ok else "FAIL")
