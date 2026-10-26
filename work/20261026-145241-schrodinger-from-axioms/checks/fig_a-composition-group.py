# U(t)=e^{-iEt/hbar} acting on an energy eigenstate: rotation in the complex plane; U(s)U(t)=U(s+t)
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D="/home/user/quantum-tutor-2/work/20261026-145241-schrodinger-from-axioms/figures/"
plt.rcParams.update({"font.size":11})
E,hb,s,t=1.0,1.0,0.7,1.1; U=lambda tt: np.exp(-1j*E*tt/hb)
assert np.isclose(U(s)*U(t),U(s+t)) and np.isclose(abs(U(s+t)),1)
fig,(a,b)=plt.subplots(1,2,figsize=(10,4.3),gridspec_kw={"width_ratios":[1,1.4]})
th=np.linspace(0,2*np.pi,400); a.plot(np.cos(th),np.sin(th),color="gray",lw=1)
for z,lab,st,c in [(1,r"$U(0)=1$","-","k"),(U(t),r"$U(t)$","-","tab:blue"),(U(s+t),r"$U(s)U(t)=U(s+t)$","--","tab:red")]:
    a.annotate("",xy=(z.real,z.imag),xytext=(0,0),arrowprops=dict(arrowstyle="->",lw=2,ls=st,color=c))
    a.text(z.real*1.12-0.1,z.imag*1.15,lab,color=c,fontsize=10)
for a0,a1,lab in [(0,-E*t,r"angle $Et/\hbar$"),(-E*t,-E*(s+t),r"+ $Es/\hbar$")]:
    tt=np.linspace(a0,a1,50); r=0.35 if lab[0]=="a" else 0.55; a.plot(r*np.cos(tt),r*np.sin(tt),"k",lw=1)
    a.text(*( (0.4,-0.2) if lab[0]=="a" else (-0.75,-0.72) ),lab,fontsize=9)
a.set_aspect("equal"); a.set_xlim(-1.4,1.6); a.set_ylim(-1.4,1.4); a.set_xlabel("Re"); a.set_ylabel("Im")
a.set_title("Composition = adding rotation angles")
tg=np.linspace(0,8,600); z=U(tg)
b.plot(tg,z.real,"k-",label=r"Re $e^{-iEt/\hbar}$"); b.plot(tg,z.imag,"--",color="tab:blue",label=r"Im $e^{-iEt/\hbar}$")
b.plot(tg,abs(z)**2,":",color="tab:red",lw=2.5,label=r"$|e^{-iEt/\hbar}|^2=1$ (unitarity)")
b.set_xlabel(r"time $t$ (units $\hbar/E$)"); b.set_ylabel("value"); b.set_ylim(-1.3,1.6)
b.legend(fontsize=9,ncol=2,loc="upper center",frameon=False); b.set_title("One energy eigenstate in time")
fig.tight_layout(); fig.savefig(D+"a-composition-group.png",dpi=150); print("ok")
