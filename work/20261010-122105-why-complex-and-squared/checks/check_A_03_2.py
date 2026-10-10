# Claim: "arm 1 passing a fraction t ... exit 1 runs between (1+√t)²/4 and (1−√t)²/4 and the two exits sum to (1+t)/2"
# also "98% visibility, which leaves a floor of about 1% of the peak"; "a loss in one arm alone also stops the minimum reaching zero"
import sympy as sp, numpy as np
t,phi=sp.symbols('t phi',positive=True)
z=sp.exp(sp.I*phi)
H=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
L=sp.diag(sp.sqrt(t)*z,1)          # lossy plate: amplitude factor sqrt(t), photon removed with chance 1-t
out=H*L*H*sp.Matrix([1,0])
P1=sp.simplify(sp.expand(out[0]*sp.conjugate(out[0]))); P2=sp.simplify(sp.expand(out[1]*sp.conjugate(out[1])))
P1=sp.simplify(P1.rewrite(sp.cos)); P2=sp.simplify(P2.rewrite(sp.cos))
print('P1 =',P1,' P2 =',P2)
ok1=sp.simplify(P1-(1+t+2*sp.sqrt(t)*sp.cos(phi))/4)==0
ok2=sp.simplify(P1.subs(phi,0)-(1+sp.sqrt(t))**2/4)==0 and sp.simplify(P1.subs(phi,sp.pi)-(1-sp.sqrt(t))**2/4)==0
ok3=sp.simplify(P1+P2-(1+t)/2)==0
# min > 0 for every t<1
mins=[float(((1-np.sqrt(tv))**2)/4) for tv in (0.5,0.9,0.99)]
ok4=all(m>0 for m in mins)
V=0.98; floor=(1-V)/(1+V)
print('max/min/sum ok',ok1,ok2,ok3,'| minima for t=0.5,0.9,0.99:',[f'{m:.2e}' for m in mins],'| V=0.98 floor/peak =',round(floor,4))
ok5=abs(floor-0.01)<0.0015
print('PASS' if all([ok1,ok2,ok3,ok4,ok5]) else 'FAIL')
