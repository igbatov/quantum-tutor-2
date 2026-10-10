# Claims: account 1 cons, two-exit "wiggle" rule "still totals 1"; account 2 cons, it "passes every
# turn untouched"; account 3, "The wiggle ... dies as soon as a third direction can be swapped in";
# account 3 premise list: grouping-independence PLUS "passes that direction every time picks out the
# squared shadow"; intro: "with three or more exits, and chances that do not depend on how the outcomes
# are grouped, it is the only rule of any kind" (same wording in 'How the accounts relate').
import numpy as np
rng = np.random.default_rng(2)
g = lambda x: x + 0.03*np.sin(2*np.pi*x)             # wiggle on the squared shadow
ok = True
xs = np.linspace(0, 1, 100001)
ok &= np.all(np.diff(g(xs)) > 0) and g(0) == 0 and abs(g(1) - 1) < 1e-15
th = np.linspace(0, 2*np.pi, 20001)
err2 = np.max(np.abs(g(np.cos(th)**2) + g(np.sin(th)**2) - 1))
print(f"2 exits: max |total-1| over all turns = {err2:.1e}"); ok &= err2 < 1e-12
print(f"wiggle not a power: g(0.25)={g(0.25):.4f} vs 0.25; differs from square by up to {np.max(np.abs(g(xs)-xs)):.3f}")
def rand_basis(n):
    z = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); q, _ = np.linalg.qr(z); return q
psi = np.array([1, 0, 0], complex)
err3 = max(abs(sum(g(abs(np.vdot(q[:, k], psi))**2) for k in range(3)) - 1) for q in (rand_basis(3) for _ in range(5000)))
print(f"3 exits: max |total-1| of wiggle rule over random measurements = {err3:.3f}"); ok &= err3 > 1e-2
# Counterexamples to the intro's short form: rules that are grouping-independent and total 1 in every
# measurement, but are NOT the squared shadow of the arrow: chance(e) = <e|rho|e> with rho != |psi><psi|.
eps = 0.1
rules = {"uniform 1/3 (ignores the arrow)": np.eye(3)/3,
         "90% squared shadow + 10% uniform": (1-eps)*np.outer(psi, psi.conj()) + eps*np.eye(3)/3}
for name, rho in rules.items():
    tot_err = 0; ctx_err = 0
    for _ in range(3000):
        q = rand_basis(3); P = np.real([np.vdot(q[:, k], rho @ q[:, k]) for k in range(3)])
        tot_err = max(tot_err, abs(P.sum() - 1))
        # share direction q0 with a different completion: chance of q0 unchanged by construction
        e = q[:, 0]; ctx_err = max(ctx_err, abs(np.real(np.vdot(e, rho @ e)) - P[0]))
    p_prepared = np.real(np.vdot(psi, rho @ psi))
    print(f"{name}: totals 1 (err {tot_err:.1e}), grouping-independent (err {ctx_err:.0e}), "
          f"chance of the arrow's own direction = {p_prepared:.3f}")
    ok &= tot_err < 1e-12 and p_prepared < 1 - 1e-6
print("=> grouping-independence + totals of 1 do NOT alone force the squared shadow;"
      " the 'passes its own direction every time' premise (stated in account 3) is needed.")
print("PASS (wiggle claims)" if ok else "FAIL (wiggle claims)")
print("FAIL (intro / relate short form omits the 'prepared direction passes every time' premise)")
