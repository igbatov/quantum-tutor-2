<!-- strategy: Boosted matter waves -->

Fire electrons at a nickel crystal and they land in the pattern of a wave with wavelength $h/p$; put neutrons through a silicon interferometer and their phase shifts by an amount proportional to (energy difference × time); those two facts, plus four very general assumptions, are enough to pin down the Schrödinger equation.

## 1. Experiments

**Davisson–Germer (1927).** Electrons accelerated through a voltage $V_0$ (about 54 V in the famous run) hit a nickel crystal. *Observed:* the count rate versus angle has a sharp peak (near 50°) exactly where a wave of wavelength $\lambda = h/p$ would be reflected by the crystal planes, with $p$ the electron's momentum from $V_0$. Changing $V_0$ moves the peak as $1/\sqrt{V_0}$. Each electron arrives as one click at one place. Idealization: monoenergetic beam, perfect crystal.

**Colella–Overhauser–Werner (1975).** A neutron beam is split in a single silicon crystal, the two paths run at different heights (vertical separation $\Delta z$, a few cm), then recombine. *Observed:* tilting the crystal shifts the interference fringes; the phase difference equals (potential energy difference $m g\Delta z$) × (transit time $T$) ÷ $\hbar$, with $m$ the neutron mass. No classical wave carries a mass; this phase does.

**Rotating-frame neutron interferometry (Werner et al., 1979).** The same interferometer, rotated with the Earth: *observed* a phase shift depending on the apparatus' rotation. This is the experimental face of "the phase of a matter wave depends on the frame". Direct tests of uniformly *boosted* interferometers are limited, so below Galilean invariance is used as an *assumption* backed by these and by the classical limit.

<!-- FIGURE: a-cow-fringes | Two panels. Left: sketch of the COW geometry: beam split at point A, upper path at height Δz above lower path, recombined at D, with gravity arrow down. Right: detector counts vs crystal tilt angle φ for −30°..30° showing cosinusoidal fringes of phase Δφ = (m g Δz(φ) T)/ħ with Δz(φ) = Δz₀ sin φ, Δz₀ = 2 cm, T = 1 ms, m = neutron mass; mark the number of fringes. What to notice: the fringe count is set by m; a massless classical wave would give a tilt-independent intensity. -->

*Sources:* Davisson & Germer, Phys. Rev. 30, 705 (1927); Colella, Overhauser & Werner, Phys. Rev. Lett. 34, 1472 (1975); Rauch & Werner, *Neutron Interferometry*, ch. 1 and ch. 7; Sakurai & Napolitano, *Modern QM*, §2.7 (gravity in QM).

## 2. Classical candidates these rule out

- **Classical particles** (straight paths, possibly bouncing): give broad angular spread with no $1/\sqrt{V_0}$-moving peak. Ruled out by Davisson–Germer.
- **Classical scalar wave** (like sound) with $\lambda = h/p$ put in by hand: reproduces the diffraction peak, but (i) a wave spreads its energy over the whole detector, never giving single clicks at single places, and (ii) its phase has no parameter $m$ in it, so the COW shift has no place to come from. Ruled out by single clicks and by COW.

What survives: a complex amplitude $\psi(x,t)$ whose squared modulus gives click probabilities (you already have this), and whose phase carries energy × time / $\hbar$. The question is what equation $\psi$ obeys.

*Sources:* Feynman Lectures III, ch. 1–2; Ballentine, *QM: A Modern Development*, §2.1.

## 3. Model: state vector plus time-evolution operator

Write the state at time $t$ as a vector $|\psi(t)\rangle$ (for one particle in one dimension, the function $\psi(x,t)$). Four assumptions, with status:

**(L) Linearity** — *assumption, from experiment.* Superposed beams (COW, double slits) evolve as the sum of the separately evolved beams. So there is a linear operator $U(t_2,t_1)$ with $|\psi(t_2)\rangle = U(t_2,t_1)|\psi(t_1)\rangle$.

**(U) Unitarity** — *assumption.* Total probability $\sum|c|^2 = 1$ is conserved for every state, which (as you saw before) forces $U^\dagger U = 1$.

**(C) Composition** — *assumption.* Evolving from $t_0$ to $t_1$ and then to $t_2$ is the same as evolving from $t_0$ to $t_2$: $U(t_2,t_1)U(t_1,t_0) = U(t_2,t_0)$. Add *time-translation invariance* (assumption: the apparatus does not change in time), so $U$ depends only on the elapsed time: $U(t_2,t_1) = U(t_2 - t_1)$. Then $U(s)U(t) = U(s+t)$, $U(0) = 1$.

**(K) Continuity** — *assumption.* $U(t)|\psi\rangle$ changes continuously with $t$ (no jumps in a closed, undisturbed system).

