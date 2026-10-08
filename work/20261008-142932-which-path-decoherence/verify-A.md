VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "about a hundred-thousandth of the momentum"; "about ten centimetres"; "about 3 GHz" | PASS | checks/check_A_01.py: 85Rb 3.036 GHz gives 9.88 cm; 780 nm / 9.88 cm = 7.9e-6; microwave kick / 2ħk_opt = 4e-6 |
| 2 | "second pulse turns 'halves alike' into A and 'halves opposite' into B" | PASS | checks/check_A_02.py: π/2 pulse, sign flip, inverse π/2 pulse map the two parts to A and B (up to sign), overlap 0 |
| 3 | "no stripes, just the smooth pattern, the two one-path chances added"; same number of atoms | PASS | checks/check_A_03.py: orthogonal tag gives exactly E(X); area of E(1+cos2πX) / area of E = 1.000000000000; Gaussian has one turning point over [-30, 30] |
| 4 | Quarter-wave plates at ±45°: axis light unchanged; H gives opposite circular; V swapped | PASS | checks/check_A_04.py (Jones matrices): H gives L behind +45°, R behind −45°; V gives R and L; overlap of the two tags 0 |
| 5 | "whichever direction you choose ... tells you the slit photon's polarization along that same direction" | FAIL | checks/check_A_05.py: for Walborn's state (HV+VH)/√2, partner at 22.5° leaves the slit photon 50/50 along 22.5°. It holds for H/V (opposite results) and ±45° (same results), and for every direction only with (HH+VV)/√2 or the singlet. Correct statement: "measure the partner along H/V or along the diagonals and you know what the slit photon would give in that same measurement (opposite for H/V, the same for the diagonals, for the state used in this experiment)." |
| 6 | (b) no stripes; (c) +45° stripes, −45° "shifted by half a stripe spacing"; groups add to (b) | PASS | checks/check_A_06.py: contrast (a) 1.000, (b) 0.000, (c±45) 1.000; peaks at +0.25 and −0.25 (separation 0.500); max\|sum − (b)\| = 7e-16 for both Ψ+ and Φ+ |
| 7 | "What is never seen: stripes ... whatever is done to the partner" | PASS | checks/check_A_06.py: 50 random partner bases; the groups always sum to (b) within 1e-15 |
| 8 | (d) a later partner measurement leaves (b) and (c) unchanged | PASS | checks/check_A_06.py: operators on the partner commute with operators on the slit photon (commutator norm 0) |
| 9 | "(b) plates in: no stripes, the smooth two-one-slit-chances-added pattern" | FAIL | checks/check_A_07.py: the claim of no two-slit stripes holds, but over the full far screen the pattern is not one smooth hump. Every X = ±4, ±8, ... is a true zero, with one-slit side bands at 4.7%, 1.7%, 0.8% of the centre. The requested −4..4 window ends at the first zeros and hides them. Correct statement: "no stripes: just the two one-slit patterns added, a broad central band with faint one-slit side bands further out." |
| 10 | "cosine of θ is the stripe strength", "sine of θ is the telling-apart power"; θ = 60° gives 0.5 and ≈0.87 | PASS | checks/check_A_08.py: V = \|⟨a\|b⟩\| = cos θ; Helstrom 2P−1 = sin θ at 0, 30, 60, 90° |
| 11 | Budget is "an equality for an ideal tag ... an inequality for a tag ... in a random state" | PASS | checks/check_A_08.py: pure tags V²+D² = 1.000000; 5000 random mixed qutrit tags: max 0.964, all below 1 |
| 12 | Erasing: "the result is a coin toss whichever slit was used" | FAIL | checks/check_A_09.py: P(+\|left) = P(+\|right) = cos²(θ/2): 0.75 at θ = 60°, 0.97 at 20°. It is 50/50 only for a perfect tag (θ = 90°). Correct statement: "the result has the same odds whichever slit was used (50/50 for a perfect tag), so it reveals nothing about the slit." |
| 13 | Halfway-direction groups: "one group shows stripes and the other anti-stripes" | PASS | checks/check_A_09.py: the + group's amplitudes have the same sign and the − group's have opposite signs, for θ = 20, 60, 90° |
| 14 | Figure a-same-situation: +1/√2 − 1/√2 = 0; +1/√2 + 1/√2 = √2, chance 2; "0 + 2 = 2, the same as column 2" | PASS | checks/check_A_10.py (sympy, exact) |
| 15 | Overlaps multiply; "overlap of 0.9 each, fifty of them ... about half a per cent" | PASS | checks/check_A_11.py: tensor-product overlap = product (to 1e-17); 0.9^50 = 0.00515 |
| 16 | "on a log scale the fall is a straight line"; stripe strength "fell exponentially with the pressure" | PASS | checks/check_A_11.py: constant log slope; Poisson collisions with perfect tags give e^(−λ) (Monte Carlo agrees to 3e-3) |
| 17 | Gas atom "wavelength of tens of picometres", "tens of thousands of times shorter" than ~1 µm; one collision is a near-perfect tag | PASS | checks/check_A_12.py: He 73, CH4 36, Ar 23, Xe 13 pm at 300 K; ratio 1.4e4 to 7.8e4; isotropic-scattering overlap 0.002 (MC noise) at kΔx = 1.7e5 |
| 18 | "one glancing collision ... barely deflects a heavy molecule" | PASS | checks/check_A_12.py: a kick of h/(1 µm) deflects C70 at 100 to 200 m/s by 2 to 5 µrad |
| 19 | "a few millionths of a millibar, about a billionth of atmospheric pressure" | PASS | checks/check_A_12.py: 1e-6 to 3e-6 mbar is 1e-9 to 3e-9 atm |
| 20 | Dust grain: "faster than any laboratory can resolve, by the standard estimates" | UNVERIFIABLE | checks/check_A_13.py: for a 10 µm grain in air the saturated collision estimate is 2.8e-19 s, about the shortest interval ever measured (~2.5e-19 s). Sunlight alone gives ~1e-12 s, which labs can resolve. Textbook tables quote ~1e-31 s, using a long-wavelength formula outside its range. Safer: "in far less than a millionth of a billionth of a second in air (a calculation, not a measurement)". |

