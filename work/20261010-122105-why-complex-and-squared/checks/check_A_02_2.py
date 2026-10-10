# Claim: "rotation by 15° takes (1,0) to (0.966, 0.259) ... 1.225 for p=1, exactly 1 for p=2, 0.875 for p=4"
import numpy as np, sympy as sp
th=np.deg2rad(15); x,y=np.cos(th),np.sin(th)
tot={p:abs(x)**p+abs(y)**p for p in (1,2,4)}
print(f'point ({x:.4f}, {y:.4f})', {p:round(v,6) for p,v in tot.items()})
e=sp.pi/12; exact4=sp.nsimplify(sp.simplify(sp.cos(e)**4+sp.sin(e)**4)); exact1=sp.simplify(sp.cos(e)+sp.sin(e))
print('exact p=4:',exact4,' exact p=1:',sp.nsimplify(exact1),'=',float(exact1))
ok = round(x,3)==0.966 and round(y,3)==0.259 and round(tot[1],3)==1.225 and abs(tot[2]-1)<1e-15 and exact4==sp.Rational(7,8)
print('PASS' if ok else 'FAIL')
