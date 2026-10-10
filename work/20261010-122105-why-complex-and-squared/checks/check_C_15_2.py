# Claims: mixture "H with chance q and R with chance 1-q" sits at q(1,0,0)+(1-q)(0,0,1), inside the sphere;
# "a pure state has a lean of length 1"; everything measurable fixed by three leans (density matrix = point in ball);
# Check-yourself: no pure state 50/50 at all three sorters; unpolarized light -> centre.
# Quaternions "would allow up to five mutually even-bet sorters for a two-exit system".
import numpy as np
X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1]); I2=np.eye(2)
r=1/np.sqrt(2); H=np.array([1,0]); R=np.array([r,1j*r])
lean=lambda rho: np.real([np.trace(rho@Z),np.trace(rho@X),np.trace(rho@Y)])   # (P_H-P_V, P_D-P_A, P_R-P_L)
ok=True
for q in np.linspace(0,1,11):
    rho=q*np.outer(H,H.conj())+(1-q)*np.outer(R,R.conj()); L=lean(rho)
    ok&=np.allclose(L,[q,0,1-q]) and np.allclose(rho,(I2+L[0]*Z+L[1]*X+L[2]*Y)/2)
    if 0<q<1: ok&=np.linalg.norm(L)<1
print("mixture lean = q(1,0,0)+(1-q)(0,0,1), inside for 0<q<1, rho rebuilt from 3 leans:",ok)
unpol=I2/2; print("unpolarized lean:",lean(unpol),"chances",[np.real(np.trace(unpol@np.outer(e,e.conj()))) for e in (H,np.array([r,r]),R)])
ok&=np.allclose(lean(unpol),0)
# pure states: |lean| = 1, so (0,0,0) impossible
rng=np.random.default_rng(3); ns=[]
for _ in range(5000):
    s=rng.normal(size=2)+1j*rng.normal(size=2); s/=np.linalg.norm(s); ns.append(np.linalg.norm(lean(np.outer(s,s.conj()))))
print("pure |lean| range:",min(ns),max(ns)); ok&=np.allclose(ns,1)
# quaternionic 2x2 Hermitian: diag real (2) + one quaternion off-diagonal (4) = 6; traceless -> 5 directions.
# Represent quaternions as 2x2 complex blocks -> 4x4 complex Hermitian matrices; find 5 anticommuting traceless ones.
q1=np.eye(2); qi=np.array([[1j,0],[0,-1j]]); qj=np.array([[0,1],[-1,0]]); qk=np.array([[0,1j],[1j,0]])
def qherm(d1,d2,o):  # [[d1, o],[conj(o), d2]] with quaternion o given as 2x2 complex block
    return np.block([[d1*np.eye(2),o],[o.conj().T,d2*np.eye(2)]])
G=[qherm(1,-1,0*q1),qherm(0,0,q1),qherm(0,0,qi),qherm(0,0,qj),qherm(0,0,qk)]
ac=all(np.allclose(G[a]@G[b]+G[b]@G[a],2*np.eye(4)*(a==b)) for a in range(5) for b in range(5))
print("5 mutually anticommuting quaternionic Pauli-type matrices:",ac)
# mutually unbiased: eigenvectors of G_a (projectors (1+G_a)/2, rank 2 = one quaternionic ray) give chance 1/2 under G_b
P=[(np.eye(4)+g)/2 for g in G]; mub=all(np.isclose(np.real(np.trace(P[a]@P[b]))/2,0.5) for a in range(5) for b in range(5) if a!=b)
print("5 sorters mutually even-bet (tr(PaPb)/2 = 1/2):",mub)
# a 6th is impossible: the traceless quaternionic Hermitian space has real dimension 5
basis=[qherm(1,-1,0*q1)]+[qherm(0,0,o) for o in (q1,qi,qj,qk)]
M=np.array([np.concatenate([b.real.ravel(),b.imag.ravel()]) for b in basis]); print("dimension of traceless quaternionic 2x2 Hermitian:",np.linalg.matrix_rank(M))
ok&=ac and mub and np.linalg.matrix_rank(M)==5
print("PASS" if ok else "FAIL")
