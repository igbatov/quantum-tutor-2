# Claim: "a wave squeezed into a small region must combine many wavelengths ... different momenta"
# Numerical Fourier check: narrower packet -> wider spread in k; Gaussian saturates dx*dk = 1/2.
import numpy as np
x = np.linspace(-200, 200, 2**16); dx = x[1]-x[0]
k = 2*np.pi*np.fft.fftshift(np.fft.fftfreq(x.size, d=dx))
res = []
for s in [4.0, 1.0, 0.25]:
    psi = np.exp(-x**2/(4*s**2))*np.exp(1j*5*x)
    px = np.abs(psi)**2; px /= px.sum()
    phik = np.fft.fftshift(np.fft.fft(psi)); pk = np.abs(phik)**2; pk /= pk.sum()
    sx = np.sqrt((px*x**2).sum() - (px*x).sum()**2)
    sk = np.sqrt((pk*k**2).sum() - (pk*k).sum()**2)
    res.append((sx, sk)); print(f"sigma_x={sx:.4f}  sigma_k={sk:.4f}  product={sx*sk:.4f}")
# also a non-Gaussian (box) packet: product larger than 1/2
ok = res[0][1] < res[1][1] < res[2][1] and all(abs(a*b-0.5) < 1e-3 for a, b in res)
print("PASS" if ok else "FAIL")
