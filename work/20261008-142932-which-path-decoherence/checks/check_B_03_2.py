# Claims (dust grain, 10 µm across, Δx = 10 µm): sunlight "about 4 × 10^11 photons per second hit it",
# "a few millionths of a millionth of a second"; CMB "in about forty seconds for this grain";
# "almost all of its photons pass ... without scattering"; "each one that does scatter makes only about
# a thousandth of a full record"; "'about a second' is Joos and Zeh's figure for a grain twice as wide";
# figure caption "microwave background at Δx/λ ≈ 0.01 (about 1,400 scattering events needed)" and
# "the times in the text are this curve multiplied by each environment's own time between scattering events".
import numpy as np
from scipy import constants as C
from scipy.special import zeta, gamma
from math import factorial
# --- sunlight
Emean = (np.pi**4/30)/zeta(3)*C.k*5772
for S, lab in [(1000, "ground"), (1361, "above atmosphere")]:
    R = S/Emean*np.pi*(5e-6)**2
    print(f"sunlight {lab}: {R:.2e} photons/s hit; time {1/R*1e12:.1f} ps")
R = 1000/Emean*np.pi*(5e-6)**2
sun_ok = 2.5e11 < R < 6e11 and 1e-12 < 1/R < 1e-11
# --- CMB, Rayleigh scattering off a sphere radius a (perfect-reflector limit), Joos-Zeh
T = 2.7255; kt = C.k*T/(C.hbar*C.c)   # thermal wavenumber, 1/m
def Lam(a): return factorial(8)*8*zeta(9)*C.c*a**6/(9*np.pi)*kt**9                 # Joos-Zeh
def Gam(a): return C.c*(8*np.pi/3)*a**6/np.pi**2*gamma(7)*zeta(7)*kt**7              # ∫ n(k) c σ(k) dk, σ=(8π/3)k^4a^6
a, dx = 5e-6, 10e-6
t = 1/(Lam(a)*dx**2); t2 = 1/(Lam(10e-6)*dx**2)
G = Gam(a); frac = Lam(a)*dx**2/G
k2 = gamma(9)*zeta(9)/(gamma(7)*zeta(7))*kt**2       # <k^2> of the scattered photons (k^6 weighting)
lam_eff = 2*np.pi/np.sqrt(k2)
print(f"CMB: fading time a=5 µm: {t:.1f} s; grain twice as wide (a=10 µm): {t2:.2f} s")
print(f"CMB scatterings per second off the 10-µm grain: {G:.1f}/s; per-scattering record fraction Λ Δx²/Γ = {frac:.2e}"
      f" (= <k²>Δx²/3 = {k2*dx**2/3:.2e}); scatterings needed ≈ {1/frac:.0f}")
print(f"rms-wavenumber wavelength of scattered CMB photons: {lam_eff*1e3:.2f} mm")
ka = 2*np.pi*a/1e-3; print(f"σ/πa² at λ = 1 mm: {(8/3)*ka**4:.1e}  (almost all photons pass unscattered)")
# figure model: isotropic, λ = 1 mm smoothed ±30%, one-sided sinc
lam = np.linspace(0.7, 1.3, 2001)
Nfig = 1/np.mean(1-np.sinc(2*0.01/lam))
print(f"figure curve at Δx/λ=0.01: {Nfig:.0f} scattering events; × (1/Γ = {1/G:.2f} s) = {Nfig/G:.0f} s vs text 40 s")
cmb_time_ok = 20 < t < 60 and 0.3 < t2 < 2
thousandth_ok = 0.5e-3 < frac < 1.5e-3
fig_consistent = abs(Nfig/G - t)/t < 0.5
print("sunlight:", "PASS" if sun_ok else "FAIL")
print("CMB 40 s and 'about a second' for twice as wide:", "PASS" if cmb_time_ok else "FAIL")
print("'about a thousandth of a full record':", "PASS" if thousandth_ok else f"FAIL (computed {frac:.1e}, a few thousandths)")
print("figure 1,400 events × time between scatterings = text time:", "PASS" if fig_consistent else f"FAIL ({Nfig/G:.0f} s vs {t:.0f} s)")
