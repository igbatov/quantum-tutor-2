import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
from scipy.stats import binom
p=0.25; N=100; m=np.arange(N+1); w=binom.pmf(m,N,p)
rng=np.random.default_rng(5); sim=rng.binomial(N,p,5000)
fig,ax=plt.subplots(figsize=(7,4))
ax.vlines(m/N,0,w,color="k",lw=3,label="binomial, N = 100, p = 0.25")
h=np.bincount(sim,minlength=N+1)/len(sim); ax.plot(m/N,h,"o",mfc="white",mec="k",ms=4,label="5000 simulated runs")
s=np.sqrt(p*(1-p)/N); ax.axvline(p,ls="--",color="gray")
ax.annotate("",(p-s,0.1),(p+s,0.1),arrowprops=dict(arrowstyle="<->")); ax.text(p+s+0.01,0.1,f"±σ = ±{s:.3f}",va="center")
ax.set_xlim(0.05,0.5); ax.set_xlabel("reflected fraction m/N in a run"); ax.set_ylabel("probability (Born rule assumed)")
ax.set_title("Model 1: with chance = squared length, counts are binomial"); ax.legend(); fig.tight_layout(); save(fig,"a-model-1")
