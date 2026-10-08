# Claim: "whichever direction you choose to measure the partner's polarization along, the
# result tells you the slit photon's polarization along that same direction."
# Walborn et al. 2002 used |Psi+> = (|H>s|V>p + |V>s|H>p)/sqrt2 (type-II SPDC).
import numpy as np
H = np.array([1, 0]); V = np.array([0, 1])
def lin(a): return np.array([np.cos(a), np.sin(a)])
states = {"Psi+ (Walborn)": (np.kron(H, V)+np.kron(V, H))/np.sqrt(2),
          "Phi+": (np.kron(H, H)+np.kron(V, V))/np.sqrt(2),
          "Psi- (singlet)": (np.kron(H, V)-np.kron(V, H))/np.sqrt(2)}
results = {}
for nm, psi in states.items():
    worst = 1.0
    for a in np.radians(np.arange(0, 180, 7.5)):
        # partner passes polarizer at angle a; ask: slit photon's result along same axis a (pass / block)
        p_part = np.kron(np.eye(2), np.outer(lin(a), lin(a)))  # order: slit (x) partner
        post = p_part @ psi; post /= np.linalg.norm(post)
        ps = abs(np.vdot(np.kron(lin(a), lin(a)), post))**2 + 0  # slit passes at a
        determinacy = max(ps, 1-ps)
        if determinacy < worst: worst, wa = determinacy, np.degrees(a)
    results[nm] = worst
    print(f"{nm}: worst-case certainty of slit result along partner's axis = {worst:.3f} (at {wa:.1f} deg)")
# for the axes actually used in the text (0, 90, +45, -45):
psi = states["Psi+ (Walborn)"]
for a in np.radians([0, 90, 45, -45]):
    p_part = np.kron(np.eye(2), np.outer(lin(a), lin(a))); post = p_part@psi; post /= np.linalg.norm(post)
    ps = abs(np.vdot(np.kron(lin(a), lin(a)), post))**2
    print(f"Psi+: partner passes {np.degrees(a):+.0f} -> slit photon passes same axis with prob {ps:.3f}")
ok = results["Psi+ (Walborn)"] > 1-1e-9
print("PASS" if ok else "FAIL  (true for Phi+ or the singlet, and for Psi+ only for H/V and +-45 deg axes; at 22.5 deg it is 50/50)")
