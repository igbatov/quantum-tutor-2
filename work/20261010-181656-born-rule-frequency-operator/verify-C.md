VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "for N = 2 the list is (0.2, 0.4, 0.4, 0.8)", squares (0.04, 0.16, 0.16, 0.64) | PASS | checks/check_C_01.py: products of c's exact, sum of squares 1 |
| 2 | "c1 = √0.8 = 0.894, c0 = √0.2 = 0.447"; N = 3 table (amplitudes 0.089/0.179/0.358/0.716, weights, group weights 0.008/0.096/0.384/0.512, total 1) | PASS | check_C_01.py: amplitudes 0.0894, 0.1789, 0.3578, 0.7155; group weights exact; total 1 |
| 3 | "no branch has the frequency 0.8" (N = 3) | PASS | check_C_01.py: readings 0, 1/3, 2/3, 1 |
| 4 | Sum rules S[1]=1, S[x_k]=p, S[x_j x_k]=p², N = 2 examples 0.8 and 0.64 | PASS | check_C_01.py and check_C_02.py: exact sympy sums for N = 1, 2, 3, 5, 10, 20 |
| 5 | "S[(m/N − p)²] = p(1−p)/N" (every algebra step) | PASS | check_C_02.py: symbolic residual 0; also exact binomial sums |
| 6 | N = 3 check "0.00512 + 0.02091 + 0.00683 + 0.02048 = 0.0533 = 0.16/3" | PASS | check_C_02.py: terms match to 5 decimals, sum 0.053333 |
| 7 | "total maverick weight < p(1−p)/(Nε²)" | PASS | check_C_03.py: holds for N from 1 to 10⁴, ε = 0.01 to 0.3 |
| 8 | "64/N ... 0.064 at N = 1000, 0.0064 at 10⁴ and 0.0009 at 70 000" | PASS | check_C_03.py: 0.064, 0.0064, 0.000914 |
| 9 | "exact maverick weight ... roughly 10⁻⁴ at N = 1000 for ε = 0.05" | PASS | check_C_03.py (exact rationals): 6.90×10⁻⁵ (m < 750: 5.07×10⁻⁵; m > 850: 1.83×10⁻⁵); 9.5×10⁻⁵ if the boundary counts m = 750, 850 are included. "About 7×10⁻⁵" would be more precise. |
| 10 | N = 4: "1 + 4 + 6 = 11 of the 16 ... 0.0016 + 0.0256 + 0.1536 = 0.181" | PASS | check_C_04.py: 11; 0.1808 |
| 11 | N = 20: "by number 0.588 ... by weight about 0.0026"; count peak m = 10 (0.176), weight peak m = 16 (0.218) | PASS | check_C_04.py: 0.58810, 0.002595, peaks 10 (0.1762) and 16 (0.2182) |
| 12 | "By number, most branches see a frequency near ½ whatever p is" | PASS | check_C_04.py: share by number within ±0.05 of ½ is 0.34 (N = 20), 0.68 (N = 100), 0.998 (N = 1000); true for large N |
| 13 | "F₂Ψ₂ = (0, 0.2, 0.2, 0.8)", not a multiple; (0, 0.6, 0.8, 0) → ½× itself | PASS | check_C_05.py |
| 14 | Parabola "S[(m/N − λ)²] = p(1−p)/N + (λ − p)²" | PASS | check_C_02.py: exact polynomial identity in λ for N = 2, 3, 7 |
| 15 | N = 2 by hand: 0.0256+0.0288+0.0256 = 0.08; 0.01+0+0.16 = 0.17; 0.04+0.08+0 = 0.12 | PASS | check_C_05.py: all terms and totals exact |
| 16 | Ψ_N "not an eigenvector at any finite N"; leftover length → 0 (Hartle) | PASS | check_C_05.py: every reading has nonzero weight; leftover length √(0.16/N) |
| 17 | "cos 1° = 0.9998477 ... 0.9998477^(10⁵) = e^(−15.2) ≈ 2.4×10⁻⁷" | PASS | check_C_06.py: exponent −15.23, value 2.43×10⁻⁷ (see Notes on the rounded 0.99985) |
| 18 | "lists for p = 0.8 and p = 0.8001 are perpendicular ... which no finite N achieves" | PASS | check_C_06.py: per-copy overlap 1 − 7.8×10⁻⁹ < 1; overlap^N > 0 for every finite N and → 0 as N → ∞ |
| 19 | SD table: 0.126, 0.040, 0.0073, 0.0028, 0.0015; counts 1.3, 4, 22, 57, 106 | PASS | check_C_07.py: 0.1265, 0.0400, 0.00730, 0.00283, 0.00151; 1.26, 4.0, 21.9, 56.6, 105.8 |
| 20 | N = 10: only m = 8 within 0.05, chance "45×0.8⁸×0.2² = 0.302" | PASS | check_C_07.py: 0.30199 |
| 21 | "about 95% of runs lie within two standard deviations" | PASS | check_C_07.py: 0.956 (N = 1000), 0.956 (10⁴), 0.954 (7×10⁴) |
| 22 | Model 3: "standard deviation ... √(p(1−p)/N), the same expression as the floor of Model 2's parabola"; Model 2 Pros: "floor p(1−p)/N is the same expression as the measured 1/√N scatter" | FAIL | check_C_08.py: the floor is p(1−p)/N = 0.0016 at N = 100; the SD is √(p(1−p)/N) = 0.04. The floor equals the variance (the SD squared), not the SD. Correct statement: "the variance of the frequency, p(1−p)/N, is exactly the floor of Model 2's parabola; the standard deviation √(p(1−p)/N) is its square root." In Pros: "the floor p(1−p)/N is the square of the measured 1/√N scatter (the variance of the frequency), once lengths are read as chances." |
| 23 | f_q = 2/3, 4/5, 8/9, 16/17; totals 1.342^N, 1, 0.805^N, 0.68^N; sum > 1 for q < 2, < 1 for q > 2 | PASS | check_C_09.py: exact; sign of (c₀^q + c₁^q − 1) checked for q in (0.05, 10); argmax m/N at N = 2×10⁴ is 0.6667 (q=1), 0.8889 (q=3) |
| 24 | N = 20 q-peaks "m = 13-14, 16 and 19"; Everett's steps with a q-norm give μ = \|a\|^q | PASS | check_C_09.py: peaks {13, 14}, {16}, {19}; k\|a\|^q additive under the q-norm (sympy) |
| 25 | electrons "on average well over a hundred kilometres apart" at about 1000 per second | PASS | check_C_10.py: at 50 kV (Tonomura's value) v = 0.413c, spacing 124 km; but 98 km at 30 kV and 58 km at 10 kV (see Notes) |
| 26 | Captions c-buildup-fraction: running fraction "settles inside the narrowing band" 0.8 ± √(0.16/N); c-rules-out uses the same band | FAIL | check_C_11.py: that band is ±1 standard deviation. Averaged over 200 simulated runs, the running fraction is outside it for 28% of N in [1000, 70000], and 28% of runs are outside it at N = 70 000. In the drawn run it is outside 72% of the time for N ≥ 1000, but outside ±2 s.d. only 3% of the time. Correct statement: "the running fraction wanders widely at small N and then closes in on 0.8; its typical distance shrinks like the band √(0.16/N), but it often sits outside this one-standard-deviation band (about a third of the time) and almost always stays within twice it." The figure draws both bands. |
| 27 | Caption c-born-spread: "the right-hand curves are 1 minus the exact deviant weights of the previous figure" | FAIL | check_C_12.py: the right panel uses ε = 0.05 and 0.01, the previous figure ε = 0.1 and 0.05. Only ε = 0.05 is shared (within + deviant = 1 checked). Correct statement: "the ε = 0.05 curve is 1 minus the ε = 0.05 deviant weight of the previous figure; the numbers are the same, and only the label differs." Alternatively, use ε = 0.1 and 0.05 in both figures. |

## Figures
- c-buildup-fraction: figures/c-buildup-fraction.png. R = \|x\| ≤ 1.89 holds exactly 80% of the pattern. The 10- and 100-dot frames look random, and stripes with dark lanes are clear by 3000. The figure adds the ±2 s.d. band (dotted) beside the requested ±1 s.d. band (dashed), because of FAIL #26. The suptitle says this is a simulation, not the Hitachi data.
- c-rules-out: figures/c-rules-out.png. Three stacked panels (flat line; tickets staircase; amplitude-rule staircase, different seeds) with the ±1 s.d. band. Same caveat as #26 about "inside the band".
- c-branch-tree: figures/c-branch-tree.png. Binary tree with amplitudes at every node, leaf strings/amplitudes/weights, and a group-weight bar chart with the dashed line at 0.8.
- c-count-vs-weight: figures/c-count-vs-weight.png. Shaded totals 0.5881 and 0.0026. The m ≤ 10 bars in the weight panel are too small to see (largest 0.0020), so an arrow and note mark them.
- c-parabola-floor: figures/c-parabola-floor.png. The left panel has an inset zoomed near the floor, because the N = 32 and 128 curves overlap at full scale. The right panel shows exact deviant weights computed with exact integer boundaries for every integer N from 10 to 10⁵. They are jagged at small N and fall far below the Chebyshev bounds.
- c-born-spread: figures/c-born-spread.png. Left: binomial for N = 100 with mean 80 and ±4 marked. Right: the chances of landing within 0.05 and within 0.01, for every integer N. They are strongly jagged and non-monotonic at small N; for example, P(within 0.01) = 0 for N = 11 to 14, because no m/N falls in the window.
- c-which-norm: figures/c-which-norm.png. f_q curve with dots at 2/3, 4/5, 8/9, 16/17, and normalized q-weights for N = 20 with peaks at 13–14, 16 and 19 (hatching distinguishes the series without relying on color).

## Notes
- #22 matters in two places (Model 2 Pros, Model 3 paragraph). "How they relate" already states the variance identity correctly.
- Overlap example: the text says "overlap 0.99985" but computes with 0.9998477. With 0.99985 itself the result is 3.1×10⁻⁷, not 2.4×10⁻⁷. Say "overlap 0.9998477 (cos 1°)" throughout.
- Electron spacing: "well over a hundred kilometres" holds only at about 50 kV and above with about 1000 electrons/s (124 km). "Tens-of-kilovolt" covers energies where it is under 100 km. Suggest "about 120 km apart at the 50 kV used" or "over a hundred kilometres".
- Maverick weight at N = 1000, ε = 0.05: strict ">" gives 6.9×10⁻⁵, so "roughly 10⁻⁴" is acceptable; "about 7×10⁻⁵" is exact to one figure.
- Non-separability: "perpendicular ... unless [the overlap] is exactly 1" agrees with von Neumann's definition (a non-convergent phase product gives inner product 0). That is fine, but a pure phase difference also counts as "not exactly 1".
- Citation typo: the closing table has "Dürr, Goldstone & Zanghì 1992"; the sources line has "Goldstein". Goldstein is correct.
- The c-buildup density uses cos² fringes, so its minima are exactly zero. Real fringes have nonzero minima, which the text's "few electrons land" already allows.
- Check-yourself answer (for the tutor): N = 4, p = 0.9, the weight of m ≤ 2 is 0.0001 + 0.0036 + 0.0486 = 0.0523; by number 11/16 = 0.6875 (check_C_04.py).
