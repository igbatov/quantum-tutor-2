# Claim: "in full sunlight with no air, roughly 10^11 photons per second scatter off it, and the
# time is a few millionths of a millionth of a second" (10 um grain).
import numpy as np
from scipy import constants as C
from scipy.special import zeta
Tsun = 5772
Emean = (np.pi**4/30)/zeta(3)*C.k*Tsun   # mean photon energy of black body = 2.701 kT
print(f"mean photon energy = {Emean/C.e:.2f} eV")
for S, lab in [(1361, "top of atmosphere"), (1000, "ground, full sun")]:
    flux = S/Emean
    for D in [10e-6]:
        sig = np.pi*(D/2)**2
        R = flux*sig
        print(f"{lab}: photon flux {flux:.2e}/m^2/s, geometric cross-section {sig:.2e} m^2, rate {R:.2e}/s, time {1/R*1e12:.1f} ps (x2 for extinction 2*pi*a^2: rate {2*R:.1e})")
R = 1000/Emean*np.pi*(5e-6)**2
print(f"text: rate 1e11 -> time {1/1e11*1e12:.0f} ps; computed rate {R:.1e} (log10 {np.log10(R):.2f}) -> {1/R*1e12:.1f} ps")
rate_ok = abs(np.log10(R) - 11) < 0.3
time_ok = 1e-12 <= 1/R < 1e-11
print("rate 'roughly 1e11':", "PASS" if rate_ok else "FAIL", "| time 'a few ps':", "PASS" if time_ok else "FAIL")
print("FAIL (rate ~4e11, i.e. a few times 1e11; time a few ps is right)" if not rate_ok else "PASS")
