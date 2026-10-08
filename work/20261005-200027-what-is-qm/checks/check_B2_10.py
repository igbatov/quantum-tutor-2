# Claim: "Left isolated, a system's arrow changes, if at all, gradually and predictably, by ... the Schrödinger equation"
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(4)
A = rng.normal(size=(5,5))+1j*rng.normal(size=(5,5)); Hm = (A+A.conj().T)/2
psi0 = rng.normal(size=5)+1j*rng.normal(size=5); psi0 /= np.linalg.norm(psi0)
ts = np.arange(0, 10, 0.01); traj = np.array([expm(-1j*Hm*t) @ psi0 for t in ts])
norm_err = np.max(abs(np.linalg.norm(traj, axis=1)-1)); step = np.max(np.linalg.norm(np.diff(traj, axis=0), axis=1))
again = expm(-1j*Hm*ts[-1]) @ psi0; det_err = np.linalg.norm(again-traj[-1])
E, V = np.linalg.eigh(Hm); ev = V[:,0]; evt = expm(-1j*Hm*3.0) @ ev
fid = abs(np.vdot(ev, evt))**2
print("norm error %.1e, max step (dt=0.01) %.4f, rerun difference %.1e, eigenstate fidelity after t=3: %.12f" % (norm_err, step, det_err, fid))
print("PASS" if norm_err < 1e-12 and step < 0.1 and det_err < 1e-12 and abs(fid-1) < 1e-12 else "FAIL")
