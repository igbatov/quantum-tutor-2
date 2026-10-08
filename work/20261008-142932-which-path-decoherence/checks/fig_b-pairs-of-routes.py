import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
out = os.path.join(os.path.dirname(__file__), "..", "figures", "b-pairs-of-routes.png")
plt.rcParams.update({"font.size": 10})
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.2))
x = np.linspace(0, 1, 200)
for off in np.linspace(-0.04, 0.04, 7):
    a.plot(x, off*np.sin(np.pi*x)*np.sin(3*np.pi*x+off*50), color="0.4", lw=1)
for amp in [0.25, -0.45, 0.7]:
    a.plot(x, amp*np.sin(np.pi*x), "k-", lw=1.2)
a.plot([0, 1], [0, 0], "ko", ms=6); a.text(-0.05, -0.12, "start"); a.text(0.95, -0.12, "end")
def pair(y1, y2, lab, xx):
    a.annotate("", (xx, y1), (xx, y2), arrowprops=dict(arrowstyle="<->", color="b")); a.text(xx+0.02, (y1+y2)/2, lab, color="b", fontsize=9)
pair(0.03, -0.03, "", 0.5); a.annotate("close pair", (0.5, -0.03), (0.42, -0.25), color="b", fontsize=9, arrowprops=dict(arrowstyle="-", color="b")); pair(0.25*np.sin(np.pi*0.3), 0, "medium pair", 0.3); pair(0.7*np.sin(np.pi*0.75), -0.45*np.sin(np.pi*0.75), "far pair", 0.75)
a.set_xlim(-0.08, 1.15); a.set_ylim(-0.6, 0.85); a.axis("off"); a.set_title("routes of a heavy object (schematic, not to scale)")
r = np.logspace(-2, 1, 2000); lam = np.linspace(0.7, 1.3, 1201)
om = np.mean(1 - np.sinc(2*r[:, None]/lam[None, :]), axis=1)
for N, ls in [(1, "-"), (10, "--"), (100, ":")]:
    b.semilogx(r, np.exp(-N*om), ls=ls, color="k", lw=2, label=f"after {N} scattering time{'s' if N > 1 else ''}")
b.set_xlabel("pair separation / scatterer wavelength, Δx/λ"); b.set_ylabel("surroundings' factor for the pair")
b.set_xlim(0.01, 10); b.set_ylim(0, 1.05); b.legend(fontsize=9, loc="upper right", bbox_to_anchor=(1, 0.85))
b.set_title("surviving window narrows as 1/√N on the sloped part", fontsize=10); b.axhline(np.exp(-1), color="gray", ls=":", lw=1); b.text(1.2, 0.4, "N=1 levels off at 1/e", fontsize=8, color="gray")
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", out)
