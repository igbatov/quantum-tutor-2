import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from _style import plt, save
import numpy as np
fig,(a1,a2)=plt.subplots(1,2,figsize=(7.5,4))
th=np.linspace(0,90,300)
a1.plot(th,np.cos(np.radians(th))**2,"-",color="k",label="T: cos²θ")
a1.plot(th,np.sin(np.radians(th))**2,"--",color="k",label="R: sin²θ")
a1.axvline(30,color="gray",lw=0.8); a1.plot([30,30],[0.75,0.25],"o",color="k")
a1.text(32,0.78,"0.75",fontsize=10); a1.text(32,0.18,"0.25",fontsize=10)
a1.set_xlabel("polarizer angle θ (degrees)"); a1.set_ylabel("fraction of photons"); a1.set_title("Malus's law (ideal optics)"); a1.legend(fontsize=9)
rng=np.random.default_rng(3); p=0.25; Nmax=10000; N=np.arange(1,Nmax+1)
for k,ls in zip(range(5),["-","--","-.",":","-"]):
    r=np.cumsum(rng.random(Nmax)<p)/N; a2.plot(N,r,ls,lw=0.9,color=str(0.1+0.15*k))
s=np.sqrt(p*(1-p)/N); a2.plot(N,p+s,color="k",lw=2); a2.plot(N,p-s,color="k",lw=2)
a2.axhline(p,color="gray",lw=0.8)
a2.set_xscale("log"); a2.set_ylim(0,0.75); a2.set_xlabel("photons counted N"); a2.set_ylabel("reflected fraction so far")
a2.set_title("5 simulated runs, p = 0.25\nthick: 0.25 ± √(p(1−p)/N)",fontsize=11)
fig.tight_layout(); save(fig,"a-experiment-1")
