VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "tiny, heavy, positive nucleus with much lighter, negative electrons" | PASS | checks/check_C2_01.py: m_p/m_e = 1836; a0 / proton radius = 6.3e4 |
| 2 | "spiral into the nucleus in about a hundred-billionth of a second" | PASS | checks/check_C2_01.py: Larmor collapse time from a0 = 1.56e-11 s |
| 3 | "orbits could be any size ... a smooth smear of all colors" | PASS | checks/check_C2_02.py: classical orbital frequency is continuous in r; orbits of 4.3 to 6.2 a0 emit 400 to 700 nm with no gaps |
| 4 | "every hydrogen atom in the universe is identical" / "so all hydrogen atoms are identical" | FAIL | checks/check_C2_04.py: deuterium, a natural form of hydrogen (about 1 atom in 6400), has a different ladder. Its red line is at 656.109 nm versus 656.288 nm (shift 0.18 nm, 2.7e-4). That is how deuterium was discovered. Correct statement: "every ordinary hydrogen atom is identical" / "so all ordinary hydrogen atoms are identical (a rare heavier kind, deuterium, has a very slightly shifted ladder)". |
| 5 | "The size of that number, squared, gives the chance" | PASS | checks/check_C2_08.py: the integral of psi_1s^2 is 1 (also checked for the momentum distribution) |
| 6 | "only certain patterns are steady, keeping their shape with one definite energy" | PASS | checks/check_C2_09.py: \|psi e^{-iEt/hbar}\|^2 does not depend on t; a mix of two energies does |
| 7 | String: 1, 2, 3 humps fit; "2.5 humps ... height 1 instead of ... 0" | PASS | checks/check_C2_07.py: sin(k pi) = 0 only for whole k; hump counts are 1, 2, 3; sin(2.5 pi) = 1 |
| 8 | Figure spec E_n = -13.6/n^2 eV (-13.6, -3.40, -1.51, -0.85, -0.54, -0.38) | PASS | checks/check_C2_03.py: CODATA with reduced mass gives -13.598, -3.400, -1.511, -0.850, -0.544, -0.378 eV |
| 9 | "hydrogen's energies crowd together toward the top" | PASS | checks/check_C2_03.py: gaps 10.20, 1.89, 0.66, 0.31, 0.17 eV, strictly shrinking |
| 10 | "while a string's frequencies are evenly spaced" | FAIL | checks/check_C2_03.py: this holds only for an ideal, perfectly flexible string. A real guitar string is stiff, so f_n = n f1 sqrt(1 + B n^2) with B about 1e-5 to 1e-4. For B = 5e-5 the gap between modes 11 and 12 is 1.0099 f1 versus 1.0002 f1 between modes 1 and 2, and mode 12 is 6 cents sharp. Correct statement: "while a string's frequencies are very nearly evenly spaced". The contrast with hydrogen still holds. |
| 11 | "rung 3 to rung 2 ... red line (656 nm)", "rung 4 to rung 2 its blue-green one", E = hf | PASS | checks/check_C2_05.py: 656.29 / 486.14 / 434.05 / 410.18 nm (air); 1.889 eV = hc/656.47 nm |
| 12 | "bigger drops make bluer light" | PASS | checks/check_C2_05.py: over all 28 pairs of rungs 1 to 8, wavelength falls strictly as the energy gap grows |
| 13 | "f, which your eye sees as color. So each gap makes one sharp color" | FAIL | checks/check_C2_05.py: of the 28 gaps among rungs 1 to 8, only 6 (the drops to rung 2) give visible light. The rest are ultraviolet (2->1: 121.6 nm) or infrared (4->3: 1876 nm). The figure itself labels 2->1 "invisible". Correct statement: "So each gap makes light of one sharp frequency, which is one sharp color when your eye can see it (many drops give ultraviolet or infrared light instead)." |
| 14 | "glowing hydrogen gives off only a few sharp colors, like a barcode" | PASS | checks/check_C2_06.py: the visible Balmer lines are 656.3, 486.1, 434.1 and 410.2 nm, plus fainter 397.0, 388.9 and 383.5 nm at the violet edge, so the count is still "a few" |
| 15 | Figure spec: strip over 400-700 nm with exactly four lines, "glowing hydrogen, as actually seen" | FAIL | checks/check_C2_06.py: the 400 nm cut sits just above the next Balmer lines (397.0, 388.9, 383.5 nm ...), which crowd toward the series limit at 364.6 nm. The ladder panel stops at rung 6 and does not show that the rungs continue. Fix (done in the redraw): widen the strip to 360-700 nm, draw the four bright lines plus fainter violet lines crowding toward 365 nm (UV band shaded), and draw faint rungs 7, 8, ... crowding toward 0. Suggested caption addition: "four bright lines, plus fainter violet ones that crowd toward the ultraviolet, just as the rungs crowd toward the top". |
| 16 | Rung 2 to rung 1 "ultraviolet (invisible)" | PASS | checks/check_C2_05.py: 121.6 nm |
| 17 | "squeezed into less space ... more energy of motion"; "bottom rung is the best balance" | PASS | checks/check_C2_08.py: exact variational family exp(-r/b): <T> = hbar^2/(2 m b^2) and <V> = -k/b; the minimum is at b = a0 with E = -13.606 eV (the exact ground state) |
| 18 | "lowest state the cloud is a round ball and nothing goes around" | PASS | checks/check_C2_08.py: psi_1s has no angle dependence; probability current Im(psi* grad psi) = 0 |
| 19 | "measure its speed and you'd find it moving fast" | PASS | checks/check_C2_08.py: rms 2.19e6 m/s, median 1.61e6 m/s; P(v < 100 km/s) = 3e-4 |
| 20 | "higher rung soon drops anyway, by giving off light"; "from the bottom rung ... nowhere lower" | PASS | checks/check_C2_09.py: 2p->1s rate 6.27e8 /s (lifetime 1.60 ns), with matrix element 128 sqrt2/243 a0 computed; n = 1 is the lowest level |
| 21 | "Measure the electron's energy ... always get one of the rungs, never anything in between" | PASS | checks/check_C2_03.py, check_C2_10.py: bound energies are discrete (hydrogen; also a finite well gives 5 isolated levels). True for the electron bound in the atom. |
| 22 | "energy ladders for anything trapped" | PASS | checks/check_C2_10.py: finite square well bound energies 1.89, 7.53, 16.77, 29.29, 44.04 (discrete) |
| 23 | "no two electrons can be in exactly the same state" | PASS | checks/check_C2_10.py: the antisymmetrized f(x1)f(x2) - f(x2)f(x1) = 0 |
| 24 | Check yourself: three rungs give "at most" 3 colors | PASS | checks/check_C2_10.py: 3 pairs, with distinct gaps 1.889, 10.2, 12.089 eV |

