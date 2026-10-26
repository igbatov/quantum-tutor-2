# Claims: "ideally sin^2(Omega t/2)" (Rabi, §1); two back-to-back pulses 30+50 us land on
# the single-pulse curve at 80 us (figure spec, "phase-continuous across pulses");
# Larmor "<sx>=cos wt, <sy>=sin wt", "at wt=2pi psi=-psi(0)", "returns at 4pi";
# Rauch "intensity oscillates in phi with period 4pi".
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp
sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1,-1]).astype(complex)
ok = True
Om = 2*np.pi*10e3; t1, t12 = 30e-6, 80e-6
# (a) rotating frame, RWA: H_rot = (hbar Om/2) sx, time independent
Ur = lambda t: expm(-1j*Om*t/2*sx)
up = np.array([1,0],complex)
P = lambda t: abs((Ur(t)@up)[1])**2
ts = np.linspace(0, 200e-6, 401)
errR = max(abs(P(t) - np.sin(Om*t/2)**2) for t in ts); ok &= errR < 1e-12
two = Ur(t12-t1)@Ur(t1)@up; one = Ur(t12)@up
c_two = np.allclose(two, one, atol=1e-12); ok &= c_two
print(f"RWA max|P-sin^2|={errR:.1e}; two-pulse state == single 80us state: {c_two}; "
      f"P(30us)={P(t1):.4f}, P(80us)={P(t12):.4f}")
# (b) full lab-frame model, linear drive 2*Om*cos(w t + ph) sx/2 (no RWA), w0 = 2pi*1 MHz
w0 = 2*np.pi*1e6
def evolve(psi, ta, tb, ph, t_ref):
    f = lambda t, y: -1j*((w0/2)*sz + Om*np.cos(w0*(t-t_ref)+ph)*sx)@y
    return solve_ivp(f, [ta, tb], psi, rtol=1e-10, atol=1e-12, max_step=2e-8).y[:, -1]
p1 = evolve(up, 0, t1, 0.0, 0.0)
p_cont = evolve(p1, t1, t12, 0.0, 0.0)          # drive keeps its phase (phase-continuous)
p_restart = evolve(p1, t1, t12, 0.0, t1)        # drive restarted with phase 0 at t1
Pc, Pr, Pid = abs(p_cont[1])**2, abs(p_restart[1])**2, np.sin(Om*t12/2)**2
print(f"lab model P(80us): phase-continuous {Pc:.4f}, restarted {Pr:.4f}, sin^2 {Pid:.4f}")
ok &= abs(Pc - Pid) < 0.01                       # Bloch-Siegert corrections ~ Om/w0
pts = [evolve(up, 0, t, 0.0, 0.0) for t in np.linspace(0, 200e-6, 21)[1:]]
dev = max(abs(abs(p[1])**2 - np.sin(Om*t/2)**2) for p, t in zip(pts, np.linspace(0,200e-6,21)[1:]))
print(f"lab model max deviation from sin^2 on 0..200us grid: {dev:.2e} (smooth, 'ideally' justified)")
ok &= dev < 0.01
# (c) Larmor
w = 1.0; psi0 = np.array([1,1],complex)/np.sqrt(2)
for t in np.linspace(0, 4*np.pi, 13):
    ps = expm(-1j*w*t/2*sz)@psi0
    ex, ey = np.vdot(ps, sx@ps).real, np.vdot(ps, sy@ps).real
    ok &= abs(ex-np.cos(w*t)) < 1e-12 and abs(ey-np.sin(w*t)) < 1e-12
    ok &= abs(ex - 2*np.real(np.conj(ps[0])*ps[1])) < 1e-12
p2 = expm(-1j*np.pi*sz)@psi0; p4 = expm(-1j*2*np.pi*sz)@psi0
c_sign = np.allclose(p2, -psi0) and np.allclose(p4, psi0); ok &= c_sign
print("Larmor <sx>,<sy> match; psi(2pi)=-psi0, psi(4pi)=psi0:", c_sign)
# (d) Rauch: I(phi) ∝ |psi + U(phi) psi|^2, random spin state; unpolarized too
rng = np.random.default_rng(0); v = rng.normal(size=2)+1j*rng.normal(size=2); v /= np.linalg.norm(v)
phis = np.linspace(0, 8*np.pi, 801)
I = np.array([np.linalg.norm(v + expm(-1j*f/2*sz)@v)**2/4 for f in phis])
c_I = np.allclose(I, (1+np.cos(phis/2))/2, atol=1e-12); ok &= c_I
i2 = np.argmin(abs(phis-2*np.pi)); i4 = np.argmin(abs(phis-4*np.pi))
print(f"Rauch I=(1+cos(phi/2))/2: {c_I}; I(0)={I[0]:.3f}, I(2pi)={I[i2]:.3f}, I(4pi)={I[i4]:.3f}")
print("PASS" if ok else "FAIL")
