## Scores
| Candidate | Strategy | Core idea | Level fit | Example | Analogies | Misconceptions | Pacing | Transfer | Total |
|---|---|---|---|---|---|---|---|---|---|
| A | One arm, one clock hand (interferometer, 2x2 unitary matrices, p-norms) | 5 | 4 | 5 | 5 | 5 | 4 | 3 | 31 |
| B | Clocks that keep their length (stationary states, beats, flow, conservation law) | 4 | 3 | 4 | 4 | 3 | 3 | 5 | 26 |
| C | Three ways to be fifty-fifty, and three slits (counting) | 5 | 3 | 5 | 5 | 4 | 3 | 3 | 28 |

## Pairwise
- A vs B: A (slight). A answers both halves with one device and 2x2 matrices I can multiply, defines every term, and explicitly corrects the quick answer's neutron-720° and 2^{1-p/2} claims. B's derivations are fuller, but two central steps make jumps I can't make: the momentum average written with −iħ d/dx, and "H21 = conj(H12) is the condition that the energies come out real", which the conservation proof depends on. Those are real stumbling points, but B's conservation argument is a genuine "why 2" that I could follow in most other places, so the gap is not decisive.
- A vs C: A (slight). C's "why complex" (two even-bet sorters vs three) is the most robust and calculator-checkable argument of the three and does not depend on the square. But its "why 2" is a measured signature (three-slit null), and it says so itself ("shows the world has the square's signature, not why"), while A gives a reason (continuous lossless mixing) plus the same Gleason closer. C's later sections also bring in undefined machinery (density matrix, trace, Bloch ball, kets). Neither difference is decisive.
- B vs C: C (slight). C's core arguments are 2-vector arithmetic at my level, and the quarter-wave plate as "multiplication by i" is very concrete. B needs the Schrödinger PDE, conjugate equations and operators. B's conservation law is the more physical "why" for the 2, though, and B has the best Check question.

## Decision
WINNER: A
MARGIN: slight
FINALISTS: A, C, B

## Notes for the learner
- A (interferometer and matrices): suits you if you want both answers from one apparatus with 2x2 matrices you can multiply yourself, and it is the most careful about what the quick answer got wrong. Weakest point: the "why 2" rests on a cited theorem (Banach–Lamperti), and the worked example rules out only one family of matrices.
- C (three sorters and three slits): suits you if you want the most hands-on, assumption-light reason for the i (it builds on the polarizer picture you chose before) and a measured test of the 2. Weakest point: the three-slit test shows the square's fingerprint rather than why, and the later sections use density matrices and kets without defining them.
- B (stationary states and conservation): suits you if you want "why 2" as a conservation law derived step by step from the Schrödinger equation, plus a real exercise at the end. Weakest point: it is the most calculus-heavy, and a few steps (the momentum operator, "energies come out real") are not explained at your level.

## Notes for revision
- A: The Check yourself question has its answer already printed twice (observation (d) and the "(d)" check: ¼ at each exit). Replace it with a new case, e.g. plate at φ = 60° with arm 2 blocked, or a second plate in arm 2. In Model 3, add one line showing that a slightly mixing matrix changes the p-total for some input when p ≠ 2 (e.g. a small rotation applied to (1,0) with p = 4), so the gradual case is shown and not only cited.
- C: Define or cut "density matrix", "Hermitian matrix of trace 1", "Bloch ball", "Tr(ρP)" and the |a⟩|A⟩ notation in Model 3 and in the Zurek step. The second half of Check yourself ("what unpolarized light must be") needs mixtures and the inside of the sphere, which the text barely mentions. Add two lines on mixtures or drop that half. Trim the length (six figures and the Wootters count make it the longest).
- B: Explain ⟨p⟩ = ∫ψ̄(−iħψ′)dx in words or cut it (the current J argument already makes the point). Show in two lines why H21 = conj(H12) makes the two energies real, or state it plainly as an assumption. Also say that the ammonia p-total table uses square-keeping dynamics, so on its own it only illustrates the point and the theorem does the work, as A does for its 2^{1-p/2} line. The opening sentence packs three inferences into one; split it.
