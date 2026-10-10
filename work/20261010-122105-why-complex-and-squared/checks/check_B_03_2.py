# Claims: "c^2 = 1/2 + 1/2 cos(2Et/hbar) pulses between 1 and 0"; table values; "dip to zero twice per period";
# "pulsing at 2E/h ... would change if you moved the zero of energy"; pendulum / circular polarization keep
# energy / intensity constant "using two real numbers at once".
import sympy as sp, numpy as np
t, E, hb, w, s = sp.symbols('t E hbar omega s', positive=True)
ok = sp.simplify(sp.cos(E*t/hb)**2 - (sp.Rational(1,2)+sp.cos(2*E*t/hb)/2)) == 0
th = np.array([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
c = np.cos(th); print("cos:", np.round(c,3), "cos^2:", np.round(c**2,3), "|e^-ith|^2:", np.abs(np.exp(-1j*th))**2)
ok &= np.allclose(np.round(c,3), [1,0.707,0,-0.707,-1]) and np.allclose(np.round(c**2,3),[1,0.5,0,0.5,1])
zeros = [z for z in sp.solveset(sp.cos(s)**2, s, sp.Interval.Ropen(0, 2*sp.pi))]
print("zeros of cos^2 in one period:", zeros); ok &= len(zeros) == 2
# shift zero of energy E -> E + d: frequency of cos^2 pulsing changes from 2E to 2(E+d); hand length unchanged
d = sp.symbols('d', positive=True)
ok &= sp.simplify(sp.Abs(sp.exp(-sp.I*(E+d)*t/hb))**2) == 1
# pendulum (harmonic) and circular polarization
x = sp.cos(w*t); v = sp.diff(x, t)
ok &= sp.simplify(v**2/2 + w**2*x**2/2 - w**2/2) == 0
ok &= sp.simplify(sp.cos(w*t)**2 + sp.sin(w*t)**2 - 1) == 0
print("PASS" if ok else "FAIL")
