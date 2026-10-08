# Claim: "a sound whose air pressure is high whenever the noise's is low ... the two largely cancel and a steady hum,
# like an engine's, becomes much quieter"
# Arithmetic: p + (-p) = 0. Real devices: anti-noise arrives with a small delay tau; residual = |1 - exp(i w tau)|.
import numpy as np
print("p + (-p) =", 1 + (-1))
tau = 50e-6
for f in [100, 300, 1000, 3000]:
    r = abs(1 - np.exp(2j*np.pi*f*tau)); print(f"f={f} Hz: residual amplitude {r:.3f} ({20*np.log10(r):.1f} dB)")
ok = abs(1 - np.exp(2j*np.pi*100*tau)) < 0.1
print("low steady hum largely cancelled (not perfectly):", "PASS" if ok else "FAIL")
