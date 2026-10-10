# Claim: "100% pass at 0°, 75% at 30°, 50% at 45°, 25% at 60°, none at 90°"
# plus "75 + 25, 50 + 50, 25 + 75" totals, shadows 0.87/0.50, 0.71/0.71, 0.50/0.87
import sympy as sp
th = sp.symbols('theta', real=True)
ok = True
claims = {0: (100, 0), 30: (75, 25), 45: (50, 50), 60: (25, 75), 90: (0, 100)}
for deg, (pp, pr) in claims.items():
    t = sp.rad(deg)
    P = sp.nsimplify(sp.cos(t)**2 * 100); R = sp.nsimplify(sp.sin(t)**2 * 100)
    good = (P == pp) and (R == pr) and (P + R == 100)
    ok &= good
    print(f"{deg:3d} deg: pass={P}%, reflect={R}%, total={P+R}%  {'ok' if good else 'MISMATCH'}")
print("cos^2+sin^2 simplifies to", sp.simplify(sp.cos(th)**2 + sp.sin(th)**2))
sh = {30: (0.87, 0.50), 45: (0.71, 0.71), 60: (0.50, 0.87)}
for deg, (a, b) in sh.items():
    t = sp.rad(deg); ca, sb = float(sp.cos(t)), float(sp.sin(t))
    g = abs(round(ca, 2) - a) < 1e-9 and abs(round(sb, 2) - b) < 1e-9
    ok &= g
    print(f"shadows at {deg}: {ca:.4f}, {sb:.4f} -> claimed {a}, {b} {'ok' if g else 'MISMATCH'}")
# classical wave: relative heights 0.87, 0.50 -> energy 75/25
print("PASS" if ok else "FAIL")
