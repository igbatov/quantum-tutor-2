# Claim: "|a+b+c|^2 = ... nine terms, each involving one slit or two"; pairs - singles = P_ABC; "I3 = 0 ... for any three hands"
import sympy as sp
a,b,c=sp.symbols('a b c'); A,B,C=sp.symbols('abar bbar cbar')
sq=lambda *z: sp.expand(sum(z[i] for i in range(0,len(z),2))*sum(z[i] for i in range(1,len(z),2)))
PABC=sp.expand((a+b+c)*(A+B+C)); terms=PABC.as_ordered_terms()
print("number of terms:",len(terms), " max distinct slits per term:", max(len({str(s).replace('bar','') for s in t.free_symbols}) for t in terms))
PAB=sp.expand((a+b)*(A+B));PAC=sp.expand((a+c)*(A+C));PBC=sp.expand((b+c)*(B+C))
PA,PB,PC=a*A,b*B,c*C
I3=sp.expand(PABC-PAB-PAC-PBC+PA+PB+PC)
print("pairs - singles - P_ABC =", sp.expand(PAB+PAC+PBC-PA-PB-PC-PABC), " I3 =", I3)
# 2Re identity
x1,y1,x2,y2=sp.symbols('x1 y1 x2 y2',real=True); z1=x1+sp.I*y1; z2=x2+sp.I*y2
idok=sp.simplify(z1*sp.conjugate(z2)+sp.conjugate(z1*sp.conjugate(z2))-2*sp.re(z1*sp.conjugate(z2)))==0
print("w + conj(w) = 2Re(w):", idok)
# also: for p=2, I4 = 0 (interference is a sum over pairs for any number of alternatives)
d,Dd=sp.symbols('d dbar'); hs=[(a,A),(b,B),(c,C),(d,Dd)]
from itertools import combinations
def P(sub): return sp.expand(sum(h for h,_ in sub)*sum(hb for _,hb in sub)) if sub else 0
I4=sum((-1)**(4-k)*P(list(S)) for k in range(0,5) for S in combinations(hs,k))
print("I4 for p=2:", sp.expand(I4))
print("PASS" if len(terms)==9 and I3==0 and idok and sp.expand(I4)==0 else "FAIL")
