VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | Step 1 "dU/dt = A U(t)" from composition | PASS | checks/check_b_01.py: random Hermitian 2×2 H; finite-difference dU/dt equals A·U(t); U(s)U(t)=U(s+t) to 1e-9 |
| 2 | Step 2 "U(t)=e^{At}", uniqueness | PASS | check_b_01: ODE V'=AV, V(0)=1 integrated, equals expm(At) to 1e-7; sympy dU/dt−AU = 0 for general Hermitian 2×2 |
| 3 | Step 3 "A†+A=0 … H†=H", converse, "Unitarity ⇔ Hermiticity" | PASS | check_b_01: i·ħ·A = H, A†+A = 0; e^{−iHt/ħ} unitary at random points (sympy); non-Hermitian H gives non-unitary U |
| 4 | Larmor "U = cos(ωt/2)1 − i sin(ωt/2)σz = diag(e^{∓iωt/2})" | PASS | check_b_01 (sympy) |
| 5 | "⟨σx⟩=cos ωt, ⟨σy⟩=sin ωt", "⟨σx⟩ = 2Re(ψ1*ψ2)" | PASS | check_b_02: 13 times in [0,4π], error < 1e-12 |
| 6 | "At ωt=2π … ψ=−ψ(0); ψ returns at 4π" | PASS | check_b_02 |
| 7 | Rauch "intensity oscillates in φ with period 4π" | PASS | check_b_02: I = (1+cos(φ/2))/2 for an arbitrary spin state; I(2π)=0, I(4π)=1 |
| 8 | Rabi "ideally sin²(Ωt/2)", "smooth … no jumps" | PASS | check_b_02: exact in the rotating-wave model; full lab model (ω0=2π·1 MHz, linear drive) differs by at most 1.6e-5 over 0–200 µs, smooth |
| 9 | Two pulses 30+50 µs land on the single-pulse curve at 80 µs (figure spec; "phase-continuous") | PASS | check_b_02: same *state*, not only same P; P(30 µs)=0.6545, P(80 µs)=0.3455 |
| 10 | G2 "BC−CB = iλav 1" (second-order expansion) | PASS | check_b_03: sympy noncommutative expansion with an order-counting parameter |
| 11 | "[K,P]=iħM", "φ=Mav/ħ" | PASS | check_b_03 (K=MX, P=−iħd/dx on test function); check_b_04: phase of ⟨W′\|W⟩ = Mav/ħ exactly (FFT grid) |
| 12 | Units: "φ dimensionless", "M has units of mass" | PASS | check_b_03 (sympy.physics.units): [K][P]/ħ = kg; Mav/ħ dimensionless |
| 13 | G4 identity and "[H,K] = −iħP + iħ²μ", shift to "[K,H]=iħP" | PASS | check_b_03 (vt coefficient, sympy); check_b_04: both sides agree up to a global phase, \|overlap\| = 1 − 1e-12 (χ = +Mv²t/2ħ in this convention) |
| 14 | G5 "[X,P²/2M] = iħP/M", "[X, H−P²/2M]=0" | PASS | check_b_03 |
| 15 | G3 "d⟨X⟩/dt = (i/ħ)⟨[H,X]⟩ = ⟨P⟩/M" | PASS | check_b_03: operator identity (sympy) and Gaussian packet by FFT: slope 2.000000 = ⟨P⟩/M |
| 16 | G6 "[P,H]=0 forces V constant" | PASS | check_b_03: [P,V(X)] = −iħV′ |
| 17 | Davisson–Germer: "ħω=ħ²k²/2M … gives M=m_e" | PASS | check_b_03: λ(54 eV) = 1.669 Å; M recovered = m_e to 1e-12 |
| 18 | COW "phase = MgΔz T/ħ" | PASS | check_b_03: identical to the standard m²gλA/(2πħ²) with A=ΔzL, T=L/v. The text gives no numbers; illustrative: λ=1.445 Å, A=10 cm² gives 56.9 rad |
| 19 | Boost phase e^{i(Mvx − Mv²t/2)/ħ} (§4 figure) | PASS | check_b_03: boosted Gaussian solves the free equation exactly; dropping −Mv²t/2 breaks it. fig_b-boost-wave.py: FFT evolution vs formula, max error 4e-16 |
| 20 | A4 "continuous one-parameter group of matrices is automatically differentiable"; Stone; Bargmann; Stone–von Neumann; "M=0 ⇒ no localizable states" | UNVERIFIABLE (cited theorems) | Standard results, correctly stated; no computation possible |

