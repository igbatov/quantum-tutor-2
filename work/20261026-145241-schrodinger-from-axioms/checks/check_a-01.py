# Claims: "dU/dt = A U(t) with A = U'(0)"; "A^dag + A = 0"; "H = i hbar A Hermitian";
# converse "d/dt(U^dag U) = U^dag(A^dag+A)U = 0"; "U(t)=e^{-iHt/hbar}" unique; stationary states.
import numpy as np
from scipy.linalg import expm
rng=np.random.default_rng(1); hb=1.0546; n=4; tol=1e-6; ok=True
X=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); H=(X+X.conj().T)/2
U=lambda t: expm(-1j*H*t/hb)
s,t=0.37,1.21
ok&=np.allclose(U(s)@U(t),U(s+t)); ok&=np.allclose(U(0),np.eye(n))
ok&=np.allclose(U(t).conj().T@U(t),np.eye(n))
eps=1e-6; A=(U(eps)-U(-eps))/(2*eps)
dU=(U(t+eps)-U(t-eps))/(2*eps); ok&=np.allclose(dU,A@U(t),atol=tol)
ok&=np.allclose(A+A.conj().T,0,atol=tol)
Hrec=1j*hb*A; ok&=np.allclose(Hrec,H,atol=1e-5); ok&=np.allclose(Hrec,Hrec.conj().T,atol=1e-5)
# converse: Hermitian H -> U^dag U const; non-Hermitian generator breaks unitarity
B=-1j*H/hb; W=lambda t: expm(B*t)
d=(W(t+eps).conj().T@W(t+eps)-W(t-eps).conj().T@W(t-eps))/(2*eps)
ok&=np.allclose(d,W(t).conj().T@(B.conj().T+B)@W(t),atol=tol) and np.allclose(d,0,atol=tol)
C=B+0.1*np.eye(n); ok&= not np.allclose(expm(C).conj().T@expm(C),np.eye(n))
# uniqueness: integrate dV/dt=-(i/hb)HV from V(0)=1 by RK4, compare with expm
V=np.eye(n,dtype=complex); N=4000; h=t/N; f=lambda V:-1j/hb*H@V
for _ in range(N):
    k1=f(V);k2=f(V+h/2*k1);k3=f(V+h/2*k2);k4=f(V+h*k3);V=V+h/6*(k1+2*k2+2*k3+k4)
ok&=np.allclose(V,U(t),atol=1e-8)
# d/dt(e^{iHt}V)=0 -> e^{iHt}V(t)=1
ok&=np.allclose(expm(1j*H*t/hb)@V,np.eye(n),atol=1e-8)
# stationary states
w,vecs=np.linalg.eigh(H); e=vecs[:,0]; ok&=np.allclose(U(t)@e,np.exp(-1j*w[0]*t/hb)*e)
print("PASS" if ok else "FAIL", "max|A+A^dag|=%.1e"%abs(A+A.conj().T).max(), "|V-expm|=%.1e"%abs(V-U(t)).max())
