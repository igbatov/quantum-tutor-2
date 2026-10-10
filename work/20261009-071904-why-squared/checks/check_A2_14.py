# Figure captions vs drawn data. a-pythagoras: "p = 1 ... peaks at 1.41 at 45°; p = 2 ... flat at 1.00;
# p = 3 ... dips to 0.71; p = 4 dips to 0.50"; left panel labels "0.87"/"0.50", sums printed.
# a-pass-fractions: "straight line meets the filled circles at 0°, 45° and 90° but misses at 30° and 60°".
import os, numpy as np
here = os.path.dirname(os.path.abspath(__file__))
ok = True
th = np.radians(np.linspace(0, 90, 9001))
for p, kind, val in [(1, "max", "1.41"), (3, "min", "0.71"), (4, "min", "0.50")]:
    S = np.cos(th)**p + np.sin(th)**p
    i = np.argmax(S) if kind == "max" else np.argmin(S)
    good = f"{S[i]:.2f}" == val and abs(np.degrees(th[i]) - 45) < 0.02; ok &= good
    print(f"p={p}: {kind} {S[i]:.4f} at {np.degrees(th[i]):.2f}° (caption {val} at 45°) {'ok' if good else 'X'}")
S2 = np.cos(th)**2 + np.sin(th)**2; ok &= np.ptp(S2) < 1e-14; print("p=2 flat, spread", np.ptp(S2))
src = open(os.path.join(here, "fig_a-pythagoras.py")).read()
for s in ["0.866² + 0.500² = 0.750 + 0.250 = 1.000", "plain sizes: 0.87 + 0.50", "every photon accounted for",
          "(cos θ)^p + (sin θ)^p", "p = 1 (plain size)", "p = 2 (square)", "p = 3 (cube)", "p = 4"]:
    good = s in src; ok &= good; print(f"pythagoras figure has '{s}': {good}")
c, s_ = np.cos(np.pi/6), np.sin(np.pi/6)
ok &= f"{c:.2f}" == "0.87" and f"{s_:.2f}" == "0.50" and f"{c**3:.3f} + {s_**3:.3f} = {c**3+s_**3:.3f}" == "0.650 + 0.125 = 0.775"
deg = np.linspace(0, 90, 9001); P = 100*np.cos(np.radians(deg))**2; hp = 100*(90 - deg)/90
meet = deg[np.abs(P - hp) < 1e-6]
print("hidden-pointer line meets cos² at (deg):", np.unique(np.round(meet, 2)))
ok &= set(np.unique(np.round(meet, 2))) == {0.0, 45.0, 90.0}
src2 = open(os.path.join(here, "fig_a-pass-fractions.py")).read()
for s in ["pass exit  (cos²θ)", "reflect exit  (sin²θ)", "pass + reflect", "hidden-pointer"]:
    good = s in src2; ok &= good; print(f"pass-fractions figure has '{s}': {good}")
print("PASS" if ok else "FAIL")
