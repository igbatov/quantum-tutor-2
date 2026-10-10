# Claim: "A proton's magnetic moment can point along the field or against it, with energies
#  E+ and E-" ... "Larmor frequency, which equals (E+ - E-)/h"; Model 1: "E± = ±hbar omega/2,
#  so omega = (E+ - E-)/hbar" (requires E+ > E-).
# Check the sign: E = -mu . B, so the moment ALONG the field has the LOWER energy.
import scipy.constants as sc
mu_p = sc.physical_constants['proton mag. mom.'][0]
B = 1.0
E_plus = -mu_p * B    # moment along field
E_minus = +mu_p * B   # moment against field
f = (E_plus - E_minus) / sc.h
print(f"E+ (along) = {E_plus:.3e} J, E- (against) = {E_minus:.3e} J")
print(f"(E+ - E-)/h = {f/1e6:.3f} MHz  (negative => the formula as labelled gives a negative frequency)")
print(f"|E+ - E-|/h = {abs(f)/1e6:.3f} MHz")
print("PASS" if f > 0 else "FAIL (sign/labelling: along-field level is the lower one; use |E+ - E-|/h or (E- - E+)/h)")
