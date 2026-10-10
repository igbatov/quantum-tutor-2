VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "R = 3.29 × 10^15 Hz", Balmer-α 4.57e14 Hz / 656 nm, Lyman-α 2.47e15 Hz / 122 nm, Balmer-β 6.17e14; "R(1/4 + 1/9) = 1.19e15 Hz … is not a hydrogen line"; caption "crowd below 0.83e15 Hz", Lyman "up to 3.29e15 Hz", the cross "sits in a gap" | PASS | checks/check_B_01_2.py: R_H c = 3.2881e15 Hz; 4.567e14 Hz (656.5 nm), 2.466e15 Hz (121.6 nm), 6.165e14 Hz. The sum is 1.187e15 Hz, 31% away from the nearest line (n ≤ 400). No line lies between the Balmer limit (8.22e14 Hz) and Lyman-α. The "coincides only when it equals a difference" wording is true as written. |
| 2 | "1.6 ns for the state that emits Lyman-α" | PASS | check_B_01_2.py: A(2p→1s) = (2/3)^8 α^5 μc²/ħ gives 1.596 ns |
| 3 | "254 nm, whose hf is 4.9 eV" | PASS | check_B_02_2.py: 4.887 eV |
| 4 | "'along' is the lower"; "at 1 T the two differ by h × 42.6 MHz" | PASS | check_B_02_2.py: E = −μ·B; 2μ_p B/h = 42.577 MHz (CODATA) |
| 5 | ammonia "2A/h ≈ 24 GHz"; "1.67 × 10⁻¹⁰ m at 54 eV" | PASS | check_B_02_2.py: 23.870 GHz (literature value, not CODATA); h/√(2m_e·54 eV) = 1.669e-10 m |
| 6 | Rabi "in the ideal case, on resonance and without losses, the swing is from 0 to 1" | PASS | check_B_02_2.py: the maximum is 1.0000 on resonance and 0.80 at detuning Ω/2, so "on resonance" is needed and is stated |
| 7 | "c² = ½ + ½cos(2Et/ħ)", table rows, "dip to zero twice per period", the pulsing would move with the zero of energy; pendulum and circular polarization keep energy and intensity fixed with two reals | PASS | check_B_03_2.py: sympy identity; the table matches to 3 decimals; the zeros are π/2 and 3π/2; v²/2 + ω²x²/2 and cos² + sin² are constant |
| 8 | "\|ψ\|² = … = A²" (each step) | PASS | check_B_04_2.py (sympy) |
| 9 | "½\|c1 + c2\|² = … = ½(a² + b² + 2ab cos((ω2 − ω1)t))"; unequal shares change "depth … timing but not its frequency" | PASS | check_B_04_2.py: each step has sympy difference 0. With complex shares 0.8 and 0.6e^{0.9i}, the FFT shows only ω2 − ω1 |
| 10 | real attempt "(c1 + c2)² = …" with 2ω1, 2ω2, ω1 + ω2 | PASS | check_B_04_2.py (sympy, expand_trig) |
| 11 | caption b-stationary-vs-cos: hand rule "½(1 + cos 0.1t)", real rule "¼(cos ω1t + cos ω2t)² … pulses at ω1 + ω2 … inside that same slow envelope", beat period 20π | PASS | check_B_04_2.py: ¼(cos t + cos 1.1t)² = cos²(1.05t)·cos²(0.05t), and cos²(0.05t) equals the hand rule exactly. Peak 1.0. The figure script plots these on 0–20π. |
| 12 | Spin worked: "E_a = −ħω/2", "c_a = e^{+iωt/2}/√2", "\|c_a\|² = ½", "+x" amplitude "cos(ωt/2)", chance "½(1 + cos ωt)", "−x" amplitude "i sin(ωt/2)", "add to 1" | PASS | check_B_05_2.py: the c's solve iħċ = Ec, and every identity holds in sympy |
| 13 | caption: tipped 60°, along-field part "cos 60° = 0.5", transverse "0.866 cos(2πt/T)" | PASS | check_B_05_2.py: ⟨σz⟩ = 0.5 and ⟨σx⟩ = sin 60° cos ωt at 11 times over 5 periods |
| 14 | Check yourself: "chance of +y is ½(1 − sin ωt)"; first −y, then +y | PASS | check_B_05_2.py: sympy gives ½ − ½ sin ωt. The spin first points along −y at t = T/4 and along +y at 3T/4. This matches the classical Bloch precession dM/dt = γM × B with γ > 0 (M(T/4) = −ŷ), so the sign issue from round 1 is resolved. |
| 15 | continuity derivation: V terms cancel; "(iħ/2m)(ψ̄ψ'' − ψψ̄'')"; the derivative identity; "J = (iħ/2m)(ψψ̄' − ψ̄ψ') = (ħ/m) Im(ψ̄ψ')" | PASS | check_B_06_2.py: sympy with ψ = u + iv and real V |
| 16 | real ψ ⇒ "J = 0"; "the equation gives a real ψ an imaginary part at once"; plane wave "J = (ħk/m)\|A\|²"; standing wave J = 0; "real at all times … Hψ = 0" | PASS | check_B_06_2.py: for a real Gaussian, ∂ψ/∂t is purely imaginary and nonzero. For real ψ(x,t), solving the real and imaginary parts forces ψ_t = 0 and Hψ = 0. |
| 17 | Model 2: "once per de Broglie wavelength"; caption "longer … by about y²/D", "y = 1 means an extra quarter wavelength", far routes "contribute far less per unit of y" | PASS | check_B_07_2.py: pλ/ħ = 2π; exact extra length / (y²/D) = 0.9998–0.99999 for y ≪ D. Fresnel phase (π/2)u² is a quarter turn at u = 1. \|sum\| per unit y is 0.895 for \|u\| ≤ 1 and 0.083 for 5 < u < 6. |
| 18 | "d\|c1\|²/dt = … = (2/ħ) Im(H12 c̄1c2)" (each step); c2 rate "(1/iħ)(H̄12 c1c̄2 − H12 c̄1c2) = −(2/ħ)Im(…)"; sum = 0 | PASS | check_B_08_2.py (sympy, H12 = h_r + i h_i general complex) |
| 19 | "−iΓ would make \|c1\|² decay as e^{−2Γt/ħ}" | PASS | check_B_08_2.py |
| 20 | "H11 = H22 = 0, H12 = 1, H21 = 4 has the real energies ±2" | PASS | check_B_08_2.py: eigenvalues ±2 |
| 21 | "yet under it \|c1\|² + \|c2\|² grows" | FAIL | check_B_08_2.py: the total does not grow steadily; it oscillates. Started in level 1 it is 1 + 3 sin²(2t/ħ), swinging between 1 and 4. Started in level 2 it swings between 1 and 1/4, so it first shrinks. Correct statement: "yet under it \|c1\|² + \|c2\|² does not stay fixed: started in level 1 it is 1 + 3 sin²(2t/ħ), swinging between 1 and 4." |
| 22 | ammonia "c1 = cos(At/ħ), c2 = i sin(At/ħ)" both checks ✓; "a real c2 = sin(At/ħ) fails the first check" | PASS | check_B_08_2.py: residuals 0, 0; real c2 leaves a residual of A(1 − i) sin(At/ħ) |
| 23 | p-table; "2·(1/√2)^p = 2^{1−p/2}"; "below 2 overshoots, above 2 undershoots, worst at π/4" | PASS | check_B_09_2.py: the table matches to 3 decimals. Sign and extremum location were checked for 30 values of p in (0.5, 2) and 30 in (2, 12]. |
| 24 | caption b-rabi-norms: \|c1\|² = cos²θ, \|c2\|² = sin²θ; p = 1 "rises to 1.414", p = 3 "dips to 0.707", p = 4 "dips to 0.5"; all meet at multiples of π/2 | PASS | check_B_09_2.py: expm integration over 0–2π; the totals equal 1 only at θ = 0, π/2, π, 3π/2, 2π |
| 25 | caption b-how-they-relate: curves for p = 1, 3, 4 "touch the motion only at its two ends" | PASS | check_B_09_2.py: cos^p + sin^p ≠ 1 everywhere strictly inside (0, π/2) for p = 1, 3, 4 |
| 26 | "p = 1 with hands that are never negative, is ordinary probability" | PASS | check_B_09_2.py: a stochastic generator moves weight gradually (0.72, 0.28) and keeps the sum exactly 1 |
| 27 | Banach–Lamperti: for p ≠ 2, only relabellings plus phases keep Σ\|c\|^p; "for p = 2 … exactly the unitary ones"; Hermitian equations generate them | PASS | check_B_10_2.py: 30/30 isometries found for each of p = 1, 3, 4 are generalized permutations (off-pattern ratio ≤ 1.1e-7). exp(−iHt) is unitary for 20 random H. The p = 2 search result is unitary and not a permutation. Numerical support, not a proof. |
| 28 | f(x) = x² + εx²(1−x²)(2x²−1): sum = 1 for two levels (each step); f(0) = 0, f(1) = 1; factor in [−1, 1/8]; non-negative for \|ε\| < 1; "1/3 − 2ε/27", total "1 − 2ε/9" | PASS | check_B_11_2.py (sympy + grid) |
| 29 | Gleason rider: certainty for the prepared level "leaves the squared shadow itself" | PASS | check_B_11_2.py: among density matrices with ⟨ψ\|ρ\|ψ⟩ = 1, only \|ψ⟩⟨ψ\| appears (random-mixture test; the standard PSD argument) |
| 30 | pilot-wave: "∂√ρ/∂t = … = −(√ρ v)' + ½√ρ v'"; "dN/dt = ½∫√ρ v' dx"; "∂σ/∂t = −(σv)' + ½σ(v' − ⟨v'⟩)" | PASS | check_B_12_2.py (sympy) |
| 31 | "\|ψ\|² … for ever"; the extra term "vanishes only when ∂v/∂x is the same everywhere … one freely spreading Gaussian"; two packets drift; caption "exact density there is about 0.48" | PASS | check_B_12_2.py: RK4 Bohmian transport to t = 4 gives these KS distances: for the \|ψ\|² cloud, 0.0012 (one packet) and 0.0008 (two). For the \|ψ\| cloud, 0.0009 (one) and 0.070 (two). The exact flow-map density of the \|ψ\| cloud at x = 0 is 0.484, against \|ψ_t\|/N = 0.093. |
| 32 | Stueckelberg: "twice as many real amplitudes plus one fixed operator that plays the role of i … the same theory" | PASS | check_B_14_2.py: the realified generator G is antisymmetric and commutes with J (J² = −1). For 20 random 3-level Hermitian H, it reproduces every amplitude, every \|c_k\|² and the transition chances \|⟨φ\|c⟩\|² |
| 33 | "complex quantum mechanics predicts up to 6√2 ≈ 8.49" (caption "3 × 2√2") | PASS | check_B_13_2.py: the standard strategy using Y scores 8.485281 for every Bell outcome |
| 34 | "real-hand theories cannot score above 7.66" | UNVERIFIABLE | check_B_13_2.py: requires the real-model SDP of Renou et al.; not reproduced (the text and caption already say it is quoted) |

