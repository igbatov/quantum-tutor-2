# Claim: "S[(m/N - p)^2] = p(1-p)/N" with S[1]=1, S[m]=Np, S[m^2]=Np+N(N-1)p^2; and N=3 check 0.0533 = 0.16/3
import sympy as sp, math
N,p,lam=sp.symbols('N p lambda',positive=True)
Sm2=N*p+N*(N-1)*p**2; Sm=N*p
expr=Sm2/N**2-2*p*Sm/N+p**2
r1=sp.simplify(expr-p*(1-p)/N)
# direct binomial check for several N with sympy exact sums
ok = r1==0
for n in [1,2,3,5,10,20]:
    pp=sp.Rational(4,5)
    S=lambda f: sum(sp.binomial(n,m)*pp**m*(1-pp)**(n-m)*f(m) for m in range(n+1))
    ok &= S(lambda m:1)==1 and S(lambda m:m)==n*pp and S(lambda m:m**2)==n*pp+n*(n-1)*pp**2
    ok &= sp.simplify(S(lambda m:(sp.Rational(m,n)-pp)**2) - pp*(1-pp)/n)==0
# parabola identity: S[(m/N-lam)^2] = p(1-p)/N + (lam-p)^2
for n in [2,3,7]:
    pp=sp.Rational(4,5)
    S=sum(sp.binomial(n,m)*pp**m*(1-pp)**(n-m)*(sp.Rational(m,n)-lam)**2 for m in range(n+1))
    ok &= sp.expand(S-(pp*(1-pp)/n+(lam-pp)**2))==0
terms=[0.008*(0-0.8)**2,0.096*(1/3-0.8)**2,0.384*(2/3-0.8)**2,0.512*(1-0.8)**2]
print("N=3 terms",[round(t,5) for t in terms],"sum",sum(terms),"0.16/3",0.16/3)
ok &= all(abs(a-b)<1e-5 for a,b in zip(terms,[0.00512,0.02091,0.00683,0.02048])) and abs(sum(terms)-0.16/3)<1e-12
print("symbolic residual",r1)
print("PASS" if ok else "FAIL")
