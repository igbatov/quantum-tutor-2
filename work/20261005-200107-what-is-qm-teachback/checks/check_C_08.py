# Claim: everyday objects' "waves have unimaginably short wavelengths" (de Broglie)
from scipy.constants import h, m_e
cases={"baseball 0.145 kg at 40 m/s":(0.145,40),"dust grain 1e-15 kg at 1 mm/s":(1e-15,1e-3),"electron at 1e6 m/s":(m_e,1e6)}
for k,(m,v) in cases.items(): print(f"{k}: lambda = {h/(m*v):.3e} m")
lb=h/(0.145*40)
print("baseball wavelength vs proton size 1e-15 m: ratio", lb/1e-15)
print("PASS" if lb<1e-30 else "FAIL")
