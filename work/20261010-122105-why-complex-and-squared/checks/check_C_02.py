# Claims: "QD = (1,i)/√2 = R", "QR = A", "QL = D", overlaps <H|R>,<D|R>,<A|R>,<R|R>,<L|R>,
# full 3x3 table, "two exits of any sorter total 1 for every state", i*(x+iy) -> (-y,x)
import sympy as sp
r2 = sp.sqrt(2); I = sp.I
H=sp.Matrix([1,0]); V=sp.Matrix([0,1]); Dd=sp.Matrix([1,1])/r2; A=sp.Matrix([1,-1])/r2
R=sp.Matrix([1,I])/r2; L=sp.Matrix([1,-I])/r2
Q=sp.Matrix([[1,0],[0,I]])
ov=lambda e,s: sp.simplify((e.H*s)[0])
ok=True
ok &= sp.simplify(Q*Dd-R)==sp.zeros(2,1); ok &= sp.simplify(Q*R-A)==sp.zeros(2,1); ok &= sp.simplify(Q*L-Dd)==sp.zeros(2,1)
print("QD=R, QR=A, QL=D:", ok)
o = {"HR":ov(H,R),"DR":ov(Dd,R),"AR":ov(A,R),"RR":ov(R,R),"LR":ov(L,R)}
print(o)
ok2 = (sp.simplify(o["HR"]-1/r2)==0 and sp.simplify(o["DR"]-(1+I)/2)==0 and sp.simplify(o["AR"]-(1-I)/2)==0
       and o["RR"]==1 and o["LR"]==0)
print("overlaps match text:", ok2)
# table, R/L sorter as physically built: Q then D/A splitter
P=lambda e,s: sp.nsimplify(sp.simplify(sp.Abs(ov(e,s))**2))
sorters={"HV":(H,V),"DA":(Dd,A),"RL_direct":(R,L)}
expected={"H":[(1,0),(sp.Rational(1,2),)*2,(sp.Rational(1,2),)*2],
          "D":[(sp.Rational(1,2),)*2,(1,0),(sp.Rational(1,2),)*2],
          "R":[(sp.Rational(1,2),)*2,(sp.Rational(1,2),)*2,(1,0)]}
ok3=True
for name,s in {"H":H,"D":Dd,"R":R}.items():
    row=[(P(e1,s),P(e2,s)) for (e1,e2) in sorters.values()]
    # physical R/L sorter: Q then 45deg splitter; R -> A-exit, L -> D-exit
    phys=(P(A,Q*s),P(Dd,Q*s))
    print(name,row,"physical R/L (A-exit,D-exit):",phys)
    ok3 &= [tuple(x) for x in row]==[tuple(x) for x in expected[name]] and phys==row[2]
# A column of fig c-quarter-wave-hands
rowA=[(P(e1,A),P(e2,A)) for (e1,e2) in sorters.values()]; print("A row:",rowA)
ok3 &= rowA==[(sp.Rational(1,2),)*2,(0,1),(sp.Rational(1,2),)*2]
# normalization for every state
s1,s2=sp.symbols('s1 s2'); s=sp.Matrix([s1,s2])
tot_ok=True
for (e1,e2) in sorters.values():
    t=sp.expand((e1.H*s)[0]*sp.conjugate((e1.H*s)[0])+(e2.H*s)[0]*sp.conjugate((e2.H*s)[0]))
    diff=sp.simplify(t-(s1*sp.conjugate(s1)+s2*sp.conjugate(s2)))
    tot_ok &= diff==0
print("exits total |s1|^2+|s2|^2 for all sorters:", tot_ok)
x,y=sp.symbols('x y',real=True)
rot=sp.expand(I*(x+I*y)); ok4 = (sp.re(rot),sp.im(rot))==(-y,x)
print("i*(x+iy) -> (-y,x):", ok4)
print("PASS" if ok and ok2 and ok3 and tot_ok and ok4 else "FAIL")