## Figures
- c-ladder-spectrum: figures/c-ladder-spectrum.png, redrawn by checks/fig_c-ladder-spectrum.py (overwrites round 1). The strip now spans 360-700 nm with a shaded UV band. It shows the four bright Balmer lines with the spec labels, the fainter lines n = 7 to 39 crowding toward the dotted series limit at 364.6 nm (labelled "fainter lines crowd toward 365 nm (UV)"), and the classical rainbow over 380-700 nm. The ladder adds grey rungs 7 and up, labelled "crowd toward 0". Everything else follows the spec.
- c-standing-waves: figures/c-standing-waves.png, unchanged from round 1. The range and caption hide nothing: sin(n pi x) is drawn over the full string, and the claims are exact for the ideal string the figure depicts.

## Notes
- Real-setup effects that do not make a claim false as written, though the explainer may want to know them:
  - Fine structure splits each rung slightly. H-alpha is several components about 0.016 nm apart (n = 2 split 4.5e-5 eV; check_C2_05.py). "One sharp color" still holds as a color.
  - Natural linewidths are about 1e-7 eV.
- "Soon drops anyway" covers a wide range: 2p lives 1.6 ns, but 2s is metastable at about 0.12 s (two-photon decay; literature value, not computed here). Very high rungs live for milliseconds to seconds. All of these end by emitting light in an isolated atom.
- "Moving fast" describes the typical measured value. The speed distribution reaches down to zero, but slow results are rare (check_C2_08.py).
- A real hydrogen discharge tube also shows faint molecular H2 lines. The text's "glowing hydrogen" means atomic hydrogen, as in stars. This was not checked computationally.
- Check-yourself: the answer is 3 for a generic ladder. For hydrogen's rungs 1 to 3, only 3->2 is visible; the other two are UV. If item 13 is reworded to "one sharp frequency", consider "how many different kinds of light (photon energies)".
- The quoted wavelengths are air values. Vacuum values are about 0.2 nm longer.
