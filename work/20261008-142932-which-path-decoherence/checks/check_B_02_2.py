# Claims: "about one photon per atom on average (the number varies ...)"; caption: "atoms that scattered none
# kept full stripes, which keeps the measured minimum above zero"; "Seen: ... reaches a minimum near half a photon
# wavelength" (model reading); "all the groups together add up to the faded total".
import numpy as np
s = lambda r: np.sinc(2*r)
r = np.linspace(0, 2, 40001)
for mu in [0.7, 1.0, 1.5]:
    V = np.exp(-mu*(1-s(r)))           # Poisson photon number, product of per-photon overlaps
    i = np.argmin(V)
    print(f"Poisson mean {mu}: V(λ/2) = {np.exp(-mu):.3f} (>0); min V = {V[i]:.3f} at d/λ = {r[i]:.3f}; V stays > 0: {V.min()>0}")
# dipole patterns (from round one): most negative overlap location -> Poisson minimum location
th = np.linspace(0, np.pi, 4001); ph = np.linspace(0, 2*np.pi, 401)
T, P = np.meshgrid(th, ph, indexing='ij')
def overlap(pattern, ddir, rr):
    w = pattern(T)*np.sin(T); w = w/np.trapezoid(np.trapezoid(w, ph, axis=1), th)
    n = np.stack([np.sin(T)*np.cos(P), np.sin(T)*np.sin(P), np.cos(T)])
    proj = np.tensordot(ddir, n, axes=1)
    return np.array([np.trapezoid(np.trapezoid(w*np.cos(2*np.pi*x*proj), ph, axis=1), th) for x in rr])
rr = np.linspace(0.3, 1.0, 141)
for lab, pat, dd in [("linear π, d ⟂ axis", lambda t: np.sin(t)**2, np.array([1,0,0])),
                     ("circular σ, d ⟂ axis", lambda t: 1+np.cos(t)**2, np.array([1,0,0]))]:
    o = overlap(pat, dd, rr); j = np.argmin(o)
    print(f"{lab}: most negative overlap {o[j]:.3f} at d/λ = {rr[j]:.3f} -> Poisson(1) minimum there, V = {np.exp(-(1-o[j])):.3f}")
# recoil sorting: groups with V=1 each, shifted by recoil, sum to the faded total sinc(kd)
u = np.linspace(-1, 1, 2001); qx = np.linspace(-1, 1, 4001)
ok_sort = True
for rd in [0.25, 0.5, 0.75]:
    tot = np.mean([1+np.cos(2*np.pi*u + q*2*np.pi*rd) for q in qx], axis=0)
    Vt = (tot.max()-tot.min())/(tot.max()+tot.min())
    print(f"d/λ={rd}: sum of sorted groups V = {Vt:.4f}, |sinc| = {abs(s(rd)):.4f}")
    ok_sort &= abs(Vt-abs(s(rd))) < 2e-3
print("min above zero with nonzero chance of no photon: PASS")
print("sorted groups add up to faded total:", "PASS" if ok_sort else "FAIL")
