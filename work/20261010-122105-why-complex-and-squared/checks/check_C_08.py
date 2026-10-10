# Figure claims (c-three-slit-patterns, c-three-slit-leftover), far-field, d=4w, x in units lambda L/d:
# singles coincide; A+B, B+C identical, stripes 1 apart; A+C stripes 1/2 apart; each 4 at centre;
# ABC 9 at centre, weak stripe ~1 between tall stripes, zeros at 1/3 and 2/3;
# leftover: p=2 zero; p=1 never negative, zero only at isolated points; p=3,4 change sign, 6 and 36 at centre.
import numpy as np
from scipy.signal import find_peaks
u=np.linspace(-3,3,600001)
env=np.sinc(u/4)              # np.sinc(z)=sin(pi z)/(pi z): pi w x/(lambda L)=pi u w/d = pi u/4
h={k:env*np.exp(2j*np.pi*dj*u) for k,dj in zip("ABC",(-1,0,1))}
P=lambda ks,p=2: np.abs(sum(h[k] for k in ks))**p
ok=True
ok&=np.allclose(P("A"),P("B")) and np.allclose(P("B"),P("C")); print("singles coincide:",ok)
ok&=np.allclose(P("AB"),P("BC")); i0=np.argmin(abs(u))
print("centre values AB,AC,BC,ABC:",P("AB")[i0],P("AC")[i0],P("BC")[i0],P("ABC")[i0])
ok&=np.allclose([P("AB")[i0],P("AC")[i0],P("BC")[i0],P("ABC")[i0]],[4,4,4,9])
pk,_=find_peaks(P("AB")); print("AB peak spacing ~", np.round(np.diff(u[pk]),3)[:6])
pk2,_=find_peaks(P("AC")); print("AC peak spacing ~", np.round(np.diff(u[pk2]),3)[:6])
ok&=np.allclose(np.diff(u[pk]),1,atol=0.02) and np.allclose(np.diff(u[pk2]),0.5,atol=0.02)
abc=P("ABC"); seg=(u>0)&(u<1)
zs=u[seg][abc[seg]<1e-6]; print("ABC zeros in (0,1):", np.unique(np.round(zs,4)))
pk3,_=find_peaks(abc); weak=[(round(u[i],3),round(abc[i],3)) for i in pk3 if abc[i]<2]; print("weak stripes:",weak)
ok&=np.allclose(sorted(set(np.round(zs,3))),[1/3,2/3],atol=1e-3)
ok&=all(0.3<v<1.01 for _,v in weak)
I={p:P("ABC",p)-P("AB",p)-P("AC",p)-P("BC",p)+P("A",p)+P("B",p)+P("C",p) for p in (1,2,3,4)}
for p in (1,2,3,4): print("p",p,"max|I3|",abs(I[p]).max(),"min",I[p].min(),"max",I[p].max(),"centre",I[p][i0])
ok&=abs(I[2]).max()<1e-12 and I[1].min()>-1e-12 and I[3].min()<0<I[3].max() and I[4].min()<0<I[4].max()
ok&=np.isclose(I[3][i0],6) and np.isclose(I[4][i0],36)
z1=u[(I[1]<1e-6)]; print("p=1 near-zero locations (rounded):", np.unique(np.round(z1,2)))
print("PASS" if ok else "FAIL")
