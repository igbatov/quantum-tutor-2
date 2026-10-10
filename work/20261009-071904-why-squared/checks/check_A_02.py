# Claim: "0.87 + 0.50 = 1.37 ... 0.71 + 0.71 = 1.41: 141%"; "Cubes: 0.649 + 0.125 = 0.774";
# "0.35 + 0.35 = 0.71: 29% ... unaccounted"; "Fourth power: 0.25 + 0.25 = 0.5 at 45°"
import numpy as np
r = np.radians
res = []
def chk(label, val, claimed, tol):
    good = abs(val - claimed) <= tol
    res.append(good)
    print(f"{label}: exact={val:.5f} claimed={claimed} {'ok' if good else 'MISMATCH'}")
chk("p=1 at 30", np.cos(r(30)) + np.sin(r(30)), 1.37, 0.005)
chk("p=1 at 45", np.cos(r(45)) + np.sin(r(45)), 1.41, 0.005)
chk("cos30^3", np.cos(r(30))**3, 0.649, 0.0005)        # 3-decimal rounding tolerance
chk("sin30^3", np.sin(r(30))**3, 0.125, 0.0005)
chk("p=3 at 30", np.cos(r(30))**3 + np.sin(r(30))**3, 0.774, 0.0005)
chk("cos45^3 (each)", np.cos(r(45))**3, 0.35, 0.005)
chk("p=3 at 45", 2*np.cos(r(45))**3, 0.71, 0.005)
print("  written arithmetic '0.35 + 0.35 =' gives", 0.35 + 0.35, "not 0.71")
chk("unaccounted at 45 (p=3) %", 100*(1 - 2*np.cos(r(45))**3), 29, 0.5)
chk("p=4 at 45", 2*np.cos(r(45))**4, 0.5, 1e-12)
chk("check-yourself p=4 at 45", 2*np.cos(r(45))**4, 0.5, 1e-12)
print("PASS" if all(res) else "FAIL")
