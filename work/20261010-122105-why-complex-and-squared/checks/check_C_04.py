# Claims (Picture/fig c-three-fifty-fifty): real arrows = great circle H,D,V,A; H/V even-bet set = great circle D,A,R,L;
# D/A even-bet set = great circle H,V,R,L; the two cross only at R and L, off the real circle.
# Check-yourself support: no pure state is 50/50 at all three sorters.
import numpy as np
X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
def stokes(s):
    s=s/np.linalg.norm(s); return np.real([s.conj()@Z@s, s.conj()@X@s, s.conj()@Y@s])  # S1:H/V, S2:D/A, S3:R/L
r=1/np.sqrt(2)
named={"H":[1,0],"V":[0,1],"D":[r,r],"A":[r,-r],"R":[r,1j*r],"L":[r,-1j*r]}
for k,v in named.items(): print(k, np.round(stokes(np.array(v,complex)),12))
P=lambda e,s: abs(np.vdot(e,s))**2
rng=np.random.default_rng(1); ok=True
for _ in range(20000):
    s=rng.normal(size=2)+1j*rng.normal(size=2); s/=np.linalg.norm(s); S=stokes(s)
    pH=P(np.array([1,0]),s); pD=P(np.array([r,r]),s); pR=P(np.array([r,1j*r]),s)
    ok &= np.isclose(pH,(1+S[0])/2) and np.isclose(pD,(1+S[1])/2) and np.isclose(pR,(1+S[2])/2)
print("P(exit)=(1+S_k)/2 for random states:",ok)
th=np.linspace(0,np.pi,1001); real=[stokes(np.array([np.cos(t),np.sin(t)],complex)) for t in th]
okreal=np.allclose(np.array(real)[:,2],0); print("real arrows have S3=0 (circle H,D,V,A):",okreal)
# even at H/V -> S1=0, even at D/A -> S2=0 ; both -> S3=±1 -> R or L
ok_int = True  # S1=S2=0 and |S|=1 => S=(0,0,±1)
print("intersection S1=S2=0 on unit sphere -> (0,0,±1) = R, L, which have S3=±1≠0 (off real circle)")
# no pure state with S1=S2=S3=0
norms=[np.linalg.norm(stokes(rng.normal(size=2)+1j*rng.normal(size=2))) for _ in range(5000)]
print("min |S| over random pure states:", min(norms))
print("PASS" if ok and okreal and np.isclose(min(norms),1) else "FAIL")
