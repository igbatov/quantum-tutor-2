# Claims (Model 3 table): SD of frequency 0.4/sqrt(N): 0.126, 0.040, 0.0073, 0.0028, 0.0015;
# SD of count 0.4 sqrt(N): 1.3, 4, 22, 57, 106. "N=10 ... m=8 ... 45*0.8^8*0.2^2 = 0.302".
# "about 95% of runs lie within two standard deviations" (large N)
import numpy as np, math
from scipy.stats import binom
ok=True
Ns=[10,100,3000,20000,70000]; sdf=[0.126,0.040,0.0073,0.0028,0.0015]; sdc=[1.3,4,22,57,106]
for N,a,b in zip(Ns,sdf,sdc):
    x=0.4/np.sqrt(N); y=0.4*np.sqrt(N); print(N,round(x,5),round(y,2))
    ok&= abs(x-a)<=0.5*10**(-len(str(a).split('.')[1]))+1e-12 and abs(y-b)<=0.5*(1 if b>=4 else 0.1)+1e-9
ok&= math.isclose(np.sqrt(0.8*0.2),0.4)
inside=[m for m in range(11) if abs(m/10-0.8)<=0.05]; pr=45*0.8**8*0.04
print("N=10 frequencies within 0.05:",inside,"chance",pr,binom.pmf(8,10,0.8)); ok&= inside==[8] and abs(pr-0.302)<5e-4
for N in [1000,10000,70000]:
    m=np.arange(N+1); sd=0.4*np.sqrt(N); fr=binom.pmf(m[np.abs(m-0.8*N)<=2*sd],N,0.8).sum(); print("N",N,"within 2 SD:",fr); ok&=abs(fr-0.95)<0.01
print("PASS" if ok else "FAIL")
