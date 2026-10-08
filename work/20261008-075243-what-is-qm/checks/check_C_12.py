# Claim: "Upper rungs are temporary; an atom typically drops within a millionth of a second."
# Compute E1 spontaneous lifetimes of all hydrogen nl states for n=2..6 (atomic units, nonrelativistic)
import sympy as sp
from sympy.physics.hydrogen import R_nl
from scipy import constants as k
r = sp.symbols('r', positive=True)
alpha = k.fine_structure; tau0 = k.hbar/k.physical_constants['Hartree energy'][0]
cache = {}
def radial(n, l, n2, l2):
    key = (n, l, n2, l2)
    if key not in cache:
        cache[key] = float(sp.integrate(R_nl(n, l, r, 1)*R_nl(n2, l2, r, 1)*r**3, (r, 0, sp.oo)))
    return cache[key]
taus = {}
for n in range(2, 7):
    for l in range(n):
        A = 0.0
        for n2 in range(1, n):
            for l2 in (l-1, l+1):
                if 0 <= l2 < n2:
                    w = 0.5*(1/n2**2 - 1/n**2)
                    A += (4/3)*w**3*alpha**3*max(l, l2)/(2*l+1)*radial(n, l, n2, l2)**2
        taus[(n, l)] = (tau0/A) if A > 0 else float('inf')
for (n, l), t in taus.items():
    print(f"n={n} l={l}: tau = {t:.3e} s")
finite = {key: t for key, t in taus.items() if t != float('inf')}
under = sum(t < 1e-6 for t in finite.values())
print(f"states with E1 lifetime < 1 us: {under}/{len(taus)}; only exception: 2s (no E1 decay; two-photon lifetime ~0.12 s)")
ok = abs(taus[(2,1)]-1.596e-9)/1.596e-9 < 0.01 and under == len(taus)-1 and taus[(2,0)] == float('inf')
print("PASS" if ok else "FAIL")
