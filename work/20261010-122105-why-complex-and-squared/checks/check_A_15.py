# Claim (Gleason): with >= 3 directions, the consistent non-contextual rule is the squared shadow
# (or weighted averages) "not the plain size, not a wiggle". Check: |<e|psi>|^2 and Tr(rho P_e) sum
# to 1 over every random orthonormal basis in dim 3 and 4; plain size and the wiggle (eps=0.3) do not.
# Also "prepared along a direction gives that direction with certainty" -> pure rho = |psi><psi|.
import numpy as np
rng = np.random.default_rng(7)
def rand_u(n):
    A = rng.normal(size=(n, n)) + 1j*rng.normal(size=(n, n)); Q, R = np.linalg.qr(A); return Q
eps = 0.3
wig = lambda a: a**2 + eps*a**2*(1-a**2)*(2*a**2-1)
dev = {'square': 0, 'mixed': 0, 'plain': 0, 'wiggle': 0}
for n in (3, 4):
    for _ in range(500):
        psi = rand_u(n)[:, 0]; B = rand_u(n)
        amps = abs(B.conj().T @ psi)
        W = rand_u(n); w = rng.dirichlet(np.ones(n)); rho = W @ np.diag(w) @ W.conj().T
        dev['square'] = max(dev['square'], abs(np.sum(amps**2) - 1))
        dev['mixed'] = max(dev['mixed'], abs(sum((B[:, k].conj() @ rho @ B[:, k]).real for k in range(n)) - 1))
        dev['plain'] = max(dev['plain'], abs(np.sum(amps) - 1))
        dev['wiggle'] = max(dev['wiggle'], abs(np.sum(wig(amps)) - 1))
print({k: f'{v:.2e}' for k, v in dev.items()})
psi = rand_u(3)[:, 0]; rho = np.outer(psi, psi.conj())
certain = abs((psi.conj() @ rho @ psi).real - 1) < 1e-12
ok = dev['square'] < 1e-12 and dev['mixed'] < 1e-12 and dev['plain'] > 0.1 and dev['wiggle'] > 1e-3 and certain
print('PASS' if ok else 'FAIL')
