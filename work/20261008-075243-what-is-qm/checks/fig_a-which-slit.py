# Figure a-which-slit: far-screen two-slit pattern with a which-slit recorder.
# Same ideal set-up as a-one-vs-both (slit separation d = 4 x slit width a, far screen,
# X = position in stripe spacings). Each slit's amplitude: A_L = s(X) e^{-i pi X}, A_R = s(X) e^{+i pi X},
# s = sinc(X/4). Recorder states |r_L>, |r_R> with overlap c = <r_L|r_R> (taken real, >= 0).
# P = |A_L|^2 + |A_R|^2 + 2 c Re(A_L* A_R)   (c = 1 no record, 0.5 partial, 0 perfect record)
import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-which-slit.png')
X = np.linspace(-8, 8, 16001)
s = np.sinc(X/4); AL = s*np.exp(-1j*np.pi*X); AR = s*np.exp(1j*np.pi*X)
def P(c): return abs(AL)**2 + abs(AR)**2 + 2*c*np.real(np.conj(AL)*AR)
Padd = abs(AL)**2 + abs(AR)**2
# --- checks backing the caption ---
assert np.allclose(P(1), abs(AL+AR)**2)                         # c=1 is the ordinary both-slit pattern
assert np.allclose(P(1), 4*np.sinc(X/4)**2*np.cos(np.pi*X)**2)  # same as a-one-vs-both bold curve
assert np.allclose(P(0), 2*np.sinc(X/4)**2)                     # c=0: the two one-slit patterns added
for xd in (0.5, 1.5):
    i = np.argmin(abs(X-xd))
    print(f"dark stripe X={xd}: no record {P(1)[i]:.2e}, partial {P(0.5)[i]:.3f}, perfect {P(0)[i]:.3f}")
i0 = np.argmin(abs(X)); i5 = np.argmin(abs(X-0.5))
print("partial: centre peak", round(P(0.5)[i0], 3), " first dark stripe", round(P(0.5)[i5], 3),
      " ratio", round(P(0.5)[i5]/P(0.5)[i0], 3))
# stripe contrast (visibility) near centre = c
Vc = (P(0.5)[i0]-P(0.5)[i5]/s[i5]**2*s[i0]**2)/(P(0.5)[i0]+P(0.5)[i5]/s[i5]**2*s[i0]**2)
print("visibility (envelope-corrected) for c=0.5:", round(Vc, 4)); assert abs(Vc-0.5) < 1e-9
# perfect record: no stripes, but faint side bands remain beyond |X|=4
m = abs(X) > 4.05; print("perfect record, side-band max beyond |X|>4:", round(P(0)[m].max(), 4),
      "at X =", round(abs(X[m][np.argmax(P(0)[m])]), 2), "; zero at X=4:", f"{P(0)[np.argmin(abs(X-4))]:.1e}")
# ----------------------------------
plt.rcParams.update({'font.size': 11})
fig, axs = plt.subplots(3, 1, figsize=(8, 7.6), sharex=True)
PAN = [(1.0, "No record: recorder ends the same either way (overlap 1)"),
       (0.5, "Partial record: recorder states half alike (overlap 0.5)"),
       (0.0, "Perfect record: recorder states fully distinguishable (overlap 0)")]
for k, (ax, (c, title)) in enumerate(zip(axs, PAN)):
    ax.plot(X, P(c), 'k-', lw=2.0, label="what is seen with this record")
    ax.plot(X, Padd, color='tab:blue', ls='--', lw=1.4, label="the two one-slit patterns added")
    ax.axhline(0, color='0.7', lw=0.6)
    ax.set_xlim(-8, 8); ax.set_ylim(-0.25, 4.4); ax.set_yticks([0, 1, 2, 3, 4])
    ax.set_title(title, fontsize=11, loc='left')
    ax.set_ylabel("relative chance")
    if k == 0:
        ax.legend(loc='upper right', fontsize=9, frameon=False)
        ax.annotate("dark stripes reach zero", xy=(0.5, 0.03), xytext=(2.6, 2.6), fontsize=9,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
    if k == 1:
        ax.annotate("stripes fainter: dark stripes\nno longer reach zero", xy=(0.5, P(0.5)[i5]), xytext=(2.6, 2.6),
                    fontsize=9, arrowprops=dict(arrowstyle='->', lw=0.8))
    if k == 2:
        ax.annotate("no stripes: bold curve lies\non the dashed one", xy=(1.0, P(0)[np.argmin(abs(X-1))]),
                    xytext=(2.6, 2.6), fontsize=9, arrowprops=dict(arrowstyle='->', lw=0.8))
        ax.annotate("faint one-slit side bands remain", xy=(5.7, 0.10), xytext=(3.3, 1.2), fontsize=9,
                    arrowprops=dict(arrowstyle='->', lw=0.8))
axs[-1].set_xlabel("position on screen (units of the stripe spacing without a record)")
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
