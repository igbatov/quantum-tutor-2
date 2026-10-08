# Claim: two-slit "dots pile up into stripes, dark where the waves ... cancel. If anything records which slit ... stripes vanish."
import numpy as np
x = np.linspace(-1, 1, 2001)
d, lam, Lscr = 1.0, 0.05, 10.0
phi1 = np.exp(1j*np.pi*d*x/(lam*Lscr)); phi2 = np.exp(-1j*np.pi*d*x/(lam*Lscr))
I_coh = abs(phi1+phi2)**2/4      # no which-path record: amplitudes add
I_inc = (abs(phi1)**2+abs(phi2)**2)/4  # which-path record: probabilities add
vis = lambda I: (I.max()-I.min())/(I.max()+I.min())
print(f"visibility coherent = {vis(I_coh):.3f}, with which-path record = {vis(I_inc):.3f}")
print(f"normalization check: mean coherent {I_coh.mean():.3f} vs incoherent {I_inc.mean():.3f}")
print("PASS" if vis(I_coh) > 0.99 and vis(I_inc) < 1e-9 else "FAIL")