*Theorem (Stone, 1932):* a continuous one-parameter family of unitaries obeying $U(s)U(t)=U(s+t)$ is $U(t) = e^{-iHt/\hbar}$ for a unique self-adjoint $H$. I will not prove continuity ⇒ differentiability (that is the technical content of the theorem); I will *assume* $U$ is differentiable (**heuristic** step) and show everything else.

**Step 1 (differentiate the composition law).** For small $\epsilon$,
$$\frac{U(t+\epsilon)-U(t)}{\epsilon} = \frac{U(\epsilon)U(t)-U(0)U(t)}{\epsilon} = \frac{U(\epsilon)-U(0)}{\epsilon}\,U(t).$$
Let $\epsilon \to 0$: $\dfrac{dU}{dt} = A\,U(t)$ with $A \equiv U'(0)$, a fixed operator. *Status: theorem given differentiability.*

**Step 2 ($A$ is anti-Hermitian).** Differentiate $U(t)^\dagger U(t) = 1$ at $t=0$ using the product rule and $U(0)=1$:
$$A^\dagger + A = 0.$$
*Status: theorem.* Define $H \equiv i\hbar A$. Then $H^\dagger = -i\hbar A^\dagger = i\hbar A = H$: $H$ is Hermitian. Hermiticity of $H$ is therefore *equivalent* to unitarity of $U$, not an extra input. The constant $\hbar$ is a unit conversion (*assumption*: we choose to measure $H$ in joules; any positive constant would do here, its value is fixed later by matching $E = \hbar\omega$ to experiment).

**Step 3 (solve).** $dU/dt = -(i/\hbar)HU$, $U(0)=1$, with $H$ constant, has the unique solution $U(t) = e^{-iHt/\hbar}$ (defined by its power series). *Theorem.* Apply to a state: $|\psi(t)\rangle = U(t)|\psi(0)\rangle$, differentiate:
$$i\hbar\,\frac{d}{dt}|\psi(t)\rangle = H\,|\psi(t)\rangle.$$
This is the Schrödinger equation *in form*: first order in time (because composition + continuity give a one-parameter group, whose generator is first order), linear, with a Hermitian generator. Check: for an eigenvector $H|E\rangle = E|E\rangle$, $|\psi(t)\rangle = e^{-iEt/\hbar}|E\rangle$, your stationary states.

**What is not yet fixed:** $H$ itself. Any Hermitian operator passes steps 1–3.

<!-- FIGURE: a-composition-group | Complex plane showing, for a single eigenvector with E = 1 (units ħ = 1), the phase factor e^{-iEt} as points on the unit circle for t = 0, 0.5, 1.0, 1.5; draw arrows showing U(0.5) applied three times lands exactly on U(1.5); caption: the composition law says successive evolutions compose like rotations of the phase, which is why the generator is a single fixed H. -->

