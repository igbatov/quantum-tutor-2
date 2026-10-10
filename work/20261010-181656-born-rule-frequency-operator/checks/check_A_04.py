# Claim: N=1,2,3 table of entries c0^{N-m} c1^m, squared sizes, readings; "squared sizes total 1";
# w_m sums to 1 by binomial theorem; "w_m is the binomial distribution"
import numpy as np, itertools, sympy as sp
ok=True
c0,c1=np.cos(np.pi/6),np.sin(np.pi/6)
exp_num={(3,0):0.650,(3,1):0.375,(3,2):0.217,(3,3):0.125,(2,0):0.75,(2,1):0.433,(2,2):0.25}
exp_sq={(3,0):0.422,(3,1):0.141,(3,2):0.047,(3,3):0.0156,(2,0):0.5625,(2,1):0.1875,(2,2):0.0625}
for (N,m),v in exp_num.items():
    e=c0**(N-m)*c1**m; print(N,m,e,e*e); ok&= abs(e-v)<6e-4 and abs(e*e-exp_sq[(N,m)])<6e-4
for N in [1,2,3,8]:
    s=sum(np.prod([c1 if x else c0 for x in st])**2 for st in itertools.product([0,1],repeat=N)); ok&= abs(s-1)<1e-12
p,Nn=sp.symbols('p N',positive=True)
for N in range(1,8):
    ok&= sp.expand(sum(sp.binomial(N,m)*p**m*(1-p)**(N-m) for m in range(N+1)))==1
print("PASS" if ok else "FAIL")
