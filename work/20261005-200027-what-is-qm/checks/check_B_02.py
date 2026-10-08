# Claim: "vertical arrow has no horizontal shadow, so none get through"
# Claim: 45 deg filter in between: "roughly 50 ... roughly 25"; bright light same by wave optics (Malus)
# Check-yourself: middle filter vertical -> expected count
import numpy as np
def chain(N, angles_deg, state_deg):
    n, s = N, np.radians(state_deg)
    out = []
    for a in np.radians(angles_deg):
        n *= np.cos(a - s)**2; s = a; out.append(n)
    return out
two = chain(100, [90], 0)          # photons already vertical, then horizontal filter
three = chain(100, [45, 90], 0)
same = chain(100, [0, 90], 0)
print("V->H:", two, " V->45->H:", three, " V->V->H (check-yourself):", same)
# Monte Carlo single photons to confirm 'roughly'
rng = np.random.default_rng(1); trials = 200000
p1 = rng.random(trials) < 0.5; p2 = p1 & (rng.random(trials) < 0.5)
print("MC per 100: after 45 =", 100*p1.mean(), " after H =", 100*p2.mean())
# Malus for classical intensity I0*cos^2(45)*cos^2(45)
I = 1.0*np.cos(np.pi/4)**2*np.cos(np.pi/4)**2
print("classical intensity fraction:", I)
ok = abs(two[0]) < 1e-12 and abs(three[0]-50)<1e-9 and abs(three[1]-25)<1e-9 and abs(I-0.25)<1e-12 and abs(same[1])<1e-12
print("PASS" if ok else "FAIL")
