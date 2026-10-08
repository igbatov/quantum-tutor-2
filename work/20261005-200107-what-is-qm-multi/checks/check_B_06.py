# Figure spec: "P(u) ∝ sinc^2(u) cos^2(5 pi u) ... slit separation five times the slit width"
import sympy as sp
a, d, s, lam = sp.symbols('a d s lambda', positive=True)
x = sp.symbols('x', real=True)
k = 2*sp.pi*s/lam                         # s = sin(theta)
single = sp.integrate(sp.exp(sp.I*k*x), (x, -a/2, a/2))
two = sp.simplify(single*(sp.exp(sp.I*k*d/2)+sp.exp(-sp.I*k*d/2)))
u = sp.symbols('u', positive=True)
# u = a s / lam ; d = 5a
expr = sp.simplify((two.subs(d, 5*a).subs(s, u*lam/a))/a)
target = 2*sp.sin(sp.pi*u)/(sp.pi*u)*sp.cos(5*sp.pi*u)
diff = sp.simplify(sp.expand_complex(expr - target))
print("amplitude/a =", sp.simplify(sp.expand_complex(expr)))
print("difference from 2 sinc(u) cos(5 pi u):", diff)
print("PASS" if diff == 0 else "FAIL")
