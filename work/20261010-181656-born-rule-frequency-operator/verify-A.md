VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "after 100 photons ... about 4 percentage points ... 10 000 by about 0.4"; table 0.433, 0.217, 0.043, 0.0043, 0.00043 | PASS | checks/check_A_01.py: sqrt(0.1875/N) = 0.4330, 0.2165, 0.0433, 0.00433, 0.000433 |
| 2 | "cos² 30° = 0.75 ... sin² 30° = 0.25" | PASS | checks/check_A_01.py: exact in sympy |
| 3 | "scatters ... by an amount that shrinks as 1/√N" | PASS | checks/check_A_01.py: Monte Carlo of 20 000 runs gives sd 0.0433 (N=100), 0.00433 (N=10⁴), within 3% of sqrt(p(1-p)/N) |
| 4 | "a classical wave divides its energy and gives at least 1" | PASS | checks/check_A_02.py: α = ⟨I²⟩/⟨I⟩² is 1.00 (steady), 2.00 (thermal), 1.33, 4.34 (other fluctuating intensities), never below 1 |
| 5 | "0.18 ± 0.06" (Grangier, Roger, Aspect) | UNVERIFIABLE | literature value; consistent with the quoted paper as far as I know, and it sits below the classical floor of 1 |
| 6 | "when the two amplitudes are equal in size, every exponent gives ½" | PASS | checks/check_A_03.py: a^q/(a^q+a^q) = 1/2 symbolically |
| 7 | Model 1: binomial "mean Np ... standard deviation sqrt(Np(1-p))" | PASS | checks/check_A_06.py (⟨F⟩ = p, ⟨F²⟩ − ⟨F⟩² = p(1−p)/N for N = 1..8) and check_A_01.py (Monte Carlo) |
| 8 | Table N = 1, 2, 3: entries 0.866/0.5; 0.75, 0.433, 0.25; 0.650, 0.375, 0.217, 0.125; squared sizes 0.422, 0.141, 0.047, 0.0156 | PASS | checks/check_A_04.py: 0.6495, 0.375, 0.2165, 0.125; squares 0.4219, 0.1406, 0.0469, 0.0156 |
| 9 | "In each row the squared sizes total 1"; Σ w_m = (p + 1 − p)^N = 1 | PASS | checks/check_A_04.py: brute-force sum over strings (N up to 8) and sympy binomial sum (N = 1..7) |
| 10 | F_N readings are "multiples of 1/N"; N=2 diagonal 0, ½, ½, 1; "0.1 is not among them" at N = 4 | PASS | checks/check_A_05.py: explicit matrices for N = 2..5 |
| 11 | "Ψ_N is not a sure-bet list at any finite N" (0 < p < 1) | PASS | checks/check_A_05.py: ‖(F − ⟨F⟩)Ψ‖ > 0 for p = 0.1, 0.25, 0.5, 0.9 and N = 1, 2, 3, 6 |
| 12 | "F_N = (1/N)(P⁽¹⁾+…+P⁽ᴺ⁾)", "P⁽ᵏ⁾P⁽ᵏ⁾ = P⁽ᵏ⁾", "⟨P⁽ʲ⁾P⁽ᵏ⁾⟩ = p²" for j ≠ k | PASS | checks/check_A_05.py and check_A_06.py: explicit matrices; weighted sums match p and p² |
| 13 | "‖(F_N − λ)Ψ_N‖² = (λ − p)² + p(1−p)/N", minimum at λ = p for every N | PASS | checks/check_A_06.py: sympy identity for N = 1..8 |
| 14 | N = 2, p = ¼: "3/32 = 0.09375"; λ = ½: "10/64 = 0.156" = "5/32"; "p = ½ gives 1/8 at N = 2" | PASS | checks/check_A_06.py: 3/32, 5/32 = 0.15625, 1/8 exact; term-by-term 24/256 confirmed |
| 15 | Deviant bound "75/N: 0.075 at 10³, 0.0075 at 10⁴, 7.5×10⁻⁵ at 10⁶"; typical part ≥ 1 − 75/N | PASS | checks/check_A_07.py: p(1−p)/ε² = 75 |
| 16 | "the exact deviant length is far smaller, falling exponentially in N" | PASS | checks/check_A_07.py: exact 2.3×10⁻⁴ (N=10³), 4.8×10⁻³⁰ (10⁴), 10⁻²⁷⁸³ (10⁶); −ln(dev)/N → 0.0064 (constant rate) |
| 17 | "at no finite N is the deviant part zero" | PASS | checks/check_A_07.py: the all-R string is always deviant, weight p^N > 0 |
| 18 | "cos 1° = 0.99985 ... 0.99985^(10⁵) = e^(−15.2) ≈ 2.4×10⁻⁷" | PASS | checks/check_A_08.py: cos 1° = 0.999848, 10⁵·ln cos 1° = −15.23, e^(−15.23) = 2.43×10⁻⁷ (see Notes on rounding) |
| 19 | f_q table "0.366, 0.250, 0.161, 0.100"; totals "1.366^N, 1, 0.775^N, 0.625^N" | PASS | checks/check_A_03.py: 0.3660, 0.2500, 0.1614, 0.1000; 1.3660, 1, 0.7745, 0.6250; numeric peak of v_m at N = 2×10⁵ matches f_q to 10⁻⁴ |
| 20 | "v_{m+1}/v_m = (N−m)/(m+1) · \|c₁\|^q/\|c₀\|^q" | PASS | checks/check_A_03.py: sympy simplification gives zero difference |
| 21 | totals equal 1 "only at q = 2" (2-normalized, both entries nonzero) | PASS | checks/check_A_03.py: c₀^q + c₁^q is strictly decreasing in q |
| 22 | "only the 2-norm is kept fixed by continuous lossless change" | PASS | checks/check_A_10.py: for rotations of (cos θ, sin θ), the q-norm varies by 0.41 (q=1), 0.12 (q=1.5), 0.11 (q=3), 0.16 (q=4) and by 10⁻¹⁶ only at q=2. Tested for real 2D rotations only; the general statement is the cited theorem |
| 23 | N = 4, p = 0.9: "0.0001 + 0.0036 + 0.0486 = 0.0523"; 0.2916; 0.6561; "11 of the 16 ... 0.6875" | PASS | checks/check_A_09.py: exact |
| 24 | "By number of branches, most branches see a fraction near ½ whatever p is" | PASS | checks/check_A_09.py: share of branches by count within 0.05 of ½ is 0.73 (N=100), 0.9986 (N=1000), while their weight at p = 0.9 is 2×10⁻¹⁹ and 10⁻¹⁷⁸. Holds for large N; at N = 4 it is "most branches have fraction ≤ ½", which is what the text actually computes |
| 25 | Figure a-weights-concentrate caption: "weight only 0.42"; spreads "0.217, 0.108, 0.054, 0.027"; "total 1 in every panel"; "at every N some weight sits away from 1/4" | PASS | checks/check_A_12.py: w₁ = 0.4219 at N = 4; spreads 0.2165, 0.1083, 0.0541, 0.0271 |
| 26 | Figure a-deviant-length caption: "every curve falls toward zero as N grows" | FAIL | checks/check_A_12.py: for integer N from 10 to 400 the exact deviant length goes up from N to N+1 at 272 values of N (ε = 0.05) and 253 values (ε = 0.1), with jumps up to ×1.6 (for example 0.47 at N = 10 to 0.74 at N = 11, ε = 0.05). The overall trend is to zero, but the curves are not monotone. Also the bound curves exceed 1 for N < 75 (ε = 0.05) and N < 19 (ε = 0.1), where they say nothing. **Correct statement:** "The bounds fall as 1/N. The exact deviant lengths zigzag at small N, because the reading m/N can only take multiples of 1/N, and then fall exponentially, far below their bounds. At no N shown is any of them zero." |
| 27 | Check yourself: p = ¾, N = 300 | PASS | checks/check_A_11.py: sqrt(0.1875/300) = 0.025; halving needs N = 1200. The question is well posed |
| 28 | Born 1926: footnote "corrected the main text's 'proportional to the amplitude'" | UNVERIFIABLE | historical; see Notes |

