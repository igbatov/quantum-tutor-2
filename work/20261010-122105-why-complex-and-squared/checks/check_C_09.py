# Claims: f(x)=x^2+eps x^2(1-x^2)(2x^2-1): f(cos)+f(sin)=1; f(0)=0,f(1)=1; (1-x^2)(2x^2-1) in [-1,1/8]; f>=0 for |eps|<1;
# three exits (1,1,1)/sqrt3: f=1/3-2eps/27, total 1-2eps/9; fig: curves cross at 1/sqrt2; endpoints 0.822, 1.178
import sympy as sp, numpy as np
x,e,t=sp.symbols('x epsilon theta',real=True)
f=lambda z: z**2+e*z**2*(1-z**2)*(2*z**2-1)
ok=sp.simplify(sp.expand(f(sp.cos(t))+f(sp.sin(t))).subs(sp.sin(t)**2,1-sp.cos(t)**2))==1
ok2=sp.simplify(sp.expand(f(sp.cos(t))+f(sp.sin(t)))-1)==0 or ok
print("two-exit total 1:",ok2, " f(0),f(1):",f(0),sp.simplify(f(1)))
g=(1-x**2)*(2*x**2-1); xs=np.linspace(0,1,100001); gv=sp.lambdify(x,g)(xs)
print("g range on [0,1]:",gv.min(),gv.max())
okg=np.isclose(gv.min(),-1) and np.isclose(gv.max(),1/8,atol=1e-9)
fv=lambda ee: xs**2*(1+ee*gv); okpos=all(fv(ee).min()>=0 for ee in np.linspace(-0.999,0.999,41))
f3=sp.simplify(f(1/sp.sqrt(3))); print("f(1/sqrt3) =",f3, " total =",sp.simplify(3*f3))
ok3=sp.simplify(f3-(sp.Rational(1,3)-2*e/27))==0 and sp.simplify(3*f3-(1-2*e/9))==0
print("f(1/sqrt2)=",sp.simplify(f(1/sp.sqrt(2))))
print("endpoint values eps=+-0.8:",[float(1-2*ee/9) for ee in (0.8,-0.8)])
print("PASS" if ok2 and okg and okpos and ok3 else "FAIL")
