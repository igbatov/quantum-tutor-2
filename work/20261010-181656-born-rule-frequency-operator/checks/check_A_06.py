# Claim: ||(F_N-lambda)Psi_N||^2 = (lambda-p)^2 + p(1-p)/N; <F>=p, <F^2>=p^2+p(1-p)/N; minimum at lambda=p;
# N=2, p=1/4: 3/32 at lambda=1/4, 10/64=5/32=0.156 at lambda=1/2; "p=1/2 gives 1/8 at N=2"; <P^jP^k>=p^2
import sympy as sp, numpy as np, itertools
ok=True
p,lam=sp.symbols('p lambda',positive=True)
for N in range(1,9):
    w=[sp.binomial(N,m)*p**m*(1-p)**(N-m) for m in range(N+1)]
    S=sum(w[m]*(sp.Rational(m,N)-lam)**2 for m in range(N+1))
    ok&= sp.expand(S-((lam-p)**2+p*(1-p)/N))==0
    ok&= sp.expand(sum(w[m]*sp.Rational(m,N) for m in range(N+1))-p)==0
    ok&= sp.expand(sum(w[m]*sp.Rational(m,N)**2 for m in range(N+1))-(p**2+p*(1-p)/N))==0
f=lambda N,pp,l: (l-pp)**2+pp*(1-pp)/N
v1=f(2,sp.Rational(1,4),sp.Rational(1,4)); v2=f(2,sp.Rational(1,4),sp.Rational(1,2)); v3=f(2,sp.Rational(1,2),sp.Rational(1,2))
print(v1,v2,float(v2),v3); ok&= v1==sp.Rational(3,32) and v2==sp.Rational(10,64) and v3==sp.Rational(1,8)
# explicit N=2 terms
t=sp.Rational(9,16)*lam**2+sp.Rational(6,16)*(sp.Rational(1,2)-lam)**2+sp.Rational(1,16)*(1-lam)**2
ok&= t.subs(lam,sp.Rational(1,4))==sp.Rational(24,256)
# numeric check of <P^j P^k> with matrices, N=3, p=0.3
N=3; pp=0.3; strs=list(itertools.product([0,1],repeat=N))
w=np.array([np.prod([pp if x else 1-pp for x in s]) for s in strs])
for j in range(N):
    for k in range(N):
        val=sum(w[i]*s[j]*s[k] for i,s in enumerate(strs)); ok&= abs(val-(pp if j==k else pp*pp))<1e-12
print("PASS" if ok else "FAIL")