Pass count: 25 PASS, 1 FAIL, 2 UNVERIFIABLE (28 claims).

## Figures
Requested in the text:
- a-weights-concentrate: figures/a-weights-concentrate.png (checks/fig_a-weights-concentrate.py). Drawn as requested; the caption numbers are verified (row 25). Each panel has its own y-scale, so the peak height grows from left to right only through the axis labels.
- a-deviant-length: figures/a-deviant-length.png (checks/fig_a-deviant-length.py). Uses every integer N from 10 to 2000, then 120 log-spaced points up to 10⁵. The y-axis is cut at 10⁻³⁰, and a note on the plot says the exact curves continue to 10⁻²⁸⁰ (ε = 0.05) and 10⁻¹⁰⁷⁷ (ε = 0.1) at N = 10⁵. The zigzag at small N is visible and labelled. Use the corrected caption from row 26.

Added, one per section that had no figure (captions proposed and checked against the scripts):
- a-overview (opening paragraph): figures/a-overview.png. Proposed caption: "Squared miss ‖(F_N − λ)Ψ_N‖² = (λ − p)² + p(1−p)/N against the trial reading λ, for θ = 30° (p = 0.25) and N = 2, 10, 100. Every curve has its lowest point at λ = 0.25, and the depth of that lowest point, p(1−p)/N, shrinks toward zero as N grows but is never zero at finite N."
- a-experiment-1: figures/a-experiment-1.png. Proposed caption: "Left: ideal Malus's law; at θ = 30° the transmitted fraction is 0.75 and the reflected fraction 0.25. Right: five *simulated* runs of the running reflected fraction (independent photons, chance 0.25 each; not laboratory data), with the band 0.25 ± sqrt(p(1−p)/N). Single runs wander in and out of the band; the band narrows as 1/sqrt N."
- a-experiment-2: figures/a-experiment-2.png. Proposed caption: "Dominant R-fraction f_q = |c₁|^q/(|c₀|^q + |c₁|^q) if size were measured with exponent q = 1, 2, 3, 4. All curves cross at ½ (a 50/50 splitter cannot tell exponents apart), but at a 25/75 split they give 0.37, 0.25, 0.16 and 0.10. Only q = 2 is the straight diagonal f = |c₁|²."
- a-classical-candidates: figures/a-classical-candidates.png. Proposed caption: "Double-firing ratio α at a beam splitter. A classical wave gives α = ⟨I²⟩/⟨I⟩² ≥ 1: exactly 1 for steady light, 2 for thermal light (computed). An ideal single photon gives 0. Grangier, Roger and Aspect measured 0.18 ± 0.06 (quoted, not computed)."
- a-model-1: figures/a-model-1.png. Proposed caption: "If chance is the squared length (Born rule assumed), the reflected fraction in a run of N = 100 photons at p = 0.25 has a binomial distribution centred on 0.25 with standard deviation 0.043. The open circles are 5000 simulated runs."
- a-model-3: figures/a-model-3.png. Proposed caption: "p = 0.9. Black/solid: squared-length weight of the branches with R-fraction m/N. Hatched/dashed: share of branches by count. At N = 4 the weight is mostly at fractions 1 and ¾, while 11 of the 16 branches have fraction ≤ ½. At N = 100 the weight peaks at 0.9 and the count peaks at 0.5, with almost no overlap."
- a-how-they-relate: figures/a-how-they-relate.png. Proposed caption: "q-norm of the polarization state (cos θ, sin θ) as it is rotated. Only the 2-norm stays constant (the flat line). The 1-, 3- and 4-norms change with angle, so a lossless continuous rotation preserves only the 2-norm."
- Check yourself: no figure added, because a plot would give away the answer.

