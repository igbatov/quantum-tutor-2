import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":11})
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","b-opening.png")
p=0.1; lam=np.linspace(0,0.4,801)
fig,(a,b)=plt.subplots(1,2,figsize=(11,4.4))
for N,ls in [(2,"-"),(10,"--"),(100,":")]:
    a.plot(lam,(lam-p)**2+p*(1-p)/N,ls,lw=2,label=f"N = {N}: minimum {p*(1-p)/N:.3g}")
a.axvline(p,color="k",lw=1); a.text(p+0.005,0.065,"lambda = p = 0.1",fontsize=9)
a.set_xlabel("candidate reading lambda (dimensionless)"); a.set_ylabel("squared length of remainder (F_N - lambda) Psi_N")
a.set_title("Shortest remainder at lambda = p, for every N",fontsize=10); a.legend(fontsize=9); a.set_ylim(0,0.13)
Ns=np.logspace(0,4.3,200); b.loglog(Ns,p*(1-p)/Ns,"k-",lw=2)
for N,v in [(2,0.045),(100,0.0009),(1e4,0.000009)]:
    b.plot(N,v,"o",color="k",ms=7); b.annotate(f"N = {int(N)}: {v:g}",xy=(N,v),xytext=(N*1.6,v*1.8),fontsize=9)
b.set_xlabel("number of ions N"); b.set_ylabel("shortest squared length p(1-p)/N")
b.set_title("p = 0.1: it falls as 1/N but is never zero at finite N",fontsize=10)
fig.suptitle("How far Psi_N is from being an eigenvector of the counter (p = 0.1)",fontsize=12)
fig.tight_layout(); fig.savefig(out,dpi=150); print(out)
