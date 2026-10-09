import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, textwrap
plt.rcParams.update({"font.size": 10})
OUT = "/home/user/quantum-tutor-2/work/20261008-142932-which-path-decoherence/figures/a-erasure-views.png"
fig, axs = plt.subplots(1, 4, figsize=(12, 4.4))
txt = ["the tag is a record, read or not; erasing = measuring it so that it predicts nothing about the slit; sorting changes what you know, not the dots",
       "a tag in one atom or one photon pair has not split the world; branches become permanent only when the record spreads into the surroundings",
       "the photon took one route; the tag is truthful; the sorted subset is striped because one wave steers the pair",
       "a one-particle tag is far too small to collapse; erasure works as in standard theory, differing only by far less than anything measurable"]
titles = ["Copenhagen-style", "Many-worlds", "Pilot-wave", "Objective collapse"]
for ax, t, tt in zip(axs, titles, txt):
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([]); ax.set_title(t, weight="bold")
    ax.text(0.05, 0.38, textwrap.fill(tt, 26), va="top", fontsize=8.8)
ax = axs[0]; ax.add_patch(plt.Rectangle((0.15, 0.6), 0.2, 0.2, fill=False, lw=1.5)); ax.text(0.17, 0.67, "tag", fontsize=8)
ax.plot([0.6, 0.6], [0.55, 0.85], "k-", lw=3); ax.text(0.65, 0.68, "polarizer", fontsize=8)
ax = axs[1]; ax.plot([0.1, 0.35], [0.7, 0.7], "k-", lw=2)
ax.plot([0.35, 0.6], [0.7, 0.85], "k-", lw=2); ax.plot([0.35, 0.6], [0.7, 0.55], "k--", lw=2)
ax.plot([0.6, 0.85], [0.85, 0.7], "k-", lw=2); ax.plot([0.6, 0.85], [0.55, 0.7], "k--", lw=2)
ax.text(0.55, 0.88, "A", fontsize=9); ax.text(0.55, 0.47, "B", fontsize=9); ax.text(0.88, 0.68, "re-\nmerge", fontsize=7.5)
ax = axs[2]; ax.plot([0.5, 0.5], [0.45, 0.62], "k-", lw=4); ax.plot([0.5, 0.5], [0.68, 0.78], "k-", lw=4); ax.plot([0.5, 0.5], [0.84, 0.95], "k-", lw=4)
for r in [0.1, 0.18, 0.26]: t = np.linspace(-0.9, 0.9, 50); ax.plot(0.3+r*np.cos(t), 0.73+r*np.sin(t), color="gray", lw=0.8)
y = np.linspace(0, 1, 50); ax.plot(0.1+0.8*y, 0.75+0.06*np.sin(3*y)-0.0*y, "k-", lw=1.5); ax.text(0.62, 0.86, "one route", fontsize=7.5)
ax.text(0.05, 0.47, "wave\nthrough both", fontsize=7.5, color="gray")
ax = axs[3]; ax.plot(0.2, 0.72, "ko", ms=5); ax.text(0.08, 0.55, "tiny tag:\nno collapse", fontsize=7.5)
rng = np.random.default_rng(0); ax.plot(0.7+0.08*rng.normal(size=60), 0.75+0.06*rng.normal(size=60), "k.", ms=3)
ax.text(0.5, 0.52, "many particles:\ncollapse (hidden\nunder decoherence)", fontsize=7.5)
fig.text(0.01, 0.01, "The four views agree on every observation in the two experiments; the panels show what each takes 'erasing' to mean. None of this is settled.", fontsize=8.5)
fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig(OUT, dpi=150); print(OUT)
