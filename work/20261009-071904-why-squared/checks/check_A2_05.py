# Claims (5) and Model 1: "paths of equal length ... comes out polarized at 0°";
# "With the splitter at 30°, ... half a wavelength ... polarized at 60° instead (in general, at twice
# the splitter angle), and the 0° test polarizer passes only a quarter";
# "mirror image of a 0° arrow across a 30° line lies at 60° ... 0.5² = 0.25";
# "three polarizers at 0°, 45° and 90° pass a quarter ... 0° and 90° alone pass none";
# half-wave plate in front of a fixed splitter "gives the same counts"; sugar-water turn keeps total.
import sympy as sp
th, ph, al, be = sp.symbols('theta phi alpha beta', real=True)
vec = lambda a: sp.Matrix([sp.cos(a), sp.sin(a)])
u, v = vec(th), sp.Matrix([-sp.sin(th), sp.cos(th)])
psi = vec(0)
a, b = (psi.T*u)[0], (psi.T*v)[0]
same = sp.simplify(a*u + b*v - psi)
delayed = sp.simplify(a*u + sp.exp(sp.I*sp.pi)*b*v)           # half-wave delay = factor -1 on one path
ok = same == sp.zeros(2, 1)
ok &= sp.simplify(delayed - vec(2*th)) == sp.zeros(2, 1)
print("equal paths ->", list(same), "(zero = back to 0°)")
print("half-wave delay -> arrow at 2θ:", sp.simplify(delayed - vec(2*th)) == sp.zeros(2, 1))
# general input phi: mirror across u -> 2θ - φ (so 'twice the splitter angle' is for 0° input, as in text)
psi_g = vec(ph); ag, bg = (psi_g.T*u)[0], (psi_g.T*v)[0]
ok &= sp.simplify(ag*u - bg*v - vec(2*th - ph)) == sp.zeros(2, 1)
out30 = delayed.subs(th, sp.pi/6)
ang = sp.atan2(out30[1], out30[0]); P0 = sp.nsimplify((out30.T*vec(0))[0]**2)
print("splitter 30°: output angle =", sp.deg(ang), "deg; 0° test passes", P0)
ok &= sp.simplify(sp.deg(ang) - 60) == 0 and P0 == sp.Rational(1, 4)
# three polarizers
Pr = lambda a: vec(a)*vec(a).T
three = sp.simplify((Pr(sp.pi/2)*Pr(sp.pi/4)*psi).norm()**2); two = sp.simplify((Pr(sp.pi/2)*psi).norm()**2)
print("0°,45°,90°:", three, " 0°,90°:", two); ok &= three == sp.Rational(1, 4) and two == 0
# half-wave plate at angle alpha: phi -> 2alpha - phi; turning photon by -theta (alpha = -theta/2) vs splitter by theta
hwp_out = vec(2*al - 0)
pass_hwp = sp.simplify(((hwp_out.T*vec(0))[0]**2).subs(al, -th/2))
pass_split = sp.simplify((psi.T*u)[0]**2)
print("HWP-turned photon at fixed splitter:", pass_hwp, " vs turned splitter:", pass_split)
ok &= sp.simplify(pass_hwp - pass_split) == 0
# sugar water: rotation by beta keeps sum of squares; pass fraction cos^2(beta) smooth
R = sp.Matrix([[sp.cos(be), -sp.sin(be)], [sp.sin(be), sp.cos(be)]]); out = R*psi
ok &= sp.simplify(out[0]**2 + out[1]**2 - 1) == 0
print("PASS" if ok else "FAIL")
