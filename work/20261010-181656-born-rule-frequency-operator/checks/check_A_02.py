# Claim: "a classical wave divides its energy and gives at least 1" (double-firing ratio alpha)
# alpha = <I_T I_R>/(<I_T><I_R>) with I_T=t*I, I_R=r*I -> <I^2>/<I>^2 >= 1 for any intensity distribution
import numpy as np
rng=np.random.default_rng(0); ok=True
for name,I in [("constant",np.ones(10**6)),("thermal",rng.exponential(1,10**6)),("random pulses",rng.gamma(0.3,1,10**6)),("uniform",rng.uniform(0,1,10**6))]:
    t,r=0.75,0.25
    a=np.mean(t*I*r*I)/(np.mean(t*I)*np.mean(r*I)); print(name,"alpha=",a); ok&= a>=1-1e-9
# ideal single photon: never both -> alpha=0
print("single photon alpha=0 (both detectors never fire)")
print("Grangier-Roger-Aspect value 0.18+-0.06 is a literature value: UNVERIFIABLE by computation (consistent with <1)")
print("PASS" if ok else "FAIL")
