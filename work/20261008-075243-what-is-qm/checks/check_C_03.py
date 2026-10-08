# Claim: "(Ordinary hydrogen; heavy hydrogen's lines sit slightly apart.)"
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from hcommon_C import *
h = air_nm(vac_nm(3,2,m_p)); d = air_nm(vac_nm(3,2,m_d))
print(f"H-alpha {h:.3f} nm, D-alpha {d:.3f} nm, shift {h-d:.3f} nm ({(h-d)/h:.2e} fractional)")
ok = 0.05 < h-d < 1.0
print("PASS" if ok else "FAIL")
