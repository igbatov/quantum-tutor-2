# Claims: "orbits could be any size ... a smooth smear of all colors" (classical prediction)
# A classical electron on a circular orbit of radius r radiates at its orbital frequency
# f = (1/2pi) sqrt(k/(m r^3)), continuous in r -> every visible wavelength is produced by some orbit size.
import numpy as np
from scipy.constants import e, epsilon_0, m_e, c, physical_constants as pc
k = e**2/(4*np.pi*epsilon_0); a0 = pc['Bohr radius'][0]
f = lambda r: np.sqrt(k/(m_e*r**3))/(2*np.pi)
lam = lambda r: c/f(r)
for lt in [400e-9, 550e-9, 700e-9]:
    r = (k/m_e)**(1/3)*(lt/(2*np.pi*c))**(2/3)
    print(f"orbit radius emitting {lt*1e9:.0f} nm: {r/a0:.2f} a0 (check: {lam(r)*1e9:.1f} nm)")
rs = np.linspace(1,20,100001)*a0
L = lam(rs)*1e9
gaps = np.max(np.diff(np.sort(L[(L>400)&(L<700)])))
print(f"max gap between emitted wavelengths in 400-700 nm over a fine grid of radii: {gaps:.4f} nm (continuous)")
print("PASS" if L.min()<400 and L.max()>700 and gaps<0.1 else "FAIL")
