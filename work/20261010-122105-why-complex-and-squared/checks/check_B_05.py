# Claims ("What this rules out"): "its square cos^2(omega t) pulses at 2 omega";
#  "c^2 = 1/2 + 1/2 cos(2Et/hbar) pulses between 1 and 0 at twice the frequency";
#  "would dip to zero twice per period"; table of cos, cos^2, |e^{-iEt/hbar}|^2;
#  "One real number per state cannot do that" (turn without changing length).
import sympy as sp
import numpy as np
th = sp.symbols('theta', real=True)
ok = True
ok &= sp.simplify(sp.cos(th)**2 - (sp.Rational(1, 2) + sp.cos(2*th)/2)) == 0
# zeros of cos^2 in one period [0, 2pi)
zs = [z for z in sp.solveset(sp.cos(th)**2, th, sp.Interval.Ropen(0, 2*sp.pi))]
print("zeros of cos^2 per period:", zs); ok &= len(zs) == 2
vals = [0, sp.pi/4, sp.pi/2, 3*sp.pi/4, sp.pi]
row1 = [float(sp.cos(v)) for v in vals]
row2 = [float(sp.cos(v)**2) for v in vals]
row3 = [float(sp.Abs(sp.exp(-sp.I*v))**2) for v in vals]
print("cos:", np.round(row1, 3)); print("cos^2:", np.round(row2, 3)); print("|hand|^2:", row3)
ok &= np.allclose(row1, [1, 0.707, 0, -0.707, -1], atol=6e-4)
ok &= np.allclose(row2, [1, .5, 0, .5, 1]) and np.allclose(row3, 1)
# A continuous real function with constant |c| cannot vary: c(t)=+-A, sign flip needs passing 0.
# (Intermediate value theorem; numerical illustration: any real path from A to -A crosses 0.)
path = np.cos(np.linspace(0, np.pi, 1001))
print("real path from 1 to -1 reaches |c| =", np.abs(path).min())
print("PASS" if ok else "FAIL")
