import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from matplotlib.patches import FancyBboxPatch
out=os.path.join(os.path.dirname(__file__),"..","figures","c-swap-step.png")
plt.rcParams.update({"font.size":11})
# compute the frames from the actual state vectors
a,b=np.eye(2); SW=np.array([[0,1],[1,0]])
psi=(np.kron(a,a)+np.kron(b,b))/np.sqrt(2)       # photon (a,b) x partner (A,B)
f2=np.kron(SW,np.eye(2))@psi; f3=np.kron(np.eye(2),SW)@f2
def rows(v):
    lab=[("a","A"),("a","B"),("b","A"),("b","B")]; return [(lab[k],v[k]) for k in range(4) if abs(v[k])>1e-12]
frames=[("1. start",psi),("2. swap a ↔ b\n(photon only)",f2),("3. swap A ↔ B\n(partner only)",f3)]
fig,ax=plt.subplots(figsize=(9,4)); ax.set_xlim(0,12.6); ax.set_ylim(0,5.4); ax.axis("off")
for i,(title,v) in enumerate(frames):
    x0=0.2+4.2*i
    ax.add_patch(FancyBboxPatch((x0,1.25),3.6,2.9,boxstyle="round,pad=0.05",fc="0.96",ec="k"))
    ax.text(x0+1.6,4.6,title,ha="center",va="center",fontsize=10,weight="bold")
    for k,((p,q),amp) in enumerate(sorted(rows(v),key=lambda r:r[0][0])):
        y=3.5-1.2*k
        ax.text(x0+0.2,y,f"photon {p} with partner {q}",va="center",fontsize=10)
        ax.annotate("",xy=(x0+0.2+2.0*amp,y-0.4),xytext=(x0+0.2,y-0.4),arrowprops=dict(arrowstyle="-|>",lw=2))
        ax.text(x0+0.3+2.0*amp,y-0.4,f"hand 1/√2 ≈ {amp:.3f}",va="center",fontsize=8)
    if i<2: ax.annotate("",xy=(x0+4.15,2.7),xytext=(x0+3.7,2.7),arrowprops=dict(arrowstyle="->",lw=2))
same=np.allclose(f3,psi)
ax.text(10.6,0.95,"same joint state as frame 1" if same else "DIFFERENT",ha="center",fontsize=10,weight="bold")
fig.text(0.5,0.02,"An operation on the partner alone undid the photon swap, so the photon's two chances cannot differ: ½ each.\n"
         "This is the equal-hands case only; the extension to unequal hands is the contested step.",ha="center",fontsize=9)
fig.savefig(out,dpi=150); print("saved",os.path.abspath(out),"frame3==frame1:",same)
