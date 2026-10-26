import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.constants import m_n, hbar
D="/home/user/quantum-tutor-2/work/20261026-145241-schrodinger-from-axioms/figures/"
plt.rcParams.update({"font.size":11})
g=9.8; dz0=0.02; T=10e-6
phi=np.linspace(-30,30,2001); dphi=m_n*g*dz0*np.sin(np.radians(phi))*T/hbar
I=0.5*(1+np.cos(dphi)); edge=dphi[-1]; nfr=(dphi[-1]-dphi[0])/(2*np.pi)
fig,(a,b)=plt.subplots(1,2,figsize=(11,4.2),gridspec_kw={"width_ratios":[1,1.5]})
A,B,C,Dp=(0,0),(1,0),(0,1),(1,1)
a.plot([A[0],B[0]],[A[1],B[1]],"k-",lw=2); a.plot([B[0],Dp[0]],[B[1],Dp[1]],"k-",lw=2)
a.plot([A[0],C[0]],[A[1],C[1]],"k-",lw=2); a.plot([C[0],Dp[0]],[C[1],Dp[1]],"k-",lw=2)
a.annotate("",xy=(0,0),xytext=(-0.5,0),arrowprops=dict(arrowstyle="->",lw=2))
a.annotate("",xy=(1.5,1.0),xytext=(1,1),arrowprops=dict(arrowstyle="->",lw=2))
for p,l,o in [(A,"A (split)",(-0.1,-0.15)),(Dp,"D (recombine)",(-0.2,0.08)),(B,"lower path",(-0.3,-0.15)),(C,"upper path",(-0.1,0.08))]:
    a.text(p[0]+o[0],p[1]+o[1],l)
a.annotate("",xy=(1.15,1),xytext=(1.15,0),arrowprops=dict(arrowstyle="<->"))
a.text(1.2,0.45,r"$\Delta z$"); a.annotate("",xy=(-0.35,0.3),xytext=(-0.35,0.9),arrowprops=dict(arrowstyle="->",lw=2.5,color="gray"))
a.text(-0.55,0.55,r"$g$",fontsize=13); a.text(1.55,0.95,"detector")
a.set_xlim(-0.7,2.1); a.set_ylim(-0.4,1.3); a.axis("off"); a.set_title("COW geometry (sketch)")
b.plot(phi,I,"k-",lw=1.5)
b.set_xlabel(r"crystal tilt $\varphi$ (degrees)"); b.set_ylabel("detector counts (normalised)")
b.axhline(0.5,ls=":",color="gray")
b.text(-29,1.04,r"massless classical wave: flat (no $m$ in phase)",fontsize=9,color="gray")
b.text(-29,-0.17,r"$\Delta\phi=mg\Delta z_0\sin\varphi\,T/\hbar$ = %.1f rad at $\pm30^\circ$;  %.1f fringes"%(edge,nfr),fontsize=10)
b.set_ylim(-0.25,1.12); b.set_title(r"Neutron fringes, $\Delta z_0$=2 cm, $T$=10 µs")
fig.tight_layout(); fig.savefig(D+"a-cow-fringes.png",dpi=150); print("edge %.2f rad, fringes %.2f"%(edge,nfr))
