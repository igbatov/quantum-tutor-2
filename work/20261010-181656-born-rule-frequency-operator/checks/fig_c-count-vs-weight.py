import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, math
from scipy.stats import binom
plt.rcParams.update({'font.size':10})
OUT='/home/user/quantum-tutor-2/work/20261010-181656-born-rule-frequency-operator/figures/c-count-vs-weight.png'
m=np.arange(21); f=m/20; cnt=np.array([math.comb(20,k) for k in m])/2**20; w=binom.pmf(m,20,0.8)
fig,axs=plt.subplots(2,1,figsize=(7,5.5),sharex=True)
for ax,y,lab,line,tot in [(axs[0],cnt,"share of branches by number\nC(20,m)/2^20",0.5,cnt[:11].sum()),(axs[1],w,"branch weight\nC(20,m) 0.8^m 0.2^(20-m)",0.8,w[:11].sum())]:
    sh=m<=10
    ax.bar(f[sh],y[sh],width=0.04,color='0.55',edgecolor='k',hatch='//',label='m ≤ 10 (frequency ≤ 1/2)')
    ax.bar(f[~sh],y[~sh],width=0.04,color='white',edgecolor='k',label='m > 10')
    ax.axvline(line,ls='--',color='k'); ax.set_ylabel(lab,fontsize=9)
    ax.text(0.02,(0.45 if line==0.8 else 0.8)*y.max(),f"shaded total = {tot:.4f}",fontsize=10)
    ax.legend(fontsize=8,loc='upper left' if line==0.8 else 'upper right')
axs[0].set_title("N = 20, p = 0.8: counting branches vs weighting them",fontsize=10)
axs[1].annotate('shaded bars m ≤ 10 are too small to see\n(largest: m = 10, weight 0.0020)',xy=(0.5,0.003),xytext=(0.12,0.04),fontsize=8,arrowprops=dict(arrowstyle='->'))
axs[1].set_xlabel("frequency m/20")
fig.tight_layout(); fig.savefig(OUT,dpi=150); print("saved",OUT,cnt[:11].sum(),w[:11].sum())
