# Claims (Model 2): "Give every route ... a clock hand whose angle is set by the route's length,
# add the hands ... chance is the squared length of the total. Combine all routes through the left slit
# into one hand and all through the right into another: alike, bright; opposite, dark."
# "for a heavy object the hands for routes near the classical path line up and the rest cancel"
import numpy as np
from scipy.special import fresnel
from scipy.constants import h, m_e, atomic_mass
# --- 1) explicit path sum through two slits (source -> slit point -> screen point), finite distances
lam = 1.0; k = 2*np.pi/lam
a, d = 20.0, 80.0; L1, L2 = 2e6, 2e6
ys = np.concatenate([np.linspace(-d/2-a/2, -d/2+a/2, 4001)])
yR = ys + d
def hand(yslit, x):
    r = np.sqrt(L1**2 + yslit**2) + np.sqrt(L2**2 + (x - yslit)**2)
    return np.trapezoid(np.exp(1j*k*r), yslit)
D = lam*L2/d * (1 + L2/L1)**0  # far-field stripe spacing for screen distance L2 (source at L1 shifts scale slightly)
# effective stripe spacing with point source at L1: lam*(L1+L2)/(d) * L2/(L1+L2)... use measured scale:
Xs = np.linspace(-6, 6, 241)
xs = Xs*lam*L2/d
HL = np.array([hand(ys, x) for x in xs]); HR = np.array([hand(yR, x) for x in xs])
P = np.abs(HL+HR)**2; P /= P[np.argmin(abs(Xs))]/4
Pf = 4*np.sinc(Xs/4)**2*np.cos(np.pi*Xs)**2
err = np.max(abs(P-Pf))
print(f"path sum vs far-field formula, max abs diff (centre peak = 4): {err:.3f}")
for X0 in [0.0, 1.0, 0.5, 1.5]:
    i = np.argmin(abs(Xs-X0)); ang = np.angle(HR[i]/HL[i], deg=True)
    print(f"X={X0}: angle between left and right hands = {ang:7.1f} deg, |L|/|R| = {abs(HL[i])/abs(HR[i]):.3f}")
ok1 = err < 0.1
# --- 2) stationary phase: free path source->screen, sum over the crossing point y of an intermediate plane
# phase ~ k y^2/2 (1/L1 + 1/L2); find half-width Y needed for partial sum within 10% of full sum
def width(lam, L1=1.0, L2=1.0):
    s = np.sqrt(lam*L1*L2/(L1+L2)/2)  # scale: phase = (pi/2)(y/s)^2 * ... -> Fresnel variable
    t = np.linspace(0.01, 50, 200000)
    C, S = fresnel(t); full = 0.5+0.5j
    part = C + 1j*S
    bad = np.abs(part-full) > 0.1*abs(full)
    return t[np.where(bad)[0].max()+1]*s
v = 100.0  # m/s, same speed for all
objs = {"electron": m_e, "C60 molecule": 720*atomic_mass, "1 um dust grain": 1e-15}
ws = {}
for n, m in objs.items():
    lamdb = h/(m*v); ws[n] = width(lamdb)
    print(f"{n:16s}: de Broglie lambda {lamdb:.2e} m, routes that matter lie within {ws[n]:.2e} m of the straight path (1 m + 1 m)")
ok2 = ws["electron"] > ws["C60 molecule"] > ws["1 um dust grain"]
print("PASS" if ok1 and ok2 else "FAIL")
