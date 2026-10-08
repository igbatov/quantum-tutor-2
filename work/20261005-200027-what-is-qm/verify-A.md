VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "about 0.95 at \|X\| = 0.5 and 0.62 at \|X\| = 1.5" | PASS | checks/check_A_01.py: P1(0.5)=0.9496, P1(1.5)=0.6150 |
| 2 | "Mark the dark stripes at X = -1.5, -0.5, 0.5, 1.5"; both-slit curve "exactly zero" there | PASS | checks/check_A_01.py: minima of 4P1cos^2(piX) in [-2,2] at exactly +-0.5, +-1.5; values ~1e-32 |
| 3 | "lands there nearly as often as at the hump's peak; with both open, essentially never" | PASS | checks/check_A_01.py: P1(0.5)/P1(0)=0.95; two-slit value 0 |
| 4 | "add the two amplitudes first, and squaring the size ... sets the chance" | PASS | checks/check_A_02.py: \|psi1+psi2\|^2 = 4 P1 cos^2(pi X) symbolically (Fraunhofer model, phase from path length) |
| 5 | "at some spots the two are equal and opposite and cancel" | PASS | checks/check_A_02.py: psi1/psi2 = -1 at X=1/2 |
| 6 | "With a record, you add chances ... two one-slit humps simply added" | PASS | checks/check_A_02.py: \|psi1\|^2+\|psi2\|^2 = 2 P1, no oscillating term |
| 7 | "twice as high at the centre" (bold vs dashed) | PASS | checks/check_A_02.py: limit ratio at X=0 is 2 |
| 8 | "slit separation = 4 x slit width" gives envelope [sin(piX/4)/(piX/4)]^2 | PASS | checks/check_A_02.py: envelope argument pi a X/d = pi X/4 for a=d/4; first envelope zero X=4 |
| 9 | "the electrons missing from the dark stripes turn up in the bright ones" | PASS | checks/check_A_03.py: integral of both-slit curve = integral of 2P1 (rel. diff 6e-14); interference only redistributes |
| 10 | "opening the second slit could only add hits there, never remove them" (classical) | PASS | checks/check_A_03.py: 2P1 >= P1 everywhere |
| 11 | "play a sound that is high wherever the noise is low, so the two add to silence" | PASS | checks/check_A_02.py: f + (-f) = 0 (trivial) |
| 12 | "well-isolated molecules of hundreds of atoms still make stripes" | UNVERIFIABLE | checks/check_A_04.py: empirical claim; de Broglie wavelengths computed (C60 at 200 m/s: 2.8 pm; 25,000 u at 250 m/s: 64 fm), consistent with published molecule-interference experiments (which reach ~2000 atoms, so "hundreds" is conservative and true) |

Pass count: 11/12 PASS, 0 FAIL, 1 UNVERIFIABLE (empirical).

## Figures
- a-buildup: figures/a-buildup.png (checks/fig_a-buildup.py; rejection sampling from cos^2(piX) sinc^2(X/4) on [-6,6], seed 12345, cumulative panels 10/100/1,000/10,000, shrinking dot size)
- a-one-vs-two: figures/a-one-vs-two.png (checks/fig_a-one-vs-two.py; grey thin / dashed / bold black curves, hollow downward arrows at the four dark stripes, open circles marking P1 = 0.95 and 0.62; distinguishable without colour)

## Notes
- The text's "Now close one slit ... leaving one broad hump" is accurate within the plotted range: the single-slit side lobes beyond |X|=4 are below 0.05 of the peak.
- The model used (both one-slit envelopes identical, centred at the same place) is the far-field (Fraunhofer) approximation; this is what makes the which-path result exactly 2*P1. Fine at the conceptual level.
- Dark stripes also occur at |X| = 2.5, 3.5, ...; the text and figure only mark the four nearest, which is consistent with "the first dark stripe beside the centre" (X = 0.5).
- The check question's expected answer (closing one slit makes the dark stripe receive hits, ~0.95 of the one-slit peak at X=0.5) is consistent with check 1.
