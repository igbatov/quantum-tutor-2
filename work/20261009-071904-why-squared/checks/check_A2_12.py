# Check-yourself: "fourth power of the shadow ... splitter at 60°, what would the two exits add up to,
# and which of the observations (1) to (5) does that contradict?"  Expected answer: 62.5%.
import sympy as sp
t = sp.pi/3
pa, pr = sp.cos(t)**4, sp.sin(t)**4
tot = sp.nsimplify(pa + pr)
print(f"pass {pa} = {float(pa):.4f}, reflect {pr} = {float(pr):.4f}, total {tot} = {float(tot)*100:.1f}%")
ok = tot == sp.Rational(5, 8)
print("contradicts (3) (total constant at 100%):", tot != 1)
print("also off (2): pass 6.25% vs measured 25%; and pass+reflect at 60° = at 30° by symmetry:",
      sp.nsimplify(sp.cos(sp.pi/6)**4 + sp.sin(sp.pi/6)**4))
print("PASS" if ok else "FAIL")
