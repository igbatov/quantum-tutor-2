# Claims: "Squeeze the wave into a smaller space ... all the energies rise and the steps between them grow";
# "More wiggles, more energy"; "Their energies aren't spaced like a guitar's notes"; rungs crowd toward the top.
import sympy as sp
n, L, hbar, m = sp.symbols('n L hbar m', positive=True)
E = n**2*sp.pi**2*hbar**2/(2*m*L**2)   # particle in a box
dE = sp.simplify(E.subs(n, n+1) - E)
ok1 = sp.diff(E, L).is_negative and sp.simplify(sp.diff(dE, L)).is_negative
ok2 = sp.diff(E, n).is_positive
# hydrogen: E_n = -13.6/n^2 ; nodes = n-1 increase with energy; gaps shrink
import numpy as np
En = -13.6057/np.arange(1, 8)**2
gaps = np.diff(En)
ok3 = np.all(np.diff(En) > 0) and np.all(np.diff(gaps) < 0)
# guitar: f_n = n f1 -> equal gaps
fg = np.arange(1, 8); ok4 = np.allclose(np.diff(np.diff(fg)), 0)
print("box: dE/dL<0 and d(gap)/dL<0:", ok1, " dE/dn>0:", ok2)
print("H levels (eV):", np.round(En, 3), " gaps:", np.round(gaps, 3))
print("PASS" if ok1 and ok2 and ok3 and ok4 else "FAIL")
