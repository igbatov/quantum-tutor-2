import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
P=np.linspace(0,1,400); c1=np.sqrt(P); c0=np.sqrt(1-P)
fig,ax=plt.subplots(figsize=(7,4))
for q,ls,mk in [(1,"-.",None),(2,"-",None),(3,"--",None),(4,":",None)]:
    f=c1**q/(c0**q+c1**q); ax.plot(P,f,ls,color="k",lw=2.2 if q==2 else 1.4,label=f"q = {q}")
ax.plot([0.5],[0.5],"o",color="k",ms=8,mfc="white"); ax.annotate("50/50 splitter: all exponents give ½",(0.5,0.5),(0.55,0.15),fontsize=10,arrowprops=dict(arrowstyle="->"))
ax.axvline(0.25,color="gray",lw=0.8); ax.text(0.26,0.9,"25/75 split:\nexponents disagree",fontsize=10)
ax.set_xlabel("|c₁|² (squared amplitude for R)"); ax.set_ylabel("dominant R-fraction f_q")
ax.set_title("Dominant fraction if size were measured with exponent q"); ax.legend(loc="upper left")
fig.tight_layout(); save(fig,"a-experiment-2")
