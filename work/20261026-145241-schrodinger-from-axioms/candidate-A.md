<!-- strategy: Boosted matter waves -->

Fire electrons at a nickel crystal and they land in the pattern of a wave with wavelength $h/p$; put neutrons through a silicon interferometer and their phase shifts by (energy difference × time)/$\hbar$; those two facts, plus four general assumptions and Galilean invariance, pin down the Schrödinger equation. Every step below is labelled *assumption*, *theorem* (follows from what precedes), or *heuristic*.

## 1. Experiments

**Davisson–Germer (1927).** Electrons accelerated through a voltage $V_0$ (54 V in the famous run) hit a nickel crystal. *Observed:* the count rate versus angle has a sharp peak (near 50°) close to where a wave of wavelength $\lambda = h/p$ would be Bragg-reflected by the crystal planes, $p$ being the momentum from $V_0$; the match becomes quantitative once refraction by the crystal's inner potential is included. Raising $V_0$ shrinks $\lambda \propto 1/\sqrt{V_0}$ and so moves the peak (Bragg: $\sin\theta \propto \lambda$). Each electron arrives as one click at one place. Idealization: monoenergetic beam, perfect crystal.

**Colella–Overhauser–Werner (1975).** A neutron beam is split in a single silicon crystal, the two paths run at different heights (vertical separation $\Delta z$, up to a few cm), then recombine. *Observed:* tilting the crystal shifts the interference fringes. The ideal formula is phase difference $= m g\Delta z\, T/\hbar$, with $m$ the neutron mass and $T$ the transit time; the 1975 data agreed with it to about 1% after correcting for the crystal's bending. Since $T = L/v = Lm/p$ at fixed wavelength, the ideal phase is $\propto m^2$: mass enters once through the potential $mgz$ and once through the transit time. No classical wave has a mass in its phase; this one does.

**Rotating-frame neutron interferometry (Werner, Staudenmann, Colella 1979).** The same interferometer, carried round by the Earth: *observed* a phase shift set by the Earth's rotation rate. This is the experimental face of "the phase of a matter wave depends on the frame". Uniformly *boosted* interferometers have not been tested directly, so below Galilean invariance is an *assumption* backed by these and by the classical limit.

<!-- FIGURE: a-cow-fringes | Two panels. Left: sketch of the COW geometry: beam split at A, upper path at height Δz above lower path, recombined at D, gravity arrow down. Right: detector counts vs crystal tilt angle φ for −30°..30°, cosinusoidal fringes with phase Δφ = m g Δz(φ) T/ħ, Δz(φ) = Δz₀ sin φ, Δz₀ = 2 cm, T = 10 µs (thermal neutrons, ~2000 m/s over ~2 cm), m = neutron mass, g = 9.8 m/s²; this gives about ±16 rad at the window edges, roughly five fringes; print the fringe count. What to notice: the fringe count is set by m; a massless classical wave would give a tilt-independent intensity. -->

*Sources:* Davisson & Germer, Phys. Rev. 30, 705 (1927); Colella, Overhauser & Werner, Phys. Rev. Lett. 34, 1472 (1975); Werner, Staudenmann & Colella, Phys. Rev. Lett. 42, 1103 (1979); Rauch & Werner, *Neutron Interferometry*, ch. 7; Sakurai & Napolitano, §2.7.

## 2. Classical candidates these rule out

- **Classical particles** (straight paths, possibly bouncing off atoms): a broad angular spread, no peak that moves with $1/\sqrt{V_0}$. Ruled out by Davisson–Germer.
- **Classical scalar wave** (like sound) with $\lambda = h/p$ put in by hand: reproduces the diffraction peak, but (i) its energy spreads over the whole detector instead of arriving as single clicks, and (ii) its phase contains no parameter $m$, so the COW shift has no place to come from. Ruled out by single clicks and by COW.

What survives: a complex amplitude $\psi(x,t)$ whose squared modulus gives click probabilities (you already have this), whose phase carries energy × time / $\hbar$. The question is what equation $\psi$ obeys.

