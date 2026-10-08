# Claims: "hydrogen's energies crowd together toward the top, while a string's frequencies are evenly spaced"
# and figure spec E_n = -13.6/n^2 eV (-13.6, -3.40, -1.51, -0.85, -0.54, -0.38).
# Real-setup check: a real (stiff) guitar string has inharmonicity f_n = n f1 sqrt(1 + B n^2),
# B ~ 1e-5 .. 1e-4 for guitar strings (plain treble strings at the high end).
import numpy as np
from scipy.constants import physical_constants as pc
Ry = pc['Rydberg constant times hc in eV'][0]/(1+pc['electron-proton mass ratio'][0])
E = np.array([-Ry/n**2 for n in range(1,7)])
claimed = np.array([-13.6,-3.40,-1.51,-0.85,-0.54,-0.38])
print("E_n (eV):", np.round(E,3)); ok_levels = np.allclose(E, claimed, atol=0.006)
gaps = np.diff(E); print("H gaps (eV):", np.round(gaps,3)); ok_crowd = np.all(np.diff(gaps)<0)
# ideal string
n = np.arange(1,13); ok_ideal = np.allclose(np.diff(n*1.0), 1.0)
# real string
for B in [1e-5, 5e-5, 1e-4]:
    fn = n*np.sqrt(1+B*n**2)
    sp = np.diff(fn)
    print(f"B={B:g}: spacing f2-f1 = {sp[0]:.5f} f1, f12-f11 = {sp[-1]:.5f} f1, "
          f"mode 12 sharp by {1200*np.log2(fn[-1]/12):.1f} cents")
B = 5e-5; fn = n*np.sqrt(1+B*n**2); dev = np.max(np.abs(np.diff(fn)-1))
ok_real_even = dev < 1e-9
print(f"real string (B=5e-5) max deviation of spacing from f1 over modes 1-12: {dev:.2e} f1")
print("levels PASS" if ok_levels else "levels FAIL")
print("H crowding PASS" if ok_crowd else "H crowding FAIL")
print("ideal string evenly spaced:", ok_ideal)
print("string 'evenly spaced' as written for a real guitar string:", "PASS" if ok_real_even else
      "FAIL (nearly, not exactly, evenly spaced; spacing grows slightly with n)")
print("PASS" if ok_levels and ok_crowd and ok_real_even else "FAIL")
