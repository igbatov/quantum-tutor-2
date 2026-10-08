# Claim: with which-slit record "one smooth hump, ... two one-slit patterns added together";
# "probabilities add instead, and nothing can cancel"
import numpy as np
rng = np.random.default_rng(0)
u = np.linspace(-2, 2, 4001)
A = np.sinc(u)
psiL = A*np.exp(-1j*5*np.pi*u); psiR = A*np.exp(1j*5*np.pi*u)
P_incoh = np.abs(psiL)**2 + np.abs(psiR)**2
P_coh = np.abs(psiL+psiR)**2
# no cos^2 fringes: incoherent pattern equals 2 sinc^2 exactly; interior of central lobe is single hump
hump = np.allclose(P_incoh, 2*np.sinc(u)**2)
c = (u > -1) & (u < 1)
d = np.diff(P_incoh[c]); sign_changes = np.sum(np.diff(np.sign(d[np.abs(d) > 1e-14])) != 0)
# visibility of coherent fringes near centre vs incoherent
print("incoherent == 2 sinc^2:", hump, "; extrema inside central lobe:", sign_changes)
print("coherent min/max in |u|<0.5:", P_coh[np.abs(u)<0.5].min().round(6), P_coh[np.abs(u)<0.5].max().round(6))
# "nothing can cancel": sum of non-negative terms >= each term
nocancel = np.all(P_incoh >= np.abs(psiL)**2 - 1e-15)
# Optional (check-yourself answer, not a claim in text): half recorded -> fringe visibility 1/2
P_half = 0.5*P_coh + 0.5*P_incoh
uc = np.abs(u) < 0.2
V = (P_half[uc].max()-P_half[uc].min())/(P_half[uc].max()+P_half[uc].min())
print("half-recorded visibility near centre ~", round(V, 3), "(info only)")
print("PASS" if hump and sign_changes == 1 and nocancel else "FAIL")
