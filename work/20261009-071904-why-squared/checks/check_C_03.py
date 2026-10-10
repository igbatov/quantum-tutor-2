# Claim: worked arithmetic at centre and "half a stripe out" for size^1,^2,^3,^4.
# e.g. "3² = 9; the pairs give 2² + 2² + 2² = 12"; "27 against 24 − 3 = 21"
import numpy as np
def compute(hands, p):
    A,B,C = hands
    P = lambda z: abs(z)**p
    three = P(A+B+C); pairs = P(A+B)+P(B+C)+P(A+C); singles = P(A)+P(B)+P(C)
    return three, pairs, singles, pairs-singles
centre = (1,1,1)
# dark line of AB, half a stripe out: phase step pi between neighbouring slits
phi = np.pi
half = tuple(np.exp(1j*phi*k) for k in range(3))   # (1,-1,1), same as (-1,1,-1) up to overall sign
print("hands half a stripe out (phase pi per slit):", np.round(half,12), "-> text uses (-1,+1,-1), equivalent")
expected = {  # (p, spot): (three, pairs, singles, pairs-singles) as stated in text
 (2,'c'):(9,12,3,9), (2,'h'):(1,4,3,1),
 (1,'c'):(3,6,3,3), (1,'h'):(1,2,3,-1),
 (3,'c'):(27,24,3,21), (3,'h'):(1,8,3,5),
 (4,'c'):(81,48,3,45),
}
ok = True
for (p,s),e in expected.items():
    got = compute(centre if s=='c' else half, p)
    good = np.allclose(got, e, atol=1e-12)
    ok &= good
    print(f"p={p} {'centre' if s=='c' else 'half  '}: three={got[0]:.3f} pairs={got[1]:.3f} singles={got[2]:.3f} pairs-singles={got[3]:.3f}  text {e}  {'ok' if good else 'MISMATCH'}")
# pair-by-pair statements half a stripe out: AB and BC cancel, A and C agree
h = (-1,1,-1)
print("half: |AB|,|BC|,|AC| =", abs(h[0]+h[1]), abs(h[1]+h[2]), abs(h[0]+h[2]), " total", h[0]+h[1]+h[2])
ok &= abs(h[0]+h[1])==0 and abs(h[1]+h[2])==0 and abs(h[0]+h[2])==2
# "The cube and every higher power fail even at the centre": 3^p - 3*2^p + 3 != 0 for p>2
ps = np.linspace(2.0001, 20, 20000)
f = 3**ps - 3*2**ps + 3
print("centre leftover 3^p-3*2^p+3 for p in (2,20]: min =", f.min())
ok &= np.all(f > 0)
# "plain size passes wherever all the hands line up": lengths add
rng = np.random.default_rng(0); L = rng.uniform(0,5,size=(1000,3))
lo = L.sum(1) - (L[:,0]+L[:,1]) - (L[:,1]+L[:,2]) - (L[:,0]+L[:,2]) + L.sum(1)
print("aligned plain-size leftover max |.| =", np.abs(lo).max()); ok &= np.abs(lo).max()<1e-12
print("PASS" if ok else "FAIL")
