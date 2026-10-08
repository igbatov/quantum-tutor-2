VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "spiral into the nucleus in about a hundred-billionth of a second" | PASS | checks/check_B_01.py: Larmor collapse time a0^3/(4 r_e^2 c) = 1.56e-11 s |
| 2 | "As it fell it would circle ever faster" | PASS | checks/check_B_01.py: omega ∝ r^(-3/2), rises from 4.1e16 to 4.1e19 rad/s as r goes a0 to a0/100 |
| 3 | "E_n = -13.6/n^2 eV ... -13.6, -3.40, -1.51, -0.85, -0.54, -0.38" (figure spec) | PASS | checks/check_B_02.py: CODATA with reduced mass gives 13.598 eV; all six values match to rounding |
| 4 | "656, 486, 434 and 410 nanometres" | PASS | checks/check_B_03.py: Rydberg formula n=3..6 → 2 gives 656.29, 486.14, 434.05, 410.18 nm (air) |
| 5 | "122 nm: ultraviolet, invisible" (figure spec) | PASS | checks/check_B_03.py: 2→1 = 121.57 nm; every drop to rung 1 is ≤ 121.6 nm, below 380 nm |
| 6 | "bigger drops give higher frequencies, towards blue and violet" | PASS | checks/check_B_03.py: gaps 1.89, 2.55, 2.86, 3.02 eV ↔ wavelengths decreasing |
| 7 | "$E = hf$ ... a fixed energy gap means a fixed frequency" | PASS | checks/check_B_04.py: [h f] = J (sympy units); 1.89 eV gap → 4.57e14 Hz → 656 nm |
| 8 | "must fit a whole number of half-waves" (guitar string) | PASS | checks/check_B_05.py: sin(nπx/L) vanishes at 0 and L iff L = nλ/2 |
| 9 | "its energy is set by its shape alone" | PASS | checks/check_B_11.py: <H>/<ψ|ψ> independent of overall scale c; depends only on shape parameter a; minimum at a = Bohr radius, E = -13.6 eV |
| 10 | "close in, that cost grows faster than the pull" | PASS | checks/check_B_06.py: ħ²/(2mr²) ÷ ke²/r → ∞ as r → 0 |
| 11 | "roughly a ten-billionth of a metre across" | PASS | checks/check_B_06.py: balance minimum r = a0 = 5.29e-11 m, diameter 1.06e-10 m |
| 12 | "Squeezing a wave ... forces it to mix many wavelengths" / uncertainty | PASS | checks/check_B_07.py: FFT of Gaussian packets, σx halved → σp doubled, σxσp = ħ/2 (minimum) |
| 13 | "opening the second slit *lowers* the number of hits" at a dark stripe | PASS | checks/check_B_08.py: one slit P = 0.50, both slits P = 8e-9 (sum of chances would give 1.0) |
| 14 | "no plan agreed in advance ... could produce, yet never ... sends a message" | PASS | checks/check_B_09.py: singlet CHSH = 2.8284 = 2√2 > 2 (max over local plans); Bob's marginals = 0.5 for each Alice setting; Schmidt rank 2 (not a product) |
| 15 | Check yourself: smaller quantum dot → bluer | PASS | checks/check_B_10.py: box gap ∝ 1/L²; 6 → 3 nm raises E2−E1 fourfold, so emitted wavelength gets shorter |

## Figures
- b-ladder-and-lines: figures/b-ladder-and-lines.png (script checks/fig_b-ladder-and-lines.py). The rung energies and line wavelengths are computed from CODATA via the Rydberg formula, not typed in. The wavelength labels sit under rung 2 with colour names ("656 nm red", etc.) so the figure does not rely on colour alone. Rungs 4–6 share one bracket label.

## Notes
- The quoted wavelengths are air values (656.3, 486.1, 434.0, 410.2). Vacuum values are about 0.1–0.2 nm longer, which rounds to the same integers except 656.47 → 656. That is fine either way.
- "486 nm blue-green": this sits on the cyan/blue boundary, so the label is reasonable.
- Claim 1 is the standard non-relativistic Larmor estimate starting from r = a0. The text's "about" covers the factor of 1.5.
- The text's "roughly a ten-billionth of a metre across" matches the diameter 2a0. The radius is 0.53e-10 m, so the claim holds for either reading at order-of-magnitude level.
- Not checked by computation (conceptual or empirical): rock ages, neon colours, decoherence remark, and the interpretation questions.
