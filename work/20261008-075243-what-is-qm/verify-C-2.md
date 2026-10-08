VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "red (656 nm) ... violet (410 nm)", "(397, 389, 384 nm)", "7, 8 and 9 to 2" | PASS | checks/check_C_01_2.py: air wavelengths with reduced mass for n=3..9 to 2 are 656.29, 486.14, 434.05, 410.18, 397.01, 388.91 and 383.54 nm. Exactly 4 lines at 400 nm or longer, and exactly 7 at 380 nm or longer. The series limit is 364.6 nm. Lyman lines span 91-122 nm (deep UV) and Paschen lines span 821-1876 nm (IR). |
| 2 | Bohr reproduces lines of "ionized helium" | PASS | checks/check_C_01_2.py: Z^2 scaling with the He-4 reduced mass gives He II 4 to 3 at 468.58 nm (observed 468.57). |
| 3 | Table entry for 3 to 2 = "difference between the two rungs' clock-hand rates" | PASS | checks/check_C_01_2.py: (E3-E2)/h = 4.566738e14 Hz, equal to c/lambda_vac to 1e-12. |
| 4 | "fainter and fainter lines crowding together at the violet edge" | PASS | checks/check_C_02_2.py: line power with equal population per state (g_n A_n2 h nu, from exact radial integrals), relative to H-alpha, is 1, 0.46, 0.24, 0.14, 0.090, 0.060, 0.042 for n=3..9. f(2 to n) = 0.641, 0.119, 0.045, ... decreases monotonically. Successive line spacings shrink: 170, 52, 24, 13, 8.1, 5.4 nm. |
| 5 | "about every 4.9 volts", "254 nm ... 4.9 eV", "neighbours at 4.7 and 5.5 eV" | PASS | checks/check_C_03_2.py: NIST Hg I levels are 6s6p 3P0 = 4.667 eV, 3P1 = 4.887 eV and 3P2 = 5.461 eV. A 253.65 nm photon carries 4.888 eV. |
| 6 | "bounces off ... only a minute recoil share"; "(bar a minute recoil)" | PASS | checks/check_C_03_2.py: the maximum elastic loss fraction for an electron on Hg is 4mM/(m+M)^2 = 1.09e-5, which is 0.05 meV at 4.9 eV. The H-alpha emission recoil fraction is 1.0e-9. |
| 7 | "can ... be taken as simply positive or negative"; clock hands "all turn together, at a rate set by its energy" | PASS | checks/check_C_04_2.py (sympy): the real 1s, 2p_z, 2p_x and 3d_xy functions satisfy H psi = E_n psi exactly. psi e^{-iE t/hbar} solves the TDSE. The ratio of amplitudes at two points does not depend on time. |
| 8 | "rungs ... crowd into bands so dense they act as continuous, often with gaps between" | PASS | checks/check_C_06_2.py: a tight-binding chain with two orbitals per atom gives N levels per band. The maximum spacing falls as 1/N (1.6e-3 at N=2000, about 6e-23 eV at N=1e23). Two bands of width 4t are separated by a gap of 2.4. |
| 9 | Figure c-ladder-lines vs text (round-one item 17) | PASS | checks/check_C_07_2.py: the text now names the 397/389/384 nm lines, so it matches the figure. The 380-700 nm window holds 7 lines, and the figure draws 4 solid and 3 dotted (rungs 7-9, not on the ladder) as the caption says. The ladder values are -13.60, -3.40, -1.51, -0.85, -0.54, -0.38 eV. |
| 10 | "every line shifted by the same fraction" | PASS | checks/check_C_05_2.py, which reruns check_C_02.py: the shift is equal for all lines to 1e-12, under both z and Doppler. |
| 11 | "heavy hydrogen's lines sit slightly apart" | PASS | check_C_05_2.py runs check_C_03.py: D-alpha is 0.18 nm from H-alpha. |
| 12 | "about a ten-billionth of a metre across" | PASS | check_C_05_2.py runs check_C_04.py: 2a0 = 1.06e-10 m. |
| 13 | "spiral into the nucleus in about a hundred-billionth of a second ... continuously changing smear" | PASS | check_C_05_2.py runs check_C_06.py: 1.56e-11 s, and the orbital frequency rises monotonically. |
| 14 | "lowest state has no orbiting at all"; pilot-wave "sits still", "energy of the wave's push" | PASS | check_C_05_2.py runs check_C_07.py: L^2 psi = Lz psi = 0, the Bohm velocity is 0, and <Q> = <T> = 13.6 eV. |
| 15 | "one half-wave, two, three, never two and a half" | PASS | check_C_05_2.py runs check_C_08.py: sin(2.5 pi) = 1, so the end is not fixed. |
| 16 | "not evenly spaced but crowd together towards the top"; "No rung lies below it" | PASS | check_C_05_2.py runs check_C_09.py: the gaps strictly decrease towards 0 eV, and E_1 is the minimum. |
| 17 | "half the wavelength, four times the energy" | PASS | check_C_05_2.py runs check_C_10.py: the ratio is exactly 4. |
| 18 | "nucleus's pull favours small patterns, the bending cost ... balance" | PASS | check_C_05_2.py runs check_C_11.py: the minimum is at the Bohr radius, E = -13.606 eV. |
| 19 | "an atom typically drops within a millionth of a second" | PASS | check_C_05_2.py runs check_C_12.py: 19 of the 20 nl states for n=2..6 decay in under 1 us. The exception is the metastable 2s. |
| 20 | "beyond a few electrons exact computation is impractical" | PASS | check_C_05_2.py runs check_C_13.py: 4 electrons need 4e15 grid values and 10 electrons need 1e39. |
| 21 | "so rarely for one electron that a single atom is practically unaffected"; "far too small to show there" | PASS | check_C_05_2.py runs check_C_14.py: the collapse probability during an excited-state lifetime is at most about 1.6e-17. |
| 22 | "predicts hydrogen's lines to better than a part in a billion" | PASS | check_C_05_2.py runs check_C_15.py: R_inf has a relative uncertainty of 1.1e-12. |
| 23 | Check yourself: three rungs, at most how many wavelengths | PASS | check_C_05_2.py runs check_C_16.py: there are 3 distinct gaps. |

## Figures
- c-string-fits: figures/c-string-fits.png (reused). The caption still matches: whole half-waves, the 2.5 case in red with a cross, and half the room giving half the wavelength and "4x the energy of motion".
- c-ladder-lines: figures/c-ladder-lines.png (reused). The caption now matches the figure: 4 bright lines, 3 dotted lines from rungs 7-9 at the violet edge, those rungs not drawn on the ladder, and a grey dashed 122 nm UV drop.

## Notes
- Item 7: the real-valued picture needs real combinations of degenerate states, such as 2p_x = (m=+1 and m=-1 combined). A definite-m state like R21 sin(theta) e^{i phi} is not real at any one moment. The text's "can ... be taken as" covers this.
- Item 4 assumes equal population per state, which favours high n. Real discharges populate high n less, so the lines fade even faster.
- Not computable, left to the critic: the Franck-Hertz remark that real curves are "shifted a volt or so" (contact potential), "the step spacing wanders slightly", and Bohr's "rough estimates of line brightness". The round-one notes on objective collapse wording and the 4.9 eV "most readily" claim are resolved in this version.
