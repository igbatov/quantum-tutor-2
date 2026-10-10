import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
import numpy as np, os
out=os.path.join(os.path.dirname(__file__),"..","figures","c-sorter-table.png")
plt.rcParams.update({"font.size":11})
fig=plt.figure(figsize=(9,4.6))
axL=fig.add_axes([0.01,0.14,0.43,0.84]); axR=fig.add_axes([0.58,0.18,0.40,0.66])
axL.set_xlim(0,10); axL.set_ylim(0,9); axL.axis("off")
def cube(ax,x,y,rot45,label,qwp=False,ports=None):
    ax.annotate("",xy=(x-0.1,y),xytext=(x-2.6 if not qwp else x-3.6,y),arrowprops=dict(arrowstyle="->",lw=1.5))
    if qwp:
        ax.add_patch(Rectangle((x-1.7,y-0.7),0.35,1.4,fc="0.75",ec="k",hatch="//"))
        ax.text(x-1.52,y+0.85,"λ/4 plate\n(slow axis V)",ha="center",va="bottom",fontsize=8)
    ax.add_patch(Rectangle((x,y-0.6),1.2,1.2,fc="0.92",ec="k",lw=1.5))
    if rot45: ax.plot([x+0.15,x+1.05],[y-0.45,y+0.45],"k-",lw=1.2); ax.text(x+0.6,y+0.75,"cube turned 45°",ha="center",fontsize=8)
    else: ax.plot([x,x+1.2],[y-0.6,y+0.6],"k-",lw=1.2); ax.text(x+0.6,y+0.75,"axis horizontal",ha="center",fontsize=8)
    ax.annotate("",xy=(x+2.6,y),xytext=(x+1.2,y),arrowprops=dict(arrowstyle="->",lw=1.3))
    ax.annotate("",xy=(x+0.6,y-1.25),xytext=(x+0.6,y-0.6),arrowprops=dict(arrowstyle="->",lw=1.3))
    ax.add_patch(Polygon([[x+2.6,y-0.3],[x+2.6,y+0.3],[x+3.05,y]],fc="k"))
    ax.add_patch(Polygon([[x+0.3,y-1.25],[x+0.9,y-1.25],[x+0.6,y-1.65]],fc="k"))
    a,b=ports if ports else label.split("/")
    ax.text(x+3.2,y,a+" exit",va="center",fontsize=10,weight="bold"); ax.text(x+1.05,y-1.45,b+" exit",va="center",fontsize=10,weight="bold")
    ax.text(0.0,y+0.25,label+"\nsorter",fontsize=11,weight="bold",va="bottom")
cube(axL,4.2,7.7,False,"H/V"); cube(axL,4.2,4.7,True,"D/A"); cube(axL,4.2,1.7,True,"R/L",qwp=True,ports=("L","R"))
# Model 1: Q R = A, Q L = D (Q = diag(1, i)); the 45° cube sends D forward and A sideways (as in the D/A row),
# so after the plate L leaves by the forward (D) port and R by the sideways (A) port.
Q=np.diag([1,1j]); R=np.array([1,1j])/np.sqrt(2); L=np.array([1,-1j])/np.sqrt(2)
D=np.array([1,1])/np.sqrt(2); A=np.array([1,-1])/np.sqrt(2)
assert np.allclose(Q@R,A) and np.allclose(Q@L,D)
axL.text(6.75,0.55,"plate turns R into A, L into D:\nR leaves by the A port (sideways),\nL by the D port (forward)",fontsize=7.5,va="center",style="italic")
axL.text(1.7,8.0,"photon in",fontsize=8)
rows=["H","D","R"]; cols=["H/V","D/A","R/L"]
for i,r in enumerate(rows):
    for j,c in enumerate(cols):
        sure=(i==j)
        axR.add_patch(Rectangle((j,2-i),1,1,fc="0.25" if sure else "0.88",ec="k"))
        axR.text(j+0.5,2-i+0.5,"100 / 0" if sure else "50 / 50",ha="center",va="center",
                 color="w" if sure else "k",fontsize=13,weight="bold" if sure else "normal")
axR.set_xlim(0,3); axR.set_ylim(0,3); axR.set_xticks([0.5,1.5,2.5]); axR.set_xticklabels([c+"\nsorter" for c in cols])
axR.set_yticks([2.5,1.5,0.5]); axR.set_yticklabels(["prepared H","prepared D","prepared R"])
axR.xaxis.tick_top(); axR.tick_params(length=0)
axR.set_title("percent of photons at the two exits",fontsize=10,pad=38)
fig.text(0.5,0.02,"Ideal lossless values; real runs match them to a few per cent. Each preparation is a sure bet (dark) at its own sorter\n"
         "and an even bet (light) at the other two: three mutually even-bet sorters.",ha="center",fontsize=9)
fig.savefig(out,dpi=150); print("saved",os.path.abspath(out))
