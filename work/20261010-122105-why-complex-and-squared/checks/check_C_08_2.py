# Fig c-three-slit-patterns caption: "first zero is at x = ±4 with fainter side bands beyond the window";
# singles coincide; A+B = B+C (stripes one unit apart); A+C half a unit; 4 at centre; ABC 9 at centre;
# "a weak stripe (about 0.95) between neighbouring tall stripes"; zeros at 1/3, 2/3;
# "tall stripes ... at x = ±3 (about 0.8) are lower than the weak stripe at x = ±1/2"
# Fig c-three-slit-leftover caption: p=2 zero; p=1 >=0, zeros only at stripe centres and 1/3, 2/3; p=3,4 change sign; 6, 36
import numpy as np
from scipy.signal import find_peaks
u=np.linspace(-6,6,1200001); env=np.sinc(u/4)
h={k:env*np.exp(2j*np.pi*dj*u) for k,dj in zip("ABC",(-1,0,1))}
P=lambda ks,p=2: np.abs(sum(h[k] for k in ks))**p
i0=np.argmin(abs(u)); res={}
res["singles coincide"]=np.allclose(P("A"),P("B")) and np.allclose(P("B"),P("C"))
res["AB==BC"]=np.allclose(P("AB"),P("BC"))
res["centre 4,4,4,9"]=np.allclose([P("AB")[i0],P("AC")[i0],P("BC")[i0],P("ABC")[i0]],[4,4,4,9])
zAB=np.arange(-2.5,3,1.0); zAC=np.arange(-2.75,3,0.5); e=lambda q: np.sinc(q/4)
res["AB zeros 1 apart, AC zeros 1/2 apart"]=max(abs(e(zAB)*(np.exp(-2j*np.pi*zAB)+1))**2)<1e-25 and max(abs(e(zAC)*2*np.cos(2*np.pi*zAC))**2)<1e-25
single=P("A"); res["envelope first zero at 4"]=abs(np.sinc(1.0))<1e-15 and single[(u>0)&(u<3.999)].min()>0
pk,_=find_peaks(single); sb=[(round(u[i],2),round(single[i],3)) for i in pk if u[i]>4]; print("single-slit side bands beyond 4:",sb)
res["side bands beyond 4"]=len(sb)>0 and all(v<0.1 for _,v in sb)
abc=P("ABC"); w=(u>=-3)&(u<=3)
z=[q for q in (1/3,2/3) if abs(np.sinc(q/4)*(np.exp(-2j*np.pi*q)+1+np.exp(2j*np.pi*q)))**2<1e-25]; res["zeros 1/3,2/3"]=len(z)==2
pk3,_=find_peaks(abc*w); peaks=[(round(u[i],3),round(abc[i],3)) for i in pk3]
weak=[pq for pq in peaks if pq[1]<abs(np.sinc(pq[0]/4))**2*2]; tall=[pq for pq in peaks if pq not in weak]
print("weak stripes in window:",weak); print("tall stripes in window:",tall)
print("ABC at x=±3:",9*np.sinc(3/4)**2)
res["tall at ±3 ≈ 0.8 < weak at ±1/2"]=abs(9*np.sinc(3/4)**2-0.8)<0.05 and 9*np.sinc(3/4)**2<min(v for x_,v in weak if abs(abs(x_)-0.5)<0.1)
inner=[v for x_,v in weak if abs(x_)<1]; res["weak stripe next to centre ≈ 0.95"]=all(abs(v-0.95)<0.03 for v in inner)
res["every weak stripe ≈ 0.95 (caption as written)"]=all(abs(v-0.95)<0.1 for _,v in weak)
I={p:P("ABC",p)-P("AB",p)-P("AC",p)-P("BC",p)+P("A",p)+P("B",p)+P("C",p) for p in (1,2,3,4)}
res["p=2 zero"]=abs(I[2]).max()<1e-12
res["p=1 >= 0"]=I[1].min()>-1e-12
res["p=3,4 change sign; 6, 36 at centre"]=all(I[p][w].min()<0<I[p][w].max() for p in (3,4)) and np.isclose(I[3][i0],6) and np.isclose(I[4][i0],36)
for k,v in res.items(): print(("ok  " if v else "NO  ")+k)
print("PASS" if all(res.values()) else "FAIL")
