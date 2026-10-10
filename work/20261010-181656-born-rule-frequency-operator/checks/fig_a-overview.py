import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
p=0.25; lam=np.linspace(0,1,500)
fig,ax=plt.subplots(figsize=(7,4))
for N,ls in [(2,"-"),(10,"--"),(100,":")]:
    y=(lam-p)**2+p*(1-p)/N; ax.plot(lam,y,ls,color="k",lw=2,label=f"N = {N}")
    ax.plot([p],[p*(1-p)/N],"o",color="k",ms=5)
ax.axvline(p,color="gray",lw=0.8); ax.text(p+0.01,0.5,"λ = |c₁|² = 0.25",fontsize=10)
ax.set_xlabel("trial counter reading λ"); ax.set_ylabel("squared miss ‖(F_N − λ)Ψ_N‖²")
ax.set_title("Squared miss vs λ, θ = 30° (p = 0.25): minimum at λ = p, depth p(1−p)/N")
ax.legend(); fig.tight_layout(); save(fig,"a-overview")
