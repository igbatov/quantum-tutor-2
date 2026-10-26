# §2 figure: classical candidates vs observation. (a) Stern-Gerlach screen; (b) interferometer vs spin-rotation angle.
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.linalg import expm
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-classical-vs-quantum.png")
z = np.linspace(-2, 2, 801); s = 0.12                       # deflection in units of max deflection; beam width s
rng = np.random.default_rng(0); cth = rng.uniform(-1, 1, 400000)   # isotropic needles: cos(theta) uniform
zc = cth + rng.normal(0, s, cth.size)
hist, edges = np.histogram(zc, bins=160, range=(-2, 2), density=True); zm = (edges[1:]+edges[:-1])/2
g = lambda m: np.exp(-(z-m)**2/(2*s*s))/np.sqrt(2*np.pi*s*s)
quant = 0.5*g(1) + 0.5*g(-1)
phi = np.linspace(0, 4*np.pi, 801)
sz = np.diag([1, -1]).astype(complex); v = np.array([0.6, 0.8j])
I_spin = np.array([np.linalg.norm(v + expm(-1j*f/2*sz)@v)**2/4 for f in phi])   # = (1+cos(phi/2))/2
I_vec = (1 + np.cos(phi))/2                                                       # classical vector rotated by phi
plt.rcParams.update({"font.size": 11})
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.5, 3.8))
a1.plot(zm, hist, "-", color="tab:blue", lw=2, label="classical needle")
a1.plot(z, quant, "k--", lw=2, label="observed (spin-½)")
a1.set_xlabel("deflection on screen (units of max deflection)"); a1.set_ylabel("probability density")
a1.set_title("(a) Stern–Gerlach screen", fontsize=11); a1.legend(fontsize=8.5, loc="upper center")
a1.set_ylim(0, 2.3)
a2.plot(phi/np.pi, I_vec, "-", color="tab:blue", lw=2, label="classical vector: period 2π")
a2.plot(phi/np.pi, I_spin, "k--", lw=2, label="spin-½ state: period 4π")
a2.axvline(2, color="0.6", lw=1, ls=":"); a2.text(2.05, 0.55, "2π turn", fontsize=9)
a2.set_xlabel("rotation angle φ (units of π rad)"); a2.set_ylabel("output intensity (fraction of max)")
a2.set_title("(b) interferometer, one path rotated", fontsize=11); a2.legend(fontsize=8.5, loc="upper center", ncol=1, framealpha=1)
a2.set_ylim(-0.05, 1.5); a2.set_xticks([0, 1, 2, 3, 4])
fig.tight_layout(); fig.savefig(out, dpi=150)
assert np.allclose(I_spin, (1+np.cos(phi/2))/2)
print("saved", os.path.abspath(out))
