# Claim: CMB "does it by sheer numbers in about a second by the Joos-Zeh estimate" for a grain
# "ten micrometres across", separation Δx = 10 um. Long-wavelength formula (Joos-Zeh; Schlosshauer eq. 3.73):
# Lambda = 8! * 8 zeta(9) c a^6 / (9 pi) * (kT/(hbar c))^9, rate = Lambda Δx^2, a = grain RADIUS.
import numpy as np
from scipy import constants as C
from scipy.special import zeta
from math import factorial
T = 2.7255
def Lam(a): return factorial(8)*8*zeta(9)*C.c*a**6/(9*np.pi)*(C.k*T/(C.hbar*C.c))**9
for a, dx, lab in [(10e-6, 10e-6, "Joos-Zeh grain a=1e-3 cm (20 um across), dx=a"),
                   (5e-6, 10e-6, "text grain: 10 um across (a=5 um), dx=10 um")]:
    L = Lam(a); r = L*dx**2
    print(f"{lab}: Lambda = {L*1e-4:.2e} cm^-2 s^-1, rate = {r:.3f}/s, time = {1/r:.1f} s")
lam_th = 2*np.pi*C.hbar*C.c/(C.k*T)
print(f"CMB thermal wavelength 2*pi*hbar*c/kT = {lam_th*1e3:.2f} mm; Wien peak {C.h*C.c/(4.965*C.k*T)*1e3:.2f} mm; dx/lambda = {10e-6/1e-3:.2f}")
t_text = 1/(Lam(5e-6)*(10e-6)**2)
print(f"for the grain as described: {t_text:.0f} s (about {t_text/60:.1f} min); dielectric factor ((eps-1)/(eps+2))^2 < 1 would make it longer")
print("FAIL ('about a second' is Joos-Zeh's figure for a grain of radius 10 um; for a 10-um-across grain it is ~40 s)" if t_text > 10 else "PASS")
