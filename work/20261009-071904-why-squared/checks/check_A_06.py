# Claim (account 2): "for every p other than 2, the only changes that keep the chances
# totalling 100% ... are swapping labels and reversing signs ... jumps, not turns.
# For p = 2 ... exactly the turns and mirror flips (unitary)"; exception "p = 1 with
# components that are never negative". Tested for integer and NON-integer p.
import numpy as np
from scipy.optimize import least_squares
rng = np.random.default_rng(0)

def gen_dim(p, n, cplx=False, nonneg=False, N=400):
    """Dimension of the space of generators A with d/dt sum|x_i|^p = 0 for all x
    (continuous 'turns' that keep the total). 0 for real => only jumps possible;
    n for complex => only per-component phase turns."""
    rows = []
    for _ in range(N):
        if cplx:
            x = rng.normal(size=n) + 1j*rng.normal(size=n)
        else:
            x = rng.normal(size=n)
            if nonneg: x = np.abs(x)
        w = p*np.abs(x)**(p-2)*np.conj(x)          # gradient weights
        # d/dt sum |x|^p = Re sum_i w_i (A x)_i ; linear in entries of A
        if cplx:
            row_re = np.real(np.outer(w, x)).ravel(); row_im = np.real(1j*np.outer(w, x)).ravel()
            rows.append(np.concatenate([row_re, row_im]))
        else:
            rows.append(np.real(np.outer(w, x)).ravel())
    M = np.array(rows); s = np.linalg.svd(M, compute_uv=False)
    return int(np.sum(s < 1e-8*s[0]))

ok = True
ps = [0.5, 1.0, 1.5, 1.9, 1.99, 2.0, 2.01, 2.1, 2.5, 3.0, 4.0]
for n in (2, 3):
    for p in ps:
        dr = gen_dim(p, n); dc = gen_dim(p, n, cplx=True)
        exp_r = n*(n-1)//2 if p == 2 else 0
        exp_c = n*n if p == 2 else n
        good = dr == exp_r and dc == exp_c; ok &= good
        print(f"n={n} p={p:<5}: real turn generators={dr} (expect {exp_r}), complex={dc} (expect {exp_c}) {'ok' if good else 'MISMATCH'}")
# p = 1, nonnegative components: sum x_i preserved by A with column sums 0 -> n(n-1) dims
for n in (2, 3):
    d1 = gen_dim(1.0, n, nonneg=True); good = d1 == n*(n-1); ok &= good
    print(f"n={n} p=1 nonneg components: generators={d1} (expect {n*(n-1)}, stochastic flows) {'ok' if good else 'MISMATCH'}")

# Finite (not just infinitesimal) check in 2D real: all linear M with sum|Mx|^p = sum|x|^p
xs = rng.normal(size=(300, 2))
def classify(M):
    A = np.abs(M); 
    sp_ = (np.allclose(np.sort(A, axis=None), [0, 0, 1, 1], atol=1e-5) and
           np.allclose(A.sum(0), 1, atol=1e-5) and np.allclose(A.sum(1), 1, atol=1e-5))
    orth = np.allclose(M.T @ M, np.eye(2), atol=1e-5)
    return sp_, orth
for p in [1.0, 1.5, 1.9, 2.0, 2.1, 3.0]:
    sols = []
    for _ in range(300):
        f = lambda m: (np.abs(xs @ m.reshape(2, 2).T)**p).sum(1) - (np.abs(xs)**p).sum(1)
        r = least_squares(f, rng.normal(size=4), xtol=1e-14, ftol=1e-14, gtol=1e-14)
        if np.max(np.abs(r.fun)) < 1e-8: sols.append(r.x.reshape(2, 2))
    cls = [classify(M) for M in sols]
    n_sp = sum(c[0] for c in cls); n_orth = sum(c[1] for c in cls)
    if p == 2:
        good = len(sols) > 0 and n_orth == len(sols) and n_sp < len(sols)
    else:
        good = len(sols) > 0 and n_sp == len(sols)
    ok &= good
    print(f"2D p={p}: {len(sols)} exact solutions found; signed permutations={n_sp}; orthogonal={n_orth} {'ok' if good else 'MISMATCH'}")
print("PASS" if ok else "FAIL")
