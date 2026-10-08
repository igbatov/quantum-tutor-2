# Claims: "E_n = -13.6/n^2 eV ... (-13.6, -3.40, -1.51, -0.85, -0.54, -0.38)" (figure spec)
# and "hydrogen's energies crowd together toward the top, while a string's frequencies are evenly spaced"
import numpy as np
from scipy.constants import physical_constants as pc
Ry = pc['Rydberg constant times hc in eV'][0]
mu = 1/(1+pc['electron-proton mass ratio'][0])
E = np.array([-Ry*mu/n**2 for n in range(1,7)])
claimed = np.array([-13.6,-3.40,-1.51,-0.85,-0.54,-0.38])
print("computed", np.round(E,3))
ok1 = np.allclose(E, claimed, atol=0.006)
gaps = np.diff(E); print("H gaps", np.round(gaps,3))
ok2 = np.all(np.diff(gaps) < 0)
f = np.arange(1,7); ok3 = np.allclose(np.diff(f), 1)  # string f_n = n f_1, even spacing
print("levels PASS" if ok1 else "levels FAIL")
print("crowding/even-spacing PASS" if ok2 and ok3 else "crowding FAIL")
print("PASS" if ok1 and ok2 and ok3 else "FAIL")
