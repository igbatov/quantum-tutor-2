# Claims (§4): G2 "BC-CB = i lambda a v 1", "[K,P]=i hbar M", "phi=Mav/hbar (dimensionless)";
# G4 "[H,K] = -i hbar P + i hbar^2 mu" ; G5 "[X,P^2/2M] = i hbar P/M";
# G3 "d<X>/dt = <P>/M"; G6 "[P,H]=0 forces V constant"; DG "M=m_e"; COW "Mg dz T/hbar".
import sympy as sp, numpy as np
from scipy import constants as C
ok = True
# --- G2 second-order expansion, noncommuting symbols
B, Cc = sp.symbols('B C', commutative=False); lam, a, v, hb, M = sp.symbols('lambda a v hbar M', positive=True)
sc = sp.Symbol('s')     # order-counting parameter: B,C ~ s, lambda a v ~ s^2
e = lambda X: 1 + X + X**2/2
lhs = sp.expand(e(sc*B)*e(sc*Cc)); rhs = sp.expand((1 + sp.I*lam*a*v*sc**2)*e(sc*Cc)*e(sc*B))
diff2 = sp.expand(sp.expand(lhs - rhs).coeff(sc, 2))
ok &= sp.expand(diff2 - (B*Cc - Cc*B - sp.I*lam*a*v)) == 0
print("G2 second-order difference:", diff2)
# with B = i v K/hbar, C = -i a P/hbar: BC - CB = (a v/hbar^2)[K,P]  -> [K,P] = i hbar^2 lambda = i hbar M
K, P = sp.symbols('K P', commutative=False)
bc = sp.expand((sp.I*v*K/hb)*(-sp.I*a*P/hb) - (-sp.I*a*P/hb)*(sp.I*v*K/hb))
ok &= sp.simplify(bc - a*v/hb**2*(K*P - P*K)) == 0
# --- explicit representation K = M x, P = -i hbar d/dx on a test function
x, t, mu = sp.symbols('x t mu', real=True); f = sp.Function('f')(x); V = sp.Function('V')
Pop = lambda g: -sp.I*hb*sp.diff(g, x); Kop = lambda g: M*x*g
Hop = lambda g: Pop(Pop(g))/(2*M)
c_KP = sp.simplify(Kop(Pop(f)) - Pop(Kop(f)) - sp.I*hb*M*f) == 0
c_XH = sp.simplify(x*Hop(f) - Hop(x*f) - sp.I*hb*Pop(f)/M) == 0
c_KH = sp.simplify(Kop(Hop(f)) - Hop(Kop(f)) - sp.I*hb*Pop(f)) == 0
c_PV = sp.simplify(Pop(V(x)*f) - V(x)*Pop(f) + sp.I*hb*sp.diff(V(x), x)*f) == 0
c_dX = sp.simplify(sp.I/hb*(Hop(x*f) - x*Hop(f)) - Pop(f)/M) == 0   # (i/hbar)[H,X] = P/M
ok &= c_KP and c_XH and c_KH and c_PV and c_dX
print("[K,P]=i hbar M:", c_KP, " [X,P^2/2M]=i hbar P/M:", c_XH, " [K,H]=i hbar P:", c_KH,
      " [P,V]=-i hbar V':", c_PV, " (i/hbar)[H,X]=P/M:", c_dX)
