# Claim: "(half the wavelength, four times the energy)"; fig: string length 0.5 -> "four times more" energy of motion
import sympy as sp
h, m, lam, L, n = sp.symbols('h m lambda L n', positive=True)
KE = (h/lam)**2/(2*m)                     # de Broglie p = h/lambda
ratio = sp.simplify(KE.subs(lam, lam/2)/KE)
print("KE(lambda/2)/KE(lambda) =", ratio)
hb = sp.symbols('hbar', positive=True)
Ebox = n**2*sp.pi**2*hb**2/(2*m*L**2)     # particle in box
rbox = sp.simplify(Ebox.subs(L, L/2)/Ebox)
print("E_box(L/2)/E_box(L) =", rbox, "; wavelength of n=1 = 2L ->", "halved")
print("PASS" if ratio == 4 and rbox == 4 else "FAIL")
