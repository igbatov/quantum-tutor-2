# Claim: "spiral into the nucleus in about a hundred-billionth of a second, ... continuously changing smear of light"
import numpy as np
from scipy import constants as k
a0 = k.physical_constants['Bohr radius'][0]; re = k.physical_constants['classical electron radius'][0]
t_analytic = a0**3/(4*re**2*k.c)
# numeric: Larmor loss for circular orbit, dr/dt = -4 re^2 c / (3 r^2) * ... derive: E=-ke^2/2r, P=2 ke^2 a^2/(3c^3)... use dr/dt = -4 re^2 c/(3 r^2)*... check by integration
ke2 = k.e**2/(4*np.pi*k.epsilon_0)
from scipy.integrate import quad
def drdt(r):
    a = ke2/(k.m_e*r**2)
    P = 2*ke2*a**2/(3*k.c**3)          # Larmor power
    dEdr = ke2/(2*r**2)                # E = -ke2/(2r)
    return -P/dEdr
# t = integral_0^a0 dr/|dr/dt|, integrate in units of a0
t_num = quad(lambda x: a0/abs(drdt(x*a0)), 0, 1, epsabs=0, epsrel=1e-12)[0]
print(f"analytic t={t_analytic:.3e} s, numeric t={t_num:.3e} s")
# orbital frequency f = sqrt(ke2/(m r^3))/(2pi) changes continuously as r shrinks
r = np.linspace(a0, a0/100, 5); f = np.sqrt(ke2/(k.m_e*r**3))/(2*np.pi)
print("orbit freq (Hz) along spiral:", ["%.2e"%x for x in f], "monotonic:", np.all(np.diff(f) > 0))
ok = 0.3e-11 < t_num < 3e-11 and abs(t_num/t_analytic-1) < 1e-3 and np.all(np.diff(f) > 0)
print("PASS" if ok else "FAIL")
