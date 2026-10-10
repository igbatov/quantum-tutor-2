# Claims (figure c-three-slits caption and text): "the three curves coincide"; pairs AB/BC
# "stripes one unit apart, peak 4", AC "half a unit apart"; A+B+C "peak 9", "faint stripe of
# height about 1", "zeros at 1/3 and 2/3"; leftover: square zero, plain size zero "at a few spots
# including the centre", cube "equal to 6 at the centre ... changing sign";
# text: "slow fall-off ... is the same for all three slits ... does not affect any comparison".
import numpy as np
from scipy.optimize import brentq
lam = 1.0; a = 1.0; d = 4*a
# position across far screen in units of AB stripe spacing: u = d sin(theta)/lam
u = np.linspace(-3, 3, 600001)
s = u*lam/d
env = np.sinc(a*s/lam)          # np.sinc(x)=sin(pi x)/(pi x); single-slit amplitude, 1 at centre
xs = {'A': -d, 'B': 0.0, 'C': d}
amp = {k: env*np.exp(-2j*np.pi*x*s/lam) for k,x in xs.items()}
tot = {'A':amp['A'],'B':amp['B'],'C':amp['C'],
       'AB':amp['A']+amp['B'],'BC':amp['B']+amp['C'],'AC':amp['A']+amp['C'],
       'ABC':amp['A']+amp['B']+amp['C']}
ok = True
P = {k: np.abs(v)**2 for k,v in tot.items()}
coinc = max(np.max(np.abs(P['A']-P['B'])), np.max(np.abs(P['C']-P['B'])))
print("singles coincide, max diff:", coinc); ok &= coinc < 1e-12
print("AB==BC max diff:", np.max(np.abs(P['AB']-P['BC']))); ok &= np.max(np.abs(P['AB']-P['BC']))<1e-12
i0 = np.argmin(np.abs(u))
print("peaks at centre: AB %.4f AC %.4f ABC %.4f" % (P['AB'][i0], P['AC'][i0], P['ABC'][i0]))
ok &= np.isclose(P['AB'][i0],4) and np.isclose(P['AC'][i0],4) and np.isclose(P['ABC'][i0],9)
def zeros(y):
    sgn = np.where(np.diff(np.sign(y))!=0)[0]; return u[sgn]
# AB dark lines: ABC amplitude of AB vanishes at half-integers
dAB = u[(P['AB']<1e-6) & (np.r_[True, np.diff(P['AB'])<0][:]) ]
abz = np.unique(np.round(u[np.r_[False,(P['AB'][1:-1]<P['AB'][:-2])&(P['AB'][1:-1]<P['AB'][2:]),False]],4))
acz = np.unique(np.round(u[np.r_[False,(P['AC'][1:-1]<P['AC'][:-2])&(P['AC'][1:-1]<P['AC'][2:]),False]],4))
print("AB minima:", abz); print("AC minima:", acz)
ok &= np.allclose(np.diff(abz),1,atol=1e-3) and np.allclose(np.diff(acz),0.5,atol=1e-3)
abcmin = np.unique(np.round(u[np.r_[False,(P['ABC'][1:-1]<P['ABC'][:-2])&(P['ABC'][1:-1]<P['ABC'][2:]),False]],4))
print("ABC minima (|u|<=1.1):", abcmin[np.abs(abcmin)<=1.1], " values:", np.round(P['ABC'][np.searchsorted(u,abcmin[np.abs(abcmin)<=1.1])],8))
ok &= np.allclose(abcmin[(abcmin>0)&(abcmin<1)], [1/3, 2/3], atol=1e-4)
ih = np.argmin(np.abs(u-0.5)); i25 = np.argmin(np.abs(u-2.5))
print("ABC faint stripe height at u=0.5: %.4f; at u=2.5: %.4f" % (P['ABC'][ih], P['ABC'][i25]))
ok &= abs(P['ABC'][ih]-1) < 0.1
# envelope stays positive in |u|<=3 (first single-slit zero at u = d/a = 4)
print("min envelope in window:", env.min()); 
# leftovers under three rules
def left(p):
    F = {k: np.abs(v)**p for k,v in tot.items()}
    return F['ABC']-F['AB']-F['BC']-F['AC']+F['A']+F['B']+F['C']
L2, L1, L3 = left(2), left(1), left(3)
print("max|leftover| square %.2e, size %.4f, cube %.4f" % (np.abs(L2).max(), np.abs(L1).max(), np.abs(L3).max()))
ok &= np.abs(L2).max() < 1e-12
print("plain size leftover at centre: %.2e; cube at centre: %.6f" % (L1[i0], L3[i0]))
ok &= abs(L1[i0])<1e-12 and np.isclose(L3[i0],6)
# where is plain-size leftover zero?
z1 = u[np.abs(L1) < 1e-4]
groups = np.split(z1, np.where(np.diff(z1)>1e-3)[0]+1)
print("plain-size leftover ~0 at u =", [round(g.mean(),3) for g in groups])
frac_nonzero = np.mean(np.abs(L1) > 0.01*np.abs(L1).max())
print("fraction of screen where |size leftover| > 1%% of its max: %.3f" % frac_nonzero)
print("plain-size leftover min %.4f max %.4f" % (L1.min(), L1.max()))
zs = np.array([g.mean() for g in groups]); print("spacing of plain-size zeros:", np.unique(np.round(np.diff(zs[1:-1]),3)))
print("cube leftover min %.3f max %.3f (sign change: %s)" % (L3.min(), L3.max(), L3.min()<0<L3.max()))
ok &= L3.min()<0<L3.max() and frac_nonzero > 0.5
# common envelope cancels from pass/fail: leftover(p) = |env|^p * leftover_unit(p)
phi = 2*np.pi*u
w = np.exp(1j*phi)
unit = lambda p: np.abs(1+w+w**2)**p-np.abs(1+w)**p-np.abs(w+w**2)**p-np.abs(1+w**2)**p+3
for p,Lp in [(1,L1),(3,L3)]:
    r = np.max(np.abs(Lp - np.abs(env)**p*unit(p)))
    print(f"p={p}: leftover = |env|^p x unit-hand leftover, max dev {r:.1e}"); ok &= r<1e-10
print("PASS" if ok else "FAIL")
