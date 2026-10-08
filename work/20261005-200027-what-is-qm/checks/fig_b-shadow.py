import os, numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Arc
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, "..", "figures", "b-shadow.png")
th = np.radians(30); tip = np.array([np.sin(th), np.cos(th)])   # angle measured from vertical
sv, sh = np.cos(th), np.sin(th)
plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots(figsize=(7, 4.6))
ax.plot([0, 0], [-0.1, 1.15], "k--", lw=1); ax.plot([-0.1, 1.25], [0, 0], "k--", lw=1)
ax.text(0.02, 1.13, "filter's axis (vertical)", ha="left", va="top", fontsize=10)
ax.text(1.25, 0.03, "across the axis\n(horizontal)", ha="right", va="bottom", fontsize=10)
ax.plot([tip[0], 0], [tip[1], tip[1]], ":", color="k", lw=1.3)
ax.plot([tip[0], tip[0]], [tip[1], 0], ":", color="k", lw=1.3)
ax.plot([0, 0], [0, sv], color="tab:blue", lw=7, solid_capstyle="butt", alpha=0.8)
ax.plot([0, sh], [0, 0], color="tab:orange", lw=7, solid_capstyle="butt", alpha=0.8)
ax.annotate("", xy=tip, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>,head_width=0.4,head_length=0.8", lw=3.5, color="k"))
ax.text(tip[0]+0.03, tip[1]+0.02, "photon's polarization\n(length 1)", fontsize=10, va="bottom")
ax.add_patch(Arc((0, 0), 0.5, 0.5, theta1=60, theta2=90, lw=1.5))
ax.text(0.07, 0.29, "30°", fontsize=11)
ax.text(-0.04, sv/2, f"shadow on vertical\ncos 30° ≈ {sv:.3f}", ha="right", va="center", color="tab:blue", fontsize=10)
ax.text(sh/2, -0.05, f"shadow on horizontal  sin 30° = {sh:.1f}", ha="center", va="top", color="tab:orange", fontsize=10)
ax.text(0.68, 0.62, f"chance to pass = {sv:.3f}² ≈ {sv**2:.2f}\n"
                    f"chance to be blocked = {sh:.1f}² = {sh**2:.2f}\n"
                    f"{sv**2:.2f} + {sh**2:.2f} = {sv**2+sh**2:.0f}, because the arrow\nhas length 1 (Pythagoras)",
        fontsize=10, va="center", bbox=dict(fc="white", ec="0.6"))
ax.set_xlim(-0.75, 1.3); ax.set_ylim(-0.22, 1.18); ax.set_aspect("equal"); ax.axis("off")
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
