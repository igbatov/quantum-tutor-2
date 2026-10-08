VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "shadow on the vertical is about 0.866 ... 0.75"; "horizontal is 0.5 ... 0.25" | PASS | checks/check_B_01.py: cos30° = 0.8660, cos² = 3/4 exactly; sin30° = 1/2, sin² = 1/4 |
| 2 | "These always add to 100% ... by Pythagoras" | PASS | checks/check_B_01.py: sympy simplifies cos²θ + sin²θ − 1 to 0 for all θ |
| 3 | "a vertical arrow has no horizontal shadow, so none get through" (ideal filters) | PASS | checks/check_B_02.py: 100·cos²90° = 0 |
| 4 | "About half pass it, roughly 50 ... half of those ... roughly 25" | PASS | checks/check_B_02.py: exact 50 and 25; Monte Carlo (single photons) 50.07, 25.08 per 100 |
| 5 | "Bright light does this too, as wave optics predicts" | PASS | checks/check_B_02.py: Malus's law I0·cos²45°·cos²45° = 0.25·I0, the same fraction |
| 6 | "A mere sieve, sorting photons by some fixed property, could never do that" | PASS | checks/check_B_03.py: 20,000 random hidden-property sieve models; P(V,45,H) − P(V,H) ≤ 0 always (max −5.9e-5); quantum gives 0.25 vs 0 |
| 7 | "secretly vertical or horizontal ... would pass only half"; "it passes every one" | PASS | checks/check_B_04.py: 50/50 mixture passes 45° filter with prob 0.5; a 45° photon passes with prob 1 |
| 8 | "a vertical photon is a superposition of the two diagonals" | PASS | checks/check_B_04.py: V = 0.707·D + 0.707·A, reconstruction error 2e-16 |
| 9 | "answer to a vertical filter is 50/50" | PASS | checks/check_B_05.py: P(pass) = 0.5, P(blocked) = 0.5 |
| 10 | "an answer is certain only when the arrow lies right along that answer's direction" | PASS | checks/check_B_05.py: exact solve; V/H answer certain only at 0°, 90°, 180° |
| 11 | "no way of preparing a photon makes both answers certain" (Heisenberg-type trade-off) | PASS | checks/check_B_05.py: scan of all pure and mixed states (Bloch ball, incl. complex); the largest achievable value of min(certainty of V/H, certainty of diagonal) is 0.853, analytic (1+1/√2)/2 = 0.854 < 1; [σz, σx] = 2iσy ≠ 0 |
| 12 | "complex numbers ... needed already for light whose wiggle goes round in circles" | PASS | checks/check_B_06.py: (1, i)/√2 passes every linear filter angle with prob 0.5 (error 2e-16); the best real arrow is off by 0.4999 at some angle |
| 13 | "turning smoothly in time ... as the Schrödinger equation describes" (length stays 1) | PASS | checks/check_B_06.py: exp(−iHt) with random Hermitian H keeps the norm at 1 to 1e-15; the steps are continuous (max step 0.0055 for dt = 0.01) |
| 14 | "two photons sharing one arrow (in a space with four directions)" | PASS | checks/check_B_07.py: 2⊗2 = 4 dimensions; Bell state has Schmidt rank 2 (can't be split into one arrow each), product state rank 1 |
| 15 | Check-yourself: middle filter turned vertical | PASS | checks/check_B_02.py: well posed; expected answer 100 → 100 → 0 |
| 16 | Rules list: a filter "blocks light wiggling straight across it"; a photon that passed a vertical filter "passes another vertical filter for certain" | FAIL | checks/check_B_08.py: this is true only for ideal filters, but the text says "assuming ideal filters" only three paragraphs later. Before that, it introduces filters as "like those in polarized sunglasses", which are real filters. A real polarizer passes an already-aligned photon with probability k1 ≈ 0.9 (not certainty) and leaks a little crossed light (0.9 of 100 at extinction ratio 100:1, 0.09 at 1000:1). The payoff survives with real filters (about 20–23 of 100 pass with the 45° filter versus 0.001–0.9 without), so only the wording needs fixing. Correct statement: introduce the idealization at first mention, e.g. "An ideal polarizing filter (good real ones, like those in polarized sunglasses, come close) passes light wiggling along its axis, blocks light wiggling straight across it ..." Alternatively, add "(ideal filters)" to the rules list. |

Pass count: 15/16.

## Figures
- b-shadow: figures/b-shadow.png (checks/fig_b-shadow.py; the arrow, the 30° angle, the shadows cos30° = 0.866 (blue) and sin30° = 0.5 (orange) are all computed; the annotations match the text)
- b-three-filters: figures/b-three-filters.png (checks/fig_b-three-filters.py; counts are computed from cos² with ideal filters: 100, 0 and 100, 50, 25; the same bar scale in both rows; filter axes drawn as line segments; the title says "ideal filters")

## Notes
- The angle convention is measured from the vertical filter axis (as the text says). Shadow on the vertical = cos θ and on the horizontal = sin θ. The figure follows this.
- "Superposition ... only means that this arrow casts a shadow on both" is fine for linear polarization. For general (complex) states, "shadow" means the magnitude of a complex amplitude. The text flags this in the zoom-out ("complex numbers in place of ordinary lengths"), so no change is needed.
- Claim 11 holds for mixed states as well as pure ones (checked across the whole Bloch ball), so "no way of preparing a photon" is true as written.
- No numerical constants are involved, so no CODATA values were needed.