*Sources:* Feynman Lectures III, ch. 1–2; Ballentine, *QM: A Modern Development*, §2.1.

## 3. Model: state vector plus time-evolution operator

Write the state at time $t$ as a vector $|\psi(t)\rangle$ (for one particle on a line, the function $\psi(x,t)$). Four assumptions:

**(L) Linearity** — *assumption, from experiment.* Superposed beams (COW, double slits) evolve as the sum of the separately evolved beams, so there is a linear operator with $|\psi(t_2)\rangle = U(t_2,t_1)|\psi(t_1)\rangle$.

**(U) Unitarity** — *assumption.* Total probability $\sum|c|^2 = 1$ is conserved for every state, which (as you saw before) forces $U^\dagger U = 1$.

**(C) Composition** — *assumption.* $U(t_2,t_1)U(t_1,t_0) = U(t_2,t_0)$. Add *time-translation invariance* (assumption: the apparatus does not change in time), so $U$ depends only on elapsed time, $U(s)U(t) = U(s+t)$, $U(0) = 1$.

**(K) Continuity** — *assumption.* $U(t)|\psi\rangle$ changes continuously with $t$.

*Theorem (Stone, 1932):* a strongly continuous one-parameter family of unitaries obeying $U(s)U(t)=U(s+t)$ is $U(t) = e^{-iHt/\hbar}$ for a unique self-adjoint $H$ (in infinite dimensions $H$ may be defined only on a dense set of functions; "self-adjoint" is the careful version of "Hermitian" used below). I will not prove continuity ⇒ differentiability, which is the theorem's technical content; I *assume* $U$ differentiable (**heuristic**) and show the rest.

**Step 1 (differentiate the composition law).** For small $\epsilon$,
$$\frac{U(t+\epsilon)-U(t)}{\epsilon} = \frac{U(\epsilon)U(t)-U(0)U(t)}{\epsilon} = \frac{U(\epsilon)-U(0)}{\epsilon}\,U(t).$$
Let $\epsilon \to 0$: $dU/dt = A\,U(t)$ with $A \equiv U'(0)$ a fixed operator. *Theorem given differentiability.* This is why the equation is first order in time: the rate of change of $U$ is a fixed operator times $U$ itself, so the present state alone fixes the future.

