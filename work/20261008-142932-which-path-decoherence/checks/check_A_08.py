# Claims (Model 1): "overlap, the cosine of theta, is the stripe strength"; "sine of theta is the
# telling-apart power" (best guess, rescaled 0..1); theta=60 -> 0.5 and ~0.87; budget
# V^2 + D^2 = 1 for an ideal tag, <= 1 for a tag "in a random state of its own".
import numpy as np
rng = np.random.default_rng(0)
def helstrom_D(r1, r2, w=0.5):
    # best success prob = 1/2 + 1/2 ||w r1 - (1-w) r2||_1 ; rescaled D = 2P-1
    ev = np.linalg.eigvalsh(w*r1-(1-w)*r2); return np.sum(np.abs(ev))
ok = True
for th in np.radians([0, 30, 60, 90]):
    a = np.array([1, 0]); b = np.array([np.cos(th), np.sin(th)])
    # stripe strength: P(X) ∝ |psi1|^2+|psi2|^2 + 2 Re(psi1 psi2* <b|a>) -> contrast |<a|b>|
    V = abs(np.vdot(b, a)); D = helstrom_D(np.outer(a, a), np.outer(b, b))
    print(f"theta={np.degrees(th):4.0f}: V={V:.4f} (cos={np.cos(th):.4f})  D={D:.4f} (sin={np.sin(th):.4f})  V^2+D^2={V*V+D*D:.6f}")
    ok &= abs(V-np.cos(th)) < 1e-12 and abs(D-np.sin(th)) < 1e-12 and abs(V*V+D*D-1) < 1e-12
# mixed tags: tag starts in random mixed state rho0 (dim 3), left/right apply random unitaries
def randU(n):
    q, r = np.linalg.qr(rng.normal(size=(n, n))+1j*rng.normal(size=(n, n))); return q
worst = 0; strict = 0
for _ in range(5000):
    n = 3; G = rng.normal(size=(n, n))+1j*rng.normal(size=(n, n)); rho = G@G.conj().T; rho /= np.trace(rho)
    UL, UR = randU(n), randU(n)
    V = abs(np.trace(UR.conj().T@UL@rho)); D = helstrom_D(UL@rho@UL.conj().T, UR@rho@UR.conj().T)
    s = V*V+D*D; worst = max(worst, s); strict += s < 1-1e-6
print(f"mixed tags: max V^2+D^2 = {worst:.6f}; strictly below 1 in {strict}/5000 cases")
ok &= worst <= 1+1e-9
print("PASS" if ok else "FAIL")
