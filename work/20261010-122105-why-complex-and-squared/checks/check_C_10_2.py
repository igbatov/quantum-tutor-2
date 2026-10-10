# Claim: H photon at a splitter turned 30°: "f(cos 30°) ... 0.75 + 0.094 ε"; "agrees with the square at shadows 0, 1/√2 and 1"
# and the two-exit total is 1 (so totals and 100/50/50 table don't fix the rule; only intermediate angles see it)
import sympy as sp
x,e=sp.symbols('x epsilon',real=True); f=x**2+e*x**2*(1-x**2)*(2*x**2-1)
v=sp.simplify(f.subs(x,sp.cos(sp.pi/6))); print("f(cos30) =",v, "coefficient", float(sp.diff(v,e)))
ok=sp.simplify(v-(sp.Rational(3,4)+e*sp.Rational(3,4)*sp.Rational(1,4)*sp.Rational(1,2)))==0 and abs(float(sp.diff(v,e))-0.094)<0.0005
roots=sp.solveset(sp.Eq(f-x**2,0),x,sp.Interval(0,1)); print("f = x^2 on [0,1] exactly at", roots)
ok&=roots==sp.FiniteSet(0,1/sp.sqrt(2),1)
print("PASS" if ok else "FAIL")
