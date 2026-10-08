VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "Ordinary light meets a vertical filter ... Half" | PASS | checks/check_C_01.py: angle-average of cos^2 = 1/2; Tr(P_V rho_unpol) = 0.5; post-state is pure vertical |
| 2 | "All pass a vertical filter, none ... horizontal ... half pass at 45°" | PASS | checks/check_C_02.py: probabilities 1, 0, 0.5; any 45° separation gives 0.5 (tested 37 orientations) |
| 3 | "A hidden mix of vertical and horizontal photons would give half ... all of them pass" | PASS | checks/check_C_03.py: any V/H mixture gives 0.5 at 45°; pure 45° state gives 1 |
| 4 | "a vertical piece and a horizontal piece, each about 0.71" | PASS | checks/check_C_04.py: cos 45° = 1/sqrt(2) = 0.7071 |
| 5 | "0.71 x 0.71, about 0.5" | PASS | checks/check_C_04.py: 0.71^2 = 0.5041, exact (1/sqrt2)^2 = 1/2 |
| 6 | "A vertical arrow is equally a superposition of the two diagonals" | PASS | checks/check_C_04.py: V = (1/sqrt2)D45 + (1/sqrt2)D135, residual 0 |
| 7 | "Crossed filters ... let nothing through" | PASS | checks/check_C_05.py: chain V then H gives 0 |
| 8 | "1/2 x 1/2 x 1/2 = 1/8" with 45° filter inserted | PASS | checks/check_C_05.py: projector chain 0.125; single-photon Monte Carlo (4e5 photons) 0.1246 |
| 9 | "A classical wave of bright light also gives one-eighth" | PASS | checks/check_C_05.py: Malus's law (1/2)cos^2 45° cos^2 45° = 0.125 |
| 10 | "sure answer to one is 50/50 on the other ... no state has sure answers to both" | PASS | checks/check_C_06.py: V/H (sigma_z) and diagonal (sigma_x) bases have all overlaps^2 = 1/2; [Z,X] != 0; no common eigenvector; Var Z + Var X = 1 for all real polarization states |
| 11 | "adds their amplitudes before squaring ... can cancel" / stripes vanish with which-path record | PASS | checks/check_C_07.py: coherent sum visibility 1.000, incoherent (recorded) sum visibility 0 |
| 12 | "their waves have unimaginably short wavelengths" | PASS | checks/check_C_08.py: baseball (0.145 kg, 40 m/s) lambda = 1.1e-34 m, ~1e-19 of a proton's size (CODATA h) |
| 13 | Check-yourself: vertical -> 45° -> horizontal -> 45° | PASS | checks/check_C_09.py: well-posed, answer 1/8 of the light leaving the vertical filter |

## Figures
- c-shadow: figures/c-shadow.png (checks/fig_c-shadow.py; components computed as sin/cos 45°, chance = amplitude^2; insets with shadow 1/chance 1 and shadow 0/chance 0)
- c-filters: figures/c-filters.png (checks/fig_c-filters.py; stage fractions computed via Malus chain: 1, 1/2, 0 and 1, 1/2, 1/4, 1/8)

## Notes
- "Whenever a photon's arrow and a filter are 45° apart, half pass" holds for linearly polarized photons (the only kind in the text); fine as stated at this level.
- The Check-yourself answer (1/8) is relative to light leaving the vertical filter, as the question words it; relative to original unpolarized light it would be 1/16. Exam/answer key should use the question's reference.
- "0.71 x 0.71, about 0.5" is correctly hedged ("about"); exact value is 1/2.
