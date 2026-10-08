# Claim: "four narrow lines, red (656 nm), blue-green (486 nm), blue-violet (434 nm) and violet (410 nm), more in the ultraviolet and infrared"
# Claim: "Rung 3 to rung 2 is the red line, 4 to 2 the blue-green, 5 and 6 to 2 the violets; drops to rung 1 are ultraviolet"
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from hcommon_C import *
ok = True
claimed = {3:656, 4:486, 5:434, 6:410}
for n, c in claimed.items():
    v = vac_nm(n,2); a = air_nm(v)
    good = abs(a-c) < 1.0
    ok &= good
    print(f"{n}->2: vac {v:.2f} nm, air {a:.2f} nm, claimed {c}: {'ok' if good else 'BAD'}")
balmer = [(n, air_nm(vac_nm(n,2))) for n in range(3,40)]
vis = [b for b in balmer if b[1] >= 400]
print("Balmer lines >= 400 nm (ISO visible/UV boundary):", [(n, round(l,1)) for n,l in vis])
ok &= len(vis) == 4
uv = [b for b in balmer if b[1] < 400]
print("Balmer lines < 400 nm (UV): count", len(uv), "first", [(n, round(l,1)) for n,l in uv[:3]], "limit", round(air_nm(1e9/R_M(m_p)*4),1))
lyman = [vac_nm(n,1) for n in range(2,50)]
print("Lyman (to rung 1) longest:", round(max(lyman),1), "nm; all < 400:", max(lyman) < 400)
ok &= max(lyman) < 400
pas = [vac_nm(n,3) for n in range(4,50)]
print("Paschen (to rung 3) range nm:", round(min(pas)), "-", round(max(pas)), "all > 700:", min(pas) > 700)
ok &= min(pas) > 700
print("PASS" if ok else "FAIL")
