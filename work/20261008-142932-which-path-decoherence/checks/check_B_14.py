# Claims: "the total number of arrivals is the same in all four panels"; dashed one-path sum "never moves";
# leftover pattern at V=0 is "the two one-path chances added"; damped wave "quarter of the strength (amplitude halved)".
import numpy as np
from scipy.integrate import quad
# far-screen, slit separation = 4 * width; u in stripe spacings; envelope sinc^2(pi u/4)
env = lambda u: np.sinc(u/4)**2
I = lambda u, V: env(u)*(1+V*np.cos(2*np.pi*u))
# integral of env*cos over the full screen: Fourier transform of sinc^2 is a triangle of half-width 1/4 < 1
L = 4000
tot = {V: quad(I, -L, L, args=(V,), limit=20000)[0] for V in [1, 0.7, 0.49, 0.343]}
print("full-screen totals:", {k: round(v, 4) for k, v in tot.items()})
win = {V: quad(I, -3, 3, args=(V,), limit=500)[0] for V in [1, 0.7, 0.49, 0.343]}
print("window -3..3 totals:", {k: round(v, 4) for k, v in win.items()})
same = max(tot.values())-min(tot.values()) < 1e-3*np.mean(list(tot.values()))
# one-path chances: each slit gives env(u)/2*... sum = env(u) -> I(u,0) == env
print("V=0 equals sum of one-path chances:", np.allclose(I(np.linspace(-3,3,101),0), env(np.linspace(-3,3,101))))
print("amplitude halved -> intensity factor", 0.5**2)
print("PASS" if same else "FAIL")
