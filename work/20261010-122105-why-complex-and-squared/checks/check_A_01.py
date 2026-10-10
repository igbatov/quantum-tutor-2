# Claim: "Multiplying by e^{i phi} turns a hand by phi without changing its length"
# plus the expanded algebra of e^{i phi}(x+iy) and its squared length.
import sympy as sp
x, y, f = sp.symbols('x y phi', real=True)
lhs = sp.expand((sp.cos(f) + sp.I*sp.sin(f))*(x + sp.I*y))
claimed = (x*sp.cos(f) - y*sp.sin(f)) + sp.I*(x*sp.sin(f) + y*sp.cos(f))
ok1 = sp.simplify(lhs - claimed) == 0
sq = (x*sp.cos(f) - y*sp.sin(f))**2 + (x*sp.sin(f) + y*sp.cos(f))**2
ok2 = sp.simplify(sq - (x**2 + y**2)) == 0
# claimed intermediate expansion
mid = x**2*sp.cos(f)**2 - 2*x*y*sp.cos(f)*sp.sin(f) + y**2*sp.sin(f)**2 + x**2*sp.sin(f)**2 + 2*x*y*sp.sin(f)*sp.cos(f) + y**2*sp.cos(f)**2
ok3 = sp.expand(sq - mid) == 0
ok4 = sp.simplify(sp.exp(sp.I*f) - (sp.cos(f) + sp.I*sp.sin(f)).rewrite(sp.exp)) == 0
z = x + sp.I*y
ok5 = sp.simplify(sp.expand(z*sp.conjugate(z)) - (x**2 + y**2)) == 0
print('product expansion', ok1, '| length kept', ok2, '| middle line', ok3, '| Euler', ok4, '| z zbar', ok5)
print('PASS' if all([ok1, ok2, ok3, ok4, ok5]) else 'FAIL')
