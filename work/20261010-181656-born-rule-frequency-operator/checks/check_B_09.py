# Claim: many-worlds table N=4, p=0.1; "Eleven of the sixteen branches, 69% by count ... weight 0.0523";
# "for N=20 the most numerous branches have fraction 1/2 whatever p is, while the group carrying the most weight has fraction 0.1";
# Everett: weight depending only on |entry|, monotone, additive on merging "must be the squared entry"
import numpy as np, sympy as sp
from math import comb
ok=True
p=0.1; each=[p**m*(1-p)**(4-m) for m in range(5)]; tot=[comb(4,m)*each[m] for m in range(5)]
print("each",np.round(each,4),"total",np.round(tot,4),"sum",sum(tot))
ok&=np.allclose(each,[0.6561,0.0729,0.0081,0.0009,0.0001]) and np.allclose(tot,[0.6561,0.2916,0.0486,0.0036,0.0001]) and abs(sum(tot)-1)<1e-12
n=sum(comb(4,m) for m in range(2,5)); wt=sum(tot[2:]); print("branches m>=2:",n,f"{n/16:.2%}","weight",wt)
ok&= n==11 and round(n/16*100)==69 and abs(wt-0.0523)<1e-12
N=20; cnt=[comb(N,m) for m in range(N+1)]; w=[comb(N,m)*p**m*(1-p)**(N-m) for m in range(N+1)]
print("N=20 most numerous m/N:",np.argmax(cnt)/N,"; most weight m/N:",np.argmax(w)/N)
ok&= np.argmax(cnt)/N==0.5 and np.argmax(w)/N==0.1
# Everett additivity: f(x)=x^q with f(sqrt(a^2+b^2))=f(a)+f(b)
a,b,q=sp.symbols('a b q',positive=True)
for qq in [1,2,3,4]:
    d=sp.simplify(sp.sqrt(a**2+b**2)**qq-a**qq-b**qq); print(f"q={qq}: f(merged)-f(a)-f(b) = {d}"); ok&= (d==0)==(qq==2)
# general: g(u)=f(sqrt u) additive & monotone -> linear -> f = k x^2 (Cauchy); numeric illustration only
print("PASS" if ok else "FAIL")
