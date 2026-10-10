import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.stats import binom
plt.rcParams.update({'font.size':10})
OUT='/home/user/quantum-tutor-2/work/20261010-181656-born-rule-frequency-operator/figures/c-parabola-floor.png'
fig,(a1,a2)=plt.subplots(1,2,figsize=(11,4.3))
lam=np.linspace(0,1,400); styles=['-','--','-.',':',(0,(5,1,1,1))]
for N,ls in zip([1,2,8,32,128],styles):
    a1.plot(lam,(lam-0.8)**2+0.16/N,ls=ls,color='k',lw=1.3,label=f"N={N}, floor {0.16/N:g}")
a1.axvline(0.8,ls='--',color='C3',lw=1); a1.set_xlabel("reading λ"); a1.set_ylabel("squared length of (F_N − λ)Ψ_N")
a1.legend(fontsize=8,loc='lower left');
ins=a1.inset_axes([0.62,0.55,0.35,0.33])
for N,ls in zip([1,2,8,32,128],styles): ins.plot(lam,(lam-0.8)**2+0.16/N,ls=ls,color='k',lw=1)
ins.set_xlim(0.6,1); ins.set_ylim(0,0.1); ins.axvline(0.8,ls='--',color='C3',lw=0.8); ins.set_title('zoom near the floor',fontsize=7); ins.tick_params(labelsize=7)
a1.set_title("Parabolas bottom out at λ = 0.8, floor 0.16/N > 0",fontsize=10)
N=np.arange(10,100001)
def dev(N,num,den):  # eps=num/den with p=4/5: deviant if m < N(4/5-eps) or m > N(4/5+eps)
    hi_num=4*den+5*num; lo_num=4*den-5*num   # N*(p±eps) = N*hi_num/(5*den)
    hi=(N*hi_num)//(5*den)                    # m > N(p+eps)  <=> m >= hi+1
    lo=-((-N*lo_num)//(5*den))                # ceil(N(p-eps)); m < that
    return binom.cdf(lo-1,N,0.8)+binom.sf(hi,N,0.8)
a2.loglog(N,0.16/N,'k-',lw=1.5,label="floor 0.16/N")
for (num,den),ls in [((1,10),'-'),((1,20),'--')]:
    eps=num/den
    a2.loglog(N,np.minimum(1,0.16/(N*eps**2)),color='C0',ls=ls,lw=1.3,label=f"Chebyshev bound, ε={eps:g}")
    d=dev(N,num,den); a2.loglog(N,np.where(d>0,d,np.nan),color='C3',ls=ls,lw=1.0,label=f"exact deviant squared length, ε={eps:g}")
a2.set_ylim(1e-12,1.5); a2.set_xlim(10,1e5); a2.set_xlabel("N (log)"); a2.set_ylabel("squared length (log)")
a2.legend(fontsize=7.5,loc='lower left'); a2.set_title("Exact deviant part falls far faster than the bound",fontsize=10)
fig.tight_layout(); fig.savefig(OUT,dpi=150); print("saved",OUT)
print("check N=1000 eps=0.05:",dev(np.array([1000]),1,20))
