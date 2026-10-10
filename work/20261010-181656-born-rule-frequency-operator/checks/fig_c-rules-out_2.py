import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10})
OUT='/home/user/quantum-tutor-2/work/20261010-181656-born-rule-frequency-operator/figures/c-rules-out.png'
N=np.arange(1,10001); sd=np.sqrt(0.16/N)
fig,axs=plt.subplots(3,1,figsize=(7,6.5),sharex=True)
axs[0].semilogx(N,np.full_like(N,0.8,dtype=float),'k-',lw=1.5)
axs[0].text(3,0.9,'(i) classical continuous wave: share in R is 0.8 at every moment — "no dots to count"',fontsize=9)
for ax,seed,lab in [(axs[1],11,'(ii) tickets: destination "in" pre-set at the source with chance 0.8'),
                    (axs[2],29,'(iii) squared-amplitude rule: each arrival in R with chance 0.8')]:
    f=np.cumsum(np.random.default_rng(seed).random(10000)<0.8)/N
    ax.semilogx(N,f,'k-',lw=0.9,drawstyle='steps-post',label='running fraction (one simulated run)')
    ax.semilogx(N,0.8+sd,'b--',lw=1,label='0.8 ± √(0.16/N) (±1 s.d.)'); ax.semilogx(N,0.8-sd,'b--',lw=1)
    ax.semilogx(N,0.8+2*sd,'g:',lw=1.3,label='0.8 ± 2√(0.16/N) (±2 s.d.)'); ax.semilogx(N,0.8-2*sd,'g:',lw=1.3)
    ax.axhline(0.8,color='C3',lw=0.8)
    ax.text(3,1.06,lab,fontsize=9); ax.legend(fontsize=8,loc='lower right')
for ax in axs: ax.set_ylim(0.3,1.15); ax.set_ylabel("fraction in R")
axs[2].set_xlabel("number of electrons N (log scale)"); axs[2].set_xlim(1,10000)
fig.tight_layout(); fig.savefig(OUT,dpi=150); print("saved",OUT)
