# Claims: picture (4): "any group picked out by the partner would be a mixture of the two one-slit
# patterns, and a mixture of those has no stripes"; Wiseman-Harrison remark: "on a far screen the
# pattern is that spread [of momenta], and it loses its stripes" when a record is made.
import numpy as np
# Far screen, d = 4a: Fraunhofer one-slit patterns from slits at +-d/2 are identical intensity envelopes.
N = 2**16; x = np.linspace(-200, 200, N, endpoint=False); dx = x[1]-x[0]; a = 1.0; d = 4.0
sl = lambda c: (np.abs(x-c) < a/2).astype(complex)
pk = np.fft.fftshift(np.fft.fftfreq(N, dx))          # spatial frequency (far-screen coordinate)
F = lambda f: np.fft.fftshift(np.fft.fft(f))
IL, IR, Ib = np.abs(F(sl(-d/2)))**2, np.abs(F(sl(d/2)))**2, np.abs(F(sl(-d/2)+sl(d/2)))**2
m = np.abs(pk) < 0.9/a                               # central band (inside first one-slit zero at 1/a)
X = pk*d                                             # units of stripe spacing
def contrast(I):
    r = I[m]/((IL+IR)[m]/2); return (r.max()-r.min())/(r.max()+r.min())
print("max |IL-IR|/max =", np.max(np.abs(IL-IR))/IL.max())
for w in [0, 0.3, 0.5, 0.8, 1]:
    print(f"mixture w={w}: stripe contrast {contrast(w*IL+(1-w)*IR):.2e}")
print(f"no record: momentum distribution contrast {contrast(Ib):.3f}; with orthogonal record: {contrast(IL+IR):.2e}")
ok = all(contrast(w*IL+(1-w)*IR) < 1e-9 for w in [0, 0.3, 0.5, 0.8, 1]) and contrast(Ib) > 0.99
print("PASS" if ok else "FAIL")
