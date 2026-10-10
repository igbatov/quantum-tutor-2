# Two slits: "plain size ... or its cube, you would still get stripes, bright where the two hands agree
#  and dark where they cancel; only the shape of the stripes would differ."
import numpy as np
phi = np.linspace(0, 2*np.pi, 200001)
amp = np.abs(1 + np.exp(1j*phi))
ok = True
for p in [1, 2, 3]:
    I = amp**p / 2**p
    fwhm = np.mean(I >= 0.5)        # fraction of one stripe period above half maximum
    print(f"p={p}: max {I.max():.3f} at phi={phi[np.argmax(I)]:.3f}, value at phi=pi {I[np.argmin(abs(phi-np.pi))]:.1e}, "
          f"fraction of period above half max {fwhm:.3f}")
    ok &= abs(I.max()-1) < 1e-12 and I[np.argmin(abs(phi-np.pi))] < 1e-9
w = [np.mean((amp**p/2**p) >= 0.5) for p in [1, 2, 3]]
ok &= w[0] > w[1] > w[2] and min(abs(w[0]-w[1]), abs(w[1]-w[2])) > 0.05
print("shapes differ (half-max widths", np.round(w, 3), ")")
print("PASS" if ok else "FAIL")
