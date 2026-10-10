import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-where-the-interpretations-stand.png")
plt.rcParams.update({"font.size": 10})
# Pilot-wave clouds moved along Bohmian velocities v = Im(psi'/psi) (hbar = m = 1), free particle.
L, Nx = 160.0, 8192
X = np.linspace(-L / 2, L / 2, Nx, endpoint=False); dx = X[1] - X[0]
K = 2 * np.pi * np.fft.fftfreq(Nx, dx)
def evolve(psi0, tt): return np.fft.ifft(np.exp(-0.5j * K**2 * tt) * np.fft.fft(psi0))
def vel(psi):
    d = np.fft.ifft(1j * K * np.fft.fft(psi))
    return np.imag(np.conj(psi) * d) / np.maximum(np.abs(psi)**2, 1e-300)
def quantiles(w, n):
    F = np.cumsum(w); F /= F[-1]; return np.interp((np.arange(n) + 0.5) / n, F, X)
def transport(psi0, P, Tend, nsteps):
    dt = Tend / nsteps; tt = 0.0
    for _ in range(nsteps):
        f = lambda p, s: np.interp(p, X, vel(evolve(psi0, s)))
        k1 = f(P, tt); k2 = f(P + dt / 2 * k1, tt + dt / 2); k3 = f(P + dt / 2 * k2, tt + dt / 2); k4 = f(P + dt * k3, tt + dt)
        P = P + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); tt += dt
    return P
g = lambda c: np.exp(-(X - c)**2 / 4.0)
cases = [("one spreading packet", g(0.0)), ("two packets overlapping", g(-3.0) + g(3.0))]
Tend, n = 4.0, 20000
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
for ax, (title, psi0) in zip(axes, cases):
    psi0 = psi0.astype(complex); psi0 /= np.sqrt((np.abs(psi0)**2).sum() * dx)
    psiT = evolve(psi0, Tend)
    bins = np.linspace(-15, 15, 121)
    for w0, lab_t, lab_h, col, ls, mk in [(np.abs(psi0)**2, "|ψ(t)|² (normalised)", "cloud started as |ψ|²", "C0", "-", "o"),
                                          (np.abs(psi0), "|ψ(t)| (normalised)", "cloud started as |ψ|", "C3", "--", "^")]:
        P = transport(psi0, quantiles(w0, n), Tend, 300)
        h, e = np.histogram(P, bins=bins, density=True)
        target = np.abs(psiT)**2 if "²" in lab_t else np.abs(psiT)
        target = target / (target.sum() * dx)
        ax.plot(X, target, ls, color=col, lw=1.8, label=lab_t)
        ax.plot(0.5 * (e[1:] + e[:-1]), h, mk, color=col, ms=3.5, mfc="none", label=lab_h + ", moved to t = 4")
    ax.set_xlim(-15, 15); ax.set_xlabel("position x (units of the initial packet width)")
    ax.set_ylabel("probability density"); ax.set_title(title + " (t = 4)", fontsize=10)
h_, l_ = axes[0].get_legend_handles_labels()
fig.legend(h_, l_, loc="lower center", ncol=2, fontsize=8.5)
fig.tight_layout(rect=(0, 0.13, 1, 1))
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT))
