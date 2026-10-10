# Claim: "A two-level atom driven in a microwave cavity shows the chance of being in the upper
#  level swinging smoothly between 0 and 1 and back (Brune et al., 1996)". Idealizations listed:
#  "isolated atoms, no damping, ..." (resonance and field state not stated).
# Check the full model: (a) detuned Rabi: P_max = W^2/(W^2+D^2); (b) Jaynes-Cummings with the
# small coherent field used by Brune et al. (mean photon number ~0.4-1): P_e(t) = sum_n p(n) cos^2(g sqrt(n+1) t).
import numpy as np
from scipy.stats import poisson
ok_ideal = True
t = np.linspace(0, 40, 40001)
W = 1.0
P = np.sin(W * t / 2) ** 2
print("resonant ideal: min %.4f max %.4f" % (P.min(), P.max())); ok_ideal &= P.min() < 1e-6 and P.max() > 1 - 1e-6
for D in [0.2, 0.5, 1.0]:
    Wg = np.hypot(W, D)
    Pd = W**2 / Wg**2 * np.sin(Wg * t / 2) ** 2
    print(f"detuning D={D}: max P = {Pd.max():.4f} (formula {W**2/Wg**2:.4f})")
for nbar in [0.0, 0.4, 0.85]:
    n = np.arange(0, 40)
    pn = poisson.pmf(n, nbar) if nbar > 0 else (n == 0).astype(float)
    Pe = (pn[:, None] * np.cos(np.sqrt(n + 1)[:, None] * t[None, :]) ** 2).sum(0)
    print(f"JC coherent nbar={nbar}: min Pe = {Pe.min():.3f}, max Pe = {Pe.max():.3f}")
print("Ideal resonant vacuum-field model swings 0<->1:", "PASS" if ok_ideal else "FAIL")
print("Claim as written about the real driven/cavity experiment (full 0<->1 swing): FAIL "
      "(needs exact resonance and a one-photon/vacuum field and no losses; detuning or a coherent field "
      "keeps P below 1 / above 0)")
