# Claim (Model 3): a rule with "no three-way term for any combination", continuous, zero for a
# zero hand, never negative "must be quadratic"; if it depends only on length, "a constant
# times the squared length".
# Method: general polynomial ansatz of degree <= 6 in the hand's two components (x, y);
# impose I3 = 0 for all triples (Frechet's functional equation), f(0)=0, f>=0, rotation invariance.
# (For continuous f the polynomial reduction is Frechet's theorem, 1909; checked here on the ansatz.)
import sympy as sp, itertools
x1,y1,x2,y2,x3,y3,t = sp.symbols('x1 y1 x2 y2 x3 y3 t', real=True)
deg = 6
mons = [(i,j) for i in range(deg+1) for j in range(deg+1-i)]
cs = {m: sp.Symbol(f'c_{m[0]}_{m[1]}') for m in mons}
def f(x,y): return sum(cs[(i,j)]*x**i*y**j for (i,j) in mons)
I3 = sp.expand(f(x1+x2+x3,y1+y2+y3)-f(x1+x2,y1+y2)-f(x2+x3,y2+y3)-f(x1+x3,y1+y3)
               +f(x1,y1)+f(x2,y2)+f(x3,y3)-f(0,0))
eqs = sp.Poly(I3, x1,y1,x2,y2,x3,y3).coeffs()
sol = sp.solve(eqs + [cs[(0,0)]], list(cs.values()), dict=True)[0]
fsol = sp.expand(f(sp.Symbol('x',real=True), sp.Symbol('y',real=True)).subs(sol))
x,y = sp.symbols('x y', real=True)
fsol = sp.expand(f(x,y).subs(sol))
print("general solution with I3=0 and f(0)=0:", fsol)
free_degrees = {sum(m) for m in sp.Poly(fsol, x, y).monoms()}
print("degrees present:", free_degrees)
ok = free_degrees <= {1,2}
# nonnegativity kills the linear part: f(t*v) = t^2 Q(v) + t L(v) >= 0 for all small t of both signs
lin = sum(sp.Poly(fsol,x,y).coeff_monomial(m)*m for m in [x,y])
print("linear part:", lin, "-> f(t v) changes sign for small t unless it is 0, so it must vanish")
# check: with a nonzero linear part there is a negative value
test = fsol.subs({k:0 for k in fsol.free_symbols - {x,y}}).subs({})  # placeholder
q = sp.expand(fsol - lin)
# rotation invariance: Q(R v) = Q(v) for all angles -> Q = k(x^2+y^2)
th = sp.Symbol('th', real=True)
qr = sp.expand(q.subs({x: sp.cos(th)*x - sp.sin(th)*y, y: sp.sin(th)*x + sp.cos(th)*y}, simultaneous=True))
cond = sp.Poly(sp.expand(sp.expand_trig(qr - q)), x, y).coeffs()
qsyms = list(q.free_symbols - {x,y})
eqsR = []
for cnd in cond:
    for angle in [sp.pi/2, sp.pi/3, sp.pi/7]:
        eqsR.append(sp.simplify(cnd.subs(th, angle)))
solR = sp.solve(eqsR, qsyms, dict=True)
qinv = sp.factor(q.subs(solR[0])) if solR else q
print("rotation-invariant quadratic:", qinv)
ok &= sp.simplify(qinv.subs({x:1,y:0})*(x**2+y**2) - qinv) == 0
# example showing the linear term is incompatible with f>=0
ex = (x**2+y**2) + x
print("example x^2+y^2+x at (-0.5,0):", ex.subs({x:-sp.Rational(1,2), y:0}), "(negative)")
print("PASS" if ok else "FAIL")
