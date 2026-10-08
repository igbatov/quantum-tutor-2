# Claim: "first pulse mixes A and B half-and-half; ... deflected part's mix ... one half flipped in
# sign ...; second pulse un-mixes, which sends the unflipped mix back to A and the flipped mix to B."
import sympy as sp
A = sp.Matrix([1, 0]); B = sp.Matrix([0, 1])
R = sp.Matrix([[1, -1], [1, 1]])/sp.sqrt(2)      # pi/2 pulse
mix = R*A; flipped = sp.diag(1, -1)*mix
Rinv = R.inv()                                   # "un-mixes"
s_out = sp.simplify(Rinv*mix); d_out = sp.simplify(Rinv*flipped)
print("mix =", list(mix), " flipped =", list(flipped))
print("unflipped -> ", list(s_out), " flipped -> ", list(d_out), " overlap", sp.simplify((s_out.H*d_out)[0]))
ok = s_out == A and (d_out == B or d_out == -B)
print("PASS" if ok else "FAIL")
