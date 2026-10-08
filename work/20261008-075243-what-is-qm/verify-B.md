VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "only two possible answers, ever: hence two spots" | PASS | checks/check_B_01.py: eigenvalues of S·n are exactly ±1/2 for every axis n; Ag ground state J=1/2 gives 2J+1 = 2 |
| 2 | "a tiny magnet because of one of its electrons" | PASS | checks/check_B_01.py: the unpaired 5s electron's moment is about 16,000 times the Ag-107 nuclear moment |
| 3 | "push would take every value between the two extremes ... one continuous band" | PASS | checks/check_B_02.py: for isotropic directions cos θ has a flat density of 1/2 on [-1,1] (sympy); sampled histogram is 0.49–0.51 everywhere, centre included |
| 4 | "field is much stronger near one pole"; pushes "along the line from one pole to the other" | PASS | checks/check_B_03.py: knife-edge (line-source) model gives \|B\| 6× larger near the edge; at the beam centre ∂\|B\|/∂x = 0, so the force is along z only |
| 5 | "two bands join at their ends, where the field is weaker" | PASS | checks/check_B_03.py: along the slit, \|B\| falls 1.00→0.32 and \|∂B/∂z\| (which sets the splitting) falls 1.00→0.03, so the bands close up at the ends (see Notes on wording) |
| 6 | Z then Z "all come out up"; Z then X "half left, half right"; then Z "half up, half down" | PASS | checks/check_B_04.py: Born probabilities 1, 0; 1/2, 1/2; 1/2, 1/2; figure counts 1000→500→500/0, 250/250, 125/125 reproduced |
| 7 | "certain at the pole, 50/50 at 90°, zero at the opposite pole ... nearer a pole, the likelier" | PASS | checks/check_B_05.py: P = cos²(θ/2) is 1, 1/2, 0 at 0°, 90°, 180°, and decreases monotonically in between |
| 8 | "'left', which is 90° from up and from down"; "no point ... at a Z pole and an X pole at once" | PASS | checks/check_B_05.py: ⟨σz⟩ = 0 for X eigenstates; [σx,σz] ≠ 0 and they share no eigenvector |
| 9 | "points scattered evenly over the globe: half up, half down" | PASS | checks/check_B_06.py: the sphere average gives ρ = I/2, so P = 0.500 along z and along x |
| 10 | fixed-label sieve "fits the first three experiments; the third magnet kills it" | PASS | checks/check_B_07.py: label model reproduces two spots, 100% up, and 50/50 left/right, but predicts 100% up at the third magnet (observed 50%) |
| 11 | chance rule checked "with the polarization of light, another two-answer system" | PASS | checks/check_B_08.py: Malus cos²φ is identical to cos²(θ/2) with θ = 2φ on the Poincaré sphere (max difference 0) |
| 12 | wave splits into two packets, "chances given by the squared sizes" (and Model 1 and Model 2 "never disagree") | PASS | checks/check_B_09.py: split-step SG simulation, packet weights 1.000/0.750/0.500/0.250 equal cos²(θ/2) at 0°/60°/90°/120°; packet overlap ~3e-6 |
| 13 | steer packets back together, "later Z magnet gives 'up' every time" (ideal), "nearly" in practice | PASS | checks/check_B_09.py: full-loop recombination gives P(up) = 1.000000; a 0.2% force mismatch gives 0.961 |
| 14 | pilot-wave: outcome "depends on exactly where in the beam it started ... no up/down label" | PASS | checks/check_B_10.py: Bohmian trajectories never cross; every start above a threshold z* goes up and every start below goes down; the fraction going up is 0.500 for P=0.5 and 0.750 for P=0.75 |
| 15 | objective collapse: packets "persist until the plate, where the vast number of particles involved triggers ... localization within a tiny fraction of a second" | FAIL | checks/check_B_11.py: with standard GRW/CSL parameters (λ = 1e-16 s⁻¹, r_C = 100 nm), one Ag atom landing at the upper vs the lower spot localizes only after about 3e4 to 3e6 years. The glass atoms it disturbs move about 1e-11 m, far below r_C, so they add nothing. Fast localization (1e-2 to 1e-7 s) needs about 1e18 to 1e23 nucleons displaced, as in an amplified record. Correct statement: "the packets are real and persist until the atom's arrival is amplified into a large record (a visible deposit, a detector's current); there the vast number of particles moved triggers a genuine, random localization within a tiny fraction of a second." |
| 16 | "a qubit is exactly one of these globes" | PASS | checks/check_B_12.py: 1000 random normalized C² states each map to a unit Bloch vector, and the vector reconstructs the state up to a global phase |
| 17 | "two-answer magnetism in the hydrogen nuclei ... MRI" | PASS | checks/check_B_12.py: proton I = 1/2 gives 2I+1 = 2 orientations |
| 18 | Check yourself: X-left into X, fraction "left" | PASS | checks/check_B_04.py: P = \|⟨L\|L⟩\|² = 1, so the expected answer is 100% (not stated in the text; consistent) |

Pass count: 17/18.

## Figures
- b-smear-vs-two: figures/b-smear-vs-two.png (checks/fig_b-smear-vs-two.py). The classical panel uses deflection ∝ cos θ for isotropic moments, which matches the requested uniform distribution on [-1,1] (check_B_02). The quantum panel is labelled as the idealization, and the note about the real plate is included. An "empty gap" arrow marks the feature.
- b-three-magnets: figures/b-three-magnets.png (checks/fig_b-three-magnets.py). All counts come from Born probabilities, the "take these" paths are drawn in bold, and each row has an italic note (same answer / 50/50 / old answer gone).

## Notes
- Row 5: the splitting is set by the field gradient, not by the field strength. In the knife-edge geometry both fall off toward the slit ends, so the sentence is true. Saying "where the field's non-uniformity is weaker" would name the actual cause more precisely. Optional change.
- Row 15 is the only FAIL and needs only a small rewording. It matters for the 1922 setup in particular: the deposit was invisible until it was chemically developed, so the large record the collapse needs came later.
- "This has been done with atoms in recent years" (the full-loop Stern–Gerlach interferometer) and "experiments with large molecules and tiny vibrating devices have so far found no sign of collapse" are historical/empirical claims. I checked their physics (rows 13 and 15) but not the historical facts.
- Row 16: the globe's surface holds the pure states. The evenly scattered source in row 9 is a mixture (centre of the ball). The text treats it as a population of surface points, which gives the same statistics.
