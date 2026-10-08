# Claim: "in a crystal the rungs of its countless atoms crowd into bands so dense they act as continuous, often with gaps between"
# Model: tight-binding chain of N atoms, two orbitals per atom (rungs at -5 and -1, hopping t=0.5, 0.3).
import numpy as np
def chain(N, eps, t):
    Hm = np.diag(np.full(N, eps)) + np.diag(np.full(N-1, -t), 1) + np.diag(np.full(N-1, -t), -1)
    return np.linalg.eigvalsh(Hm)
ok = True
for N in (2, 10, 100, 2000):
    lv = np.sort(np.concatenate([chain(N, -5.0, 0.5), chain(N, -1.0, 0.3)]))
    b1 = lv[:N]; b2 = lv[N:]
    sp1 = np.max(np.diff(b1)); gap = b2[0] - b1[-1]
    print(f"N={N}: band1 [{b1[0]:.3f},{b1[-1]:.3f}] max spacing {sp1:.2e}; band2 [{b2[0]:.3f},{b2[-1]:.3f}]; gap {gap:.3f}")
ok &= sp1 < 1e-2 and gap > 2.0 and abs((b1[-1]-b1[0]) - 2.0) < 1e-3
# N = 10^23: max spacing ~ 4t*pi/N -> ~ 1e-23 eV-scale, effectively continuous
print("max level spacing for N=1e23 (t=0.5 eV): %.1e eV" % (4*0.5*np.pi/1e23))
print("PASS" if ok else "FAIL")
