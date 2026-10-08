# Claim: "a microwave photon carries about a hundred-thousandth of the momentum" of an
# optical photon; "about ten centimetres against less than a thousandth of a millimetre";
# hyperfine splitting "about 3 GHz"; "far too little to shift an atom by anything like a stripe".
from scipy.constants import c, h
f_hfs = 3.0357e9          # 85Rb ground hyperfine splitting (Dürr et al. used 85Rb)
lam_mw = c / f_hfs
lam_opt = 780.24e-9       # Rb D2 line (standing-wave light near it)
ratio = lam_opt / lam_mw  # p = h/lambda
print(f"microwave wavelength = {lam_mw*100:.2f} cm ; optical = {lam_opt*1e3:.5f} mm")
print(f"p_mw/p_opt = {ratio:.2e}  (claim ~1e-5)")
# beam splitter gives 2 hbar k_opt; the stripe pattern is set by that momentum difference,
# so a kick that blurs stripes must be of order hbar k_opt / few. Microwave kick relative to that:
blur_ratio = (h/lam_mw) / (2*h/lam_opt)
print(f"microwave kick / splitting momentum 2hbar k = {blur_ratio:.1e}")
ok = (5 < lam_mw*100 < 15) and (lam_opt < 1e-6) and (3e-6 < ratio < 3e-5) and (2.5e9 < f_hfs < 3.5e9) and blur_ratio < 1e-4
print("PASS" if ok else "FAIL")
