VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "isotropic idealization: V = \|sin(2πd/λ)/(2πd/λ)\|" | PASS | checks/check_B_01.py: sympy sphere average of exp(ik n·d) gives sin(kd)/(kd) exactly |
| 2 | "first zero at d = λ/2"; "V stays above 0 for d < λ/2" | PASS | check_B_01: zero at d/λ = 0.5000; \|V\| > 0 on the whole interval (0, λ/2) |
| 3 | "weak revival near d ≈ 0.72λ (height about 0.22)" | PASS | check_B_01: maximum at d/λ = 0.7151, height 0.2172 |
| 4 | "dipole pattern changes the details ... not the half-wavelength scale" | PASS | check_B_02: first zero at 0.44λ, 0.54λ or 0.72λ depending on dipole type and orientation; stays on the half-wavelength scale |
| 5 | "about one photon per atom on average" ... visibility "nearly gone when d reaches about half a photon wavelength" | FAIL | check_B_03: with a Poisson mean of 1 photon, 37% of atoms scatter none, so the model's relative visibility at d = λ/2 is e^-1 = 0.37, not near 0 (0.14 for mean 2, 0.05 for mean 3). Near zero only if nearly every atom scatters at least one photon. Correct statement: "falls to a minimum near half a photon wavelength", or drop "on average" and say the laser was strong enough that nearly every atom scattered a photon (if that is what the paper reports). |
| 6 | "all the groups together add up to the stripe-free total" | FAIL | check_B_03: at d = λ/4 every recoil-sorted group has V = 1, but their sum has V = 0.64, not 0. The total is stripe-free only where the overlap is about 0 (d ≈ λ/2, λ, ...). Correct statement: "all the groups together add up to the faded total". |
| 7 | random-kick picture: shift "uniformly between −0.25 and +0.25 stripe spacings", average "≈ 0.64, identical" | PASS | check_B_04: projection of an isotropic direction is uniform on [−1, 1] (Monte Carlo); kick average 0.6370 vs overlap 2/π = 0.6366; sympy shows uniform-phase average equals sin(kd)/(kd) for every d |
| 8 | "three scatterings with overlap 0.7 each leave 0.7×0.7×0.7 ≈ 0.34" | PASS | check_B_05: coherence of the explicit tensor-product recorder state = 0.3430; panel values 1, 0.7, 0.49, 0.343 |
| 9 | "average visibility is exp(−(mean number)(1 − c)), still an exponential in pressure" | PASS | check_B_05: sympy Poisson sum of c^n gives exp(−μ(1−c)) exactly |
| 10 | C70 "about 840 times the mass of a hydrogen atom" | PASS | check_B_06: 840.8 u / 1.008 u = 834 (within 1%) |
| 11 | room-temperature gas atom wavelength "a few hundredths of a nanometre", "tens of thousands of times shorter" than 1 µm | PASS | check_B_06: argon 0.023 nm (1 µm/λ = 43,000); N2 0.028 nm (36,000) |
| 12 | Talbot–Lau grating spacing "a few tens of centimetres" | PASS | check_B_06: d²/λ_dB for d = 991 nm, C70 at 100–200 m/s = 21–41 cm |
| 13 | Exp. 3: at 1,000 K "hardly any emitted photons" < 2 µm; at 3,000 K "visible and near-infrared"; short-photon number "rises steeply" | PASS | check_B_07 (black body): fraction < 2 µm is 2.1% at 1000 K, 25% at 2000 K, 49% at 3000 K; photon-number peak 3.7 → 1.2 µm; rate of < 2 µm photons ×620 from 1000 to 3000 K; hotter curves are higher at every wavelength |
| 14 | "λ/d = 20 (overlap about 0.98)"; Check-yourself photon (20 µm at 1 µm) | PASS | check_B_01: overlap 0.9836, so the stripes fade only slightly (~2%) |
| 15 | 10 µm grain in air "struck about 10^18 times per second", "within about a billionth of a billionth of a second"; mean speed "about 470 m/s" | PASS | check_B_08: n v̄/4 × 4πr² with r = 5 µm gives 9.2×10^17/s, i.e. 1.1×10^-18 s; v̄ = 463 m/s, n = 2.50×10^25 m^-3 |
| 16 | fig b-two-reasons: 1 nm ~10^10/s, 100 nm ~10^14/s; 10^-6 mbar "a billion times lower" | PASS | check_B_08: 9.2×10^9 and 9.2×10^13/s (sizes taken as diameters); 10^-6/1013 = 0.99×10^-9 |
| 17 | sunlight: "roughly 10^11 photons per second scatter off it, ... a few millionths of a millionth of a second" | FAIL | check_B_09: 1000 W/m² solar spectrum (mean photon energy 1.34 eV) gives a flux of 4.7×10^21 /m²/s; the geometric cross-section of a 10 µm grain gives 3.6×10^11/s (5×10^11 above the atmosphere), so a time of 2–3 ps. The time is right, but the rate is about 4× higher than stated, and 10^11/s would give 10 ps, which is not "a few" ps. Correct statement: "a few times 10^11 photons per second hit it, and the time is a few millionths of a millionth of a second". |
| 18 | CMB "does it by sheer numbers in about a second by the Joos–Zeh estimate" (grain "ten micrometres across", Δx = 10 µm) | FAIL | check_B_10: Joos–Zeh's Λ = 8!·8ζ(9)c a^6 (kT/ħc)^9/(9π) gives 1.6×10^6 cm^-2 s^-1 and about 0.6 s for a = 10 µm radius (their grain, 20 µm across). For the grain in the text (radius 5 µm, Λ ∝ a^6) it is 0.026/s, i.e. about 40 s, longer still with a dielectric factor below 1. This is more than the stated factor of ten. Correct statement: "in under a minute (Joos and Zeh's 'about a second' is for a grain twice as wide)". Alternatively make the grain 20 µm across, which raises the air and sunlight rates by 4×. |
| 19 | long-wavelength rule "fading rate growing as the square of the separation"; reference line (6/(2π)²)(λ/Δx)²; "flattens to about one event time once Δx exceeds about λ/2" | PASS | check_B_11: 1 − sinc x = x²/6 − x⁴/120; unsmoothed ratio to the reference is 1.0002 at Δx/λ = 0.01; for Δx/λ > 0.5 the smoothed fading time stays within 0.87–1.04 event times; at Δx/λ = 20 it is 1.000 |
| 20 | window "narrows as 1/√(number of scatterings) on the sloped part" | PASS | check_B_11: the width where N(kΔx)²/6 = 1 shrinks by 3.162 = √10 per decade of N |
| 21 | fig b-pairs-of-routes caption: factor "near 0 beyond" (for 1, 10, 100 scattering times) | FAIL | check_B_15: after 1 average scattering time the factor for resolved separations levels off at e^-1 = 0.37, not near 0. It is about 0 after 10 or 100. Correct statement: "near 0 beyond, once several scatterings have occurred (after one average scattering time it levels off at 1/e)". |
| 22 | Δx/λ marks: CMB ≈ 0.01, sunlight ≈ 20, air ≈ 5×10^5 | PASS | 10 µm/1 mm = 0.01; 10 µm/0.5 µm = 20; 10 µm/(0.02–0.028 nm) = 3.6–5×10^5 (check_B_06 wavelengths) |
| 23 | de Broglie at 100 m/s: electron ~7 µm, C70 (~1.4×10^-24 kg) ~5 pm, 10^-12 kg grain ~7×10^-24 m; 10 µm grain ≈ 10^-12 kg | PASS | check_B_12: 7.27 µm; 1.396×10^-24 kg, 4.75 pm; 6.6×10^-24 m; 10 µm sphere at 2000 kg/m³ = 1.05×10^-12 kg |
| 24 | grain at 1 mm/s: "under a billionth of a nanometre, a thousand times smaller than an atomic nucleus" | PASS | check_B_12: λ = 6.6×10^-19 m < 10^-18 m; 10^-15 m / λ = 1500 |
| 25 | microwave kick "about a hundred thousand times smaller" than the splitting laser's | PASS | check_B_13: 2ħk Bragg kick at 780 nm vs one microwave photon: 1.1×10^5 (87Rb, 6.8 GHz) to 2.5×10^5 (85Rb, 3.0 GHz) |
| 26 | "total number of arrivals is the same in all four panels"; V = 0 pattern = "two one-path chances added"; "quarter of the strength (amplitude halved)" | PASS | check_B_14: full-screen integrals 3.9996 for V = 1, 0.7, 0.49, 0.343 (sinc² envelope transform vanishes at the stripe frequency); V = 0 equals the envelope; 0.5² = 0.25 |

