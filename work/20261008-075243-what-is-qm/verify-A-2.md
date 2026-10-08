VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "alike, the total is 2 and the chance 4 ... total is 0" | PASS | checks/check_A_01_2.py: (1+1)^2=4, (1-1)^2=0, chances added = 2; \|1+e^{iφ}\|^2 = 2+2cos φ |
| 2 | "wide bright band in the middle with much fainter bands further out" | PASS | checks/check_A_02_2.py: Fraunhofer integral matches formula to 7e-7; one-slit maxima only at 0 and ±5.72 (side band 0.047); P1(0.5)=0.950, P1(1.5)=0.615 |
| 3 | "At the dark stripes near the middle ... (none in the ideal set-up), electrons now land" + Check-yourself | PASS | checks/check_A_03_2.py: every both-slit zero with \|X\|<3.9 is at a half-integer; there P_both ≤ 1e-31 and P1 = 0.019 to 0.95 > 0; with a 5% speed spread P_both(0.5)=0.008, so "almost no electrons" holds. The round-1 FAIL (X=±4 spots) is fixed by "near the middle" |
| 4 | "Opening a second slit took hits away" | PASS | checks/check_A_03_2.py, check_A_06_2.py: P_both < P1 at the near-middle dark stripes; one-slit-or-other model gives P_L+P_R ≥ P_L everywhere |
| 5 | "faster electrons give narrower stripes" | PASS | checks/check_A_04_2.py: relativistic λ=h/p; spacing decreases with v over 1 km/s to 0.99c |
| 6 | "tells the slits apart for certain ... two one-slit patterns added; partly ... only partly fades" | PASS | checks/check_A_05_2.py: visibility = recorder-state overlap (1, 0.5, 0.2, 0); orthogonal records give exactly P_L+P_R |
| 7 | "the same rule applied to hydrogen predicts the colours it emits" | PASS | checks/check_A_07_2.py: Balmer lines 656.470/486.274/434.173/410.294 nm vs NIST to ≤1.1e-5 |
| 8 | "Combine all routes through the left slit ... alike, bright; opposite, dark" | PASS | checks/check_A_08_2.py: explicit path sum matches formula (max diff 0.009 of 4); hands at 0° on bright, 180° on dark lines |
| 9 | "for a heavy object ... only routes very close to it matter" | PASS | checks/check_A_08_2.py: relevant band electron 6 mm, C60 5 µm, 1 µm grain 0.2 nm |
| 10 | Pilot wave: "one slit on a definite bent path, kept away from the dark lines" | PASS | checks/check_A_09_2.py: 3000 Bohmian trajectories, 0 cross the midline, final positions match \|ψ\|² (KS p=0.51) |
| 11 | Objective collapse: "extremely rarely for one electron ... almost at once" for particles set in motion in the screen | PASS | checks/check_A_10_2.py: GRW electron collapse probability in flight 7e-28; 1e23 nucleons: 1e-7 s |
| 12 | Objective collapse: "faint warming and faint radiation"; difference "grows with the amount of matter" | PASS | checks/check_A_17_2.py: GRW heating 1.7e-44 W per nucleon (~1e-17 W/kg, nonzero but tiny); fringe loss over 1 ms: electron ~0, C60 5e-14, 25 kDa 6e-11, 1 µm grain ~1 (CSL N² scaling) |
| 13 | "sent so rarely that each has almost always landed before the next one leaves" | PASS | checks/check_A_13_2.py: 50 keV, 1.5 m flight 1.2e-8 s; at 1000 e/s Poisson overlap chance 1.2e-5 (so "almost always" is the right wording) |
| 14 | "a screen far enough away that the pattern no longer changes shape" | PASS | checks/check_A_14_2.py: Fresnel two-slit integral at L = 0.6 d²/λ differs from far-field shape by 0.08; from L ≥ 6 d²/λ by ≤0.002 (numerical floor) |
| 15 | "two electrons can never share one state ... photons can pile into one state, which a laser exploits" | PASS | checks/check_A_15_2.py: antisymmetric two-fermion state in one orbital = 0 (sympy); symmetric boson state nonzero; stimulated emission factor n+1; Z=10 filling energy -4 vs -10 if all in n=1 |
| 16 | Dust grain: "stripes would be far too fine to resolve" and "air and light constantly record its position" | PASS | checks/check_A_16_2.py, check_A_11_2.py: 1-10 µm grain at thermal speed λ = 4e-16 to 1e-17 m, stripe spacing (d=1 mm, L=1 m) 4e-13 to 1e-14 m; air collisions 9e17/s, decoherence ~1e-18 s |
| 17 | "After thousands of electrons ... stripes"; "a few dots land far from the centre" | PASS | checks/check_A_12_2.py: N=1000: 578 dots near bright vs 44 near dark lines; N=10 no pattern; 5.0% of probability at \|X\|>4 |

Passed: 17 of 17.

## Figures
- a-dots-buildup: figures/a-dots-buildup.png (reused; the new caption matches: cumulative 10/100/1,000/10,000 dots from the same d=4a pattern, dots smaller in later panels, a few far from centre)
- a-one-vs-both: figures/a-one-vs-both.png (reused; the new caption matches: thin grey one slit, dashed sum, bold both; arrows and open circles at ±0.5, ±1.5; inset shows the 0.047 side bands and X=4 labelled dark with one slit too)

## Notes
- Historical claims (1976, 1989 and 2013 experiments, Feynman 1948, objective-collapse searches finding nothing so far) were not checked by computation. They agree with the standard record.
- "Almost at once" for objective collapse still assumes the detection displaces a macroscopic number of nucleons (about 1e20 or more at GRW's rate). That is standard.
- "Faint radiation" refers to the CSL-predicted spontaneous X-ray emission, whose bounds come from experiments. Only the existence and smallness of the warming was computed.
