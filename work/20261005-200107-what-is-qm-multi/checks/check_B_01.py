# Claim: "+1 and -1 ... add to 0, and 0^2 = 0" ; "add to 2, and 2^2 = 4 units, ... four times the hits of one slit"
import sympy as sp
one = sp.Integer(1)
dark = (one + (-one))**2
bright = (one + one)**2
single = one**2
ok = dark == 0 and bright == 4 and bright/single == 4
print("dark:", dark, "bright:", bright, "single:", single, "bright/single:", bright/single)
# Also in the physical far-field model psi_L,R = sinc(u) e^{-/+ i 5 pi u}: at u=0 (central bright) ratio 4
u = sp.symbols('u', real=True)
sinc = sp.sin(sp.pi*u)/(sp.pi*u)
psiL = sinc*sp.exp(-sp.I*5*sp.pi*u); psiR = sinc*sp.exp(sp.I*5*sp.pi*u)
P2 = sp.simplify(sp.expand(sp.Abs(psiL+psiR)**2))
P1 = sp.simplify(sp.Abs(psiL)**2)
r = sp.limit((4*sinc**2*sp.cos(5*sp.pi*u)**2)/(sinc**2), u, 0)
print("model ratio P2/P1 at u->0:", r)
print("PASS" if ok and r == 4 else "FAIL")
