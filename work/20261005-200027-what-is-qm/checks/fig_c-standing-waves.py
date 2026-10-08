import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here,'..','figures','c-standing-waves.png')
plt.rcParams.update({'font.size':12})
x = np.linspace(0,1,600)
rows = [(1,"1 hump: fits (lowest note)",'k'),(2,"2 humps: fits (higher note)",'k'),
        (3,"3 humps: fits (higher still)",'k'),(2.5,"2.5 humps: misses the pinned end, can't ring steadily",'red')]
fig, axes = plt.subplots(4,1,figsize=(7,6),sharex=True)
for ax,(n,lab,col) in zip(axes,rows):
    y = np.sin(n*np.pi*x)
    ax.plot(x,y,color=col if col=='red' else '0.1',lw=2.2)
    if col=='k': ax.plot(x,-y,color='0.6',lw=1.2,ls='--')
    ax.plot([0,1],[0,0],'o',color='k',ms=8,zorder=5)
    if col=='red':
        ax.plot(1,1,marker='x',color='red',ms=14,mew=3,zorder=6)
    ax.text(0.5,1.25,lab,ha='center',va='bottom',fontsize=11,color='red' if col=='red' else 'k',
            fontweight='bold' if col=='red' else 'normal')
    ax.set_ylim(-1.3,1.9); ax.set_xlim(-0.05,1.08); ax.axis('off')
fig.suptitle("Only whole numbers of humps fit between pinned ends",fontsize=13)
fig.tight_layout(rect=[0,0,1,0.96]); fig.savefig(out,dpi=150); print(os.path.abspath(out))
