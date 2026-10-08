# Claims: "A photon's polarization is one example of a qubit"; "two photons can share a single arrow,
# in a way that leaves neither photon an arrow of its own"
import numpy as np
print("polarization space dimension = 2 (two orthogonal filter answers) -> qubit")
bell = np.array([1,0,0,1])/np.sqrt(2); prod = np.kron([1,0],[np.sqrt(.5),np.sqrt(.5)])
for name, s in [("Bell (HH+VV)/sqrt2", bell), ("product", prod)]:
    M = s.reshape(2,2); rho = M @ M.conj().T; pur = np.real(np.trace(rho@rho)); sv = np.linalg.svd(M, compute_uv=False)
    print(f"{name}: dim {s.size}, Schmidt coeffs {np.round(sv,4)}, one-photon purity {pur:.3f}")
M = bell.reshape(2,2); rho = M@M.T; ok = abs(np.trace(rho@rho)-0.5) < 1e-12
# also: no single-photon arrow phi reproduces rho: max |<phi|rho|phi>| = 0.5 < 1
ok &= max(np.linalg.eigvalsh(rho)) < 1 - 1e-9
print("PASS" if ok else "FAIL")
