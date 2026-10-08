# Claims: long-wavelength rule "fading rate growing as the square of the separation"; reference line
# (6/(2pi)^2)(lam/dx)^2; "flattens to about one event time once dx exceeds about lam/2";
# window "narrows as 1/sqrt(number of scatterings) on the sloped part"; "rate stops growing and equals the impact rate".
import numpy as np, sympy as sp
x = sp.symbols('x', positive=True)
ser = sp.series(1 - sp.sin(x)/x, x, 0, 6).removeO()
print("1 - sinc(x) series:", ser)
lead_ok = sp.simplify(ser.coeff(x, 2) - sp.Rational(1, 6)) == 0
def smooth_one_minus(r, spread=0.3, n=2001):
    lam = np.linspace(1-spread, 1+spread, n)
    return np.mean(1 - np.sinc(2*r[:, None]/lam[None, :]), axis=1)
r = np.logspace(-2, 3, 2000)
tfade = 1/smooth_one_minus(r)
ref = 6/(2*np.pi)**2/r**2
print(f"small dx: tfade/ref at dx/lam=0.01: {tfade[0]/ref[0]:.4f}")
big = r > 0.5
print(f"for dx/lam>0.5: tfade range {tfade[big].min():.3f} .. {tfade[big].max():.3f}; at dx/lam=20: {tfade[np.argmin(abs(r-20))]:.3f}")
# window width where N*(1-overlap) = 1, sloped part
w = lambda N: np.sqrt(6/N)/(2*np.pi)
print(f"window dx/lam at N=1,10,100 (small-x approx): {w(1):.3f}, {w(10):.3f}, {w(100):.3f}; ratio per x10 = {w(1)/w(10):.3f} (sqrt10={np.sqrt(10):.3f})")
ok = lead_ok and abs(tfade[0]/ref[0]-1) < 0.01 and tfade[big].min() > 0.75 and tfade[big].max() < 1.35
print("PASS" if ok else "FAIL")
