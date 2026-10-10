import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.stats import binom
plt.rcParams.update({"font.size":11})
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","b-model-2.png")
p=0.1; eps=0.05
fig,ax=plt.subplots(figsize=(7.5,4.5))
for N,ls,mk in [(10,"-","o"),(100,"--","s"),(1000,":",None)]:
    m=np.arange(N+1); w=binom(N,p).pmf(m)
    ax.plot(m/N,w*N,ls,marker=mk,ms=4,lw=1.8,label=f"N = {N}: spread {np.sqrt(p*(1-p)/N):.3f}")
ax.axvspan(p-eps,p+eps,color="0.85",zorder=0); ax.text(p+eps+0.005,40,"typical band |m/N - p| <= 0.05",fontsize=9)
ax.axvline(p,color="k",lw=1)
ax.set_xlim(0,0.5); ax.set_xlabel("fraction m/N of ions up")
ax.set_ylabel("N x w_m  (w_m = C(N,m) p^m (1-p)^(N-m))")
ax.set_title("p = 0.1: the same numbers are coin probabilities or squared lengths;\nthey pile up at m/N = p as N grows (law of large numbers)",fontsize=10)
ax.legend(fontsize=9); fig.tight_layout(); fig.savefig(out,dpi=150); print(out)
