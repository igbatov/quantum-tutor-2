import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
t=np.linspace(0,180,721)
fig,ax=plt.subplots(figsize=(7,4))
for q,ls in [(1,"-."),(2,"-"),(3,"--"),(4,":")]:
    n=(np.abs(np.cos(np.radians(t)))**q+np.abs(np.sin(np.radians(t)))**q)**(1/q)
    ax.plot(t,n,ls,color="k",lw=2.4 if q==2 else 1.4,label=f"q = {q}")
ax.set_xlabel("rotation angle of the polarization (degrees)"); ax.set_ylabel("q-norm of (cos θ, sin θ)")
ax.set_title("Only the 2-norm (flat line) is unchanged by rotation"); ax.set_xticks([0,45,90,135,180]); ax.legend(ncol=4,loc="upper center")
ax.set_ylim(0.75,1.5); fig.tight_layout(); save(fig,"a-how-they-relate")
