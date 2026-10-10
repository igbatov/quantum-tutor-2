# Claims: "squared shadows along perpendicular directions add up to ... 1, for every arrow";
# "Not the plain shadow, not its cube: nothing else is consistent"; Gleason needs
# "at least three outcomes"; "a quadratic formula ... also covers mixtures" (Tr(rho P)).
import numpy as np
from scipy.stats import unitary_group
rng = np.random.default_rng(3)
ok = True
for d in [2,3,5]:
    worst = {1:0,2:0,3:0}
    for _ in range(2000):
        psi = rng.normal(size=d)+1j*rng.normal(size=d); psi/=np.linalg.norm(psi)
        U = unitary_group.rvs(d, random_state=rng)          # columns = perpendicular directions
        sh = np.abs(U.conj().T @ psi)
        for p in worst: worst[p] = max(worst[p], abs((sh**p).sum()-1))
    print(f"d={d}: max |sum of shadow^p - 1|: p=1 {worst[1]:.3f}, p=2 {worst[2]:.1e}, p=3 {worst[3]:.3f}")
    ok &= worst[2] < 1e-12 and worst[1] > 0.1 and worst[3] > 0.1
# mixtures: chance = Tr(rho P) sums to 1 for any density matrix; reduces to |<e|psi>|^2 for pure
d=3
M = rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)); rho = M@M.conj().T; rho/=np.trace(rho)
U = unitary_group.rvs(d, random_state=rng)
pr = [np.real(U[:,k].conj()@rho@U[:,k]) for k in range(d)]
print("mixture Tr(rho P_k):", np.round(pr,4), "sum", sum(pr)); ok &= np.isclose(sum(pr),1) and min(pr)>=0
# why 'at least three': in a real 2D space a non-quadratic rule still sums to 1 over every
# perpendicular pair: f(theta) = 1/2 + 0.4 cos^3(2 theta), theta = angle from arrow
th = np.linspace(0,2*np.pi,10001)
f = lambda t: 0.5 + 0.4*np.cos(2*t)**3
s = f(th)+f(th+np.pi/2)
print("2D counterexample: max|f(t)+f(t+pi/2)-1| =", np.abs(s-1).max(), " min f =", f(th).min(),
      " differs from cos^2 by up to", np.abs(f(th)-np.cos(th)**2).max())
ok &= np.abs(s-1).max()<1e-12 and f(th).min()>=0 and np.abs(f(th)-np.cos(th)**2).max()>0.05
print("PASS" if ok else "FAIL")
