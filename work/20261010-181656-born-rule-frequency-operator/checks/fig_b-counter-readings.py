import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from math import comb
plt.rcParams.update({"font.size":11})
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","b-counter-readings.png")
N=4; x=np.arange(N+1)/N
fig,axs=plt.subplots(1,2,figsize=(10,4.6),sharey=True)
for ax,p,lab in [(axs[0],0.5,"p = 1/2"),(axs[1],0.1,"p = 0.1")]:
    for m in range(N+1):
        each=p**m*(1-p)**(N-m)
        for k in range(comb(N,m)):
            ax.bar(x[m],each,bottom=k*each,width=0.16,color="0.55",edgecolor="white",linewidth=1.2)
        w=comb(N,m)*each
        ax.text(x[m],w+0.02,f"{w:.4g}",ha="center",fontsize=9,bbox=dict(fc="white",ec="none",pad=1))
    ax.axvline(p,ls="--",color="k",lw=1.3); ax.text(p+0.01,0.93,f"p = {p}",fontsize=9)
    sd=np.sqrt(p*(1-p)/N); yb=0.8
    ax.annotate("",xy=(p-sd,yb),xytext=(p+sd,yb),arrowprops=dict(arrowstyle="|-|",lw=1.3))
    ax.text(p,yb+0.03,f"spread sqrt(p(1-p)/4) = {sd:.2f}",ha="center",fontsize=9,bbox=dict(fc="white",ec="none",pad=1))
    ax.text(0.98,0.55,"heights total 1",ha="right",transform=ax.transAxes,fontsize=10)
    ax.set_title(lab+" ("+" + ".join(str(comb(N,m)) for m in range(N+1))+" = 16 blocks, one per string)",fontsize=10)
    ax.set_xticks(x); ax.set_xlim(-0.2,1.2); ax.set_ylim(0,1)
    ax.set_xlabel("reading of the counter F_4 (fraction of ions up)")
axs[0].set_ylabel("squared length w_m of the piece\nof the list with that reading")
axs[1].text(0.88,0.12,"bars at 0.75 and 1:\n0.0036 and 0.0001,\nnonzero but too small to see",fontsize=8,ha="center")
fig.suptitle("The list Psi_4 split by the counter's reading",fontsize=12)
fig.tight_layout(); fig.savefig(out,dpi=150); print(out)
