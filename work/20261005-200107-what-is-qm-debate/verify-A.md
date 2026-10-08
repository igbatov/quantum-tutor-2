VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "Lined up ... 4 units: twice the 2"; "opposite ... 0 units" | PASS | checks/check_A_01.py: sympy gives \|1\|²=1, \|1+1\|²=4, \|1−1\|²=0, 1+1=2, ratio 4/2=2 |
| 2 | "Averaged across the bands, the chance comes back to 2 units" | PASS | checks/check_A_02.py: \|1+e^{iφ}\|²=2+2cosφ, mean over a period = 2 exactly; with the figure envelope, area of 4S·cos²(πx) vs 2S over [−6,6] differ by 0.04% |
| 3 | "opening the second slit drops the hits almost to zero" / "a second slit could only add hits" | PASS | checks/check_A_03.py: added chances 2S ≥ S everywhere; at x=0.5 one slit = 0.968 ("about 1"), two slits = 0; solid/dotted = 2 at every bright band |
| 4 | "wavelength ... shorter for faster electrons"; momentum "mass times velocity" | PASS | checks/check_A_04.py: λ = h/p decreases monotonically with v (7.3 nm at 10⁵ m/s down to 1.6 pm at 2.5×10⁸ m/s, relativistic); p = mv holds non-relativistically |
| 5 | "Nobody has to read the record; it only has to exist" | PASS | checks/check_A_05.py: P = \|a\|²+\|b\|²+2Re(ab*⟨r_b\|r_a⟩); orthogonal record gives a flat pattern (min=max=1) without any readout; the electron's reduced state is I/2; partial overlap 0.5 gives partial fringes |
| 6 | "a confined wave must mix many wavelengths" (uncertainty) | PASS | checks/check_A_06.py: FFT widths for Gaussians give Δx·Δk = 0.500; for cosine-in-box shapes 0.568; narrowing x widens k in proportion |
| 7 | "squeezing ... more energy of motion, a cost that balances the nucleus's pull" | PASS | checks/check_A_07.py: minimising ħ²/(2mr²) − e²/(4πε₀r) gives r = a₀ = 5.29×10⁻¹¹ m and E = −13.606 eV |
| 8 | "spiralling in within about a hundred-billionth of a second" | PASS | checks/check_A_08.py: classical Larmor collapse t = a₀³/(4r_e²c) = 1.56×10⁻¹¹ s |
| 9 | "one sharp colour per kind of drop" | PASS | checks/check_A_09.py: hydrogen n→2 drops give 656.47, 486.27, 434.17, 410.29 nm (vacuum), matching NIST within 0.2 nm |
| 10 | "no answers agreed in advance ... could reproduce"; "no message can be sent" | PASS | checks/check_A_10.py: Bell-state CHSH = 2.828 = 2√2 vs best pre-agreed strategy = 2; Bob's reduced state is I/2 whether Alice measures Z or X |
| 11 | "amplitudes change over time in a fully predictable way" | PASS | checks/check_A_11.py: e^{−iHt} is unitary, preserves norm (1.0) and gives identical results on repeat |
| 12 | Check question: long arrow + short arrow, dark bands still dark? | PASS | checks/check_A_12.py: P = a²+b²+2ab·cosφ, minimum (a−b)² > 0 for a≠b (e.g. 1/4 for a=1, b=1/2); the question is well-posed and the answer is "no" |
| 13 | "Interference ... even 2,000-atom molecules" | UNVERIFIABLE | checks/check_A_13.py: this is a literature fact and can't be computed. It is consistent with Fein et al., Nature Physics 15, 1242 (2019): up to ~2,000 atoms, >25,000 amu, λ_dB ~ 6×10⁻¹⁴ m |

## Figures
- a-dot-buildup: figures/a-dot-buildup.png (checks/fig_a-dot-buildup.py; rejection sampling from cos²(πx)·sinc²(x/5), seed 12345, dot size shrinks with count; the caption says the dots are simulated)
- a-one-vs-two: figures/a-one-vs-two.png (checks/fig_a-one-vs-two.py; 4001 points, the three curves as specified, a grey line at x = 0.5, the legend below the axes, and both arrow insets at the same scale with grey leader lines to (0, 4) and (0.5, 0))

## Notes
- The dark-band claim is "almost to zero" in the text but exactly 0 in the equal-amplitude model the figure uses. The two agree: "almost" covers real slits with unequal amplitudes, and check 12 shows this.
- "Twice the 2 you'd get by adding chances" holds at bright-band centres. Averaged over the bands the two match (claim 2). The text states both correctly.
- Momentum "mass times velocity" is the non-relativistic form. That is fine at this level.
- Claim 13 is the only one computation can't check. It matches the published experiment.
