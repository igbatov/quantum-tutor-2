# Claims: with a which-slit record "the pattern is, ideally, the two one-slit patterns added";
# "A trace that only partly tells the slits apart only partly fades the stripes";
# "parts tied to different recorder states can't cancel; their chances just add".
import numpy as np
X = np.linspace(-8, 8, 8001)
P1 = np.sinc(X/4)**2
psiL = np.sinc(X/4)*np.exp(-1j*np.pi*X); psiR = np.sinc(X/4)*np.exp(1j*np.pi*X)
def pattern(gamma):
    # state (psiL|rL> + psiR|rR>), <rL|rR> = gamma; trace out recorder
    return np.abs(psiL)**2 + np.abs(psiR)**2 + 2*np.real(np.conj(psiL)*psiR*gamma)
def visibility(P):
    # local fringe visibility at the centre: compare peak at X=0 with the adjacent minimum at X=0.5,
    # correcting for the slowly varying one-slit envelope
    i0 = np.argmin(abs(X)); i5 = np.argmin(abs(X-0.5))
    Pmax = P[i0]/P1[i0]; Pmin = P[i5]/P1[i5]
    return (Pmax-Pmin)/(Pmax+Pmin)
ok = True
for g in [1.0, 0.5, 0.2, 0.0]:
    V = visibility(pattern(g)); print(f"overlap {g}: central fringe visibility {V:.3f}")
    ok &= abs(V - g) < 2e-2
full = pattern(0.0)
ok &= np.max(abs(full - 2*P1)) < 1e-12
print("orthogonal records -> P = P_L + P_R exactly:", np.max(abs(full - 2*P1)) < 1e-12)
print("PASS" if ok else "FAIL")
