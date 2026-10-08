# Claim: "2.5 humps ... curve sits at height 1 instead of meeting the dot at height 0"
# and n = 1,2,3 fit pinned ends (sin(n pi x) = 0 at x=0,1); humps count = n
import sympy as sp
x = sp.symbols('x')
ok = all(sp.sin(n*sp.pi*0)==0 and sp.sin(n*sp.pi*1)==0 for n in [1,2,3])
v = sp.sin(sp.Rational(5,2)*sp.pi)
print("sin(2.5 pi) =", v)
import numpy as np
xs = np.linspace(0,1,100001)
humps = [int(np.sum(np.diff(np.sign(np.sin(n*np.pi*xs[1:-1])))!=0))+1 for n in [1,2,3]]
print("humps", humps)
print("PASS" if ok and v==1 and humps==[1,2,3] else "FAIL")
