# Claim: "Of all the powers, fractional ones included, only the second keeps the total at
# exactly 1 for every angle; any smaller positive power overshoots ..., any larger one undershoots, worst at 45°."
import numpy as np, sympy as sp
p = sp.symbols('p', real=True)
sol = sp.solve(sp.Eq(2*(sp.sqrt(2)/2)**p, 1), p)
print("p with total 1 at 45°:", sol)
ok = sol == [2]
th = np.linspace(1e-3, np.pi/2 - 1e-3, 4001)
for P in np.concatenate([np.linspace(0.05, 6, 1191), [1.9, 1.99, 2.01, 2.1]]):
    if abs(P - 2) < 1e-12: continue
    S = np.cos(th)**P + np.sin(th)**P
    over = np.all(S > 1) if P < 2 else np.all(S < 1)
    worst = abs(th[np.argmax(np.abs(S - 1))] - np.pi/4) < 1e-3
    if not (over and worst):
        ok = False; print("violation at p =", P)
S2 = np.cos(th)**2 + np.sin(th)**2
ok &= np.max(np.abs(S2 - 1)) < 1e-14
print("p=1.9 at 45°:", 2*np.cos(np.pi/4)**1.9, " p=2.1:", 2*np.cos(np.pi/4)**2.1)
print("PASS" if ok else "FAIL")
