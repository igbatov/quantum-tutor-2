# Claim: "chance rule has been checked ... with the polarization of light, another two-answer system" (same globe)
import numpy as np
phi=np.linspace(0,np.pi/2,91)                 # polarizer angle
malus=np.cos(phi)**2; globe=np.cos(2*phi/2)**2 # Poincare-sphere angle = 2*phi
print("max |Malus - globe rule| =",np.max(abs(malus-globe)))
print("90 deg on globe <-> 45 deg polarizer: P =",np.cos(np.pi/4)**2)
print("PASS" if np.allclose(malus,globe) else "FAIL")
