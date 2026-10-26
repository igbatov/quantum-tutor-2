<!-- strategy: Spinning two-state matrices -->

Send a beam of molecules through Rabi's apparatus and the spin after a pulse of length $t_1$ followed by a pulse of length $t_2$ is the spin after one pulse of length $t_1+t_2$; that composition law, with linearity, unitarity and continuity, is almost enough to write down the equation of motion. Galilean invariance then fixes what the Hamiltonian is. Below, each step is labelled **[theorem]** (follows from what came before), **[assumption]** (put in by hand, motivated by experiment) or **[heuristic]** (true, but the full proof is beyond this level).

## 1. Experiments

**Rabi resonance and Ramsey fringes (1938, 1950).** Molecules with a magnetic moment pass through a static field $B_0$ and an oscillating field. In Ramsey's version two short oscillating pulses are separated by a drift region; the detector counts molecules whose spin flipped. Observed: the flip probability oscillates with the drift time ("Ramsey fringes"), and a sequence of pulses gives the same counts as one pulse of the summed duration (in the idealization of a uniform field and no relaxation). This is the composition law and continuity in time, seen directly.

**Rauch's $4\pi$ neutron spin rotation (1975).** A neutron beam is split in a silicon interferometer; one path passes through a magnetic field that precesses the spin by an angle $\phi$. Observed: the interference contrast returns to its original value only when $\phi = 4\pi$, not $2\pi$. The state vector, not just the outcome probabilities, is what evolves, and it changes sign under a $2\pi$ rotation.

**Davisson–Germer (1927)** is used only in §4: electrons scattering from nickel give a diffraction pattern with wavelength $h/p$, which pins down one constant in the final result.

<!-- FIGURE: b-ramsey-fringes | Ramsey flip probability P = cos^2(Δ·T/2) vs drift time T for detuning Δ = 2π×1 kHz, T from 0 to 3 ms; overlay the same curve computed as one pulse of length T and as two pulses of lengths T/3 and 2T/3 composed (identical, drawn dashed on top). Caption: the two curves coincide; two evolutions in sequence equal one evolution of the summed time. -->

*Sources:* Ramsey, *Molecular Beams*, ch. V; Rauch & Werner, *Neutron Interferometry*, ch. 3; Feynman Lectures III, ch. 7 and ch. 10.

## 2. Classical candidates and the models that survive

A **classical magnetic needle** precesses continuously and can point anywhere, so a Stern–Gerlach-type analyser would give a continuous spread of deflections. Observed: exactly two spots. Ruled out by the two-valued outcomes, and it has no state that changes sign at $2\pi$. A **classical wave** has a continuous amplitude but no sign flip at $2\pi$ for a rotation, and gives no single clicks. Ruled out.

The surviving model: a state is a vector $\psi$ (two complex components for a spin-½; a function $\psi(x)$ for a particle on a line), probabilities are squared magnitudes of components, and time evolution is a map $\psi(0)\mapsto\psi(t)=U(t)\psi(0)$. Interpretations (Copenhagen-style, many-worlds, pilot-wave, objective collapse) all use the same $U(t)$ between measurements; the derivation below is neutral among them, and they differ on what happens at measurement, which is not touched here.

## 3. From the four assumptions to $i\hbar\,\dot\psi = H\psi$ (two-state case, every step)

Work with $2\times 2$ matrices so every step can be multiplied out.

**A1 Linearity [assumption].** $U(t)$ is a linear map (a matrix). Motivation: superpositions evolve to superpositions, which is what interferometers test.

**A2 Unitarity [assumption].** $U(t)^\dagger U(t) = \mathbb 1$, where $\dagger$ is conjugate-transpose. Equivalent (you have seen this) to $\sum|c_i|^2$ staying $1$ for every state.

