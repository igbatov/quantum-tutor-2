# Claims (quarter-wave plates, axes at +45 / -45): H -> circular, opposite handedness behind the two
# slits; V -> circular, swapped; "Diagonally polarized light ... unchanged, only delayed by a quarter
# wave behind one slit and not the other (and the other way round for the other diagonal)".
import numpy as np
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def qwp(t): return rot(t) @ np.diag([1, 1j]) @ rot(-t)    # fast axis at t, slow axis delayed by pi/2
J1, J2 = qwp(np.pi/4), qwp(-np.pi/4)                       # left slit +45, right slit -45
H = np.array([1, 0]); V = np.array([0, 1]); P = np.array([1, 1])/np.sqrt(2); M = np.array([1, -1])/np.sqrt(2)
Rc = np.array([1, 1j])/np.sqrt(2); Lc = np.array([1, -1j])/np.sqrt(2)
def hd(v): return "R" if abs(np.vdot(Rc, v))**2 > 1-1e-12 else ("L" if abs(np.vdot(Lc, v))**2 > 1-1e-12 else "?")
print("H: left", hd(J1@H), " right", hd(J2@H), "| V: left", hd(J1@V), " right", hd(J2@V))
ok = hd(J1@H) != hd(J2@H) and hd(J1@V) == hd(J2@H) and hd(J2@V) == hd(J1@H) and "?" not in hd(J1@H)+hd(J2@H)
for nm, v in [("+45", P), ("-45", M)]:
    o1, o2 = np.vdot(v, J1@v), np.vdot(v, J2@v)   # amplitude to stay in v (phase = delay)
    rel = np.degrees(np.angle(o2/o1))
    print(f"{nm}: unchanged pol: |<v|J1 v>|={abs(o1):.3f}, |<v|J2 v>|={abs(o2):.3f}; phase left {np.degrees(np.angle(o1)):+.0f} deg, right {np.degrees(np.angle(o2)):+.0f} deg; right-left {rel:+.0f} deg")
    ok &= abs(abs(o1)-1) < 1e-12 and abs(abs(o2)-1) < 1e-12 and abs(abs(rel)-90) < 1e-9
pl = np.angle(np.vdot(P, J1@P)); pr = np.angle(np.vdot(P, J2@P)); ml = np.angle(np.vdot(M, J1@M)); mr = np.angle(np.vdot(M, J2@M))
ok &= abs(pl) < 1e-12 and abs(mr) < 1e-12 and abs(pr-np.pi/2) < 1e-12 and abs(ml-np.pi/2) < 1e-12   # +45 delayed only right, -45 only left
print("PASS" if ok else "FAIL")
