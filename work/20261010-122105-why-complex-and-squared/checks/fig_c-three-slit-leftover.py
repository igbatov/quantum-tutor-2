import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out=os.path.join(os.path.dirname(__file__),"..","figures","c-three-slit-leftover.png")
plt.rcParams.update({"font.size":11})
u=np.linspace(-3,3,6001); env=np.sinc(u/4)
h={k:env*np.exp(2j*np.pi*dj*u) for k,dj in zip("ABC",(-1,0,1))}
def I3(p):
    P=lambda ks: np.abs(sum(h[k] for k in ks))**p
    return P("ABC")-P("AB")-P("AC")-P("BC")+P("A")+P("B")+P("C")
fig,ax=plt.subplots(4,1,figsize=(7.5,7.4),sharex=True)
names={1:"p = 1 (plain size)",2:"p = 2 (square)",3:"p = 3 (cube)",4:"p = 4 (fourth power)"}
for a,p in zip(ax,(1,2,3,4)):
    y=I3(p); m=np.abs(y).max()
    a.plot(u,y,"k-",lw=1.8); a.axhline(0,color="0.5",lw=0.8,ls="--")
    txt="max |I3| = 0 to rounding (%.0e)"%m if p==2 else "max |I3| = %.2f"%m
    a.text(0.99,0.88,txt,transform=a.transAxes,ha="right",va="top",fontsize=9,bbox=dict(fc="w",ec="0.6"))
    a.text(0.01,0.88,names[p],transform=a.transAxes,ha="left",va="top",fontsize=10,weight="bold")
    a.set_ylabel("I3"); a.grid(alpha=0.3)
    if p==2: a.set_ylim(-1,1)
    if p==1:
        zs=[k+f for k in range(-3,3) for f in (0,1/3,2/3)]+[3]
        a.plot(zs,np.zeros(len(zs)),"o",mfc="w",mec="k",ms=5,label="zeros")
        a.set_ylim(-0.3,2.6)
ax[3].set_xlabel("screen position x in units of the A+B stripe spacing λL/d")
fig.text(0.5,0.005,"Leftover I3 = P_ABC − P_AB − P_AC − P_BC + P_A + P_B + P_C with chance = |amplitude|^p (one slit = 1 at centre).\n"
         "Ideal far screen, independent slits, d = 4w. Measured bound: |I3| below about 0.01 of the stripe strength.\n"
         "p = 1 is never negative; its zeros (circles) are at the tall stripes and at the three-slit dark spots (1/3, 2/3).",ha="center",fontsize=8.5)
fig.tight_layout(rect=(0,0.075,1,1)); fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
