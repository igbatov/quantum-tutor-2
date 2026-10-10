# Check-yourself: p=3/4, N=300: sqrt(p(1-p)/N) = 0.025; halving needs 4N = 1200 (answer well posed)
import numpy as np
s=np.sqrt(0.75*0.25/300); s2=np.sqrt(0.75*0.25/1200); print(s,s2)
print("PASS" if abs(s-0.025)<1e-12 and abs(s2-s/2)<1e-12 and abs(np.sin(np.radians(60))**2-0.75)<1e-12 else "FAIL")
