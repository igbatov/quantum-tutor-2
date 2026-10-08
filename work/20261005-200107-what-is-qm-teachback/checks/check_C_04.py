# Claims: "a vertical piece and a horizontal piece, each about 0.71 long";
# "0.71 x 0.71, about 0.5"; "A vertical arrow is equally a superposition of the two diagonals"
import sympy as sp
c=sp.cos(sp.pi/4)
print("cos45 =",c,"=",float(c)," 0.71^2 =",0.71**2," exact square =",c**2)
V=sp.Matrix([0,1]); D45=sp.Matrix([1,1])/sp.sqrt(2); D135=sp.Matrix([-1,1])/sp.sqrt(2)
a=(D45.T*V)[0]; b=(D135.T*V)[0]
recon=sp.simplify(a*D45+b*D135-V)
print("V = %s*D45 + %s*D135, residual %s"%(a,b,recon.T))
ok = abs(float(c)-0.71)<0.005 and c**2==sp.Rational(1,2) and recon==sp.zeros(2,1) and sp.simplify(a**2-sp.Rational(1,2))==0 and sp.simplify(b**2-sp.Rational(1,2))==0
print("PASS" if ok else "FAIL")
