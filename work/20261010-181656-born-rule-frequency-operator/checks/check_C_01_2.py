# Claim: "for N = 2 the list is (0.2, 0.4, 0.4, 0.8) ... squared lengths (0.04, 0.16, 0.16, 0.64)"
# Also: c1 = sqrt(0.8) = 0.894, c0 = sqrt(0.2) = 0.447; N=3 table amplitudes/weights/group weights.
import numpy as np, itertools, math
p=0.8; c1=math.sqrt(p); c0=math.sqrt(1-p); tol=5e-4; ok=True
print("c1,c0",c1,c0); ok&=abs(c1-0.894)<tol and abs(c0-0.447)<tol
L2=[ (c1 if a else c0)*(c1 if b else c0) for a,b in itertools.product([0,1],repeat=2)]
print("N=2 list",np.round(L2,4), "sq",np.round(np.square(L2),4), "sum",sum(np.square(L2)))
ok&=np.allclose(L2,[0.2,0.4,0.4,0.8]) and np.allclose(np.square(L2),[0.04,.16,.16,.64])
amps=[c0**(3-m)*c1**m for m in range(4)]; w=[a*a for a in amps]; gw=[math.comb(3,m)*w[m] for m in range(4)]
print("N=3 amps",np.round(amps,4),"w",np.round(w,4),"group",np.round(gw,4),"total",sum(gw))
ok&=np.allclose(amps,[0.089,0.179,0.358,0.716],atol=6e-4) and np.allclose(w,[.008,.032,.128,.512]) and np.allclose(gw,[.008,.096,.384,.512]) and abs(sum(gw)-1)<1e-12
# Rule 2/3 at N=2
print("S[x1] N=2:",0.16+0.64,"S[x1x2]:",0.64)
# no branch at frequency 0.8 for N=3
ok&= all(abs(m/3-0.8)>1e-9 for m in range(4))
print("PASS" if ok else "FAIL")
