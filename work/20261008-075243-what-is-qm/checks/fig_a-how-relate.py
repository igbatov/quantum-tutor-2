# Figure a-how-relate (schematic map, no computed data): one theory in two forms (wave function <-> sum
# over paths, same predictions); three interpretations as readings of it (no experiment tells them apart);
# objective collapse as a slightly different theory (tiny departures growing with mass; not found so far).
import os, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-how-relate.png')
plt.rcParams.update({'font.size': 11})
fig, ax = plt.subplots(figsize=(11.5, 5.8))
ax.set_xlim(0, 11.5); ax.set_ylim(0.35, 6.1); ax.axis('off')

def rbox(x, y, w, h, ec='k', fc='white', ls='-', lw=1.3, r=0.15):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={r}', ec=ec, fc=fc, ls=ls, lw=lw))
def arrow(a, b, style='-|>', ls='-', color='k', lw=1.3, cs='arc3'):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=15, ls=ls, color=color, lw=lw, connectionstyle=cs))

# --- one theory (top) ---
rbox(0.3, 3.75, 7.0, 2.2, fc='0.95', lw=1.6)
ax.text(3.8, 5.62, "ONE THEORY: standard quantum mechanics", ha='center', fontsize=12, weight='bold')
rbox(0.6, 4.0, 2.6, 1.25)
ax.text(1.9, 4.62, "wave function\n(Schrödinger\nequation)", ha='center', va='center', fontsize=10.5)
rbox(4.4, 4.0, 2.6, 1.25)
ax.text(5.7, 4.62, "sum over paths\n(Feynman, 1948)", ha='center', va='center', fontsize=10.5)
arrow((3.25, 4.62), (4.35, 4.62), style='<|-|>', lw=1.6)
ax.text(3.8, 4.82, "same\npredictions,\nalways", ha='center', va='bottom', fontsize=8.8)

# --- three readings (bottom left) ---
names = ["Copenhagen-\nstyle", "many-worlds", "pilot-wave"]
xs = [0.45, 2.75, 5.05]
for x, n in zip(xs, names):
    rbox(x, 1.45, 2.0, 0.95)
    ax.text(x+1.0, 1.92, n, ha='center', va='center', fontsize=10.5)
    arrow((x+1.0, 3.72), (x+1.0, 2.45), color='0.3')
ax.text(3.8, 3.05, "three readings of the same theory", ha='center', va='center', fontsize=10,
        bbox=dict(fc='white', ec='none', pad=1.5))
ax.plot([0.45, 0.45, 7.05, 7.05], [1.3, 1.15, 1.15, 1.3], color='k', lw=1.1)
ax.text(3.75, 1.0, "they agree on every prediction: no experiment has ever told them apart;\n"
                   "the choice is taste and economy, and the question is open", ha='center', va='top', fontsize=9.8)

# --- objective collapse (right) ---
rbox(8.6, 2.55, 2.75, 3.4, ls='--', lw=1.5)
ax.text(9.975, 5.55, "objective\ncollapse", ha='center', va='center', fontsize=11.5, weight='bold')
ax.text(9.975, 4.68, "a slightly different\ntheory: adds random\nlocalization", ha='center', va='center', fontsize=9.8)
ax.text(9.975, 3.42, "tiny departures,\ngrowing with the amount\nof matter involved;\nsearched for, not\nfound so far", ha='center', va='center', fontsize=9.3)
arrow((7.35, 4.85), (8.55, 4.85), ls='--', color='0.3')
ax.text(7.95, 5.0, "changes the\nequation slightly", ha='center', va='bottom', fontsize=8.3)
ax.text(9.975, 2.3, "one electron: far too\nsmall to see", ha='center', va='top', fontsize=9.3, style='italic')

fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
