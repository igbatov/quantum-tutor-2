import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.stats import binom
plt.rcParams.update({'font.size':10})
OUT='/home/user/quantum-tutor-2/work/20261010-181656-born-rule-frequency-operator/figures/c-born-spread.png'
fig,(a1,a2)=plt.subplots(1,2,figsize=(11,4.3))
m=np.arange(60,101); a1.bar(m,binom.pmf(m,100,0.8),color='0.6',edgecolor='k',width=0.8)
a1.axvline(80,color='k',lw=1.5,label='mean 80'); a1.axvline(76,color='k',ls='--',lw=1,label='mean ± 1 s.d. (4)'); a1.axvline(84,color='k',ls='--',lw=1)
a1.annotate('',xy=(84,0.105),xytext=(80,0.105),arrowprops=dict(arrowstyle='<->')); a1.text(82,0.108,'4',ha='center')
a1.set_xlabel("count m of electrons in R (N = 100)"); a1.set_ylabel("probability"); a1.legend(fontsize=8); a1.set_ylim(0,0.12)
N=np.arange(10,100001)
def within(N,num,den):
    lo=-((-N*(4*den-5*num))//(5*den)); hi=(N*(4*den+5*num))//(5*den)
    return binom.cdf(hi,N,0.8)-binom.cdf(lo-1,N,0.8)
a2.semilogx(N,within(N,1,20),'k-',lw=0.7,label='within 0.05 of 0.8')
a2.semilogx(N,within(N,1,100),color='C3',ls='-',lw=0.5,alpha=0.8,label='within 0.01 of 0.8')
a2.set_xlabel("N (log)"); a2.set_ylabel("chance that m/N is within ε of 0.8"); a2.set_xlim(10,1e5); a2.set_ylim(-0.02,1.02)
a2.legend(fontsize=8,loc='center right'); a2.set_title("Jagged at small N: only some m/N fall in the window",fontsize=9)
fig.tight_layout(); fig.savefig(OUT,dpi=150); print("saved",OUT)
print("eps=0.01 N=11..14:",within(np.arange(11,15),1,100))
