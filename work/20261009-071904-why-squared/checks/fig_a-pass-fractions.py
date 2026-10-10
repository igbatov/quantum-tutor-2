import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "a-pass-fractions.png")
plt.rcParams.update({"font.size": 11})
th = np.linspace(0, 90, 901); r = np.radians(th)
P, R = 100*np.cos(r)**2, 100*np.sin(r)**2
hp = 100*(90 - th)/90                      # hidden pointer, nearest axis wins (computed in check_A_04)
fig, ax = plt.subplots(figsize=(7.5, 5.6))
ax.plot(th, P, "k-", lw=3, label="pass exit  (cos²θ)")
ax.plot(th, R, "k-", lw=1.2, label="reflect exit  (sin²θ)")
ax.plot(th, P + R, "k--", lw=1.5, label="pass + reflect")
ax.plot(th, hp, "k:", lw=2, label="hidden-pointer model, nearest axis wins")
pts = np.array([0, 30, 45, 60, 90]); vals = 100*np.cos(np.radians(pts))**2
ax.plot(pts, vals, "ko", ms=8, label="ideal single-photon values (real runs within a few per cent)")
for x_, y_ in zip(pts, vals):
    ax.annotate(f"{y_:.0f}%", (x_, y_), textcoords="offset points", xytext={30: (8, 6), 45: (-34, -15), 60: (-34, -15)}.get(int(x_), (7, 4)), fontsize=10, fontweight="bold")
hx = np.array([30, 60]); hy = 100*(90 - hx)/90
ax.plot(hx, hy, "o", mfc="white", mec="k", ms=8)
for x_, y_ in zip(hx, hy):
    ax.annotate(f"{y_:.0f}%", (x_, y_), textcoords="offset points", xytext=(8, -16) if x_ == 30 else (4, 7), fontsize=10)
ax.set_xlim(-2, 92); ax.set_ylim(-3, 112); ax.set_xticks(range(0, 91, 15))
ax.set_xlabel("splitter angle θ (degrees)"); ax.set_ylabel("fraction of photons (%)")
ax.set_title("Single photons at a turned polarizing beam splitter (ideal)")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), fontsize=9, ncol=2, frameon=False)
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
