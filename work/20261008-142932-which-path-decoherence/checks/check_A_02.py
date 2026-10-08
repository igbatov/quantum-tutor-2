# Claim: "first pulse puts ... half-and-half mix of A and B; ... deflected part ... flipped
# in sign; second pulse turns 'halves alike' into A and 'halves opposite' into B."
import sympy as sp
A = sp.Matrix([1, 0]); B = sp.Matrix([0, 1])
R = sp.Matrix([[1, -1], [1, 1]]) / sp.sqrt(2)         # pi/2 pulse, A -> (A+B)/sqrt2
mix = R * A
print("after pulse 1:", list(mix))
straight = mix
deflected = sp.diag(1, -1) * mix                         # relative sign flip on deflected part
R2 = R.T                                                  # second pi/2 pulse with opposite phase (= R^-1)
s_out = sp.simplify(R2 * straight); d_out = sp.simplify(R2 * deflected)
print("straight ->", list(s_out), " deflected ->", list(d_out))
ok = (s_out == A) and (d_out == B or d_out == -B) and sp.simplify((s_out.T*d_out)[0]) == 0
# (deflected -> -B is state B up to an overall sign, physically the same state)
# with identical second pulse (same phase) the labels just swap; orthogonality is what matters
s2 = sp.simplify(R*straight); d2 = sp.simplify(R*deflected)
print("same-phase second pulse: straight ->", list(s2), " deflected ->", list(d2), " overlap", (s2.T*d2)[0])
print("PASS" if ok else "FAIL")
