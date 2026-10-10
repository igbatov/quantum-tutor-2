# Claim: "one real number per exit allows at most two mutually even-bet sorters"
# Also: D chance = (1+sin2θ)/2; even at H/V -> θ=45,135 -> sure bet at D/A; general monotone rule: D shadow 0 or ±1
import sympy as sp, numpy as np
th = sp.symbols('theta', real=True)
Dsh = (sp.cos(th)+sp.sin(th))/sp.sqrt(2)
ok1 = sp.simplify(sp.expand_trig(Dsh**2 - (1+sp.sin(2*th))/2)) == 0
sols = sp.solveset(sp.Eq(sp.cos(th)**2, sp.Rational(1,2)), th, sp.Interval.Ropen(0, sp.pi))
print("D chance identity:", ok1, " H/V-even solutions in [0,pi):", sols)
Dvals = [sp.nsimplify(Dsh.subs(th, s)**2) for s in sols]
print("D chances at those:", Dvals)
ok2 = set(Dvals) == {0, 1} and sols == sp.FiniteSet(sp.pi/4, 3*sp.pi/4)
# brute-force: any theta with both |cos|=|sin| and |D shadow|=|A shadow| ?
t = np.linspace(0, np.pi, 2_000_001)
c, s = np.cos(t), np.sin(t)
d, a = (c+s)/np.sqrt(2), (c-s)/np.sqrt(2)
gap = np.maximum(np.abs(np.abs(c)-np.abs(s)), np.abs(np.abs(d)-np.abs(a)))
print("min over theta of max(| |c|-|s| |, | |D|-|A| |) =", gap.min())
ok3 = gap.min() > 0.5
# general: s0 = 1/sqrt2 forced; D shadow at |c|=|s|=1/sqrt2
vals = sorted({round(float((sc*1+ss*1)/np.sqrt(2)/np.sqrt(2)),12) for sc in (1,-1) for ss in (1,-1)})
print("D shadow values when |cos|=|sin|=1/sqrt2:", vals)
ok4 = vals == [-1.0, 0.0, 1.0]
print("PASS" if ok1 and ok2 and ok3 and ok4 else "FAIL")
