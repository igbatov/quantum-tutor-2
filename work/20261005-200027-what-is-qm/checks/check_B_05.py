# Claim: "a 45 photon's answer ... to a vertical filter is 50/50"
# Claim: "an answer is certain only when the arrow lies right along that answer's direction"
# Claim: "no way of preparing a photon makes both answers certain" (incl. complex and mixed states)
# Claim: trade-off of Heisenberg kind -> the two questions are incompatible (non-commuting)
import numpy as np
V, H = np.array([1,0], complex), np.array([0,1], complex)
D = (V+H)/np.sqrt(2)
p = abs(np.vdot(V, D))**2
print("45 photon at vertical filter: pass", p, " block", 1-p)
# certainty only along direction: P(a|psi)=1 iff |<a|psi>|=1 (Cauchy-Schwarz); exact solve for real arrows
import sympy as sp
t = sp.symbols('t', real=True)
sols = sorted(set(sp.solveset(sp.cos(t)**2 - 1, t, sp.Interval(0, sp.pi)))
              | set(sp.solveset(sp.cos(t)**2, t, sp.Interval(0, sp.pi))))
cert_deg = [float(sp.deg(x)) for x in sols]
print("real angles (deg) in [0,180] where V/H answer certain:", cert_deg)
# Bloch ball scan incl. mixed: certainty of Z question = |z|, of X question = |x|
rng = np.random.default_rng(0)
v = rng.normal(size=(400000, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
r = rng.random(400000)**(1/3); v *= r[:, None]
best = np.max(np.minimum((1+abs(v[:,2]))/2, (1+abs(v[:,0]))/2))
print("max over states of min(prob of likelier answer to V/H, to diagonal) =", best,
      " analytic (1+1/sqrt2)/2 =", (1+1/np.sqrt(2))/2)
sz = np.diag([1,-1]).astype(complex); sx = np.array([[0,1],[1,0]], complex)
comm = sz@sx - sx@sz
print("[sz,sx] =\n", comm)
ok = abs(p-0.5)<1e-12 and set(cert_deg) == {0.0, 90.0, 180.0} \
     and best < 0.86 and np.linalg.norm(comm) > 1
print("PASS" if ok else "FAIL")
