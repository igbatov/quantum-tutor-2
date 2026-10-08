# Claim: "Lined up, the walk ends 2 ... 4 units: twice the 2"; "Pointing opposite ways ... 0 units";
# "either slit alone gives 1 unit of chance"
import sympy as sp
a = sp.Integer(1); b_in = sp.Integer(1); b_opp = sp.Integer(-1)
one = sp.Abs(a)**2
bright = sp.Abs(a + b_in)**2
dark = sp.Abs(a + b_opp)**2
added = sp.Abs(a)**2 + sp.Abs(b_in)**2
print("one slit:", one, " bright:", bright, " dark:", dark, " chances added:", added, " ratio bright/added:", bright/added)
ok = one == 1 and bright == 4 and dark == 0 and added == 2 and bright/added == 2
print("PASS" if ok else "FAIL")
