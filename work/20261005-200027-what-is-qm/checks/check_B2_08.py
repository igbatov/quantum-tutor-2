# Claim: arrows "of a richer kind than the ones drawn here (light whose wiggle goes round in circles already needs this)"
import numpy as np
def u(a): a = np.radians(a); return np.array([np.sin(a), np.cos(a)])
angs = np.linspace(0, 180, 361)
R = np.array([1, 1j])/np.sqrt(2)
pc = np.array([abs(np.vdot(u(a), R))**2 for a in angs]); print("circular: P(pass) range", pc.min(), pc.max())
best = min(max(abs((u(a)@u(b))**2-0.5) for a in angs) for b in np.linspace(0, 180, 721))
print("best real (linear) arrow: max deviation from 0.5 over filter angles =", best)
print("PASS" if np.allclose(pc, 0.5) and best > 0.49 else "FAIL")
