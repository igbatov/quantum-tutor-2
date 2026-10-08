# Claims: "none get through"; "Roughly half, about 50 ... about 25"; "each now polarized at 45°";
# "Bright light does the same"; Check-yourself (middle filter vertical) answer = 0.
import numpy as np
rng = np.random.default_rng(1)
def u(a): a = np.radians(a); return np.array([np.sin(a), np.cos(a)])  # angle from vertical
def run(N, filters):  # single photons, ideal filters, projective update
    counts = [N]; alive = np.ones(N, bool); state = np.tile(u(0), (N, 1))
    for a in filters:
        p = (state @ u(a))**2; passed = alive & (rng.random(N) < p)
        state[passed] = u(a); alive = passed; counts.append(alive.sum())
    return counts
exact = lambda fs: [100*np.prod([np.cos(np.radians(b-a))**2 for a, b in zip([0]+fs[:i], fs[:i])]) for i in range(len(fs)+1)]
print("exact V->H:", np.round(exact([90]), 6), " exact V->45->H:", np.round(exact([45, 90]), 6), " V->V->H:", np.round(exact([0, 90]), 6))
M = 200000
mc = np.array(run(M, [45, 90]))*100/M; mc2 = np.array(run(M, [90]))*100/M; mc3 = np.array(run(M, [0, 90]))*100/M
print("Monte Carlo per 100: V->45->H", mc, " V->H", mc2, " V->V->H", mc3)
post = u(45) * (u(0) @ u(45)); post /= np.linalg.norm(post); print("state after 45 filter:", post, "= u(45)", u(45))
I = 1.0*np.cos(np.radians(45))**2*np.cos(np.radians(45))**2; print("Malus (bright light) V->45->H fraction:", I)
ok = abs(exact([90])[1]) < 1e-9 and np.allclose(exact([45, 90]), [100, 50, 25]) and abs(exact([0, 90])[2]) < 1e-9
ok &= abs(mc[1]-50) < 0.5 and abs(mc[2]-25) < 0.5 and mc2[1] == 0 and mc3[2] == 0 and np.allclose(post, u(45)) and abs(I-0.25) < 1e-12
print("PASS" if ok else "FAIL")
