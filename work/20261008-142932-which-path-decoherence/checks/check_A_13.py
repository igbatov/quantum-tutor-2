# Claim: dust grain: "air and sunlight write its position into the surroundings faster than
# any laboratory can resolve, by the standard estimates".
import numpy as np
from scipy.constants import k, atomic_mass as u, h, c
a = 10e-6; sigma = np.pi*a**2      # 10 um radius grain (Joos-Zeh / Schlosshauer standard example)
n_air = 101325/(k*300); v = np.sqrt(8*k*300/(np.pi*29*u))
rate_air = n_air*sigma*v           # each air collision is a perfect tag for dx >> 30 pm
flux_sun = 1000/(h*c/550e-9)       # photons /m^2/s
rate_sun = flux_sun*sigma
print(f"air: collision rate {rate_air:.1e} /s -> time {1/rate_air:.1e} s")
print(f"sunlight: scattering rate {rate_sun:.1e} /s -> time {1/rate_sun:.1e} s (for dx >~ 0.5 um)")
print("shortest time interval measured in a lab (Grundmann et al., Science 2020): ~2.5e-19 s")
print("Textbook table values (Joos-Zeh, Schlosshauer Table 3.2 style) quote ~1e-31 s for air, which uses the")
print("long-wavelength formula outside its range; the saturated estimate above is ~3e-19 s.")
print("UNVERIFIABLE: sunlight alone (~1e-12 s) is resolvable; air (~3e-19 s) is at the edge of zeptosecond metrology")
