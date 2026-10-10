# Round 2 re-run against final-C.md (unchanged claims).
# Claims: Zurek swap: (|aA>+|bB>)/√2 -> swap a<->b -> (|bA>+|aB>)/√2 -> swap A<->B -> original state;
# unequal hands √(2/3), √(1/3): split A into two equal sub-branches -> 3 equal hands -> 2/3, 1/3
import numpy as np
a,b=np.eye(2); A,B=np.eye(2)
psi=(np.kron(a,A)+np.kron(b,B))/np.sqrt(2)
SW=np.array([[0,1],[1,0]])
s1=np.kron(SW,np.eye(2))@psi; s2=np.kron(np.eye(2),SW)@s1
ok=np.allclose(s1,(np.kron(b,A)+np.kron(a,B))/np.sqrt(2)) and np.allclose(s2,psi)
print("swap steps reproduce text, final = original:",ok)
# unequal: photon a with partner A split into A1,A2 (3-dim partner space)
A1,A2,Bp=np.eye(3)
phi=np.sqrt(2/3)*np.kron(a,(A1+A2)/np.sqrt(2))+np.sqrt(1/3)*np.kron(b,Bp)
hands=phi[np.abs(phi)>1e-12]; print("sub-branch hands:",hands)
ok2=np.allclose(hands,1/np.sqrt(3)); print("equal hands -> chances a:",2/3,"b:",1/3)
print("PASS" if ok and ok2 else "FAIL")
