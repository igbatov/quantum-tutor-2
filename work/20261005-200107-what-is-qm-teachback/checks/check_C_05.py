# Claim: crossed filters pass nothing; with 45° between: "1/2 x 1/2 x 1/2 = 1/8"
# Also: "A classical wave of bright light also gives one-eighth" (Malus's law)
import numpy as np
rng=np.random.default_rng(1)
def P(deg):
    t=np.radians(deg); v=np.array([np.sin(t),np.cos(t)]); return np.outer(v,v)
def chain(angles):
    rho=np.eye(2)/2; tot=1.0
    for a in angles:
        p=np.trace(P(a)@rho); tot*=p
        if p<1e-15: return 0.0
        rho=P(a)@rho@P(a)/p
    return tot
two=chain([0,90]); three=chain([0,45,90])
# classical Malus: I0/2 * cos^2(45) * cos^2(45)
malus=0.5*np.cos(np.radians(45))**2*np.cos(np.radians(45))**2
# Monte Carlo single photons
N=400000; th=rng.uniform(0,np.pi,N); alive=np.ones(N,bool); ang=th.copy()
for a in (0,45,90):
    a=np.radians(a); p=np.cos(ang-a)**2; alive&=rng.random(N)<p; ang[:]=a
mc=alive.mean()
print("two crossed:",two," three:",three," Malus classical:",malus," MC photons:",mc)
ok=two<1e-15 and abs(three-1/8)<1e-12 and abs(malus-1/8)<1e-12 and abs(mc-1/8)<0.003
print("PASS" if ok else "FAIL")
