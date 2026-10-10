# Claim: "The sign change is forced by losslessness" (for the 50/50 splitter).
# Test: a 50/50 splitter e^{i t_jk}/sqrt2 is unitary iff t11 + t22 - t12 - t21 = pi (mod 2pi).
# The real convention realises this with one -1; the symmetric convention [[1,i],[i,1]]/sqrt2
# realises it with no sign change at all. So a relative PHASE is forced, not specifically a sign.
import numpy as np
rng = np.random.default_rng(0)
ok_cond = True
for _ in range(2000):
    t = rng.uniform(0, 2*np.pi, 4); M = np.exp(1j*t.reshape(2, 2))/np.sqrt(2)
    unit = np.allclose(M.conj().T @ M, np.eye(2), atol=1e-9)
    cond = abs(np.angle(np.exp(1j*(t[0]+t[3]-t[1]-t[2]))) - np.pi) < 1e-6 or abs(np.angle(np.exp(1j*(t[0]+t[3]-t[1]-t[2]))) + np.pi) < 1e-6
    ok_cond &= (unit == cond)
for t11 in np.linspace(0, 2*np.pi, 7):   # construct cases satisfying the condition: all unitary
    t = [t11, 0.3, 1.1, np.pi + 0.3 + 1.1 - t11]; M = np.exp(1j*np.reshape(t, (2, 2)))/np.sqrt(2)
    ok_cond &= np.allclose(M.conj().T @ M, np.eye(2))
S = np.array([[1, 1j], [1j, 1]])/np.sqrt(2)
sym_unitary = np.allclose(S.conj().T @ S, np.eye(2))
no_minus = not np.any(np.isclose(S*np.sqrt(2), -1))
H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
# same fringe with S, shifted by a constant
phi = np.linspace(0, 2*np.pi, 9)
P1S = [abs((S @ np.diag([np.exp(1j*p), 1]) @ S @ [1, 0])[0])**2 for p in phi]
print('unitary <=> phase condition:', ok_cond, '| [[1,i],[i,1]]/rt2 unitary:', sym_unitary, ', contains no -1 entry:', no_minus)
print('exit-1 fraction with symmetric splitters:', np.round(P1S, 3), '(= sin^2(phi/2): fringe shifted by pi)')
print('FAIL: losslessness forces a relative phase (sum condition = pi), not specifically a sign change'
      if ok_cond and sym_unitary and no_minus else 'PASS')
