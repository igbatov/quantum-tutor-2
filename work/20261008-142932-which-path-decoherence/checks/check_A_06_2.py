# Claims: "through the left slit" ends as "left-turning with the partner vertical, or right-turning
# with the partner horizontal", right slit "the same with the handednesses swapped"; "can ... be told
# apart with certainty, but only by looking at both photons"; "the slit photon's handedness alone, or
# the partner alone, says nothing about the slit".
import numpy as np
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def qwp(t): return rot(t) @ np.diag([1, 1j]) @ rot(-t)
J1, J2 = qwp(np.pi/4), qwp(-np.pi/4)
H = np.array([1, 0]); V = np.array([0, 1])
psi = (np.kron(H, V)+np.kron(V, H))/np.sqrt(2)
tL = np.kron(J1, np.eye(2))@psi; tR = np.kron(J2, np.eye(2))@psi
c1 = J1@H/np.linalg.norm(J1@H); c2 = J1@V      # handedness behind the left plate for H and V input
# decompose tL in {circ} x {H,V}
for nm, t in [("left", tL), ("right", tR)]:
    comps = {f"{a}{b}": abs(np.vdot(np.kron(x, y), t))**2 for a, x in [("cH", c1), ("cV", c2)] for b, y in [("H", H), ("V", V)]}
    print(nm, {k: round(v, 3) for k, v in comps.items()})
print("handedness from H input behind left plate = same as V input behind right plate:", abs(abs(np.vdot(c1, J2@V))-1) < 1e-12)
ov = abs(np.vdot(tL, tR)); print(f"overlap of the two joint tag states = {ov:.2e}")
def red(t, keep):
    r = np.outer(t, t.conj()).reshape(2, 2, 2, 2)
    return np.einsum('ijkj->ik', r) if keep == 0 else np.einsum('jijk->ik', r)
for k, nm in [(0, "slit photon"), (1, "partner")]:
    print(f"{nm}: reduced state same for both slits: {np.allclose(red(tL, k), red(tR, k))}, = I/2: {np.allclose(red(tL, k), np.eye(2)/2)}")
# structure: left = c1 (x) V + c2 (x) H (each 1/2), right swapped
okL = abs(abs(np.vdot(np.kron(c1, V), tL))**2-0.5) < 1e-12 and abs(abs(np.vdot(np.kron(c2, H), tL))**2-0.5) < 1e-12
okR = abs(abs(np.vdot(np.kron(c2, V), tR))**2-0.5) < 1e-12 and abs(abs(np.vdot(np.kron(c1, H), tR))**2-0.5) < 1e-12
ok = okL and okR and ov < 1e-12 and all(np.allclose(red(tL, k), red(tR, k)) for k in (0, 1))
print("note: which handedness is called 'left-turning' is a convention; the structure (one handedness with V, the other with H, swapped between slits) is what is checked")
print("PASS" if ok else "FAIL")
