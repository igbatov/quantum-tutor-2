# Claims: f_q = |c1|^q/(|c0|^q+|c1|^q) = 2^q/(1+2^q): 2/3, 4/5, 8/9, 16/17; totals 1.342^N, 1, 0.805^N, 0.68^N;
# |c0|^q+|c1|^q >1 for q<2, <1 for q>2; N=20 peaks at m = 13-14, 16, 19; Everett with q-norm gives mu=|a|^q
import numpy as np, math, sympy as sp
ok=True; c0=math.sqrt(.2); c1=math.sqrt(.8)
for q,f in [(1,2/3),(2,.8),(3,8/9),(4,16/17)]:
    fq=c1**q/(c0**q+c1**q); t=c0**q+c1**q; print("q",q,"f_q",fq,"total base",t); ok&=abs(fq-f)<1e-12
ok&= abs((c0+c1)-1.342)<5e-4 and abs(c0**3+c1**3-0.805)<5e-4 and abs(c0**4+c1**4-0.68)<1e-12
qs=np.linspace(0.05,10,2000); s=c0**qs+c1**qs
ok&= np.all(s[qs<1.999]>1) and np.all(s[qs>2.001]<1)
for q,expect in [(1,{13,14}),(2,{16}),(4,{19})]:
    v=np.array([math.comb(20,m)*c0**(q*(20-m))*c1**(q*m) for m in range(21)])
    peaks={m for m in range(21) if abs(v[m]-v.max())/v.max()<1e-9}; print("q",q,"peak m",peaks); ok&= peaks==expect
# Large-N dominant frequency approaches f_q
for q in [1,3]:
    N=20000; m=np.arange(N+1); from scipy.special import gammaln
    lv=gammaln(N+1)-gammaln(m+1)-gammaln(N-m+1)+q*(N-m)*np.log(c0)+q*m*np.log(c1); print(" q",q,"N=2e4 argmax m/N",m[lv.argmax()]/N)
# Cauchy additive with q-norm: g(x)=mu(x^(1/q)) linear -> mu(a)=k a^q; consistency check
a=sp.symbols('a',positive=True); q=sp.symbols('q',positive=True); k=sp.symbols('k')
mu=lambda x:k*x**q; a1,a2=sp.symbols('a1 a2',positive=True)
ok&= sp.simplify(mu((a1**q+a2**q)**(1/q))-mu(a1)-mu(a2))==0
print("PASS" if ok else "FAIL")
