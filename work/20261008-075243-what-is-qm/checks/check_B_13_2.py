# Claim: "other kinds of atom can give a different number of spots, but always a definite number"
from fractions import Fraction as Fr
ground={"Ag 2S1/2":Fr(1,2),"H 2S1/2":Fr(1,2),"Zn 1S0":Fr(0),"O 3P2":Fr(2),"Cr 7S3":Fr(3),"Fe 5D4":Fr(4),"Dy 5I8":Fr(8)}
ok=True
for k,J in ground.items():
    n=2*J+1; print(f"{k}: J={J} -> {n} spots"); ok &= n.denominator==1 and n>=1
ok &= (2*ground["Ag 2S1/2"]+1)==2 and len({2*J+1 for J in ground.values()})>1
print("PASS" if ok else "FAIL")
