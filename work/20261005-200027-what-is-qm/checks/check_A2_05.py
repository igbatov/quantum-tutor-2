# Claim: "Air and light bouncing off big objects ... washing out their interference almost instantly"
# Joos-Zeh / Schlosshauer long-wavelength-limit scattering constant for air molecules:
#   Lambda = (8/(3 hbar^2)) (N/V) sqrt(2 pi m_air) a^2 (kT)^(3/2);  tau_D = 1/(Lambda dx^2) for dx << thermal wavelength of air,
#   saturating at the total collision rate for dx >> a (use collision rate as a conservative bound).
import numpy as np
from scipy import constants as c
T = 300; P = 101325; n = P/(c.k*T); m_air = 29*c.atomic_mass
vbar = np.sqrt(8*c.k*T/(np.pi*m_air))
for a in [1e-6, 1e-5, 1e-3]:   # grain radius (m)
    Lam = 8/(3*c.hbar**2)*n*np.sqrt(2*np.pi*m_air)*a**2*(c.k*T)**1.5
    lam_air = c.hbar/np.sqrt(2*m_air*c.k*T)
    tau_short = 1/(Lam*lam_air**2)            # at the shortest relevant separation (air thermal wavelength)
    tau_sat = 1/(n*np.pi*a**2*vbar)          # saturated: one collision resolves position
    print(f"grain radius {a:.0e} m: Lambda={Lam:.2e} m^-2 s^-1; tau(dx=air thermal wl {lam_air:.1e} m) = {tau_short:.1e} s; "
          f"tau(dx>=a, one collision) = {tau_sat:.1e} s")
ok = (1/(n*np.pi*(1e-6)**2*vbar)) < 1e-9
print("decoherence of a micron grain in air faster than a nanosecond:", "PASS" if ok else "FAIL")
