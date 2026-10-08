VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | Previous FAIL (#16): ideal filters must be introduced before the rules list | PASS (fixed) | checks/check_B2_01.py: "from here on all filters are assumed ideal" appears at char 953, before the rules list (char 1440) and before the Update rule |
| 2 | "Good laboratory filters come close" | PASS | checks/check_B2_01.py: Jones-matrix model of real polarizers (coherent leakage included). With k1 ≥ 0.95 and extinction ≥ 1e4: V→H ≤ 0.01 of 100 (ideal 0); V→45→H 22.1–24.5 (ideal 25); V→V 95–99 (ideal 100). All are within 15%. For context, a sheet-type filter (k1 = 0.9, 1e3:1) gives 0.09, 19.0 and 90 |
| 3 | "An ideal filter passes all ... blocks all ... passes part of any slanted light" | PASS | checks/check_B2_03.py: cos² gives 1 at 0°, 0 at 90° and strictly between at other angles (0.5 at 45°) |
| 4 | "very dim light delivers them almost always one at a time" | PASS | checks/check_B2_07.py (scipy.constants): 1 pW at 500 nm gives 2.5e6 photons/s, a mean of 0.0025 per 1 ns window. P(≥2 \| ≥1) = 1.3e-3 for laser (Poisson) light and 2.5e-3 for thermal light |
| 5 | "shadow on the vertical is about 0.866 ... 0.75"; "horizontal is 0.5 ... 0.25" | PASS | checks/check_B2_02.py: cos30° = 0.8660; cos² = 3/4 exactly; sin30° = 1/2; sin² = 1/4 |
| 6 | "At every angle the two chances add up to 100%" | PASS | checks/check_B2_02.py: sympy reduces cos²θ + sin²θ − 1 to 0 |
| 7 | "A vertical arrow has no shadow on the horizontal, so none get through" | PASS | checks/check_B2_03.py: exact 0; Monte Carlo with 200,000 single photons gives 0 |
| 8 | "Roughly half, about 50 ... each now polarized at 45° ... about 25" | PASS | checks/check_B2_03.py: exact 50, 25. Monte Carlo per 100: 50.07, 25.08. The post-filter state equals the 45° unit vector |
| 9 | "Bright light does the same, as ordinary wave physics predicts" | PASS | checks/check_B2_03.py: Malus's law gives cos²45°·cos²45° = 0.25 of the intensity, the same fraction |
| 10 | "A mere sieve ... leaving the ones that pass unchanged ... an extra sieve can only remove photons" | PASS | checks/check_B2_04.py: 20,000 random hidden-property sieve models (deterministic and stochastic). P(with 45°) − P(without) ≤ 0 in all of them (max 0.0); quantum gives +0.25 |
| 11 | "secretly vertical or horizontal ... would pass only about half"; "it passes every one" | PASS | checks/check_B2_05.py: a 50/50 V/H mixture passes with probability 0.5; V and H each pass with 0.5; a 45° photon passes with 1.0 |
| 12 | "a vertical photon is a superposition of the two diagonals, 45° and 135°" | PASS | checks/check_B2_05.py: V = 0.707·D − 0.707·A, reconstruction error 0 |
| 13 | "answer to a 45° filter is certain, but ... vertical filter is 50/50" | PASS | checks/check_B2_06.py: P(45) = 1.000, P(V) = 0.500 |
| 14 | "an answer is certain only when the arrow lies right along that answer's direction" | PASS | checks/check_B2_06.py: sympy solveset shows the V-filter answer is certain only at 0, π/2 and π |
| 15 | "no way of preparing a photon makes its answers to both a vertical and a 45° filter certain" | PASS | checks/check_B2_06.py: over the full Bloch ball (pure, mixed and complex states), max of min(certainty_V, certainty_45) = 0.8536 = (1+1/√2)/2 < 1; [σz, σx] ≠ 0 |
| 16 | "momentum (roughly, mass times velocity)" | PASS | checks/check_B2_07.py: p/(mv) = γ = 1.00005 at 0.01c and 1.005 at 0.1c. "Roughly" covers the relativistic correction |
| 17 | "light whose wiggle goes round in circles already needs this" (richer arrows) | PASS | checks/check_B2_08.py: (1, i)/√2 passes every linear filter with 0.5. The best real arrow is off by 0.49998 at some filter angle |
| 18 | "after an ideal measurement that leaves the system intact, its arrow points along the answer it gave" | PASS | checks/check_B2_09.py: Lüders projection on random 4-dim observables (including degenerate ones). The post-state lies in the answer's subspace, and repeating the measurement gives the same answer with certainty (max deviation 2e-12) |
| 19 | "Left isolated ... changes, if at all, gradually and predictably" (Schrödinger equation) | PASS | checks/check_B2_10.py: exp(−iHt) keeps the norm at 1 (3e-15). Steps are continuous (max 0.028 for dt = 0.01). A rerun reproduces the state exactly. An energy eigenstate stays the same state (fidelity 1), which covers "if at all" |
| 20 | "polarization is one example of a qubit"; "two photons can share a single arrow ... neither photon an arrow of its own" | PASS | checks/check_B2_11.py: the polarization space is 2-dimensional. The Bell state has Schmidt coefficients (0.707, 0.707) and one-photon purity 0.5, so it has no single-photon pure state; a product state has purity 1 |
| 21 | Check-yourself: middle filter turned vertical | PASS | checks/check_B2_03.py: the question is well posed; 100 → 100 → 0 (exact and Monte Carlo) |
| 22 | Figure labels (b-shadow, b-three-filters) true and matching the captions | PASS | checks/check_B2_12.py: cos30° ≈ 0.866, sin30° = 0.5, 0.866² ≈ 0.75, 0.5² = 0.25 and 0.75 + 0.25 = 1 all hold. Counts are 100/0 and 100/50/25, with the same bar scale in both rows. Both PNGs regenerated from their scripts are pixel-identical to the files on disk |

Pass count: 22/22.

## Figures
- b-shadow: figures/b-shadow.png (checks/fig_b-shadow.py, unchanged; regenerated identical). The labels match the caption: blue vertical shadow cos 30° ≈ 0.866, orange horizontal shadow sin 30° = 0.5, chances 0.75 and 0.25, sum 1. The 30° arc sits between the arrow and the vertical axis. The axes have equal scaling.
- b-three-filters: figures/b-three-filters.png (checks/fig_b-three-filters.py, unchanged; regenerated identical). The labels match the caption: "light travels left to right", the first bar in each row is 100 after the vertical filter, the last-filter count rises from 0 to 25, and the title says "expected photon counts, ideal filters". No re-plot was needed.

## Notes
- The verify-B.md FAIL is fixed: the idealization now comes at the first mention of filters, before the rules.
- Wording only, not errors: the b-shadow box says "chance to pass", while the text now says "get through". The arrow label says "photon's polarization (length 1)", while the text says the arrow *describes* the state. Both are consistent with the text. Changing them to "chance to get through" and "photon's state arrow (length 1)" would match the new wording exactly, if the explainer wants that.
- Claim 18: for a degenerate answer (several directions sharing one answer), "points along the answer" means "lies within that answer's set of directions". The statement is true in that reading, and it is exact for the photon case.
- Claim 2 depends on typical specs for crystal polarizers (transmission ≥ 95%, extinction ≥ 1e4:1). These are an input to the model, not something computation can establish. Sheet polarizers are noticeably further from ideal (19 instead of 25).
- Claim 4 uses an illustrative 1 pW / 1 ns setting; any dimmer beam or shorter window makes multi-photon events rarer still.
