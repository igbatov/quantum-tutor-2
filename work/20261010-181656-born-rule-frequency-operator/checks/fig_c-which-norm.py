import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt, math
plt.rcParams.update({'font.size':10})
OUT='/home/user/quantum-tutor-2/work/20261010-181656-born-rule-frequency-operator/figures/c-which-norm.png'
c0,c1=math.sqrt(.2),math.sqrt(.8)
fig,(a1,a2)=plt.subplots(1,2,figsize=(11,4.3))
q=np.linspace(0.5,4,300); a1.plot(q,2**q/(1+2**q),'k-',lw=1.5,label='f_q = 2^q/(1+2^q)')
qs=np.array([1,2,3,4]); fq=2.0**qs/(1+2.0**qs); a1.plot(qs,fq,'ko',ms=6)
for x,y,t in zip(qs,fq,['2/3','4/5','8/9','16/17']): a1.text(x+0.06,y-0.03,t)
a1.set_xlim(0.4,4.5); a1.axhline(0.8,ls='--',color='C3',label='0.8 = |c1|²'); a1.set_xlabel("norm exponent q"); a1.set_ylabel("dominant frequency f_q")
a1.legend(fontsize=8,loc='lower right'); a1.set_title("Only q = 2 returns 0.8",fontsize=10)
m=np.arange(21)
for q,(col,h,off) in zip([1,2,4],[('C0','',-0.012),('C3','//',0),('C2','..',0.012)]):
    v=np.array([math.comb(20,k)*c0**(q*(20-k))*c1**(q*k) for k in m]); v/=v.sum()
    a2.bar(m/20+off,v,width=0.012,color=col,hatch=h,edgecolor='k',lw=0.3,label=f"q = {q} (peak m = {', '.join(str(k) for k in m[np.isclose(v,v.max())])})")
a2.set_xlabel("frequency m/20"); a2.set_ylabel("normalized q-weight"); a2.legend(fontsize=8,loc='upper left')
a2.set_title("N = 20: peaks at m = 13–14, 16, 19",fontsize=10)
fig.tight_layout(); fig.savefig(OUT,dpi=150); print("saved",OUT)
