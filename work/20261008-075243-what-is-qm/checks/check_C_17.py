# Figure spec c-ladder-lines: strip over 380-700 nm, "glowing hydrogen ... four thin bright lines at 410, 434, 486 and 656 nm"
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from hcommon_C import *
inwin = [(n, air_nm(vac_nm(n, 2))) for n in range(3, 60) if 380 <= air_nm(vac_nm(n, 2)) <= 700]
print("Balmer lines inside 380-700 nm:", [(n, round(l, 1)) for n, l in inwin])
print("count:", len(inwin), "(spec says four)")
print("PASS" if len(inwin) == 4 else "FAIL")
