# Check question: narrowed slit (long arrow + short arrow) -> are dark bands still completely dark?
# Expected answer: no; minimum chance is (a-b)^2 > 0 when a != b.
import sympy as sp
a, b, phi = sp.symbols('a b phi', positive=True)
P = sp.expand(sp.expand_complex(sp.Abs(a + b*sp.exp(sp.I*phi))**2).subs({sp.re(a):a}))
P = sp.simplify(a**2 + b**2 + 2*a*b*sp.cos(phi))
Pmin = sp.factor(P.subs(phi, sp.pi))
print("P(phi) =", P, "; minimum =", Pmin, "; at a=1,b=0.5:", Pmin.subs({a:1, b:sp.Rational(1,2)}))
ok = sp.simplify(Pmin - (a-b)**2) == 0 and Pmin.subs({a:1, b:sp.Rational(1,2)}) > 0
print("PASS" if ok else "FAIL", "(dark bands not completely dark: question is well-posed, answer 'no')")
