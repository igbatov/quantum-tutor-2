# Claims: "secretly vertical or horizontal ... would pass only about half"; "it passes every one";
# "a vertical photon is a superposition of the two diagonals, 45° and 135°"
import numpy as np
V, H = np.array([0, 1.0]), np.array([1.0, 0])
def u(a): a = np.radians(a); return np.array([np.sin(a), np.cos(a)])
D, A = u(45), u(135)
mix = 0.5*np.outer(V, V) + 0.5*np.outer(H, H); P45 = np.outer(D, D)
p_mix = np.trace(mix @ P45); p_pure = (D @ D)**2
print("P(pass 45) mixture of V/H:", p_mix, "; 45-degree photon:", p_pure)
print("V and H each pass 45 filter with:", (V@D)**2, (H@D)**2)
c = np.array([V@D, V@A]); recon = c[0]*D + c[1]*A
print("V = %.4f*D + %.4f*A, error %.1e" % (c[0], c[1], np.linalg.norm(recon-V)))
ok = abs(p_mix-0.5) < 1e-12 and abs(p_pure-1) < 1e-12 and np.allclose([(V@D)**2, (H@D)**2], 0.5) and np.linalg.norm(recon-V) < 1e-12 and np.all(np.abs(c) > 0.1)
print("PASS" if ok else "FAIL")
