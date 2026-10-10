# Claims (Wootters count): complex qubit 3, real rebit 2; complex pair 15 = 3+3+9; real pair 9 but local 2+2+4 = 8
import numpy as np, itertools
I2=np.eye(2); X=np.array([[0,1],[1,0]]); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1.,-1])
def dim_real_span(mats):
    M=np.array([np.concatenate([m.real.ravel(),m.imag.ravel()]) for m in mats]); return np.linalg.matrix_rank(M)
herm2=[I2,X,Y,Z]; sym2=[I2,X,Z]
print("complex 2x2 Hermitian dim:",dim_real_span(herm2),"-> params",dim_real_span(herm2)-1)
print("real 2x2 symmetric dim:",dim_real_span(sym2),"-> params",dim_real_span(sym2)-1)
# all 4x4 Hermitian / real symmetric
basisH=[np.kron(a,b) for a in herm2 for b in herm2]; print("4x4 Hermitian dim:",dim_real_span(basisH),"-> params",dim_real_span(basisH)-1)
E=[]
for i in range(4):
    for j in range(i,4):
        m=np.zeros((4,4)); m[i,j]=m[j,i]=1; E.append(m)
print("4x4 real symmetric dim:",len(E),"-> params",len(E)-1)
loc_c=dim_real_span([np.kron(a,b) for a in herm2 for b in herm2])-1
loc_r=dim_real_span([np.kron(a,b) for a in sym2 for b in sym2])-1
print("locally accessible params: complex",loc_c,"(3+3+9=15); real",loc_r,"(2+2+4=8)")
yy=np.kron(Y,Y); print("Y(x)Y is real symmetric:",np.allclose(yy.imag,0) and np.allclose(yy,yy.T)," -> the invisible real-pair parameter")
ok=(dim_real_span(herm2)-1==3 and dim_real_span(sym2)-1==2 and len(E)-1==9 and loc_c==15 and loc_r==8)
print("6*sqrt2 =",6*np.sqrt(2)); ok&=abs(round(6*np.sqrt(2),2)-8.49)<1e-9
print("7.66 real-QM bound: literature value (Renou et al. 2021), not recomputed here")
print("PASS" if ok else "FAIL")
