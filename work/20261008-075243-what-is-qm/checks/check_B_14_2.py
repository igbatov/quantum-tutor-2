# Claims (Model 2): wave has "north" and "south" pieces "in proportions set by the angle (the nearer
# the point to north, the bigger the north piece)"; "point and the two pieces are one state described two ways";
# chances "given by the squared sizes of the two pieces"
import sympy as sp, numpy as np
th,ph=sp.symbols('theta phi',real=True)
a=sp.cos(th/2); b=sp.exp(sp.I*ph)*sp.sin(th/2)
norm=sp.simplify(a**2+sp.Abs(b)**2); print("|north|^2+|south|^2 =",norm)
ok = norm==1
d=sp.diff(a,th); print("d|north|/dtheta =",d,"(<0 on (0,pi): bigger as point nears north)")
ok &= all(float(d.subs(th,t))<0 for t in np.linspace(0.01,3.13,50))
# pieces -> point: Bloch vector reconstructed
psi=sp.Matrix([a,b]); sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-sp.I],[sp.I,0]]); sz=sp.diag(1,-1)
vec=[sp.simplify(sp.expand_complex((psi.H*s*psi)[0]).rewrite(sp.cos)) for s in (sx,sy,sz)]
target=[sp.sin(th)*sp.cos(ph),sp.sin(th)*sp.sin(ph),sp.cos(th)]
diff=[sp.simplify(sp.trigsimp(v-t)) for v,t in zip(vec,target)]; print("Bloch vector - point:",diff)
ok &= all(x==0 for x in diff)
P_up=sp.simplify(a**2); print("squared north piece =",P_up,"= Model 1 chance cos^2(theta/2)")
print("PASS" if ok else "FAIL")
