import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from fractions import Fraction
plt.rcParams.update({"font.size":11})
here=os.path.dirname(os.path.abspath(__file__)); out=os.path.join(here,"..","figures","c-filters.png")
def malus_chain(angles):
    fr=[Fraction(1)]; cur=None
    for a in angles:
        if cur is None: f=Fraction(1,2)
        else:
            c2=np.cos(np.radians(a-cur))**2; f=Fraction(c2).limit_denominator(8)
        fr.append(fr[-1]*f); cur=a
    return fr
def darrow(ax,x,y,ang,L=0.28,**kw):  # ang from vertical, double-headed
    t=np.radians(ang); dx,dy=L*np.sin(t)/2,L*np.cos(t)/2
    ax.annotate("",xy=(x+dx,y+dy),xytext=(x-dx,y-dy),arrowprops=dict(arrowstyle="<|-|>",lw=2,color=kw.get("c","k"),mutation_scale=7,shrinkA=0,shrinkB=0))
def filt(ax,x,y,ang):
    ax.add_patch(plt.Circle((x,y),0.3,fill=False,lw=2))
    t=np.radians(ang); dx,dy=0.27*np.sin(t),0.27*np.cos(t)
    ax.plot([x-dx,x+dx],[y-dy,y+dy],color="k",lw=2.5)
fig,ax=plt.subplots(figsize=(7.5,4.2))
rng=np.random.default_rng(3)
rows=[("Two crossed filters",[0,90],1.6),("Slip a 45° filter in between",[0,45,90],0.0)]
for title,angles,y in rows:
    ax.text(-0.2,y+0.62,title,fontsize=12,fontweight="bold")
    fr=malus_chain(angles)
    # unpolarized
    for ang,dx,dy in zip(rng.uniform(0,180,4),[-0.12,0.12,-0.12,0.12],[0.12,0.12,-0.12,-0.12]):
        darrow(ax,0.3+dx,y+dy,ang,L=0.3,c="gray")
    ax.text(0.3,y-0.5,"1",ha="center")
    x=0.3
    for i,a in enumerate(angles):
        x+=0.85; filt(ax,x,y,a); ax.annotate("",xy=(x-0.33,y),xytext=(x-0.62,y),arrowprops=dict(arrowstyle="->",color="lightgray"))
        x+=0.85
        f=fr[i+1]
        if f>0:
            pass
            for dxx in (-0.13,0.13): darrow(ax,x+dxx,y,a,L=0.42,c="tab:blue")
        else:
            ax.text(x,y,"nothing",ha="center",va="center",fontsize=10,color="tab:red",fontweight="bold")
        ax.text(x,y-0.5,str(f),ha="center",fontsize=12,fontweight="bold" if i==len(angles)-1 else None)
        if i<len(angles)-1 or f>0: ax.annotate("",xy=(x-0.3,y),xytext=(x-0.52,y),arrowprops=dict(arrowstyle="->",color="lightgray"))
ax.text(-0.2,-0.95,"line in circle = direction the filter passes;  numbers = fraction of the original light",fontsize=10)
ax.text(6.0,-0.95,"light travels →",fontsize=10,ha="right")
ax.set_xlim(-0.3,5.6); ax.set_ylim(-1.1,2.35); ax.set_aspect("equal"); ax.axis("off")
fig.tight_layout(); fig.savefig(out,dpi=150); print("saved",os.path.abspath(out),"fractions",malus_chain([0,90]),malus_chain([0,45,90]))
