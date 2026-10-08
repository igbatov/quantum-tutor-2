# Claim: dust grain "some ten micrometres across in ordinary air, each air molecule that hits it is a
# near-perfect tag ...; the standard estimate ... far less than a millionth of a billionth of a second".
import numpy as np
from scipy.constants import k, atomic_mass as u, h
T = 300; a = 5e-6                       # 10 um across -> radius 5 um
for rad in [5e-6, 10e-6]:
    n = 101325/(k*T); v = np.sqrt(8*k*T/(np.pi*29*u)); rate = n*np.pi*rad**2*v
    print(f"radius {rad*1e6:.0f} um: collision rate {rate:.1e}/s -> time between perfect tags {1/rate:.1e} s")
lam_air = h/np.sqrt(3*29*u*k*T); print(f"air molecule wavelength {lam_air*1e12:.0f} pm vs grain width 10 um: ratio {10e-6/lam_air:.0e}")
t_max = 1/(101325/(k*T)*np.pi*a**2*np.sqrt(8*k*T/(np.pi*29*u)))
print(f"longest estimate {t_max:.1e} s vs 1e-15 s: factor {1e-15/t_max:.0f} shorter")
print("PASS" if (t_max < 1e-16 and 10e-6/lam_air > 1e4) else "FAIL")
