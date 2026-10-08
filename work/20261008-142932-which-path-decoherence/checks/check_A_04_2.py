# Claims (pair state, Walborn 2002, Psi+ = (HV+VH)/sqrt2): "horizontal and vertical ... always ...
# opposite"; "diagonals ... always the same result"; "each photon on its own ... 50/50 ... any direction".
import numpy as np
H = np.array([1, 0]); V = np.array([0, 1])
psi = (np.kron(H, V)+np.kron(V, H))/np.sqrt(2)          # order: slit (x) partner
lin = lambda a: np.array([np.cos(a), np.sin(a)])
def joint(a, b): return abs(np.vdot(np.kron(lin(a), lin(b)), psi))**2
pHH, pHV = joint(0, 0), joint(0, np.pi/2)
pPP, pPM = joint(np.pi/4, np.pi/4), joint(np.pi/4, -np.pi/4)
pMM = joint(-np.pi/4, -np.pi/4)
print(f"P(H,H)={pHH:.3f} P(H,V)={pHV:.3f} | P(+45,+45)={pPP:.3f} P(-45,-45)={pMM:.3f} P(+45,-45)={pPM:.3f}")
rho = np.outer(psi, psi.conj()).reshape(2, 2, 2, 2)
rs = np.einsum('ijkj->ik', rho); rp = np.einsum('jijk->ik', rho)
print("reduced slit:", np.round(rs, 6).tolist(), " reduced partner:", np.round(rp, 6).tolist())
# 50/50 along any direction incl. elliptical: reduced state = I/2
ok = pHH < 1e-12 and abs(pHV-0.5) < 1e-12 and abs(pPP-0.5) < 1e-12 and abs(pMM-0.5) < 1e-12 and pPM < 1e-12 \
     and np.allclose(rs, np.eye(2)/2) and np.allclose(rp, np.eye(2)/2)
print("PASS" if ok else "FAIL")
