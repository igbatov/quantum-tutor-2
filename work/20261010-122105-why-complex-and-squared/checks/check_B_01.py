# Claims (candidate-B, "The experiments" (1)):
#  "R = 3.29 x 10^15 Hz"; "Balmer-alpha is R(1/4 - 1/9) = 4.57e14 Hz ... 656 nm";
#  "Lyman-alpha is R(1 - 1/4) = 2.47e15 Hz, at 122 nm"; Balmer-beta 6.17e14 Hz (figure);
#  "No line sits at a sum of terms: R(1/4 + 1/9) = 1.19e15 Hz is not a hydrogen line."
#  Figure caption: "emitted frequencies are differences of terms, never sums".
from fractions import Fraction as F
import scipy.constants as sc

ok = True
R_inf = sc.Rydberg * sc.c                       # Hz
R_H = R_inf / (1 + sc.m_e / sc.m_p)             # reduced-mass correction
print(f"R_inf c = {R_inf:.4e} Hz, R_H c = {R_H:.4e} Hz (text 3.29e15)")
ok &= abs(R_H - 3.29e15) / 3.29e15 < 2e-3

def chk(name, val, text, tol=5e-3):
    global ok
    good = abs(val - text) / text < tol
    ok &= good
    print(f"{name}: {val:.4e} vs text {text:.3e} -> {'ok' if good else 'MISMATCH'}")

R = 3.29e15
chk("Balmer-alpha f", R * (1/4 - 1/9), 4.57e14)
chk("Balmer-alpha lambda (vacuum)", sc.c / (R_H * (1/4 - 1/9)), 656e-9)
chk("Lyman-alpha f", R * (1 - 1/4), 2.47e15)
chk("Lyman-alpha lambda", sc.c / (R_H * 0.75), 122e-9)
chk("Balmer-beta f", R * (1/4 - 1/16), 6.17e14)
chk("sum R(1/4+1/9)", R * (1/4 + 1/9), 1.19e15)

# Is R(1/4+1/9) a hydrogen line (gross structure)? Need 13/36 = 1/a^2 - 1/b^2 exactly.
N = 400
diffs = {}
for a in range(1, N):
    for b in range(a + 1, N):
        diffs.setdefault(F(1, a*a) - F(1, b*b), (a, b))
x = F(1, 4) + F(1, 9)
print("R(1/4+1/9) equals a line R(1/a^2-1/b^2)?", x in diffs)
ok &= x not in diffs
# nearest lines to 1.19e15 Hz
fl = sorted(float(d) * R for d in diffs)
below = max(f for f in fl if f < float(x) * R); above = min(f for f in fl if f > float(x) * R)
print(f"nearest lines: {below:.3e} Hz (Balmer limit side) and {above:.3e} Hz (Lyman-alpha)")

# General claim "never sums": search sums of two terms (incl. the same term twice) equal to a difference
coinc = []
for n in range(1, 60):
    for m in range(n, 60):
        s = F(1, n*n) + F(1, m*m)
        if s in diffs:
            coinc.append(((n, m), diffs[s]))
print("sums of terms that coincide exactly with a line:", coinc[:8], "... total", len(coinc))
general_ok = len(coinc) == 0
print("Example: R(1/9+1/9) =", float(F(2, 9)) * R, "Hz; R(1/4-1/36) (H-delta, 6->2) =", float(F(1, 4) - F(1, 36)) * R)
print("Numbers and the 1.19e15 example:", "PASS" if ok else "FAIL")
print("General 'no line sits at a sum of terms' / 'never sums':", "PASS" if general_ok else "FAIL")
