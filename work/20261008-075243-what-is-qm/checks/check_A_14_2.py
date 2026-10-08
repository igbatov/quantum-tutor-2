# Claim: "a screen far enough away that the pattern no longer changes shape with distance"
# Fresnel integral for two slits (width a, separation d=4a); pattern vs scaled X=x d/(lambda L)
import numpy as np
lam = 1.0; a = 10.0; d = 40.0
xs = np.concatenate([np.linspace(-d/2-a/2, -d/2+a/2, 400), np.linspace(d/2-a/2, d/2+a/2, 400)])
Xs = np.linspace(-6, 6, 601)
def pattern(L):
    x = Xs*lam*L/d
    amp = np.exp(1j*np.pi*(x[:,None]-xs[None,:])**2/(lam*L)).sum(1)
    P = np.abs(amp)**2; return P/P.max()
far = np.sinc(Xs/4)**2*np.cos(np.pi*Xs)**2; far /= far.max()
prev = None
for L in (1e3, 1e4, 1e5, 1e6, 1e7):
    P = pattern(L); dev = np.abs(P-far).max()
    print(f"L/(d^2/lambda)={L*lam/d**2:9.2g}: max diff from far-field shape = {dev:.3f}")
    prev = dev
print("PASS" if prev < 0.01 else "FAIL")
