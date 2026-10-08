# Claim: "a confined wave must mix many wavelengths ... no sharp position and sharp momentum"
# Check: Fourier width product for several confined wavefunctions satisfies dx*dk >= 1/2; narrower -> wider in k.
import numpy as np
N = 2**16; L = 400.0
x = np.linspace(-L/2, L/2, N, endpoint=False); dx_ = x[1]-x[0]
k = 2*np.pi*np.fft.fftshift(np.fft.fftfreq(N, d=dx_))
def widths(psi):
    p = np.abs(psi)**2; p /= p.sum()
    sx = np.sqrt((p*x**2).sum() - (p*x).sum()**2)
    phik = np.fft.fftshift(np.fft.fft(psi)); q = np.abs(phik)**2; q /= q.sum()
    sk = np.sqrt((q*k**2).sum() - (q*k).sum()**2)
    return sx, sk
ok = True
for s in [0.5, 1, 2, 4]:
    sx, sk = widths(np.exp(-x**2/(4*s**2))*np.exp(1j*3*x))
    print(f"gaussian s={s}: dx={sx:.4f} dk={sk:.4f} product={sx*sk:.4f}")
    ok &= sx*sk >= 0.5 - 1e-3
for w in [1, 2, 4]:
    psi = np.where(np.abs(x) < w/2, np.cos(np.pi*x/w), 0)
    sx, sk = widths(psi)
    print(f"cosine-in-box w={w}: dx={sx:.4f} dk={sk:.4f} product={sx*sk:.4f}")
    ok &= sx*sk >= 0.5 - 1e-3
print("PASS" if ok else "FAIL")
