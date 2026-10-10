# Check-yourself: "N = 4 and p = 0.9 ... leftover (F_4 - lambda)Psi_4 at lambda = 1 ... which lambda shortest"
# Expected answer: 0.0325 both ways, minimum at lambda = 0.9
import sympy as sp, itertools
p=sp.Rational(9,10); N=4; lam=sp.symbols('lambda')
w=[sp.binomial(N,m)*p**m*(1-p)**(N-m) for m in range(N+1)]
print("group weights",[float(x) for x in w],"sum",sum(w))
fromw=sum(w[m]*(sp.Rational(m,N)-1)**2 for m in range(N+1))
terms=[float(w[m]*(sp.Rational(m,N)-1)**2) for m in range(N+1)]
parab=p*(1-p)/N+(1-p)**2
# full 16-entry vector check
c1=sp.sqrt(p); c0=sp.sqrt(1-p); tot=0
for s in itertools.product([0,1],repeat=N):
    a=sp.prod([c1 if x else c0 for x in s]); tot+=((sp.Rational(sum(s),N)-1)*a)**2
gen=sp.expand(sum(w[m]*(sp.Rational(m,N)-lam)**2 for m in range(N+1)))
lmin=sp.solve(sp.diff(gen,lam),lam)[0]
print("terms",terms,"from weights",fromw,float(fromw),"parabola",parab,"16-entry",sp.nsimplify(tot),"argmin",lmin,"min",gen.subs(lam,lmin))
ok= fromw==sp.Rational(13,400) and parab==fromw and sp.simplify(tot-fromw)==0 and lmin==p and gen.subs(lam,lmin)==p*(1-p)/N
print("0.0325 ==",float(fromw))
print("PASS" if ok else "FAIL")
