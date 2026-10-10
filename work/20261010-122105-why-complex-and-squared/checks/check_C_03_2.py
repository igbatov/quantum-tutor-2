# Claim: "|s1 - is2|^2 = ... + i s1 s̄2 - i s̄1 s2", "|s1 + is2|^2 = ... - i s1 s̄2 + i s̄1 s2"; cross terms cancel, total 1
# also <R|s> = (s1 - i s2)/√2, <L|s> = (s1 + i s2)/√2
import sympy as sp
x1,y1,x2,y2=sp.symbols('x1 y1 x2 y2',real=True); I=sp.I
s1=x1+I*y1; s2=x2+I*y2; c=sp.conjugate
first=sp.expand((s1-I*s2)*c(s1-I*s2)); second=sp.expand((s1+I*s2)*c(s1+I*s2))
t1=sp.expand(s1*c(s1)+s2*c(s2)+I*s1*c(s2)-I*c(s1)*s2)
t2=sp.expand(s1*c(s1)+s2*c(s2)-I*s1*c(s2)+I*c(s1)*s2)
ok1=sp.simplify(first-t1)==0 and sp.simplify(second-t2)==0
ok2=sp.simplify((first+second)/2-(s1*c(s1)+s2*c(s2)))==0
R=sp.Matrix([1,I])/sp.sqrt(2); L=sp.Matrix([1,-I])/sp.sqrt(2); s=sp.Matrix([s1,s2])
ok3=sp.simplify((R.H*s)[0]-(s1-I*s2)/sp.sqrt(2))==0 and sp.simplify((L.H*s)[0]-(s1+I*s2)/sp.sqrt(2))==0
print("expansions as written:",ok1," half-sum = |s1|^2+|s2|^2:",ok2," <R|s>,<L|s> as written:",ok3)
print("PASS" if ok1 and ok2 and ok3 else "FAIL")
