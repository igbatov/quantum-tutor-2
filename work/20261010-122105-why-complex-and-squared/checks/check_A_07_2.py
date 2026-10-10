# Claims: quaternion amplitudes "pass (a) to (d) just as well"; Peres: two plates in the same arm "could give different counts in the two orders"
import numpy as np
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
def qexp(axis,ang):
    axis=np.array(axis,float); axis/=np.linalg.norm(axis); return np.r_[np.cos(ang),np.sin(ang)*axis]
one=np.array([1.,0,0,0])
# (b),(c),(d) with a unit-quaternion plate q in arm 1: exit amps (q+1)/2,(q-1)/2
ok=True
for ang in np.linspace(0,2*np.pi,13):
    q=qexp([0,1,1],ang)
    P1=np.sum(((q+one)/2)**2); P2=np.sum(((q-one)/2)**2)
    if abs(P1+P2-1)>1e-12 or abs(P1-np.cos(ang/2)**2)>1e-12 or abs(np.sum((q/np.sqrt(2))**2)-0.5)>1e-12: ok=False
print('quaternion plate: smooth sweep cos^2, total 1, arm count 1/2:',ok)
# two plates A,B in arm 1 in both orders; reference arm amplitude c
A=qexp([1,0,0],0.7); B=qexp([0,1,0],1.1)
for name,c in [('real reference arm',one),('generic quaternion reference arm',qexp([0,0,1],0.9))]:
    cbar=c*np.array([1,-1,-1,-1])
    P=lambda q: np.sum(((q+c)/2)**2)
    print(f'{name}: P1(AB) = {P(qmul(A,B)):.4f}, P1(BA) = {P(qmul(B,A)):.4f}')
diff=abs(np.sum(((qmul(A,B)+qexp([0,0,1],0.9))/2)**2)-np.sum(((qmul(B,A)+qexp([0,0,1],0.9))/2)**2))
print('order dependence possible ("could give different counts"):', diff>1e-3)
print('PASS' if ok and diff>1e-3 else 'FAIL')
print('note: with a purely real/complex-commuting reference arm, Re(AB)=Re(BA) and the orders agree')
