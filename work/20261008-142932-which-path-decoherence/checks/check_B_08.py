# Claims: "a ten-micrometre grain is struck about 10^18 times per second" in sea-level air;
# "gone within about a billionth of a billionth of a second"; fig: 1 nm ~1e10/s, 100 nm ~1e14/s;
# vacuum "a millionth of a millibar, a billion times lower"; mean speed about 470 m/s.
import numpy as np
from scipy import constants as C
T = 293.15; m = 28.97*C.atomic_mass
vbar = np.sqrt(8*C.k*T/(np.pi*m)); n = 101325/(C.k*T)
print(f"mean speed = {vbar:.0f} m/s, number density = {n:.3e} /m^3")
def rate(D, n=2.5e25, v=470.):
    return n*v/4*4*np.pi*(D/2)**2
ok = True
for D, target in [(1e-9, 1e10), (100e-9, 1e14), (10e-6, 1e18)]:
    R = rate(D); print(f"D={D:.0e} m (diameter): rate = {R:.2e}/s  (target ~{target:.0e}); with radius=D: {rate(2*D):.2e}")
    ok &= abs(np.log10(R/target)) < 0.5
print(f"10 um: time between impacts = {1/rate(10e-6):.2e} s")
print(f"1e-6 mbar / 1013 mbar = {1e-6/1013.25:.2e}")
ok &= abs(vbar-470) < 20 and abs(np.log10(1/rate(10e-6)) + 18) < 0.5
print("PASS" if ok else "FAIL")
