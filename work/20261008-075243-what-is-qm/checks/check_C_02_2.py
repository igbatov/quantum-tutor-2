# Claim: "then fainter and fainter lines crowding together at the violet edge"
# Model: emission power per line ~ g_n * A(n->2) * h nu (equal population per state, an optimistic case
# for high n); also absorption oscillator strengths f(2->n). Spacing between successive lines should shrink.
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
import sympy as sp
from sympy.physics.hydrogen import R_nl
from hcommon_C import *
r = sp.symbols('r', positive=True)
alpha = k.fine_structure; tau0 = k.hbar / k.physical_constants['Hartree energy'][0]
def rad(n, l, n2, l2): return float(sp.integrate(R_nl(n, l, r, 1) * R_nl(n2, l2, r, 1) * r**3, (r, 0, sp.oo)))
P = {}; f = {}
for n in range(3, 10):
    w = 0.5 * (1/4 - 1/n**2); tot = 0.0; fsum = 0.0
    for l in range(n):
        for l2 in (l - 1, l + 1):
            if 0 <= l2 < 2:
                A = (4/3) * w**3 * alpha**3 * max(l, l2) / (2*l + 1) * rad(n, l, 2, l2)**2 / tau0
                tot += (2*l + 1) * A
                # absorption 2 l2 -> n l, averaged over the 4 n=2 orbital states (weights 2l2+1)
                fsum += (2*l2 + 1) / 4 * (2/3) * w * max(l, l2) / (2*l2 + 1) * rad(n, l, 2, l2)**2
    P[n] = tot * w; f[n] = fsum
    print(f"n={n}: sum g*A = {tot:.3e} /s, relative power {tot*w/1:.3e}, f(2->n) = {fsum:.4f}, lambda {air_nm(vac_nm(n,2)):.1f} nm")
pw = [P[n] for n in range(3, 10)]; fs = [f[n] for n in range(3, 10)]
gaps = [air_nm(vac_nm(n, 2)) - air_nm(vac_nm(n+1, 2)) for n in range(3, 9)]
print("power ratios to H-alpha:", [round(p/pw[0], 4) for p in pw])
print("successive line spacings (nm):", [round(g, 1) for g in gaps])
ok = all(a > b for a, b in zip(pw, pw[1:])) and all(a > b for a, b in zip(fs, fs[1:])) and all(a > b for a, b in zip(gaps, gaps[1:]))
ok &= abs(fs[0] - 0.641) < 0.005  # known Balmer-alpha f
print("PASS" if ok else "FAIL")
