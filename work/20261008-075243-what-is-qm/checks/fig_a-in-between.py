# Figure a-in-between (section "What happens in between?"): schematic of the record argument.
# Numbers used (same relative units as the text's Model 1 example, at a spot that is dark with both slits):
#   amplitude via left slit = +1, via right slit = -1.
#   No record:  same final situation -> amplitudes add: (+1) + (-1) = 0 -> chance 0.
#   Perfect record: different final situations -> chances add: |+1|^2 + |-1|^2 = 2.
#   Partial record (overlap s of recorder states, 0<s<1): chance = 1 + 1 + 2*(+1)(-1)*s = 2 - 2s.
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-in-between.png')
AL, AR = 1.0, -1.0
no_record = abs(AL + AR)**2
record = abs(AL)**2 + abs(AR)**2
assert no_record == 0.0 and record == 2.0
for s in (0.0, 0.5, 1.0):
    print(f"overlap {s}: chance = {abs(AL)**2 + abs(AR)**2 + 2*AL*AR*s:g}")

plt.rcParams.update({'font.size': 11})
fig, axs = plt.subplots(1, 2, figsize=(11, 5.2))
def box(ax, x, y, w, h, text, fc='0.92', fs=10):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle='round,pad=0.02,rounding_size=0.08',
                                fc=fc, ec='k', lw=1.1))
    ax.text(x, y, text, ha='center', va='center', fontsize=fs)
def arrow(ax, p, q, ls='-'):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=14, lw=1.4, color='k', ls=ls,
                                 shrinkA=2, shrinkB=2))
def hand(ax, x, y, sign, L=0.32):
    # a small "clock hand": up for +1, down for -1
    ax.add_patch(FancyArrowPatch((x, y), (x, y + sign*L), arrowstyle='-|>', mutation_scale=11, lw=2.0,
                                 color='k', shrinkA=0, shrinkB=0))

for ax in axs:
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis('off')
    box(ax, 2.0, 8.6, 2.4, 0.8, "left slit")
    box(ax, 2.0, 5.6, 2.4, 0.8, "right slit")

# ---- left panel: no record ----
ax = axs[0]
ax.set_title("No record of the slit", fontsize=12.5)
box(ax, 7.4, 7.1, 2.6, 1.0, "dot here", fc='white', fs=11)
arrow(ax, (3.2, 8.6), (6.1, 7.35)); arrow(ax, (3.2, 5.6), (6.1, 6.85))
ax.text(5.35, 8.6, "amplitude +1", ha='right', va='center', fontsize=9.5); hand(ax, 5.6, 8.25, +1, L=0.65)
ax.text(5.35, 5.65, "amplitude −1", ha='right', va='center', fontsize=9.5); hand(ax, 5.6, 6.0, -1, L=0.65)
ax.text(7.4, 6.25, "same final situation", ha='center', va='top', fontsize=9.5, style='italic')
# tip-to-tail sum: up then down, ends where it started
x0, y0 = 4.6, 4.0
hand(ax, x0, y0, +1, L=1.0); hand(ax, x0 + 0.3, y0 + 1.0, -1, L=1.0)
ax.plot([x0 - 0.12, x0 + 0.42], [y0, y0], color='0.5', lw=0.8)
ax.text(5.25, 4.5, "added tip to tail, the two hands\nend where they started: total 0", fontsize=9, va='center')
ax.text(5.0, 3.3, "amplitudes add first:  (+1) + (−1) = 0", ha='center', fontsize=10.5)
ax.text(5.0, 2.6, "chance here = 0²  =  0", ha='center', fontsize=10.5, weight='bold')
ax.text(5.0, 1.6, "the two slits' combined amplitudes\nmeet and can cancel: a dark stripe", ha='center', va='center', fontsize=10)

# ---- right panel: with a record ----
ax = axs[1]
ax.set_title("A record of the slit (perfectly readable)", fontsize=12.5)
box(ax, 7.4, 8.6, 2.9, 1.05, "dot here,\nrecorder says left", fc='white', fs=10)
box(ax, 7.4, 5.6, 2.9, 1.05, "dot here,\nrecorder says right", fc='white', fs=10)
arrow(ax, (3.2, 8.6), (5.95, 8.6)); arrow(ax, (3.2, 5.6), (5.95, 5.6))
ax.text(4.55, 8.85, "amplitude +1", ha='center', fontsize=9.5); hand(ax, 4.55, 7.55, +1, L=0.65)
ax.text(4.55, 5.85, "amplitude −1", ha='center', fontsize=9.5); hand(ax, 4.55, 5.35, -1, L=0.65)
ax.text(7.4, 7.1, "two different final situations", ha='center', va='center', fontsize=9.5, style='italic')
ax.text(5.0, 3.3, "nothing to add them to; each gives its own chance:", ha='center', fontsize=10.5)
ax.text(5.0, 2.6, "chance here = 1² + (−1)²  =  2", ha='center', fontsize=10.5, weight='bold')
ax.text(5.0, 1.6, "no cancelling: the stripes are gone\n(the two one-slit chances just add)", ha='center', va='center', fontsize=10)

fig.text(0.5, 0.025, "Schematic. Same spot on the screen in both panels (a dark stripe when there is no record); relative units; "
         "thick arrows: each amplitude as a clock hand, up = +1, down = −1.\n"
         "+1 is all the ways through the left slit, taken together; −1 is all the ways through the right slit, taken together.\n"
         "A record that tells the slits apart only partly lies in between: the two slits' amplitudes partly cancel and fainter stripes survive.",
         ha='center', fontsize=9, color='0.25')
fig.tight_layout(rect=(0, 0.10, 1, 1)); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
