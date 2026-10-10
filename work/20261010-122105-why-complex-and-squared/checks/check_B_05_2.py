# Claims (spin worked + Check yourself + precession caption): "E_a = -hbar w/2 (along...)", "c_a = e^{+iwt/2}/sqrt2",
# "|c_a|^2 = 1/2, constant"; "+x" amplitude "= cos(wt/2)", chance "1/2(1 + cos wt)"; "-x" amplitude "i sin(wt/2)";
# "add to 1"; Check yourself: chance of +y "1/2(1 - sin wt)"; caption: tipped 60 deg, along = 0.5, transverse 0.866 cos(2pi t/T).
import sympy as sp, numpy as np
from scipy.integrate import solve_ivp
t, w, hb = sp.symbols('t omega hbar', positive=True)
Ea, Eb = -hb*w/2, hb*w/2
ca, cb = sp.exp(sp.I*w*t/2)/sp.sqrt(2), sp.exp(-sp.I*w*t/2)/sp.sqrt(2)
ok = sp.simplify(sp.I*hb*sp.diff(ca, t) - Ea*ca) == 0 and sp.simplify(sp.I*hb*sp.diff(cb, t) - Eb*cb) == 0
ok &= sp.simplify(ca*sp.conjugate(ca) - sp.Rational(1,2)) == 0
apx, amx = (ca+cb)/sp.sqrt(2), (ca-cb)/sp.sqrt(2)
ok &= sp.simplify((apx - sp.cos(w*t/2)).rewrite(sp.exp)) == 0
ok &= sp.simplify((amx - sp.I*sp.sin(w*t/2)).rewrite(sp.exp)) == 0
ok &= sp.simplify(sp.cos(w*t/2)**2 - (1+sp.cos(w*t))/2) == 0
ok &= sp.simplify(sp.expand(apx*sp.conjugate(apx) + amx*sp.conjugate(amx))) == 1
apy = sp.conjugate(1/sp.sqrt(2))*ca + sp.conjugate(sp.I/sp.sqrt(2))*cb
Py = sp.simplify(sp.expand(apy*sp.conjugate(apy)).rewrite(sp.cos))
print("P(+y) =", Py); okY = sp.simplify(Py - (1 - sp.sin(w*t))/2) == 0
print("Check-yourself P(+y) = 1/2(1 - sin wt):", okY); ok &= okY
# first -y (P(+y)=0) at wt = pi/2 (T/4), first +y at wt = 3pi/2 (3T/4)
s = np.linspace(1e-6, 2*np.pi, 200001); P = 0.5*(1-np.sin(s))
t_my, t_py = s[np.argmin(P)], s[np.argmax(P)]
print("first -y at wt =", t_my/np.pi, "pi; first +y at wt =", t_py/np.pi, "pi")
ok &= abs(t_my-np.pi/2)<1e-3 and abs(t_py-1.5*np.pi)<1e-3
# physical consistency: proton (gamma>0), dM/dt = gamma M x B, B along z, M(0) along x -> goes to -y first
f = lambda tt, M: np.cross(M, [0, 0, 1.0])
sol = solve_ivp(f, [0, np.pi/2], [1, 0, 0], rtol=1e-10, atol=1e-12)
print("Bloch, gamma B = 1, M at t = T/4:", np.round(sol.y[:, -1], 6)); ok &= np.allclose(sol.y[:, -1], [0, -1, 0], atol=1e-6)
# caption: tipped 60 deg; <s_z> stays cos60, <s_x> = sin60 cos(wt)
th = np.pi/3; psi0 = np.array([np.cos(th/2), np.sin(th/2)], complex)
sx = np.array([[0,1],[1,0]]); sz = np.diag([1,-1])
for tt in np.linspace(0, 5*2*np.pi, 11):
    U = np.diag([np.exp(1j*tt/2), np.exp(-1j*tt/2)]); ps = U @ psi0
    ok &= abs(np.vdot(ps, sz@ps).real - 0.5) < 1e-12 and abs(np.vdot(ps, sx@ps).real - np.sin(th)*np.cos(tt)) < 1e-12
print("sin 60 =", np.sin(th))
print("PASS" if ok else "FAIL")
