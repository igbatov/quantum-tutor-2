# Claim: "seven bright stripes under the central envelope and faint ones beyond it"
# (figure spec: P(u) ~ sinc^2(u) cos^2(4 pi u), slit separation 4x slit width, u in [-1.5,1.5])
import numpy as np
u = np.linspace(-1.5, 1.5, 300001)
S = np.sinc(u)**2            # numpy sinc = sin(pi u)/(pi u)
P = S*np.cos(4*np.pi*u)**2
# local maxima
idx = np.where((P[1:-1] > P[:-2]) & (P[1:-1] > P[2:]) & (P[1:-1] > 1e-6))[0] + 1
peaks = u[idx]
H = P[idx]
print("all peaks:", np.round(peaks,3)); print("heights:", np.round(H,4))
# 'bright' = at least 1% of the central maximum; the split missing-order peaks near |u|=0.93 are ~0.2%
bright = H > 0.01*P.max()
inside = peaks[(np.abs(peaks) < 1) & bright]
print("tiny sub-peaks inside (not bright):", np.round(peaks[(np.abs(peaks)<1) & ~bright],3), np.round(H[(np.abs(peaks)<1) & ~bright],4))
outside = peaks[(np.abs(peaks) > 1) & bright]
print("peaks inside |u|<1:", np.round(inside, 3), "count", len(inside))
print("bright peaks beyond |u|>1:", np.round(outside, 3), "heights", np.round(H[(np.abs(peaks) > 1) & bright], 4))
ok = len(inside) == 7 and len(outside) > 0 and H[np.abs(peaks) > 1].max() < 0.5*H[(np.abs(peaks) < 1) & bright].min()
print("PASS" if ok else "FAIL")
