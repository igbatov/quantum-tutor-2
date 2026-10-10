# Claim: N=4, p=0.9: w0+w1+w2 = 0.0001+0.0036+0.0486 = 0.0523; w3=0.2916, w4=0.6561; 11 of 16 = 0.6875;
# "By number of branches, most branches see a fraction near 1/2 whatever p is"; maverick bound
import numpy as np
from math import comb
from scipy.stats import binom
ok=True; p=0.9; N=4
w=[comb(N,m)*p**m*(1-p)**(N-m) for m in range(5)]; print(w)
ok&= np.allclose(w[:3],[0.0001,0.0036,0.0486]) and abs(sum(w[:3])-0.0523)<1e-12 and abs(w[3]-0.2916)<1e-12 and abs(w[4]-0.6561)<1e-12
ok&= comb(4,0)+comb(4,1)+comb(4,2)==11 and 11/16==0.6875
for N in [100,1000,10000]:
    cnt=binom.cdf(int(np.floor(N*0.55)),N,0.5)-binom.cdf(int(np.ceil(N*0.45))-1,N,0.5)
    wt=binom.cdf(int(np.floor(N*0.55)),N,p)-binom.cdf(int(np.ceil(N*0.45))-1,N,p)
    print(N,"fraction of branches by count within 0.05 of 1/2:",cnt,"by weight:",wt)
ok&= cnt>0.99
print("PASS" if ok else "FAIL")
