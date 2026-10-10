import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11})
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","b-how-they-relate.png")
p=np.linspace(0,1,501)
fig,ax=plt.subplots(figsize=(7,4.5))
for q,ls in [(1,"-."),(2,"-"),(3,"--"),(4,":")]:
    f=p**(q/2)/((1-p)**(q/2)+p**(q/2)); ax.plot(p,f,ls,lw=3 if q==2 else 1.8,color="k" if q==2 else None,label=f"q = {q}"+("  (lies on f = p)" if q==2 else ""))
ax.plot(0.5,0.5,"ko",ms=6); ax.annotate("all q agree at p = 1/2",xy=(0.5,0.5),xytext=(0.55,0.3),arrowprops=dict(arrowstyle="->"),fontsize=9)
for q in [1,2,3,4]:
    ax.plot(0.1,1/(3**q+1),"o",color="0.3",ms=4)
ax.annotate("p = 0.1: f = 0.25, 0.10, 0.036, 0.012\n(q = 1, 2, 3, 4)",xy=(0.1,0.1),xytext=(0.2,0.04),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.text(0.6,0.12,"all q also agree at p = 0 and p = 1",fontsize=9)
ax.set_xlabel("p = |c_1|^2 (dimensionless)"); ax.set_ylabel("fraction f_q where the q-size of the\nN-copy list concentrates")
ax.set_title("Which exponent? Only the 2-norm makes the long-run fraction equal |c_1|^2",fontsize=10)
ax.legend(fontsize=9,loc="upper left"); fig.tight_layout(); fig.savefig(out,dpi=150); print(out)
