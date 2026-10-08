# Claim: "answers that update the state and erase the answers to incompatible questions"
import numpy as np
up=np.array([1.,0.]); dn=np.array([0.,1.]); r=np.array([1,1])/np.sqrt(2); l=np.array([1,-1])/np.sqrt(2)
proj=lambda v: np.outer(v,v.conj())
Z=np.diag([1,-1]); X=np.array([[0,1],[1,0]])
ok=True
c_ZZ=np.linalg.norm(Z@Z-Z@Z); c_ZX=np.linalg.norm(Z@X-X@Z)
print("||[Z,Z]|| =",c_ZZ,"  ||[Z,X]|| =",round(c_ZX,3))
# compatible: Z-up, ask Z again -> state unchanged, answer kept
s=proj(up)@up; s/=np.linalg.norm(s); print("after Z,Z: P(up) =",abs(up@s)**2)
ok &= abs(abs(up@s)**2-1)<1e-12 and c_ZZ==0
# incompatible: Z-up, ask X -> left; P(up) drops to 1/2
s=proj(l)@up; s/=np.linalg.norm(s); p=abs(up@s)**2; print("after Z,X(left): P(up) =",round(p,6))
ok &= abs(p-0.5)<1e-12 and c_ZX>0
print("PASS" if ok else "FAIL")
