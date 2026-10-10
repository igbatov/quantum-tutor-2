import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out=os.path.join(os.path.dirname(__file__),"..","figures","c-three-slit-patterns.png")
plt.rcParams.update({"font.size":11})
u=np.linspace(-3,3,6001); env=np.sinc(u/4)   # d = 4w; u = x d/(lambda L)
h={k:env*np.exp(2j*np.pi*dj*u) for k,dj in zip("ABC",(-1,0,1))}
P=lambda ks: np.abs(sum(h[k] for k in ks))**2
fig,ax=plt.subplots(3,1,figsize=(7.5,6.6),sharex=True)
for k,ls in zip("ABC",["-","--",":"]): ax[0].plot(u,P(k),ls,lw=2,label=f"slit {k} alone")
ax[0].set_ylim(0,1.2); ax[0].legend(fontsize=8,loc="upper right",ncol=3); ax[0].set_title("single slits (all three curves coincide)",fontsize=10)
ax[1].plot(u,P("AB"),"-",lw=2,label="A+B"); ax[1].plot(u,P("BC"),"--",lw=1.5,label="B+C (same as A+B)")
ax[1].plot(u,P("AC"),"-",color="0.5",lw=1.2,label="A+C (stripes half as far apart)")
ax[1].set_ylim(0,4.6); ax[1].legend(fontsize=8,loc="upper right"); ax[1].set_title("pairs (4 at the centre)",fontsize=10)
abc=P("ABC"); ax[2].plot(u,abc,"k-",lw=2,label="A+B+C")
for z in (1/3,2/3,-1/3,-2/3): ax[2].plot(z,0,"v",color="k",ms=7)
ax[2].annotate("weak stripe ≈ 0.95",xy=(0.5,0.95),xytext=(1.1,4.5),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax[2].annotate("zeros at 1/3 and 2/3",xy=(0.6667,0),xytext=(1.25,2.5),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax[2].set_ylim(0,9.8); ax[2].set_title("all three open (9 at the centre)",fontsize=10)
ax[2].set_xlabel("screen position x in units of the A+B stripe spacing λL/d")
for a in ax: a.set_ylabel("chance\n(one slit = 1)"); a.grid(alpha=0.3)
fig.text(0.5,0.005,"Ideal far-screen (Fraunhofer) patterns, slit width w, spacing d = 4w, each slit's wave independent of the others.\n"
         "The three-slit pattern is not the pair patterns added, yet it equals (pairs added) − (singles added) at every x.",ha="center",fontsize=8.5)
fig.tight_layout(rect=(0,0.06,1,1)); fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
