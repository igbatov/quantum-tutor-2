# Claim: "expanding, the cross terms −i s1 s̄2 + i s̄1 s2 and +i s1 s̄2 − i s̄1 s2 cancel"
# (as cross terms of ½|s1 − i s2|^2 and ½|s1 + i s2|^2 respectively)
import sympy as sp
s1,s2=sp.symbols('s1 s2'); c1,c2=sp.symbols('c1 c2')  # c = conjugates
I=sp.I
first = sp.expand((s1 - I*s2)*(c1 + I*c2))
second= sp.expand((s1 + I*s2)*(c1 - I*c2))
cross1 = first - s1*c1 - s2*c2; cross2 = second - s1*c1 - s2*c2
print("cross terms of |s1 - i s2|^2:", cross1)
print("cross terms of |s1 + i s2|^2:", cross2)
text1 = -I*s1*c2 + I*c1*s2; text2 = I*s1*c2 - I*c1*s2
print("cancel:", sp.simplify(cross1+cross2)==0)
print("text order matches:", sp.simplify(cross1-text1)==0 and sp.simplify(cross2-text2)==0)
print("text order swapped:", sp.simplify(cross1-text2)==0)
print("PASS" if sp.simplify(cross1-text1)==0 else "FAIL (signs swapped; conclusion 'cancel, total 1' still correct)")
