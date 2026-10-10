# Claims: "|psi|^2 = ... = A^2"; "1/2|c1+c2|^2 = 1/2(a^2+b^2+2ab cos((w2-w1)t))"; real "(c1+c2)^2 = ..." expansion;
# unequal shares "changes the depth ... can shift its timing but not its frequency";
# figure: "hand rule gives 1/2(1+cos 0.1t)"; real rule "1/4(cos w1 t + cos w2 t)^2 ... pulses at w1+w2 inside the same envelope".
import sympy as sp, numpy as np
t, th, A, a, b, w1, w2 = sp.symbols('t theta A a b omega1 omega2', real=True)
ok = sp.simplify(sp.expand(A*sp.exp(-sp.I*th)*A*sp.exp(sp.I*th)) - A**2) == 0
c1, c2 = a*sp.exp(-sp.I*w1*t), b*sp.exp(-sp.I*w2*t)
chance = sp.Rational(1,2)*(c1+c2)*sp.conjugate(c1+c2)
step = sp.Rational(1,2)*(a**2+b**2+a*b*sp.exp(-sp.I*(w1-w2)*t)+a*b*sp.exp(sp.I*(w1-w2)*t))
fin = sp.Rational(1,2)*(a**2+b**2+2*a*b*sp.cos((w2-w1)*t))
ok &= sp.simplify(sp.expand(chance-step)) == 0 and sp.simplify((step-fin).rewrite(sp.cos)) == 0
r1, r2 = a*sp.cos(w1*t), b*sp.cos(w2*t)
rhs = a**2/2*(1+sp.cos(2*w1*t)) + b**2/2*(1+sp.cos(2*w2*t)) + a*b*(sp.cos((w1-w2)*t)+sp.cos((w1+w2)*t))
ok &= sp.simplify(sp.expand_trig(sp.expand((r1+r2)**2 - rhs))) == 0
# complex fixed shares alpha, beta: chance = |alpha c1 + beta c2|^2 -> only frequency w2-w1, phase shift arg
tt = np.linspace(0, 400, 2**14); W1, W2 = 1.0, 1.3
al, be = 0.8, 0.6*np.exp(0.9j)
sig = np.abs(al*np.exp(-1j*W1*tt) + be*np.exp(-1j*W2*tt))**2
F = np.abs(np.fft.rfft((sig-sig.mean())*np.hanning(len(tt)))); fr = 2*np.pi*np.fft.rfftfreq(len(tt), tt[1]-tt[0])
peaks = fr[F > 0.05*F.max()]; print("complex-share beat frequencies present:", np.unique(np.round(peaks,1)))
ok &= np.all(np.abs(peaks-0.3) < 0.05)
# figure identities, w1=1, w2=1.1, a=b=1/sqrt2
T = sp.symbols('T', real=True)
hand = sp.Rational(1,2)*sp.Abs(sp.exp(-sp.I*T)/sp.sqrt(2)+sp.exp(-sp.I*sp.Rational(11,10)*T)/sp.sqrt(2))**2
x = np.linspace(0, 20*np.pi, 20001)
handn = sp.lambdify(T, hand, 'numpy')(x)
ok &= np.allclose(handn, 0.5*(1+np.cos(0.1*x)))
real = 0.25*(np.cos(x)+np.cos(1.1*x))**2
ok &= np.allclose(real, np.cos(1.05*x)**2*np.cos(0.05*x)**2) and np.allclose(np.cos(0.05*x)**2, handn)
ok &= np.all(real <= handn + 1e-12)
print("real rule = cos^2(1.05t) [freq 2.1 = w1+w2] x envelope cos^2(0.05t) = hand rule:", ok)
print("beat period 2pi/0.1 = 20pi; peak of real rule", real.max())
print("PASS" if ok else "FAIL")
