# Caption claims: "four bright lines, plus fainter ones crowding toward 365 nm in the ultraviolet,
# just as the rungs crowd toward the top"; "line positions to scale, brightness only suggested";
# text: "a few bright, sharp colors, like a barcode"
import sympy as sp, numpy as np
from sympy.physics.hydrogen import R_nl
from scipy.constants import physical_constants as pc, k as kB, e
R_H = pc['Rydberg constant'][0]/(1+pc['electron-proton mass ratio'][0]); n_air = 1.000277
lam = lambda u: 1e9/(R_H*(0.25-1/u**2))/n_air
lim = 1e9/(R_H*0.25)/n_air; print(f"Balmer series limit {lim:.1f} nm (air)")
r = sp.symbols('r', positive=True)
def S(n):  # line strength n->2, summed over l,l' (units a0^2, spin omitted)
    tot = 0
    for l in range(n):
        for lp in (0,1):
            if abs(l-lp) == 1:
                I = sp.integrate(R_nl(n,l,r,1)*R_nl(2,lp,r,1)*r**3,(r,0,sp.oo))
                tot += max(l,lp)*float(I)**2
    return tot
Ry = 13.598
rows = []
for n in range(3,13):
    w = Ry*(0.25-1/n**2); s = S(n)
    P_eq = w**4*s                                   # equal population per state (optically thin)
    P_T = P_eq*np.exp(-Ry*(1-1/n**2)/(kB*10000/e))  # Boltzmann at 10,000 K
    rows.append((n, lam(n), P_eq, P_T))
P0 = rows[0][2]; PT0 = rows[0][3]
for n,l_,a,b in rows: print(f"n={n:2d} {l_:7.2f} nm  power(equal pop) {a/P0:.3f}  power(10^4 K) {b/PT0:.4f}")
eq = np.array([x[2] for x in rows]); bt = np.array([x[3] for x in rows])
ok_dec = np.all(np.diff(eq) < 0) and np.all(np.diff(bt) < 0)
ok_crowd = np.all(np.diff([x[1] for x in rows]) < 0) and rows[-1][1]-lim < 15
ok_4 = all(x[1] > 400 for x in rows[:4]) and all(x[1] < 400 for x in rows[4:])
print(f"brightness falls steadily line by line: {ok_dec}; Hdelta/Hepsilon = {eq[3]/eq[4]:.2f} (equal pop), "
      f"{bt[3]/bt[4]:.2f} (10^4 K)")
print("four lines above 400 nm, the rest between 365 and 400 nm crowding to the limit:", ok_4 and ok_crowd)
print("PASS" if ok_dec and ok_crowd and ok_4 else "FAIL")
