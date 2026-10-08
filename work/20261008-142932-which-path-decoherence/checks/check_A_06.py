# Claims (Exp. 2 a-d): (b) plates in: no stripes; (c) partner +45: stripes; -45: "stripes again,
# shifted by half a stripe spacing"; "the two groups together are exactly the smooth pattern of (b)";
# "never ... stripes ... whatever is done to the partner"; (d) time order changes nothing.
# Also the Check-yourself (partner at horizontal): what that group shows.
import numpy as np
def rot(t): return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
def qwp(t): return rot(t) @ np.diag([1, 1j]) @ rot(-t)
H = np.array([1, 0]); V = np.array([0, 1])
J1, J2 = qwp(np.pi/4), qwp(-np.pi/4)
X = np.linspace(-12, 12, 24001)
S = np.sinc(X/4)**2                      # np.sinc(x)=sin(pi x)/(pi x) -> sinc^2(pi X/4), d=4a
amp = np.sqrt(S/2)
psi1 = amp*np.exp(1j*np.pi*X); psi2 = amp*np.exp(-1j*np.pi*X)
def vis(P, w=None):
    # stripe contrast = amplitude of the cos term relative to the envelope: P = n*S*(1+V cos(..))
    m = np.abs(X) < 3.5
    r = P[m]/S[m]; return (r.max()-r.min())/(r.max()+r.min())
def pattern(state_name, plates, partner_vec=None):
    # joint state: sum over polarization pairs; slit pol vector depends on partner's pol (Psi+ or Phi+)
    pairs = [(V, H), (H, V)] if state_name == "Psi+" else [(H, H), (V, V)]
    P = np.zeros_like(X)
    basis = [partner_vec] if partner_vec is not None else [H, V]
    for pv in basis:
        field = np.zeros((2, X.size), complex)
        for sv, partner in pairs:
            c = np.vdot(pv, partner)/np.sqrt(2)
            a1 = (J1 @ sv) if plates else sv; a2 = (J2 @ sv) if plates else sv
            field += c*(np.outer(a1, psi1) + np.outer(a2, psi2))
        P += np.sum(np.abs(field)**2, axis=0)
    return P
ok = True
for st in ["Psi+", "Phi+"]:
    Pa = pattern(st, False); Pb = pattern(st, True)
    p45 = np.array([1, 1])/np.sqrt(2); m45 = np.array([1, -1])/np.sqrt(2)
    Pc1 = pattern(st, True, p45); Pc2 = pattern(st, True, m45)
    PH = pattern(st, True, H)
    print(f"[{st}] visibility (a) {vis(Pa):.3f}  (b) {vis(Pb):.3f}  (c+45) {vis(Pc1):.3f}  (c-45) {vis(Pc2):.3f}  partner-H group {vis(PH):.3f}")
    print(f"[{st}] max|(c+45)+(c-45)-(b)| = {np.max(np.abs(Pc1+Pc2-Pb)):.2e};  max|(b)-S| = {np.max(np.abs(Pb-S)):.2e}")
    # shift between the two groups: location of peak nearest centre
    m = np.abs(X) <= 0.5
    x1 = X[m][np.argmax(Pc1[m]/S[m])]; x2 = X[m][np.argmax(Pc2[m]/S[m])]
    shift = abs(((x1-x2)+0.5) % 1 - 0.5)
    print(f"[{st}] peak positions +45: {x1:+.3f}, -45: {x2:+.3f}; separation mod 1 = {shift:.3f}")
    # any partner basis: groups sum to (b)
    rng = np.random.default_rng(1); worst = 0
    for _ in range(50):
        u = rng.normal(size=2)+1j*rng.normal(size=2); u /= np.linalg.norm(u)
        w = np.array([-np.conj(u[1]), np.conj(u[0])])
        worst = max(worst, np.max(np.abs(pattern(st, True, u)+pattern(st, True, w)-Pb)))
    print(f"[{st}] random partner bases: worst |sum - (b)| = {worst:.2e}")
    ok &= vis(Pa) > 0.99 and vis(Pb) < 1e-3 and vis(Pc1) > 0.99 and vis(Pc2) > 0.99 \
          and np.max(np.abs(Pc1+Pc2-Pb)) < 1e-12 and abs(shift-0.5) < 0.01 and worst < 1e-12
# (d) time order: operators on partner commute with any operator on slit photon
A = np.kron(np.random.rand(2, 2), np.eye(2)); B = np.kron(np.eye(2), np.random.rand(2, 2))
print("commutator norm slit-op vs partner-op:", np.linalg.norm(A@B-B@A))
print("PASS" if ok else "FAIL")