PASS 21 / 26, FAIL 5.

## Figures
- b-one-photon: figures/b-one-photon.png
- b-many-records: figures/b-many-records.png
- b-hot-molecule: figures/b-hot-molecule.png (right panel on a log vertical axis so all three curves are visible on one common scale)
- b-dust-grain: figures/b-dust-grain.png
- b-rules-out: figures/b-rules-out.png
- b-recorders-multiply: figures/b-recorders-multiply.png
- b-pairs-of-routes: figures/b-pairs-of-routes.png. The N = 1 curve visibly levels off at 1/e (marked with a dotted line), which contradicts the caption's "near 0 beyond" (row 21).
- b-does-it-explain-the-dot: figures/b-does-it-explain-the-dot.png (schematic)
- b-two-reasons: figures/b-two-reasons.png

## Notes
- Smoothing over λ ± 30% puts the small-Δx part of the dust-grain curve 9% below the dashed reference line (the average of 1/λ² is 1/(0.7·1.3)). The curve dips to about 0.87 event times near Δx/λ ≈ 0.7 before flattening at 1. Both are minor, but the learner checks figures closely.
- Row 5 concerns the text's own model. Whether the 1995 data actually went near zero depends on the real photon-number distribution, which I could not check offline.
- Sunlight (row 17): a 10 µm grain scatters much of the light into a forward diffraction lobe of angle about λ/a, and those photons only partly resolve Δx = a. "One impact = complete record" is therefore an overestimate for that part, which is within the stated factor-of-ten roughness.
- Experimental values (pressure range, temperatures, 1999 grating period, Brune 1996, Fein 2019 size) were not checkable by computation and were not scored.
