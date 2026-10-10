import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-stationary-vs-cos.png")
plt.rcParams.update({"font.size": 10})
w1, w2 = 1.0, 1.1
a = b = 1 / np.sqrt(2)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 5.6))
t = np.linspace(0, 6 * np.pi, 3000)
ax1.plot(t, np.abs(np.exp(-1j * w1 * t))**2, "-", lw=2.2, label="hand rule |e^(−iω₁t)|² (flat)")
ax1.plot(t, np.cos(w1 * t)**2, "--", lw=1.5, label="one real number cos²(ω₁t)")
ax1.set_ylim(-0.05, 1.3); ax1.set_xlim(0, 6 * np.pi)
ax1.set_xlabel("time t (units of 1/ω₁)"); ax1.set_ylabel("chance")
ax1.set_title("One state of definite energy", fontsize=10)
ax1.legend(fontsize=8, loc="upper right", ncol=2)

# Bottom: window widened to one full beat period 2π/(ω₂-ω₁) = 20π so the slow beat is visible.
T2 = np.linspace(0, 20 * np.pi, 8000)
outcome_amp_hand = (a * np.exp(-1j * w1 * T2) + b * np.exp(-1j * w2 * T2)) / np.sqrt(2)
outcome_amp_real = (a * np.cos(w1 * T2) + b * np.cos(w2 * T2)) / np.sqrt(2)
ax2.plot(T2, np.abs(outcome_amp_real)**2, "--", lw=0.9, color="C1",
         label="real rule ¼(cos ω₁t + cos ω₂t)²: pulses at ω₁+ω₂")
ax2.plot(T2, np.abs(outcome_amp_hand)**2, "-", lw=2.4, color="C0",
         label="hand rule ½(1 + cos 0.1t): one slow beat")
ax2.set_xlim(0, 20 * np.pi); ax2.set_ylim(-0.05, 1.3)
ax2.set_xlabel("time t (units of 1/ω₁); ω₂ = 1.1 ω₁, one beat period = 20π")
ax2.set_ylabel("chance")
ax2.set_title("Equal superposition of two levels, outcome (level 1 + level 2)/√2", fontsize=10)
ax2.legend(fontsize=8, loc="upper right", ncol=1)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT))
