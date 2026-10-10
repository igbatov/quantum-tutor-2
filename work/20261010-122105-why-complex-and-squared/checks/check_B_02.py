# Claims: "glows in the ultraviolet at 254 nm, whose hf is 4.9 eV";
#  proton "42.6 MHz per tesla"; ammonia "2A/h approx 24 GHz";
#  Davisson-Germer "lambda = h/p ... 1.67e-10 m at 54 eV"; "k = 2 pi/lambda = p/hbar".
import numpy as np
import scipy.constants as sc

ok = True
E_254 = sc.h * sc.c / 253.7e-9 / sc.e
print(f"hc/253.7 nm = {E_254:.3f} eV (text 4.9 eV)"); ok &= abs(E_254 - 4.9) < 0.05

gp = sc.physical_constants['proton gyromag. ratio in MHz/T'][0]
print(f"proton gamma/2pi = {gp:.4f} MHz/T (text 42.6)"); ok &= abs(gp - 42.6) < 0.05
mu_p = sc.physical_constants['proton mag. mom.'][0]
dE = 2 * mu_p * 1.0
print(f"2 mu_p B / h at 1 T = {dE / sc.h / 1e6:.3f} MHz (text: E+ - E- = h x 42.6 MHz in magnitude)")
ok &= abs(dE / sc.h / 1e6 - 42.6) < 0.05

# Ammonia inversion: maser line NH3 (J,K)=(3,3) 23.870 GHz (literature reference, not CODATA)
f_nh3 = 23.8701e9
print(f"NH3 (3,3) inversion line {f_nh3/1e9:.3f} GHz vs text ~24 GHz"); ok &= abs(f_nh3 - 24e9) / 24e9 < 0.01

E = 54 * sc.e
p = np.sqrt(2 * sc.m_e * E)
lam = sc.h / p
print(f"lambda(54 eV electron) = {lam:.4e} m (text 1.67e-10)"); ok &= abs(lam - 1.67e-10) / 1.67e-10 < 3e-3
k = 2 * np.pi / lam
print("k - p/hbar relative:", abs(k - p / sc.hbar) / k); ok &= abs(k - p / sc.hbar) / k < 1e-12
print("PASS" if ok else "FAIL")
