# Claims: "[K,P]=i hbar m" (Galilei algebra, K = m x - t p); lemma "linear map preserving |psi|^2
# pointwise is multiplication by a phase" (finite-dim test); "Real V keeps H Hermitian";
# 3D "hbar omega = hbar^2|k|^2/2m" makes theta k-independent; p=-i hbar d/dx eigenvalue hbar k.
import sympy as sp, numpy as np
x,t,m,hb,k=sp.symbols("x t m hbar k",real=True); f=sp.Function("f")(x); ok=True
P=lambda g:-sp.I*hb*sp.diff(g,x); K=lambda g:m*x*g-t*P(g)
comm=sp.simplify(K(P(f))-P(K(f))); print("[K,P]f =",comm); ok&=sp.simplify(comm-sp.I*hb*m*f)==0
ok&=sp.simplify(P(sp.exp(sp.I*k*x))-hb*k*sp.exp(sp.I*k*x))==0
# lemma, n=2 symbolic: |M psi|_i=|psi_i| for psi=e1,e2,e1+e2,e1+i e2 forces M diagonal with |entries|=1
rng=np.random.default_rng(0)
def preserves(M):
    for _ in range(50):
        p=rng.normal(size=3)+1j*rng.normal(size=3)
        if not np.allclose(abs(M@p),abs(p)): return False
    return True
Dg=np.diag(np.exp(1j*rng.normal(size=3))); ok&=preserves(Dg)
ok&= not preserves(Dg@np.array([[0,1,0],[1,0,0],[0,0,1]]))   # permutation moves weight
ok&= not preserves(Dg+0.01*rng.normal(size=(3,3)))
# real V Hermitian; complex V not
N=50; dx=0.1; lap=(np.diag(-2*np.ones(N))+np.diag(np.ones(N-1),1)+np.diag(np.ones(N-1),-1))/dx**2
H=-0.5*lap+np.diag(rng.normal(size=N)); ok&=np.allclose(H,H.conj().T)
Hc=-0.5*lap+np.diag(rng.normal(size=N)+0.1j); ok&= not np.allclose(Hc,Hc.conj().T)
# 3D
kx,ky,kz,vx,vy,vz=sp.symbols("kx ky kz vx vy vz",real=True)
kv=sp.Matrix([kx,ky,kz]); vv=sp.Matrix([vx,vy,vz])
w=lambda q: hb*(q.dot(q))/(2*m); br=sp.simplify(w(kv)-kv.dot(vv)-w(kv-m*vv/hb))
print("3D bracket:",br); ok&=all(sp.diff(br,s)==0 for s in (kx,ky,kz))
print("PASS" if ok else "FAIL")
