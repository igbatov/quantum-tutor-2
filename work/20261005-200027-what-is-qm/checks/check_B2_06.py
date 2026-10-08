# Claims: "45° photon's answer to a 45° filter is certain ... vertical filter is 50/50";
# "an answer is certain only when the arrow lies right along that answer's direction";
# "no way of preparing a photon makes its answers to both a vertical and a 45° filter certain"
import numpy as np, sympy as sp
def u(a): a = np.radians(a); return np.array([np.sin(a), np.cos(a)])
print("45 photon: P(45)=%.3f, P(V)=%.3f" % ((u(45)@u(45))**2, (u(45)@u(0))**2))
# linear arrows: certain (prob 0 or 1) for V-filter only at 0, 90, 180 deg
t = sp.symbols('t', real=True)
sols = sorted(set(sp.solveset(sp.cos(t)**2*(1-sp.cos(t)**2), t, sp.Interval(0, sp.pi))))
print("angles (rad) where the V-filter answer is certain:", sols)
# all states (pure+mixed, incl. complex) via Bloch vector r: P(V)=(1+z)/2, P(45)=(1+x)/2; certainty c = max(P,1-P)
best = 0
for th in np.linspace(0, np.pi, 721):
    for ph in np.linspace(0, 2*np.pi, 721):
        x, z = np.sin(th)*np.cos(ph), np.cos(th)
        best = max(best, min((1+abs(z))/2, (1+abs(x))/2))
print("max over all states of min(certainty_V, certainty_45) = %.4f (analytic %.4f)" % (best, (1+1/np.sqrt(2))/2))
sz = sp.Matrix([[1,0],[0,-1]]); sx = sp.Matrix([[0,1],[1,0]]); print("[sz,sx] =", (sz*sx-sx*sz).tolist())
ok = abs((u(45)@u(0))**2-0.5) < 1e-12 and sols == [0, sp.pi/2, sp.pi] and best < 0.86
print("PASS" if ok else "FAIL")
