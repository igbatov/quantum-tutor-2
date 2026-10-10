# Claims (account 1): "0.866 + 0.500 = 1.37"; "0.707 + 0.707 = 1.41: 141%";
# "Cubes: at 30°, 0.650 + 0.125 = 0.775; at 45°, 0.354 + 0.354 = 0.71: 29% ... unaccounted";
# "Fourth power: 0.25 + 0.25 = 0.5 at 45°"; figure: "plain sizes 0.87 + 0.50 = 1.37".
import numpy as np
c30, s30 = np.cos(np.pi/6), np.sin(np.pi/6); c45 = np.cos(np.pi/4)
checks = [
  ("plain 30° total", c30 + s30, "1.37", 2),
  ("plain 45° total", 2*c45, "1.41", 2),
  ("cube 30° pass", c30**3, "0.650", 3),
  ("cube 30° reflect", s30**3, "0.125", 3),
  ("cube 30° total", c30**3 + s30**3, "0.775", 3),
  ("cube 45° term", c45**3, "0.354", 3),
  ("cube 45° total", 2*c45**3, "0.71", 2),
  ("missing at 45° (cube), %", 100*(1 - 2*c45**3), "29", 0),
  ("fourth 45° term", c45**4, "0.25", 2),
  ("fourth 45° total", 2*c45**4, "0.50", 2),
]
ok = True
for name, v, txt, nd in checks:
    good = f"{v:.{nd}f}" == txt; ok &= good
    print(f"{name}: exact {v:.5f}, text {txt} {'ok' if good else 'X'}")
# printed sums of the rounded terms must also add up as written
for a, b, s in [(0.87, 0.50, 1.37), (0.650, 0.125, 0.775), (0.354, 0.354, 0.708), (0.25, 0.25, 0.5), (0.750, 0.250, 1.0)]:
    good = abs(a + b - s) < 1e-9; ok &= good
    print(f"rounded-term arithmetic {a} + {b} = {a+b:.3f} (text {s}) {'ok' if good else 'X'}")
print("note: 0.354+0.354 = 0.708, written 0.71 (rounded to 2 dp) - consistent")
print("PASS" if ok else "FAIL")
