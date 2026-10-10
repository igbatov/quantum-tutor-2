# Claim: the table of I3 for p=1..4 at hands (1,1,-1), (1,1,1), (1,i,-1)
import numpy as np
def I3(h,p):
    a,b,c=h; f=lambda z: abs(z)**p
    return f(a+b+c)-f(a+b)-f(a+c)-f(b+c)+f(a)+f(b)+f(c)
cols=[(1,1,-1),(1,1,1),(1,1j,-1)]
text={1:[2,0,4-2*np.sqrt(2)],2:[0,0,0],3:[-4,6,4-2*2**1.5],4:[-12,36,-4]}
ok=True
for p in range(1,5):
    got=[I3(h,p) for h in cols]; print(p,np.round(got,4),"text",np.round(text[p],4))
    ok&=np.allclose(got,text[p],atol=1e-12)
print("approximations: 4-2sqrt2 =",4-2*np.sqrt(2)," 4-2*2^1.5 =",4-2*2**1.5)
ok&=abs(round(4-2*np.sqrt(2),2)-1.17)<1e-9 and abs(round(4-2*2**1.5,2)+1.66)<1e-9
# row entries P_ABC and pair sums
for p in (1,3):
    h=(1,1j,-1); print("p",p,"P_ABC",abs(sum(h))**p,"pairs",abs(1+1j)**p+abs(0)**p+abs(1j-1)**p)
print("PASS" if ok else "FAIL")
