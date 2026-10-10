# Claim: "H ... keeps the total chance"; "H is a reflection"; sign-free matrix
# "would send the input (1,-1)/sqrt2 to (0,0)".
import sympy as sp
u, v = sp.symbols('u v')
H = sp.Matrix([[1, 1], [1, -1]])/sp.sqrt(2)
ub, vb = sp.conjugate(u), sp.conjugate(v)
lhs = sp.expand((u+v)*(ub+vb) + (u-v)*(ub-vb))
ok1 = sp.simplify(lhs - 2*(u*ub + v*vb)) == 0
ok2 = sp.simplify(H.T*H - sp.eye(2)) == sp.zeros(2)       # real orthogonal = unitary
ok3 = H.det() == -1                                        # reflection
ok4 = H == H.T and sp.simplify(H*H) == sp.eye(2)
N = sp.Matrix([[1, 1], [1, 1]])/sp.sqrt(2)
out = N*sp.Matrix([1, -1])/sp.sqrt(2)
ok5 = out == sp.zeros(2, 1)
Hv = H*sp.Matrix([u, v])
ok6 = sp.simplify(Hv - sp.Matrix([u+v, u-v])/sp.sqrt(2)) == sp.zeros(2, 1)
print('norm identity', ok1, '| unitary', ok2, '| det', H.det(), '| involution', ok4, '| sign-free kills', out.T, '| H action', ok6)
print('PASS' if all([ok1, ok2, ok3, ok4, ok5, ok6]) else 'FAIL')
