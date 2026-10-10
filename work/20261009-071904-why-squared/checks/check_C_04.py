# Claims: two-slit "If the chance were the plain size ... or its cube, you would still get stripes,
# bright where the two hands agree and dark where they cancel"; balls: "holds trivially";
# classical wave "passes the add-and-subtract test too"; "every interference effect ... is a sum of
# conversations between pairs" (N alternatives).
import numpy as np, sympy as sp
ok = True
phi = np.linspace(0, 4*np.pi, 4001)
for p in [1,2,3]:
    I = np.abs(1+np.exp(1j*phi))**p
    maxpos = phi[np.isclose(I, I.max())]; minval = I[np.argmin(np.abs(phi-np.pi))]
    print(f"two-slit, power {p}: max {I.max():.3f} at phi=0,2pi,...; value at phi=pi: {minval:.2e}")
    ok &= np.isclose(I[0], 2**p) and minval < 1e-12
# balls: P_XY = P_X + P_Y
pA,pB,pC = sp.symbols('pA pB pC', positive=True)
lhs = (pA+pB)+(pB+pC)+(pA+pC)-(pA+pB+pC)
print("balls: pairs - singles =", sp.simplify(lhs), "; three-slit =", pA+pB+pC)
ok &= sp.simplify(lhs-(pA+pB+pC))==0
# classical real wave heights: energy ~ height^2
u = sp.symbols('u1:4', real=True)
E = lambda h: h**2
I3 = sp.expand(E(u[0]+u[1]+u[2])-E(u[0]+u[1])-E(u[1]+u[2])-E(u[0]+u[2])+E(u[0])+E(u[1])+E(u[2]))
print("classical wave I3 =", I3); ok &= I3==0
# N alternatives: |sum z|^2 = sum|z|^2 + sum_{i<j} 2Re(z_i z_j*); hence all-N from singles+pairs
rng = np.random.default_rng(2)
for N in [3,4,5,7]:
    z = rng.normal(size=N)+1j*rng.normal(size=N)
    full = abs(z.sum())**2
    pairs = sum(abs(z[i]+z[j])**2 for i in range(N) for j in range(i+1,N))
    singles = sum(abs(z)**2)
    pred = pairs - (N-2)*singles
    print(f"N={N}: |sum|^2={full:.6f}, from pairs and singles: {pred:.6f}")
    ok &= np.isclose(full, pred, rtol=1e-12)
print("PASS" if ok else "FAIL")
