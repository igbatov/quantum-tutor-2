VERDICT: revise

The figure was produced and checked. The verdict is `revise` because two of the learner's descriptions of the regimes (rows 3 and 5) are not true as written, so the caption must use the corrected wording.

Model: 1D scalar paraxial (Fresnel) propagation of a monochromatic plane wave through two slits of width a, centres at -2a and +2a (d = 4a), using exact Fresnel integrals. Panels are normalised to the both-open maximum, and the left-slit-only curve uses the same scale. Chosen distances: **N = d²/(λL) = 20 (close), 3 (middle), 0.05 (far)**. N = 3 was used instead of 1 because at N = 1 each one-slit band is already 14a wide (FWHM, against d = 4a) and 37% of it lies on the far half, so it already looks like the far pattern.

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | Fresnel-integral field is a correct paraxial propagation | PASS | checks/check_A_fig3_01.py: agrees with independent FFT angular-spectrum propagation to 0.2–0.9% of peak (all three N) |
| 2 | Close: "two bands, one behind each slit" | PASS | check_A_fig3_02.py: left-only peak at x = -2.000a, exactly symmetric about -2a (1e-15); FWHM 0.72a; centre 2a from middle = 2.8 FWHM = 10 stripe spacings |
| 3 | Close: "little overlap, almost no stripes" | FAIL (wording) | Overlap is small: 1.6% of the left band falls on the right half. On the bands, stripe visibility is only 0.02 to 0.21, but the other slit's tail still makes ripples (both/left = 0.72 to 1.26 across the band). In the dim gap the stripes have full contrast (V = 1.00 at x = 0) and reach up to 12% of peak within ±1a. Correct statement: "Two bands, one behind each slit, with ripples on them; faint stripes in the dim gap between them." |
| 4 | Middle: "bands spread and overlap" | PASS | FWHM grows from 0.72a to 4.73a; 16.7% of the left band falls on the right half; centre still at -2a (1.5 stripe spacings, 0.42 FWHM from middle) |
| 5 | Middle: "stripes only in the overlap zone" | FAIL | V = 1.00 at the middle, with dark stripes at ±0.66a down to 2.8% of peak. V = 0.55 behind each slit, dropping to 0.07 at x = ±3.3a (the outer part of each band, where one band dominates). Stripes come back at the faint outer edges: V up to 0.93 at |x| ≈ 5.9a, peaks about 0.11 of max, caused by the other slit's side band. Correct statement: "Stripes are strongest where the bands overlap and almost disappear on the outer part of each band; faint stripes return at the far edges." |
| 6 | Far: "overlap complete" | PASS | One-slit band centred at -2a, which is 0.025 stripe spacings and 0.7% of its 283a FWHM from the middle; 49.3% on the other half |
| 7 | Far: "stripes everywhere" | PASS | V ≥ 0.998 wherever both-open > 5% of peak (|x| ≤ 252a); full contrast also in side bands |
| 8 | Far: "shape stops changing; matches a-one-vs-both.png" | PASS | Max deviation from cos²(πX)·sinc²(X/4) over ±8 stripe spacings = 1e-4 of peak; N = 0.05 vs 0.025 differ by 1e-4 |
| 9 | Spots where both-open ≈ 0 but one slit is well above 0 | PASS (computed) | check_A_fig3_03.py. Far: dark stripes at x = ±40, ±120, ±200a (±0.5, 1.5, 2.5 stripe spacings) have both-open ≤ 1e-4 while left-only is 95%, 62% and 22% of its peak. Middle: deepest at ±0.66a, both 0.028 vs left 0.33 (cut by 91%, not to zero). Close: none; the strongest cut is at ±0.69a (both 0.012 vs left 0.040, both tiny), and on the band both-open drops to 0.72× left-only. |
| 10 | Figure annotations: "at most 12% of peak" (close gap), "under 5% of peak" (far side bands) | PASS | check_A_fig3_04.py: 0.120 within ±1a; 0.045 beyond ±4 stripe spacings |

## Figures
- a-three-distances: figures/a-three-distances.png (script checks/fig_a-three-distances.py). Three stacked panels: bold = both open, thin grey = left slit only. Slits are drawn as black bars on the x-axis; in the far panel they show as one tick with a note. x-ranges are ±5a, ±14a and ±640a, and the far panel has a top axis in stripe spacings (±8, same range as figure 2). Annotated features: ripples on the close bands; faint gap stripes; full stripes in the overlap, weak stripes in the outer part of each band, and stripes again at the outer edges (middle); side bands beyond ±4 stripe spacings (far).

## Notes
- Features the caption must not hide:
  - Close: Fresnel edge ripples. Left-only varies from 0.29 to 1.15 of the geometric-shadow value inside the slit image. The one-slit side maxima are 7% of its peak at -3.1a and -0.9a.
  - Close: faint full-contrast stripes in the gap.
  - Middle: stripes again at the outer edges.
  - Far: side bands under 5% of peak, and zeros at ±4 stripe spacings, where the one-slit pattern is also zero.
- In the close panel the one-slit peak is 0.98 of the both-open peak. In the far panel it is 0.25 (the familiar factor 4).
- Local visibility is V = 2√(I_L I_R)/(I_L+I_R), the exact stripe contrast. Measuring the bold curve over one-stripe windows agrees in the middle; at band edges the window measure is inflated by the slope of the envelope.
