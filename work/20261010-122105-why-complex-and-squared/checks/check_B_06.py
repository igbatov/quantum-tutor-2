# Claims (Model 1): "|psi|^2 = ... = A^2" for psi = A e^{-i theta};
#  "1/2|c1+c2|^2 = 1/2(a^2 + b^2 + 2ab cos((w2-w1)t))": one beat at the difference frequency;
#  real attempt "(c1+c2)^2 = a^2/2(1+cos 2w1t) + b^2/2(1+cos 2w2t) + ab[cos(w1-w2)t + cos(w1+w2)t]";
#  "with some fixed unequal shares, which changes only the depth of the beat".
import sympy as sp
import numpy as np
A, a, b, t, w1, w2, th = sp.symbols('A a b t omega1 omega2 theta', real=True)
ok = True
psi = A * sp.exp(-sp.I * th)
r = sp.simplify(sp.expand(psi * sp.conjugate(psi)))
print("|psi|^2 =", r); ok &= sp.simplify(r - A**2) == 0
c1 = a * sp.exp(-sp.I * w1 * t); c2 = b * sp.exp(-sp.I * w2 * t)
chance = sp.Rational(1, 2) * (c1 + c2) * sp.conjugate(c1 + c2)
target = sp.Rational(1, 2) * (a**2 + b**2 + 2*a*b*sp.cos((w2 - w1)*t))
d = sp.simplify(sp.expand_complex(sp.expand(chance - target)))
print("complex beat difference:", d); ok &= d == 0
cr1 = a*sp.cos(w1*t); cr2 = b*sp.cos(w2*t)
lhs = (cr1 + cr2)**2
rhs = a**2/2*(1+sp.cos(2*w1*t)) + b**2/2*(1+sp.cos(2*w2*t)) + a*b*(sp.cos((w1-w2)*t) + sp.cos((w1+w2)*t))
d2 = sp.simplify(sp.expand(sp.expand_trig(lhs - rhs)))
print("real-attempt expansion difference:", d2); ok &= d2 == 0
# spectrum check numerically: frequencies present
W1, W2 = 1.0, 1.3
T = np.linspace(0, 2000, 2**17); dt = T[1]-T[0]
for name, sig in [("hand", 0.5*np.abs(np.exp(-1j*W1*T)/np.sqrt(2)+np.exp(-1j*W2*T)/np.sqrt(2))**2),
                  ("real", 0.5*(np.cos(W1*T)/np.sqrt(2)+np.cos(W2*T)/np.sqrt(2))**2)]:
    S = np.abs(np.fft.rfft((sig - sig.mean()) * np.hanning(len(T))))
    fr = 2*np.pi*np.fft.rfftfreq(len(T), dt)
    peaks = fr[(S > 0.05*S.max()) & (np.r_[0, S[1:-1] > S[:-2], 0] > 0) & (np.r_[0, S[1:-1] > S[2:], 0] > 0)]
    print(name, "angular frequencies present:", np.round(peaks, 2))
# unequal shares alpha, beta: frequency still |w2-w1|; complex shares add a phase offset too
al, be = 0.8, 0.6*np.exp(0.7j)
sig = np.abs(al*np.exp(-1j*W1*T) + be*np.exp(-1j*W2*T))**2
pred = abs(al)**2 + abs(be)**2 + 2*abs(al*be)*np.cos((W2-W1)*T - np.angle(np.conj(al)*be))
print("unequal complex shares: max dev from 'depth + phase offset' formula", np.abs(sig-pred).max())
ok &= np.abs(sig-pred).max() < 1e-9
print("PASS" if ok else "FAIL")
