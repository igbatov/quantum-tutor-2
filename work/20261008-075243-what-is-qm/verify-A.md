VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "alike, the total is 2 and the chance 4 ... total is 0" | PASS | checks/check_A_01.py: (1+1)^2=4, (1-1)^2=0, chances added = 2; general \|1+e^{iφ}\|^2 = 2+2cos φ |
| 2 | "wide bright band in the middle with much fainter bands further out" (one slit) | PASS | checks/check_A_02.py: numerical Fraunhofer integral for d=4a matches cos²(πX)·sinc²(πX/4) to 1e-6; one-slit maxima only at 0 and ±5.72, side-band peak 0.047; figure values P1(0.5)=0.950, P1(1.5)=0.615 |
| 3 | "where with both slits open almost no electrons land (none in the ideal set-up)" | PASS | checks/check_A_03.py: ideal P_both=0 at half-integer X; with a 5% speed spread P_both(0.5)=0.008 vs P1(0.5)=0.95 |
| 4 | "At the dark stripes ... electrons now land. Opening a second slit took hits away." (and the Check-yourself question) | FAIL | checks/check_A_03.py: true at the interference dark lines (X=±0.5, ±1.5, ... P1 from 0.95 down to 0.004), but not at every dark spot. P_both = 4·P1·cos²(πX), so every zero of the one-slit pattern is dark with both slits too: at X=±4, ±8 (d=4a) a dark band (max 0.2% of the central peak) stays dark with one slit, and there opening the second slit gives more hits, not fewer (P_both ≥ P1 for 3.83<X<4.17). The Check-yourself question as worded ("a spot that stays dark when both slits are open") has the answer "it depends" at those spots. Correct statement: "At the dark stripes near the middle, where with both slits open almost no electrons land (none in the ideal set-up), electrons now land." Check question: "At one of the dark stripes near the middle of the screen, ..." |
| 5 | "faster electrons give narrower stripes" / "faster, shorter" | PASS | checks/check_A_04.py: relativistic λ=h/p, spacing λL/d; d(spacing)/dv<0 for v from 1 km/s to 0.99c; 50 keV: 5.36 pm, 100 keV: 3.70 pm |
| 6 | "the pattern is, ideally, the two one-slit patterns added"; "partly tells ... only partly fades"; "can't cancel; their chances just add" | PASS | checks/check_A_05.py: tracing out a recorder with overlap γ gives fringe visibility = γ (1.0, 0.5, 0.2, 0.0); γ=0 gives exactly P_L+P_R |
| 7 | "each ball uses one slit, so a second slit could only add hits" | PASS | checks/check_A_06.py: P_L+P_R ≥ P_L for any non-negative chances; the quantum model has P_both < P1 at the dark lines |
| 8 | "the same rule applied to hydrogen predicts the colours it emits" | PASS | checks/check_A_07.py: Schrödinger levels with reduced mass give Balmer lines 656.470, 486.274, 434.173, 410.294 nm vs NIST 656.469, 486.271, 434.169, 410.289 nm (agree to 1e-5) |
| 9 | "Combine all routes through the left slit into one hand ... alike, bright; opposite, dark" | PASS | checks/check_A_08.py: explicit path sum (source → slit point → screen) reproduces the formula (max diff 0.009 on a scale of 4); angle between hands 0° at X=0, 1 and 180° at X=0.5, 1.5 |
| 10 | "for a heavy object ... only routes very close to it matter" | PASS | checks/check_A_08.py: the band of routes that matter (Fresnel zone) at 100 m/s over 1 m + 1 m: electron 6 mm, C60 5 µm, 1 µm dust grain 0.2 nm |
| 11 | Pilot wave: "goes through one slit on a definite bent path, kept away from the dark lines", chance from unknown start | PASS | checks/check_A_09.py: 3000 Bohmian trajectories, two Gaussian slits; 0 cross the symmetry line; final positions match \|ψ\|² (KS p=0.51); 1 trajectory within ±0.5 of a dark line (\|ψ\|² predicts 0.3) |
| 12 | Objective collapse: "extremely rarely for one electron ... almost at once" for the screen | PASS | checks/check_A_10.py: GRW λ=1e-16/s: electron collapse probability during flight ~7e-28; 1e23 nucleons: 1e-7 s (Adler rate 1e-8/s: even faster). Needs about 1e20 or more nucleons displaced by the detection to be "almost at once" at GRW's rate |
| 13 | "a dust grain shows no stripes in practice because air and light record its position constantly" | PASS | checks/check_A_11.py: 10 µm grain in air: 9e17 collisions/s, each resolving position to ~2e-11 m, so decoherence in ~1e-18 s |
| 14 | "After thousands of electrons the dots form bright and dark stripes" | PASS | checks/check_A_12.py: at N=1000, 578 dots within ±0.15 of bright lines vs 44 near dark lines; at N=10 no pattern (4 vs 1) |
| 15 | Figure note: "a few dots land even far from the centre" | PASS | checks/check_A_12.py: 5.0% of the probability lies at \|X\|>4 (sample: 4.8%) |

Passed: 14 of 15.

## Figures
- a-dots-buildup: figures/a-dots-buildup.png (cumulative 10 / 100 / 1,000 / 10,000 dots, seed 12345, sampled from the stated P(X) over -8..8; dot size shrinks per panel)
- a-one-vs-both: figures/a-one-vs-both.png (three curves as specified; arrows and open circles mark the dark stripes at ±0.5, ±1.5. An inset with a stretched vertical scale shows the one-slit side bands (peak 0.047 at 5.7), which are otherwise only about 1% of the plot height. It also marks X=4, where the both-slit pattern is dark and the one-slit pattern is dark too, so the figure does not imply that every dark spot lights up with one slit)

## Notes
- The one FAIL is about scope, not the physics of the central dark stripes. Adding "near the middle" to the sentence and to the Check-yourself question fixes it. The single-slit zeros at X=±4, ±8 only appear because d=4a was chosen for the figure; any d/a ratio has such points somewhere.
- Not checked by computation (historical claims). They agree with the standard record: 1976 biprism (Merli, Missiroli, Pozzi), 1989 (Tonomura et al.), 2013 real slits (Bach et al.), and Feynman's path-integral paper (Rev. Mod. Phys., 1948).
- Dust grain: decoherence is a correct reason. As a second reason, a 10 µm grain's own wavelength at thermal speed is ~1e-17 m, so its stripes (~1e-14 m for d=1 mm, L=1 m) would be far too fine to see anyway. The text is not wrong, but it gives only one of the two reasons.
- Objective collapse "almost at once" assumes the detection displaces a macroscopic number of nucleons. That is standard for GRW, but it is an extra assumption.
