import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, itertools, math
plt.rcParams.update({'font.size':9})
OUT='/home/user/quantum-tutor-2/work/20261010-181656-born-rule-frequency-operator/figures/c-branch-tree.png'
c0,c1=math.sqrt(.2),math.sqrt(.8)
fig=plt.figure(figsize=(9,6.5)); ax=fig.add_axes([0.02,0.36,0.96,0.62]); ax.axis('off')
pos={(): (0.5,3)}
def amp(s): return np.prod([c1 if b else c0 for b in s]) if s else 1.0
for d in range(1,4):
    for s in itertools.product([0,1],repeat=d):
        idx=int(''.join(map(str,s)),2); pos[s]=((idx+0.5)/2**d,3-d)
for s,(x,y) in pos.items():
    if len(s)<3:
        for b in [0,1]:
            t=s+(b,); x2,y2=pos[t]; ax.plot([x,x2],[y,y2],'k-' if b else 'k--',lw=1)
            ax.text((x+x2)/2+(0.012 if b else -0.012),(y+y2)/2,f"{'in' if b else 'out'}\n×{c1 if b else c0:.3f}",ha='left' if b else 'right',fontsize=7.5)
    a=amp(s); ax.plot(x,y,'o',ms=5,color='k')
    if 0<len(s)<3: ax.text(x,y+0.12,f"{a:.3f}",ha='center',fontsize=8)
    elif len(s)==3:
        m=sum(s); ax.text(x,y-0.12,"\n".join('in' if b else 'out' for b in s)+f"\namp {a:.3f}\nweight {a*a:.3f}",ha='center',va='top',fontsize=8)
ax.text(0.5,3.12,"root, amplitude 1.000",ha='center'); ax.set_ylim(-1.6,3.45); ax.set_xlim(0,1)
ax.text(0.0,2.0,"solid = in (×0.894)\ndashed = out (×0.447)",fontsize=8)
ax2=fig.add_axes([0.25,0.08,0.5,0.24])
fr=np.array([0,1,2,3])/3; gw=[math.comb(3,m)*.8**m*.2**(3-m) for m in range(4)]
ax2.bar(fr,gw,width=0.12,color='0.6',edgecolor='k',hatch='//')
for f,g in zip(fr,gw): ax2.text(f,g+0.02,f"{g:.3f}",ha='center')
ax2.axvline(0.8,ls='--',color='k'); ax2.text(0.79,0.58,"0.8: not an available reading",fontsize=8,ha="right")
ax2.set_xticks(fr); ax2.set_xticklabels(['0','1/3','2/3','1']); ax2.set_ylim(0,0.66)
ax2.set_xlabel("frequency m/3"); ax2.set_ylabel("group weight"); ax2.set_title("8 branches, weights total 1",fontsize=9)
fig.savefig(OUT,dpi=150,bbox_inches='tight'); print("saved",OUT,"sum",sum(gw))
