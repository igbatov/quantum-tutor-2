import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Wedge
# ---- Figure 1: 1D step, k2 = k1/2
k1=2*np.pi; k2=k1/2
r=(k1-k2)/(k1+k2); t=2*k1/(k1+k2)
print("r,t",r,t,"r+t",r+t,"|r|+|t|",abs(r)+abs(t),"|r|^2+|t|^2",r**2+t**2,"flux",r**2+(k2/k1)*t**2)
fig,ax=plt.subplots(2,1,figsize=(9,7),gridspec_kw={'height_ratios':[1.3,1]})
x1=np.linspace(-3,0,600); x2=np.linspace(0,3,600)
a=ax[0]
a.axvspan(0,3,color='0.92'); a.text(1.5,2.25,"lower kinetic energy region\n(slower: k₂ = k₁/2)",ha='center',fontsize=9)
a.text(-1.5,2.25,"incoming side (k₁)",ha='center',fontsize=9)
a.plot(x1,np.cos(k1*x1),color='C0',lw=1.2,label='incoming  e^{ik₁x}, amplitude 1')
a.plot(x1,r*np.cos(-k1*x1),color='C3',lw=1.2,label=f'reflected, amplitude r = {r:.3f}')
a.plot(x2,t*np.cos(k2*x2),color='C2',lw=1.6,label=f'transmitted, amplitude t = {t:.3f}')
for y,c,s,d in [(1.6,'C0','→',1),(-1.6,'C3','←',-1)]:
    a.add_patch(FancyArrowPatch((-2.4 if d>0 else -0.6,y),(-0.6 if d>0 else -2.4,y),arrowstyle='-|>',mutation_scale=15,color=c))
a.add_patch(FancyArrowPatch((0.6,1.6),(2.4,1.6),arrowstyle='-|>',mutation_scale=15,color='C2'))
a.axvline(0,color='k',lw=0.8); a.set_ylim(-2,2.7); a.set_yticks([]); a.set_xlabel("x (units of incoming wavelength)")
a.set_title("A wave meets a step: what goes in must come out (one electron at a time)")
a.legend(loc='lower right',fontsize=8)
b=ax[1]
labels=["r + t\n(plain amplitudes)","|r| + |t|\n(sizes)","|r|² + |t|²\n(squares only)","|r|² + (k₂/k₁)|t|²\n(squares × speed = flux)"]
vals=[r+t,abs(r)+abs(t),r**2+t**2,r**2+(k2/k1)*t**2]
cols=['0.6','0.6','0.6','C2']
bars=b.bar(range(4),vals,color=cols)
b.axhline(1,color='k',ls='--',lw=1); b.text(3.45,1.03,"1 = one electron",fontsize=8,ha='right')
for i,v in enumerate(vals): b.text(i,v+0.04,f"{v:.3f}",ha='center',fontsize=9)
b.set_xticks(range(4)); b.set_xticklabels(labels,fontsize=8.5); b.set_ylim(0,2); b.set_ylabel("total 'outgoing' ")
b.set_title("Only the squared amplitudes, weighted by speed, add up to the one incoming electron",fontsize=10)
plt.tight_layout(); plt.savefig("figures/step-flux.png",dpi=130)
# ---- Figure 2: 3D scattering geometry
fig,a=plt.subplots(figsize=(8,5.2))
z=np.linspace(-6,-0.6,400)
for yy in np.linspace(-2.2,2.2,9): a.plot(z,yy+0*z,color='C0',lw=0.6,alpha=0.5)
for zz in np.arange(-6,-0.6,0.8): a.plot([zz,zz],[-2.3,2.3],color='C0',lw=1,alpha=0.6)
a.text(-3.3,2.6,"incoming plane wave  A e^{ikz}\nflux in: j_in = (ħk/m)|A|²  electrons per area per second",ha='center',fontsize=8.5,color='C0')
a.plot(0,0,'ko',ms=9); a.text(0.1,-0.45,"atom",fontsize=9)
for R in [1.2,2.2,3.2,4.2,5.2]:
    th=np.linspace(-1.2,1.2,200); a.plot(R*np.cos(th),R*np.sin(th),color='C3',lw=1,alpha=0.7)
a.text(3.0,-3.3,"outgoing spherical wave  A f(θ) e^{ikr}/r",color='C3',fontsize=8.5,ha='center')
th0,dth=0.55,0.18; R=4.2
a.add_patch(Wedge((0,0),R,np.degrees(th0-dth/2),np.degrees(th0+dth/2),width=R-0.0,color='C2',alpha=0.25))
a.plot([R*np.cos(th0-dth/2),R*np.cos(th0+dth/2)],[R*np.sin(th0-dth/2),R*np.sin(th0+dth/2)],color='C2',lw=3)
a.text(R*np.cos(th0)+0.2,R*np.sin(th0)+0.3,"detector: area r²dΩ\ncounts per second =\n j_in |f(θ)|² dΩ",color='C2',fontsize=8.5)
a.annotate("θ",(1.3*np.cos(th0/2),1.3*np.sin(th0/2)),fontsize=10)
a.set_xlim(-6.2,6.5); a.set_ylim(-3.6,3.4); a.set_aspect('equal'); a.axis('off')
a.set_title("Scattering: outgoing flux through r²dΩ is (ħk/m)|A|²|f|²/r² × r²dΩ — the 1/r² cancels")
plt.tight_layout(); plt.savefig("figures/scattering-flux.png",dpi=130)
