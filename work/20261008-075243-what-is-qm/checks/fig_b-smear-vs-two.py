import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
out="/home/user/quantum-tutor-2/work/20261008-075243-what-is-qm/figures/b-smear-vs-two.png"
rng=np.random.default_rng(1922); n=3000; sd=0.08
# classical: isotropic moments -> deflection prop. to cos(theta), which is uniform on [-1,1] (check_B_02)
v=rng.normal(size=(n,3)); v/=np.linalg.norm(v,axis=1)[:,None]
yc=v[:,2]; xc=rng.normal(0,sd,n)
# quantum (idealized narrow beam): only +-1
s=np.where(rng.random(n)<0.5,1,-1); yq=s+rng.normal(0,sd,n); xq=rng.normal(0,sd,n)
plt.rcParams.update({"font.size":11})
fig,axs=plt.subplots(1,2,figsize=(7,4.6),sharey=True)
for ax,x,y,t in [(axs[0],xc,yc,"if atoms were tiny magnets pointing\nevery which way (classical prediction)"),
                 (axs[1],xq,yq,"what is seen\n(idealized narrow beam)")]:
    ax.scatter(x,y,s=2,c="k",alpha=0.5,linewidths=0)
    ax.set_facecolor("white"); ax.set_xlim(-0.6,0.6); ax.set_ylim(-1.45,1.45)
    ax.set_xticks([]); ax.set_title(t,fontsize=10)
    for sp_ in ax.spines.values(): sp_.set_linewidth(1.5)
axs[0].set_yticks([-1,0,1]); axs[0].set_yticklabels(["down","0","up"])
axs[0].set_ylabel("deflection along the magnet's axis")
axs[1].annotate("empty gap",xy=(0.0,0.0),xytext=(0.22,0.0),fontsize=9,va="center",
                arrowprops=dict(arrowstyle="->",lw=1))
fig.text(0.75,0.035,"the real 1922 plate shows two bands, separated in the middle and\njoined at their ends where the field is weaker; two clean clumps\nare the idealization of a very narrow beam",
         ha="center",fontsize=7.5)
fig.tight_layout(rect=(0,0.1,1,1)); fig.savefig(out,dpi=150); print("saved",out)
