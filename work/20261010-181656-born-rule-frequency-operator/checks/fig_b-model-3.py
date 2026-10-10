import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from math import comb
plt.rcParams.update({"font.size":11})
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","figures","b-model-3.png")
N=20; p=0.1; m=np.arange(N+1); x=m/N
cnt=np.array([comb(N,k) for k in m])/2**N; w=np.array([comb(N,k)*p**k*(1-p)**(N-k) for k in m])
fig,ax=plt.subplots(figsize=(7.5,4.5)); d=0.012
ax.bar(x-d,cnt,width=0.022,color="white",edgecolor="k",hatch="///",label="share of the 2^20 branches (by count)")
ax.bar(x+d,w,width=0.022,color="0.35",label="share of the total weight (squared entries), p = 0.1")
ax.annotate("most branches: fraction 1/2",xy=(0.5,cnt.max()),xytext=(0.58,0.24),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.annotate("most weight: fraction 0.1",xy=(0.1+d,w.max()),xytext=(0.2,0.29),arrowprops=dict(arrowstyle="->"),fontsize=9)
ax.set_xlabel("fraction of ions up recorded in the branch, m/20"); ax.set_ylabel("share (dimensionless)")
ax.set_title("Many-worlds, N = 20 ions, p = 0.1: counting branches vs weighing them",fontsize=10)
ax.set_ylim(0,0.32); ax.legend(fontsize=9,loc="upper right"); fig.tight_layout(); fig.savefig(out,dpi=150); print(out)
