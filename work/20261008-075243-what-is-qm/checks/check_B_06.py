# Claim: "points scattered evenly over the globe: half up, half down" (and 50/50 along any axis)
import numpy as np
rng=np.random.default_rng(1); n=400000
v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]
rho=0.5*(np.eye(2)+np.mean(v,0)[0]*np.array([[0,1],[1,0]])+np.mean(v,0)[1]*np.array([[0,-1j],[1j,0]])+np.mean(v,0)[2]*np.diag([1,-1]))
print("average density matrix:\n",np.round(rho,3))
pup=np.mean((1+v[:,2])/2); px=np.mean((1+v[:,0])/2)
print(f"P(up)={pup:.4f}  P(X-right)={px:.4f}")
ok=abs(pup-.5)<3e-3 and abs(px-.5)<3e-3 and np.allclose(rho,np.eye(2)/2,atol=3e-3)
print("PASS" if ok else "FAIL")
