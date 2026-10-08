# Claims: "add the two amplitudes first, and squaring the size of that total sets the chance";
# "at some spots the two are equal and opposite and cancel"; "With a record, you add chances";
# "two one-slit humps simply added"; "twice as high at the centre"; slit separation = 4 x slit width.
import sympy as sp
X, A = sp.symbols('X A', real=True)
# Fraunhofer model in units where fringe spacing = 1: each slit amplitude = envelope * phase from path length
env = sp.sin(sp.pi*X/4)/(sp.pi*X/4)            # slit width a = d/4 -> envelope argument pi a x/(lambda L) = pi X/4
psi1 = env*sp.exp(sp.I*sp.pi*X)                 # path-length phase +pi X  (path difference d x / L -> 2 pi X)
psi2 = env*sp.exp(-sp.I*sp.pi*X)
P_both = sp.simplify(sp.expand(sp.Abs(psi1+psi2)**2).rewrite(sp.cos))
target = 4*env**2*sp.cos(sp.pi*X)**2
ok = sp.simplify(sp.expand_complex((psi1+psi2)*sp.conjugate(psi1+psi2)) - target) == 0
print("|psi1+psi2|^2 == 4 P1 cos^2(pi X):", ok)
P_record = sp.expand_complex(psi1*sp.conjugate(psi1) + psi2*sp.conjugate(psi2))
ok2 = sp.simplify(P_record - 2*env**2) == 0
print("|psi1|^2+|psi2|^2 == 2 P1:", ok2)
# cancellation at X=1/2: amplitudes equal and opposite
r = sp.simplify((psi1/psi2).subs(X, sp.Rational(1, 2)))
print("psi1/psi2 at X=1/2:", r); ok3 = r == -1
# centre ratio
ratio = sp.limit(target/(2*env**2), X, 0)
print("both-slit / which-path at centre:", ratio); ok4 = ratio == 2
# noise-cancelling arithmetic: f + (-f) = 0
f = sp.Function('f')(X); ok5 = sp.simplify(f + (-f)) == 0
# slit separation = 4 x width: fringe period lambda L/d = 1 => envelope sinc(pi a x/(lambda L)) = sinc(pi X a/d) = sinc(pi X/4)
d, a = sp.symbols('d a', positive=True)
ok6 = sp.simplify((sp.pi*X*a/d).subs(a, d/4) - sp.pi*X/4) == 0
print("envelope first zero at X =", sp.solve(sp.Eq(sp.pi*X/4, sp.pi), X))
print("PASS" if all([ok, ok2, ok3, ok4, ok5, ok6]) else "FAIL")
