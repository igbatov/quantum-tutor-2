# Claims (Flow): continuity equation d|psi|^2/dt = -dJ/dx with
#  "J = (i hbar/2m)(psi conj(psi)' - conj(psi) psi') = (hbar/m) Im(conj(psi) psi')";
#  intermediate "(i hbar/2m)(conj(psi) psi'' - psi conj(psi)'')"; "real psi => J = 0";
#  "<p> = 0" for real psi vanishing at infinity; "psi = A e^{ikx}: J = (hbar k/m)|A|^2";
#  "If psi were real at all times ... H psi = 0".
import sympy as sp
import numpy as np
hb, m = sp.symbols('hbar m', positive=True)
# real symbols: u0..u3 = u and its x-derivatives, same for v; V0, V1 = V and V'
u0, u1, u2, u3, v0, v1, v2, v3, V0, V1 = sp.symbols('u0 u1 u2 u3 v0 v1 v2 v3 V0 V1', real=True)
psi, psi1, psi2 = u0 + sp.I*v0, u1 + sp.I*v1, u2 + sp.I*v2
c = sp.conjugate
chain = [(u0, u1), (u1, u2), (u2, u3), (v0, v1), (v1, v2), (v2, v3), (V0, V1)]
def D(e):  # d/dx
    return sum(sp.diff(e, a)*b for a, b in chain)
ok = True
dpsi = (-(hb**2/(2*m))*psi2 + V0*psi)/(sp.I*hb)          # Schrodinger equation
drho = sp.expand(c(psi)*dpsi + psi*c(dpsi))
inter = sp.I*hb/(2*m)*(c(psi)*psi2 - psi*c(psi2))
ok &= sp.simplify(sp.expand(drho - inter)) == 0
J = sp.I*hb/(2*m)*(psi*c(psi1) - c(psi)*psi1)
J2 = hb/m*sp.im(sp.expand(c(psi)*psi1))
ok &= sp.simplify(sp.expand(J - J2)) == 0
ok &= sp.simplify(sp.expand(drho + D(J))) == 0
ok &= sp.simplify(sp.expand(D(c(psi)*psi1 - psi*c(psi1)) - (c(psi)*psi2 - psi*c(psi2)))) == 0
print("continuity + both J forms + derivative identity:", ok)
Jreal = sp.simplify(J.subs({v0: 0, v1: 0}))
print("J for real psi:", Jreal); ok &= Jreal == 0
# <p> for a real normalizable psi
X = np.linspace(-30, 30, 20001); dx = X[1] - X[0]
f = np.exp(-(X - 1.3)**2/3)*(1 + 0.4*np.sin(2*X)); f /= np.sqrt((f**2).sum()*dx)
p_mean = (-1j*f*np.gradient(f, dx)).sum()*dx
print("<p> real psi (hbar=1):", p_mean); ok &= abs(p_mean) < 1e-8
# plane wave and standing wave
x, k = sp.symbols('x k', real=True); Aa = sp.symbols('A')
pw = Aa*sp.exp(sp.I*k*x)
Jpw = sp.simplify(sp.I*hb/(2*m)*(pw*sp.diff(c(pw), x) - c(pw)*sp.diff(pw, x)))
print("J plane wave:", Jpw); ok &= sp.simplify(Jpw - hb*k/m*Aa*c(Aa)) == 0
cw = sp.cos(k*x)
Jcw = sp.simplify(sp.I*hb/(2*m)*(cw*sp.diff(cw, x) - cw*sp.diff(cw, x)))
print("J standing wave:", Jcw); ok &= Jcw == 0
# real at all times: i hbar u_t purely imaginary, H u real (V real) -> both vanish
ut = sp.symbols('u_t', real=True)
r1 = sp.re(sp.I*hb*ut) == 0; r2 = sp.im(-(hb**2/(2*m))*u2 + V0*u0) == 0
print("real-at-all-times: lhs imaginary, rhs real ->", r1, r2); ok &= r1 and r2
print("PASS" if ok else "FAIL")
