import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figures", "b-closing-note-pairs-of-systems.png")
plt.rcParams.update({"font.size": 10})
# Complex-QM value computed from the strategy (Bell measurement + Pauli Z, X, Y for Alice and
# (P +- Q)/sqrt2 for Charlie): three CHSH values of 2 sqrt2. The real-hand bound 7.66 is quoted
# from Renou et al. (2021), not computed here.
I2 = np.eye(2); Z = np.diag([1, -1]).astype(complex); Xp = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]])
phi = np.array([1, 0, 0, 1]) / np.sqrt(2)
E = lambda A, C: np.real(np.vdot(phi, np.kron(A, C) @ phi))
chsh = []
for P, Q in [(Z, Xp), (Z, Y), (Xp, Y)]:
    C1 = (P.conj() + Q.conj()) / np.sqrt(2); C2 = (P.conj() - Q.conj()) / np.sqrt(2)
    chsh.append(E(P, C1) + E(Q, C1) + E(P, C2) - E(Q, C2))
q = sum(chsh)
fig, ax = plt.subplots(figsize=(7, 4))
ax.barh([1], [q], color="C0", height=0.5)
ax.barh([0], [7.66], color="0.6", height=0.5, hatch="//")
ax.text(q + 0.05, 1, f"complex QM: 3 × 2√2 = {q:.2f}", va="center", fontsize=9)
ax.text(7.66 + 0.05, 0, "best any real-hand theory can do: 7.66\n(Renou et al. 2021)", va="center", fontsize=9)
ax.axvline(7.66, color="k", ls="--", lw=1)
ax.text(7.7, 1.55, "experiments above this line → real hands excluded\n(assumes independent sources)", fontsize=8)
ax.set_yticks([0, 1]); ax.set_yticklabels(["real hands", "complex hands"])
ax.set_xlim(6, 10.5); ax.set_ylim(-0.5, 2.0)
ax.set_xlabel("score of the three-party, two-source test (dimensionless)")
ax.set_title("Two independent sources: real and complex hands predict different scores", fontsize=10)
fig.tight_layout()
fig.savefig(OUT, dpi=150)
print("saved", os.path.abspath(OUT), "; computed complex score", q, "; CHSH parts", np.round(chsh, 4))
