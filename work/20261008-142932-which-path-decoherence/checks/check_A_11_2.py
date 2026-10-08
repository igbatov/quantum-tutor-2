# Claim (figure a-same-situation): no tag (+1)+(-1)=0; perfect tag: chance 1+1=2; halfway measurement:
# "+" group +1/sqrt2 - 1/sqrt2 = 0; "-" group +1/sqrt2 + 1/sqrt2 = sqrt2, chance 2; "0 + 2 = 2, the same as column 2".
import sympy as sp
A = sp.Matrix([1, 0]); B = sp.Matrix([0, 1]); p = (A+B)/sp.sqrt(2); m = (A-B)/sp.sqrt(2)
aL, aR = 1, -1
ap = sp.simplify(aL*(p.T*A)[0] + aR*(p.T*B)[0]); am = sp.simplify(aL*(m.T*A)[0] + aR*(m.T*B)[0])
print("+ group terms:", aL*(p.T*A)[0], aR*(p.T*B)[0], "sum", ap, "| - group terms:", aL*(m.T*A)[0], aR*(m.T*B)[0], "sum", am)
col1 = (aL+aR)**2; col2 = aL**2+aR**2; col3 = sp.simplify(ap**2+am**2)
print("col1", col1, "col2", col2, "col3", col3)
print("PASS" if (ap == 0 and am == sp.sqrt(2) and col1 == 0 and col2 == 2 and col3 == 2) else "FAIL")
