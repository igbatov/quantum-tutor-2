# Claim: "pinned at both ends ... must fit a whole number of half-waves" (guitar string)
import sympy as sp
x, L, k = sp.symbols('x L k', positive=True)
n = sp.symbols('n', integer=True, positive=True)
# sin(kx) with y(0)=0 already; y(L)=0 => sin(kL)=0 => kL = n*pi => L = n*(lambda/2)
y = sp.sin(n*sp.pi*x/L)
ok = sp.simplify(y.subs(x, 0)) == 0 and sp.simplify(y.subs(x, L)) == 0
lam = 2*sp.pi/(n*sp.pi/L)
ok &= sp.simplify(L - n*lam/2) == 0
# non-integer fails
y2 = sp.sin(sp.Rational(5,2)*sp.pi*x/L)
ok &= sp.simplify(y2.subs(x, L)) != 0
print(f"sin(n pi x/L) vanishes at 0,L; L = n*lambda/2: {ok}")
print("PASS" if ok else "FAIL")
