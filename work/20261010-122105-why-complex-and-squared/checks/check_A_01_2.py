# Claim: "each term expands by the binomial series ... a series in whole powers of t"
# with L = p(|a|^{p-1}sgn(a)g + |b|^{p-1}sgn(b)d), Q = p(p-1)/2(|a|^{p-2}g^2+|b|^{p-2}d^2)
# and the three cases p<2 / p>2 / p=2, plus "both inputs landing on the same exit gives a linear term".
import sympy as sp, numpy as np
t,p=sp.symbols('t p',real=True)
ok=True
for aval in [sp.Rational(3,5), -sp.Rational(3,5), sp.Rational(7,4), -sp.Rational(1,3)]:
    for g in [sp.Rational(2,7), -sp.Rational(5,3)]:
        for pv in [sp.Rational(1,2),1,sp.Rational(3,2),2,3,sp.Rational(5,2),4]:
            expr=(sp.Abs(aval)**pv)*(1+g/aval*t)**pv   # = |a+tg|^p for small t
            full=sp.expand(sp.series(expr,t,0,3).removeO())
            ser=sum(full.coeff(t,k)*t**k for k in range(3))
            L1=pv*sp.Abs(aval)**(pv-1)*sp.sign(aval)*g
            Q1=pv*(pv-1)/2*sp.Abs(aval)**(pv-2)*g**2
            target=sp.Abs(aval)**pv+L1*t+Q1*t**2
            if sp.simplify(sp.expand(ser-target))!=0: ok=False; print('mismatch',aval,g,pv)
            # numeric check that expr really equals |a+tg|^p near 0
            for tv in [1e-3,-1e-3]:
                lhs=abs(float(aval)+tv*float(g))**float(pv); rhs=float(expr.subs(t,tv))
                if abs(lhs-rhs)>1e-12: ok=False
print('binomial expansion, L and Q coefficients:',ok)

# p<2: |t|^p not reproducible by power series. Second derivative of |t|^p at small t:
for pv in [0.5,1.0,1.5,1.9]:
    ts=np.array([1e-2,1e-4,1e-6])
    d1=pv*ts**(pv-1); d2=pv*(pv-1)*ts**(pv-2) if pv!=1 else np.zeros(3)
    print(f'p={pv}: slope at t->0+ {d1}, second deriv {d2}')
# p=1: slope +1 on right, -1 on left (jump). p<1: slope -> inf (cusp). 1<p<2: slope -> 0, curvature -> inf
# => for 1<p<2 there is NO corner or cusp (|t|^p is differentiable with zero slope at 0).
corner_wording_ok = False
print('"corner or cusp" true for 1<p<2?', corner_wording_ok, '(differentiable, slope 0; only curvature blows up)')

# p>2: Q=0 with a,b nonzero forces g=d=0
a,b,g,d=sp.symbols('a b g d',real=True)
pv=3
Q=sp.Rational(pv*(pv-1),2)*(sp.Abs(a)**(pv-2)*g**2+sp.Abs(b)**(pv-2)*d**2)
print('p=3 Q is sum of nonneg terms; zero only for g=d=0:', sp.solve([sp.Eq(Q.subs({a:1,b:2}),0)],[g,d],dict=True) )
# numerical: for p=3, random mixing matrices with columns of p-total 1 cannot keep 1+|t|^p
from scipy.optimize import minimize
worst=[]
ts=np.linspace(-0.5,0.5,101)
for pv in [0.5,1,1.5,2,3,4]:
    def unit(th):
        c,s=np.cos(th),np.sin(th); n=(abs(c)**pv+abs(s)**pv)**(1/pv); return np.array([c,s])/n
    def err(x):
        th1=0.2+ (np.pi/2-0.4)/(1+np.exp(-x[0]))   # first column strictly inside first quadrant: mixing (sizes >= ~0.2)
        M=np.column_stack([unit(th1),unit(x[1])])
        return max(abs(np.sum(np.abs(M@np.array([1,tt]))**pv)-(1+abs(tt)**pv)) for tt in ts)
    best=min(minimize(err,[a0,b0],method='Nelder-Mead').fun for a0 in np.linspace(-3,3,7) for b0 in np.linspace(0,2*np.pi,13))
    worst.append((pv,best)); print(f'p={pv}: smallest max |output p-total - (1+|t|^p)| over mixing devices, |t|<=0.5: {best:.3e}')
# p=2: conditions = orthonormal columns -> rotation family
th=sp.symbols('theta',real=True)
R=sp.Matrix([[sp.cos(th),-sp.sin(th)],[sp.sin(th),sp.cos(th)]])
out=R*sp.Matrix([1,t]); tot=sp.simplify(out[0]**2+out[1]**2)
print('p=2 rotation keeps 1+t^2:', sp.simplify(tot-(1+t**2))==0)
# same exit, real entries: (1,0)->(s1,0),(0,1)->(s2,0); input (1,t): |s1+ s2 t|^p = 1 + p s1 s2 t + ...
for s1 in [1,-1]:
    for s2 in [1,-1]:
        ser=sp.series(sp.Abs(s1+s2*t)**3 if False else (1+s1*s2*t)**p,t,0,2).removeO()
        print('same exit linear coeff', sp.simplify(ser.coeff(t,1)))
# complex caveat: (1,0)->(1,0),(0,1)->(i,0): |1+it|^p=(1+t^2)^(p/2) has no linear term
print('complex same-exit with (1,i): series', sp.series((1+t**2)**(p/2),t,0,3))
print('  but input (1, -i t) gives |1+t|^p = 1 + p t + ...: linear term restored')
allok = ok and all((e>1e-3) if pv!=2 else (e<1e-8) for pv,e in worst)
print('PASS (mathematics)' if allok else 'FAIL', '| wording FAIL: "corner or cusp" for 1<p<2')
