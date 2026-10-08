# Claims: "all come out up"; "half left, half right"; third Z "half up, half down";
# figure counts 1000->500->500/0, 250/250, 125/125; Check-yourself X-left into X -> fraction left
import sympy as sp
up=sp.Matrix([1,0]); dn=sp.Matrix([0,1])
r=sp.Matrix([1,1])/sp.sqrt(2); l=sp.Matrix([1,-1])/sp.sqrt(2)   # X eigenstates (labels arbitrary)
P=lambda a,b: sp.simplify(abs((a.H*b)[0])**2)
res={}
res['Z then Z up']=P(up,up); res['Z then Z down']=P(dn,up)
res['Zup->X left']=P(l,up); res['Zup->X right']=P(r,up)
res['Xleft->Z up']=P(up,l); res['Xleft->Z down']=P(dn,l)
res['Xleft->X left (check-yourself)']=P(l,l)
for k,v in res.items(): print(k,v)
ok = res['Z then Z up']==1 and res['Z then Z down']==0 and res['Zup->X left']==sp.Rational(1,2) \
     and res['Xleft->Z up']==sp.Rational(1,2) and res['Xleft->X left (check-yourself)']==1
N=1000; n1=N*sp.Rational(1,2); n2=n1*res['Zup->X left']; n3=n2*res['Xleft->Z up']
print("counts:",N,n1,n1*res['Z then Z up'],n2,n3); ok &= (n1,n2,n3)==(500,250,125)
print("PASS" if ok else "FAIL")
