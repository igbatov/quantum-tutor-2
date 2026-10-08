# Claim: chance rule "checked at many angles with neutrons" (neutrons are spin-1/2: same globe rule)
import numpy as np
from scipy import constants as c
sz=np.diag([1,-1]).astype(complex); sy=np.array([[0,-1j],[1j,0]])
ok=True
I_n=0.5; print("neutron spin 1/2 -> 2I+1 =",int(2*I_n+1))
th=np.linspace(0,np.pi,181); maxerr=0
for t in th:
    U=np.cos(t/2)*np.eye(2)-1j*np.sin(t/2)*sy      # rotate spin by angle t about y
    psi=U@np.array([1,0]); P=abs(psi[0])**2
    maxerr=max(maxerr,abs(P-np.cos(t/2)**2))
print("max |P_up(after rotation by theta) - cos^2(theta/2)| =",maxerr)
ok &= maxerr<1e-12
print("neutron moment (J/T):",c.physical_constants['neutron mag. mom.'][0], "(nonzero: SG-sortable)")
print("historical fact of the experiments not checked computationally")
print("PASS" if ok else "FAIL")
