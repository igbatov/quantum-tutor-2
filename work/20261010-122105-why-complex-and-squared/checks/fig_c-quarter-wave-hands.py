import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out=os.path.join(os.path.dirname(__file__),"..","figures","c-quarter-wave-hands.png")
plt.rcParams.update({"font.size":10})
r=1/np.sqrt(2)
basis={"H":np.array([1,0]),"V":np.array([0,1]),"D":np.array([r,r]),"A":np.array([r,-r]),"R":np.array([r,1j*r]),"L":np.array([r,-1j*r])}
P=lambda e,s: abs(np.vdot(basis[e],s))**2
Q=np.diag([1,1j]); D=basis["D"]
states=[("D = (1, 1)/√2",D),("after one λ/4 plate:\nR = (1, i)/√2",Q@D),("after a second plate:\nA = (1, −1)/√2",Q@Q@D)]
fig,axs=plt.subplots(2,3,figsize=(9,7.2))
for j,(title,s) in enumerate(states):
    for i,(comp,name,ls,col) in enumerate(((s[0],"H hand","-","k"),(s[1],"V hand","--","tab:blue"))):
        ax=axs[i,j]
        ax.add_patch(plt.Circle((0,0),r,fill=False,ls=":",color="0.6"))
        ax.axhline(0,color="0.75",lw=0.8); ax.axvline(0,color="0.75",lw=0.8)
        ax.annotate("",xy=(comp.real,comp.imag),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",lw=2.5,ls=ls,color=col,mutation_scale=18))
        ax.text(0.03,0.97,f"{name}: length {abs(comp):.3f}",transform=ax.transAxes,va="top",fontsize=9,color=col)
        ax.set_xlim(-1,1); ax.set_ylim(-1,1); ax.set_aspect("equal"); ax.set_xticks([-0.7,0,0.7]); ax.set_yticks([-0.7,0,0.7])
        ax.set_ylabel("imag. part",fontsize=9)
        if i==1: ax.set_xlabel("real part",fontsize=9)
        else: ax.set_xticklabels([])
        if i==0: ax.set_title(title,fontsize=10)
    tbl="H/V %3d / %-3d\nD/A %3d / %-3d\nR/L %3d / %-3d"%tuple(round(100*P(e,s)) for e in ("H","V","D","A","R","L"))
    axs[1,j].text(0.5,-0.38,"chances (%)\n"+tbl,transform=axs[1,j].transAxes,ha="center",va="top",fontsize=9.5,family="monospace")
fig.text(0.5,0.01,"The quarter-wave plate (slow axis V) multiplies the V hand by i. No hand changes length; only the V hand turns a quarter turn,\n"
         "and that alone moves the sure bet: D/A (D exit) → R/L (R exit) → D/A (A exit). Chances computed from Model 1.",ha="center",fontsize=8.5)
fig.tight_layout(rect=(0,0.15,1,0.97)); fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
