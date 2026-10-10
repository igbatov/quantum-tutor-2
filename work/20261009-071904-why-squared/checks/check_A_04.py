# Claim: hidden-pointer model "shrinks in a straight line: 67% at 30°, 50% at 45°, 33% at 60°"
# and it "agrees with the circles at 0°, 45° and 90° but misses at 30° and 60°"
import numpy as np
rng = np.random.default_rng(1)
lam = rng.uniform(-90, 90, 4_000_000)          # pointer angles (polarization is mod 180)
def d(a, b):                                    # angular distance mod 180
    x = np.abs((a - b + 90) % 180 - 90); return x
passed0 = lam[d(lam, 0) < 45]                   # survivors of 0-deg polarizer (angle left alone)
ok = True
for th, claim in [(0, 100), (30, 67), (45, 50), (60, 33), (90, 0)]:
    frac = 100*np.mean(d(passed0, th) < 45)
    exact = 100*(90 - th)/90
    qm = 100*np.cos(np.radians(th))**2
    good = abs(round(exact) - claim) == 0 and abs(frac - exact) < 0.2
    ok &= good
    print(f"theta={th:2d}: MC={frac:6.2f}%, linear={exact:6.2f}%, claimed={claim}%, QM cos^2={qm:6.2f}%  {'ok' if good else 'MISMATCH'}")
agree = [abs(100*(90-t)/90 - 100*np.cos(np.radians(t))**2) < 0.5 for t in (0, 45, 90)]
miss = [abs(100*(90-t)/90 - 100*np.cos(np.radians(t))**2) > 5 for t in (30, 60)]
ok &= all(agree) and all(miss)
print("agrees at 0/45/90:", agree, " misses at 30/60:", miss)
print("PASS" if ok else "FAIL")
