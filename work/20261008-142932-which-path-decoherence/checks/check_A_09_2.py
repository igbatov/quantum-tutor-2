# Claims (Model 1): overlap cos(theta) = stripe strength; sin(theta) = telling-apart power; theta=60 ->
# 0.5 and ~0.87; budget equality for an ideal tag, inequality for a tag "in a random state of its own";
# "A complex overlap ... also shifts the stripes sideways".
import numpy as np
rng = np.random.default_rng(0)
def D_hel(r1, r2): return np.sum(np.abs(np.linalg.eigvalsh(0.5*r1-0.5*r2)))
ok = True
for th in np.radians([0, 30, 60, 90]):
    a = np.array([1, 0]); b = np.array([np.cos(th), np.sin(th)])
    Vv = abs(np.vdot(a, b)); D = D_hel(np.outer(a, a), np.outer(b, b))
    print(f"theta {np.degrees(th):3.0f}: V={Vv:.4f} D={D:.4f} V^2+D^2={Vv**2+D**2:.6f}")
    ok &= abs(Vv-np.cos(th)) < 1e-12 and abs(D-np.sin(th)) < 1e-12
def randU(n):
    q, _ = np.linalg.qr(rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))); return q
worst = 0
for _ in range(3000):
    G = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3)); rho = G@G.conj().T; rho /= np.trace(rho).real
    UL, UR = randU(3), randU(3)
    Vv = abs(np.trace(UR.conj().T@UL@rho)); D = D_hel(UL@rho@UL.conj().T, UR@rho@UR.conj().T); worst = max(worst, Vv**2+D**2)
print(f"mixed tags: max V^2+D^2 = {worst:.4f}")
ok &= worst <= 1+1e-9
# complex overlap: P(X) = 1 + |g| cos(2 pi X - arg g)  -> shift arg(g)/(2pi), contrast |g|
X = np.linspace(-0.5, 0.5, 100001)
for g in [0.6, 0.6*np.exp(1j*np.pi/2)]:
    Pp = np.abs(np.exp(1j*np.pi*X))**2 + 1 + 2*np.real(np.exp(1j*np.pi*X)*np.conj(np.exp(-1j*np.pi*X))*np.conj(g))
    xpk = X[np.argmax(Pp)]; Vc = (Pp.max()-Pp.min())/(Pp.max()+Pp.min())
    print(f"overlap {np.round(g,3)}: contrast {Vc:.3f}, peak at X = {xpk:+.3f}")
    ok &= abs(Vc-abs(g)) < 1e-6 and abs(xpk-np.angle(g)/(2*np.pi)) < 1e-4
print("PASS" if ok else "FAIL")
