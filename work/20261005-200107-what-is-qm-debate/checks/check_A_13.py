# Claim: "Interference has been seen with ... even 2,000-atom molecules"
# Literature fact (Fein et al., Nature Physics 15, 1242 (2019): molecules up to ~2000 atoms, >25,000 amu).
# Cannot be computed; offline sanity check of the implied de Broglie wavelength only.
from scipy.constants import h, atomic_mass
m = 25000*atomic_mass; v = 250.0  # m/s, typical beam speed in that experiment
print(f"de Broglie wavelength ~ {h/(m*v):.2e} m (tens of femtometres)")
print("UNVERIFIABLE (literature claim; consistent with Fein et al. 2019)")
