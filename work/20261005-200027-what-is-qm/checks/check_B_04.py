# Claim: "secretly vertical or horizontal ... a 45 filter would pass only half"; "In fact, it passes every one."
# Claim: "a vertical photon is a superposition of the two diagonals, 45 and 135"
import numpy as np
V, H = np.array([1.,0]), np.array([0.,1])
D = (V+H)/np.sqrt(2); A = (V-H)/np.sqrt(2)     # 45 and 135 deg (axes measured from vertical)
P = lambda s, f: abs(np.vdot(f, s))**2
mix = 0.5*P(V, D) + 0.5*P(H, D)
pure = P(D, D)
cD, cA = np.vdot(D, V), np.vdot(A, V)
recon = cD*D + cA*A
print("mixture passes 45 filter:", mix, " real 45 photon passes:", pure)
print("V components on 45,135:", cD, cA, " reconstruction error:", np.linalg.norm(recon - V))
ok = abs(mix-0.5)<1e-12 and abs(pure-1)<1e-12 and abs(cD)>0.1 and abs(cA)>0.1 and np.linalg.norm(recon-V)<1e-12
print("PASS" if ok else "FAIL")
