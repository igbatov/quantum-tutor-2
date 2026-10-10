# Figure request b-stationary-vs-cos: "a = b = 1/sqrt(2): hand rule (1/2)|e^{-i w1 t} + e^{-i w2 t}|^2
#  = (1/2)(1 + cos(0.1 t))"; "real rule (cos(w1 t) + cos(w2 t))^2 / 2 ... peaks reaching 2";
#  window "t from 0 to 6 pi/omega_1" with "one slow beat".
import sympy as sp
import numpy as np
t = sp.symbols('t', real=True)
w1, w2 = 1, sp.Rational(11, 10)
e1, e2 = sp.exp(-sp.I*w1*t), sp.exp(-sp.I*w2*t)
stated = sp.Rational(1, 2)*(1 + sp.cos(t/10))
expr = sp.simplify(sp.expand_complex(sp.Rational(1, 2)*(e1 + e2)*sp.conjugate(e1 + e2)))
print("(1/2)|e1+e2|^2 =", expr, "; equals stated?", sp.simplify(expr - stated) == 0)
a = b = 1/sp.sqrt(2)
consistent = sp.simplify(sp.expand_complex(sp.Rational(1, 2)*(a*e1 + b*e2)*sp.conjugate(a*e1 + b*e2)))
print("with a=b=1/sqrt2 and outcome (1+2)/sqrt2:", consistent, "; equals stated?", sp.simplify(consistent - stated) == 0)
T = np.linspace(0, 200, 400001)
real_stated = (np.cos(T) + np.cos(1.1*T))**2/2
real_consistent = 0.5*(np.cos(T)/np.sqrt(2) + np.cos(1.1*T)/np.sqrt(2))**2
print("max of stated real rule:", real_stated.max(), "; max of the a=b=1/sqrt2 real rule:", real_consistent.max())
beat = 2*np.pi/0.1
print(f"beat period = {beat:.2f}; requested window 6 pi = {6*np.pi:.2f} covers {6*np.pi/beat:.2f} of one beat")
formula_ok = sp.simplify(expr - stated) == 0
window_ok = 6*np.pi >= beat
print("formula in figure spec:", "PASS" if formula_ok else "FAIL (factor 2: (1/2)|e1+e2|^2 = 1 + cos(0.1t))")
print("window shows one slow beat:", "PASS" if window_ok else "FAIL (window shows under a third of the beat; use 0..20 pi)")
