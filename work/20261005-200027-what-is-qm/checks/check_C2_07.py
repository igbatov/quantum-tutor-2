# Claims: "Only whole numbers of humps fit between pinned ends"; n = 1,2,3 have 1,2,3 humps;
# "2.5 humps ... curve sits at height 1 instead of meeting the dot at height 0"
import sympy as sp, numpy as np
x = sp.symbols('x', real=True); kk = sp.symbols('k', positive=True)
sol = sp.solveset(sp.sin(kk*sp.pi), kk, sp.Interval(0.1, 10))
print("k with sin(k pi)=0 in (0,10]:", sol)
v = sp.sin(sp.Rational(5,2)*sp.pi); print("sin(2.5 pi) =", v)
xs = np.linspace(0,1,200001)[1:-1]
humps = [int(np.sum(np.diff(np.sign(np.sin(n*np.pi*xs)))!=0))+1 for n in [1,2,3]]
print("humps", humps)
ok = sol == sp.FiniteSet(*range(1,11)) and v==1 and humps==[1,2,3]
print("PASS" if ok else "FAIL")
