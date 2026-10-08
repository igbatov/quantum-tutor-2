# Claim: "the same rule applied to hydrogen predicts the colours it emits"
# Schroedinger hydrogen levels E_n = -R_H hc / n^2 (reduced mass) -> Balmer lines vs measured (vacuum, nm)
import numpy as np
from scipy.constants import physical_constants as pc, m_e, m_p, h, c
Rinf = pc['Rydberg constant'][0]
RH = Rinf/(1 + m_e/m_p)
meas = {3: 656.469, 4: 486.271, 5: 434.169, 6: 410.289}  # NIST vacuum wavelengths
ok = True
for n, lm in meas.items():
    lam = 1/(RH*(1/4 - 1/n**2))*1e9
    rel = abs(lam-lm)/lm; ok &= rel < 1e-4
    print(f"n={n}->2: predicted {lam:.3f} nm, measured {lm:.3f} nm, rel diff {rel:.1e}")
print("PASS" if ok else "FAIL")
