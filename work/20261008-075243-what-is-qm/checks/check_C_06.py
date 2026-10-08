# Claim: "spiral into the nucleus in about a hundred-billionth of a second, ... continuously changing smear of light"
import numpy as np
from scipy import constants as k
from scipy.integrate import solve_ivp
a0 = k.physical_constants['Bohr radius'][0]; re = k.physical_constants['classical electron radius'][0]
t_analytic = a0**3/(4*re**2*k.c)
# numeric: Larmor loss for circular orbit, dr/dt = -4 re^2 c / (3 r^2) * ... derive: E=-ke^2/2r, P=2 ke^2 a^2/(3c^3)... use dr/dt = -4 re^2 c/(3 r^2)*... check by integration
ke2 = k.e**2/(4*np.pi*k.epsilon_0)
def rhs(t, r):
    a = ke2/(k.m_e*r[0]**2)
    P = 2*ke2*a**2/(3*k.c**3)
    dEdr = ke2/(2*r[0]**2)
    return [-P/dEdr]
ev = lambda t, r: r[0]-1e-15; ev.terminal = True
sol = solve_ivp(rhs, [0, 1e-9], [a0], events=ev, rtol=1e-10, atol=1e-25)
t_num = sol.t_events[0][0]
print(f"analytic t={t_analytic:.3e} s, numeric t={t_num:.3e} s")
# orbital frequency f = sqrt(ke2/(m r^3))/(2pi) changes continuously as r shrinks
r = np.linspace(a0, a0/100, 5); f = np.sqrt(ke2/(k.m_e*r**3))/(2*np.pi)
print("orbit freq (Hz) along spiral:", ["%.2e"%x for x in f], "monotonic:", np.all(np.diff(f) > 0))
ok = 0.3e-11 < t_num < 3e-11 and abs(t_num/t_analytic-1) < 1e-3 and np.all(np.diff(f) > 0)
print("PASS" if ok else "FAIL")
