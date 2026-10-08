# Claims (decoherence): overlaps of independent taggers "multiply"; "overlap of 0.9 each, fifty of
# them leave stripes about half a per cent strong"; spreading "does not weaken the stripes any
# further (... later collisions among the surroundings alone leave it as it is)"; figure: "on a log
# scale the fall is a straight line"; Hornberger: fell "exponentially with the pressure, each equal
# step in pressure cutting it by the same factor".
import numpy as np
rng = np.random.default_rng(2)
ps = rng.uniform(0.3, 0.95, 6); L = np.array([1.0+0j]); R = np.array([1.0+0j])
for p in ps:
    th = np.arccos(p); L = np.kron(L, [1, 0]); R = np.kron(R, [np.cos(th), np.sin(th)])
ov = abs(np.vdot(L, R)); print(f"joint overlap {ov:.6f} vs product {np.prod(ps):.6f}")
# spreading: random unitary acting on the environment alone (6 taggers + 2 extra fresh particles)
fresh = np.zeros(4); fresh[0] = 1
L2 = np.kron(L, fresh); R2 = np.kron(R, fresh); n = L2.size
q, _ = np.linalg.qr(rng.normal(size=(n, n))+1j*rng.normal(size=(n, n)))
ov2 = abs(np.vdot(q@L2, q@R2)); print(f"after scrambling among surroundings ({n}-dim): overlap {ov2:.6f}")
v50 = 0.9**50; print(f"0.9^50 = {v50:.5f}")
y = np.log10(0.9**np.arange(61)); print("constant log slope:", np.allclose(np.diff(y), np.diff(y)[0]))
lam = np.linspace(0, 5, 6); mc = [np.mean(0.0**rng.poisson(l, 200000)) for l in lam]
print("Poisson, perfect tags: MC", np.round(mc, 4), " exp(-lam)", np.round(np.exp(-lam), 4))
ratios = np.exp(-lam[1:])/np.exp(-lam[:-1]); print("factor per equal pressure step:", np.round(ratios, 4))
ok = abs(ov-np.prod(ps)) < 1e-12 and abs(ov2-ov) < 1e-12 and 0.004 < v50 < 0.006 and np.allclose(mc, np.exp(-lam), atol=3e-3) and np.allclose(ratios, ratios[0])
print("PASS" if ok else "FAIL")
