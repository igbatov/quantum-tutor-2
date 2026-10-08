# Claim: "about one photon per atom on average" ... visibility "nearly gone when d reaches
# about half a photon wavelength". Also: sorted groups "all ... add up to the stripe-free total".
import numpy as np
c = lambda r: np.sinc(2*r)
for nbar in [1.0, 2.0, 3.0]:
    V = np.exp(-nbar*(1-c(0.5)))   # Poisson-averaged visibility at d = lam/2, c = 0
    print(f"Poisson mean {nbar}: relative visibility at d=lam/2 = {V:.3f}; at revival d=0.715 lam: {np.exp(-nbar*(1-abs(c(0.715)))):.3f}")
print("exactly one photon per atom: visibility at d=lam/2 =", round(abs(c(0.5)),3))
# Recoil sorting: each recoil k_x in [-k,k] uniform (isotropic); group pattern 1+cos(2pi u + k_x d)
u = np.linspace(-1, 1, 2001); kd = 2*np.pi*0.25
kx = np.linspace(-1, 1, 4001)
tot = np.mean([1+np.cos(2*np.pi*u + q*kd) for q in kx], axis=0)
Vt = (tot.max()-tot.min())/(tot.max()+tot.min())
print(f"d=lam/4: each sorted group has V=1, their sum has V={Vt:.3f} (not stripe-free)")
fail = np.exp(-1) > 0.2
print("FAIL: with mean one photon (Poisson) the model minimum is ~0.37, not 'nearly gone'; groups sum to the faded (not always stripe-free) total" if fail else "PASS")