All PNGs were opened and inspected. Labels do not overlap, and line styles or hatching keep curves apart without relying on color.

## Notes
- Row 18 rounding: with the rounded value, 0.99985^(10⁵) = 3.06×10⁻⁷ (e^(−15.0)). The 2.4×10⁻⁷ comes from the unrounded cos 1° = 0.9998477. Suggest writing "(cos 1°)^(10⁵) = e^(−15.2) ≈ 2.4×10⁻⁷".
- Row 28: as I recall, Born's main text says the amplitude Φ "determines" (bestimmt) the probability, and the footnote added in proof says it is proportional to the square of Φ. The quoted "proportional to the amplitude" puts words in quotation marks that the main text may not contain. Safer wording: "the main text said the amplitude determines the probability; a footnote added in proof said it is proportional to the square".
- Typo in the "How they relate" table: "Dürr, Goldstone & Zanghì 1992" should be "Dürr, Goldstein & Zanghì", as in the Sources line.
- "the exact deviant length is far smaller" is true at the N values the text quotes (10³ and up). At N ≲ 75 the Chebyshev bound is above 1 and gives no information; mentioning this would help the learner read the figure.
- Row 22 was tested only for real rotations in two dimensions. The general claim (the Banach–Lamperti theorem: isometries of ℓ^p for p ≠ 2 are only permutations with phases, so they allow no continuous mixing of components) is a cited theorem, not something computed here.