PASS 32 / 34 (FAIL 1, UNVERIFIABLE 1).

## Figures
- b-terms-and-precession: figures/b-terms-and-precession.png, reused. The caption matches the script (three bold lines, grey ticks for the other lines, a cross at 1.19e15 Hz, 60° tilt, five periods).
- b-what-this-rules-out: figures/b-what-this-rules-out.png, redrawn with the y-label "value / \"chance of along\"" (it was "chance of up") to match the table. The rest is unchanged and matches the caption.
- b-stationary-vs-cos: figures/b-stationary-vs-cos.png, reused. The caption matches (top 0–6π, bottom 0–20π, thin dashed real rule inside the hand-rule envelope; row 11).
- b-model-2-sum-over-paths: figures/b-model-2-sum-over-paths.png, reused. The caption matches (row 17).
- b-rabi-norms: figures/b-rabi-norms.png, reused. The caption matches (row 24; grey band present).
- b-where-the-interpretations-stand: figures/b-where-the-interpretations-stand.png, reused. The caption matches (circles and solid for \|ψ\|², triangles and dashed for \|ψ\|; spike value in row 31).
- b-closing-note-pairs-of-systems: figures/b-closing-note-pairs-of-systems.png, reused. The caption matches (dashed line at 7.66).
- b-how-they-relate: figures/b-how-they-relate.png, reused. The caption matches (eight grey arrows; thick motion over the thin p = 2 curve; row 25).

## Notes
- Row 21 is the only failure. It is a one-word fix and doesn't change the argument: the norm is still not conserved.
- Row 29 is checked by a numerical spot test plus the standard positivity argument, not a full proof. Gleason's theorem itself and Busch's extension are not checked by computation.
- Not checked by computation: citations, historical statements (Born's footnote, Ritz 1908, Haroche et al. "no other modulation frequency"), the claim that the 2022 experiments "exceeded 7.66 by many standard deviations", and the interpretation debates.
