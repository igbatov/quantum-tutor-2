# Claim: projection noise "variance ... Np(1-p) ... 100 ions at p=1/2 is 25, sd 5 ... p=0.1 is 9, sd 3";
# "a fixed spread of shares ... lowers the scatter a little, while field noise ... run to run would raise it";
# "error bars of size sqrt(p(1-p)/M)"; figure maxima 0.158, 0.050, 0.0158
import numpy as np
from scipy.stats import binom
ok=True
for p,v,s in [(0.5,25,5),(0.1,9,3)]:
    var=binom(100,p).var(); print(f"p={p}: var={var}, sd={np.sqrt(var)}"); ok&=abs(var-v)<1e-9 and abs(np.sqrt(var)-s)<1e-9
for p in [0,1]: ok&=binom(100,p).var()==0
ps=np.linspace(0,1,1001); vv=ps*(1-ps); ok&=ps[np.argmax(vv)]==0.5
for N,want in [(10,0.158),(100,0.050),(1000,0.0158)]:
    m=np.sqrt(0.25/N); print(f"N={N} max sd of fraction {m:.4f} (text {want})"); ok&=abs(m-want)<6e-4*max(1,want/0.05)
# static spread: Poisson-binomial variance sum p_i(1-p_i) = N pbar(1-pbar) - sum (p_i-pbar)^2
rng=np.random.default_rng(0); worst=-1
for _ in range(2000):
    pbar=rng.uniform(0.05,0.95); pi=np.clip(pbar+rng.normal(0,0.03,100),0,1)
    diff=np.sum(pi*(1-pi))-100*pi.mean()*(1-pi.mean()); worst=max(worst,diff)
print("static spread: max [sum p_i(1-p_i) - N pbar(1-pbar)] =",worst,"(<=0: lowered)"); ok&=worst<=1e-9
# run-to-run field noise common to all ions: Monte Carlo of Rabi angle jitter, N=100
N=100; R=200000; th0=np.pi/2   # p=1/2 nominal
for sig in [0.05,0.1]:
    th=th0+rng.normal(0,sig,R); p_run=np.sin(th/2)**2
    m=rng.binomial(N,p_run); pbar=p_run.mean()
    exact=N*np.mean(p_run*(1-p_run))+N**2*np.var(p_run)
    print(f"common jitter sigma={sig}: var(m)={m.var():.2f}, formula {exact:.2f}, binomial N pbar(1-pbar)={N*pbar*(1-pbar):.2f}")
    ok&= m.var()>N*pbar*(1-pbar)
# per-ion independent jitter leaves variance at N pbar(1-pbar) (noted, not claimed)
th=th0+rng.normal(0,0.1,(R//10,N)); m=rng.binomial(1,np.sin(th/2)**2).sum(1); pb=np.mean(np.sin(th/2)**2)
print(f"independent per-ion jitter: var(m)={m.var():.2f} vs N pbar(1-pbar)={N*pb*(1-pb):.2f}")
M=500;p=0.3; print("sd of fraction over M runs:",binom(M,p).std()/M,"vs",np.sqrt(p*(1-p)/M)); ok&=abs(binom(M,p).std()/M-np.sqrt(p*(1-p)/M))<1e-12
print("PASS" if ok else "FAIL")
