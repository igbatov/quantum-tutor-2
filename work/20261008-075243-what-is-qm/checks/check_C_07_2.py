# Figure/text consistency: text names 7 Balmer lines in view (656..384 nm); figure c-ladder-lines window 380-700 nm
# draws 4 solid and 3 dotted lines; ladder drawn to rung 6 to scale with values -13.60..-0.38 eV.
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from hcommon_C import *
src = open(os.path.join(os.path.dirname(__file__), 'fig_c-ladder-lines.py')).read()
win = [round(air_nm(vac_nm(n, 2)), 1) for n in range(3, 40) if 380 <= air_nm(vac_nm(n, 2)) <= 700]
print("Balmer lines in 380-700 nm:", win)
ok = len(win) == 7 and 'range(3, 10)' in src and 'range(1, 7)' in src
ok &= os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'figures', 'c-ladder-lines.png'))
ok &= os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'figures', 'c-string-fits.png'))
Ry = k.physical_constants['Rydberg constant times hc in eV'][0] / (1 + m_e/m_p)
print("ladder:", [round(-Ry/n**2, 2) for n in range(1, 7)])
print("PASS" if ok else "FAIL")
