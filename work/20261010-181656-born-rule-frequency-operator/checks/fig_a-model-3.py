import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
from scipy.stats import binom
p=0.9
fig,(a1,a2)=plt.subplots(1,2,figsize=(7.5,4))
N=4; m=np.arange(N+1); w=binom.pmf(m,N,p); c=binom.pmf(m,N,0.5)
a1.bar(m/N-0.04,w,0.08,color="k",label="weight $w_m$"); a1.bar(m/N+0.04,c,0.08,color="white",edgecolor="k",hatch="//",label="share by count")
a1.set_xticks(m/N); a1.set_xticklabels(["0","¼","½","¾","1"]); a1.set_xlabel("R-fraction m/N"); a1.set_ylabel("share of total")
a1.set_title("N = 4, p = 0.9"); a1.legend(fontsize=9,loc="upper left")
N=100; m=np.arange(N+1)
a2.plot(m/N,binom.pmf(m,N,p),"-",color="k",lw=2,label="weight"); a2.plot(m/N,binom.pmf(m,N,0.5),"--",color="k",label="share by count")
a2.axvline(0.9,color="gray",lw=0.8); a2.axvline(0.5,color="gray",lw=0.8)
a2.set_xlabel("R-fraction m/N"); a2.set_title("N = 100, p = 0.9"); a2.legend(fontsize=9,loc="upper left")
fig.suptitle("Weight piles up at p; branch count piles up at ½",y=1.0); fig.tight_layout(); save(fig,"a-model-3")
