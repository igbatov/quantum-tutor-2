# Claim: "when the two amplitudes are equal in size, every exponent gives 1/2"; f_q table 0.366,0.250,0.161,0.100;
# totals 1.366^N, 1, 0.775^N, 0.625^N; "1 only when ... q = 2"; ratio v_{m+1}/v_m and peak location
import numpy as np, sympy as sp
from scipy.special import gammaln
ok=True
q=sp.symbols('q',positive=True); a=sp.Symbol('a',positive=True)
fq=a**q/(a**q+a**q); ok&= sp.simplify(fq-sp.Rational(1,2))==0
c0,c1=np.sqrt(3)/2,0.5
exp={1:(0.366,1.366),2:(0.250,1.0),3:(0.161,0.775),4:(0.100,0.625)}
for qq,(f,t) in exp.items():
    F=c1**qq/(c0**qq+c1**qq); T=c0**qq+c1**qq; print(qq,F,T); ok&= abs(F-f)<6e-4 and abs(T-t)<6e-4
# uniqueness of q=2: g(q)=c0^q+c1^q strictly decreasing
qs=np.linspace(0.1,10,10000); g=c0**qs+c1**qs; ok&= np.all(np.diff(g)<0)
# numeric peak of v_m at large N
N=200000
for qq in [1,2,3,4]:
    m=np.arange(N+1); lv=gammaln(N+1)-gammaln(m+1)-gammaln(N-m+1)+qq*(N-m)*np.log(c0)+qq*m*np.log(c1)
    pk=m[np.argmax(lv)]/N; print("q",qq,"peak m/N",pk); ok&= abs(pk-c1**qq/(c0**qq+c1**qq))<1e-4
# ratio formula symbolic
Ns,ms=sp.symbols('N m',positive=True,integer=True); A,B=sp.symbols('A B',positive=True)
v=lambda mm: sp.binomial(Ns,mm)*A**(q*(Ns-mm))*B**(q*mm)
r=sp.simplify(sp.combsimp(v(ms+1)/v(ms)) - (Ns-ms)/(ms+1)*B**q/A**q); ok&= r==0
print("PASS" if ok else "FAIL")
