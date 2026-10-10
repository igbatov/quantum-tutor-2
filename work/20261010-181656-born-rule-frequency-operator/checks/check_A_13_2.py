# New/revised caption numbers:
# overview "p(1-p)/N = 0.094, 0.019, 0.0019"; minimum at lambda=0.25
# model-1 "window 0.05 to 0.50 leaves out ... total probability below one in a million"; sd 0.043
# model-3 "0.656 and 0.292"; "11 of the 16 ... 0.6875"; N=100 "humps barely overlap"
# how-they-relate "1-norm rises to 1.41 at 45 deg, 3- and 4-norms fall to 0.89 and 0.84; all return to 1 at 90,180"
# experiment-2 "All four curves pass through (0,0),(1/2,1/2),(1,1)"; "0.37,0.25,0.16,0.10"; only q=2 diagonal
import numpy as np
from scipy.stats import binom
ok=True; p=0.25
d=[p*(1-p)/N for N in (2,10,100)]; print("overview depths",d); ok&= all(abs(a-b)<6e-4*b/0.0019*0.001+5e-4*(b>0.01)+5e-5 for a,b in zip(d,[0.094,0.019,0.0019]))
lam=np.linspace(0,1,100001)
for N in (2,10,100): ok&= abs(lam[np.argmin((lam-p)**2+d[0])]-p)<1e-4
m=np.arange(101); pm=binom.pmf(m,100,p); f=m/100
out=pm[(f<0.05-1e-12)|(f>0.5+1e-12)].sum(); print("model-1 mass outside [0.05,0.5]:",out, " sd",np.sqrt(p*(1-p)/100)); ok&= out<1e-6
w=binom.pmf(np.arange(5),4,0.9); print("model-3 N=4 weights",w); ok&= abs(w[4]-0.656)<6e-4 and abs(w[3]-0.292)<6e-4
ok&= sum(binom.pmf(k,4,0.5)*16 for k in range(3))==11
wN=binom.pmf(m,100,0.9); cN=binom.pmf(m,100,0.5); ov=np.minimum(wN,cN).sum(); print("N=100 overlap (sum of min):",ov, "peaks",m[np.argmax(wN)]/100,m[np.argmax(cN)]/100); ok&= ov<1e-3
th=np.radians([45,90,180]); 
for q,val in [(1,1.41),(3,0.89),(4,0.84)]:
    n=(np.abs(np.cos(th))**q+np.abs(np.sin(th))**q)**(1/q); print("q",q,n); ok&= abs(n[0]-val)<0.006 and np.allclose(n[1:],1)
n2=(np.cos(np.linspace(0,np.pi,1000))**2+np.sin(np.linspace(0,np.pi,1000))**2); ok&= np.allclose(n2,1)
x=np.linspace(0,1,1001)
def fq(x,q): c1=np.sqrt(x); c0=np.sqrt(1-x); return c1**q/(c0**q+c1**q)
for q,val in [(1,0.37),(2,0.25),(3,0.16),(4,0.10)]:
    v=fq(0.25,q); print("f_q",q,v, fq(0.0,q),fq(0.5,q),fq(1.0,q)); ok&= abs(v-val)<0.006 and fq(0.,q)==0 and abs(fq(.5,q)-.5)<1e-12 and fq(1.,q)==1
    if q!=2: ok&= np.max(np.abs(fq(x,q)-x))>0.05
ok&= np.max(np.abs(fq(x,2)-x))<1e-12
print("PASS" if ok else "FAIL")
