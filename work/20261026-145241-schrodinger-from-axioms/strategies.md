# Strategies: Schrödinger equation from linearity + unitarity + continuity + composition + Galilean invariance

Learner: intermediate (algebra, complex numbers, vectors, basic calculus), every step shown, status of every claim marked (theorem / assumption / heuristic), experiment-first, one figure per section, textbook sources per section. Debate setup, K = 2.

## Candidate plans

1. **Matter-wave route (plane waves, neutron/electron interferometry).** Experiments: Davisson–Germer and G. P. Thomson electron diffraction (λ = h/p, 1927), neutron Bonse–Hart interferometer with the Colella–Overhauser–Werner gravity phase (1975) and the Sagnac/Fizeau-type shifts showing that phase depends on frame and mass. Models: classical particle (ruled out by diffraction), classical wave (ruled out by single-detector clicks and by the mass-dependent phase), then the wavefunction with the time-evolution operator. Derivation: composition + continuity ⇒ one-parameter group ⇒ U = e^{-iHt/ħ} (Stone, sketched); Galilei boost of a plane wave ⇒ the phase e^{i(mvx − mv²t/2)/ħ} (mass as central charge) ⇒ ω = ħk²/2m ⇒ H = p²/2m. Fit 5: continuous with the learner's known stationary states and probability current; the Galilei step is physical (a real boosted interferometer), not abstract.

2. **Two-state route (spin precession, Rabi/Ramsey).** Experiments: Rabi molecular-beam resonance (1938), Ramsey separated fields, neutron 4π spin rotation in an interferometer (Rauch/Werner 1975). Models: classical magnetic needle (ruled out by two-valued Stern–Gerlach outcomes), then 2×2 unitaries. Derivation: write U(t) as a 2×2 matrix, prove from composition + continuity that U(t) = e^{-iHt/ħ} with H Hermitian by explicit differentiation (Stone's theorem made concrete). Galilean part done with operators: boost generator K, [K, P] = iħM (why a non-zero central term is forced, with a 2×2 "toy" showing commutators can't all vanish), [H, K] = iħP ⇒ H = P²/2M + V. Fit 5: every step computable with matrices; strongest on "theorem vs assumption" because the 2×2 case is fully explicit.

3. **Atomic spectra route (Balmer, Franck–Hertz).** Spectra force discrete stationary states; from e^{-iEt/ħ} back out a first-order equation. Fit 2: spectra test the solutions of H, not the structure of U(t); the Galilei step is unmotivated. Rejected.

4. **Group-theory-first route (Bargmann, projective representations).** Start with the Galilei group, classify projective unitary reps, read off H = P²/2M. Fit 3: this is the real theorem but the experiments arrive late and the Lie-algebra machinery exceeds intermediate level without 2×2 scaffolding. Rejected as a stand-alone; its content is absorbed into plan 2.