**A3 Composition [assumption].** $U(s)\,U(t) = U(s+t)$ and $U(0)=\mathbb 1$. This also assumes time-translation invariance (the apparatus does not change in time); otherwise the law reads $U(t_2,t_1)U(t_1,t_0)=U(t_2,t_0)$ and $H$ may depend on $t$.

**A4 Continuity [assumption, strengthened to differentiability: heuristic].** $U(t)$ depends continuously on $t$. For matrices, a continuous one-parameter group is automatically differentiable (a theorem, not proved here); I use differentiability directly.

**Step 1 [theorem].** Define the matrix $A = \dfrac{dU}{dt}\Big|_{t=0}$. Then for any $t$:
$$\frac{dU}{dt}(t)=\lim_{\varepsilon\to0}\frac{U(t+\varepsilon)-U(t)}{\varepsilon}
=\lim_{\varepsilon\to0}\frac{U(\varepsilon)U(t)-U(0)U(t)}{\varepsilon}
=\left(\lim_{\varepsilon\to0}\frac{U(\varepsilon)-U(0)}{\varepsilon}\right)U(t)=A\,U(t).$$
The second equality uses A3 twice ($U(t+\varepsilon)=U(\varepsilon)U(t)$ and $U(t)=U(0)U(t)$). In words: the rate of change of $U$ is a fixed matrix $A$ times $U$ itself. This is why the equation is first order in time: the composition law makes the whole future depend on the present state only.

**Step 2 [theorem].** The solution is $U(t)=e^{At}\equiv\sum_{n\ge0}\frac{(At)^n}{n!}$. Check: differentiating the series term by term gives $A e^{At}$, and $e^{A\cdot0}=\mathbb 1$. Uniqueness: if $V(t)$ also satisfies $\dot V = AV$, $V(0)=\mathbb 1$, then $\frac{d}{dt}\big(e^{-At}V\big) = -Ae^{-At}V + e^{-At}AV = 0$ (since $A$ commutes with $e^{-At}$), so $e^{-At}V(t)=\mathbb 1$ for all $t$.

**Step 3 [theorem].** Write $A = -\,iH/\hbar$, i.e. define $H \equiv i\hbar A$. Differentiate A2 at $t=0$: $\frac{d}{dt}(U^\dagger U)\big|_0 = A^\dagger + A = 0$. With $A^\dagger = +iH^\dagger/\hbar$ this reads $iH^\dagger/\hbar - iH/\hbar = 0$, so $H^\dagger = H$. Unitarity of $U$ is equivalent to Hermiticity of $H$ (the converse: if $H^\dagger=H$ then $\frac{d}{dt}(U^\dagger U)=U^\dagger(A^\dagger+A)U=0$, so $U^\dagger U = \mathbb 1$ for all $t$).

**Step 4 [theorem].** Apply Step 1 to $\psi(t)=U(t)\psi(0)$:
$$i\hbar\,\frac{d\psi}{dt} = H\,\psi .$$
This is the Schrödinger equation in its general (abstract) form.

**Where $\hbar$ comes from [assumption].** Steps 1–4 hold with any nonzero constant in place of $\hbar$; $H$ is then just $i\times$(that constant)$\times A$. Calling the constant $\hbar$ is the choice to measure $H$ in energy units; that the eigenvalues of $H$ so defined are the measured energies is a separate identification (the stationary states $e^{-iEt/\hbar}$ you already know), fixed by experiment, e.g. the Rabi resonance condition $\hbar\omega = $ level spacing.

