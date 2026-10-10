# Claims (final-C, short answer and two-slit section):
#  "plain size, the cube and every other power predict a genuine three-way effect"
#  "a number the square rule predicts to be zero at every spot, which no other power manages"
import numpy as np
rng = np.random.default_rng(1)
def I3(z, p):
    a, b, c = z
    f = lambda w: np.abs(w)**p
    return f(a+b+c) - f(a+b) - f(b+c) - f(a+c) + f(a) + f(b) + f(c)
Z = rng.normal(size=(3, 20000)) + 1j*rng.normal(size=(3, 20000))
# (1) random complex triples, exponents 0..20
ps = np.round(np.arange(0.0, 20.0001, 0.01), 4)
zero_ps = []
for p in ps:
    v = I3(Z, p) if p > 0 else np.ones(Z.shape[1])   # size^0 = 1 for every nonzero hand: 1-3+3 = 1
    scale = np.max(np.abs(Z.sum(0)))**p + 1
    if np.max(np.abs(v)) < 1e-9*scale: zero_ps.append(p)
print("exponents in [0,20] (step 0.01) with leftover = 0 for all random hands:", zero_ps)
# (2) the real screen: far-field three-slit pattern, d = 4a, any p != 2 leaves a leftover somewhere
u = np.linspace(-3, 3, 6001); s = u/4
env = np.sinc(s); w = np.exp(2j*np.pi*u)
hands = np.array([env/w, env, env*w])
bad = []
for p in [0.5, 1, 1.5, 1.9, 1.99, 2.01, 2.1, 2.5, 3, 4, 6]:
    m = np.max(np.abs(I3(hands, p)))
    print(f"far-screen max|leftover|, p={p}: {m:.3e}")
    if m < 1e-6: bad.append(p)
m2 = np.max(np.abs(I3(hands, 2)))
print(f"far-screen max|leftover|, p=2: {m2:.1e}")
ok = zero_ps == [2.0] and not bad and m2 < 1e-12
print("PASS" if ok else "FAIL")
