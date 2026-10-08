# Claims (Model 1, Erasing): outcomes "have the same chances whichever slit was used (a coin toss for a
# perfect tag)"; "one group shows stripes, the other anti-stripes, and the two together give back the
# pattern"; "at theta = 60, three quarters of the dots land in the stripes group and one quarter in the
# anti-stripes group, and the two add up to half-strength stripes".
import numpy as np
X = np.linspace(-0.5, 0.5, 20001)
ok = True
for thd in [20, 60, 90]:
    th = np.radians(thd); a = np.array([1, 0]); b = np.array([np.cos(th), np.sin(th)])
    ep = (a+b)/np.linalg.norm(a+b); em = np.array([-ep[1], ep[0]])
    pL, pR = (ep@a)**2, (ep@b)**2
    p1 = np.exp(1j*np.pi*X)/np.sqrt(2); p2 = np.exp(-1j*np.pi*X)/np.sqrt(2)
    Gp = np.abs(p1*(ep@a)+p2*(ep@b))**2; Gm = np.abs(p1*(em@a)+p2*(em@b))**2
    tot = np.abs(p1)**2+np.abs(p2)**2+2*np.real(p1*np.conj(p2))*(a@b)
    frac_p = np.trapezoid(Gp, X)/np.trapezoid(Gp+Gm, X)
    vis = lambda P: (P.max()-P.min())/(P.max()+P.min())
    print(f"theta {thd}: P(+|L)={pL:.3f} P(+|R)={pR:.3f}; fraction in + group {frac_p:.3f}; + group peak at X={X[np.argmax(Gp)]:+.2f} (stripes), "
          f"- group peak at X={X[np.argmax(Gm)]:+.2f}; contrasts {vis(Gp):.3f}/{vis(Gm):.3f}; sum contrast {vis(Gp+Gm):.3f}; max|sum-total|={np.max(np.abs(Gp+Gm-tot)):.1e}")
    ok &= abs(pL-pR) < 1e-12 and np.max(np.abs(Gp+Gm-tot)) < 1e-12 and abs(X[np.argmax(Gp)]) < 1e-3 and abs(abs(X[np.argmax(Gm)])-0.5) < 1e-3
    if thd == 90: ok &= abs(pL-0.5) < 1e-12
    if thd == 60: ok &= abs(frac_p-0.75) < 1e-6 and abs(vis(Gp+Gm)-0.5) < 1e-6
print("PASS" if ok else "FAIL")
