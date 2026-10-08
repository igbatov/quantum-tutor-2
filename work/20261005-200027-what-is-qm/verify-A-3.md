VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "narrow stripes are replaced by one wide bright band, with much fainter bands further out" (fixes verify-A-2 row 1) | PASS | checks/check_A3_01.py: P1 = sinc^2(X/4) over \|X\|<=60. The central band has no narrow stripes. Brightest side band is 0.047 of the centre (X = 5.72), the next is 0.017. 90.3% of hits fall in the central band. Same result with the near-field offset of 0.5. |
| 2 | Caption: "flanked by dark gaps and much fainter side bands, the brightest about 5%" | PASS | checks/check_A3_01.py: zeros at X = +-4, +-8 (1.5e-33); first side band 4.72% of the centre. |
| 3 | "first dark stripe beside the centre ... 95% as often as at the wide band's peak; with both open, almost never" | PASS | checks/check_A3_02.py: first zero of the two-slit pattern is at X = 0.5. There P1 = 0.9496 and the ideal two-slit value is 1e-32. |
| 4 | "opening the second slit made some spots almost unreachable" (fixes verify-A-2 row 4) | PASS | checks/check_A3_02.py: realistic both-open/one-slit ratios at the dark stripe are 3.3% (spot 0.1 wide), 1% (amplitude ratio 0.9) and 2% (visibility 0.99). Small but nonzero, so "almost" is correct. |
| 5 | Caption: "falls to zero in this ideal calculation, and to nearly zero in real experiments, though one slit alone gives 95% or 62%"; text: "completely in an ideal set-up, almost completely in a real one" | PASS | checks/check_A3_02.py: P1(0.5) = 0.950, P1(1.5) = 0.615 (rounds to 62%); realistic minima as in row 4. |
| 6 | "opening the second slit could only add hits there, never remove them" (under the stated assumption) | PASS | checks/check_A3_03.py: 2P1 >= P1 everywhere on \|X\|<=40. |
| 7 | "+1 and -1 add to 0 ... +1 and +1 add to 2, which squares to 4, twice the 1 + 1 = 2" | PASS | checks/check_A3_03.py: arithmetic checks out; ratio is 2. |
| 8 | "add the two amplitudes first, and the square of the total's size sets the chance"; "depends on the length of its route" | PASS | checks/check_A3_03.py: with a path-length phase, \|psi1+psi2\|^2 - 4A^2 cos^2(pi X) = 0 symbolically. |
| 9 | Caption: "At the bright stripes the bold curve rises above the dashed one (twice as high at the centre)" | PASS | checks/check_A3_03.py: bold/dashed = 2.000000 at every stripe centre X = integer where P1 > 0 (the text defines bright stripes as where the two amplitudes match). See Notes for tiny bumps near X = +-4. |
| 10 | Caption: "over the whole screen the totals are equal" | PASS | checks/check_A3_03.py: integrals over \|X\|<2000 agree to 5e-13. |
| 11 | "If the record reliably tells the slits apart, the narrow stripes disappear; a fuzzy record only fades them" | PASS | checks/check_A3_04.py: P = 2 + 2g cos(2 pi X) for record overlap g. Visibility equals g, so the stripes vanish when g = 0 and only fade when 0 < g < 1. |
| 12 | "exactly the two one-slit patterns added together, much like the broad spread you probably first guessed" (fixes verify-A-2 row 8) | PASS | checks/check_A3_04.py and check_A3_01.py: g = 0 gives exactly \|psi1\|^2 + \|psi2\|^2 = 2P1. It has no narrow stripes and 90% of hits in one band. The 4.7% side bands remain, so "much like" is accurate and not overstated. |
| 13 | "almost never more than one electron in flight at a time" | PASS | checks/check_A3_05.py: with Tonomura-type parameters (50 kV, 1000 e/s, 1.5 m), electrons are about 124 km apart. The chance of a second electron in flight is 1.2e-5. |
| 14 | Headphones: "the two largely cancel and a steady hum ... becomes much quieter" | PASS | checks/check_A3_06.py: p + (-p) = 0. With a 50 us delay, the residual is -30 dB at 100 Hz but only -0.8 dB at 3 kHz. "Largely", and the steady low hum, are therefore apt. |
| 15 | "Air and light bouncing off big objects ... washing out their interference almost instantly" | PASS | checks/check_A3_07.py: first air collision for a 1 um grain at 2.8e-17 s, and for a 0.1 um grain at 2.8e-15 s. |
| 16 | "well-isolated molecules of hundreds of atoms still make stripes" | UNVERIFIABLE | checks/check_A3_07.py: this is an empirical claim. The de Broglie wavelengths (C60 2.8 pm; 10,000 u 0.4 pm; 25,000 u 64 fm) are consistent with Arndt 1999, Gerlich 2011 and Fein 2019. |
| 17 | Figure matches caption: d = 4a, "magnified about 18 times", arrows at dark stripes, circles at 0.95/0.62, legend labels | PASS | checks/check_A3_08.py: envelope zeros at 4 and 8; magnification is 4.6/0.25 = 18.4; arrows at +-0.5 and +-1.5, where the two-slit value is about 1e-32; circles at 0.950 and 0.615. No legend label contains "actually seen" or "one slit or the other". |

Pass count: 16/17 PASS, 0 FAIL, 1 UNVERIFIABLE. All three FAILs from verify-A-2.md (rows 1, 4, 8) are fixed (rows 1, 4, 12 above).

## Figures
- a-one-vs-two: figures/a-one-vs-two.png, re-plotted by checks/fig_a-one-vs-two.py. The labels are now:
  - Main-panel legend: "one slit open (either one)", "if chances simply added (also with a which-slit detector)", "both slits open (ideal set-up)".
  - Main-panel note: "arrows: dark stripes: zero with both slits open (ideal set-up); circles: one slit alone (0.95 and 0.62)".
  - Zoomed side-band panel (kept, -14..14, x18): new legend "one slit open" and "chances added (which-slit detector)". The side-band annotations were moved so the legend doesn't overlap them.

  Line styles match the caption: grey for one slit, dashed for chances added, bold for both open.
- a-buildup: figures/a-buildup.png, not redrawn. Its caption makes no shape claim that the model contradicts.

## Notes
- Row 9 edge case: the envelope zero at X = +-4 removes the bright stripe there. It is flanked by tiny bold-curve bumps at X = 3.72 and 4.27 (0.2% of the centre's height) that sit slightly below the dashed curve. They are not at stripe centres, where the amplitudes match, and they are invisible at the plotted scale, so the caption is true as written. If the explainer wants to be exhaustive, "at the bright stripes" could become "at each bright stripe". No change is needed.
- Model: Fraunhofer, identical slits, d = 4a. In near field, the X = +-4 zeros become shallow minima of about 1.4% (see verify-A-2). None of the text's claims depend on exact zeros there.
