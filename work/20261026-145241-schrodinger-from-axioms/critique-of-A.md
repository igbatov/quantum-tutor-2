# Critique of candidate A ("Boosted matter waves") by the author of B

## Where it will fail this learner

1. **Step 2 claims "Hermiticity of H is equivalent to unitarity" but shows one direction only** (unitary ⇒ A anti-Hermitian). The converse (H Hermitian ⇒ U unitary for all t) is never shown. This learner distinguishes "related" from "the same" and will quote "equivalent" and ask why. One line fixes it: d/dt(U†U) = U†(A†+A)U = 0.

2. **Step 3 asserts uniqueness of U = e^{-iHt/ħ} as a "theorem" with no argument.** The learner wants every step; uniqueness is a two-line computation (d/dt[e^{-At}V] = 0) and should be given.

3. **Step 6 labels p = −iħ∂ₓ a "theorem".** What is shown is only that this operator has e^{ikx} as eigenfunction with eigenvalue ħk. That the physical momentum *is* this operator rests on the identification p = ħk (de Broglie, experimental input) plus the choice to define p by its action on plane waves. Status should be "definition + experimental identification", not theorem. A reader will ask "why that operator and not another with the same plane-wave eigenvalues?".

4. **Wrong attribution in §4.** "That nothing else is possible [than phase × relabelling] is part of Bargmann's theorem" is not right. Bargmann's theorem classifies projective representations of the Galilei group by one constant (mass). The statement actually needed, that a *linear* map preserving |ψ(x)|² pointwise for every ψ is multiplication by a phase function, is elementary and could be proved in three lines (apply to ψ with disjoint supports). Citing Bargmann for it misplaces what is theorem and what is assumption.

5. **Step 5, the "constant slope" sentence skips the argument.** From ω′(k) − ω′(k−u) = ħu/m for all k,u, define g(k) = ω′(k) − ħk/m; then g(k) = g(k−u) for all u, so g is constant. A says "a function whose difference over any interval u is (ħ/m)u has constant slope" without this step; the learner will quote it.

6. **The ck term and "reflection symmetry" is an unnecessary extra assumption.** ħk²/2m + ck = (ħ/2m)(k + mc/ħ)² − mc²/2ħ, so c ≠ 0 is just the same dispersion seen from a boosted frame (shift of the zero of momentum). Galilean invariance already allows one to set c = 0 by choice of rest frame; presenting it as a new symmetry assumption inflates the assumption list.

7. **"The same Schrödinger equation" in the moving frame is the whole content of (G), but it is introduced in passing.** The demand in Step 4 that a boosted momentum eigenstate is again a momentum eigenstate with the *same* function ω(k′) is where invariance does its work; A never says "this is the step where (G) is used", though the request asked for exactly that.

## Misleading or overstated experimental statements

- Davisson–Germer: "exactly where a wave of wavelength h/p would be reflected" is overstated; the original data required a crystal inner-potential (refraction) correction to match Bragg's law. "The peak moves as 1/√V₀" conflates wavelength (∝ 1/√V₀) with peak angle (sin θ ∝ λ). Exact quantifiers matter to this learner.
- COW: "the phase difference equals mgΔzT/ħ" — the 1975 result agreed with theory only to about 1% after a bending correction, and T is path-length/velocity, so the formula is the idealized one; say "ideal". Also COW gives Δφ ∝ m²: the mass enters once through V = mgz and once through T ∝ m/p at fixed λ; A's phrase "mass in the phase" is correct but the learner may ask which m.
- Figure a-cow-fringes: T = 1 ms is unphysical for a few-cm interferometer (thermal neutrons ~2000 m/s give T ~ 10 µs). With the stated parameters the phase is ~3000 rad, hundreds of fringes across the window, not the ~tens of radians COW measured. The learner checks domains and will notice.
- "first order in time (because … whose generator is first order)" is circular as written; B's reason (composition ⇒ dU/dt = A U, so the present state fixes the future) is the actual argument.

## Omissions

- No 3D statement and no mention that the free-particle argument is for one dimension; the request asked for domains of validity when results are combined.
- The potential V(x) is labelled an assumption but there is no reason given why V must be a *multiplication* operator rather than any Hermitian addition; B's G6 at least names that locality assumption explicitly.
- Stone's theorem is stated but the infinite-dimensional subtlety (H defined only on a dense domain) is not mentioned; "unique self-adjoint H" is right, "Hermitian" is used interchangeably later.

## What A does better than B (conceded)

- **The mass enters visibly and elementarily.** A's Step 4–5 plane-wave calculation is complete and checkable with calculus alone; B's G2 leans on "expanding to second order … can be shown (Bargmann)", which this learner will quote. A's route is more honest about *what* fixes H: a measured input (p = ħk, p′ = p − mv) rather than a cited theorem.
- **Experiments really carry the argument.** COW's mass-dependent phase is exactly the observable that the Galilean phase θ predicts; B's spin experiments motivate composition well but say nothing about the Galilei part, so B's §4 is less experiment-first.
- **The group-velocity check** (ħω = ½m v_group²) is a good limiting-case test B lacks.
- A's "cons" paragraph (boosts not directly tested by interferometers; Lorentz replaces Galilei) is a clear domain statement.
- A's boost-phase figure makes "same |ψ|², different phase" concrete; B's figures illustrate composition only.

If I were revising A, I would keep its route and add the four missing lines (converse of Step 2, uniqueness, g(k) constant, the pointwise-phase lemma), relabel Step 6 and the ck remark, mark where (G) is used, and fix the figure's T.
