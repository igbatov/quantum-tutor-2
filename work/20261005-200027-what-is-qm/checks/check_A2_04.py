# Claim: "The stripes disappear, and you get the two one-slit humps simply added:
# the smooth spread you first guessed." (earlier: "a smooth spread of hits with no pattern")
# Full model of the which-path result: P1(X-s)+P1(X+s), s = slit offset (0 in far field), over |X|<=40.
import numpy as np
P1 = lambda X: np.sinc(X/4)**2
X = np.linspace(-40, 40, 400001)
for s in [0.0, 0.5]:
    y = P1(X-s) + P1(X+s)
    imax = np.where((y[1:-1] > y[:-2]) & (y[1:-1] > y[2:]))[0] + 1
    fine = np.abs(np.fft.rfft(y - y.mean()))
    print(f"offset s={s}: local maxima at X =", np.round(X[imax][np.abs(X[imax]) < 14], 2),
          "heights rel. centre:", np.round(y[imax][np.abs(X[imax]) < 14]/y.max(), 4))
    ymin_in = y[(np.abs(X) > 3.5) & (np.abs(X) < 4.5)].min()/y.max()
    print(f"   min near X=+-4 (rel. peak): {ymin_in:.2e}")
# fine stripes gone: no period-1 modulation in the central band
y = 2*P1(X); c = y[np.abs(X) < 3]; print("central band monotone on each side:", np.all(np.diff(c[c.size//2:]) <= 1e-15))
print("'The (fine) stripes disappear': PASS")
print("'smooth spread with no pattern' / 'two humps': FAIL - still the one-slit pattern: a central band plus fainter side bands (~4.7% of peak) and dark gaps at X=+-4, +-8")
