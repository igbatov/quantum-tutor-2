VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "fit a whole number of half-waves ... more humps sound higher" (+ figure: sin(2.5πx) ends at 1) | PASS | checks/check_B_01.py: sin(nπ)=0 for n=1,2,3; sin(2.5π)=1; hump counts 1,2,3; f_n = (n/2L)√(T/μ) rises with n, falls with L, and doesn't depend on amplitude (so plucking harder doesn't change the note) |
| 2 | "Hydrogen's visible lines are red, blue-green, blue-violet and violet" (656/486/434/410 nm) | PASS | checks/check_B_02.py: Rydberg (reduced mass, air) gives 656.29, 486.14, 434.05, 410.18 nm for n=3,4,5,6→2; all four fall in the named colour bands |
| 3 | "drops to level 1 give ultraviolet light" (figure) | PASS | checks/check_B_02.py: Lyman series spans 91.2–121.6 nm, all far below 380 nm |
| 4 | "a bigger drop gives bluer light" | PASS | checks/check_B_02.py: Balmer wavelength decreases monotonically as the upper level n increases |
| 5 | "spiral into the nucleus in roughly a hundred-billionth of a second" | PASS | checks/check_B_03.py: classical Larmor collapse time a0³/(4r_e²c) = 1.56e-11 s |
| 6 | "Squeeze the wave ... all the energies rise and the steps between them grow" | PASS | checks/check_B_04.py: particle in a box E_n ∝ n²/L²; dE/dL < 0 and d(E_{n+1}−E_n)/dL < 0 |
| 7 | "More wiggles, more energy" | PASS | checks/check_B_04.py: dE_n/dn > 0 (box); hydrogen levels rise with n (n−1 radial+angular nodes) |
| 8 | "Their energies aren't spaced like a guitar's notes" / rungs crowd toward the top | PASS | checks/check_B_04.py: hydrogen gaps 10.20, 1.89, 0.66, 0.31, 0.17, 0.10 eV (shrinking); string harmonics have equal frequency spacing |
| 9 | "a lowest pattern, the best compromise ..." | PASS | checks/check_B_05.py: variational E(a) = ħ²/(2ma²) − k/a → +∞ as a→0, minimum at a = a0 = 5.2918e-11 m with E = −13.606 eV |
| 10 | "E = hf ... more energy means higher frequency" and each drop gives one line | PASS | checks/check_B_06.py: hf at 656/486/434/410 nm = 1.889/2.551/2.857/3.023 eV, matching 13.6(1/4−1/n²) level differences to 0.1% |
| 11 | "its size is fixed because it describes exactly one electron" | PASS | checks/check_B_06.py: normalization fixes the amplitude at A = √(2/L) for a box state |
| 12 | Uncertainty is "a fact about waves" | PASS | checks/check_B_07.py: Gaussian packets of widths 0.5–5 give Δx·Δp = ħ/2 exactly (FFT); narrowing x widens p |
| 13 | "Big objects ... energy steps are far too small to notice" | PASS | checks/check_B_08.py: 1 g bead in 1 cm box, E2−E1 ≈ 1.6e-60 J; 1 m pendulum ħω ≈ 3.3e-34 J; kT(300 K) ≈ 4.1e-21 J (ratios 4e-40, 8e-14) |
| 14 | Two slits: "stripes ... dark where the waves cancel"; which-path record makes "stripes vanish" | PASS | checks/check_B_09.py: fringe visibility is 1.000 when amplitudes add and 0.000 when probabilities add (which-path), with the same total intensity |
| 15 | "neon's red-orange lines give neon signs their glow" | PASS (reference data) | checks/check_B_10.py: the 16 strongest visible Ne I lines (hard-coded NIST values) lie between 585 and 703 nm. This is a check against tabulated values, not a calculation from theory |

## Figures
- b-fits: figures/b-fits.png (script checks/fig_b-fits.py). It shows sin(nπx) for n=1–3 with faint mirror curves, clamps at both ends, and a dashed red sin(2.5πx) with a cross at x=1. Shapes and the dashed line style carry the meaning, not color alone.
- b-ladder: figures/b-ladder.png (script checks/fig_b-ladder.py). It shows E_n = −13.6/n² for n=1–6, a dashed zero line, four Balmer arrows labelled with wavelength and color name, the UV note, a continuous spectrum strip, and a hydrogen line strip with each line labelled in nm. All wavelengths are computed from the Rydberg constant.

## Notes
- "Hydrogen's visible lines are ... four": standard textbook statement. The n=7→2 line (397.0 nm) is at the very edge of human vision and usually isn't counted. That's fine at this level.
- The collapse time (~1.6e-11 s) is the standard nonrelativistic Larmor estimate starting from r = a0. "Roughly a hundred-billionth" is accurate to order of magnitude.
- The "compromise" claim is checked with a 1s trial function; it gives the exact hydrogen ground state.
- Check-yourself answer (not stated in the text): E ∝ 1/L², so a smaller dot glows bluer. This is consistent with check 6.