**Worked check: Larmor precession [theorem].** Take $H=\tfrac{\hbar\omega}{2}\sigma_z$, with $\sigma_z=\mathrm{diag}(1,-1)$. Since $\sigma_z^2=\mathbb 1$, the series splits into even and odd powers:
$$U(t)=e^{-i\omega t\sigma_z/2}=\cos\tfrac{\omega t}{2}\,\mathbb 1 - i\sin\tfrac{\omega t}{2}\,\sigma_z=\mathrm{diag}\!\big(e^{-i\omega t/2},\,e^{+i\omega t/2}\big).$$
Start with spin along $+x$: $\psi(0)=\tfrac{1}{\sqrt2}(1,1)$. Then $\psi(t)=\tfrac1{\sqrt2}\big(e^{-i\omega t/2},e^{i\omega t/2}\big)$, and the expectation values $\langle\sigma_x\rangle = 2\,\mathrm{Re}(\psi_1^*\psi_2)=\cos\omega t$, $\langle\sigma_y\rangle=2\,\mathrm{Im}(\psi_1^*\psi_2)=\sin\omega t$: the spin direction precesses about $z$ at angular frequency $\omega$ (Rabi's static-field precession). At $\omega t = 2\pi$ the direction is back but $\psi(2\pi/\omega) = -\psi(0)$: the sign flip Rauch measured; $\psi$ returns only at $4\pi$.

<!-- FIGURE: b-bloch-precession | Bloch sphere (3D or top view of the equator) with the vector (sin θ cos φ, sin θ sin φ, cos θ) at θ = 90°, precessing about z under H = (ħω/2)σ_z; draw the arc from φ=0 to φ=ωt1 (ωt1 = 70°) in one colour, then from ωt1 to ω(t1+t2) (ωt2 = 50°) in a second colour, and the single arc 0 to 120° dashed on top; mark the endpoints coinciding. Caption: two successive rotations land exactly where one rotation of the summed angle lands; composition law as rotations composing. -->

**Beyond $2\times2$: Stone's theorem [theorem, not proved].** For a particle on a line, $\psi$ is a function and $U(t)$ an infinite-dimensional operator. Stone's theorem states that the same conclusion holds: every strongly continuous one-parameter group of unitaries is $e^{-iHt/\hbar}$ with $H$ self-adjoint (though $H$ may be defined only on a dense set of functions; this is where "differentiable" needs care).

*Sources:* Ballentine, *Quantum Mechanics: A Modern Development*, §3.1–3.2; Sakurai & Napolitano, *Modern Quantum Mechanics*, §2.1; Weinberg, *Lectures on Quantum Mechanics*, §3.1 and §3.6.

## 4. Galilean invariance fixes $H = P^2/2M + V(X)$

Everything so far says $H$ is *some* Hermitian operator. The Rabi/Rauch experiments tell us the spin Hamiltonian; for a particle moving in space, the Galilei group does the job.

**G1 [assumption, motivated by the same reasoning as §3].** Space translations by $a$, boosts by velocity $v$ and time translations by $t$ each act on $\psi$ as a continuous one-parameter group of unitaries, so by Stone's theorem they are $e^{-iaP/\hbar}$, $e^{+ivK/\hbar}$, $e^{-iHt/\hbar}$ with Hermitian generators $P$ (momentum), $K$ (boost generator) and $H$. Why unitary: a translated or boosted preparation must give the same probabilities as the original, moved.

**G2 [theorem, sketched: heuristic at this level].** Classically, "translate by $a$ then boost by $v$" and "boost then translate" give the same final motion. On state vectors two operations with the same physical effect may differ by a phase (phases are unobservable), so
$e^{ivK/\hbar}e^{-iaP/\hbar} = e^{i\varphi(a,v)}\,e^{-iaP/\hbar}e^{ivK/\hbar}$.
Expanding both sides to second order in small $a,v$ gives $[K,P] \equiv KP-PK = c\,\mathbb 1$ for a constant $c$; the phase can be shown to be $\varphi = av\,\mathrm{Im}(c)/\hbar$ and cannot be removed by redefining $K$ and $P$ (Bargmann, 1954). Write $c = i\hbar M$; $M$ is a real constant with units of mass. This is the "central charge". Why it may be nonzero: in the Rabi experiment two pulses about *different* axes applied in opposite orders give different final spins, so generators of physically distinct operations need not commute; that a commutator of generators can be a multiple of $\mathbb 1$ is the new feature here. **[theorem, cited]** With $M=0$ there are no normalizable states localized in position (the representation is not a particle), so $M\neq0$ for any particle; its sign is a convention.

**G3 [assumption/definition].** Define the position operator by $X \equiv K/M$ (at $t=0$). Then $[X,P] = i\hbar\,\mathbb 1$. In the representation where $\psi$ is a function of $x$ and $X$ multiplies by $x$, $P = -i\hbar\,d/dx$ satisfies this; **[theorem, Stone–von Neumann, cited]** any other choice is unitarily equivalent.

**G4 [assumption].** Time translation of a boost: boosting then waiting $t$ equals waiting $t$ then boosting *and* translating by $vt$ (that is Galilean kinematics). Expanding this to first order in $v$ and $t$ gives $[K,H] = i\hbar P$.

**G5 [theorem].** From G3 and G4, $[X,H] = [K,H]/M = i\hbar P/M$. Compute, using $[X,P]=i\hbar$:
$$\Big[X,\tfrac{P^2}{2M}\Big]=\tfrac{1}{2M}\big([X,P]P+P[X,P]\big)=\tfrac{i\hbar P}{M}.$$
So $[X,\;H-\tfrac{P^2}{2M}] = 0$: the difference commutes with $X$.

**G6 [assumption].** The only operators commuting with $X$ are functions of $X$ (true in the $x$-representation for operators that are multiplication or differential operators; for a spinless particle this is the standard result). Hence
$$H = \frac{P^2}{2M} + V(X),\qquad i\hbar\,\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2M}\frac{\partial^2\psi}{\partial x^2}+V(x)\psi .$$
A free particle must also be translation-invariant, $[P,H]=0$, which forces $V$ constant (set to $0$). A nonconstant $V(x)$ is an *added* assumption of an external local potential, outside the Galilei group.

