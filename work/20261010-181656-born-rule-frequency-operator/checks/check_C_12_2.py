# Caption c-born-spread: "within-0.05 curve is 1 minus the eps = 0.05 deviant squared length of the previous figure";
# "within 0.01 of 0.8, no m/N does for N = 11 to 14, so that chance is 0 there"
import numpy as np
from scipy.stats import binom
from fractions import Fraction as Fr
def within(N,eps):
    return sum(binom.pmf(m,N,0.8) for m in range(N+1) if abs(Fr(m,N)-Fr(4,5))<=eps)
def dev(N,eps):
    return sum(binom.pmf(m,N,0.8) for m in range(N+1) if abs(Fr(m,N)-Fr(4,5))>eps)
ok=all(abs(within(N,Fr(1,20))+dev(N,Fr(1,20))-1)<1e-12 for N in [10,37,100,1000,5000])
z=[N for N in range(10,20) if within(N,Fr(1,100))==0]; print("N in 10..19 with zero chance within 0.01:",z)
ok&= all(N in z for N in [11,12,13,14]) and 15 not in z  # claim: zero for N=11..14 (also zero for 16..19, not claimed)
print("PASS" if ok else "FAIL")
