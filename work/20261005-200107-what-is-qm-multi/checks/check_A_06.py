# Claims: "we see low frequencies as red and high ones as violet";
# Check yourself: rungs farther apart -> bigger drop -> higher f -> bluer (E = hf)
from scipy.constants import c, h, e
f_red = c/700e-9; f_violet = c/400e-9
print(f"f(700nm)={f_red:.3e} Hz, f(400nm)={f_violet:.3e} Hz")
for dE in (1.9, 3.0):
    lam = h*c/(dE*e)*1e9
    print(f"drop {dE} eV -> {lam:.0f} nm")
ok = f_red < f_violet and h*c/(3.0*e) < h*c/(1.9*e)
print("PASS (bigger spacing -> shorter wavelength -> bluer)" if ok else "FAIL")
