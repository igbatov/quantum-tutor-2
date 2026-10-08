# Claim: "neon's red-orange lines give neon signs their glow" (reference data, not derivable here)
# Strong visible Ne I lines (NIST ASD, air wavelengths, nm), hard-coded:
ne = [585.25, 588.19, 594.48, 607.43, 609.62, 614.31, 616.36, 621.73, 626.65, 633.44, 638.30, 640.22, 650.65, 659.90, 692.95, 703.24]
inband = [l for l in ne if 585 <= l <= 705]
print(f"{len(inband)}/{len(ne)} strongest listed Ne lines lie 585-705 nm (yellow-orange to red)")
print("PASS (against tabulated reference values)" if len(inband) == len(ne) else "FAIL")
