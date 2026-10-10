# Claim: "cos 1 deg = 0.99985 ... 0.99985^(10^5) = e^-15.2 ~ 2.4e-7"; product-state overlap -> 0 unless |overlap|=1
import numpy as np
ok=True
c=np.cos(np.radians(1)); L=1e5*np.log(c); print(c,L,np.exp(L)); ok&= abs(c-0.99985)<1e-5 and abs(L+15.2)<0.05 and abs(np.exp(L)-2.4e-7)<0.1e-7
# also with rounded 0.99985
print(0.99985**1e5)
print("PASS" if ok else "FAIL")
