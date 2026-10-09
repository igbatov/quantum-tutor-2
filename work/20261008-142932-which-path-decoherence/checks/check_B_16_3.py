# Claims (final-B.md text + b-dust-grain caption): "about ten a second do scatter";
# "about one part in four hundred"; "forty seconds"; "mark is at 0.019 ... about 380 events";
# "naive position ... 0.01 ... about 1,400"; "effective wavelength is about 0.7 mm";
# "time (about a tenth of a second)"; "about 9% below the dashed line"; "dips to about 0.87 ... 0.7λ".
import numpy as np
from scipy import constants as C
from scipy.special import zeta, gamma
from scipy.optimize import brentq
from math import factorial
ok = {}
# --- full Joos-Zeh calculation, CMB on a grain of radius 5 µm, Δx = 10 µm
T = 2.7255; kt = C.k*T/(C.hbar*C.c)
a, dx = 5e-6, 10e-6
Lam = factorial(8)*8*zeta(9)*C.c*a**6/(9*np.pi)*kt**9
Gam = C.c*(8*np.pi/3)*a**6/np.pi**2*gamma(7)*zeta(7)*kt**7  # ∫ c σ(k) n(k) dk, σ=(8π/3)k^4 a^6, n(k)=k²/(π²(e^{ħck/kT}-1))
tfade = 1/(Lam*dx**2); frac = Lam*dx**2/Gam; N = 1/frac
ok_identity = abs(frac/(k2_tmp := gamma(9)*zeta(9)/(gamma(7)*zeta(7))*kt**2*dx**2/3) - 1) < 1e-9; print(f"record = <k²>Δx²/3 identity: {ok_identity}")
k2 = gamma(9)*zeta(9)/(gamma(7)*zeta(7))*kt**2; lam_eff = 2*np.pi/np.sqrt(k2)
print(f"full calc: Γ = {Gam:.2f}/s, 1/Γ = {1/Gam:.3f} s, record/scattering = {frac:.2e} = 1/{N:.0f}, "
      f"events = {N:.0f}, fading time = {tfade:.1f} s, Γ·t = {Gam*tfade:.0f}, λ_eff = {lam_eff*1e3:.2f} mm")
ok["~10 scatterings/s"] = 7 < Gam < 13
ok["~1/400 record each"] = abs(N/400 - 1) < 0.1 and 2e-3 < frac < 5e-3
ok["~40 s"] = abs(tfade/40 - 1) < 0.1
ok["~380 events"] = abs(N/380 - 1) < 0.05
ok["~0.1 s between events"] = abs(1/Gam/0.1 - 1) < 0.15
ok["λ_eff ≈ 0.7 mm"] = abs(lam_eff*1e3/0.7 - 1) < 0.05
# --- figure model (same as fig_b-dust-grain_3.py)
lam = np.linspace(0.7, 1.3, 1201)
curve = lambda x: 1/np.mean(1 - np.sinc(2*x/lam))
c019, c010 = curve(0.019), curve(0.01)
xmatch = brentq(lambda x: curve(x) - N, 0.005, 0.1)
print(f"figure curve: at 0.019 -> {c019:.0f} events; at 0.01 -> {c010:.0f}; curve equals full-calc {N:.0f} at Δx/λ = {xmatch:.4f}")
ok["mark at 0.019 reads ~380"] = abs(c019/380 - 1) < 0.05
ok["naive 0.01 reads ~1,400"] = abs(c010/1400 - 1) < 0.05
ok["0.019 is where curve = full calc"] = abs(xmatch - 0.019) < 0.001
ok["0.019 rounds to 'Δx/λ ≈ 0.02'"] = round(0.019, 2) == 0.02
ok["~380 events × 1/Γ ≈ 40 s"] = abs(c019/Gam/40 - 1) < 0.1
print(f"curve at mark × 1/Γ = {c019/Gam:.1f} s")
ratio = curve(0.01)/(6/(2*np.pi)**2/0.01**2)
xs = np.linspace(0.4, 1.2, 801); ys = [curve(x) for x in xs]; i = int(np.argmin(ys))
print(f"solid/dashed at small Δx: {ratio:.3f}; minimum {ys[i]:.3f} at Δx/λ = {xs[i]:.2f}")
ok["~9% below dashed"] = abs((1 - ratio) - 0.09) < 0.01
ok["dip ~0.87 near 0.7λ"] = abs(ys[i] - 0.87) < 0.01 and abs(xs[i] - 0.7) < 0.05
for k, v in ok.items(): print(("PASS" if v else "FAIL"), k)
print("PASS" if all(ok.values()) else "FAIL")
