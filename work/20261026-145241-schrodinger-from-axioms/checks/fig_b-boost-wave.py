# §4 figure: free packet in the lab frame and the boosted packet psi_v = e^{i(Mvx - Mv^2 t/2)/hbar} psi(x - vt, t).
# Units hbar = M = 1, x in units of the initial width sigma, t in units of M sigma^2/hbar.
import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-boost-wave.png")
N, L = 8192, 200.0; x = np.linspace(-L/2, L/2, N, endpoint=False); k = 2*np.pi*np.fft.fftfreq(N, L/N)
evolve = lambda p, t: np.fft.ifft(np.exp(-1j*k**2*t/2)*np.fft.fft(p))
lab = lambda X, T: (np.pi*(1+1j*T)**2)**-0.25*np.exp(-X**2/(2*(1+1j*T)))  # exact free Gaussian, sigma=1
v, T = 3.0, 2.0
psi0 = lab(x, 0); boost0 = np.exp(1j*v*x)*psi0
psiT = evolve(psi0, T); boostT = evolve(boost0, T)               # evolve each by the Schrodinger equation
formula = np.exp(1j*(v*x - v**2*T/2))*lab(x - v*T, T)
err = np.max(abs(boostT - formula)); assert err < 1e-10, err
assert np.max(abs(psiT - lab(x, T))) < 1e-10
plt.rcParams.update({"font.size": 11})
fig, axs = plt.subplots(2, 1, figsize=(7, 4.6), sharex=True)
for ax, (pl, pb, tt) in zip(axs, [(psi0, boost0, 0.0), (psiT, boostT, T)]):
    ax.plot(x, pl.real, "-", color="tab:blue", lw=1.8, label="lab frame: Re ψ")
    ax.plot(x, pb.real, "-", color="tab:orange", lw=1.2, label="boosted by v: Re ψ_v")
    ax.plot(x, abs(pb), "k--", lw=1.4, label="|ψ_v| (envelope)")
    ax.axvline(v*tt, color="0.5", ls=":", lw=1)
    ax.text(0.01, 0.85, f"t = {tt:g} Mσ²/ħ", transform=ax.transAxes, fontsize=10)
    ax.set_ylabel("ψ (σ$^{-1/2}$)"); ax.set_ylim(-0.85, 0.85)
idx = slice(None, None, 25)
axs[1].plot(x[idx], formula.real[idx], "o", ms=3.5, mfc="none", mec="k", label=r"formula $e^{i(Mvx-Mv^2t/2)/\hbar}\psi(x-vt,t)$")
axs[1].text(v*T+0.2, -0.75, "x = vt", fontsize=9)
axs[1].set_xlabel("position x (units of σ)"); axs[1].set_xlim(-6, 12)
h1, l1 = axs[1].get_legend_handles_labels()
fig.legend(h1, l1, loc="upper center", ncol=2, fontsize=8.5, frameon=False)
fig.tight_layout(rect=(0, 0, 1, 0.88)); fig.savefig(out, dpi=150)
print("saved", os.path.abspath(out), "max |numeric - formula| =", err)