**Step 2 ($A$ anti-Hermitian ⇔ $U$ unitary).** Differentiate $U^\dagger U = 1$ at $t=0$ (product rule, $U(0)=1$): $A^\dagger + A = 0$. Define $H \equiv i\hbar A$; then $H^\dagger = -i\hbar A^\dagger = i\hbar A = H$. Converse: if $H^\dagger = H$ then $\frac{d}{dt}(U^\dagger U) = U^\dagger(A^\dagger + A)U = 0$ and $U^\dagger U = 1$ at $t=0$, so for all $t$. *Theorem*, both directions. The constant $\hbar$ is a unit conversion (*assumption*: any positive constant works here; calling it $\hbar$ is the choice to measure $H$ in joules, and that $H$'s eigenvalues are the measured energies is fixed by experiment, e.g. $E=\hbar\omega$ in §4).

**Step 3 (solve).** $dU/dt = -(i/\hbar)HU$, $U(0)=1$, $H$ constant. $U(t) = e^{-iHt/\hbar}$ (power series) satisfies it: differentiate term by term. Uniqueness: if $V(t)$ also satisfies it, $\frac{d}{dt}\big(e^{iHt/\hbar}V\big) = e^{iHt/\hbar}\big(\tfrac{i}{\hbar}H - \tfrac{i}{\hbar}H\big)V = 0$, so $e^{iHt/\hbar}V(t) = 1$ for all $t$. *Theorem.* Apply to a state and differentiate:
$$i\hbar\,\frac{d}{dt}|\psi(t)\rangle = H\,|\psi(t)\rangle.$$
The Schrödinger equation *in form*: first order, linear, Hermitian generator. Check: $H|E\rangle = E|E\rangle$ gives $|\psi(t)\rangle = e^{-iEt/\hbar}|E\rangle$, your stationary states.

**Not yet fixed:** $H$ itself. Any Hermitian operator passes steps 1–3.

*Sources:* Ballentine §3.1–3.2; Weinberg, *Lectures on QM*, §3.5 (Stone's theorem); Sakurai & Napolitano §2.1.

## 4. Galilean invariance fixes $H$

**Assumption (G):** the free-particle law is the same in a frame moving at constant velocity $v$. If $\psi(x,t)$ describes the particle in the lab, the moving observer uses $x' = x - vt$, $t' = t$ and a wavefunction $\psi'$ with (G1) the same $|\psi'|^2$ at the same physical point (a click is a click) and (G2) satisfying the *same* Schrödinger equation, with the same $H$.

*Lemma (theorem, elementary):* a linear map that preserves $|\psi|^2$ pointwise is multiplication by a phase function. Sketch: if $\psi_1,\psi_2$ vanish outside disjoint regions, the map must keep each one inside its own region (else $|\psi_1+\psi_2|^2$ would change where only one is nonzero), so the image at $x'$ depends only on $\psi$ at $x'$ and has the same modulus; linearity then makes the factor the same for all $\psi$. So
$$\psi'(x',t') = e^{i\theta(x',t';v)}\,\psi(x'+vt',t'),$$
with $\theta$ one fixed function, not depending on which $\psi$ is boosted. (Bargmann's 1954 theorem is a different, deeper result: it classifies all possible phase conventions for the whole Galilei group by one constant, the mass. It is not needed here.)

**Input from experiment:** de Broglie, $p = \hbar k$ (Davisson–Germer), and classical velocity addition $p' = p - mv$ for the momentum measured in the moving frame (*assumption*: the classical limit). So a plane wave of wavenumber $k$ must become one of wavenumber $k' = k - mv/\hbar$.

**Step 4 (boost a plane wave). This is where (G2) does its work.** Take $\psi = e^{i(kx - \omega(k)t)}$ with $\omega(k)$ the unknown frequency, i.e. $H e^{ikx} = \hbar\omega(k)e^{ikx}$. Relabelling gives $\psi(x'+vt',t') = e^{i(kx' + kvt' - \omega(k)t')}$. (G2) demands that $e^{i\theta}$ times this be a solution in the moving frame with the *same* function $\omega$: the plane wave $e^{i(k'x' - \omega(k')t')}$. Matching exponents:
$$\theta = -\frac{mv}{\hbar}x' + \big[\omega(k) - kv - \omega(k - mv/\hbar)\big]\,t'.$$

**Step 5 ($\theta$ must not depend on $k$).** The $x'$ coefficient already doesn't. Set $u = mv/\hbar$ and require $\omega(k) - (\hbar u/m)k - \omega(k-u)$ independent of $k$. Differentiate in $k$: $\omega'(k) - \omega'(k-u) = \hbar u/m$ for all $k,u$. Define $g(k) \equiv \omega'(k) - \hbar k/m$; then $g(k) - g(k-u) = \hbar u/m - \hbar u/m = 0$ for every $u$, so $g$ is a constant $c$. Integrate:
$$\omega(k) = \frac{\hbar k^2}{2m} + c\,k + \omega_0 .$$
*Theorem given the assumptions.* $\omega_0$ is the zero of energy, invisible in $|\psi|^2$. The $ck$ term is not new physics: $\frac{\hbar k^2}{2m} + ck = \frac{\hbar}{2m}\big(k + \tfrac{mc}{\hbar}\big)^2 - \frac{mc^2}{2\hbar}$, the same dispersion with the zero of wavenumber shifted, i.e. seen from a frame moving at $-c$. Setting $c=0$ is the *choice* of which frame is called "at rest" (the one where $\omega$ is smallest at $k=0$), not an extra symmetry. Substituting back, the bracket is $-mv^2/2\hbar$, so
$$\theta = -\frac{1}{\hbar}\Big(mv\,x' + \tfrac12 m v^2 t'\Big),$$
the mass-dependent boost phase. Mass entered only as the constant linking the $k$-shift to $v$.

**Step 6 (read off $H$).** $E = \hbar\omega = \hbar^2k^2/2m$. *Definition + experimental identification:* momentum is the operator whose eigenvalue on $e^{ikx}$ is the measured $p = \hbar k$; the operator $-i\hbar\,\partial_x$ does this (check by differentiating), and taking it to *be* $p$ on all superpositions is a definition, with (L) extending it. Then, on one line,
$$H_{\text{free}} = \frac{p^2}{2m} = -\frac{\hbar^2}{2m}\,\partial_x^2,\qquad i\hbar\,\partial_t\psi = -\frac{\hbar^2}{2m}\,\partial_x^2\psi .$$
In three dimensions the same steps with a vector $\mathbf k$ and boost $\mathbf v$ give $\hbar\omega = \hbar^2|\mathbf k|^2/2m$ and the Laplacian. Check: $\hbar\omega = \tfrac12 m v_{\text{g}}^2$ with $v_{\text{g}} = d\omega/dk = \hbar k/m = p/m$, the classical kinetic energy.

**Adding a potential.** *Assumption* (locality): external forces enter by adding to $H$ a term whose value at $x$ depends only on $\psi$ at $x$ — a real function $V(x)$ multiplying $\psi$. Real $V$ keeps $H$ Hermitian (step 2). This is not derived from (G) — a potential breaks boost invariance — and nothing above excludes other Hermitian additions; locality is the extra assumption, and COW confirms the form for $V = mgz$.

<!-- FIGURE: a-boost-phase | Re ψ vs x at t = 0 for the same free-particle plane wave seen in two frames: lab, k = 5 (units ħ = m = 1), and a frame moving at v = 2, so k' = 3; overlay |ψ|² = 1 as a flat line for both. x from 0 to 10. What to notice: |ψ|² is identical, the wavelength changes from 2π/5 to 2π/3; the whole difference is a phase. -->

*Sources:* Ballentine §3.3–3.4 (Galilei generators, mass as central charge); Weinberg §3.6; Sakurai & Napolitano §2.4; Bargmann, Ann. Math. 59, 1 (1954).

## 5. How it fits together, and the honest ledger

The same equation is reached by other routes — Feynman's sum over paths with $L = \tfrac12 mv^2$, Heisenberg's matrix form, or the Galilei-algebra route ($[K,P]=i\hbar m$) — *equivalent formulations*, not rivals: identical predictions. Interpretations (Copenhagen-style, many-worlds, pilot-wave, objective collapse) differ about what $\psi$ *is* and what happens at a click; nothing above depends on that, except that objective-collapse models modify (U) slightly, a live experimental question.

| Step | Status |
|---|---|
| $U$ linear | assumption (superposition experiments) |
| $U$ unitary ⇔ $H$ Hermitian | assumption ⇔ theorem (step 2, both directions) |
| composition + time-translation invariance | assumption |
| continuity ⇒ differentiable ⇒ $U = e^{-iHt/\hbar}$ unique | theorem (Stone); differentiability assumed; uniqueness shown |
| $\hbar$ | unit convention, value from experiment |
| boost = phase × relabelling | theorem (lemma) given (G1) + (L) |
| $p' = p - mv$, same $\omega$ in moving frame | assumption (classical limit, G2) |
| $\omega = \hbar k^2/2m$ | theorem; $c=0$ is a frame choice |
| $p = -i\hbar\partial_x$ | definition + de Broglie |
| $V(x)$ added | assumption (locality) |

Pros of this route: every ingredient is tied to a measured fact and the mass enters by elementary calculus. Cons: boost invariance is assumed, not directly tested by boosted interferometers; the argument is one-particle and non-relativistic — replacing Galilean by Lorentz invariance gives Klein–Gordon or Dirac instead.

**Check yourself:** In step 5, what would go wrong if you demanded $\theta$ be independent of $x'$ as well as $k$ — which experiment contradicts that?
