# Claims: "J(x,y) = (-y,x) ... J^2(x,y) = (-x,-y)"; "rewritten with two real numbers per arm
# and 4x4 real matrices, provided one real matrix J is carried along" (Stueckelberg).
import numpy as np
rng = np.random.default_rng(1)
J2 = np.array([[0, -1], [1, 0]])
ok = np.allclose(J2 @ J2, -np.eye(2)) and np.allclose(J2 @ [3, 5], [-5, 3])
ok &= np.isclose(np.exp(1j*np.pi/2), 1j)          # quarter-wavelength turn = multiply by i
def realify(M):
    return np.block([[M.real, -M.imag], [M.imag, M.real]])
def vec(v):
    return np.concatenate([v.real, v.imag])
J = realify(1j*np.eye(2))
ok &= np.allclose(J @ J, -np.eye(4))
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
worst = 0
for _ in range(200):
    phi = rng.uniform(0, 2*np.pi)
    U = H @ np.diag([np.exp(1j*phi), 1]) @ H
    A = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); Q, _ = np.linalg.qr(A)
    for M in (U, Q):
        R = realify(M)
        ok &= np.allclose(R.T @ R, np.eye(4)) and np.allclose(R @ J, J @ R)
        v = rng.normal(size=2) + 1j*rng.normal(size=2); v /= np.linalg.norm(v)
        w = M @ v; wr = R @ vec(v)
        probs_c = abs(w)**2; probs_r = wr[:2]**2 + wr[2:]**2
        worst = max(worst, np.max(abs(probs_c - probs_r)))
ok &= worst < 1e-12
print('J^2=-1 ok; max prob diff complex vs 4x4 real:', worst)
print('PASS' if ok else 'FAIL')
