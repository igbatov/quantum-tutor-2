# Claims: atom -> "only certain steady patterns fit, each with one fixed energy";
# "color fixed by the energy difference"; "lowest pattern with nothing below it"
# Numerical: hydrogen radial Schrodinger equation (l=0), atomic units, finite differences.
import numpy as np
from scipy.linalg import eigh_tridiagonal
from scipy.constants import h, c, e, physical_constants
N, rmax = 20000, 400.0
r = np.linspace(rmax/N, rmax, N); dr = r[1]-r[0]
d = 1/dr**2 - 1/r; off = -0.5/dr**2*np.ones(N-1)
E = eigh_tridiagonal(d, off, select='i', select_range=(0, 5))[0]
Ha = physical_constants['Hartree energy in eV'][0]
print("lowest l=0 energies (eV):", np.round(E*Ha, 4))
exact = -Ha/2/np.arange(1, 7)**2
print("Bohr -13.6/n^2 (eV):     ", np.round(exact, 4))
ok1 = np.allclose(E[:4]*Ha, exact[:4], rtol=2e-3)
# Balmer lines from energy differences (reduced-mass-corrected Rydberg)
Ry = physical_constants['Rydberg constant times hc in eV'][0]
mu = 1/(1+physical_constants['electron-proton mass ratio'][0])
for n in [3, 4, 5]:
    dE = Ry*mu*(1/4 - 1/n**2)
    print(f"H {n}->2: dE={dE:.4f} eV, vacuum lambda = {h*c/(dE*e)*1e9:.2f} nm")
lamHa = h*c/(Ry*mu*(1/4-1/9)*e)*1e9
ok2 = abs(lamHa - 656.47) < 0.1   # H-alpha vacuum wavelength 656.47 nm
ok3 = E[0] == E.min() and E[0]*Ha > -14  # bounded below, ground state ~ -13.6 eV
print("PASS" if ok1 and ok2 and ok3 else "FAIL")
