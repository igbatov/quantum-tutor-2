# Claim (pilot-wave): outcome "fixed by exactly where in the beam it started and how the magnet is set"
# Uses the Bohmian SG model of check_B_10_2 (same parameters) for Z-up atoms: Z magnet vs X magnet vs reversed magnet.
import numpy as np, importlib.util, sys, os
spec=importlib.util.spec_from_file_location("b10",os.path.join(os.path.dirname(__file__),"check_B_10_2.py"))
import io, contextlib
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    b10=importlib.util.module_from_spec(spec); spec.loader.exec_module(b10)
ok=True
zs,zt_Z=b10.run(1.0)      # Z-up atom, Z magnet: whole wave in upper packet
_,zt_X=b10.run(0.5)       # Z-up atom, X magnet: equal pieces
fZ=(zt_Z>0).mean(); fX=(zt_X>0).mean()
print(f"Z magnet: fraction to upper side {fZ:.3f}; X magnet: {fX:.3f}")
i=np.argmin(abs(zs+0.5)); print(f"start z0={zs[i]:.3f}: Z magnet ends {zt_Z[i]:+.2f}, X magnet ends {zt_X[i]:+.2f}")
ok &= fZ==1.0 and abs(fX-0.5)<0.01 and zt_Z[i]>0 and zt_X[i]<0
# reversed field: (F -> -F) is equivalent to swapping pieces; trajectories don't cross, so upper starts still go
# to the upper side, which is now the 'down'-answer packet: answer depends on magnet setting
print("same start, different magnet setting -> different answer")
print("in-principle unpredictability rests on quantum equilibrium (positions distributed as |psi|^2); a postulate, not computed")
print("PASS" if ok else "FAIL")
