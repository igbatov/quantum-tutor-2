# Claim: "narrow stripes are replaced by one wide bright band, with much fainter bands further out"
# Caption: "wide central band is flanked by dark gaps and much fainter side bands, the brightest about 5%"
# Full one-slit model P1 = sinc^2(X/4) (slit width a, spacing d = 4a) over |X|<=60, plus near-field offset.
import numpy as np
P1 = lambda X: np.sinc(X/4)**2
X = np.linspace(-60, 60, 1200001)
ok = True
for s in [0.0, 0.5]:   # s: one-slit pattern centred behind its own slit (offset, near-field check)
    y = P1(X - s)
    im = np.where((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:]))[0] + 1
    h = y[im]/y.max(); pos = X[im]-s
    side = h[np.abs(pos) > 1]
    central_fine = y[np.abs(X - s) < 3.9]
    c = central_fine[central_fine.size//2:]
    mono = np.all(np.diff(c) <= 1e-15)        # no narrow stripes in the central band
    print(f"offset {s}: brightest side band {side.max():.4f} of centre at X={pos[np.abs(pos)>1][np.argmax(side)]:.2f}; "
          f"next {np.sort(side)[-3]:.4f}; dark-gap minima near X=+-4: {y[np.abs(np.abs(X-s)-4)<0.05].min():.1e}; "
          f"central band free of narrow stripes: {mono}")
    ok &= mono and 0.04 < side.max() < 0.06
# fraction of all hits in the central band
from scipy.integrate import quad
frac = quad(P1, -4, 4, limit=200)[0]/4.0   # integral of sinc^2(X/4) over all X = 4
print(f"fraction of hits in central band: {frac:.3f}")
print("one wide band + much fainter side bands (~5%), dark gaps:", "PASS" if ok else "FAIL")
