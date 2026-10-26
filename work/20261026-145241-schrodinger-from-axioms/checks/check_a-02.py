# Claims (Step 4-5): "theta = -(mv/hbar)x' + [omega(k)-kv-omega(k-mv/hbar)]t'";
# "omega(k)=hbar k^2/2m + c k + omega0" unique; bracket "= -mv^2/2hbar"; ck term = frame shift at -c;
# "hbar omega = 1/2 m v_g^2"; boosted psi solves same free SE (any psi).
import sympy as sp
x,t,k,v,m,hb,c,w0,u=sp.symbols("x t k v m hbar c omega0 u",real=True)
om=sp.Function("omega"); ok=True
kp=k-m*v/hb
theta=-(m*v/hb)*x+(om(k)-k*v-om(kp))*t
lhs=sp.I*(k*x+k*v*t-om(k)*t)+sp.I*theta; rhs=sp.I*(kp*x-om(kp)*t)
ok&=sp.simplify(lhs-rhs)==0
# derivative condition
expr=om(k)-(hb*u/m)*k-om(k-u)
ok&=sp.simplify(sp.diff(expr,k)-(sp.diff(om(k),k)-sp.diff(om(k-u),k)-hb*u/m))==0
# polynomial ansatz deg 6: k-independence of bracket for all u
a=sp.symbols("a0:7"); W=sum(a[i]*k**i for i in range(7))
br=sp.expand(W-(hb*u/m)*k-W.subs(k,k-u))
eqs=sp.Poly(br,k,u).coeffs(); eqs=[e for e,mon in zip(sp.Poly(br,k,u).coeffs(),sp.Poly(br,k,u).monoms()) if mon[0]>0]
sol=sp.solve(eqs,a[2:],dict=True); print("polynomial solution:",sol)
ok&= sol==[{a[2]:hb/(2*m),a[3]:0,a[4]:0,a[5]:0,a[6]:0}]
# non-polynomial alternatives fail
for name,Wa in [("relativistic",sp.sqrt(k**2+m**2)),("quartic",hb*k**2/(2*m)+k**4)]:
    b=Wa-(hb*u/m)*k-Wa.subs(k,k-u); d=sp.diff(b,k).subs({k:1.3,u:0.7,m:1,hb:1})
    print(name,"d(bracket)/dk =",sp.N(d)); ok&=abs(sp.N(d))>1e-6
# bracket value and theta
w=hb*k**2/(2*m)+c*k+w0
brk=sp.simplify(w-k*v-w.subs(k,kp)); print("bracket:",brk); ok&=sp.simplify(brk-(c*m*v/hb - m*v**2/(2*hb)))==0
ok&=sp.simplify(brk.subs(c,0)+m*v**2/(2*hb))==0
# completing square
ok&=sp.simplify(hb*k**2/(2*m)+c*k-(hb/(2*m)*(k+m*c/hb)**2-m*c**2/(2*hb)))==0
# relabelled (no phase) wave in frame v has omega-kv = hbar k^2/2m - v k : c=-v, i.e. v=-c
ok&=sp.simplify((hb*k**2/(2*m)-k*v)-(hb*k**2/(2*m)+c*k).subs(c,-v))==0
# hbar omega = 1/2 m vg^2
w=hb*k**2/(2*m); vg=sp.diff(w,k); ok&=sp.simplify(hb*w-m*vg**2/2)==0 and sp.simplify(vg-hb*k/m)==0
# boosted psi solves same free SE: use exact free Gaussian packet psi(x,t)
a0,k0=sp.symbols("a0 k0",positive=True)
def gauss(X,T):
    q=1+sp.I*hb*T/(m*a0**2)
    return sp.exp(-(X-sp.I*a0**2*k0)**2/(2*a0**2*q))/sp.sqrt(q)
SE=lambda P: sp.I*hb*sp.diff(P,t)+hb**2/(2*m)*sp.diff(P,x,2)
g=gauss(x,t); r0=sp.simplify(SE(g)/g); print("lab SE residual/psi:",r0); ok&=r0==0
th=-(m*v*x+m*v**2*t/2)/hb; P=sp.exp(sp.I*th)*gauss(x+v*t,t)
r1=sp.simplify(SE(P)/P); print("boosted SE residual/psi:",r1); ok&=r1==0
P2=gauss(x+v*t,t); r2=sp.simplify(SE(P2)/P2); print("relabel w/o phase residual/psi:",r2); ok&=r2!=0
print("PASS" if ok else "FAIL")
