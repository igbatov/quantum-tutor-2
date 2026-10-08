# Claim: "a dipole pattern changes the details of the curve but not the half-wavelength scale"
import numpy as np
from scipy.integrate import dblquad
from scipy.optimize import brentq
def overlap(r, pattern, dvec):
    kd = 2*np.pi*r
    def g(th, ph):
        n = np.array([np.sin(th)*np.cos(ph), np.sin(th)*np.sin(ph), np.cos(th)])
        return pattern(n)*np.cos(kd*np.dot(n, dvec))*np.sin(th)
    return dblquad(lambda th, ph: g(th, ph), 0, 2*np.pi, 0, np.pi)[0]
lin = lambda n: 3/(8*np.pi)*(1-n[2]**2)          # linear dipole along z
circ = lambda n: 3/(16*np.pi)*(1+n[2]**2)        # circular (sigma) dipole, axis z
cases = {"linear, d along axis": (lin, [0,0,1]), "linear, d perp axis": (lin, [1,0,0]),
         "circular, d along axis": (circ, [0,0,1]), "circular, d perp axis": (circ, [1,0,0])}
ok = True
for name, (p, dv) in cases.items():
    norm = overlap(1e-9, p, np.array(dv, float))
    r = np.linspace(0.02, 2.0, 199)
    vals = np.array([overlap(x, p, np.array(dv, float)) for x in r])
    i = np.where(np.sign(vals[:-1]) != np.sign(vals[1:]))[0]
    z = brentq(lambda x: overlap(x, p, np.array(dv, float)), r[i[0]], r[i[0]+1]) if len(i) else None
    mn = vals.min(); print(f"{name}: norm={norm:.4f}, first zero d/lam={z}, min over 0..2 = {mn:.3f}, |V| at d=lam/2: {abs(overlap(0.5,p,np.array(dv,float))):.3f}")
    if z is None or not (0.35 < z < 0.75): ok = False
print("PASS (first zero stays within 0.35-0.75 lambda for all dipole cases)" if ok else "FAIL")
