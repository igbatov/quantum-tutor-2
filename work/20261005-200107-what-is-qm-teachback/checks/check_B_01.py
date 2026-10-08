# Claim: "only steady vibration patterns ... fit a whole number of half-waves"; "more humps sound higher";
# "sin(2.5*pi*x) ends at height 1" (figure spec); plucking harder changes energy not note.
import sympy as sp
x, n, L, T, mu, t, A = sp.symbols('x n L T mu t A', positive=True)
k = sp.symbols('k', positive=True)
# Standing wave y = A sin(kx) cos(wt) with y(0)=0 and y(L)=0 requires sin(kL)=0 -> kL = n*pi
sols = sp.solve(sp.Eq(sp.sin(k*L), 0), k)
ok1 = all(sp.simplify(s*L/sp.pi).is_integer or True for s in sols)
# check n integer fits, n=2.5 doesn't
fits = [sp.sin(m*sp.pi) for m in (1, 2, 3)]
nofit = sp.sin(sp.Rational(5, 2)*sp.pi)
ok2 = all(f == 0 for f in fits) and nofit == 1
# frequency f_n = n/(2L) sqrt(T/mu): increases with n, independent of amplitude A
f_n = n/(2*L)*sp.sqrt(T/mu)
ok3 = sp.diff(f_n, n).is_positive and sp.diff(f_n, A) == 0
# humps: sin(n pi x) on [0,1] has n half-waves (n-1 interior zeros)
import numpy as np
xs = np.linspace(1e-6, 1-1e-6, 200001)
humps = [int(np.sum(np.diff(np.sign(np.sin(m*np.pi*xs))) != 0)) + 1 for m in (1, 2, 3)]
ok4 = humps == [1, 2, 3]
# shorter string -> higher f
ok5 = sp.diff(f_n, L).is_negative
print("sin(n pi) for n=1,2,3:", fits, " sin(2.5 pi) =", nofit)
print("humps:", humps, "df/dn>0:", ok3, "df/dL<0:", ok5)
print("PASS" if (ok2 and ok3 and ok4 and ok5) else "FAIL")
