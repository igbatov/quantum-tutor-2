# Claims: "about 3 GHz"; microwave photon "about a hundred-thousandth of the momentum" of an optical
# photon; "about ten centimetres against less than a thousandth of a millimetre"; "far too little
# to shift an atom by any noticeable fraction of a stripe".
import numpy as np
from scipy.constants import c, h, atomic_mass as u
f_hfs = 3.0357e9            # 85Rb ground-state hyperfine splitting
lam_mw = c/f_hfs; lam_opt = 780.24e-9
ratio = lam_opt/lam_mw
print(f"lambda_mw = {lam_mw*100:.2f} cm, lambda_opt = {lam_opt*1e3:.6f} mm, p_mw/p_opt = {ratio:.2e}")
# Far screen: pattern = momentum distribution; stripe period in momentum = h/d (d = path separation).
# A kick dp shifts the pattern by dp/(h/d) = d/lambda_mw of a stripe, for any d.
for d in [1e-6, 10e-6, 100e-6, 1e-3]:
    print(f"path separation {d*1e6:7.0f} um -> shift = {d/lam_mw:.1e} of a stripe spacing")
v_kick = h/lam_mw/(85*u); print(f"recoil velocity of 85Rb from one microwave photon: {v_kick:.1e} m/s")
ok = 2.5e9 < f_hfs < 3.5e9 and 0.05 < lam_mw < 0.15 and lam_opt < 1e-6 and 3e-6 < ratio < 3e-5 and 1e-3/lam_mw < 0.02
print("PASS" if ok else "FAIL")
