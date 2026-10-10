import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
rng=np.random.default_rng(0)
def alpha(I): return np.mean(0.75*I*0.25*I)/(np.mean(0.75*I)*np.mean(0.25*I))
vals=[("classical wave,\nsteady",alpha(np.ones(10**5))),("classical wave,\nthermal",alpha(rng.exponential(1,10**6))),("ideal single\nphoton",0.0)]
fig,ax=plt.subplots(figsize=(7,4))
x=np.arange(4); hatches=["//","//","..","xx"]
for i,(n,v) in enumerate(vals): ax.bar(i,v,color="white",edgecolor="k",hatch=hatches[i])
ax.bar(3,0.18,yerr=0.06,color="lightgray",edgecolor="k",hatch="xx",capsize=6)
ax.set_xticks(x); ax.set_xticklabels([v[0] for v in vals]+["measured\n(Grangier et al. 1986)"],fontsize=10)
ax.text(2,0.04,"α = 0",ha="center",fontsize=11); ax.axhline(1,ls="--",color="k"); ax.text(2.6,1.05,"classical floor: α ≥ 1",fontsize=10)
ax.set_ylabel("double-firing ratio α\n(coincidences / independent-click rate)"); ax.set_ylim(0,2.4)
ax.set_title("Coincidence test at a beam splitter (bars 1-3 computed; bar 4 quoted)",fontsize=11)
fig.tight_layout(); save(fig,"a-classical-candidates")
