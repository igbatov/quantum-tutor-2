# Claim: "Psi_2 = (0.9, 0.3, 0.3, 0.1)" and the lambda table for N=2, p=0.1 (0.055, 0.045, 0.205, 0.855)
import numpy as np
ok=True
c0,c1=np.sqrt(0.9),np.sqrt(0.1)
print("c0,c1 =",round(c0,4),round(c1,4)); ok &= round(c0,4)==0.9487 and round(c1,4)==0.3162
psi=np.array([c0*c0,c0*c1,c1*c0,c1*c1]); print("Psi2 =",psi.round(6)); ok &= np.allclose(psi,[0.9,0.3,0.3,0.1])
print("squared entries",(psi**2).round(4),"total",(psi**2).sum())
P1=np.diag([0,0,1,1]); P2=np.diag([0,1,0,1]); F2=(P1+P2)/2
ok &= np.allclose(np.diag(F2),[0,.5,.5,1])
table={0:([0,.15,.15,.10],0.055),0.1:([-.09,.12,.12,.09],0.045),0.5:([-.45,0,0,.05],0.205),1:([-.90,-.15,-.15,0],0.855)}
for lam,(ent,sq) in table.items():
    R=(F2-lam*np.eye(4))@psi; f=(lam-0.1)**2+0.045
    print(f"lam={lam}: R={R.round(4)}, |R|^2={R@R:.4f}, formula={f:.4f}, text {sq}")
    ok &= np.allclose(R,ent,atol=1e-12) and abs(R@R-sq)<1e-12 and abs(f-sq)<1e-12
# sqrt spreads
for p,want in [(0.5,0.05),(0.1,0.03)]:
    v=np.sqrt(p*(1-p)/100); print(f"sqrt(p(1-p)/100) p={p}: {v:.4f} (text {want})"); ok&=abs(v-want)<1e-12
print("PASS" if ok else "FAIL")