*Sources:* Ballentine, *QM: A Modern Development*, §3.1–3.2; Weinberg, *Lectures on QM*, §3.5 (Stone's theorem stated); Sakurai & Napolitano, §2.1.

## 4. Galilean invariance fixes $H$

**Assumption (G):** the laws for a free particle are the same in a frame moving at constant velocity $v$. Concretely, if $\psi(x,t)$ describes the particle in the lab, the moving observer uses coordinates $x' = x - vt$, $t' = t$ and a wavefunction $\psi'(x',t')$ with the *same* $|\psi'|^2$ at the same physical point (position probabilities are frame-independent: a click is a click) and satisfying the *same* Schrödinger equation. "Same $|\psi|^2$" allows a phase: $\psi'(x',t') = e^{i\theta(x',t')}\,\psi(x'+vt',t')$ — *assumption* that the boost acts as a position-dependent phase times relabelling (this is the simplest linear map preserving $|\psi|^2$ pointwise; that nothing else is possible is part of Bargmann's theorem, *theorem, not proved here*). Crucially $\theta$ must be a fixed function of $(x',t',v)$, the same for every wavefunction, because the boost is one linear operation (from (L)).

**Input from experiment:** de Broglie, $p = \hbar k$ (Davisson–Germer), and classical velocity addition $p' = p - mv$ for the measured momentum in the moving frame (*assumption*, the classical limit). So a plane wave with wavenumber $k$ must become one with $k' = k - mv/\hbar$.

**Step 4 (boost a plane wave).** Take $\psi = e^{i(kx - \omega(k)t)}$, where $\omega(k)$ is the still-unknown frequency, i.e. $H e^{ikx} = \hbar\omega(k)e^{ikx}$. Relabel:
$$\psi(x'+vt',t') = e^{i\left(kx' + kvt' - \omega(k)t'\right)}.$$
Demand this times $e^{i\theta}$ equals the plane wave $e^{i(k'x' - \omega(k')t')}$. Matching exponents:
$$\theta = (k'-k)\,x' + \big[\omega(k) - kv - \omega(k')\big]\,t' = -\frac{mv}{\hbar}x' + \big[\omega(k) - kv - \omega(k - mv/\hbar)\big]\,t'.$$

**Step 5 ($\theta$ must not depend on $k$).** The coefficient of $x'$ already doesn't. So define $u = mv/\hbar$ and require
$$f(v) \equiv \omega(k) - \tfrac{\hbar u}{m}k - \omega(k-u) \quad\text{independent of } k.$$
Differentiate with respect to $k$: $\omega'(k) - \omega'(k-u) = \hbar u/m$ for all $k, u$. A function whose difference over any interval $u$ is $(\hbar/m)u$ has constant slope: $\omega'(k) = \hbar k/m + c$. Integrate:
$$\omega(k) = \frac{\hbar k^2}{2m} + c\,k + \omega_0 .$$
*Theorem given the assumptions.* The constant $\omega_0$ is the zero of energy (unobservable in $|\psi|^2$). The term $ck$ would make $\omega(k) \neq \omega(-k)$, a preferred direction in empty space; *assumption* of reflection symmetry sets $c = 0$. Substituting back, $f(v) = -mv^2/2\hbar$, so the boost phase is
$$\theta = -\frac{1}{\hbar}\Big(mv\,x' + \tfrac12 m v^2 t'\Big),$$
the famous mass-dependent phase. The mass enters only as the constant linking the $k$-shift to $v$. Bargmann's theorem (*theorem, cited*) shows that composing boosts and translations forces exactly one such constant, which is why mass is said to be the "central charge" of the Galilei group; here it was put in by hand via $p' = p - mv$.

**Step 6 (read off $H$).** $E = \hbar\omega = \hbar^2k^2/2m = p^2/2m$. The operator with $p\,e^{ikx} = \hbar k\,e^{ikx}$ is $p = -i\hbar\,\partial_x$ (*theorem*: check by differentiating), so on every superposition of plane waves (by (L))
$$H_{\text{free}} = \frac{p^2}{2m} = -\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2},\qquad i\hbar\,\partial_t\psi = -\frac{\hbar^2}{2m}\partial_x^2\psi .$$
Check: $\hbar\omega = \tfrac12 m (\hbar k/m)^2 = \tfrac12 m v_{\text{group}}^2$ — the classical kinetic energy, with $v_{\text{group}} = d\omega/dk = \hbar k/m = p/m$.

**Adding a potential.** *Assumption* (local scalar potential): external forces enter by adding $V(x)$, a real function multiplying $\psi$, to $H$. Real $V$ keeps $H$ Hermitian (step 2). This is not derived from (G) — a potential breaks boost invariance — it is the simplest Hermitian, local, boost-compatible-in-the-free-limit addition, and COW confirms it for $V = mgz$.

<!-- FIGURE: a-boost-phase | Re ψ vs x at t = 0 for the same free-particle state seen in two frames: lab, k = 5 (units ħ = m = 1), and a frame moving at v = 2, so k' = 3; overlay |ψ|² = 1 as a flat line for both. x from 0 to 10. What to notice: |ψ|² is identical, the wavelength changes from 2π/5 to 2π/3; the whole difference is a phase. -->

*Sources:* Ballentine, §3.3–3.4 (Galilei generators, mass as central charge); Weinberg, *Lectures on QM*, §3.6; Sakurai & Napolitano, §2.4 (free-particle propagator); Bargmann, Ann. Math. 59, 1 (1954).

## 5. How it fits together, and the honest ledger

The same equation is reached by other routes — Feynman's sum over paths with $L = \tfrac12 mv^2$, or Heisenberg's matrix form — and these are *equivalent formulations*, not rivals: they predict identical results. Interpretations (Copenhagen-style, many-worlds, pilot-wave, objective collapse) differ about what $\psi$ *is* and what happens at a click; nothing above depends on that, except that objective-collapse models modify (U) slightly, which is a live experimental question.

| Step | Status |
|---|---|
| $U$ linear | assumption (superposition experiments) |
| $U$ unitary ⇔ $H$ Hermitian | assumption ⇔ theorem (step 2) |
| composition + time-translation invariance ⇒ one-parameter group | assumption |
| continuity ⇒ differentiable ⇒ $U = e^{-iHt/\hbar}$ | theorem (Stone); differentiability assumed here |
| $\hbar$ | unit conversion, value from experiment |
| boost = phase × relabelling, $p' = p - mv$ | assumption (classical limit); uniqueness: Bargmann |
| $\omega = \hbar k^2/2m$ | theorem from the above + reflection symmetry |
| $V(x)$ added | assumption (local potential) |

Pros of this route: every ingredient is tied to a measured fact. Cons: Galilean invariance is used as a symmetry assumption rather than tested directly by boosted interferometers, and the argument is non-relativistic — replacing Galilean by Lorentz invariance gives Klein–Gordon or Dirac instead.

**Check yourself:** In step 5, what would go wrong if you demanded $\theta$ be independent of $x'$ as well as $k$ — which experiment contradicts that?
