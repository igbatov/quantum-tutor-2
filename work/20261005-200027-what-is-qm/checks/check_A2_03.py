# Claims: "add the two amplitudes first, and squaring the size ... sets the chance";
# "at some spots the two are equal and opposite and cancel ... Where they match, they reinforce";
# "opening the second slit could only add hits there, never remove them" (classical);
# "With a record, you add chances instead of amplitudes, so nothing cancels";
# figure: "twice as high at the centre", "electrons missing from the dark stripes turn up in the bright ones";
# headphones: "high wherever the noise is low, so the two add to silence".
import sympy as sp, numpy as np
from scipy.integrate import quad
X = sp.symbols('X', real=True)
env = sp.sin(sp.pi*X/4)/(sp.pi*X/4)
psi1 = env*sp.exp(-sp.I*sp.pi*X); psi2 = env*sp.exp(sp.I*sp.pi*X)   # path-length phase +-pi X
both = sp.simplify(sp.expand((psi1+psi2)*sp.conjugate(psi1+psi2)).rewrite(sp.cos))
diff = sp.simplify(both - 4*env**2*sp.cos(sp.pi*X)**2)
print("|psi1+psi2|^2 - 4 P1 cos^2(pi X) =", diff); ok_a = diff == 0
r = sp.simplify(psi1/psi2); print("psi1/psi2 at X=1/2:", r.subs(X, sp.Rational(1,2)), " at X=1:", r.subs(X, 1))
ok_b = r.subs(X, sp.Rational(1,2)) == -1 and r.subs(X, 1) == 1
inc = sp.simplify(sp.expand(psi1*sp.conjugate(psi1) + psi2*sp.conjugate(psi2) - 2*env**2)); print("|psi1|^2+|psi2|^2 - 2P1 =", inc); ok_c = inc == 0
ratio = sp.limit((4*env**2*sp.cos(sp.pi*X)**2)/(2*env**2), X, 0); print("centre ratio:", ratio); ok_d = ratio == 2
# which-path record with environment overlap g: P = P1+P1 + 2 Re(g psi1* psi2) -> g=0 no interference term
g = sp.symbols('g', real=True)
Pg = sp.simplify(sp.expand(2*env**2 + 2*g*sp.re(sp.conjugate(psi1)*psi2)))
print("with record overlap g:", sp.simplify(Pg.subs(g, 0) - 2*env**2) == 0)
f = lambda x: np.sinc(x/4)**2
I2 = quad(lambda x: 4*f(x)*np.cos(np.pi*x)**2, -400, 400, limit=4000)[0]; Ic = quad(lambda x: 2*f(x), -400, 400, limit=4000)[0]
print("total both-slit vs total no-interference:", I2, Ic, "rel diff", abs(I2-Ic)/Ic); ok_e = abs(I2-Ic)/Ic < 1e-3
xs = np.linspace(-40, 40, 200001); ok_f = np.all(2*f(xs) >= f(xs)); print("classical 2P1 >= P1 everywhere:", ok_f)
t = np.linspace(0, 1, 1001); noise = np.sin(7*t)+0.3*np.cos(19*t); ok_g = np.allclose(noise + (-noise), 0)
for name, ok in [("amplitudes add then square", ok_a), ("cancel/reinforce", ok_b), ("record -> add chances", ok_c),
                 ("twice at centre", ok_d), ("redistribution", ok_e), ("classical only adds", ok_f), ("headphones", ok_g)]:
    print(name, "PASS" if ok else "FAIL")
