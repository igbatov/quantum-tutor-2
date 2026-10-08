VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "tiny, heavy, positive nucleus with much lighter, negative electrons" | PASS | checks/check_C3_01.py: m_p/m_e = 1836.2; a0/r_p = 6.3e4 |
| 2 | "must circle the nucleus ... or they would fall straight in" | PASS | checks/check_C3_01.py: the Laplacian of the Coulomb potential is 0, so there is no stable static point (Earnshaw) |
| 3 | "spiral into the nucleus in about a hundred-billionth of a second" | PASS | checks/check_C3_01.py: Larmor collapse from a0 takes 1.56e-11 s |
| 4 | "orbits could be any size ... a smooth smear of all colors" | PASS | checks/check_C3_01.py: orbits of 4.26 to 6.18 a0 radiate continuously over 400 to 700 nm |
| 5 | "every atom of ordinary hydrogen has the same allowed energies" (round-2 FAIL 4, fixed) | PASS | checks/check_C3_02.py: the 1H ladder is fixed by constants alone. The qualifier "ordinary" is needed and is now present: deuterium's H-alpha is 656.291 nm vacuum, against 656.470 nm for 1H |
| 6 | "amplitude ... squared, gives the chance of finding the electron" | PASS | checks/check_C3_03.py: the integral of \|psi_1s\|^2 is 1 |
| 7 | "only certain patterns are steady, keeping their shape with one definite energy" | PASS | checks/check_C3_03.py: a one-energy state has a time-independent \|Psi\|^2; a mix of two energies does not |
| 8 | String "one hump, two, three ... each with its own note"; "2.5 humps would miss the pinned end" | PASS | checks/check_C3_03.py: sin(k pi) = 0 for k = 1, 2, 3; sin(2.5 pi) = 1; f_k = k v/2L are distinct |
| 9 | "hydrogen's energies crowd together toward the top, while an ideal string's frequencies are evenly spaced" (round-2 FAIL 10, fixed) | PASS | checks/check_C3_02.py: gaps 10.20, 1.89, 0.66, 0.31, 0.17 eV, strictly shrinking toward 0; ideal f_n = n f1 |
| 10 | "measuring its energy always gives one of the rungs, never anything in between" | PASS | checks/check_C3_02.py, check_C3_08.py: the bound levels are discrete (hydrogen; a finite well gives 5 isolated levels) |
| 11 | "each rung turns out to be a tight cluster of sub-rungs" | PASS | checks/check_C3_04.py: fine structure splits n = 2, 3, 4 into 2, 3, 4 levels (n = 2 spread 4.5e-5 eV). n = 1 is split by hyperfine structure, 5.87e-6 eV (the 21 cm line). Spread/gap is at most 2.4e-5, so the clusters are tight |
| 12 | "the atom usually gives off a single photon"; "one sharply defined frequency" | PASS | checks/check_C3_05.py: the H-alpha natural width is about 6.5e-8 of the frequency, and the Doppler width at 1000 K is about 2.3e-5. The only two-photon decay is 2s->1s (8.23/s, literature value), so "usually" is apt |
| 13 | "$E = hf$"; "bigger drops give higher frequencies" | PASS | checks/check_C3_05.py: the 3->2 gap of 1.8887 eV equals hc/656.47 nm |
| 14 | "Rung 3 to rung 2 ... red line (656 nm)", "rung 4 to rung 2 its blue-green one", "rung 2 to rung 1 ... ultraviolet" | PASS | checks/check_C3_05.py: 656.29 and 486.14 nm (air); 121.6 nm |
| 15 | "Your eye sees visible frequencies as colors, from red (lowest) to violet (highest)" (round-2 FAIL 13, fixed) | PASS | checks/check_C3_05.py: the text now says each drop gives one sharp frequency, and only visible ones are colors. That is consistent with UV for 2->1 |
| 16 | "glowing hydrogen gives off a few bright, sharp colors, like a barcode" | PASS | checks/check_C3_06.py: four lines above 400 nm (656.3, 486.1, 434.0, 410.2), the rest crowding below 400 nm |
| 17 | Caption: "Each colored arrow is a drop to rung 2 that makes one visible line ... grey higher rungs crowd toward the line where the electron is set free" | PASS | checks/check_C3_05.py: 3..6->2 all fall between 410 and 656 nm. check_C3_02.py: E_39 = -0.009 eV, approaching 0 |
| 18 | Caption: "four bright lines, plus fainter ones crowding toward 365 nm in the ultraviolet" (round-2 FAIL 15, fixed) | PASS | checks/check_C3_06.py: the computed relative line power (sympy hydrogen radial integrals) falls steadily: 1, 0.46, 0.24, 0.14, then 0.09, 0.06, ... (equal population per state); also at 10^4 K. Lines n >= 7 lie at 397.0 nm and below, crowding to the limit at 364.6 nm |
| 19 | "pressing a guitar string to a fret ... raises its note"; "sharper wiggles mean more energy of motion"; "bottom rung is the best balance" | PASS | check_C3_03.py: df1/dL < 0. check_C3_07.py: <T> = hbar^2/(2 m b^2) and <V> = -k/b, minimized at b = 1.0000 a0 with E = -13.606 eV |
| 20 | "electron on a higher rung drops down sooner or later, giving off light ... from the bottom ... nowhere lower" | PASS | checks/check_C3_08.py: 2p->1s rate 6.27e8 /s (1.60 ns); n = 1 is the lowest level |
| 21 | "lowest state the cloud is a round, fuzzy ball and nothing orbits" | PASS | checks/check_C3_07.py: psi_1s has no angle dependence, and its probability current is 0 |
| 22 | "measure the electron's speed ... usually get more than a thousand kilometers per second" | PASS | checks/check_C3_07.py: from the 1s momentum distribution (reduced mass, v0 = 2.1865e6 m/s), P(v > 1000 km/s) = 0.793. This confirms the writer's ~79%. Also P(v > 500 km/s) = 0.964 and P(v > 2000 km/s) = 0.347 |
| 23 | "ladders of allowed energies for anything trapped" | PASS | checks/check_C3_08.py: finite-well bound energies 1.89, 7.53, 16.77, 29.29, 44.04 |
| 24 | "no two electrons can be in exactly the same state" | PASS | checks/check_C3_08.py: the antisymmetrized f(x1)f(x2) - f(x2)f(x1) = 0 |
| 25 | Check yourself: three rungs give at most 3 lines "(visible or not)" | PASS | checks/check_C3_08.py: 3 pairs with distinct gaps of 1.889, 10.2 and 12.089 eV |

