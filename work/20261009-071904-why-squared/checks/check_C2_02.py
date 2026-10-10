# Claims (final-C, arithmetic paragraph and figure caption row 4):
#  "where the three hands point 120 deg apart ... every power ... gives 3 - 3 = 0"
#  "each pair's total is exactly as long as a single hand"
#  "Everywhere else on this screen the plain size fails"
#  caption: plain size "never negative", zero "only at isolated points every third of a unit"
import numpy as np
w = np.exp(2j*np.pi/3); h = np.array([1, w, w**2])
pairs = [abs(h[0]+h[1]), abs(h[1]+h[2]), abs(h[0]+h[2])]
print("120 deg hands: |A+B+C| =", abs(h.sum()), " pair lengths:", np.round(pairs, 12))
ok120 = abs(h.sum()) < 1e-12 and np.allclose(pairs, 1)
for p in [0.5, 1, 2, 3, 7]:
    L = abs(h.sum())**p - sum(x**p for x in pairs) + 3
    print(f"  p={p}: three-slit {abs(h.sum())**p:.1e}, pairs-singles = {sum(x**p for x in pairs):.6f} - 3, leftover {L:.1e}")
    ok120 &= abs(L) < 1e-6   # p=0.5 turns the 3e-16 rounding residue of |A+B+C| into 2e-8
# periodic part of the plain-size leftover vs phase step phi between neighbouring slits
phi = np.linspace(0, 2*np.pi, 600001)
W = np.exp(1j*phi)
L1 = np.abs(1+W+W**2) - 2*np.abs(1+W) - np.abs(1+W**2) + 3
print("plain-size leftover (unit hands): min", L1.min(), " max", L1.max())
# zeros: local minima below tolerance
idx = np.where(L1 < 1e-4)[0]
groups = np.split(idx, np.where(np.diff(idx) > 1)[0]+1)
zeros = [phi[g[np.argmin(L1[g])]]/(2*np.pi) for g in groups]
print("zeros at phi/2pi =", np.round(zeros, 4))
okzeros = np.allclose(sorted(set(np.round(np.mod(zeros, 1), 3))), [0, 1/3, 2/3], atol=2e-3)
# minimum away from the zeros (outside +-0.01 of each)
mask = np.ones_like(phi, bool)
for z in [0, 1/3, 2/3, 1]:
    mask &= np.abs(phi/(2*np.pi) - z) > 0.01
print("min of plain-size leftover more than 0.01 unit from those zeros:", L1[mask].min())
# whole far screen with the single-slit envelope (d = 4a): envelope zeros at u = 4k, on the 1/3 grid
u = np.linspace(-40, 40, 2400001)
env = np.abs(np.sinc(u/4))
Lfull = env*np.interp(np.mod(u, 1)*2*np.pi, phi, L1)
grid = np.round(u*3)/3
off = np.abs(u-grid) > 0.003
print("full screen |u|<=40: min leftover", Lfull.min(), "; points off the 1/3 grid with leftover < 1e-9:", int(np.sum(off & (Lfull < 1e-9))))
ok = ok120 and L1.min() > -1e-12 and okzeros and L1[mask].min() > 1e-3 and Lfull.min() > -1e-12 and np.sum(off & (Lfull < 1e-9)) == 0
print("PASS" if ok else "FAIL")
