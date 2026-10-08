# Claims: "one slit open, electrons land there often"; "both open ... none land there";
# figure: "curve (1) is about 0.95 there while curve (3) is 0"; "peaks reach twice curve (2)";
# Check yourself: covering one slit at a dark stripe -> more hits.
import sympy as sp
u = sp.symbols('u', real=True)
S = (sp.sin(sp.pi*u)/(sp.pi*u))**2
one = S
recorded = 2*S
both = 4*S*sp.cos(4*sp.pi*u)**2
u0 = sp.Rational(1, 8)
v1 = sp.N(one.subs(u, u0)); v3 = sp.simplify(both.subs(u, u0))
print("S(0.125) =", v1, " both-open(0.125) =", v3)
# first dark stripe: smallest positive zero of cos(4 pi u)
print("first zero of cos(4 pi u):", sp.nsolve(sp.cos(4*sp.pi*u), u, 0.1))
# peaks of curve 3 at cos^2=1 equal 2x curve 2
ratio = sp.simplify((both/recorded).subs(sp.cos(4*sp.pi*u)**2, 1))
print("peak ratio both/recorded at cos^2=1:", ratio)
# adding nonnegative chances can never decrease: p1+p2 >= p1
ok = abs(v1 - 0.95) < 0.01 and v3 == 0 and ratio == 2 and v1 > v3
print("PASS" if ok else "FAIL")
