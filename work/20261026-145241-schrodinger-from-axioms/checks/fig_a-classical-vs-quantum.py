# Toy model of Davisson-Germer: wave = Ni(111) surface grating (d=2.15 A) with depth attenuation;
# classical particles = diffuse, voltage-independent spread. Peak angle from d sin(phi)=lambda.
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.constants import h,m_e,e
D="/home/user/quantum-tutor-2/work/20261026-145241-schrodinger-from-axioms/figures/"
plt.rcParams.update({"font.size":11})
d=2.15e-10; phi=np.radians(np.linspace(10,90,1500)); n=np.arange(40); w=np.exp(-n/6)
fig,ax=plt.subplots(figsize=(7.5,4.2))
cls=np.sin(phi)*np.cos(phi/2)**0.5; cls/=cls.max()
ax.plot(np.degrees(phi),cls,"k:",lw=2.2,label="classical particles (any $V_0$)")
for V,ls in [(40,"-"),(54,"--"),(70,"-.")]:
    lam=h/np.sqrt(2*m_e*e*V); kk=2*np.pi/lam
    I=abs((w[None,:]*np.exp(1j*kk*d*n[None,:]*np.sin(phi)[:,None])).sum(1))**2
    I=0.15+0.85*I/I.max(); pk=np.degrees(np.arcsin(lam/d))
    ax.plot(np.degrees(phi),I,ls,lw=1.6,label=r"wave, $V_0$=%d V: peak at %.0f$^\circ$"%(V,pk))
    print(V,"V peak %.1f deg"%pk)
ax.set_xlabel("scattering angle (degrees)"); ax.set_ylabel("count rate (normalised)")
ax.set_title(r"Davisson–Germer toy model: the peak moves with $\lambda=h/p\propto1/\sqrt{V_0}$")
ax.legend(fontsize=9,loc="upper left"); ax.set_ylim(0,1.25)
fig.tight_layout(); fig.savefig(D+"a-classical-vs-quantum.png",dpi=150)