**Check against Davisson–Germer [theorem].** For $V=0$, $\psi=e^{i(kx-\omega t)}$ solves the equation iff $\hbar\omega=\hbar^2k^2/2M$. With $p=\hbar k$ (electron wavelength $h/p$, measured) this is $E=p^2/2M$, the non-relativistic kinetic energy, so $M$ is the inertial mass.

*Sources:* Ballentine §3.3–3.4 (the Galilei algebra, central charge, and $H=P^2/2M+V$); Weinberg §3.6; Sakurai & Napolitano §1.6–1.7 (translations, $[X,P]=i\hbar$, $P=-i\hbar\,d/dx$).

## 5. Status summary and how the pieces relate

| Step | Status |
|---|---|
| Linearity, unitarity, composition, continuity, time-translation invariance | assumption (experiment-motivated) |
| $\dot U = AU$, $U=e^{At}$, $H^\dagger=H$ | theorem (finite dimensions, shown) |
| Same in infinite dimensions | theorem (Stone, cited) |
| $\hbar$, energy units | assumption / convention |
| Galilei operations are unitary one-parameter groups | assumption |
| $[K,P]=i\hbar M$, $M\neq0$ | theorem (Bargmann, sketched) |
| $X=K/M$, $[K,H]=i\hbar P$ | definition / kinematic assumption |
| $H=P^2/2M+V(X)$ | theorem given G6 (locality assumption) |

The $2\times2$ spin case and the particle-on-a-line case are *the same* theorem (Stone) in two sizes, not merely related; what differs is only which symmetry group then fixes $H$ (rotations for spin, Galilei group for a particle). Domain: Galilean invariance means this is the non-relativistic equation; for $v$ near $c$ the group changes (Poincaré) and the result changes (Dirac, Klein–Gordon).

**Check yourself:** In Step 3, what goes wrong if you drop the $i$ and write $A = -H/\hbar$ with $H$ Hermitian; what does $U(t)$ do to the norm of $\psi$ then?
