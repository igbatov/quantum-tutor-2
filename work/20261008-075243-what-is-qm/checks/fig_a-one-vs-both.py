import os, numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(here, '..', 'figures', 'a-one-vs-both.png')
X = np.linspace(-8, 8, 8001)
P1 = np.sinc(X/4)**2; P2 = 2*P1; Pb = 4*P1*np.cos(np.pi*X)**2
plt.rcParams.update({'font.size': 11})
fig, ax = plt.subplots(figsize=(8, 4.6))
ax.plot(X, Pb, 'k-', lw=2.2, label="both slits open (what is seen)")
ax.plot(X, P2, color='tab:blue', ls='--', lw=1.6, label="if each electron simply went through one slit\nor the other, chances adding")
ax.plot(X, P1, color='0.45', lw=1.0, label="one slit open (either one)")
for xd in (-1.5, -0.5, 0.5, 1.5):
    y1 = np.sinc(xd/4)**2
    ax.annotate('', xy=(xd, 0.02), xytext=(xd, -0.45), arrowprops=dict(arrowstyle='-|>', color='crimson', lw=1.3))
    ax.plot([xd], [y1], 'o', mfc='white', mec='0.3', ms=5)
ax.text(0, -0.62, "dark stripes: zero with both slits, but reachable with one slit (open circles)",
        ha='center', va='top', fontsize=9.5, color='crimson')
ax.set_xlim(-8, 8); ax.set_ylim(-0.95, 4.3)
ax.axhline(0, color='0.7', lw=0.6)
ax.set_xlabel("position on screen (units of the stripe spacing)")
ax.set_ylabel("relative chance of landing here")
ax.legend(loc='upper left', fontsize=8.5, frameon=False)
# inset: magnify side bands so the faint one-slit side bands are visible
ins = ax.inset_axes([0.69, 0.47, 0.30, 0.45])
m = X > 3
ins.plot(X[m], Pb[m], 'k-', lw=1.8); ins.plot(X[m], P2[m], color='tab:blue', ls='--', lw=1.3)
ins.plot(X[m], P1[m], color='0.45', lw=1.0)
ins.set_xlim(3, 8); ins.set_ylim(0, 0.3); ins.tick_params(labelsize=8)
ins.set_title("zoom, right side (vertical scale stretched)", fontsize=8.5)
ins.annotate("one-slit side band\n(peak 0.047 at 5.7)", xy=(5.72, 0.047), xytext=(6.25, 0.235), fontsize=7.5,
             arrowprops=dict(arrowstyle='->', lw=0.8))
ins.annotate("X = 4: dark with\none slit too", xy=(4, 0.003), xytext=(3.35, 0.235), fontsize=7.5,
             arrowprops=dict(arrowstyle='->', lw=0.8))
fig.tight_layout(); fig.savefig(out, dpi=150); print("saved", os.path.abspath(out))
