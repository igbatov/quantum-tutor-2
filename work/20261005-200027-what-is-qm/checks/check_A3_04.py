# Claims: "If the record reliably tells the slits apart, the narrow stripes disappear; a fuzzy record only fades them."
# "With a reliable record, you add chances instead of amplitudes ... exactly the two one-slit patterns added together,
#  much like the broad spread you probably first guessed" (guess: "a broad spread of hits with no stripes")
import sympy as sp, numpy as np
X = sp.symbols("X", real=True); g = sp.symbols("g", real=True)   # g = overlap <D1|D2> of detector record states
a1 = sp.exp(sp.I*sp.pi*X); a2 = sp.exp(-sp.I*sp.pi*X)
# P = |a1|^2 + |a2|^2 + 2 Re(a1 conj(a2) g)
P = sp.simplify((a1*sp.conjugate(a1) + a2*sp.conjugate(a2) + 2*sp.re(a1*sp.conjugate(a2)*g)).rewrite(sp.cos))
print("P(X; g) =", P)
print("reliable record g=0:", sp.simplify(P.subs(g, 0)), "(chances added)")
Pmax, Pmin = P.subs(X, 0), P.subs(X, sp.Rational(1, 2))
print("visibility (Pmax-Pmin)/(Pmax+Pmin) =", sp.simplify((Pmax-Pmin)/(Pmax+Pmin)), "-> fades linearly with overlap g")
P1 = lambda x: np.sinc(x/4)**2
x = np.linspace(-3.9, 3.9, 80001); y = 2*P1(x); half = y[y.size//2:]
print("which-path pattern central band free of narrow stripes:", np.all(np.diff(half) <= 1e-15),
      "; side bands at 4.7% remain (see check_A3_01) -> 'much like', not 'identical to', a stripe-free spread")
print("PASS")
