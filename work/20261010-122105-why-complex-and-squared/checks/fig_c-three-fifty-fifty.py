import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out=os.path.join(os.path.dirname(__file__),"..","figures","c-three-fifty-fifty.png")
plt.rcParams.update({"font.size":11})
fig=plt.figure(figsize=(11,5.2))
ax=fig.add_axes([0.06,0.25,0.42,0.68])
th=np.linspace(0,180,1801); t=np.radians(th)
pH=np.cos(t)**2; pD=(1+np.sin(2*t))/2
ax.plot(th,pH,"k-",lw=2,label="H-exit chance cos²θ"); ax.plot(th,pD,"k--",lw=2,label="D-exit chance cos²(θ−45°)")
ax.axhline(0.5,color="0.5",lw=1)
ax.plot([45,135],[0.5,0.5],"o",ms=9,mfc="w",mec="k",mew=2,label="H curve = 1/2")
ax.plot([0,90,180],[0.5,0.5,0.5],"s",ms=8,mfc="0.6",mec="k",label="D curve = 1/2")
ax.set_xlabel("angle θ of the real arrow (cos θ, sin θ) (degrees)"); ax.set_ylabel("chance")
ax.set_xticks([0,45,90,135,180]); ax.set_ylim(-0.02,1.25); ax.legend(fontsize=8,loc="upper center",ncol=2); ax.grid(alpha=0.3)
ax.set_title("real arrows: no θ is 50/50 at both sorters",fontsize=10)
ax3=fig.add_axes([0.52,0.17,0.46,0.8],projection="3d")
u=np.linspace(0,2*np.pi,400)
uu,vv=np.meshgrid(np.linspace(0,2*np.pi,40),np.linspace(0,np.pi,20))
ax3.plot_wireframe(np.cos(uu)*np.sin(vv),np.sin(uu)*np.sin(vv),np.cos(vv),color="0.85",lw=0.4)
ax3.plot(np.cos(u),np.sin(u),0*u,"k-",lw=3,label="real arrows (H, D, V, A)")
ax3.plot(0*u,np.cos(u),np.sin(u),"--",color="tab:blue",lw=2,label="even bet at H/V (D, A, R, L)")
ax3.plot(np.cos(u),0*u,np.sin(u),":",color="tab:red",lw=2.5,label="even bet at D/A (H, V, R, L)")
pts={"H":(1,0,0),"V":(-1,0,0),"D":(0,1,0),"A":(0,-1,0),"R":(0,0,1),"L":(0,0,-1)}
for k,(x,y,z) in pts.items():
    big=k in "RL"
    ax3.scatter([x],[y],[z],s=90 if big else 30,c="gold" if big else "k",edgecolors="k",depthshade=False)
    ax3.text(x*1.18,y*1.18,z*1.18,k,fontsize=13,weight="bold")
ax3.set_box_aspect((1,1,1)); ax3.set_axis_off(); ax3.view_init(elev=22,azim=35)
ax3.legend(fontsize=8,loc="upper left",bbox_to_anchor=(0.0,1.02))
ax3.text2D(0.5,0.02,"the two even-bet circles cross only at R and L (gold),\nwhich lie off the real-arrow circle",transform=ax3.transAxes,ha="center",fontsize=9)
fig.text(0.5,0.015,"Left: one real number per exit. The H curve is 1/2 only at 45° and 135°, the D curve only at 0°, 90°, 180°: no θ puts both at 1/2.\n"
         "Right: the Poincaré sphere, a picture of Model 1's two-component complex states (one point per state; opposite points are perfectly distinguishable).",ha="center",fontsize=8.5)
fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
