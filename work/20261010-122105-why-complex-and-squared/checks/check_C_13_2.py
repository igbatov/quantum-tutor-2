# Round 2 re-run against final-C.md (unchanged claims).
# Claims: "a quarter-period delay ... is exactly the quarter turn" (V component multiplied by i);
# Beth: angular momentum per photon of energy hf is hbar (L = E/omega).
import numpy as np, scipy.constants as k
w=2*np.pi*5e14; T=2*np.pi/w; t=np.linspace(0,3*T,1000)
delayed=np.exp(-1j*w*(t-T/4)); ok=np.allclose(delayed,1j*np.exp(-1j*w*t))
print("e^{-i w (t-T/4)} = i e^{-i w t} (convention e^{-iwt}):",ok)
print("with e^{+iwt} convention the delay is a factor -i (handedness label swaps; text says convention-dependent)")
f=5e14; E=k.h*f; Lph=E/(2*np.pi*f); print("E/omega =",Lph," hbar =",k.hbar); ok2=np.isclose(Lph,k.hbar)
print("PASS" if ok and ok2 else "FAIL")
