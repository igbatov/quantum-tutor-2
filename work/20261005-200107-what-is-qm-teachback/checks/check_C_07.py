# Claim: "adds their amplitudes before squaring ... amplitudes ... can cancel" -> two-slit stripes;
# stripes vanish when which-slit is recorded.
import numpy as np
x=np.linspace(-1,1,2001); k=40
a1=np.exp(1j*k*x)/np.sqrt(2); a2=np.exp(-1j*k*x)/np.sqrt(2)
coh=abs(a1+a2)**2; incoh=abs(a1)**2+abs(a2)**2
vis=lambda I:(I.max()-I.min())/(I.max()+I.min())
print("coherent visibility",vis(coh)," min",coh.min()," incoherent visibility",vis(incoh))
print("PASS" if vis(coh)>0.999 and vis(incoh)<1e-9 else "FAIL")
