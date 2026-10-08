# Claim (Model 1, Erasing): measuring along the halfway direction: "the result is a coin toss
# whichever slit was used and reveals nothing about the slit"; "one group shows stripes and the
# other anti-stripes".
import numpy as np
ok_same = True; coin = True; ok_sign = True
for th in np.radians([20, 60, 90]):
    a = np.array([1, 0]); b = np.array([np.cos(th), np.sin(th)])
    hp = (a+b)/np.linalg.norm(a+b); hm = np.array([-hp[1], hp[0]])
    pL, pR = abs(hp@a)**2, abs(hp@b)**2
    print(f"theta={np.degrees(th):3.0f}: P(+|left)={pL:.3f}  P(+|right)={pR:.3f}")
    ok_same &= abs(pL-pR) < 1e-12; coin &= abs(pL-0.5) < 1e-12
    # signs: + group amplitudes (hp.a, hp.b) same sign; - group opposite sign
    ok_sign &= (hp@a)*(hp@b) > 0 and (hm@a)*(hm@b) < 0
print("same odds for both slits (reveals nothing):", ok_same, "| stripes / anti-stripes signs:", ok_sign)
print("coin toss (50/50) for every theta:", coin)
print("PASS" if (ok_same and ok_sign and coin) else "FAIL: odds are cos^2(theta/2) vs sin^2(theta/2), the same for both slits; 50/50 only for a perfect tag (theta = 90)")
