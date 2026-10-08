# Claim: "complex numbers ... (needed already for light whose wiggle goes round in circles)"
# Claim: arrows "turning smoothly in time between measurements as the Schrodinger equation describes" (length stays 1)
import numpy as np
from scipy.linalg import expm
th = np.linspace(0, np.pi, 721)
def pass_probs(a, b):  # amplitude vector (a along V, b along H); linear filter at angle th from V
    return np.abs(a*np.cos(th) + b*np.sin(th))**2
# Circular light: passes every linear polarizer half the time (classically: 50% intensity at all angles).
circ = pass_probs(1/np.sqrt(2), 1j/np.sqrt(2))
# Best real unit arrow at matching that: minimize max deviation over phi
phis = np.linspace(0, np.pi, 3601)
dev_real = min(np.max(np.abs(pass_probs(np.cos(f), np.sin(f)) - 0.5)) for f in phis)
print("complex (1,i)/sqrt2: max |P-0.5| =", np.max(abs(circ-0.5)))
print("best real arrow: max |P-0.5| =", dev_real)
# Schrodinger evolution: random Hermitian H, check norm preserved and continuity
rng = np.random.default_rng(0)
M = rng.normal(size=(2,2)) + 1j*rng.normal(size=(2,2)); Hm = (M + M.conj().T)/2
psi0 = np.array([1,0], complex)
ts = np.linspace(0, 5, 501)
psis = np.array([expm(-1j*Hm*t) @ psi0 for t in ts])
norms = np.linalg.norm(psis, axis=1)
steps = np.max(np.linalg.norm(np.diff(psis, axis=0), axis=1))
print("norm range:", norms.min(), norms.max(), " max step for dt=0.01:", steps)
ok = np.max(abs(circ-0.5)) < 1e-12 and dev_real > 0.4 and np.allclose(norms, 1, atol=1e-12) and steps < 0.05
print("PASS" if ok else "FAIL")
