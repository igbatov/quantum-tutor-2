# Claims: F2 Psi2 = (0, 0.2, 0.2, 0.8), not an eigenvector; (0,0.6,0.8,0) -> 1/2 x itself;
# N=2 parabola by hand: 0.0256+0.0288+0.0256=0.08; at 1/2: 0.01+0+0.16=0.17; at 1: 0.04+0.08+0=0.12
import numpy as np, itertools
ok=True
F=np.diag([0,.5,.5,1]); P=np.array([.2,.4,.4,.8]); FP=F@P; print("F2 Psi2",FP)
ok&=np.allclose(FP,[0,.2,.2,.8]); ok&= np.linalg.matrix_rank(np.vstack([FP,P]))==2
v=np.array([0,.6,.8,0]); ok&=np.allclose(F@v,0.5*v); print("F2 v",F@v)
def lf(l): return [0.04*l**2,0.32*(0.5-l)**2,0.64*(1-l)**2]
for l,exp_terms,tot in [(0.8,[0.0256,0.0288,0.0256],0.08),(0.5,[0.01,0,0.16],0.17),(1,[0.04,0.08,0],0.12)]:
    t=lf(l); print("lam",l,np.round(t,5),sum(t)); ok&=np.allclose(t,exp_terms) and abs(sum(t)-tot)<1e-12 and abs(tot-((l-0.8)**2+0.08))<1e-12
# Psi_N not an eigenvector for any finite N: entries at every reading nonzero
for N in range(1,12):
    w=[ (0.8**m*0.2**(N-m)) for m in range(N+1)]; ok&=min(w)>0
# Leftover length sqrt(0.16/N) -> 0 (Hartle)
print("leftover length N=1e6:",np.sqrt(0.16/1e6))
print("PASS" if ok else "FAIL")
