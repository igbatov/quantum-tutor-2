import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
plt.rcParams.update({"font.size":11})
here=os.path.dirname(os.path.abspath(__file__)); out=os.path.join(here,"..","figures","c-shadow.png")
theta=np.radians(45)               # angle from vertical
vx,vy=np.sin(theta),np.cos(theta)  # components = amplitudes
amp=vy; chance=amp**2
fig=plt.figure(figsize=(7,4.2))
ax=fig.add_axes([0.02,0.04,0.62,0.92])
ax.plot([0,0],[-0.25,1.2],ls="--",color="k",lw=1.2)
ax.text(0.03,1.17,"vertical filter's direction",va="top",fontsize=10)
ax.plot([0,vx],[vy,vy],ls=":",color="gray",lw=1.2); ax.plot([vx,vx],[0,vy],ls=":",color="gray",lw=1.2)
ax.plot([0,vx],[0,0],ls=":",color="tab:blue",lw=2)
ax.text(vx/2,-0.07,f"horizontal piece = {vx:.2f}",ha="center",va="top",fontsize=10,color="tab:blue")
ax.plot([0,0],[0,vy],color="tab:orange",lw=7,solid_capstyle="butt",alpha=0.9)
ax.text(-0.04,vy/2,f"shadow = amplitude\n= {amp:.2f}",ha="right",va="center",fontsize=10,color="tab:red",fontweight="bold")
ax.annotate("",xy=(vx,vy),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",lw=2.5,color="k",mutation_scale=18))
ax.text(vx+0.03,vy+0.03,"photon's polarization\n(45°)",fontsize=10,va="bottom")
ax.text(0.15,-0.33,f"chance to pass = {amp:.2f} × {amp:.2f} ≈ {chance:.1f}",fontsize=11,
        bbox=dict(boxstyle="round",fc="lightyellow",ec="gray"))
ax.set_xlim(-0.75,1.15); ax.set_ylim(-0.45,1.3); ax.set_aspect("equal"); ax.axis("off")
for i,(ang,title) in enumerate([(0,"along the line"),(90,"at right angles")]):
    a=fig.add_axes([0.66,0.50-0.47*i,0.32,0.38])
    t=np.radians(ang); x,y=np.sin(t),np.cos(t); s=abs(y)
    a.plot([0,0],[-0.2,1.15],ls="--",color="k",lw=1)
    a.annotate("",xy=(0.9*x,0.9*y),xytext=(0,0),arrowprops=dict(arrowstyle="-|>",lw=2,color="k"))
    if s>0: a.plot([0,0],[0,0.9*s],color="tab:orange",lw=6,alpha=0.6,solid_capstyle="butt")
    else: a.plot([0],[0],"o",color="tab:orange",ms=6)
    a.set_title(f"{title}:\nshadow {s:.0f}, chance {s**2:.0f}",fontsize=10)
    a.set_xlim(-0.3,1.1); a.set_ylim(-0.25,1.2); a.set_aspect("equal"); a.axis("off")
fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
