# Account 2 worked numbers:
# "let the pieces at 30° be 0.909 and 0.630 instead, whose cubes come to 0.75 and 0.25";
# "0.909 and 0.630 are the ordinary shadows raised to the power two-thirds"; "cube of the renamed piece
# is just square of the shadow"; "renamed amplitudes no longer add";
# "turn by 45° gives pieces 0.707 and 0.707, total 1.41; a turn by just 1° gives 0.9998 and 0.0175, total 1.017";
# "square world ... 0.500 + 0.500 = 1.000 and 0.9997 + 0.0003 = 1.0000";
# "Every ordinary turn, however small, breaks the total."
import numpy as np, sympy as sp
ok = True
c, s = np.cos(np.pi/6), np.sin(np.pi/6)
r1, r2 = 0.75**(1/3), 0.25**(1/3)
print(f"cube roots: {r1:.4f}, {r2:.4f}; shadows^(2/3): {c**(2/3):.4f}, {s**(2/3):.4f}")
ok &= f"{r1:.3f}" == "0.909" and f"{r2:.3f}" == "0.630" and abs(r1 - c**(2/3)) < 1e-12 and abs(r2 - s**(2/3)) < 1e-12
x = sp.symbols('x', positive=True); ok &= sp.simplify((x**sp.Rational(2, 3))**3 - x**2) == 0
# renamed amplitudes do not add: re-adding the renamed pieces of the 30° arrow (as in (5)) along u, v
u = np.array([c, s]); v = np.array([-s, c])
# 0° arrow on u (30°) and v: signed shadows c and -s; renamed pieces r1 and -r2
rebuilt_true = c*u - s*v; rebuilt_ren = r1*u - r2*v
print("re-add true shadows ->", rebuilt_true.round(4), " re-add renamed ->", rebuilt_ren.round(4),
      "length", np.linalg.norm(rebuilt_ren).round(4))
ok &= np.allclose(rebuilt_true, [1, 0]) and not np.allclose(np.linalg.norm(rebuilt_ren), 1, atol=1e-2)
# also: renaming (x -> sign(x)|x|^(2/3)) is not additive
ren = lambda z: np.sign(z)*np.abs(z)**(2/3)
print("ren(0.5)+ren(0.5) =", round(2*ren(0.5), 4), " ren(1) =", ren(1.0)); ok &= abs(2*ren(0.5) - ren(1.0)) > 0.1
# turns
for deg, txt_pieces, txt_tot1, txt_sq in [(45, ("0.707", "0.707"), "1.41", ("0.500", "0.500", "1.000")),
                                          (1, ("0.9998", "0.0175"), "1.017", ("0.9997", "0.0003", "1.0000"))]:
    t = np.radians(deg); a, b = np.cos(t), np.sin(t)
    nd = len(txt_pieces[0].split('.')[1]); nd1 = len(txt_tot1.split('.')[1]); nds = len(txt_sq[0].split('.')[1])
    got = (f"{a:.{nd}f}", f"{b:.{nd}f}", f"{a+b:.{nd1}f}", f"{a*a:.{nds}f}", f"{b*b:.{nds}f}", f"{a*a+b*b:.{nds}f}")
    want = (*txt_pieces, txt_tot1, *txt_sq)
    good = got == want; ok &= good
    print(f"turn {deg}°: exact a={a:.6f} b={b:.6f} a+b={a+b:.6f} a²={a*a:.6f} b²={b*b:.6f}; text {want} {'ok' if good else 'X ' + str(got)}")
# 'every ordinary turn ... breaks the total' for the 0° arrow under the plain-size rule
T = np.radians(np.linspace(0, 360, 360001)); tot = np.abs(np.cos(T)) + np.abs(np.sin(T))
kept = np.degrees(T[np.abs(tot - 1) < 1e-9])
print("turn angles (deg) in [0,360] where plain-size total stays 1:", np.unique(np.round(kept, 3)))
small = (np.degrees(T) > 0) & (np.degrees(T) < 90)
print("all turns strictly between 0° and 90° break it:", bool(np.all(tot[small] > 1)))
claim_every_turn = np.all(np.abs(tot[np.degrees(T) > 0] - 1) > 1e-9)
print("literal 'every turn breaks the total' true?", bool(claim_every_turn))
print("PASS (numbers)" if ok else "FAIL (numbers)")
print("FAIL (wording): turns by 90°, 180°, 270° keep the plain-size total" if not claim_every_turn else "PASS (wording)")