Passed 16 of 20 (3 FAIL, 1 UNVERIFIABLE).

## Figures
- a-atom-tag: figures/a-atom-tag.png (checks/fig_a-atom-tag.py; schematic plus computed Gaussian-envelope stripes and tag-on curve with equal areas)
- a-eraser-sorting: figures/a-eraser-sorting.png (checks/fig_a-eraser-sorting.py). **Range widened from −4..4 to −8..8** so the one-slit side bands and the zeros at X = ±4 show (see claim 9). One annotation added, "faint one-slit side bands (not two-slit stripes)". Dots are drawn by sampling from S(X) and sorted with probability (1 ± cos2πX)/2; the two groups use different markers (o and x) and different dash styles.
- a-ruled-out: figures/a-ruled-out.png (checks/fig_a-ruled-out.py)
- a-arrows-budget: figures/a-arrows-budget.png (checks/fig_a-arrows-budget.py)
- a-same-situation: figures/a-same-situation.png (checks/fig_a-same-situation.py)
- a-leaked-tag: figures/a-leaked-tag.png (checks/fig_a-leaked-tag.py; p = 0.5 leaves the 1e-6 axis at N ≈ 20, as expected)
- a-erasure-views: figures/a-erasure-views.png (checks/fig_a-erasure-views.py)
- a-relate-map: figures/a-relate-map.png (checks/fig_a-relate-map.py)

## Notes
- For the real plate settings (fast axes at ±45°), the ±45° groups' stripes sit a quarter spacing either side of the untagged stripes (check_A_06: peaks at ±0.25), not on them. The text and the a-eraser-sorting caption already hedge this ("depends on the exact plate and polarizer settings"), so it is consistent. The figure follows the requested convention (+45° group peaks at the centre).
- Check-yourself (partner polarizer horizontal): check_A_06 gives contrast 0.000 for that group under both Ψ+ and Φ+. The intended answer, no stripes, holds whichever Bell state is assumed.
- Claim 12 also affects the a-same-situation caption ("a coin toss whichever slit was used"). There it is correct, because that figure assumes a perfect tag. Only the general Model 1 sentence needs fixing.
- Claim 5 is a definition sentence, but the experiment's real state (HV+VH)/√2 makes it false as written. The fix only needs to name the two measurement pairs the text actually uses.
