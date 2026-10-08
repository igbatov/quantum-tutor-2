# Claim: "E = hf ... More energy means higher frequency: bluer light"; "the odds of finding it somewhere total 100%"
# fixes amplitude (normalization of a box state).
import sympy as sp
from scipy.constants import h, c, e
for lam in (656.3e-9, 486.1e-9, 434.0e-9, 410.2e-9):
    f = c/lam; print(f"lambda={lam*1e9:.1f} nm  f={f:.3e} Hz  E=hf={h*f/e:.3f} eV")
# compare with hydrogen level differences 13.6(1/4-1/n^2)
import numpy as np
dE = [13.6057*(1/4-1/n**2)/(1+1/1836.15) for n in (3, 4, 5, 6)]
print("Level differences (eV):", np.round(dE, 3))
x, L, A, n = sp.symbols('x L A n', positive=True)
nn = 2
Asol = sp.solve(sp.Eq(sp.integrate((A*sp.sin(nn*sp.pi*x/L))**2, (x, 0, L)), 1), A)
print("normalized amplitude A =", Asol)
Es = [h*c/l/e for l in (656.3e-9, 486.1e-9, 434.0e-9, 410.2e-9)]
ok = np.allclose(Es, dE, rtol=2e-3) and Asol == [sp.sqrt(2)/sp.sqrt(L)]
print("PASS" if ok else "FAIL")
