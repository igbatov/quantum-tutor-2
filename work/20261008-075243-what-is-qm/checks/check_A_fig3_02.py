# Checks the learner-described regimes for figure a-three-distances:
# "close: two bands, one behind each slit, little overlap, almost no stripes";
# "intermediate: bands spread and overlap; stripes only in the overlap zone";
# "far: overlap complete, stripes everywhere, shape stops changing".
# 1D scalar paraxial (Fresnel) propagation, slits of width a, centres at +-d/2, d = 4a.
import numpy as np
from scipy.special import fresnel
from scipy.signal import argrelextrema
a, d = 1.0, 4.0
def u(x, c, lL):
    s = np.sqrt(2/lL); S1, C1 = fresnel(s*(c-a/2-x)); S2, C2 = fresnel(s*(c+a/2-x))
    return ((C2-C1) + 1j*(S2-S1))/np.sqrt(2j)
PANELS = [("close", 20.0, 5.0), ("intermediate", 3.0, 14.0), ("far", 0.05, 640.0)]
def fwhm(x, I):
    m = I >= I.max()/2; xs = x[m]; return xs.max()-xs.min()
def win_vis(x, Ib, x0, p):
    m = abs(x-x0) <= p/2; w = Ib[m]; return (w.max()-w.min())/(w.max()+w.min())
results = {}
for name, N, W in PANELS:
    lL = d*d/N; p = lL/d                       # stripe spacing
    x = np.linspace(-W, W, 400001)
    uL, uR = u(x, -d/2, lL), u(x, d/2, lL)
    IL, IR, Ib = abs(uL)**2, abs(uR)**2, abs(uL+uR)**2
    M = Ib.max(); ILn, Ibn = IL/M, Ib/M
    print(f"\n=== {name}: N = d^2/(lambda L) = {N}, lambda L = {lL:g} a^2, per-slit a^2/(lambda L) = {a*a/lL:g}, "
          f"stripe spacing lambda L/d = {p:g} a, x-range +-{W:g} a")
    # (1) band centre
    pk = x[np.argmax(IL)]
    sym = np.max(abs(u(-2+x[:2001]*0+np.linspace(0,W,2001), -d/2, lL))**2 - abs(u(-2-np.linspace(0,W,2001), -d/2, lL))**2)
    fw = fwhm(x, IL)
    print(f"(1) left-slit band: peak at x = {pk:+.3f} a (slit centre -2 a); symmetric about -2a to {sym:.1e}; "
          f"FWHM = {fw:.3g} a; offset of centre from middle = 2 a = {2/fw:.3g} FWHM = {2/p:.3g} stripe spacings; "
          f"one-slit peak height = {ILn.max():.3f} of both-open peak")
    fr = np.sum(IL[x > 0])/np.sum(IL)
    print(f"    fraction of left-slit band (within plotted range) on the right half: {fr:.3f}")
    # (2) visibility
    Vloc = 2*abs(uL)*abs(uR)/(IL+IR)
    # local fringe visibility: Ib = IL+IR+2 sqrt(IL IR) cos(phi), phi varying over one stripe spacing,
    # so the stripe contrast at x is V = 2 sqrt(IL IR)/(IL+IR)
    for lab, x0 in (("middle", 0.0), ("behind left slit", -2.0)):
        i = np.argmin(abs(x-x0))
        print(f"(2) {lab:17s} x = {x0:+.1f} a: V = {Vloc[i]:.3f} (one-stripe window on bold: {win_vis(x, Ib, x0, p):.3f}); "
              f"both-open {Ibn[i]:.3f}, left-only {ILn[i]:.3f} of panel max")
    pkL = ILn.max()
    band = (ILn >= 0.5*pkL)
    j = np.argmin(np.where(band, Vloc, 9))
    print(f"    inside left band (left-only >= 50% of its peak, x in [{x[band].min():+.2f},{x[band].max():+.2f}] a): "
          f"V from {Vloc[band].min():.3f} (at x = {x[j]:+.2f} a) to {Vloc[band].max():.3f}")
    sh = (ILn >= 0.1*pkL) & (ILn < 0.5*pkL) & (x < -2)
    if sh.any():
        k = np.argmax(np.where(sh, Vloc, -1))
        print(f"    outer shoulder (left-only 10-50% of its peak, x < -2a): V up to {Vloc[k]:.3f} at x = {x[k]:+.2f} a "
              f"(left-only there {ILn[k]/pkL:.2f} of its peak)")
    vis = Ibn > 0.05
    print(f"    wherever both-open > 5% of panel max (x in [{x[vis].min():+.1f},{x[vis].max():+.1f}] a): V from {Vloc[vis].min():.3f} to {Vloc[vis].max():.3f}")
    # stripe modulation amplitude (absolute) in units of panel max
    mid = abs(x) <= 1.0
    print(f"    middle |x|<=1a: both-open max {Ibn[mid].max():.3f}, min {Ibn[mid].min():.4f} (of panel max)")
    # (3) both-open near zero where one-slit well above zero
    imin = argrelextrema(Ibn, np.less_equal, order=5)[0]
    bad = [(x[i], Ibn[i], ILn[i]) for i in imin if Ibn[i] < 0.02 and ILn[i] > 0.05]
    peakL = ILn.max()
    print(f"(3) local minima with both-open < 0.02 and left-only > 0.05 (of panel max): {len(bad)}")
    for b in bad[:6]: print(f"      x = {b[0]:+8.3f} a: both {b[1]:.4f}, left-only {b[2]:.3f} ({b[2]/peakL:.2f} of left peak)")
    strong = ILn > 0.2*peakL
    r = Ibn[strong]/ILn[strong]
    j = np.argmin(r)
    print(f"    where left-only > 20% of its peak: min(both/left) = {r.min():.3f} at x = {x[strong][j]:+.3f} a "
          f"(points where both < left: {np.mean(r<1):.2%})")
    # (4) features
    if name == "close":
        inside = abs(x+2) < 0.5
        print(f"(4) edge ripples: left-only inside geometric slit image ranges {IL[inside].min():.3f}..{IL[inside].max():.3f} "
              f"(1 = geometric shadow value)")
        gap = abs(x) <= 1.0
        print(f"    faint stripes in gap: both-open in |x|<=1a ranges {Ibn[gap].min():.4f}..{Ibn[gap].max():.4f} of peak")
        band = abs(x+2) <= 0.6
        print(f"    ripple from other slit on band (|x+2|<=0.6a): both/left ranges {np.min(Ib[band]/IL[band]):.3f}..{np.max(Ib[band]/IL[band]):.3f}")
    results[name] = (x, Ibn, ILn, lL)