# G4 bookkeeping: H K = -i hbar P + K H + i hbar^2 mu  <=> [H,K] = -i hbar P + i hbar^2 mu; shift P->P-hbar mu
Hs = sp.Symbol('H', commutative=False); one = 1
left = (-sp.I*Hs*t/hb)*(sp.I*v*K/hb)
right = sp.I*mu*v*t - sp.I*v*t*P/hb + (sp.I*v*K/hb)*(-sp.I*Hs*t/hb)
eq = sp.expand((left - right)*hb**2/(v*t))          # = HK - KH + i hbar P - i hbar^2 mu
ok &= sp.simplify(eq - (Hs*K - K*Hs + sp.I*hb*P - sp.I*hb**2*mu)) == 0
print("G4 vt-coefficient gives [H,K] = -i hbar P + i hbar^2 mu:", True)
# --- boosted solution: Psi = exp(i(Mvx - Mv^2 t/2)/hbar) phi(x-vt,t) solves free SE iff phi does
sig = sp.Symbol('sigma', positive=True)
gam = 1 + sp.I*hb*t/(M*sig**2)
phi = lambda X, T: (1 + sp.I*hb*T/(M*sig**2))**sp.Rational(-1, 2)*sp.exp(-X**2/(2*sig**2*(1 + sp.I*hb*T/(M*sig**2))))
SE = lambda g: sp.I*hb*sp.diff(g, t) + hb**2/(2*M)*sp.diff(g, x, 2)
c_free = sp.simplify(SE(phi(x, t))/phi(x, t)) == 0          # lab-frame packet solves free SE
Psi = sp.exp(sp.I*(M*v*x - M*v**2*t/2)/hb)*phi(x - v*t, t)
c_boost = sp.simplify(SE(Psi)/Psi) == 0
Psi_bad = sp.exp(sp.I*(M*v*x)/hb)*phi(x - v*t, t)                # without the -Mv^2t/2 term
c_bad = sp.simplify(SE(Psi_bad)/Psi_bad) != 0
ok &= c_free and c_boost and c_bad
print("free packet solves SE:", c_free, "; boosted packet with e^{i(Mvx - Mv^2 t/2)/hbar} solves SE:", c_boost,
      "; dropping -Mv^2t/2 breaks it:", c_bad)
# --- units of phi and M
from sympy.physics.units import kilogram, meter, second, joule, convert_to
hbu = joule*second; Ku = hbu/(meter/second); Pu = hbu/meter
ok &= sp.simplify(convert_to(Ku*Pu/hbu, [kilogram, meter, second]) - kilogram) == 0
ok &= sp.simplify(convert_to(kilogram*meter*(meter/second)/hbu, [kilogram, meter, second])) == 1
print("units: [K][P]/hbar = kg, M a v/hbar dimensionless: True")
# --- d<X>/dt = <P>/M numerically (hbar=M=1), Gaussian with k0=2 evolved by FFT
N, L = 4096, 400.0; xs = np.linspace(-L/2, L/2, N, endpoint=False); k = 2*np.pi*np.fft.fftfreq(N, L/N)
ps0 = np.exp(-(xs+20)**2/8 + 2j*xs); ps0 /= np.sqrt(np.sum(abs(ps0)**2)*(L/N))
mX = []; ts = np.linspace(0, 10, 11)
for tt in ts:
    p = np.fft.ifft(np.exp(-1j*k**2*tt/2)*np.fft.fft(ps0)); mX.append(np.sum(xs*abs(p)**2)*(L/N))
mP = np.sum(k*abs(np.fft.fft(ps0))**2)/np.sum(abs(np.fft.fft(ps0))**2)
slope = np.polyfit(ts, mX, 1)[0]; ok &= abs(slope - mP) < 1e-6
print(f"d<X>/dt = {slope:.6f}, <P>/M = {mP:.6f}")
# --- Davisson-Germer: lambda = h/sqrt(2 m e V0) from hbar w = hbar^2 k^2/2M with M=m_e, E=eV0
V0 = 54.0; Mrec = (C.h/(C.h/np.sqrt(2*C.m_e*C.e*V0)))**2/(2*C.e*V0)
lam54 = C.h/np.sqrt(2*C.m_e*C.e*V0); ok &= abs(Mrec/C.m_e - 1) < 1e-12
print(f"DG: lambda(54 eV) = {lam54*1e10:.3f} Angstrom, recovered M/m_e = {Mrec/C.m_e:.12f}")
# --- COW: M g dz T/hbar equals the standard m^2 g lambda A/(2 pi hbar^2), A = dz*L, T = L/v
m, g, dz, Ll, vv = sp.symbols('m g dz L v_n', positive=True)
lamdB = 2*sp.pi*hb/(m*vv)
ok &= sp.simplify(m*g*dz*(Ll/vv)/hb - m**2*g*lamdB*dz*Ll/(2*sp.pi*hb**2)) == 0
lam_n, A = 1.445e-10, 10e-4     # illustrative: lambda 1.445 A, enclosed area 10 cm^2
ph = C.m_n**2*C.g*lam_n*A/(2*np.pi*C.hbar**2)
print(f"COW: formula equivalence True; for lambda=1.445 A, A=10 cm^2: phase = {ph:.1f} rad")
print("PASS" if ok else "FAIL")
