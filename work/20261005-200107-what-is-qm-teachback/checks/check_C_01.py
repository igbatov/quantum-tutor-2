# Claim: "Ordinary light meets a vertical filter ... Half" ; passed photons are vertical
import numpy as np, sympy as sp
th = sp.symbols('theta', real=True)
# unpolarized = uniform average of cos^2 over angle
avg = sp.integrate(sp.cos(th)**2, (th, 0, 2*sp.pi))/(2*sp.pi)
# density-matrix version
rho = np.eye(2)/2
PV = np.array([[0,0],[0,1.0]])  # basis (H, V)
p = np.trace(PV@rho)
post = PV@rho@PV/p
ok = avg == sp.Rational(1,2) and abs(p-0.5)<1e-12 and np.allclose(post, PV)
print("avg cos^2 =", avg, " Tr(P_V rho) =", p, " post-state =", post.tolist())
print("PASS" if ok else "FAIL")
