# Figure c-square-of-a-sum: (a+b+c)^2 as a 3x3 grid; (a+b+c)^3 as three horizontal layers.
import os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.gridspec import GridSpec
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, '..', 'figures', 'c-square-of-a-sum.png')
a,b,c = 3,2,1
sides = [a,b,c]; names = ['a','b','c']
edges = np.cumsum([0]+sides)
plt.rcParams.update({'font.size': 11})
box = dict(facecolor='white', edgecolor='none', alpha=0.85, pad=1.5)
fig = plt.figure(figsize=(13,5.8))
gs = GridSpec(2, 4, figure=fig, width_ratios=[2.3,1,1,1], height_ratios=[1,0.12], wspace=0.15)
ax = fig.add_subplot(gs[0,0])
total = 0
for i in range(3):
    for j in range(3):
        w, h = sides[j], sides[i]; total += w*h
        diag = (i==j)
        ax.add_patch(Rectangle((edges[j], 6-edges[i]-h), w, h,
                     facecolor='#f4b183' if diag else '#9dc3e6',
                     hatch='' if diag else '//', edgecolor='k', lw=1))
        lab = f"{names[i]}·{names[j]} = {sides[i]*sides[j]}"
        ax.text(edges[j]+w/2, 6-edges[i]-h/2, lab, ha='center', va='center',
                fontsize=11 if w*h>2 else 8, bbox=box)
assert total == 36
ax.add_patch(Rectangle((0, 6-(a+b)), a+b, a+b, fill=False, lw=3.5, edgecolor='k', ls='--'))
ax.text((a+b)/2, 6.12, 'dashed outline: what the pair A+B alone gives', ha='center', va='bottom', fontsize=10)
for k,(e,s) in enumerate(zip(edges[:-1],sides)):
    ax.text(e+s/2, -0.2, names[k]+f" = {s}", ha='center', va='top')
    ax.text(-0.2, 6-e-s/2, names[k]+f" = {s}", ha='right', va='center')
ax.set_xlim(-1.1,6.2); ax.set_ylim(-0.8,6.7); ax.set_aspect('equal'); ax.axis('off')
ax.set_title("Square rule: chance = (a + b + c)², area 36", fontsize=12.5)
lax = fig.add_subplot(gs[1,0]); lax.axis('off')
lax.legend(handles=[Patch(facecolor='#f4b183', edgecolor='k', label='single-slit pieces (diagonal): 9 + 4 + 1'),
                    Patch(facecolor='#9dc3e6', hatch='//', edgecolor='k', label='pair pieces (rectangles): 2 × (6 + 3 + 2)')],
           loc='center', fontsize=10, frameon=False, ncol=1)

vol = 0; n_abc = 0
for L in range(3):     # layer of thickness sides[L]
    axl = fig.add_subplot(gs[0,1+L])
    for i in range(3):
        for j in range(3):
            w, h = sides[j], sides[i]
            v = w*h*sides[L]; vol += v
            three = len({i,j,L})==3
            if three: n_abc += 1
            axl.add_patch(Rectangle((edges[j], 6-edges[i]-h), w, h,
                          facecolor='#c00000' if three else '#eeeeee',
                          hatch='' if three else '', edgecolor='k', lw=1.6 if three else 0.6))
            if three:
                axl.text(edges[j]+w/2, 6-edges[i]-h/2, "a·b·c\n= 6", ha='center', va='center',
                         color='white', fontsize=9 if w*h>2 else 7, fontweight='bold')
    for k,(e,s) in enumerate(zip(edges[:-1],sides)):
        axl.text(e+s/2, -0.15, names[k], ha='center', va='top', fontsize=10)
        axl.text(-0.15, 6-e-s/2, names[k], ha='right', va='center', fontsize=10)
    axl.set_xlim(-0.8,6.1); axl.set_ylim(-0.8,6.3); axl.set_aspect('equal'); axl.axis('off')
    axl.set_title(f"layer of thickness {names[L]} = {sides[L]}", fontsize=10.5)
assert vol == 216 and n_abc == 6
fig.text(0.715, 0.93, "Cube rule: chance = (a + b + c)³, volume 216 (cube cut into three horizontal layers)",
         ha='center', fontsize=12.5)
tax = fig.add_subplot(gs[1,1:]); tax.axis('off')
tax.text(0.5, 0.5, "dark boxes: the six pieces involving all three slits at once, a·b·c = 6 each "
         "(36 of the 216 unit cubes);\nno single-slit or pair run contains them, so none can measure them",
         ha='center', va='center', fontsize=10.5)
fig.subplots_adjust(left=0.03, right=0.99, top=0.88, bottom=0.04)
fig.savefig(out, dpi=150)
print("saved", os.path.abspath(out))
