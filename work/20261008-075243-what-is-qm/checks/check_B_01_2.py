# Round 2 claim: "for a silver atom that question has only two possible answers, ever"; "tiny magnet, because of one of its electrons"
import sympy as sp
from scipy import constants as c
ok=True
sx=sp.Matrix([[0,1],[1,0]])/2; sy=sp.Matrix([[0,-sp.I],[sp.I,0]])/2; sz=sp.Matrix([[1,0],[0,-1]])/2
th,ph=sp.symbols('theta phi',real=True)
Sn=sp.sin(th)*sp.cos(ph)*sx+sp.sin(th)*sp.sin(ph)*sy+sp.cos(th)*sz
ev=[sp.simplify(e) for e in Sn.eigenvals()]
print("eigenvalues of S.n (hbar=1):",ev); ok &= set(ev)=={sp.Rational(1,2),-sp.Rational(1,2)}
# Ag ground state 4d10 5s1: L=0,S=1/2 -> J=1/2 -> 2J+1 = 2 beams
J=sp.Rational(1,2); print("2J+1 =",2*J+1); ok &= (2*J+1==2)
# electron moment vs Ag-107 nuclear moment (|mu|=0.1135 mu_N, literature value)
mu_e=abs(c.physical_constants['electron mag. mom.'][0]); mu_N=c.physical_constants['nuclear magneton'][0]
r=mu_e/(0.1135*mu_N); print(f"electron/Ag-107 nuclear moment ratio = {r:.0f}"); ok &= r>1e3
print("PASS" if ok else "FAIL")
