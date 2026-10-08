# Claim: "two photons sharing one arrow (in a space with four directions) instead of one each"
import numpy as np
V, H = np.array([1.,0]), np.array([0.,1])
dim = np.kron(V, V).size
bell = (np.kron(V,V) + np.kron(H,H))/np.sqrt(2)
schmidt = np.linalg.svd(bell.reshape(2,2), compute_uv=False)
prod = np.kron(V, (V+H)/np.sqrt(2))
schmidt_p = np.linalg.svd(prod.reshape(2,2), compute_uv=False)
print("two-photon dimension:", dim)
print("Schmidt coeffs entangled:", schmidt, " product:", schmidt_p)
ok = dim == 4 and np.sum(schmidt > 1e-12) == 2 and np.sum(schmidt_p > 1e-12) == 1
print("PASS" if ok else "FAIL")
