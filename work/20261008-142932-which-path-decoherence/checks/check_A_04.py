# Claims: quarter-wave plates at +45 and -45 deg: "light polarized along either of its axes
# passes ... unchanged"; "Horizontally polarized light leaves circularly polarized ... one way
# behind the left slit and the other way behind the right"; "vertically ... handednesses swapped".
import numpy as np
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def qwp(t): return rot(t) @ np.diag([1, 1j]) @ rot(-t)   # fast axis at angle t
H = np.array([1, 0]); V = np.array([0, 1])
R = np.array([1, 1j])/np.sqrt(2); L = np.array([1, -1j])/np.sqrt(2)
def handed(v):
    pR, pL = abs(np.vdot(R, v))**2, abs(np.vdot(L, v))**2
    return "R" if pR > 1-1e-12 else ("L" if pL > 1-1e-12 else f"not circular (R={pR:.3f})")
J1, J2 = qwp(np.pi/4), qwp(-np.pi/4)
ok = True
for name, J in [("+45 plate", J1), ("-45 plate", J2)]:
    for ang in [np.pi/4, -np.pi/4]:
        v = np.array([np.cos(ang), np.sin(ang)]); out = J @ v
        unchanged = abs(abs(np.vdot(v, out)) - 1) < 1e-12
        ok &= unchanged
        print(f"{name}: axis-polarized {np.degrees(ang):+.0f} deg unchanged: {unchanged}")
hL, hR_ = handed(J1 @ H), handed(J2 @ H); vL, vR = handed(J1 @ V), handed(J2 @ V)
print("H behind +45 plate:", hL, " behind -45 plate:", hR_)
print("V behind +45 plate:", vL, " behind -45 plate:", vR)
ok &= hL in "RL" and hR_ in "RL" and hL != hR_ and vL == hR_ and vR == hL
print("overlap of the two tags for H input:", abs(np.vdot(J1@H, J2@H)))
print("PASS" if ok else "FAIL")
