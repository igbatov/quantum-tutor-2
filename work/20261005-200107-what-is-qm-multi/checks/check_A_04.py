# Claim: Planck's constant "about 6.6 x 10^-34 ... (joule-seconds)"; E = hf (dims J = J s * 1/s)
from scipy.constants import h
print("h =", h, "J s")
print("PASS" if abs(h-6.6e-34)/6.6e-34 < 0.01 else "FAIL")
