# Claim (5): "equal length ... comes out polarized at 0°"; "Lengthen one path by half a
# wavelength and the photon comes out polarized at 60°", "0° test polarizer passes only a quarter"
# Also: "three polarizers at 0°, 45° and 90° pass a quarter"; spin-1/2 "75% at 60°, 50% at 90°"
import sympy as sp
th = sp.symbols('theta', real=True)
psi = sp.Matrix([1, 0])                                  # 0-deg polarization
u = sp.Matrix([sp.cos(th), sp.sin(th)]); v = sp.Matrix([-sp.sin(th), sp.cos(th)])
a, b = (u.T*psi)[0], (v.T*psi)[0]                         # shadows on pass / reflect
out_equal = sp.simplify(a*u + b*v)
out_half = sp.simplify(a*u + sp.exp(sp.I*sp.pi)*b*v)      # half-wavelength delay on reflect path
print("equal paths ->", list(out_equal))
print("half-wave delay ->", [sp.trigsimp(x) for x in out_half], " = polarization at angle 2*theta")
pass0 = sp.simplify(out_half[0]**2)
print("0-deg test polarizer pass fraction after delay:", sp.trigsimp(pass0))
ok_equal = out_equal == sp.Matrix([1, 0])
res = {}
for deg in [15, 30, 45, 60]:
    t = sp.rad(deg)
    vec = out_half.subs(th, t)
    ang = sp.deg(sp.atan2(vec[1], vec[0]))
    res[deg] = (sp.nsimplify(ang), sp.nsimplify(vec[0]**2))
    print(f"splitter at {deg} deg: output at {res[deg][0]} deg, 0-deg test passes {res[deg][1]}")
ok_60 = res[30] == (60, sp.Rational(1, 4))
general = all(res[d][0] == 60 for d in res)
print("60 deg / one quarter holds only for splitter at 30 deg (not stated in (5)):", ok_60 and not general)
# three polarizers
P = lambda deg: (lambda t: sp.Matrix([[sp.cos(t)**2, sp.cos(t)*sp.sin(t)], [sp.cos(t)*sp.sin(t), sp.sin(t)**2]]))(sp.rad(deg))
three = (P(90)*P(45)*psi).norm()**2; two = (P(90)*psi).norm()**2
print("0,45,90 pass fraction:", sp.nsimplify(three), " 0,90:", two)
spin = {60: sp.cos(sp.rad(60)/2)**2, 90: sp.cos(sp.rad(90)/2)**2}
print("spin-1/2 cos^2(theta/2):", {k: sp.nsimplify(v) for k, v in spin.items()})
ok_other = three == sp.Rational(1, 4) and two == 0 and spin[60] == sp.Rational(3, 4) and spin[90] == sp.Rational(1, 2)
print("equal-path recombination:", "PASS" if ok_equal else "FAIL")
print("60 deg / quarter claim:", "PASS" if general else "FAIL (true only if splitter is at 30 deg; generally output at 2*theta, test passes cos^2(2 theta))")
print("three polarizers & spin-1/2:", "PASS" if ok_other else "FAIL")
