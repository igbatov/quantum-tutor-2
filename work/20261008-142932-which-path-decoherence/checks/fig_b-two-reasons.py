import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np, os
from scipy import constants as C
out = os.path.join(os.path.dirname(__file__), "..", "figures", "b-two-reasons.png")
plt.rcParams.update({"font.size": 10})
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.3))
m = np.logspace(np.log10(C.m_e), -12, 200)
a.loglog(m, C.h/(m*100), "k-", lw=2)
a.axhline(1e-15, ls="--", color="gray"); a.text(1e-29, 2e-15, "atomic nucleus (10⁻¹⁵ m)", color="gray", fontsize=9)
mC70 = 70*12.011*C.atomic_mass
for mm, lab, off in [(C.m_e, "electron\n~7 µm", (30, 0.02)), (mC70, "C70\n~5 pm", (30, 0.02)), (1e-12, "10 µm dust grain\n~7×10⁻²⁴ m", (1e-6, 20))]:
    a.plot(mm, C.h/(mm*100), "o", ms=7, mfc="white", mec="k")
    a.annotate(lab, (mm, C.h/(mm*100)), (mm*off[0], C.h/(mm*100)*off[1]), fontsize=9, arrowprops=dict(arrowstyle="->"))
a.set_xlabel("mass (kg)"); a.set_ylabel("de Broglie wavelength at 100 m/s (m)")
a.set_title("too fine to resolve")
D = np.logspace(-9, -4, 200)
R = lambda D, n: n*470/4*4*np.pi*(D/2)**2
b.loglog(D*1e6, R(D, 2.5e25), "k-", lw=2, label="sea-level air, room temperature")
b.loglog(D*1e6, R(D, 2.5e25*1e-6/1013), "k--", lw=1.5, label="10⁻⁶ mbar vacuum (Exp. 2)")
for d, lab in [(1e-9, "~10¹⁰ /s"), (1e-7, "~10¹⁴ /s"), (1e-5, "~10¹⁸ /s")]:
    b.plot(d*1e6, R(d, 2.5e25), "o", ms=7, mfc="white", mec="k"); b.text(d*1e6*1.3, R(d, 2.5e25)*0.15, lab, fontsize=9)
b.set_xlabel("object diameter (µm)"); b.set_ylabel("air-molecule impacts per second (lower bound)")
b.set_title("constantly recorded"); b.legend(fontsize=8, loc="upper left")
fig.text(0.01, 0.005, "Each air impact resolves separations > ~0.02 nm, so fading time ≈ one impact time; surface impacts only, so true rate is at least this.", fontsize=8)
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(out, dpi=150); print("saved", out)
