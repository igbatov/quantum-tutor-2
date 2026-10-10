# Claims: "R = 3.29e15 Hz"; "Balmer-alpha ... 4.57e14 Hz ... 656 nm"; "Lyman-alpha ... 2.47e15 Hz, at 122 nm";
# "R(1/4 + 1/9) = 1.19e15 Hz ... is not a hydrogen line"; "a sum ... coincides with a line only when it equals a difference";
# caption: Balmer-beta 6.17e14; "Balmer and lower series crowd below 0.83e15 Hz"; Lyman "up to 3.29e15 Hz";
# "1.6 ns for the state that emits Lyman-alpha".
import numpy as np
from scipy import constants as C
Rinf = C.physical_constants['Rydberg constant times c in Hz'][0]
mu = C.m_e*C.m_p/(C.m_e+C.m_p); RH = Rinf*mu/C.m_e
ok = abs(RH/1e15-3.29) < 0.005
ba, la, bb = RH*(1/4-1/9), RH*(1-1/4), RH*(1/4-1/16)
lam_ba, lam_la = C.c/ba, C.c/la
print(f"R_H c = {RH:.4e} Hz; Balmer-a {ba:.4e} Hz {lam_ba*1e9:.1f} nm (vac); Lyman-a {la:.4e} Hz {lam_la*1e9:.1f} nm; Balmer-b {bb:.4e}")
ok &= abs(ba/1e14-4.57)<0.01 and abs(la/1e15-2.47)<0.01 and abs(bb/1e14-6.17)<0.01 and abs(lam_ba*1e9-656)<1 and abs(lam_la*1e9-122)<0.6
s = RH*(1/4+1/9); print(f"sum = {s:.4e} Hz")
ok &= abs(s/1e15-1.19)<0.005
lines = np.array([RH*(1/a**2-1/b**2) for a in range(1,400) for b in range(a+1,401)])
near = np.min(np.abs(lines-s))/s
print("relative distance of sum to nearest line (n<=400):", near)
ok &= near > 0.05
print("Balmer limit R/4 =", RH/4, "-> below 0.83e15:", RH/4 < 0.83e15)
ok &= RH/4 < 0.83e15 and RH < 3.3e15 and not np.any((lines > RH/4) & (lines < la))   # gap between series
# 2p -> 1s lifetime: A = (2/3)^8 alpha^5 m c^2/hbar (reduced mass correction small)
A = (2/3)**8*C.alpha**5*C.m_e*C.c**2/C.hbar*(mu/C.m_e)
print(f"2p lifetime = {1/A*1e9:.3f} ns")
ok &= abs(1/A*1e9-1.6) < 0.05
print("PASS" if ok else "FAIL")
