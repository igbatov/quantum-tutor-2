# Claims: "four bright narrow lines, red (656 nm) ... violet (410 nm)", "fainter lines ... (397, 389, 384 nm)",
# "7, 8 and 9 to 2 the faint lines at the violet edge", "further sets ... deep ultraviolet and the infrared",
# "drops to rung 1 are ultraviolet", Bohr reproduces "ionized helium", Heisenberg entry = difference of clock rates.
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from hcommon_C import *
ok = True
quoted = {3: 656, 4: 486, 5: 434, 6: 410, 7: 397, 8: 389, 9: 384}
for n, q in quoted.items():
    a = air_nm(vac_nm(n, 2)); good = abs(a - q) < 0.6; ok &= good
    print(f"{n}->2: air {a:.2f} nm (quoted {q}) {'ok' if good else 'MISMATCH'}")
vis = [n for n in range(3, 60) if air_nm(vac_nm(n, 2)) >= 400]
print("Balmer lines >= 400 nm:", vis); ok &= vis == [3, 4, 5, 6]
inwin = [n for n in range(3, 60) if air_nm(vac_nm(n, 2)) >= 380]
print("Balmer lines >= 380 nm:", inwin); ok &= inwin == list(range(3, 10))
print("Balmer limit (air) %.1f nm" % air_nm(1e9 / R_M(m_p) / 0.25))
ly = [vac_nm(n, 1) for n in range(2, 200)]; print(f"Lyman: {min(ly):.1f}-{max(ly):.1f} nm (deep UV)"); ok &= max(ly) < 200
pa = [vac_nm(n, 3) for n in range(4, 200)]; print(f"Paschen: {min(pa):.0f}-{max(pa):.0f} nm (IR)"); ok &= min(pa) > 700
# ionized helium, one-electron atom: Z^2 scaling with He-4 nuclear mass; He II 4->3 known at 468.6 nm (air)
M_He = k.physical_constants['alpha particle mass'][0]
heii = air_nm(1e9 / (4 * R_M(M_He) * (1/9 - 1/16))); print(f"He II 4->3: {heii:.2f} nm (observed 468.57)"); ok &= abs(heii - 468.57) < 0.1
# Heisenberg: frequency of 3->2 entry = (E3-E2)/h equals c/lambda_vac
E = lambda n: -k.h * k.c * R_M(m_p) / n**2
nu = (E(3) - E(2)) / k.h; nu2 = k.c / (vac_nm(3, 2) * 1e-9)
print(f"(E3-E2)/h = {nu:.6e} Hz, c/lambda = {nu2:.6e} Hz"); ok &= abs(nu/nu2 - 1) < 1e-12
print("PASS" if ok else "FAIL")
