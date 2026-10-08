# Claim: "Nobody has to read the record; it only has to exist." / recording slit -> "add chances instead of arrows"
# Model: electron amplitudes a,b entangled with record states |r_a>,|r_b>; P(x) = |a|^2+|b|^2+2Re(a b* <r_b|r_a>).
import numpy as np
phi = np.linspace(0, 2*np.pi, 1001)
a = np.ones_like(phi)/np.sqrt(2); b = np.exp(1j*phi)/np.sqrt(2)
def P(overlap):
    return np.abs(a)**2 + np.abs(b)**2 + 2*np.real(a*np.conj(b)*overlap)
full = P(1.0); rec = P(0.0); partial = P(0.5)
print("no record: min/max =", full.min().round(6), full.max().round(6))
print("orthogonal record (never read): min/max =", rec.min().round(6), rec.max().round(6))
print("partial record overlap 0.5: min/max =", partial.min().round(6), partial.max().round(6))
# Reading the record = tracing it out; the electron's reduced state is the same whether or not it's read
psi = np.kron([1,0],[1,0]) + np.kron([0,1],[0,1]); psi = psi/np.linalg.norm(psi)
rho = np.outer(psi, psi.conj()).reshape(2,2,2,2)
rho_e = np.einsum('ijkj->ik', rho)
print("electron reduced density matrix with orthogonal record:\n", rho_e.real)
ok = np.allclose(rec, 1.0) and full.max() > 1.99 and full.min() < 1e-9 and np.allclose(rho_e, np.eye(2)/2)
print("PASS" if ok else "FAIL")
