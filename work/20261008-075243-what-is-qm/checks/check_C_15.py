# Claim: "The full quantum theory now predicts hydrogen's lines to better than a part in a billion"
# Evidence: CODATA's Rydberg constant is fixed by fitting QED theory to hydrogen/deuterium spectroscopy;
# its relative uncertainty measures the theory-experiment consistency.
from scipy import constants as k
v, u, unc = k.physical_constants['Rydberg constant']
print(f"R_inf = {v} 1/m, uncertainty {unc} -> relative {unc/v:.1e}")
ok = unc/v < 1e-9
print("PASS" if ok else "FAIL")
