VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "spiral into the nucleus in about a hundred-billionth of a second" | PASS | checks/check_C_01.py: classical Larmor collapse from the Bohr radius, t = a0^3/(4 r_e^2 c) = 1.56e-11 s |
| 2 | "E_n = -13.6/n^2 ... (-13.6, -3.40, -1.51, -0.85, -0.54, -0.38)" (figure spec) | PASS | checks/check_C_02.py: CODATA with reduced mass gives -13.598, -3.400, -1.511, -0.850, -0.544, -0.378 eV |
| 3 | "hydrogen's energies crowd together toward the top, while a string's frequencies are evenly spaced" | PASS | checks/check_C_02.py: H gaps 10.20, 1.89, 0.66, 0.31, 0.17 eV (strictly shrinking); string f_n = n f_1 (spacing constant) |
| 4 | "rung 3 to rung 2 gives hydrogen's red line (wavelength 656 nanometers)" | PASS | checks/check_C_03.py: 656.47 nm vacuum, 656.29 nm air; photon 1.889 eV = 13.6(1/4-1/9) eV (consistent with E = hf) |
| 5 | "rung 4 to rung 2 its blue-green one"; figure 486/434/410 nm | PASS | checks/check_C_03.py: air wavelengths 486.14, 434.05, 410.18 nm (claimed 486.1, 434.0, 410.2) |
| 6 | "bigger drops make bluer light" | PASS | checks/check_C_03.py: wavelength decreases monotonically as the upper rung goes 3 to 6 |
| 7 | rung 2 to rung 1 "ultraviolet (invisible)" | PASS | checks/check_C_03.py: 121.6 nm (Lyman-alpha) |
| 8 | Guitar-string modes n = 1, 2, 3 fit; "2.5 humps ... sits at height 1" at x = 1 | PASS | checks/check_C_04.py: sin(n pi) = 0 for n = 1, 2, 3, with 1, 2, 3 humps; sin(2.5 pi) = 1 exactly |
| 9 | "The bottom rung is the best balance of the two" (squeezing vs. pull) | PASS | checks/check_C_05.py: minimizing hbar^2/(2 m a^2) - k/a gives a = a0 = 5.29e-11 m and E = -13.606 eV |
| 10 | "lowest state the cloud is a round ball"; "size of that number, squared, gives the chance" | PASS | checks/check_C_05.py: psi_100 = exp(-r/a0)/sqrt(pi a0^3) has no angle dependence and integral of psi^2 = 1 |
| 11 | "measure its speed and you'd find it moving fast" | PASS | checks/check_C_05.py: <p^2> = hbar^2/a0^2, so the rms speed is 2.19e6 m/s = alpha c ~ 0.7% of c |
| 12 | "only certain patterns are steady, keeping their shape with one definite energy" | PASS | checks/check_C_05.py: |psi exp(-iEt/hbar)|^2 is independent of t |
| 13 | Check yourself: three rungs give at most 3 colors | PASS | checks/check_C_06.py: 3 pairs (2->1, 3->1, 3->2) with distinct gaps 1.89, 10.2, 12.09 eV |

## Figures
- c-standing-waves: figures/c-standing-waves.png (checks/fig_c-standing-waves.py; sin(n pi x) for n = 1, 2, 3 with dashed mirror images, plus the 2.5-hump red row with an X at (1, 1))
- c-ladder-spectrum: figures/c-ladder-spectrum.png (checks/fig_c-ladder-spectrum.py; the ladder is to scale from CODATA; arrow wavelengths are computed from the Rydberg formula with air index 1.000277; the line strip is at 410.2, 434.0, 486.1, 656.3 nm; the rainbow strip is schematic, as requested)

## Notes
- Quoted wavelengths are air values (656.3, 486.1 ...). Vacuum values are about 0.2 nm longer (656.5, 486.3). Both round to the text's "656 nm".
- Check-yourself answer: 3 photon energies. For hydrogen's actual rungs 1 to 3, only 3->2 is visible; 2->1 and 3->1 are ultraviolet. "Colors of light" is fine for a generic ladder, but if the learner answers with hydrogen in mind, "different photon energies (some may be invisible)" is the safer wording.
- The collapse time of 1.6e-11 s rounds to "a hundred-billionth of a second" at the order-of-magnitude level the text intends.
