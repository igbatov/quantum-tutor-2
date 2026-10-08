# Claim (rules list, stated before "assuming ideal filters" appears):
#   filter "blocks light wiggling straight across it"; a photon that passed a vertical
#   filter "passes another vertical filter for certain".
# Real setup: a real polarizer (e.g. sunglasses / polarizing film) has principal
# transmittances k1 < 1 along its axis and k2 > 0 across it. Per photon: P(pass) = k1 cos^2 + k2 sin^2.
# Representative ranges (illustrative, not a specific product): k1 ~ 0.7-0.95, k1/k2 ~ 1e2 (sunglasses) to 1e5 (good film/crystal).
import numpy as np
def chain(N, angles, k1, k2, state=0.0):
    n, s = N, np.radians(state)
    for a in np.radians(angles):
        c2 = np.cos(a - s)**2
        n *= k1*c2 + k2*(1-c2); s = a   # passing photons leave aligned with axis
    return n
fail = False
for k1, ext in [(1.0, np.inf), (0.9, 1e2), (0.9, 1e3), (0.95, 1e5)]:
    k2 = 0.0 if ext == np.inf else k1/ext
    same = chain(1, [0], k1, k2)          # already-vertical photon at a 2nd vertical filter
    cross = chain(100, [90], k1, k2)      # 100 vertical photons at horizontal filter
    three = chain(100, [45, 90], k1, k2)  # 100 vertical photons at 45 then horizontal
    print(f"k1={k1}, extinction={ext:g}: P(pass 2nd vertical)={same:.3f}, V->H of 100: {cross:.4f}, V->45->H of 100: {three:.2f}")
    if k1 < 1 and same < 1: fail = True
print("Ideal filters reproduce the text exactly (1, 0, 25). Real filters: 'for certain' and 'blocks' are")
print("only approximate; the payoff (adding a filter raises the count) survives in every case.")
print("FAIL (as written, before the ideal-filter assumption is stated)" if fail else "PASS")
