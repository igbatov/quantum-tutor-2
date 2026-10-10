# Claim: grid picture "No piece involves all three"; "adding the three pair blocks
# counts each diagonal square twice and each rectangle once"; aligned-direction scaling
# "from the full area ... through zero at right angles, to minus the full area".
import sympy as sp
a,b,c = sp.symbols('a b c', positive=True)
full = sp.expand((a+b+c)**2)
print("(a+b+c)^2 =", full)
pairs = sp.expand((a+b)**2 + (b+c)**2 + (a+c)**2)
print("sum of pair blocks =", pairs)
ok = sp.expand(pairs - 2*(a**2+b**2+c**2) - (2*a*b+2*a*c+2*b*c)) == 0  # diag twice, each rectangle (2 per pair) once
ok &= sp.expand(pairs - (a**2+b**2+c**2) - full) == 0
ok &= sp.Poly(full, a,b,c).coeff_monomial(a*b*c) == 0
ok &= sp.expand((a+b)**2 - (a**2 + 2*a*b + b**2)) == 0
# directions: hands of length a,b,c at angles ta,tb,tc
ta,tb,tc = sp.symbols('ta tb tc', real=True)
za,zb,zc = a*sp.exp(sp.I*ta), b*sp.exp(sp.I*tb), c*sp.exp(sp.I*tc)
tot = sp.expand(sp.simplify(sp.expand_complex((za+zb+zc)*sp.conjugate(za+zb+zc))))
target = a**2+b**2+c**2 + 2*a*b*sp.cos(ta-tb) + 2*a*c*sp.cos(ta-tc) + 2*b*c*sp.cos(tb-tc)
diff = sp.simplify(sp.expand_trig(tot - target))
print("|za+zb+zc|^2 - (squares + rectangles*cos(angle)) =", diff)
ok &= diff == 0
for ang,name in [(0,'same way'),(sp.pi/2,'right angle'),(sp.pi,'opposite')]:
    print(name, ": rectangle scale cos =", sp.cos(ang))
# figure numbers a=3,b=2,c=1
vals = {a:3,b:2,c:1}
print("areas aa,bb,cc,ab,ac,bc:", [ (e).subs(vals) for e in [a*a,b*b,c*c,a*b,a*c,b*c]], "total", full.subs(vals))
ok &= full.subs(vals) == 36
cube = sp.expand((a+b+c)**3)
print("cube coefficient of abc:", sp.Poly(cube,a,b,c).coeff_monomial(a*b*c), " volume", cube.subs(vals),
      " abc-pieces volume", 6*(a*b*c).subs(vals))
ok &= cube.subs(vals)==216 and 6*(a*b*c).subs(vals)==36
print("PASS" if ok else "FAIL")
