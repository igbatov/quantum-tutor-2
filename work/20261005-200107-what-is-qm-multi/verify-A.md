VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "crash into the proton in roughly 10^-11 seconds (a hundred-billionth...)" | PASS | checks/check_A_01.py: Larmor in-spiral from a0, t = a0^3/(4 r_e^2 c) = 1.56e-11 s; 1/100e9 = 1e-11 |
| 2 | "the frequency of its light would rise smoothly" | PASS | checks/check_A_02.py: circular Coulomb orbit omega ∝ r^(-3/2), d omega/dr < 0 for all r > 0 |
| 3 | "about 656, 486, 434, 410 nm" (Rydberg, R_H = 1.0968e7 /m) | PASS | checks/check_A_03.py: 656.46, 486.26, 434.16, 410.28 nm; same from E_n = -13.598/n^2 eV to within 0.01 nm |
| 4 | "just four sharp visible colors" | PASS | checks/check_A_03.py: exactly 4 Balmer lines in 400-700 nm; next are 397 and 389 nm (see Notes) |
| 5 | "E_n = -13.6/n^2 eV" (figure spec) | PASS | checks/check_A_03.py and check_A_05.py: hydrogen Rydberg energy 13.598 eV (reduced mass), minimum of the energy balance is -13.606 eV |
| 6 | "Planck's constant h ... about 6.6 x 10^-34 ... joule-seconds" | PASS | checks/check_A_04.py: h = 6.62607015e-34 J s (0.4% from 6.6e-34) |
| 7 | "about a tenth of a nanometer (a ten-millionth of a millimeter) across" | PASS | checks/check_A_05.py: 2 a0 = 0.106 nm; 1e-3 mm/1e7 = 1e-10 m = 0.1 nm |
| 8 | "Squeezing a wave costs energy ... The best balance is the bottom rung" | PASS | checks/check_A_05.py: minimizing hbar^2/(2 m r^2) - k e^2/r gives r = a0 exactly, E = -13.606 eV |
| 9 | "low frequencies as red and high ones as violet" | PASS | checks/check_A_06.py: f(700 nm) = 4.28e14 Hz < f(400 nm) = 7.50e14 Hz |
| 10 | Check-yourself answer (wider rungs -> bluer) | PASS | checks/check_A_06.py: larger drop gives higher f and shorter lambda (1.9 eV -> 653 nm, 3.0 eV -> 413 nm) |
| 11 | "give off its photon within the next nanosecond" (ns is the right timescale) | PASS | checks/check_A_07.py: H 2p lifetime = 1.60 ns; P(decay within 1 ns) = 0.47 |

## Figures
- a-hydrogen-ladder: figures/a-hydrogen-ladder.png (script checks/fig_a-hydrogen-ladder.py). Wavelengths come from the Rydberg formula with R_H = 1.0968e7 /m. Every line and arrow has a text label, so the figure reads without colour.

## Notes
- "Four visible colors" depends on where you put the edge of the visible range. H-epsilon (7→2) is at 397 nm, and some people can faintly see it. "Four" is the standard textbook statement, so this is fine. The figure's 380-700 nm axis would technically include 397 and 389 nm, but the spec asks for only four lines, so only four are drawn.
- The computed wavelengths are vacuum values (656.46 nm). Tables of air wavelengths give 656.28 nm. Both round to 656.
- The 10^-11 s figure assumes the classical in-spiral starts at the Bohr radius, which is the standard estimate.
- Not checked by computation (no data offline, and the claims are descriptive): neon glows red-orange and sodium yellow (the sodium D line is about 589 nm, which is consistent).
