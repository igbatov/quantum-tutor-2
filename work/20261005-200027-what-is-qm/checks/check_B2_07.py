# Claims: "very dim light delivers them almost always one at a time";
# "momentum (roughly, mass times velocity)"
import numpy as np
from scipy import constants as c
P, lam, win = 1e-12, 500e-9, 1e-9          # 1 pW at 500 nm, 1 ns detector resolving window
rate = P/(c.h*c.c/lam); mu = rate*win
pois = (1-np.exp(-mu)-mu*np.exp(-mu))/(1-np.exp(-mu))         # laser (Poisson)
th = (mu/(1+mu))**2/(1-1/(1+mu))                                # thermal (Bose-Einstein): P(>=2)/P(>=1) = mu/(1+mu)
print("photon rate %.3g /s, mean per ns %.3g; P(>=2 | >=1): laser %.2e, thermal %.2e" % (rate, mu, pois, th))
for v in [0.001, 0.01, 0.1]:
    g = 1/np.sqrt(1-v**2); print("v=%.3fc: p/(mv) = gamma = %.6f" % (v, g))
ok = pois < 0.01 and th < 0.01 and 1/np.sqrt(1-0.01**2)-1 < 1e-4
print("PASS" if ok else "FAIL")
