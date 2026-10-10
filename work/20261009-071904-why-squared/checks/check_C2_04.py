# Model 3 (final-C): "Consider any rule that works out the chance from the total hand alone ...
#  must be quadratic ... never from a component on its own and never from three multiplied together"
# and "How they relate": "one smooth, never-negative, direction-blind rule, 'pairwise only' forces the square".
# Check (polynomial ansatz up to degree 6, Frechet's theorem covers continuous f):
#  (i) the 7-term leftover vanishing for all hands already forces f(0) = 0 (no separate assumption needed)
#  (ii) solutions are linear + quadratic; never-negative or direction-blind removes the linear part
#  (iii) direction-blind quadratic = k (x^2 + y^2)
import sympy as sp, itertools
x, y = sp.symbols('x y', real=True)
D = 6
cs = {(i, j): sp.Symbol(f'c_{i}_{j}') for i in range(D+1) for j in range(D+1-i)}
f = lambda X, Y: sum(c*X**i*Y**j for (i, j), c in cs.items())
v = sp.symbols('x1 y1 x2 y2 x3 y3', real=True)
a, b, c = (v[0], v[1]), (v[2], v[3]), (v[4], v[5])
add = lambda *h: (sum(t[0] for t in h), sum(t[1] for t in h))
I3 = f(*add(a, b, c)) - f(*add(a, b)) - f(*add(b, c)) - f(*add(a, c)) + f(*a) + f(*b) + f(*c)
eqs = sp.Poly(sp.expand(I3), *v).coeffs()
sol = sp.solve(eqs, list(cs.values()), dict=True)[0]
fs = sp.expand(f(x, y).subs(sol))
print("general solution of leftover = 0 (7 terms, f(0) not imposed):", fs)
print("f(0) =", fs.subs({x: 0, y: 0}))
degs = {sp.Poly(t, x, y).total_degree() for t in fs.as_ordered_terms()}
print("degrees present:", degs)
ok = fs.subs({x: 0, y: 0}) == 0 and degs <= {1, 2}
# direction-blind: f(R z) = f(z) for all rotations R
th = sp.Symbol('th', real=True)
rot = sp.expand(fs.subs({x: sp.cos(th)*x - sp.sin(th)*y, y: sp.sin(th)*x + sp.cos(th)*y}, simultaneous=True) - fs)
eq2 = sp.Poly(sp.expand(sp.expand_trig(rot)), x, y).coeffs()
free = [s for s in fs.free_symbols if s.name.startswith('c_')]
cond = []
for e in eq2:
    for tv in [sp.pi/3, sp.pi/2]:
        cond.append(sp.nsimplify(e.subs(th, tv)))
sol2 = sp.solve(cond, free, dict=True)[0]
fr = sp.factor(fs.subs(sol2))
print("direction-blind solution:", fr)
ok &= sp.simplify(fr - list(fr.free_symbols - {x, y})[0]*(x**2+y**2)) == 0
print("PASS" if ok else "FAIL")
