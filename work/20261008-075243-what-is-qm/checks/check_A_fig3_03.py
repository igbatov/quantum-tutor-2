# Lists the dark stripes (local minima of both-open) in each panel with the one-slit value there:
# tests whether "opening the second slit makes spots (nearly) unreachable" holds at each distance,
# and how large the stripe swings are in absolute terms (panel-max units) where one slit dominates.
import numpy as np
from scipy.special import fresnel
from scipy.signal import argrelextrema
a, d = 1.0, 4.0
def u(x, c, lL):
    s = np.sqrt(2/lL); S1, C1 = fresnel(s*(c-a/2-x)); S2, C2 = fresnel(s*(c+a/2-x))
    return ((C2-C1) + 1j*(S2-S1))/np.sqrt(2j)
for name, N, W in (("close", 20.0, 5.0), ("intermediate", 3.0, 14.0), ("far", 0.05, 640.0)):
    lL = d*d/N; x = np.linspace(0 if False else -W, 0, 200001)
    uL, uR = u(x, -2, lL), u(x, 2, lL); IL = abs(uL)**2; Ib = abs(uL+uR)**2
    M = abs(u(np.array([0.0]), -2, lL)+u(np.array([0.0]), 2, lL))**2
    xf = np.linspace(-W, W, 400001); M = (abs(u(xf, -2, lL)+u(xf, 2, lL))**2).max()
    Ibn, ILn = Ib/M, IL/M
    mn = argrelextrema(Ibn, np.less, order=3)[0]; mx = argrelextrema(Ibn, np.greater, order=3)[0]
    rows = sorted([(x[i], Ibn[i], ILn[i]) for i in mn if ILn[i] > 0.02], key=lambda r: r[1]/r[2])[:5]
    print(f"\n{name} (N={N}): deepest dark spots relative to left-only (x<=0 half; symmetric):")
    for r in rows:
        print(f"   x = {r[0]:+8.2f} a: both-open {r[1]:.4f}, left-only {r[2]:.3f} -> both/left = {r[1]/r[2]:.3f}")
    # absolute stripe swing (adjacent max - min) on the outer side x < -2.5a (close/intermediate)
    if name != "far":
        for lo, hi in ((-W, -4.5), (-4.5, -2.5), (-1.0, 0.0)):
            m = (x >= lo) & (x <= hi)
            print(f"   x in [{lo:+.1f},{hi:+.1f}] a: both-open ranges {Ibn[m].min():.3f}..{Ibn[m].max():.3f} of panel max")
