# Claims: Model 3 "the variance p(1-p)/N, is exactly the floor of Model 2's parabola";
# Model 2 Pros: "floor p(1-p)/N is the variance ..., the square of the measured 1/sqrt N scatter"
import sympy as sp
p,N,lam=sp.symbols('p N lambda',positive=True)
floor=p*(1-p)/N; sd=sp.sqrt(p*(1-p)/N)
# variance of binomial frequency
m=sp.symbols('m'); n=6; pp=sp.Rational(4,5)
var=sum(sp.binomial(n,k)*pp**k*(1-pp)**(n-k)*(sp.Rational(k,n)-pp)**2 for k in range(n+1))
ok = sp.simplify(floor-sd**2)==0 and var==floor.subs({p:pp,N:n})
# floor = min over lambda of p(1-p)/N + (lambda-p)^2
par=floor+(lam-p)**2; lmin=sp.solve(sp.diff(par,lam),lam)[0]
ok &= sp.simplify(lmin-p)==0 and sp.simplify(par.subs(lam,lmin)-floor)==0
print("floor == SD^2:",sp.simplify(floor-sd**2)==0,"; binomial variance N=6 p=0.8:",var,"floor:",floor.subs({p:pp,N:n}),"; argmin",lmin)
print("PASS" if ok else "FAIL")
