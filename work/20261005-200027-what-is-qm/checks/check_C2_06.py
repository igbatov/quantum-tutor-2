# Claims: "glowing hydrogen gives off only a few sharp colors, like a barcode";
# figure spec: strip over 400-700 nm with exactly four lines (410.2, 434.0, 486.1, 656.3) "as actually seen".
# Full model: the Balmer series continues below 400 nm, converging at ~364.6 nm.
import numpy as np
from scipy.constants import physical_constants as pc
R_H = pc['Rydberg constant'][0]/(1+pc['electron-proton mass ratio'][0]); n_air = 1.000277
bal = {u: 1e9/(R_H*(1/4-1/u**2))/n_air for u in range(3,15)}
print("Balmer lines (air, nm):", {u: round(v,1) for u,v in bal.items()})
print(f"series limit: {1e9/(R_H/4)/n_air:.1f} nm")
in_400_700 = [u for u,v in bal.items() if 400<=v<=700]
in_380_400 = [u for u,v in bal.items() if 380<=v<400]
print("lines in 400-700 nm:", in_400_700, "; lines in 380-400 nm (edge of vision):", in_380_400)
# Paschen limit (IR) check: nothing from drops to rung 3 is visible
print(f"Paschen series limit {1e9/(R_H/9):.0f} nm (infrared)")
ok_few = len([v for v in bal.values() if v>380]) < 10
print("text 'only a few sharp colors':", "PASS" if ok_few else "FAIL")
print("figure 'four lines over 400-700' hides the fainter lines just below 400 nm:",
      "FAIL" if in_380_400 else "PASS")
print("FAIL" if in_380_400 else "PASS")
