# Claim (G4): "e^{-iHt/h} e^{ivK/h} = e^{i chi} e^{-ivtP/h} e^{ivK/h} e^{-iHt/h}" for H=P^2/2M, K=MX
# (hbar = M = 1), and G2 "W = e^{i phi} W'" with phi = Mav/hbar. Checked on a grid by FFT.
import numpy as np
N, L = 8192, 400.0; x = np.linspace(-L/2, L/2, N, endpoint=False); k = 2*np.pi*np.fft.fftfreq(N, L/N)
dx = L/N; ip = lambda f, g: np.sum(np.conj(f)*g)*dx
Ht = lambda p, t: np.fft.ifft(np.exp(-1j*k**2*t/2)*np.fft.fft(p))     # e^{-iHt}
Tr = lambda p, a: np.fft.ifft(np.exp(-1j*k*a)*np.fft.fft(p))          # e^{-iaP}
Bo = lambda p, v: np.exp(1j*v*x)*p                                       # e^{ivK}, K = M X
psi = np.exp(-(x-3)**2/6 + 0.7j*x); psi /= np.sqrt(ip(psi, psi).real)
ok = True
v, t, a = 0.9, 4.0, 2.5
L4 = Ht(Bo(psi, v), t); R4 = Tr(Bo(Ht(psi, t), v), v*t)
ov = ip(R4, L4); ok &= abs(abs(ov) - 1) < 1e-9
print(f"G4: |<R|L>| = {abs(ov):.12f}, chi = {np.angle(ov):.6f} (-M v^2 t/2 hbar = {-v*v*t/2:.6f} mod 2pi)")
W = Bo(Tr(psi, a), v); Wp = Tr(Bo(psi, v), a)
ov2 = ip(Wp, W); ok &= abs(abs(ov2) - 1) < 1e-9 and abs(np.angle(ov2) - a*v) < 1e-9
print(f"G2: |<W'|W>| = {abs(ov2):.12f}, phase = {np.angle(ov2):.6f}, M a v/hbar = {a*v:.6f}")
print("PASS" if ok else "FAIL")
