import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
from scipy.stats import binom
from scipy.special import logsumexp
p=0.25
Ns=np.unique(np.concatenate([np.arange(10,2001),np.logspace(np.log10(2000),5,120).astype(int)]))
def logdev(N,eps):
    m=np.arange(N+1); lw=binom.logpmf(m,N,p); mask=np.abs(m/N-p)>eps+1e-12
    return logsumexp(lw[mask])
fig,ax=plt.subplots(figsize=(7,4.5))
ends={}
for eps,ls in [(0.05,"-"),(0.1,"-")]:
    ld=np.array([logdev(N,eps) for N in Ns])/np.log(10); ends[eps]=ld[-1]
    lw=1.6 if eps==0.05 else 1.0
    ax.plot(Ns,10**np.maximum(ld,-300),ls,color="k" if eps==0.05 else "tab:blue",lw=lw,label=f"exact deviant, ε = {eps}")
    ax.plot(Ns,p*(1-p)/(Ns*eps**2),"--",color="k" if eps==0.05 else "tab:blue",label=f"bound {p*(1-p)/eps**2:g}/N, ε = {eps}")
ax.plot(Ns,p*(1-p)/Ns,":",color="gray",lw=2,label="p(1−p)/N = 0.1875/N")
ax.set_xscale("log"); ax.set_yscale("log"); ax.set_ylim(1e-30,20); ax.set_xlim(10,1e5)
ax.axhline(1,color="gray",lw=0.5)
ax.text(1.2e3,3e-29,f"exact curves continue off the plot, never reaching 0:\n$10^{{{ends[0.05]:.0f}}}$ (ε=0.05) and $10^{{{ends[0.1]:.0f}}}$ (ε=0.1) at N = $10^5$",fontsize=9,va="bottom")
ax.annotate("zigzag: m/N takes only\nmultiples of 1/N",(14,0.5),(30,1e-6),fontsize=9,arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("number of photons N"); ax.set_ylabel("squared length (dimensionless)")
ax.set_title("Squared length of the deviant part, p = 1/4"); ax.legend(loc="lower left",fontsize=9)
fig.tight_layout(); save(fig,"a-deviant-length")
