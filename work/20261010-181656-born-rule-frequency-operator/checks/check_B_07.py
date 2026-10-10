# Claim: overlap of product lists "(c0c0' + c1c1')^N"; "differ by 1 deg (p=0.100 vs p=0.111)";
# "cos 1 deg = 0.9998477 ... 0.9998477^100000 = e^-15.23 ~ 2.4e-7"
import itertools, numpy as np
ok=True
a=np.array([np.sqrt(.9),np.sqrt(.1)]); b=np.array([np.sqrt(1-.111),np.sqrt(.111)])
for N in [1,2,3,5]:
    A=np.array([np.prod([a[x] for x in s]) for s in itertools.product([0,1],repeat=N)])
    B=np.array([np.prod([b[x] for x in s]) for s in itertools.product([0,1],repeat=N)])
    ok&=abs(A@B-(a@b)**N)<1e-12
ang=np.degrees(np.arcsin(np.sqrt(.111))-np.arcsin(np.sqrt(.1))); print("angle between p=0.100 and 0.111 arrows:",ang,"deg")
ok&=abs(ang-1)<0.05
c=np.cos(np.radians(1)); print("cos1deg",c); ok&=abs(c-0.9998477)<1e-7
L=1e5*np.log(c); print("exponent",L,"value",np.exp(L)); ok&=abs(L+15.23)<0.01 and abs(np.exp(L)-2.4e-7)<0.05e-7
print("PASS" if ok else "FAIL")
