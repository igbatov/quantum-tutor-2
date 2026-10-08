import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-same-situation.png"
s2 = 1/np.sqrt(2)
fig, axs = plt.subplots(1, 3, figsize=(11, 4.8))
def hand(ax, x, y, a, lab):   # clock hand of length |a| pointing up (+) or down (-)
    ax.annotate("", xy=(x, y+0.55*a), xytext=(x, y), arrowprops=dict(arrowstyle="-|>", lw=2.2))
    ax.add_patch(plt.Circle((x, y), 0.6*abs(a)+0.05, fill=False, lw=0.8, color="gray")); ax.text(x-0.35, y-0.95, lab, fontsize=8.5)
for ax in axs: ax.set_xlim(0, 4); ax.set_ylim(-2.4, 2.6); ax.axis("off")
ax = axs[0]; ax.set_title("1. no tag", fontsize=10)
ax.text(0.2, 2.1, 'both end in "dot here"', fontsize=9)
hand(ax, 1, 0.9, 1, "left: +1"); hand(ax, 3, 0.9, -1, "right: −1")
ax.text(0.2, -1.0, "added: (+1) + (−1) = 0\nchance 0", fontsize=10)
ax = axs[1]; ax.set_title("2. tag (A or B, told apart\nwith certainty)", fontsize=10)
hand(ax, 1, 0.9, 1, '"dot here, tag A": +1'); hand(ax, 3, 0.9, -1, '"dot here, tag B": −1')
ax.text(0.2, -1.0, "different situations, never added\nchance 1 + 1 = 2", fontsize=10)
ax = axs[2]; ax.set_title("3. tag, then measured along\nthe halfway direction", fontsize=10)
for y0, sgn, lab, res in [(1.5, -1, 'partner says +', "sum 0, chance 0"), (-0.6, +1, 'partner says −', "sum √2, chance 2")]:
    ax.text(0.0, y0+0.75, f'"dot here, {lab.split()[-1]}":', fontsize=8.5)
    for x, a, l in [(0.7, 1, "+1/√2"), (1.9, sgn, ("−1/√2" if sgn < 0 else "+1/√2"))]:
        ax.annotate("", xy=(x, y0+0.42*a), xytext=(x, y0), arrowprops=dict(arrowstyle="-|>", lw=2)); ax.text(x+0.1, y0-0.1, l, fontsize=8.5)
    ax.text(2.6, y0-0.05, res, fontsize=9)
ax.text(0.0, -2.2, "total at this spot: 0 + 2 = 2, the same as column 2", fontsize=9.5, weight="bold")
fig.text(0.01, 0.005, "One spot that is dark with no tag. Cancelling happens only between parts that end in the same situation; the tag makes the situations differ; sorting by a tag (or partner)\n"
         "result that is a coin toss whichever slit was used makes them the same again within each group, with a sign flip in one group. The total at the spot does not change.\n"
         "In the real photon experiment the plates' quarter-wave delays also shift where each group's stripes sit; the logic is unchanged. Idealization: a perfect tag.", fontsize=7.8)
fig.tight_layout(rect=(0, 0.1, 1, 1)); fig.savefig(OUT, dpi=150); print(OUT)
