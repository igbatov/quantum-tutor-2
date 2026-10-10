# Claim: "overlap 0.99985 (... cos 1° = 0.9998477) ... after 10^5 copies ... e^{-15.2} ≈ 2.4e-7"
# and "lists for p = 0.8 and p = 0.8001 are perpendicular" (overlap per copy < 1 -> overlap^N -> 0)
import numpy as np
ok=True
c=np.cos(np.radians(1)); print("cos1deg",c); ok&=abs(c-0.9998477)<1e-7
ln=1e5*np.log(c); val=np.exp(ln); print("exponent",ln,"overlap^1e5",val); ok&=abs(ln+15.2)<0.05 and abs(val-2.4e-7)/2.4e-7<0.05
print("with rounded 0.99985 instead:",0.99985**1e5)
ov=np.sqrt(0.8*0.8001)+np.sqrt(0.2*0.1999); print("per-copy overlap p=0.8 vs 0.8001:",ov,"1-ov",1-ov)
ok&= ov<1
for N in [1e3,1e6,1e9,1e12]: print(" N",N,"overlap^N",ov**N)
print("PASS" if ok else "FAIL")
