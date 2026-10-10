# Claims: "254 nm, whose hf is 4.9 eV"; proton "at 1 T the two differ by h x 42.6 MHz"; "'along' is the lower";
# ammonia "2A/h ~ 24 GHz"; "1.67e-10 m at 54 eV"; Rabi "in the ideal case, on resonance and without losses, ... 0 to 1".
import numpy as np
from scipy import constants as C
from scipy.linalg import expm
ok = True
E254 = C.h*C.c/253.7e-9/C.e; print("hc/254nm =", E254, "eV"); ok &= abs(E254-4.9)<0.05
mup = C.physical_constants['proton mag. mom.'][0]
dE = 2*mup*1.0/C.h; print("2 mu_p B/h at 1 T =", dE/1e6, "MHz"); ok &= abs(dE/1e6-42.6)<0.05
E_along, E_against = -mup*1.0, +mup*1.0   # E = -mu.B
print("along lower:", E_along < E_against); ok &= E_along < E_against
print("NH3 (3,3) inversion line 23.870 GHz (literature value) ~ 24 GHz"); ok &= abs(23.870-24) < 0.2
p = np.sqrt(2*C.m_e*54*C.e); lam = C.h/p; print("lambda(54 eV) =", lam); ok &= abs(lam/1e-10-1.67)<0.01
# Rabi two-level, on resonance (rotating frame): max upper-state chance 1; detuned < 1
def pmax(Om, De):
    H = 0.5*np.array([[De, Om],[Om, -De]])
    return max(abs((expm(-1j*H*t) @ [1,0])[1])**2 for t in np.linspace(0, 40, 4001))
p0, p1 = pmax(1,0), pmax(1,0.5)
print("max P_up on resonance", p0, "; detuned D=Om/2:", p1); ok &= p0 > 0.9999 and p1 < 0.81
print("PASS" if ok else "FAIL")
