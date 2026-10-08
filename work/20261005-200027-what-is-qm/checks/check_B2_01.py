# Claim (fix of verify-B #16): "An ideal filter passes all ... Good laboratory filters come close"
# 1) the idealization must be stated before the rules list; 2) with realistic filter specs the
# ideal predictions (0 and 25 of 100; certain re-pass) are approached.
import os, re, numpy as np
txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "final-B.md")).read()
i_ideal = txt.find("from here on all filters are assumed ideal")
i_rules = txt.find("**State:**"); i_update = txt.find("**Update:**")
order_ok = 0 <= i_ideal < i_rules < i_update
print("idealization stated at char", i_ideal, "; rules list starts at", i_rules, "->", order_ok)
def real(seq, k1, ext):          # Jones-matrix model of a real polarizer: amplitude sqrt(k1) along axis, sqrt(k1/ext) across
    n = 100.0; E = np.array([0.0, 1.0])  # (x, y) = vertical
    for a in seq:
        a = np.radians(a); u = np.array([np.sin(a), np.cos(a)]); v = np.array([np.cos(a), -np.sin(a)])
        P = np.sqrt(k1)*np.outer(u, u) + np.sqrt(k1/ext)*np.outer(v, v)
        E = P @ E
    return 100*np.dot(E, E)
ok = order_ok
for k1, ext in [(0.90, 1e3), (0.95, 1e4), (0.98, 1e5), (0.99, 1e6)]:
    two, three, again = real([90], k1, ext), real([45, 90], k1, ext), real([0], k1, ext)
    print(f"k1={k1}, extinction={ext:.0e}: V->H {two:.4f}/100, V->45->H {three:.2f}/100, V->V {again:.1f}/100")
    if k1 >= 0.95 and ext >= 1e4:   # 'good laboratory' (crystal) polarizers; k1=0.9 row is shown for context only
        ok &= (two < 0.1) and (abs(three-25)/25 < 0.15) and (again >= 90)
print("ideal: 0, 25, 100. Within 15% for good lab filters (k1>=0.95, extinction>=1e4):", ok)
print("PASS" if ok else "FAIL")