# side bands of the one-slit pattern in each panel
for name, (x, Ibn, ILn, lL) in results.items():
    imax = argrelextrema(ILn, np.greater, order=50)[0]
    pkv = ILn.max(); sb = [(x[i], ILn[i]/pkv) for i in imax if ILn[i] < 0.9*pkv and x[i] < 0]
    sb = sorted(sb, key=lambda t: -t[1])[:3]
    print(f"(4) {name}: strongest one-slit side maxima (x, height/left peak): " + ", ".join(f"({s[0]:+.1f} a, {s[1]:.3f})" for s in sb))
# far: shape stops changing / matches existing figure (Fraunhofer cos^2 * sinc^2 in stripe units)
x, Ibn, ILn, lL = results["far"]; X = x*d/lL
fra = np.cos(np.pi*X)**2*np.sinc(X/4)**2
dev = np.max(abs(Ibn-fra/fra.max()))
x2 = X*lL*0.5/d*1.0
lL2 = 2*lL; xx = X*lL2/d
I2 = abs(u(xx, -2, lL2)+u(xx, 2, lL2))**2; I2 /= I2.max()
dev2 = np.max(abs(Ibn-I2))
print(f"\nfar: max |Fresnel(N=0.05) - Fraunhofer cos^2(pi X) sinc^2(X/4)| over +-8 stripe spacings = {dev:.4f} of peak")
print(f"far: max |pattern(N=0.05) - pattern(N=0.025)| in stripe units = {dev2:.4f} of peak")
print("far: PASS (shape stops changing, matches a-one-vs-both)" if max(dev, dev2) < 0.02 else "far: FAIL")
# intermediate N=1 comparison (task suggested N~1)
for N in (1.0, 2.0, 4.0):
    lL = d*d/N; x = np.linspace(-4*lL, 4*lL, 200001); IL = abs(u(x, -2, lL))**2
    print(f"overlap check N={N}: left-band FWHM {fwhm(x, IL):.2f} a vs slit separation 4 a; fraction of left band on right half {np.sum(IL[x>0])/np.sum(IL):.3f}")
