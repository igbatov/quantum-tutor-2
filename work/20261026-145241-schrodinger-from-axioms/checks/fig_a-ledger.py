# Ledger diagram: assumptions -> theorems -> Schrodinger equation (structure of candidate-A §3-5)
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
D="/home/user/quantum-tutor-2/work/20261026-145241-schrodinger-from-axioms/figures/"
plt.rcParams.update({"font.size":10})
fig,ax=plt.subplots(figsize=(10,5)); ax.axis("off"); ax.set_xlim(0,10); ax.set_ylim(0,6)
A=dict(boxstyle="round,pad=0.35",fc="white",ec="k",ls="--")      # assumption: dashed
T=dict(boxstyle="round,pad=0.35",fc="#e8e8e8",ec="k",lw=1.5)     # theorem: grey, solid
S=dict(boxstyle="round,pad=0.45",fc="#d0d0d0",ec="k",lw=2.5)     # result: thick
def box(x,y,txt,st): ax.text(x,y,txt,ha="center",va="center",bbox=st)
def arr(p,q): ax.annotate("",xy=q,xytext=p,arrowprops=dict(arrowstyle="->",lw=1.3))
ax.text(1.3,5.7,"ASSUMPTIONS (dashed)",ha="center",weight="bold")
ax.text(5.0,5.7,"THEOREMS (grey)",ha="center",weight="bold")
ax.text(8.6,5.7,"RESULT",ha="center",weight="bold")
box(1.3,4.9,"(L) linearity\n(U) unitarity",A); box(1.3,3.9,"(C) composition +\ntime-translation, (K) continuity",A)
box(1.3,2.75,"(G) Galilean invariance\n+ de Broglie $p=\\hbar k$\n+ $p'=p-mv$",A)
box(1.3,1.55,"$c=0$: rest-frame choice\n$p=-i\\hbar\\partial_x$: definition",A)
box(1.3,0.55,"locality: real $V(x)$",A)
box(5.0,4.4,"Stone: $U(t)=e^{-iHt/\\hbar}$\n$H$ Hermitian (Step 2)\n$\\Rightarrow i\\hbar\\,\\partial_t\\psi=H\\psi$",T)
box(5.0,2.75,"lemma: boost = phase × relabel\nSteps 4–5: $\\omega=\\hbar k^2/2m$",T)
box(5.0,1.3,"$H_{free}=p^2/2m$\n$=-(\\hbar^2/2m)\\,\\partial_x^2$",T)
box(8.6,3.0,"$i\\hbar\\,\\partial_t\\psi=$\n$-\\frac{\\hbar^2}{2m}\\partial_x^2\\psi+V\\psi$",S)
for p,q in [((2.45,4.9),(3.5,4.55)),((2.95,3.9),(3.5,4.2)),((2.65,2.75),(3.35,2.75)),
            ((5.0,2.3),(5.0,1.75)),((2.75,1.55),(3.95,1.35)),((6.55,4.3),(7.6,3.3)),
            ((6.2,1.3),(7.6,2.7))]: arr(p,q)
ax.annotate('',xy=(8.6,2.45),xytext=(2.3,0.55),arrowprops=dict(arrowstyle='->',lw=1.3,connectionstyle='angle,angleA=0,angleB=90,rad=0'))
ax.text(5.0,0.15,"heuristic: $U$ assumed differentiable (Stone's technical step not proved)",ha="center",fontsize=8.5,style="italic")
fig.tight_layout(); fig.savefig(D+"a-ledger.png",dpi=150); print("ok")
