# Claims: "100% pass at 0°, 75% at 30°, 50% at 45°, 25% at 60°, none at 90°";
# "75 + 25, 50 + 50, 25 + 75"; "amplitude at 0.866 ... 75% is its square, not ... (87%) nor its cube (65%)";
# classical wave "relative height 0.866 ... 0.500 ... energy divides 75/25";
# Model 1 shadows "0.866 / 0.500; 0.707 / 0.707; 0.500 / 0.866", squares "0.75/0.25; 0.50/0.50; 0.25/0.75";
# Pythagoras "0.750 + 0.250 = 1 at 30°, 0.500 + 0.500 = 1 at 45°".
import sympy as sp
th = sp.symbols('theta', real=True)
ok = True
exp_pass = {0: 100, 30: 75, 45: 50, 60: 25, 90: 0}
for d, e in exp_pass.items():
    c2 = sp.nsimplify(100*sp.cos(sp.rad(d))**2); s2 = sp.nsimplify(100*sp.sin(sp.rad(d))**2)
    good = (c2 == e) and (c2 + s2 == 100); ok &= good
    print(f"{d:>2}°: pass {c2}%, reflect {s2}%, total {c2+s2}%  {'ok' if good else 'X'}")
ok &= sp.simplify(sp.cos(th)**2 + sp.sin(th)**2 - 1) == 0
a = float(sp.cos(sp.pi/6))
print(f"amplitude at 30° = {a:.4f} -> {round(100*a)}%; square {a**2:.4f}; cube {a**3:.4f} -> {round(100*a**3)}%")
ok &= f"{a:.3f}" == "0.866" and round(100*a) == 87 and round(100*a**3) == 65 and abs(a**2 - 0.75) < 1e-12
for d, (c_t, s_t) in {30: ("0.866", "0.500"), 45: ("0.707", "0.707"), 60: ("0.500", "0.866")}.items():
    c = float(sp.cos(sp.rad(d))); s = float(sp.sin(sp.rad(d)))
    good = f"{c:.3f}" == c_t and f"{s:.3f}" == s_t; ok &= good
    print(f"{d}°: shadows {c:.4f}, {s:.4f}; squares {c*c:.4f}, {s*s:.4f}; sum {c*c+s*s:.12f} {'ok' if good else 'X'}")
print("PASS" if ok else "FAIL")
