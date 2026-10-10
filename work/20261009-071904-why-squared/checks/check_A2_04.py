# Claim (hidden pointer): "overlap ... shrinks in a straight line: 67% at 30°, 50% at 45°, 33% at 60°."
import numpy as np
rng = np.random.default_rng(1)
phi = rng.uniform(0, np.pi, 4_000_000)                 # pointer angles (mod 180°), all equally likely
def nearer(phi, ax):                                   # is pointer within 45° of axis ax (mod 180°)?
    d = np.abs((phi - ax + np.pi/2) % np.pi - np.pi/2); return d < np.pi/4
passed0 = phi[nearer(phi, 0.0)]
ok = True
for d, e in [(0, 100), (30, 67), (45, 50), (60, 33), (90, 0)]:
    f = 100*np.mean(nearer(passed0, np.radians(d))); line = 100*(90 - d)/90
    good = round(f) == e and abs(f - line) < 0.2; ok &= good
    print(f"{d}°: MC {f:.2f}%, line {line:.2f}%, cos² {100*np.cos(np.radians(d))**2:.1f}% {'ok' if good else 'X'}")
print("PASS" if ok else "FAIL")
