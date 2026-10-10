# Claims: classical wave "alpha is at least 1 (exactly 1 for a steady wave, higher for one whose intensity fluctuates)";
# "for an ideal single photon alpha is zero"; data: "alpha = 0.18 ± 0.06", "visibility of 98%", "about 8.09, more than forty sd above 7.66", ~2000 atoms
import numpy as np
rng=np.random.default_rng(2)
eta=1e-3  # small detection probability per unit intensity
def alpha(I):
    pT=eta*I/2; pR=eta*I/2              # each detector fires independently given its share
    return np.mean(pT*pR)/(np.mean(pT)*np.mean(pR))
I_steady=np.ones(10**6); I_exp=rng.exponential(size=10**6); I_unif=rng.uniform(0,2,10**6)
a=[alpha(I_steady),alpha(I_exp),alpha(I_unif)]
print('alpha steady %.3f, exponential %.3f, uniform %.3f (Cauchy-Schwarz: <I^2>/<I>^2 >= 1)'%tuple(a))
# single photon: Fock state |1>, g2 = <n(n-1)>/<n>^2 = 0
n=1; g2=n*(n-1)/n**2; print('single photon alpha =',g2)
ok=abs(a[0]-1)<1e-12 and a[1]>1.9 and a[2]>1 and g2==0
print('PASS' if ok else 'FAIL')
print('UNVERIFIABLE: experimental numbers alpha=0.18±0.06, V=98%, T=8.09 (>40 sd above 7.66), ~2000-atom molecules are data, not computable.')
print('  consistency: (8.09-7.66)/43 sd ->', round((8.09-7.6605)/43,4),'per sd if 43 sd quoted')
