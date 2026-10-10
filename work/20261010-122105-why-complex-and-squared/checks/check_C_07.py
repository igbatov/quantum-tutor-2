# Claims: "The plain size passes where all hands line up ... and fails elsewhere";
# "cube and fourth power fail even at the centre"; p=4 expansion has three-hand products;
# Sorkin: "a rule of degree p has interference up to order p" (test p=4: I4!=0, I5=0); p=1 never negative (fig)
import numpy as np, sympy as sp
from itertools import combinations
def In(h,p):
    n=len(h); tot=0
    for k in range(0,n+1):
        for S in combinations(h,k):
            tot+=(-1)**(n-k)*abs(sum(S))**p if S else 0
    return tot
w=np.exp(2j*np.pi/3)
print("p=1 at aligned (1,2,0.5):", In((1,2,.5),1))
print("p=1 at (1, w, w^2) (not aligned, sum 0):", In((1,w,w**2),1))
print("p=1 at three-slit dark spot hands (e^{-2pi i/3},1,e^{2pi i/3}):", In((np.exp(-2j*np.pi/3),1,np.exp(2j*np.pi/3)),1))
rng=np.random.default_rng(0)
mins=min(In(tuple(rng.normal(size=3)+1j*rng.normal(size=3)),1) for _ in range(200000))
print("min of p=1 I3 over 2e5 random hands (Hlawka => >=0):", mins)
print("p=3,4 at centre (1,1,1):", In((1,1,1),3), In((1,1,1),4))
# p=4 symbolic: does I3 contain all-three-hand products?
a,b,c,A,B,C=sp.symbols('a b c A B C')
P=lambda zs,Zs: sp.expand((sum(zs)*sum(Zs))**2)
I3p4=sp.expand(P([a,b,c],[A,B,C])-P([a,b],[A,B])-P([a,c],[A,C])-P([b,c],[B,C])+P([a],[A])+P([b],[B])+P([c],[C]))
print("p=4 I3 has terms:",len(I3p4.as_ordered_terms()),"; contains a*A*b*C:", (I3p4.coeff(a*A*b*C)!=0))
# Sorkin hierarchy for p=4
h5=tuple(rng.normal(size=5)+1j*rng.normal(size=5)); h4=h5[:4]
print("p=4: I4 =",In(h4,4)," I5 =",In(h5,4))
print("p=2: I3 =",In(h5[:3],2))
plain_fails_elsewhere = abs(In((1,w,w**2),1))>1e-9
print("Claim 'plain size fails elsewhere (only passes when aligned)':", "true" if plain_fails_elsewhere else "FALSE: also zero at (1,w,w^2)")
ok_rest = mins>-1e-9 and In((1,1,1),3)!=0 and In((1,1,1),4)!=0 and abs(In(h4,4))>1e-6 and abs(In(h5,4))<1e-8
print("other claims (p=3,4 at centre, p=4 triple terms, Sorkin p=4, p=1 >=0):", "PASS" if ok_rest else "FAIL")
print("PASS" if plain_fails_elsewhere and ok_rest else "FAIL")
