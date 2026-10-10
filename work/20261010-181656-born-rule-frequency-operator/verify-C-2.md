VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "for N = 2 the list is (0.2, 0.4, 0.4, 0.8)", squares (0.04, 0.16, 0.16, 0.64) | PASS | checks/check_C_01_2.py: exact products, squares sum to 1 |
| 2 | "c1 = √0.8 = 0.894, c0 = √0.2 = 0.447"; N = 3 table | PASS | check_C_01_2.py: amplitudes 0.0894/0.1789/0.3578/0.7155; group weights 0.008/0.096/0.384/0.512; total 1 |
| 3 | "no branch has the frequency 0.8" (N = 3) | PASS | check_C_01_2.py: readings 0, 1/3, 2/3, 1 |
| 4 | Sum rules S[1]=1, S[x_k]=p, S[x_j x_k]=p²; N = 2 examples 0.8, 0.64 | PASS | check_C_01_2.py, check_C_02_2.py: exact sympy sums for N = 1, 2, 3, 5, 10, 20 |
| 5 | "S[(m/N − p)²] = p(1−p)/N" (each step) | PASS | check_C_02_2.py: symbolic residual 0 |
| 6 | "0.00512 + 0.02091 + 0.00683 + 0.02048 = 0.0533 = 0.16/3" | PASS | check_C_02_2.py |
| 7 | "total maverick weight < p(1−p)/(Nε²)" | PASS | check_C_03_2.py: holds for N = 1 to 10⁴, ε = 0.01 to 0.3 |
| 8 | "64/N ... 0.064 at N = 1000, 0.0064 at 10⁴ and 0.0009 at 70 000" | PASS | check_C_03_2.py: 0.064, 0.0064, 0.000914 |
| 9 | "about 7×10⁻⁵ at N = 1000 for ε = 0.05" | PASS | check_C_03_2.py (exact): 6.90×10⁻⁵ |
| 10 | N = 4, p = 0.8: "11 of the 16 ... 0.0016 + 0.0256 + 0.1536 = 0.181" | PASS | check_C_04_2.py: 11; 0.1808 |
| 11 | N = 20: "0.588 ... about 0.0026", peaks at m = 10 and 16 | PASS | check_C_04_2.py: 0.58810, 0.002595, peaks 10 and 16 |
| 12 | "By number, most coarse branches see a frequency near ½" | PASS | check_C_04_2.py: share within ±0.05 of ½ is 0.34, 0.68, 0.998 at N = 20, 100, 1000 (true for large N) |
| 13 | "F₂Ψ₂ = (0, 0.2, 0.2, 0.8)"; (0, 0.6, 0.8, 0) → ½× itself | PASS | check_C_05_2.py |
| 14 | Parabola "p(1−p)/N + 0 + (λ − p)²" | PASS | check_C_02_2.py: exact polynomial identity in λ for N = 2, 3, 7 |
| 15 | N = 2 by hand: 0.08, 0.17, 0.12 and their terms | PASS | check_C_05_2.py |
| 16 | Ψ_N "not an eigenvector at any finite N"; leftover → 0 | PASS | check_C_05_2.py |
| 17 | "cos 1° = 0.9998477 ... 0.9998477^(10⁵) = e^(−15.2) ≈ 2.4×10⁻⁷" | PASS | check_C_06_2.py: exponent −15.23, value 2.43×10⁻⁷ |
| 18 | p = 0.8 vs 0.8001 perpendicular only in the limit | PASS | check_C_06_2.py: per-copy overlap 1 − 7.8×10⁻⁹ |
| 19 | SD table 0.126 … 0.0015; counts 1.3 … 106 | PASS | check_C_07_2.py |
| 20 | N = 10: "45×0.8⁸×0.2² = 0.302", only m = 8 within 0.05 | PASS | check_C_07_2.py: 0.30199 |
| 21 | "about 95% of runs lie within two standard deviations" | PASS | check_C_07_2.py: 0.956, 0.956, 0.954 at N = 10³, 10⁴, 7×10⁴ |
| 22 | "the variance p(1−p)/N, is exactly the floor"; Pros: "the square of the measured 1/√N scatter" | PASS | check_C_08_2.py: floor = SD²; binomial variance at N = 6 equals floor; parabola minimum at λ = p equals floor |
| 23 | f_q = 2/3, 4/5, 8/9, 16/17; totals 1.342^N, 1, 0.805^N, 0.68^N | PASS | check_C_09_2.py |
| 24 | N = 20 q-peaks "m = 13–14, 16 and 19"; q-norm gives μ = \|a\|^q | PASS | check_C_09_2.py |
| 25 | "at the 50 kV used ... about 0.41 of the speed of light ... roughly 120 km apart" | PASS | check_C_10_2.py: v = 0.4127c; spacing at 1000 e/s = 123.7 km; chance of a second electron during the ~10 ns transit ~10⁻⁵ |
| 26 | Caption c-buildup-fraction: outside the 1-s.d. band "about a third of the time ... (this run more often ...) ... almost always inside twice it" | PASS | check_C_11_2.py: exact P(outside 1 s.d.) 0.31–0.32 at N = 10³–7×10⁴; average over 400 runs 0.30; drawn run (seed replicated) outside 72% for N ≥ 1000, outside 2 s.d. 3.3% |
| 27 | Caption c-born-spread: "within-0.05 curve is 1 minus the ε = 0.05 deviant"; "no m/N does for N = 11 to 14" | PASS | check_C_12_2.py: within + deviant = 1 exactly; chance 0 at N = 11–14 (see Notes) |
| 28 | Caption c-rules-out: "(ii) and (iii) ... each stepping outside the one-standard-deviation band for stretches of a few hundred arrivals" | FAIL | check_C_11_2.py: run (iii) (seed 29) does this, with stretches of at most 264 arrivals. Run (ii) (seed 11) is outside the band continuously from N = 1811 to 10 000, a stretch of 8190 arrivals, and is outside 94% of the time. That is normal for a random run (z = 1.4 at N = 10⁴). Correct statement: "(ii) and (iii) are the same kind of staircase, both wandering outside the one-standard-deviation band (run (ii) stays just outside it from about N = 1800 on, which happens to random runs) and both staying near twice it, so counts alone cannot tell tickets from amplitudes." The figure is now redrawn with the ±2 s.d. band (dotted). Add "dotted: twice that" to the caption. |
| 29 | Check yourself: N = 4, p = 0.9, leftover at λ = 1 is 0.0325 both ways, shortest at λ = 0.9 | PASS | check_C_13_2.py: weights 0.0001, 0.0036, 0.0486, 0.2916, 0.6561; Σ w_m(m/4 − 1)² = 0.0001 + 0.002025 + 0.01215 + 0.018225 + 0 = 13/400 = 0.0325; parabola 0.09/4 + 0.01 = 0.0325; full 16-entry vector also gives 13/400; minimum at λ = 9/10, value 0.0225 |

## Figures
- c-buildup-fraction: figures/c-buildup-fraction.png, reused; it matches the new caption (both bands drawn; frames at 10, 100, 3000, 20 000).
- c-rules-out: figures/c-rules-out.png, redrawn by checks/fig_c-rules-out_2.py with the same seeds and an added dotted ±2 s.d. band, because of FAIL #28.
- c-branch-tree, c-count-vs-weight, c-parabola-floor, c-born-spread, c-which-norm: reused; their captions still match.

## Notes
- #27: within 0.01 of 0.8 the chance is also 0 at N = 16–19 (13/16 = 0.8125). The caption's "N = 11 to 14" is true but not the full list. "for N = 11 to 14 and 16 to 19" would be complete.
- #29: the tutor answer is 0.0325 = 0.0225 (floor) + 0.01 ((1 − 0.9)²), and the shortest leftover is at λ = 0.9 with squared length 0.0225.
- The Goldstein spelling is now consistent in the table and the sources.
