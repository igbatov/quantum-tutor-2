# Claims (candidate-B §3, Steps 1-4): "dU/dt = A U(t)", "U(t)=e^{At}",
# "Unitarity of U <=> Hermiticity of H", H = i hbar A, with explicit 2x2 matrices.
import numpy as np, sympy as sp
from scipy.linalg import expm
rng = np.random.default_rng(1); hb = 1.054571817e-34; tol = 1e-9
ok = True
# random 2x2 Hermitian H (energy units ~ hbar*1e9 /s)
X = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)); H = (X + X.conj().T)/2 * hb*1e9
U = lambda t: expm(-1j*H*t/hb)
s, t = 3.1e-9, 1.7e-9
c1 = np.allclose(U(s)@U(t), U(s+t), atol=tol); ok &= c1
c2 = np.allclose(U(t).conj().T@U(t), np.eye(2), atol=tol); ok &= c2
# Step 1: numerical derivative of the group = A U(t), A = dU/dt at 0
e = 1e-15; A = (U(e)-U(-e))/(2*e)
dU = (U(t+e)-U(t-e))/(2*e)
c3 = np.allclose(dU, A@U(t), rtol=1e-5, atol=1e-3*np.abs(A).max()); ok &= c3
c4 = np.allclose(1j*hb*A, H, rtol=1e-5, atol=1e-6*np.abs(H).max()); ok &= c4   # H = i hbar A
c5 = np.allclose(A.conj().T + A, 0, atol=1e-6*np.abs(A).max()); ok &= c5       # A^dag + A = 0
# Step 2 uniqueness: solve V' = A V numerically, compare with expm(A t)
from scipy.integrate import solve_ivp
Ad = -1j*H/hb
f = lambda tt, y: (Ad@y.reshape(2,2)).ravel()
sol = solve_ivp(f, [0, t], np.eye(2, dtype=complex).ravel(), rtol=1e-11, atol=1e-13)
c6 = np.allclose(sol.y[:, -1].reshape(2,2), expm(Ad*t), atol=1e-7); ok &= c6
# Converse fails for non-Hermitian H: U not unitary
Hn = H + 0.3j*hb*1e9*np.eye(2)
Un = expm(-1j*Hn*t/hb); c7 = not np.allclose(Un.conj().T@Un, np.eye(2), atol=1e-3); ok &= c7
# Symbolic: d/dt (U^dag U) = U^dag (A^dag + A) U for general 2x2 A, U = e^{At} (sympy, Pauli basis)
a0,a1,a2,a3,tt = sp.symbols('a0:4 t', real=True)
sx = sp.Matrix([[0,1],[1,0]]); sy = sp.Matrix([[0,-sp.I],[sp.I,0]]); sz = sp.Matrix([[1,0],[0,-1]])
Hs = a0*sp.eye(2) + a1*sx + a2*sy + a3*sz      # general Hermitian 2x2
assert sp.simplify(Hs - Hs.H) == sp.zeros(2)
As = -sp.I*Hs                                  # hbar = 1
Us = sp.simplify((As*tt).exp())
D = Us.H*Us - sp.eye(2)   # sympy cannot fully simplify sqrt terms; test at random points
c8 = all(abs(complex(sp.N(D[i].subs({a0:.3,a1:-1.2,a2:.7,a3:2.1,tt:v})))) < 1e-12
         for i in range(4) for v in (0.4, 1.9, 7.3)); ok &= c8
c9 = sp.simplify(Us.diff(tt) - As*Us) == sp.zeros(2); ok &= c9
# Larmor closed form: H=(hbar w/2) sz -> diag(e^{-iwt/2}, e^{iwt/2}) = cos 1 - i sin sz
w = sp.symbols('omega', positive=True)
UL = sp.simplify((-sp.I*w*tt/2*sz).exp())
c10 = sp.simplify(UL - (sp.cos(w*tt/2)*sp.eye(2) - sp.I*sp.sin(w*tt/2)*sz)).rewrite(sp.exp).expand() == sp.zeros(2); ok &= c10
print("composition", c1, "unitary", c2, "dU=AU", c3, "H=i hbar A", c4, "A^+A=0", c5,
      "ODE uniqueness", c6, "nonHermitian->nonunitary", c7, "sym unitary", c8, "sym dU=AU", c9, "Larmor form", c10)
print("PASS" if ok else "FAIL")
