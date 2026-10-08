# Claim: "A hidden mix of vertical and horizontal photons would give half ... But all of them pass"
import numpy as np
D=np.array([1,1])/np.sqrt(2); V=np.array([0,1.]); H=np.array([1.,0])
PD=np.outer(D,D)
rho_mix=0.5*np.outer(V,V)+0.5*np.outer(H,H)
p_mix=np.trace(PD@rho_mix); p_pure=np.trace(PD@np.outer(D,D))
# also any mixture with weights w: still 1/2
pw=[np.trace(PD@(w*np.outer(V,V)+(1-w)*np.outer(H,H))) for w in np.linspace(0,1,11)]
print("mix:",p_mix,"pure 45:",p_pure,"any V/H mixture:",np.round(pw,12))
print("PASS" if abs(p_mix-0.5)<1e-12 and abs(p_pure-1)<1e-12 and np.allclose(pw,0.5) else "FAIL")
