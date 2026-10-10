import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
from matplotlib.patches import FancyBboxPatch
out=os.path.join(os.path.dirname(__file__),"..","figures","c-map.png")
plt.rcParams.update({"font.size":10})
fig,ax=plt.subplots(figsize=(10,6)); ax.set_xlim(0,10); ax.set_ylim(0,6.2); ax.axis("off")
def box(x,y,w,h,t,ls="-",fc="0.95",fs=10):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05",fc=fc,ec="k",ls=ls,lw=1.4)); ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs)
box(0.4,4.9,3.8,0.9,"Model 1: overlaps of\ntwo-component complex states")
box(5.8,4.9,3.8,0.9,"Model 2: squared length of a\nsum over alternatives")
ax.text(5.0,5.35,"=",ha="center",va="center",fontsize=22,weight="bold")
ax.text(5.0,6.05,"shared line: chance = squared length of a sum, pair pieces only",ha="center",fontsize=9.5,style="italic")
box(3.3,2.0,3.4,0.7,"Model 3: theorems",fc="0.85",fs=11)
labs=[(1.6,0.9,"three sorters ⇒\npairs of reals\n(one system)"),(4.2,5.0,"parameter count +\nnetwork test ⇒ pairs of\nreals (composite systems)"),(8.4,9.1,"three-slit null\n+ Gleason\n⇒ exponent 2")]
for xt,xl,t in labs:
    ax.annotate("",xy=(xt,4.85),xytext=(5.0,2.77),arrowprops=dict(arrowstyle="-|>",lw=1.5))
    ax.text(xl,3.8,t,ha="center",va="center",fontsize=8.5,bbox=dict(fc="w",ec="0.7",pad=2))
names=["Copenhagen-style","many-worlds","pilot-wave","objective collapse"]
for i,n in enumerate(names): box(0.3+2.4*i,0.35,2.0,0.6,n,ls="--" if i==3 else "-",fc="w")
ax.plot([0.3,7.1],[1.15,1.15],"k-",lw=1.2); ax.plot([0.3,0.3],[1.0,1.15],"k-"); ax.plot([7.1,7.1],[1.0,1.15],"k-")
ax.text(3.7,1.3,"same predictions, differ on meaning",ha="center",fontsize=9)
ax.text(8.5,1.35,"slightly changed law;\ndepartures not found so far",ha="center",fontsize=8.5)
fig.text(0.5,0.02,"How the pieces relate: Models 1 and 2 are one rule; Model 3 says why the i and the 2; interpretations differ on meaning.",ha="center",fontsize=9)
fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
