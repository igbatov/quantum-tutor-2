# Claim: wiggle rule f(x) = x^2 + eps x^2(1-x^2)(2x^2-1): f(cos)+f(sin)=1 for every theta;
# f(0)=0, f(1)=1, f>=0 for |eps|<1 since "(1-x^2)(2x^2-1) never goes below -1 on 0<=x<=1";
# three-way state: f = 1/3 - 2eps/27, total 1 - 2eps/9; eps=0.5 -> 0.889, "eleven per cent".
import sympy as sp, numpy as np
x, e, t = sp.symbols('x epsilon theta', real=True)
f = lambda a: a**2 + e*a**2*(1-a**2)*(2*a**2-1)
ok = sp.simplify(sp.expand_trig(f(sp.cos(t)) + f(sp.sin(t)) - 1)) == 0
c = sp.cos(t)**2; s = sp.sin(t)**2
ok &= sp.simplify(f(sp.cos(t)) - (c + e*c*s*(2*c-1))) == 0
ok &= sp.simplify(f(sp.sin(t)) - (s + e*s*c*(1-2*c))) == 0
ok &= f(0) == 0 and sp.simplify(f(1) - 1) == 0
xs = np.linspace(0, 1, 100001); br = (1-xs**2)*(2*xs**2-1)
ok &= br.min() >= -1 - 1e-15 and abs(br.min()+1) < 1e-12 and abs(br.max()-1/8) < 1e-6
for ev in (-0.999, -0.5, 0.5, 0.999):
    fv = xs**2 + ev*xs**2*br; ok &= fv.min() >= -1e-15
f3 = sp.simplify(f(1/sp.sqrt(3)))
ok &= sp.simplify(f3 - (sp.Rational(1, 3) - 2*e/27)) == 0
tot = sp.simplify(3*f3); ok &= sp.simplify(tot - (1 - 2*e/9)) == 0
v = float(tot.subs(e, 0.5)); ok &= abs(v - 0.889) < 5e-4 and abs((1-v)*100 - 11.1) < 0.05
print('f3 =', f3, '| total =', tot, '| eps=0.5 ->', round(v, 4), 'missing', round(100*(1-v), 2), '% | bracket range', br.min(), br.max())
print('PASS' if ok else 'FAIL')
