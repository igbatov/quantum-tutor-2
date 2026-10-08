# Claims: "amplitude at a spot, squared, gives the chance"; "only certain patterns are steady ...
# one definite energy"; string "rings in a steady pattern only if the pattern fits: one hump, two, three";
# "2.5 humps would miss the pinned end"; "pressing a guitar string to a fret ... raises its note"
import sympy as sp, numpy as np
r,a0,t,E,hb = sp.symbols('r a0 t E hbar', positive=True)
psi = sp.exp(-r/a0)/sp.sqrt(sp.pi*a0**3)
norm = sp.integrate(4*sp.pi*r**2*psi**2,(r,0,sp.oo)); print("integral |psi_1s|^2 =", sp.simplify(norm))
Psi = psi*sp.exp(-sp.I*E*t/hb); ok_stat = not sp.simplify(Psi*sp.conjugate(Psi)).has(t)
E1,E2,f1,f2 = sp.symbols('E1 E2 f1 f2', positive=True)
S = f1*sp.exp(-sp.I*E1*t/hb)+f2*sp.exp(-sp.I*E2*t/hb); ok_mix = sp.simplify(sp.expand(S*sp.conjugate(S))).has(t)
print("single-energy pattern steady:", ok_stat, "; two-energy mix changes:", ok_mix)
# string modes: sin(k pi x) vanishes at x=1 only for whole k; hump count = k
x = np.linspace(0,1,200001)
for k in [1,2,3,2.5]:
    y = np.sin(k*np.pi*x); humps = np.sum(np.diff(np.sign(np.diff(y))) != 0)+0
    print(f"k={k}: value at pinned end = {y[-1]:+.3f}; turning points (humps) = {humps}")
ok_fit = all(abs(np.sin(k*np.pi))<1e-12 for k in [1,2,3]) and abs(np.sin(2.5*np.pi)-1)<1e-12
# "each with its own note": f_k = k v/(2L), distinct; fret: f1 = v/(2L) rises as L shrinks
L, v = sp.symbols('L v', positive=True); f1L = v/(2*L)
ok_fret = sp.diff(f1L, L).is_negative
print("df1/dL < 0 (shorter string, higher note):", ok_fret)
print("PASS" if sp.simplify(norm-1)==0 and ok_stat and ok_mix and ok_fit and ok_fret else "FAIL")
