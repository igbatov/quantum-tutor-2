# Claim: "a photon with a sure answer to one is 50/50 on the other ... no state has sure answers to both"
import sympy as sp
Z=sp.Matrix([[1,0],[0,-1]])  # V/H question
X=sp.Matrix([[0,1],[1,0]])   # diagonal question
print("[Z,X] =",(Z*X-X*Z).tolist())
ez=[v[2][0] for v in Z.eigenvects()]; ex=[v[2][0] for v in X.eigenvects()]
probs=[sp.simplify((u.normalized().T*w.normalized())[0]**2) for u in ez for w in ex]
print("overlap^2 between eigenbases:",probs)
# common eigenvector? check if any Z eigvec is X eigvec
common=any((X*u).cross(u)==sp.zeros(1,3) if False else sp.Matrix.hstack(X*u,u).rank()==1 for u in ez)
print("common eigenvector exists:",common)
# uncertainty: for any state, Var(Z)+Var(X) >= 1 (so both can't be zero)
a,b=sp.symbols('a b',real=True)
th=sp.symbols('th',real=True)
psi=sp.Matrix([sp.cos(th),sp.sin(th)])
var=lambda A: sp.simplify((psi.T*A*A*psi)[0]-(psi.T*A*psi)[0]**2)
s=sp.simplify(var(Z)+var(X)); print("Var Z + Var X (real states) =",s)
ok=all(p==sp.Rational(1,2) for p in probs) and not common and sp.simplify(s-1)==0
print("PASS" if ok else "FAIL")
