# Claims: "every hydrogen atom in the universe is identical"; "all hydrogen atoms are identical";
# "Physics, not history, sets the ladder". Real setup: hydrogen has isotopes (deuterium, D/H ~ 1.6e-4
# in nature); the nuclear mass enters the ladder via the reduced mass.
from scipy.constants import physical_constants as pc
R_inf = pc['Rydberg constant'][0]
me_mp = pc['electron-proton mass ratio'][0]; me_md = pc['electron-deuteron mass ratio'][0]
n_air = 1.000277
lamH = 1/(R_inf/(1+me_mp)*(1/4-1/9))/n_air*1e9
lamD = 1/(R_inf/(1+me_md)*(1/4-1/9))/n_air*1e9
print(f"H-alpha (protium) {lamH:.3f} nm, D-alpha (deuterium) {lamD:.3f} nm, shift {lamH-lamD:.3f} nm "
      f"({(lamH-lamD)/lamH:.1e} fractional)")
# identical atoms of the same isotope: ladder depends only on constants
print("All protium atoms share one ladder (constants only): True")
print("'every hydrogen atom identical' incl. deuterium:", "FAIL" if abs(lamH-lamD)>0.01 else "PASS")
print("FAIL" if abs(lamH-lamD)>0.01 else "PASS")
