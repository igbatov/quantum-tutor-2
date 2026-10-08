# Claim (figure a-same-situation): partner '+': (+1/sqrt2) + (-1/sqrt2) = 0; partner '-': sum sqrt2,
# chance 2; "total at this spot: 0 + 2 = 2, the same as column 2" (1 + 1).
import sympy as sp
A = sp.Matrix([1, 0]); B = sp.Matrix([0, 1]); p = (A+B)/sp.sqrt(2); m = (A-B)/sp.sqrt(2)
aL, aR = 1, -1
amp_p = aL*(p.T*A)[0] + aR*(p.T*B)[0]; amp_m = aL*(m.T*A)[0] + aR*(m.T*B)[0]
print("partner +: terms", (p.T*A)[0]*aL, (p.T*B)[0]*aR, "sum", sp.simplify(amp_p))
print("partner -: terms", (m.T*A)[0]*aL, (m.T*B)[0]*aR, "sum", sp.simplify(amp_m))
col1 = (aL+aR)**2; col2 = aL**2 + aR**2; col3 = sp.simplify(amp_p**2 + amp_m**2)
print("column1", col1, "column2", col2, "column3 total", col3)
ok = sp.simplify(amp_p) == 0 and sp.simplify(amp_m - sp.sqrt(2)) == 0 and col1 == 0 and col2 == 2 and col3 == 2
print("PASS" if ok else "FAIL")