5. **Path-integral route (Feynman's short-time propagator).** Double slit, then sum over paths with L = mv²/2 ⇒ Schrödinger equation. Fit 3: a genuinely different model, but Galilean invariance is smuggled in through the classical Lagrangian, and unitarity/composition are outputs rather than inputs. The learner would ask "why that Lagrangian?" Rejected for this question; good for a later "another-angle".

6. **Photonic-gate route (beam splitters, quantum circuits).** Composition law as gate sequencing; unitarity from probability conservation. Fit 2: photons are relativistic; Galilean invariance does not apply to them, so the second half fails the learner's domain-of-validity check. Rejected.

7. **Historical Hamilton–Jacobi / optical analogy.** Fit 2: heuristic, not the route the learner named. Rejected.

## Chosen strategies

### Strategy A: Boosted matter waves

**Experiments.** (i) Davisson–Germer / Thomson electron diffraction: λ = h/p, measured by varying accelerating voltage. (ii) COW neutron interferometer: phase shift proportional to mass × potential difference × transit time, confirming that phase accumulates as (energy × time)/ħ and depends on m, which no classical wave carries. (iii) Rauch–Werner neutron interferometer with a moving/rotating frame (Sagnac term) as the experimental face of Galilean boosts. Idealizations named: monochromatic beams, no decoherence.

**Models.** Classical particle (fails diffraction); classical scalar wave (fails single clicks and the mass-dependent phase); wavefunction with time-evolution operator U(t); interpretations only in one paragraph (the derivation is interpretation-neutral).

**Plan.** Linearity (assumption, from superposition experiments) gives U linear. Unitarity (assumption ⇔ Σ|c|² conserved, already known). Composition U(t₂,t₁)U(t₁,t₀) = U(t₂,t₀) plus time-translation invariance ⇒ U(t) is a one-parameter group; continuity ⇒ differentiable (heuristic at this level; Stone's theorem cited as the theorem). Differentiate: dU/dt = −(i/ħ)HU, H Hermitian from unitarity (theorem, shown in two lines). ħ as unit conversion (assumption). Then boost a plane wave: a Galilean boost of ψ(x,t) must give another solution with the same |ψ|²; write the most general allowed phase, impose composition of two boosts, and obtain the phase factor with mass as the only free constant (the central charge; name Bargmann's theorem, status: theorem, only sketched). Comparing ω(k) before and after the boost forces ω = ħk²/2m + const ⇒ H = p²/2m. V(x) enters by the assumption of a local scalar potential. Sources at end of each section: Ballentine ch. 3; Weinberg *Lectures* ch. 3; Sakurai ch. 2; Rauch & Werner *Neutron Interferometry*.

**Figure.** `a-boost-phase`: the same plane wave seen in the lab frame and in a frame moving at speed v, real part vs x at fixed t, showing the changed wavelength and the extra phase; caption says |ψ|² is unchanged while the phase is not.

**Opening sentence.** "Fire electrons at a nickel crystal and they land in the pattern of a wave with wavelength h/p; put neutrons through a silicon interferometer and their phase shifts by an amount proportional to their mass; those two facts, plus four very general assumptions, are enough to pin down the Schrödinger equation."

### Strategy B: Spinning two-state matrices

**Experiments.** (i) Rabi resonance and Ramsey fringes: a spin's state after two successive pulses equals the state after one combined pulse (composition law tested directly). (ii) Rauch 4π neutron spin rotation: the state vector, not just the outcome, evolves continuously and unitarily. (iii) Davisson–Germer only in the last section, to fix the dispersion ω(k). Idealizations: pure states, no relaxation.

**Models.** Classical magnetic needle (fails two-valued outcomes); 2×2 unitary matrices with the Bloch sphere; then the operator algebra of x, p, boosts for the Galilei part. Interpretations in one paragraph.

**Plan.** Order reversed relative to A: build the 2×2 case completely first. Write U(t) as a 2×2 matrix; from U(s)U(t) = U(s+t), U(0) = 1 and differentiability derive U(t) = e^{-iHt/ħ} by differentiating at t = 0, every step shown; prove H† = H from U†U = 1 (theorem). Compute e^{-iHt/ħ} for H = (ħω/2)σ_z and show it is Larmor precession, matching Rabi/Rauch (worked calculation, 4 lines). State Stone's theorem as the infinite-dimensional version (theorem, not proved). Then Galilei: define boost generator K and momentum P by what they do to expectation values of x and p (assumption: these generators exist, by the same Stone argument); show that [K, P] must be a constant times the identity and that composition of boosts forces the constant to be iħM, with a 2×2 commutator toy showing why "all commutators zero" is not an option; use [H, K] = iħP (time translation of a boost, assumption from Galilean composition) to derive H = P²/2M + V(X) with V from a local-potential assumption. Honest status table at the end: theorem / assumption / heuristic. Sources: Ballentine ch. 3 (§3.3–3.4), Weinberg ch. 3, Sakurai ch. 1–2, Feynman Lectures III ch. 8.

**Figure.** `b-bloch-precession`: Bloch vector precessing under e^{-iHt/ħ} with H ∝ σ_z, two successive rotations (t₁ then t₂) landing exactly on the single rotation (t₁ + t₂); caption: composition law seen as rotations composing.

**Opening sentence.** "Send a beam of molecules through Rabi's apparatus and the spin after a pulse of length t₁ followed by a pulse of length t₂ is exactly the spin after one pulse of length t₁ + t₂; that composition law, together with linearity, unitarity and continuity, is almost enough to write down the equation of motion."
