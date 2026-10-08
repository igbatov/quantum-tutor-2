# Claims: "Air and light bouncing off big objects ... washing out their interference almost instantly";
# "well-isolated molecules of hundreds of atoms still make stripes"
import numpy as np
from scipy import constants as c
T, P = 300, 101325; n = P/(c.k*T); m_air = 29*c.atomic_mass; vbar = np.sqrt(8*c.k*T/(np.pi*m_air))
for a in [1e-7, 1e-6, 1e-5]:
    print(f"grain radius {a:.0e} m: time to first air collision {1/(n*np.pi*a**2*vbar):.1e} s")
print("decoherence of a micron grain in air < 1 ns:", "PASS" if 1/(n*np.pi*1e-12*vbar) < 1e-9 else "FAIL")
for name, m, v in [("C60 (60 atoms)", 720, 200), ("~800-atom molecule (Gerlich 2011, ~10,000 u)", 1e4, 100), ("~2,000-atom (Fein 2019, ~25,000 u)", 2.5e4, 250)]:
    lam = c.h/(m*c.atomic_mass*v); print(f"{name}: de Broglie wavelength {lam*1e15:.0f} fm")
print("molecules of hundreds of atoms interfering: UNVERIFIABLE by computation (empirical; consistent with published experiments)")
