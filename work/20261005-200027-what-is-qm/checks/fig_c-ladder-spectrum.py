# Redraw (round 3): bottom strip retitled 'line positions to scale (brightness only suggested)';
# line heights fall steadily with n (computed relative Balmer line power, equal population per state,
# compressed as power**0.35 so faint lines stay visible); lines below 380 nm (UV) drawn grey; 'UV' label on strip.
# Round 2:: strip widened to 360-700 nm so the fainter Balmer lines below 400 nm and the
# series limit at 364.6 nm are visible; ladder shows faint rungs 7, 8, ... crowding toward 0.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.constants import physical_constants as pc
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here,'..','figures','c-ladder-spectrum.png')
plt.rcParams.update({'font.size':11})
Ry = pc['Rydberg constant times hc in eV'][0]/(1+pc['electron-proton mass ratio'][0])
E = {n:-Ry/n**2 for n in range(1,7)}
R_H = pc['Rydberg constant'][0]/(1+pc['electron-proton mass ratio'][0])
bal = {n:1e9/(R_H*(0.25-1/n**2))/1.000277 for n in range(3,40)}   # air wavelengths, nm
lim = 1e9/(R_H*0.25)/1.000277

def wl_rgb(w):
    if w<380: return (0.45,0.3,0.6)
    if w<440: r,g,b=-(w-440)/60,0,1
    elif w<490: r,g,b=0,(w-440)/50,1
    elif w<510: r,g,b=0,1,-(w-510)/20
    elif w<580: r,g,b=(w-510)/70,1,0
    elif w<645: r,g,b=1,-(w-645)/65,0
    else: r,g,b=1,0,0
    f = 0.3+0.7*(w-380)/40 if w<420 else (0.3+0.7*(700-w)/80 if w>620 else 1)
    f=min(max(f,0.45),1); return (r*f,g*f,b*f)

fig = plt.figure(figsize=(11.5,5.2))
ax = fig.add_axes([0.07,0.1,0.42,0.8])
for n,e in E.items(): ax.hlines(e,0,1,color='k',lw=1.6)
for n in range(7,40): ax.hlines(-Ry/n**2,0,1,color='0.6',lw=0.6)
ax.annotate("grey: rungs 7, 8, 9 ...\ncrowd toward 0",xy=(0.97,-0.12),xytext=(1.03,1.0),fontsize=9,color='0.3',
            ha='left',va='center',arrowprops=dict(arrowstyle='->',color='0.4',lw=0.8))
lab_y = {4:-0.95,5:-0.45,6:0.15}
for n in E:
    y = lab_y.get(n,E[n])
    ax.text(1.03,y,"rung 1 (bottom)" if n==1 else f"rung {n}",va='center',fontsize=10)
    if n>=4: ax.plot([1.0,1.025],[E[n],y],color='0.5',lw=0.7)
ax.hlines(0,0,1,color='k',ls='--',lw=1.2); ax.text(0.02,0.3,"electron set free",va='bottom',fontsize=10)
for x0,n in zip([0.1,0.24,0.38,0.52],[3,4,5,6]):
    col = wl_rgb(bal[n])
    ax.annotate('',xy=(x0,E[2]),xytext=(x0,E[n]),arrowprops=dict(arrowstyle='-|>',color=col,lw=2.5,mutation_scale=14))
    ax.text(x0,E[2]-0.45-0.9*(n%2==0),f"{bal[n]:.0f} nm",ha='center',va='top',fontsize=9,color=col,fontweight='bold')
ax.annotate('',xy=(0.82,E[1]),xytext=(0.82,E[2]),arrowprops=dict(arrowstyle='-|>',color='0.5',lw=2.5,mutation_scale=14))
ax.text(0.80,(E[1]+E[2])/2,"ultraviolet\n(invisible)",ha='right',va='center',fontsize=9,color='0.35')
ax.set_xlim(0,1.45); ax.set_ylim(-15,1.8); ax.set_yticks([0,-5,-10,-15])
ax.set_ylabel("energy (electron-volts)"); ax.set_xticks([])
for s in ['top','right','bottom']: ax.spines[s].set_visible(False)
ax.set_title("Hydrogen's energy ladder (to scale)")
# right: spectra, 360-700 nm
x0, x1 = 360, 700
ax1 = fig.add_axes([0.56,0.6,0.41,0.2]); ax2 = fig.add_axes([0.56,0.15,0.41,0.2])
w = np.linspace(380,700,641)
ax1.set_facecolor('k'); ax1.imshow(np.array([[wl_rgb(v) for v in w]]),aspect='auto',extent=[380,700,0,1])
ax1.set_xlim(x0,x1); ax1.set_ylim(0,1); ax1.set_yticks([])
ax1.set_title("classical prediction (schematic): a smooth smear of all colors",fontsize=10.5)
ax2.set_facecolor('k'); ax2.set_xlim(x0,x1); ax2.set_ylim(0,1); ax2.set_yticks([])
import sympy as sp
from sympy.physics.hydrogen import R_nl
from scipy.integrate import quad
rr = sp.symbols('r', positive=True)
def S(n):   # line strength n->2 summed over l (units a0^2)
    tot = 0.0
    for l in range(n):
        for lp in (0,1):
            if abs(l-lp)==1:
                f = sp.lambdify(rr, R_nl(n,l,rr,1)*R_nl(2,lp,rr,1)*rr**3, 'numpy')
                I = quad(f, 0, 6*n**2+60, limit=400)[0]; tot += max(l,lp)*I**2
    return tot
pw = {n:(0.25-1/n**2)**4*S(n) for n in bal}            # relative power, equal population per state
hgt = {n:(pw[n]/pw[3])**0.35 for n in bal}             # compressed: brightness only suggested
print({n:round(hgt[n],3) for n in list(bal)[:8]})
for n,v in bal.items():
    col = wl_rgb(v) if v>=380 else '0.6'
    if n<=6:
        ax2.axvline(v,ymax=hgt[n],color=col,lw=3); ax2.text(v,1.04,{3:"656.3",4:"486.1",5:"434.0",6:"410.2"}[n],ha='center',va='bottom',fontsize=8)
    else:
        ax2.axvline(v,ymax=hgt[n],zorder=3,color=col,lw=max(0.5,1.4-0.15*(n-7)))
ax2.axvline(lim,color='w',ls=':',lw=1)
ax2.text(505,0.62,"\u2190 fainter lines crowd\n    toward 365 nm (UV)",ha='left',va='center',fontsize=9,color='w')
ax2.set_title("hydrogen's lines: positions to scale (brightness only suggested)",fontsize=10.5,pad=22)
for a_ in (ax1,ax2):
    a_.axvspan(x0,380,color='0.75',alpha=0.2,zorder=1)
    a_.set_xticks([400,500,600,700]); a_.set_xlabel("wavelength (nanometers)")
ax1.text(370,0.5,"UV",ha='center',va='center',fontsize=9,color='w')
ax2.text(370,0.93,"UV",ha='center',va='center',fontsize=9,color='w',fontweight='bold')
fig.savefig(out,dpi=150); print(os.path.abspath(out))