## Figures
- c-ladder-spectrum: figures/c-ladder-spectrum.png, re-plotted by checks/fig_c-ladder-spectrum.py.
  - The bottom strip is retitled "hydrogen's lines: positions to scale (brightness only suggested)". The old "glowing hydrogen, as actually seen" is gone.
  - Line heights now fall steadily with n. They are computed from the relative Balmer line power (hydrogen radial integrals, equal population per state), compressed as power^0.35 so the faint lines stay visible. The four lines are no longer drawn at equal strength.
  - The shaded band on the bottom strip is labelled "UV". Lines below 380 nm are drawn grey.
  - Positions are to scale (air wavelengths). The series limit at 364.6 nm is dotted.
  - The figure now matches the final-C.md caption.
- c-standing-waves: figures/c-standing-waves.png, unchanged. The labels are true for the ideal string drawn: "1 hump: fits (lowest note)", "2 humps: fits (higher note)", "3 humps: fits (higher still)", and "2.5 humps: misses the pinned end, can't ring steadily" (sin(2.5 pi) = 1 at the pinned end). They agree with the caption.

## Notes
- "Four bright lines" is a convention ("the four visible lines"). The brightness falls steadily, and H-delta is only about 1.6 to 1.8 times brighter than H-epsilon (check_C3_06.py). The figure shows this gradual fall. To the eye, H-epsilon at 397 nm is far dimmer still, because eye sensitivity drops steeply below 410 nm.
- Relative line strengths in a real source depend on how the atoms are excited (discharge versus nebula). The figure's brightness is therefore labelled as suggested only.
- The 3p lifetime (5.4 ns) and the 2s two-photon rate (8.23 /s) are literature values used for context, not computed here.
- Quoted wavelengths are air values. Vacuum values are about 0.18 nm longer for H-alpha.
- The c-standing-waves figure has no legend for its dashed grey curves (the string half a cycle later). This is optional to add.
