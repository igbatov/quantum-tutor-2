# Claims: "+1 and -1 add to 0"; "+1 and +1 add to 2, which squares to 4, twice the 1 + 1 = 2";
# "add the two amplitudes first, and the square of the total's size sets the chance"; "Each amplitude depends on the length of its route";
# "could only add hits there, never remove them"; caption: "bold rises above dashed at bright stripes (twice as high at the centre)";
# "over the whole screen the totals are equal"
import sympy as sp, numpy as np
from scipy.integrate import quad
print("(+1)+(-1) =", 1 + (-1), "; (1+1)^2 =", (1+1)**2, "; 1+1 =", 1+1, "; ratio", sp.Rational((1+1)**2, 1+1))
X, A = sp.symbols("X A", real=True)
psi1 = A*sp.exp(sp.I*sp.pi*X); psi2 = A*sp.exp(-sp.I*sp.pi*X)     # phase difference 2*pi*X from path-length difference
diff = sp.simplify(sp.expand(sp.Abs(psi1+psi2)**2 - 4*A**2*sp.cos(sp.pi*X)**2).rewrite(sp.cos))
print("|psi1+psi2|^2 - 4A^2cos^2(piX) =", diff)
P1 = lambda x: np.sinc(x/4)**2
x = np.linspace(-40, 40, 400001)
print("classical sum never below one slit:", np.all(2*P1(x) >= P1(x)))
bold = 4*P1(x)*np.cos(np.pi*x)**2
im = np.where((bold[1:-1] > bold[:-2]) & (bold[1:-1] > bold[2:]))[0] + 1
# bright stripes = spots where the two amplitudes match: X integer (cos^2 = 1). Ratio there is exactly 2 wherever P1 > 0.
k = np.arange(-40, 41); k = k[P1(k) > 1e-20]
rk = 4*P1(k)*np.cos(np.pi*k)**2/(2*P1(k)); print("bold/dashed at bright-stripe centres X = integer: min", rk.min().round(6), "max", rk.max().round(6), "; centre ratio", 4*P1(0)/(2*P1(0)))
r = bold[im]/(2*P1(x[im])); low = im[r < 1]
print("note: tiny bold bumps below dashed (flanking missing stripes at the envelope zeros):",
      [(round(x[i], 2), f"{bold[i]/4:.4f} of centre") for i in low if 0 < x[i] < 9])
L = 2000
I2 = quad(lambda t: 4*P1(t)*np.cos(np.pi*t)**2, -L, L, limit=20000)[0]; Ic = quad(lambda t: 2*P1(t), -L, L, limit=20000)[0]
print(f"totals over |X|<{L}: both-open {I2:.6f}, chances added {Ic:.6f}, rel diff {abs(I2-Ic)/Ic:.1e}")
ok = diff == 0 and abs(rk.min()-2) < 1e-9 and abs(I2-Ic)/Ic < 1e-3
print("PASS" if ok else "FAIL")
