# Claim: "the square rule has two-way interference and nothing beyond";
# "plain size, the cube, the fourth power, and mixtures ... contain three-way interference";
# "holds at every spot, at any screen distance and for any slit shape"
# Sorkin combination I3 = P_ABC - P_AB - P_BC - P_AC + P_A + P_B + P_C for P = |z|^p.
import sympy as sp, numpy as np
x1,y1,x2,y2,x3,y3 = sp.symbols('x1 y1 x2 y2 x3 y3', real=True)
a = x1+sp.I*y1; b = x2+sp.I*y2; c = x3+sp.I*y3
def P2(z): return sp.expand(z*sp.conjugate(z))
I3_sq = sp.simplify(P2(a+b+c)-P2(a+b)-P2(b+c)-P2(a+c)+P2(a)+P2(b)+P2(c))
print("p=2 symbolic I3 (arbitrary complex a,b,c):", I3_sq)
# I2 for p=2 must be nonzero (two-way interference present)
I2_sq = sp.simplify(P2(a+b)-P2(a)-P2(b))
print("p=2 symbolic I2:", I2_sq)
ok = (I3_sq == 0) and (I2_sq != 0)

# Real positive (all hands aligned) case for polynomial powers
A,B,C = sp.symbols('a b c', positive=True)
for p in [1,2,3,4]:
    f = lambda s: s**p
    expr = sp.factor(sp.expand(f(A+B+C)-f(A+B)-f(B+C)-f(A+C)+f(A)+f(B)+f(C)))
    print(f"aligned hands, power {p}: I3 =", expr)
cube_aligned = sp.factor(sp.expand((A+B+C)**3-(A+B)**3-(B+C)**3-(A+C)**3+A**3+B**3+C**3))
ok &= sp.simplify(cube_aligned - 6*A*B*C) == 0

# Numerical: random complex triples, several rules
rng = np.random.default_rng(1)
Z = rng.normal(size=(20000,3)) + 1j*rng.normal(size=(20000,3))
def I3num(f):
    za,zb,zc = Z.T
    return f(za+zb+zc)-f(za+zb)-f(zb+zc)-f(za+zc)+f(za)+f(zb)+f(zc)
rules = {
 'size^1': lambda z: np.abs(z),
 'size^2': lambda z: np.abs(z)**2,
 'size^3': lambda z: np.abs(z)**3,
 'size^4': lambda z: np.abs(z)**4,
 'size^2 + 0.01 size^4': lambda z: np.abs(z)**2 + 0.01*np.abs(z)**4,
}
for k,f in rules.items():
    v = I3num(f); scale = np.max(np.abs(f(Z.sum(1))))
    print(f"{k:22s} max|I3| = {np.max(np.abs(v)):.3e}  (scale {scale:.2e})")
    if k=='size^2': ok &= np.max(np.abs(v)) < 1e-9*scale
    else: ok &= np.max(np.abs(v)) > 1e-3
# Scan of real exponents: I3 identically zero only at p=2
ps = np.linspace(0.25,6,231)
mx = np.array([np.max(np.abs(I3num(lambda z: np.abs(z)**p))) for p in ps])
zero_ps = ps[mx<1e-8]
print("exponents in [0.25,6] (step 0.025) with I3==0 on all samples:", zero_ps)
ok &= np.allclose(zero_ps,[2.0])
print("PASS" if ok else "FAIL")
