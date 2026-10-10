# Claim: q-size ratio v_{m+1}/v_m = (N-m)/(m+1) (c1/c0)^q; peak fraction f_q = c1^q/(c0^q+c1^q);
# table p=0.1: f_q = 1/4, 1/10, 1/28=0.0357, 1/82=0.0122; totals 1.2649^N, 1, 0.8854^N, 0.82^N;
# "Only q=2 delivers p"; "equal amplitudes ... every q gives 1/2"; 2-norm only preserved by small mixing maps (Banach-Lamperti)
import numpy as np, sympy as sp
from math import comb
ok=True
c0,c1=np.sqrt(.9),np.sqrt(.1)
q_,N_,m_=sp.symbols('q N m',positive=True)
ratio=sp.simplify(sp.binomial(N_,m_+1)/sp.binomial(N_,m_)); print("C(N,m+1)/C(N,m) =",sp.simplify(sp.combsimp(ratio)))
ok&=sp.simplify(sp.combsimp(ratio)-(N_-m_)/(m_+1))==0
for q,ft,tot in [(1,0.25,1.2649),(2,0.10,1.0),(3,0.0357,0.8854),(4,0.0122,0.82)]:
    f=c1**q/(c0**q+c1**q); T=c0**q+c1**q
    N=2000; v=np.array([comb(N,m)*(c0**q)**(N-m)*(c1**q)**m for m in range(N+1)],dtype=float) if q>=2 else None
    # use logs to avoid overflow
    lv=np.array([np.log(float(comb(N,m))) if comb(N,m)<1e300 else sum(np.log(np.arange(N-m+1,N+1)))-sum(np.log(np.arange(1,m+1))) for m in range(N+1)])+q*((N-np.arange(N+1))*np.log(c0)+np.arange(N+1)*np.log(c1))
    peak=np.argmax(lv)/N
    print(f"q={q}: f_q={f:.4f} (1/(3^q+1)={1/(3**q+1):.4f}, text {ft}), peak m/N at N=2000: {peak:.4f}, base={T:.4f} (text {tot})")
    ok&=abs(f-ft)<6e-5 and abs(f-1/(3**q+1))<1e-12 and abs(T-tot)<6e-5 and abs(peak-f)<1e-3
for p in [0.05,0.1,0.3,0.7]:
    a0,a1=np.sqrt(1-p),np.sqrt(p)
    hits=[q for q in np.linspace(0.5,6,1101) if abs(a1**q/(a0**q+a1**q)-p)<1e-9]
    print(f"p={p}: q with f_q=p:",np.round(hits,3)); ok&=len(hits)==1 and abs(hits[0]-2)<1e-6
ok&=all(abs(0.5**(q/2)/(2*0.5**(q/2))-0.5)<1e-12 for q in [1,2,3,4])
# small rotation preserves 2-norm, not q-norms (q != 2)
v=np.array([c0,c1]); th=0.01; R=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]]); w=R@v
for q in [1,2,3]:
    print(f"q={q}: q-size before {np.sum(np.abs(v)**q):.6f} after small rotation {np.sum(np.abs(w)**q):.6f}")
ok&=abs(np.sum(w**2)-1)<1e-12 and abs(np.sum(np.abs(w))-np.sum(np.abs(v)))>1e-4
print("PASS" if ok else "FAIL")
