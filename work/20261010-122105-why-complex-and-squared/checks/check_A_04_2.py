# Claim (check-yourself): plates turning arm 1 by 90° and arm 2 by 30°, H, input (1,0): exit-1 fraction (expected answer 0.75)
# Also: "the i convention shifts it by π" and "Any lossless choice gives the same counts"
import numpy as np, sympy as sp
H=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
D=sp.diag(sp.exp(sp.I*sp.pi/2),sp.exp(sp.I*sp.pi/6))
out=H*D*H*sp.Matrix([1,0])
P1=sp.nsimplify(sp.simplify(sp.expand(out[0]*sp.conjugate(out[0])))); P2=sp.nsimplify(sp.simplify(sp.expand(out[1]*sp.conjugate(out[1]))))
print('P1 =',P1,' P2 =',P2,' (only the 60° difference matters: cos^2(30°) =',sp.nsimplify(sp.cos(sp.pi/6)**2),')')
B=sp.Matrix([[1,sp.I],[sp.I,1]])/sp.sqrt(2)
phi=sp.symbols('phi',real=True)
o=B*sp.diag(sp.exp(sp.I*phi),1)*B*sp.Matrix([1,0])
Pb=sp.simplify((o[0]*sp.conjugate(o[0])).rewrite(sp.cos))
print('i-convention exit-1 fraction:',Pb,'; equals cos^2((phi+pi)/2):',sp.simplify(Pb-sp.cos((phi+sp.pi)/2)**2)==0)
ok = P1==sp.Rational(3,4) and P2==sp.Rational(1,4) and sp.simplify(Pb-sp.cos((phi+sp.pi)/2)**2)==0
print('PASS' if ok else 'FAIL')
