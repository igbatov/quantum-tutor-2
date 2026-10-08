VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "for a silver atom ... only two possible answers, ever" | PASS | checks/check_B_01_2.py: the eigenvalues of S·n are ±1/2 for every axis; Ag ground state J=1/2 gives 2J+1 = 2 |
| 2 | "tiny magnet, because of one of its electrons" | PASS | checks/check_B_01_2.py: the electron moment is about 16,200 times the Ag-107 nuclear moment |
| 3 | "other kinds of atom can give a different number of spots, but always a definite number" | PASS | checks/check_B_13_2.py: 2J+1 is an integer for every J. Examples: Zn 1, Ag/H 2, O 5, Cr 7, Fe 9, Dy 17 |
| 4 | "every value between the two extremes ... one continuous band"; caption "evenly", "empty gap exactly where the classical band is as full as anywhere" | PASS | checks/check_B_02_2.py: pdf of cos θ is 1/2 (sympy). Sampled density ranges 0.495–0.511 and is 0.501 at the centre. The idealized quantum panel's density at the centre is 1e-34 of its peak |
| 5 | "field much stronger near one of them"; "pushes ... along the pole-to-pole line" | PASS | checks/check_B_03_2.py: in the knife-edge model, \|B\| is 6× larger near the edge, and ∂\|B\|/∂x = 0 at the beam centre |
| 6 | "bands join at their ends, where the field, and its unevenness, are weaker" | PASS | checks/check_B_03_2.py: along the slit, \|B\| falls from 1.00 to 0.32 and \|∂B/∂z\| from 1.00 to 0.03. The round-1 wording note is resolved |
| 7 | Z,Z "all ... up"; Z,X "half left, half right"; Z,X,Z "half up, half down" | PASS | checks/check_B_04_2.py: probabilities 1/0, 1/2/1/2, 1/2/1/2; counts 1000→500→500/0, 250/250, 125/125 |
| 8 | "certain at the pole, 50/50 at 90°, zero at the opposite pole ... nearer a pole, the likelier" | PASS | checks/check_B_05_2.py: P = cos²(θ/2), monotonic |
| 9 | "'left' is 90° from both up and down"; "no point ... at a Z pole and an X pole at once" | PASS | checks/check_B_05_2.py: ⟨σz⟩ = 0 for X eigenstates; [σx,σz] ≠ 0 and the two share no eigenvector |
| 10 | "points arrive scattered evenly ... every count in the figure follows" | PASS | checks/check_B_06_2.py: the sphere average gives ρ = I/2, so P = 0.5 along z and along x. Together with row 7 this reproduces every figure count |
| 11 | sieve "fits the first three experiments; the third magnet kills it" | PASS | checks/check_B_07_2.py: the label model predicts 100% up at the third magnet; 50% is observed |
| 12 | chance rule "checked at many angles with neutrons" | PASS | checks/check_B_08_2.py: the neutron is spin 1/2, and P_up after a rotation by θ equals cos²(θ/2) to 0 error at 181 angles. The historical fact itself was not checked. The light/polarizer claim from round 1 has been removed |
| 13 | "a qubit is exactly one of these globes" | PASS | checks/check_B_12_2.py: pure C² states map one-to-one onto unit Bloch vectors (up to a global phase) |
| 14 | "north" and "south" pieces "in proportions set by the angle"; "one state described two ways" | PASS | checks/check_B_14_2.py: \|north\| = cos(θ/2) decreases as θ grows, the norm is 1, the Bloch vector rebuilt from the pieces equals the point, and \|north\|² = Model 1's chance |
| 15 | packets "fly apart"; chances "given by the squared sizes"; Models 1 and 2 "never disagree" | PASS | checks/check_B_09_2.py: packet weights 1.000/0.750/0.500/0.250 equal cos²(θ/2); packet overlap is about 3e-6 |
| 16 | steer packets back together, "'up' every time (in an ideal set-up; ... nearly)" | PASS | checks/check_B_09_2.py: the ideal loop gives P(up) = 1.000000; a 0.2% force mismatch gives 0.961 |
| 17 | pilot-wave: "fixed by exactly where in the beam it started"; "No up/down label" | PASS | checks/check_B_10_2.py: trajectories never cross, a threshold start position decides the outcome, and the fraction going up is 0.500 / 0.750 |
| 18 | pilot-wave: "... and how the magnet is set" | PASS | checks/check_B_15_2.py: a Z-up atom starting at z = -0.5 ends up (+22) in a Z magnet and down (-23) in an X magnet. Unpredictability "in principle" rests on the quantum-equilibrium postulate, which can't be computed |
| 19 | collapse "until ... amplified into a large record"; "For a lone atom ... far too weak"; "fourth changes the theory slightly" | PASS | checks/check_B_11_2.py: a lone Ag atom collapses in 3e4 to 3e6 yr. The chance of a collapse during a 1–10 ms flight or loop is 1e-15 to 1e-14 (nonzero, negligible). A record with 1e18 to 1e23 nucleons collapses in 1e-2 to 1e-7 s. The round-1 FAIL is fixed |
| 20 | "erase the answers to incompatible questions" | PASS | checks/check_B_16_2.py: [Z,Z] = 0 and Z,Z keeps P(up) = 1; \|\|[Z,X]\|\| = 2.83 and Z,X(left) drops P(up) to 0.5 |
| 21 | "two-answer magnetism ... hydrogen nuclei ... MRI" | PASS | checks/check_B_12_2.py: the proton has I = 1/2, so 2I+1 = 2 |
| 22 | Check yourself: X-left into X, fraction "left" | PASS | checks/check_B_04_2.py: \|⟨L\|L⟩\|² = 1, so the answer is 100% (not stated in the text) |

Pass count: 22/22.

## Figures
- b-smear-vs-two: figures/b-smear-vs-two.png (reused, not redrawn). It matches the new caption: the classical panel is uniform on [-1,1] (row 4) and the quantum panel shows two clumps with the empty gap marked. The note on the figure says "where the field is weaker". That is consistent with the text's "the field, and its unevenness, are weaker", though less complete.
- b-three-magnets: figures/b-three-magnets.png (reused, not redrawn). The counts match the caption and row 7. The row notes say "same answer", "50/50", "old answer gone".

## Notes
- Historical claims were not checked computationally: neutron angle tests, the recent full-loop atom interferometer, and the null results for collapse with large molecules and tiny vibrating devices. Their physics is consistent (rows 12, 16, 19).
- Row 10: the evenly scattered source is a mixture (ρ = I/2), not a single point on the globe. Treating it as a population of points gives identical statistics.
