import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out="/home/user/quantum-tutor-2/work/20261008-075243-what-is-qm/figures/b-three-magnets.png"
# counts from Born rule (check_B_04)
up=np.array([1,0]); dn=np.array([0,1]); L=np.array([1,-1])/np.sqrt(2); R=np.array([1,1])/np.sqrt(2)
P=lambda a,b: abs(np.vdot(a,b))**2
N=1000; zu=N*0.5; zd=N*0.5   # unpolarized source
plt.rcParams.update({"font.size":9})
fig,ax=plt.subplots(figsize=(7.5,4.6)); ax.set_xlim(0,10.5); ax.set_ylim(0,6.6); ax.axis("off")
def box(x,y,lab):
    ax.add_patch(FancyBboxPatch((x-0.6,y-0.32),1.2,0.64,boxstyle="round,pad=0.03",fc="white",ec="k",lw=1.4))
    ax.text(x,y,lab,ha="center",va="center",fontsize=7.5)
def arrow(x0,y0,x1,y1,lab,bold=False,dy=0.13):
    ax.annotate("",xy=(x1,y1),xytext=(x0,y0),arrowprops=dict(arrowstyle="->",lw=2.2 if bold else 1))
    ax.text((x0+x1)/2,(y0+y1)/2+dy,lab,ha="center",va="bottom",fontsize=8,fontweight="bold" if bold else "normal")
Zl="Z magnet\n(up/down)"; Xl="X magnet\n(left/right)"
rows=[(5.3,"ask Z twice"),(3.3,"ask Z, then X"),(1.3,"ask Z, then X, then Z")]
for y,t in rows:
    ax.text(0.05,y+0.75,t,fontsize=9,fontweight="bold",ha="left")
    arrow(0.15,y,1.0,y,f"{N} in"); box(1.6,y,Zl)
    arrow(2.2,y+0.1,3.2,y+0.45,f"{zu:.0f} up",bold=True); arrow(2.2,y-0.1,3.2,y-0.45,f"{zd:.0f} down",dy=-0.35)
# row1
y=5.3; box(3.9,y+0.45,Zl); arrow(4.5,y+0.55,5.5,y+0.85,f"{zu*P(up,up):.0f} up"); arrow(4.5,y+0.35,5.5,y+0.05,f"{zu*P(dn,up):.0f} down",dy=-0.33)
# row2
y=3.3; box(3.9,y+0.45,Xl); arrow(4.5,y+0.55,5.5,y+0.85,f"{zu*P(L,up):.0f} left"); arrow(4.5,y+0.35,5.5,y+0.05,f"{zu*P(R,up):.0f} right",dy=-0.33)
# row3
y=1.3; box(3.9,y+0.45,Xl); nl=zu*P(L,up)
arrow(4.5,y+0.55,6.4,y+0.85,f"{nl:.0f} left (take these)",bold=True,dy=0.18); arrow(4.5,y+0.35,5.5,y+0.05,f"{zu*P(R,up):.0f} right",dy=-0.33)
box(7.0,y+0.85,Zl); arrow(7.6,y+0.95,8.5,y+1.25,f"{nl*P(up,L):.0f} up"); arrow(7.6,y+0.75,8.5,y+0.45,f"{nl*P(dn,L):.0f} down",dy=-0.33)
ax.text(8.0,5.75,"same question:\nsame answer",fontsize=8,style="italic")
ax.text(5.8,3.75,"new question: 50/50",fontsize=8,style="italic")
ax.text(8.75,1.95,"old 'up' answer\nis gone: 50/50",fontsize=8,style="italic")
ax.set_title("The newest answer is kept; the older one is gone",fontsize=11)
fig.text(0.5,0.02,"counts are expected averages for an ideal set-up and a source whose atoms have not been lined up",ha="center",fontsize=8)
fig.tight_layout(rect=(0,0.04,1,1)); fig.savefig(out,dpi=150); print("saved",out)
