import numpy as np, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from scipy.linalg import expm
import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-rabi-continuity.png")
sx = np.array([[0,1],[1,0]], complex); up = np.array([1,0], complex)
Om = 2*np.pi*10e3; t1, t2 = 30e-6, 50e-6
U = lambda t: expm(-1j*Om*t/2*sx)            # rotating frame, resonant drive, fixed drive phase
P = lambda psi: abs(psi[1])**2
ts = np.linspace(0, 200e-6, 801)
curve = [P(U(t)@up) for t in ts]
psi1 = U(t1)@up                                # after pulse 1 (30 us)
seg2 = np.linspace(0, t2, 200)
p2 = [P(U(s)@psi1) for s in seg2]             # pulse 2 acting on the state left by pulse 1
psi12 = U(t2)@psi1
plt.rcParams.update({"font.size": 12})
fig, ax = plt.subplots(figsize=(7, 4))
ax.axvspan(0, 30, color="0.92"); ax.axvspan(30, 80, color="0.82")
ax.text(15, 1.04, "pulse 1", ha="center", fontsize=10); ax.text(55, 1.04, "pulse 2", ha="center", fontsize=10)
ax.plot(ts*1e6, curve, "k-", lw=2, label="one pulse of length t")
ax.plot((t1+seg2)*1e6, p2, "--", color="tab:orange", lw=2.5, label="pulse 1 (30 µs), then pulse 2")
ax.plot(t1*1e6, P(psi1), "o", ms=9, mfc="white", mec="k", mew=2)
ax.plot((t1+t2)*1e6, P(psi12), "s", ms=10, mfc="tab:orange", mec="k", mew=1.5)
ax.annotate(f"after 30 µs:\nP = {P(psi1):.3f}", (30, P(psi1)), (3, 0.76), fontsize=10,
            arrowprops=dict(arrowstyle="->"))
ax.annotate(f"30 µs + 50 µs: P = {P(psi12):.3f}\n= single 80 µs pulse", (80, P(psi12)), (55, 0.07), fontsize=10, ha="center",
            arrowprops=dict(arrowstyle="->"))
ax.set_xlabel("pulse length t (µs)"); ax.set_ylabel("spin-flip probability P(t)")
ax.set_xlim(0, 200); ax.set_ylim(-0.02, 1.12)
ax.set_title(r"$P(t)=\sin^2(\Omega t/2)$, $\Omega=2\pi\times10$ kHz", fontsize=12)
ax.legend(loc="upper right", fontsize=9, framealpha=0.95)
fig.tight_layout(); fig.savefig(out, dpi=150)
assert np.allclose(psi12, U(t1+t2)@up)       # composition: same state, not only same P
print("saved", os.path.abspath(out), "P30=%.4f P80=%.4f" % (P(psi1), P(psi12)))
