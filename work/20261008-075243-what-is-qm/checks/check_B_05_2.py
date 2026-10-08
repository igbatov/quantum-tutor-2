# Claims: "certain at the pole, 50/50 at 90 deg, zero at the opposite pole, ... the nearer a pole, the likelier";
# "left ... is 90 deg from up and from down"; "no point on the globe is at a Z pole and an X pole at once"
import sympy as sp, numpy as np
th=sp.symbols('theta',real=True)
psi=sp.Matrix([sp.cos(th/2),sp.sin(th/2)])          # Bloch point at polar angle th
Pup=sp.simplify(psi[0]**2); print("P(up)(theta) =",Pup)
ok = Pup.subs(th,0)==1 and Pup.subs(th,sp.pi/2)==sp.Rational(1,2) and Pup.subs(th,sp.pi)==0
t=np.linspace(0,np.pi,1001); f=sp.lambdify(th,Pup)(t); ok &= np.all(np.diff(f)<=0)
print("monotonic decreasing from north to south pole:",np.all(np.diff(f)<=0))
# Bloch vector of X-left state and angle to z
sx=sp.Matrix([[0,1],[1,0]]); sz=sp.Matrix([[1,0],[0,-1]])
l=sp.Matrix([1,-1])/sp.sqrt(2); nz=(l.H*sz*l)[0]; print("<sigma_z> for X eigenstate =",nz,"-> 90 deg from both Z poles"); ok&= nz==0
comm=sx*sz-sz*sx; print("[sx,sz] =",comm.tolist()); ok &= comm!=sp.zeros(2)
# common eigenvector? eigenvectors of sz are |0>,|1>; neither is eigvec of sx
for v in (sp.Matrix([1,0]),sp.Matrix([0,1])):
    w=sx*v; ok &= sp.Matrix.hstack(v,w).rank()==2
print("no common eigenvector of sz and sx")
print("PASS" if ok else "FAIL")
