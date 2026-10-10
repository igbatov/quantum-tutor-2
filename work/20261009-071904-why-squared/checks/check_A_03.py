# Claim: "only the second keeps the total at exactly 1 for every angle;
#  any smaller power overshoots ... any larger one undershoots, worst at 45°"
# Tested over integer AND non-integer p (dense grid), plus symbolic argument.
import numpy as np, sympy as sp

# Symbolic: at 45 deg, S(p) = 2*(1/sqrt2)^p = 2^(1-p/2); equals 1 iff p = 2 (all real p)
p = sp.symbols('p', real=True)
S45 = 2*(1/sp.sqrt(2))**p
sol = sp.solve(sp.Eq(S45, 1), p)
print("solutions of S_p(45deg)=1 over reals:", sol)

th = np.linspace(1e-6, np.pi/2 - 1e-6, 20001)
interior = (th > np.radians(0.01)) & (th < np.radians(89.99))
ps = np.concatenate([np.linspace(0.05, 6, 1192), [1.9, 1.99, 2.01, 2.1, 0.5, 1.5, 2.5, 3, 4]])
ok = True
for pp in ps:
    S = np.cos(th)**pp + np.sin(th)**pp
    dev = np.abs(S - 1)
    if abs(pp - 2) < 1e-12:
        continue
    if pp < 2 and not np.all(S[interior] > 1): ok = False; print("no overshoot p=", pp)
    if pp > 2 and not np.all(S[interior] < 1): ok = False; print("no undershoot p=", pp)
    worst = np.degrees(th[np.argmax(dev)])
    if abs(worst - 45) > 0.01: ok = False; print("worst not at 45 for p=", pp, worst)
S2 = np.cos(th)**2 + np.sin(th)**2
print("p=2 max |S-1| =", np.max(np.abs(S2 - 1)))
ok &= np.max(np.abs(S2 - 1)) < 1e-12
for pp in [1.9, 1.99, 2.01, 2.1]:
    print(f"p={pp}: S(45deg) = {2**(1-pp/2):.5f}")
# Non-positive powers (not 'plain powers' in the physical sense, reported for completeness)
for pp in [0, -1]:
    S = np.cos(th[interior])**pp + np.sin(th[interior])**pp
    print(f"p={pp}: S ranges {S.min():.3f}..{S.max():.1f} (p=0: constant 2; p<0: deviation largest near 0/90, smallest at 45)")
print("PASS (for all p>0; uniqueness of p=2 holds for every real p)" if ok and sol == [2] else "FAIL")
