import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D="/home/user/quantum-tutor-2/work/20261026-145241-schrodinger-from-axioms/figures/"
plt.rcParams.update({"font.size":11})
k,v,m,hb=5.0,2.0,1.0,1.0; kp=k-m*v/hb
x=np.linspace(0,10,2000)
psi=np.exp(1j*k*x)                         # lab, t=0
psip=np.exp(-1j*m*v*x/hb)*psi              # moving frame, t'=0: theta*relabel
assert np.allclose(psip,np.exp(1j*kp*x))
fig,ax=plt.subplots(figsize=(7,4))
ax.plot(x,psi.real,"k-",lw=1.3,label=r"lab: Re$\,\psi$, $k=5$ ($\lambda=2\pi/5$)")
ax.plot(x,psip.real,"--",color="tab:red",lw=1.6,label=r"frame $v=2$: Re$\,\psi'$, $k'=3$ ($\lambda=2\pi/3$)")
ax.plot(x,abs(psi)**2,"-",color="tab:blue",lw=4,alpha=0.5,label=r"$|\psi|^2$ (lab)")
ax.plot(x,abs(psip)**2,":",color="k",lw=2,label=r"$|\psi'|^2$ (moving)")
ax.set_xlabel(r"$x$ (units $\hbar=m=1$)"); ax.set_ylabel("amplitude"); ax.set_ylim(-1.3,1.9)
ax.legend(loc="upper center",ncol=2,fontsize=8.5,frameon=False)
ax.set_title(r"Same particle, two frames: $\psi'=e^{-imvx/\hbar}\psi$ at $t=0$")
fig.tight_layout(); fig.savefig(D+"a-boost-phase.png",dpi=150); print("ok")
