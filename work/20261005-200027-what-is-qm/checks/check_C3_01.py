# Claims: "tiny, heavy, positive nucleus with much lighter, negative electrons";
# "must circle the nucleus ... or they would fall straight in" (no static equilibrium, Earnshaw);
# "spiral into the nucleus in about a hundred-billionth of a second";
# "orbits could be any size ... a smooth smear of all colors"
import numpy as np, sympy as sp
from scipy.constants import physical_constants as pc, c, m_e, m_p, e, epsilon_0, pi
a0 = pc['Bohr radius'][0]; re = pc['classical electron radius'][0]; r_p = pc['proton rms charge radius'][0]
print(f"m_p/m_e = {m_p/m_e:.1f}; a0/r_p = {a0/r_p:.0f}")
ok1 = m_p/m_e > 1000 and a0/r_p > 1e4
# Earnshaw: Coulomb potential of the nucleus is harmonic away from r=0 -> no stable static point
x,y,z = sp.symbols('x y z', real=True); V = -1/sp.sqrt(x**2+y**2+z**2)
lap = sp.simplify(sum(sp.diff(V,s,2) for s in (x,y,z))); print("Laplacian of Coulomb potential:", lap)
ok2 = lap == 0
# Larmor collapse from a0: t = a0^3/(4 re^2 c)
t = a0**3/(4*re**2*c); print(f"collapse time = {t:.3e} s (claim: about 1e-11 s)")
ok3 = 0.3e-11 < t < 3e-11
# classical orbit frequency f = (1/2pi) sqrt(k/(m r^3)) is continuous in r -> any color
k = e**2/(4*pi*epsilon_0)
f = lambda r: np.sqrt(k/(m_e*r**3))/(2*pi)
rs = np.linspace(1,10,10001)*a0; lam = c/f(rs)*1e9
cover = lam.min() < 400 and lam.max() > 700 and np.all(np.diff(lam) > 0)
r400 = (k/m_e/(2*pi*c/400e-9)**2)**(1/3)/a0; r700 = (k/m_e/(2*pi*c/700e-9)**2)**(1/3)/a0
print(f"orbits {r400:.2f}-{r700:.2f} a0 radiate 400-700 nm continuously: {cover}")
print("PASS" if ok1 and ok2 and ok3 and cover else "FAIL")
