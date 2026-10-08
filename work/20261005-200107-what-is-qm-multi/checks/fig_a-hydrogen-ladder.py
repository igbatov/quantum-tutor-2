import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "figures", "a-hydrogen-ladder.png")
RH = 1.0968e7
E = lambda n: -13.6/n**2
lam = {n: 1e9/(RH*(0.25-1/n**2)) for n in (3,4,5,6)}
plt.rcParams.update({"font.size": 10})
fig, (axL, axR) = plt.subplots(1, 2, figsize=(7.5, 4.2), gridspec_kw={"width_ratios":[1,1.25]})
# LEFT: ladder
for n in range(1,7):
    axL.hlines(E(n), 0, 1, color="k", lw=1.5)
    lbl = "rung 1 (lowest)" if n==1 else f"rung {n}"
    y = E(n)
    if n >= 3: y = {3:-1.75, 4:-0.95, 5:-0.25, 6:0.45}[n]  # spread crowded labels
    axL.text(1.03, y, lbl, va="center", fontsize=8)
    if n>=3: axL.plot([1,1.02],[E(n),y],color="0.5",lw=0.6)
axL.hlines(0, 0, 1, color="k", ls="--", lw=1)
axL.text(0.5, 0.35, "electron no longer bound", ha="center", fontsize=8)
xs = {3:0.15, 4:0.37, 5:0.59, 6:0.81}
cols = {3:"#d00000", 4:"#00a0b0", 5:"#2040ff", 6:"#7a00c0"}
for n,x in xs.items():
    axL.annotate("", xy=(x, E(2)), xytext=(x, E(n)),
                 arrowprops=dict(arrowstyle="-|>", color=cols[n], lw=1.6))
    axL.text(x, E(2)-(0.35 if n in (3,5) else 1.25), f"{lam[n]:.0f} nm", ha="center", va="top", fontsize=8.5)
    if n in (4,6): axL.vlines(x, E(2)-1.25, E(2)-0.1, color="0.6", lw=0.6)
axL.set_xlim(0, 1.45); axL.set_ylim(-14.5, 1)
axL.set_xticks([]); axL.set_ylabel("Energy (eV)")
for s in ("top","right","bottom"): axL.spines[s].set_visible(False)
axL.set_title("Hydrogen's energy ladder", fontsize=10)
# RIGHT: spectra
w = np.linspace(380, 700, 600)
def wl_rgb(l):
    hue = np.interp(l, [380,440,490,510,580,645,700],[0.78,0.67,0.5,0.33,0.16,0.0,0.0])
    return hsv_to_rgb([hue,1,1])
rain = np.array([[wl_rgb(l) for l in w]])
axR.imshow(rain, extent=[380,700,1.15,2.0], aspect="auto")
axR.text(540, 2.05, "continuous spectrum, e.g. a hot glowing filament\n(for comparison)", ha="center", va="bottom", fontsize=8)
axR.add_patch(plt.Rectangle((380,0),320,0.85,color="k"))
for n,l in lam.items():
    axR.vlines(l, 0, 0.85, color=wl_rgb(l), lw=2.2)
    axR.text(l, -0.08, f"{l:.0f} nm ({n}→2)", rotation=90, ha="center", va="top", fontsize=7.5)
axR.text(540, 0.92, "hydrogen: four sharp lines, nothing in between", ha="center", va="bottom", fontsize=8)
axR.set_xlim(380,700); axR.set_ylim(-1.3, 2.6)
axR.set_yticks([]); axR.set_xlabel("Wavelength (nm)")
for s in ("top","right","left"): axR.spines[s].set_visible(False)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT))
