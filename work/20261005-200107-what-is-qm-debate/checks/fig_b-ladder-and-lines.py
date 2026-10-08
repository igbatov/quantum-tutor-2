# Figure b-ladder-and-lines: hydrogen energy ladder (left) and emission spectrum vs classical smear (right).
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
from scipy import constants as C

RUN = "/Users/igbatov/Claude/quantum-tutor 2/work/20261005-200107-what-is-qm-debate"
Ry_eV = C.physical_constants['Rydberg constant times hc in eV'][0] * C.m_p/(C.m_e+C.m_p)
E = {n: -Ry_eV/n**2 for n in range(1, 7)}
def lam_air(nu, nl):
    lv = C.h*C.c/((E[nu]-E[nl])*C.e)*1e9
    return lv/1.000277 if lv > 200 else lv

def wl_to_rgb(w):
    # simple visible-wavelength to RGB approximation
    if w < 380 or w > 750: return (0.5, 0.5, 0.5)
    if w < 440: r, g, b = -(w-440)/60, 0.0, 1.0
    elif w < 490: r, g, b = 0.0, (w-440)/50, 1.0
    elif w < 510: r, g, b = 0.0, 1.0, -(w-510)/20
    elif w < 580: r, g, b = (w-510)/70, 1.0, 0.0
    elif w < 645: r, g, b = 1.0, -(w-645)/65, 0.0
    else: r, g, b = 1.0, 0.0, 0.0
    f = 1.0 if 420 <= w <= 700 else (0.3+0.7*(w-380)/40 if w < 420 else 0.3+0.7*(750-w)/50)
    return (r*f, g*f, b*f)

plt.rcParams.update({"font.size": 10})
fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.8), gridspec_kw={"width_ratios": [1.15, 1]})

# LEFT: ladder
xmin, xmax = 0.0, 1.0
for n, En in E.items():
    axL.hlines(En, xmin, xmax, color="black", lw=1.6)
for n in (1, 2, 3):
    axL.text(xmax+0.02, E[n], f"rung {n}  ({E[n]:.2f} eV)", va="center", fontsize=9)
axL.text(xmax+0.02, E[1]-0.75, "lowest rung: nothing below it", va="center", fontsize=9, style="italic")
# bracket for rungs 4-6
ytop, ybot = E[6], E[4]
axL.plot([xmax+0.03, xmax+0.06, xmax+0.06, xmax+0.03], [ytop, ytop, ybot, ybot], color="black", lw=1)
axL.text(xmax+0.08, (ytop+ybot)/2+0.25, "rungs 4-6: higher rungs\ncrowd together near 0", va="center", fontsize=8.5)

xs = {3: 0.22, 4: 0.40, 5: 0.58, 6: 0.76}
for nu, x in xs.items():
    w = lam_air(nu, 2)
    col = wl_to_rgb(w)
    axL.annotate("", xy=(x, E[2]), xytext=(x, E[nu]),
                 arrowprops=dict(arrowstyle="-|>", color=col, lw=2.4, mutation_scale=14))
    name = {3: "red", 4: "blue-green", 5: "blue", 6: "violet"}[nu]
    axL.text(x, E[2]-0.25, f"{w:.0f} nm\n{name}", ha="center", va="top", fontsize=8.5, color="black")
# Lyman alpha
xL = 0.08
axL.annotate("", xy=(xL, E[1]), xytext=(xL, E[2]),
             arrowprops=dict(arrowstyle="-|>", color="grey", lw=1.8, ls="--", mutation_scale=14))
axL.text(xL+0.03, (E[1]+E[2])/2 - 1.5, f"{lam_air(2,1):.0f} nm: ultraviolet, invisible", va="center", fontsize=9, color="dimgray")

axL.set_xlim(0, 1.75); axL.set_ylim(-14.5, 0.3)
axL.set_xticks([]); axL.set_ylabel("energy (eV)")
axL.axhline(0, color="lightgray", lw=0.8, ls=":")
axL.set_title("hydrogen's energy ladder")
for s in ("top", "right", "bottom"): axL.spines[s].set_visible(False)

# RIGHT: spectra
wl = np.linspace(400, 700, 600)
rainbow = np.array([wl_to_rgb(w) for w in wl])[None, :, :]
axR.imshow(rainbow, extent=[400, 700, 1.15, 2.0], aspect="auto")
axR.add_patch(plt.Rectangle((400, 0.0), 300, 0.85, color="black"))
for nu in (3, 4, 5, 6):
    w = lam_air(nu, 2)
    axR.vlines(w, 0.0, 0.85, color=wl_to_rgb(w), lw=3)
    axR.text(w, -0.08, f"{w:.0f}", ha="center", va="top", fontsize=8.5)
axR.text(550, 2.08, "classical expectation: a smear of all colours", ha="center", va="bottom", fontsize=9.5)
axR.text(550, 0.93, "what hydrogen actually emits", ha="center", va="bottom", fontsize=9.5)
axR.set_xlim(400, 700); axR.set_ylim(-0.45, 2.45)
axR.set_yticks([]); axR.set_xlabel("wavelength (nm)")
for s in ("top", "right", "left"): axR.spines[s].set_visible(False)
axR.set_title("hydrogen's visible light")

fig.tight_layout()
out = f"{RUN}/figures/b-ladder-and-lines.png"
fig.savefig(out, dpi=150)
print("saved", out)
