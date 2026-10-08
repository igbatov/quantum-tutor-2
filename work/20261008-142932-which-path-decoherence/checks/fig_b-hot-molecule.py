import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from scipy import constants as C
out = os.path.join(os.path.dirname(__file__), "..", "figures", "b-hot-molecule.png")
plt.rcParams.update({"font.size": 10})
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2))
q = np.logspace(np.log10(0.2), np.log10(50), 2000)   # lambda/d
ov = np.abs(np.sinc(2/q))
a.semilogx(q, ov, "k-", lw=2)
a.axvspan(0.2, 2, color="0.8", hatch="//", edgecolor="0.5", lw=0); a.text(0.25, 0.55, "tells the\npaths apart", fontsize=9)
a.axvspan(10, 50, color="0.9", hatch="..", edgecolor="0.6", lw=0); a.text(11, 0.55, "records\nalmost\nnothing", fontsize=9)
a.plot(2, 0, "o", mfc="white", mec="k"); a.annotate("λ/d = 2, overlap 0", (2, 0), (2.4, 0.15), arrowprops=dict(arrowstyle="->"), fontsize=9)
a.plot(20, np.sinc(0.1), "s", color="k"); a.annotate("λ/d = 20,\noverlap ≈ 0.98", (20, 0.98), (3.0, 0.62), arrowprops=dict(arrowstyle="->"), fontsize=9)
a.set_xlabel("photon wavelength / path separation, λ/d"); a.set_ylabel("overlap = surviving fraction of visibility")
a.set_xlim(0.2, 50); a.set_ylim(0, 1.05); a.set_title("one emitted photon (isotropic idealization)")
hc_k = C.h*C.c/C.k
lam = np.logspace(np.log10(0.3e-6), -5, 600)
nph = lambda T: 2*C.c/lam**4/np.expm1(hc_k/(lam*T))
ref = nph(3000).max()
for T, ls in [(1000, ":"), (2000, "--"), (3000, "-")]:
    b.loglog(lam*1e6, nph(T)/ref, ls=ls, color="k", lw=1.8, label=f"{T} K")
b.axvline(1, color="b", lw=1); b.axvline(2, color="r", lw=1.2)
b.text(1.03, 2e-7, "1 µm\n(path sep.)", color="b", fontsize=8); b.text(2.1, 2e-6, "2 µm", color="r", fontsize=8)
b.set_xlim(0.3, 10); b.set_ylim(1e-7, 2)
b.set_xlabel("wavelength (µm)"); b.set_ylabel("photons per unit wavelength per time\n(relative, one common scale)")
b.set_title("ideal black-body shape (schematic trend)"); b.legend(fontsize=9, loc="lower right")
fig.text(0.01, 0.005, "Hotter: more photons and shorter wavelengths, so photons left of the 2 µm line rise steeply (×~600 from 1000 K to 3000 K). 2004 data not drawn.", fontsize=8)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(out, dpi=150); print("saved", out)
