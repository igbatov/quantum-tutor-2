VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | Short answer: "single pieces and pair pieces and nothing else"; other powers "predict a genuine three-way effect" | PASS | check_C_01.py (rerun): I3 = 0 symbolically for size², nonzero for size, size³, size⁴ and mixtures. check_C2_03.py: abc coefficient of (a+b+c)³ is 6, and 0 in every single and pair run |
| 2 | "a number the square rule predicts to be zero at every spot, which no other power manages" | PASS | check_C2_01.py: exponents 0 to 20 in steps of 0.01 on 20 000 random complex triples; only p = 2 gives zero everywhere. On the far screen (d = 4a), max\|leftover\| is 4e-15 for p = 2 and 2.6e-2 already at p = 1.99 and 2.01 |
| 3 | Two slits: size or cube "still give stripes ... only the shape of the stripes would differ" | PASS | check_C2_07.py: \|1+e^{iφ}\|^p peaks at φ = 0 and is 0 at φ = π for p = 1, 2, 3. The fraction of each period above half maximum is 0.667, 0.500, 0.416 |
| 4 | Detectors "click together far less often than any wave ... could manage" | PASS | check_C2_08.py: for any classical intensity statistics, the coincidence ratio α = ⟨I²⟩/⟨I⟩² ≥ 1 (computed minimum 1.000 over five distributions); a single photon gives α = 0. The measured 0.18 is a literature value, not computed |
| 5 | Balls: rule "holds trivially"; classical wave "passes the add-and-subtract test too" | PASS | check_C_04.py (rerun) |
| 6 | Sorkin: square has "two-way interference and nothing beyond"; size, cube, fourth power, mixtures have three-way | PASS | check_C_01.py (rerun): max\|I3\| is 4.5, 114, 1900 and 19 for size, size³, size⁴ and size²+0.01size⁴; size² gives 3e-14 |
| 7 | Grid: "No piece involves all three"; pair blocks count "each diagonal square twice and each rectangle once" | PASS | check_C_02.py (rerun) |
| 8 | Rectangles scaled "from the full area ... through zero ... to minus the full area" | PASS | check_C_02.py (rerun): \|Σz\|² = Σ squares + Σ 2·(product)·cos θ |
| 9 | Square figure caption: "(9, 4 and 1)", "(6, 3 and 2, each twice)", dashed A+B block, "six dark boxes, each a·b·c = 6", volume 216 | PASS | check_C2_03.py: areas, total 36, (a+b)² = 9+6+6+4, six 3-edge boxes. Viewed figures/c-square-of-a-sum.png: the labels, dashed outline and six dark boxes match the caption |
| 10 | Centre and half-stripe arithmetic (9/12/3; 1/4/3; size 3 vs 3, 1 vs −1; cube 27 vs 21, 1 vs 5; fourth 81 vs 45) | PASS | check_C_03.py (rerun): all 18 numbers match |
| 11 | "The cube and every higher power fail even at the centre" | PASS | check_C_03.py: 3^p − 3·2^p + 3 > 0 for p in (2, 20] |
| 12 | "The plain size passes wherever all the hands line up" | PASS | check_C_03.py: residual 4e-15 for aligned random lengths |
| 13 | NEW: hands "120° apart": "each pair's total is exactly as long as a single hand", "every power ... gives 3 − 3 = 0" | PASS | check_C2_02.py: \|A+B+C\| = 3e-16, the three pair lengths are 1.000000000000, and the leftover is ≤ 2e-8 for p = 0.5, 1, 2, 3, 7 (rounding only) |
| 14 | NEW: "Everywhere else on this screen the plain size fails" | PASS | check_C2_02.py: the plain-size leftover is ≥ 0, zero only at φ/2π = 0, 1/3, 2/3, and ≥ 0.002 more than 0.01 unit away from them. On the whole far screen \|u\| ≤ 40 there are no zeros off the 1/3 grid (envelope zeros at u = 4k fall on the grid) |
| 15 | Fall-off of each slit's band "is the same for all three slits" | PASS | check_C_05.py (rerun) |
| 16 | Three-slit caption, rows 1–3: curves coincide; A+B = B+C, 1 unit; A+C, ½ unit; 4 and 9 at centre; faint stripe "about 1 near the centre, lower further out"; zeros at 1/3 and 2/3 | PASS | check_C2_03.py: zero spacings 1.000 and 0.500; centre values 4, 4, 9; faint stripe 0.950, 0.615, 0.221 at u = 0.5, 1.5, 2.5; three-slit zeros at fractional positions 0.333 and 0.667 |
| 17 | Row 4: square "zero at every point, to rounding"; cube "6 at the centre, swinging between positive and negative" | PASS | check_C2_03.py: max\|square leftover\| = 7e-15; cube leftover 6.000 at the centre, range −3.70 to 6.00 |
| 18 | Row 4, plain size (round-one FAIL): "never negative ... dropping to zero only at isolated points every third of a unit ... the tall stripes ... and the three-slit zeros" | PASS (fixed) | check_C2_02.py, check_C2_03.py: minimum −2e-16 (rounding), zeros exactly on the 1/3 grid; integers are tall stripes, 1/3 and 2/3 are three-slit zeros. The open circles in figures/c-three-slits.png sit on those points |
| 19 | "a sum of pair terms, one for each pair of alternatives"; Check-yourself (four slits from singles and pairs) | PASS | check_C2_06.py: interference = Σ_{i<j} 2Re(z_i z̄_j), with N(N−1)/2 terms for N = 2, 3, 4, 5, 8; symbolically \|A+B+C+D\|² = Σpairs − 2Σsingles |
| 20 | Model 3: chance "from the total hand alone", no three-way term ⇒ quadratic, "never from a component on its own and never from three multiplied together" | PASS | check_C2_04.py: degree-6 polynomial ansatz with f(0) NOT imposed. The 7-term leftover vanishing already forces f(0) = 0 and leaves only degrees 1 and 2; check_C_06.py: never-negative removes the linear part. Continuous to polynomial is Fréchet's theorem, cited rather than computed |
| 21 | "direction-blind" ⇒ "a constant times the squared length" (also "How they relate") | PASS | check_C2_04.py: rotation invariance leaves c·(x² + y²) (this also removes the linear terms on its own) |
| 22 | Pythagoras: squared shadows add to 1 "for every arrow"; "Not the plain shadow, not its cube" | PASS | check_C_07.py (rerun): p = 2 deviation 1.5e-15; p = 1 and p = 3 deviate by up to 1.2 and 0.55 |
| 23 | NEW Gleason wording: "weighted average of squared shadows"; certainty along the arrow ⇒ "squared shadow of that one arrow"; "every outcome equally likely" is such an average | PASS | check_C2_05.py: Tr(ρP) = Σ p_i \|⟨e\|ψ_i⟩\|² to 1e-15 in d = 3, 4, 6; a mixed ρ reaches at most its largest weight (< 1) in any direction, so certainty forces a single arrow; the average of \|ψ⟩⟨ψ\| over uniformly random arrows is I/3 (deviation 3e-4, Monte Carlo), giving 1/3 to every outcome, not 1 along the arrow |
| 24 | "at least three perpendicular directions" | PASS | check_C_07.py (rerun): a 2D frame function ½ + 0.4cos³2θ is valid and not cos²θ |
| 25 | Pilot wave: squared cloud carried into squared cloud; size or cube "in general, carried into something else" | PASS | check_C_08.py (rerun): continuity residual 8e-8 and 2e-7 for p = 2 vs 1.2 to 4.1 (p = 1) and 0.35 to 1.15 (p = 3) |
| 26 | NEW: objective collapse departs "only up to departures far too small to see in these experiments" | PASS | check_C2_09.py, order of magnitude: GRW rate 1e-16 s⁻¹ per nucleon, ~1000 u, 10 ms of flight gives about 1e-15 per molecule (1e-7 even at Adler's CSL rate), against a precision of about 1e-2. GRW localization does not act on photons. The molecular parameters are assumed |

Score: 26 PASS, 0 FAIL out of 26.

## Figures
- c-square-of-a-sum: figures/c-square-of-a-sum.png (from round one, checks/fig_c-square-of-a-sum.py). The caption matches the figure: diagonal 9, 4, 1; rectangles 6, 3, 2 twice; dashed A+B outline; cube as three layers with six dark a·b·c = 6 boxes.
- c-three-slits: figures/c-three-slits.png (from round one, checks/fig_c-three-slits.py). The caption matches the panel titles and data: row titles, "max \|leftover\|" values 4.2e-15, 1.95 and 6.00, faint-stripe annotation 0.95, and open circles every 1/3 unit in the plain-size panel.

## Notes
- The round-one FAIL (claim 22, plain-size zeros described as "a few spots") is fixed in both the caption and the body. The new sentence on the 120° spots is exactly right, including "every power" there.
- Not computable here (literature): the 1/100 bound, the 2014, 2016 and 2017 results, Born's footnote, Busch 2003 (his result covers every dimension, including 2, so "extended ... to two-dimensional systems" is accurate), Gisin, and the interpretation attributions.
- Claim 26 rests on assumed molecule mass and flight time. Even with parameters a thousand times larger, the conclusion holds.
