import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
from scipy.stats import binom
p=0.25
fig,axs=plt.subplots(1,4,figsize=(7.5,4),sharey=False)
for ax,N in zip(axs,[4,16,64,256]):
    m=np.arange(N+1); w=binom.pmf(m,N,p)
    ax.vlines(m/N,0,w,color="k",lw=max(0.6,6/np.sqrt(N)))
    ax.axvline(0.25,ls="--",color="gray")
    s=np.sqrt(p*(1-p)/N)
    ax.set_title(f"N = {N}\nspread {s:.3f}"); ax.set_xlim(-0.03,1.03); ax.set_xticks([0,0.25,0.5,1]); ax.set_xticklabels(["0","¼","½","1"])
    ax.set_xlabel("counter reading m/N"); ax.text(0.97,0.80,f"total {w.sum():.3f}",transform=ax.transAxes,ha="right",va="top",fontsize=9)
    if N==4: ax.annotate(f"w at ¼: {binom.pmf(1,4,p):.2f}",(0.25,binom.pmf(1,4,p)),(0.45,0.36),fontsize=9,arrowprops=dict(arrowstyle="->"))
axs[0].set_ylabel("squared length $w_m$ (dimensionless)")
fig.suptitle("Weights $w_m=C(N,m)p^m(1-p)^{N-m}$, p = 1/4 (dashed: 1/4)",y=1.02)
fig.tight_layout(); save(fig,"a-weights-concentrate")