## Figures
- **b-rabi-continuity.png** (§1 Experiments; requested): figures/b-rabi-continuity.png.
  Caption: "Spin-flip probability P(t)=sin²(Ωt/2) for a resonant pulse of length t (Ω=2π×10 kHz). The curve is continuous in t, with no jumps. The dashed segment is a 30 µs pulse followed by a 50 µs pulse with the same drive phase. It ends (square) exactly on the single-pulse curve at 80 µs: the composition law."
- **b-classical-vs-quantum.png** (§2 Classical candidates; extra): figures/b-classical-vs-quantum.png.
  Caption: "(a) Stern–Gerlach screen: randomly oriented classical needles give a flat spread of deflections, but two separate spots are observed. (b) Interferometer with one path's spin rotated by φ: a classical vector repeats every 2π, but the spin-½ state (observed, Rauch 1975) repeats only every 4π. At φ=2π the intensity is zero because ψ → −ψ."
- **b-bloch-precession.png** (§3 Four assumptions, after the Larmor check; requested): figures/b-bloch-precession.png.
  Caption: "Top view of the Bloch-sphere equator under H=(ħω/2)σz. A rotation of 70° followed by one of 50° (solid arcs) ends where one rotation of 120° (dashed, drawn just outside the circle) ends. Two successive rotations land where one rotation of the summed angle lands: the composition law as rotations composing."
- **b-boost-wave.png** (§4 Galilean invariance; extra): figures/b-boost-wave.png.
  Caption: "A free Gaussian packet (units ħ=M=σ=1). Top, t=0: lab-frame packet (real, so it lies under its envelope) and the same packet boosted by v=3, which is multiplied by e^{iMvx/ħ}. Bottom, t=2: the lab packet has spread around x=0, while the boosted packet is centred at x=vt. The circles are the formula e^{i(Mvx−Mv²t/2)/ħ}ψ(x−vt,t), which match the Schrödinger evolution exactly. The mass M sits in the phase."
- **b-status-map.png** (§5 Status summary; extra): figures/b-status-map.png.
  Caption: "Which inputs are assumed and which are proved. Square thin boxes are assumptions, thick rounded boxes are theorems shown in the text, dashed boxes are theorems cited, and the zigzag box is a convention. The arrows show which inputs each step uses."

## Notes
- §1 Rabi (historical, not computable): Rabi's 1938 molecular-beam experiment swept the static field B0 through resonance at a fixed transit time. It did not vary the pulse length t. Flip probability oscillating in pulse length was observed later (transient nutation, Torrey 1949; Ramsey, *Molecular Beams*, ch. V discusses both). I suggest rewording to "Rabi's resonance formula predicts, and later pulsed experiments show, a flip fraction that is a smooth function of t." Otherwise the learner may quote "Observed" and ask for the data.
- G2 is tagged [theorem], but its first sentence, that classically commuting operations commute on rays, is an assumption (part of G1/Galilean kinematics). Only the step from there to [K,P]=iħM is a theorem.
- "Same drive phase" in the figure spec means phase-continuous in the rotating frame. In check_b_02 a drive restarted at t1 happened to agree only because 30 µs is a whole number of 1 MHz cycles. In general, a phase jump changes the rotation axis and breaks the composition shown.
- COW: the "observed" shift agreed with MgΔzT/ħ to about 1% (later experiments found small percent-level discrepancies). "Equal to" is right at leading order.
- Stone–von Neumann ("any other choice is unitarily equivalent") needs irreducibility and the exponentiated (Weyl) form of [X,P]=iħ. G6's "spinless" assumption supplies irreducibility. Consider stating it.
