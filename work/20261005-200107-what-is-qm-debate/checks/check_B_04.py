# Claim: "E = hf ... a fixed energy gap means a fixed frequency"; check dimensions and
# that the 3->2 gap (1.89 eV) gives f ~ 4.57e14 Hz -> 656 nm.
import sympy as sp
from scipy import constants as C
from sympy.physics.units import joule, second, hertz, convert_to, kilogram, meter
h_dim = joule*second
E_dim = sp.simplify(convert_to(h_dim*hertz, [kilogram, meter, second]))
ok_dim = sp.simplify(E_dim - convert_to(joule, [kilogram, meter, second])) == 0
gap = 13.6057*(1/4-1/9)*C.e
f = gap/C.h
lam = C.c/f*1e9
print(f"[h*f] = {E_dim}  (joule in SI base): {ok_dim}")
print(f"3->2 gap {gap/C.e:.4f} eV -> f = {f:.4e} Hz -> lambda = {lam:.1f} nm (vacuum)")
print("PASS" if ok_dim and abs(lam-656.5) < 1 else "FAIL")
