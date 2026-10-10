# Claims: "The plain size passes at a few special spots and fails elsewhere": passes where hands line up and at
# (1,w,w^2): "P_ABC = 0, each pair sum has length 1, I3 = 0 - 3 + 3 = 0"; "never negative (Hlawka)";
# "cube and fourth power fail even at the centre"; p=4 products "in which all three hands appear";
# Sorkin "degree p has interference up to order p"; "N single terms plus N(N-1)/2 pair terms"
import numpy as np, sympy as sp
from itertools import combinations
def In(h,p):
    n=len(h); return sum((-1)**(n-k)*abs(sum(S))**p for k in range(1,n+1) for S in combinations(h,k))
w=np.exp(2j*np.pi/3); h=(1,w,w**2)
pairs=[abs(1+w),abs(1+w**2),abs(w+w**2)]
print("(1,w,w^2): P_ABC",abs(sum(h)),"pair lengths",np.round(pairs,12),"I3(p=1)",In(h,1))
ok=abs(sum(h))<1e-12 and np.allclose(pairs,1) and abs(In(h,1))<1e-12
ok&=abs(In((1,2,.5),1))<1e-12 and abs(In((1+1j,2+2j,.3+.3j),1))<1e-12   # aligned
# screen geometry: hands env*(e^{-i phi},1,e^{i phi}), phi=2 pi x; zeros of p=1 I3 over a wide range
x=np.linspace(-12,12,2400001); phi=2*np.pi*x
g=3+np.abs(1+2*np.cos(phi))-4*np.abs(np.cos(phi/2))-2*np.abs(np.cos(phi))   # I3/|env| for p=1
env=np.abs(np.sinc(x/4)); I1=env*g
print("p=1 min over |x|<=12:",I1.min())
fr=np.mod(x,1); special=(np.minimum(fr,1-fr)<2e-3)|(np.abs(fr-1/3)<2e-3)|(np.abs(fr-2/3)<2e-3)
# local minima of g (one period) and where they sit
from scipy.signal import argrelmin
y=np.linspace(0,1,1000001); gy=3+np.abs(1+2*np.cos(2*np.pi*y))-4*np.abs(np.cos(np.pi*y))-2*np.abs(np.cos(2*np.pi*y))
im=argrelmin(np.concatenate([[gy[-2]],gy]))[0]-1; lm=sorted(set(np.round(np.mod(y[im],1),4)))
print("local minima of p=1 I3/env in one period at x mod 1 =",lm,"values",np.round(gy[im],12))
fr=np.mod(x,1); far=(np.minimum(fr,1-fr)>0.02)&(np.abs(fr-1/3)>0.02)&(np.abs(fr-2/3)>0.02)
print("min of I3/env at least 0.02 from integers and thirds:",g[far].min())
ok&=I1.min()>-1e-12 and g[far].min()>1e-3 and np.allclose(gy[im],0,atol=1e-4) and all(min(abs(v-t) for t in (0,1/3,2/3,1))<1e-3 for v in lm)
rng=np.random.default_rng(0)
mn=min(In(tuple(rng.normal(size=3)+1j*rng.normal(size=3)),1) for _ in range(100000)); print("Hlawka min over random hands:",mn); ok&=mn>-1e-12
print("centre p=3,4:",In((1,1,1),3),In((1,1,1),4)); ok&=In((1,1,1),3)==6 and In((1,1,1),4)==36
a,b,c,A,B,C=sp.symbols('a b c A B C')
P=lambda z,Z: sp.expand((sum(z)*sum(Z))**2)
I3p4=sp.expand(P([a,b,c],[A,B,C])-P([a,b],[A,B])-P([a,c],[A,C])-P([b,c],[B,C])+P([a],[A])+P([b],[B])+P([c],[C]))
ok&=I3p4.coeff(a*A*b*C)!=0 and I3p4.coeff(a*B*a*C)!=0; print("p=4 I3 contains a A b C and a^2 B C terms")
h5=tuple(rng.normal(size=5)+1j*rng.normal(size=5))
print("p=4: I4",In(h5[:4],4)," I5",In(h5,4)); ok&=abs(In(h5[:4],4))>1e-6 and abs(In(h5,4))<1e-8
for N in (3,4,5):
    z=sp.symbols(f'z0:{N}'); Z=sp.symbols(f'Z0:{N}')
    terms=sp.expand(sum(z)*sum(Z)).as_ordered_terms(); diag=sum(1 for t in terms if any(t==z[i]*Z[i] for i in range(N)))
    print(N,"alternatives:",diag,"single terms,",(len(terms)-diag)//2,"conjugate-pair terms; N(N-1)/2 =",N*(N-1)//2)
    ok&=diag==N and (len(terms)-diag)//2==N*(N-1)//2
print("PASS" if ok else "FAIL")
