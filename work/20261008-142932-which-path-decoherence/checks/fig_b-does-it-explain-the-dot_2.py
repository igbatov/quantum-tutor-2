import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from matplotlib.patches import Circle
out = os.path.join(os.path.dirname(__file__), "..", "figures", "b-does-it-explain-the-dot.png")
plt.rcParams.update({"font.size": 10})
views = [("Copenhagen-style", "the dot is the result; the record is\nclassical for all practical purposes"),
         ("Many-worlds", "both dots happen, in two branches that\ncan no longer interfere; we are in one"),
         ("Pilot-wave", "the particle was on one path all along;\nthe other part of the wave is tied to the\nwrong surroundings and no longer steers"),
         ("Objective collapse", "a real localization, too rare to see\nfor a molecule, too fast to miss for a screen")]
fig, axs = plt.subplots(1, 4, figsize=(13, 4.2))
for a, (t, ans) in zip(axs, views):
    a.set_xlim(0, 11); a.set_ylim(-1.2, 10); a.axis("off"); a.set_title(t, fontsize=11, weight="bold")
    a.plot([1, 5], [6, 8], "b-", lw=2); a.plot([1, 5], [6, 4], "b-", lw=2)
    a.text(0.2, 6.6, "molecule", fontsize=8, color="b")
    a.annotate("", (8, 9.3), (5, 8), arrowprops=dict(arrowstyle="->", ls="--", color="r"))
    a.annotate("", (8, 2.7), (5, 4), arrowprops=dict(arrowstyle="->", ls="--", color="r"))
    a.text(5.5, 9.3, "photon state A", fontsize=8, color="r"); a.text(5.5, 2.2, "photon state B", fontsize=8, color="r")
    a.plot([9, 9], [3.5, 8.5], "k-", lw=3); a.text(9.2, 5.6, "screen:\nno\nstripes", fontsize=8)
    if t == "Pilot-wave": a.add_patch(Circle((3.5, 7.5), 0.3, color="k"))
    a.text(0.0, -1.0, "What makes it one dot?\n" + ans, fontsize=8.5, va="bottom", bbox=dict(fc="0.95", ec="0.6"))
fig.text(0.5, 0.01, "Same predictions for every experiment above; objective collapse differs only by amounts far too small\nto detect for molecules, growing with the amount of matter.", ha="center", fontsize=10, style="italic")
fig.tight_layout(rect=(0, 0.08, 1, 1)); fig.savefig(out, dpi=150); print("saved", out)
