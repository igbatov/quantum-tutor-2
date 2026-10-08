# Claims (Model 1 / Model 2, photon pair): "the partner's diagonal polarizer ...: its result is 50/50
# whichever slit was used"; "the slit photon that goes with each result has the same diagonal
# polarization whichever slit it used, differing only by the plates' quarter-wave delay";
# Model 2: "In the +45 group the slit photon's polarization is the same diagonal as its partner's";
# "In the -45 group the delay is behind the other slit".
import numpy as np
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def qwp(t): return rot(t) @ np.diag([1, 1j]) @ rot(-t)
H = np.array([1, 0]); V = np.array([0, 1]); J1, J2 = qwp(np.pi/4), qwp(-np.pi/4)
P = np.array([1, 1])/np.sqrt(2); M = np.array([1, -1])/np.sqrt(2)
psi = (np.kron(H, V)+np.kron(V, H))/np.sqrt(2)
ok = True
for pn, pv in [("+45", P), ("-45", M)]:
    cond = np.kron(np.eye(2), pv.conj()) @ psi          # slit-photon state given partner result (unnormalized)
    prob = np.vdot(cond, cond).real
    same = abs(np.vdot(pv, cond/np.sqrt(prob)))**2
    sl, sr = J1@cond/np.sqrt(prob), J2@cond/np.sqrt(prob)
    pl = np.angle(np.vdot(pv, sl)); pr = np.angle(np.vdot(pv, sr))
    for slitname, J in [("left", J1), ("right", J2)]:
        p_given = np.vdot(np.kron(J, np.eye(2))@psi, np.kron(np.eye(2), np.outer(pv, pv))@np.kron(J, np.eye(2))@psi).real
        print(f"P(partner {pn} | {slitname} slit) = {p_given:.3f}")
        ok &= abs(p_given-0.5) < 1e-12
    print(f"partner {pn}: slit photon in same diagonal with prob {same:.3f}; after plates |<{pn}|left>|={abs(np.vdot(pv, sl)):.3f}, |<{pn}|right>|={abs(np.vdot(pv, sr)):.3f}; phase left {np.degrees(pl):+.0f}, right {np.degrees(pr):+.0f} deg, relative {np.degrees(np.angle(np.vdot(pv, sr)/np.vdot(pv, sl))):+.0f} deg")
    ok &= abs(same-1) < 1e-12 and abs(abs(np.vdot(pv, sl))-1) < 1e-12 and abs(abs(np.vdot(pv, sr))-1) < 1e-12 and abs(abs(np.degrees(np.angle(np.vdot(pv, sr)/np.vdot(pv, sl))))-90) < 1e-9
print("PASS" if ok else "FAIL")
