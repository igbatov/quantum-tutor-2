# Claim: "two electrons can never share one state ... photons can pile into one state, which a laser exploits"
import sympy as sp
x1, x2 = sp.symbols('x1 x2')
phi = sp.Function('phi'); chi = sp.Function('chi')
anti_same = phi(x1)*phi(x2) - phi(x2)*phi(x1)        # fermions, both in phi
sym_same = phi(x1)*phi(x2) + phi(x2)*phi(x1)         # bosons, both in phi
print("fermions, same state (antisymmetric):", sp.simplify(anti_same))
print("bosons, same state (symmetric):", sp.simplify(sym_same))
# bosonic enhancement: emission into a mode with n photons goes as |<n+1|a^dag|n>|^2 = n+1
n = sp.symbols('n', nonnegative=True, integer=True)
print("stimulated-emission factor:", sp.sqrt(n+1)**2)
# filling levels: ground-state energies of Z non-interacting electrons in hydrogen-like levels (2n^2 per shell)
def fill(Z):
    E, left, k = 0, Z, 1
    while left: take = min(left, 2*k*k); E += take*(-1/k**2); left -= take; k += 1
    return E
print("Z=10: Pauli energy", fill(10), " vs all in n=1:", -10)
ok = sp.simplify(anti_same) == 0 and sp.simplify(sym_same) != 0 and fill(10) > -10
print("PASS" if ok else "FAIL")
