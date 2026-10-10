import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.stats import binom
plt.rcParams.update({"font.size":11})
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","b-what-this-rules-out.png")
N=100; m=np.arange(N+1)
fig,axs=plt.subplots(1,2,figsize=(11,4.4),sharey=True)
for ax,p in zip(axs,[0.5,0.1]):
    ax.bar(m,binom(N,p).pmf(m),width=0.9,color="0.6",edgecolor="0.3",label="tickets / biased coin / quantum (identical):\nbinomial, mean %g, spread %g" % (N*p,np.sqrt(N*p*(1-p))))
    ax.vlines(N*p,0,0.42,colors="k",linestyles="--",lw=2.5,label="fixed-share glow picture:\nlight of exactly %g ions every run" % (N*p))
    ax.set_xlim(N*p-25 if p==0.5 else -1, N*p+25 if p==0.5 else 30)
    ax.set_title(f"100 ions, p = {p}",fontsize=10); ax.set_xlabel("ions found up in one run (count)")
    ax.legend(fontsize=8.5,loc="upper left" if p==0.5 else "upper right")
    ax.text(N*p+0.7,0.24,"(all runs here:\n true height 1,\n off scale)",fontsize=8)
axs[0].set_ylabel("fraction of runs with that count"); axs[0].set_ylim(0,0.45)
fig.suptitle("Run-to-run counts: three pictures predict the same scatter; the fixed-share picture predicts none",fontsize=11)
fig.tight_layout(); fig.savefig(out,dpi=150); print(out)
