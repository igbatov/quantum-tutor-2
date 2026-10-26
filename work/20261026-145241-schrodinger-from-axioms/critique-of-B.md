# Critique of candidate-B (Spinning two-state matrices)

## Where it will fail this learner

1. **The experiments don't bear on the question asked.** The learner asked how the *Schrödinger equation* follows from five assumptions. B spends §1–3 on spin (Rabi, Ramsey, Rauch 4π) and reaches only the abstract $i\hbar\dot\psi=H\psi$; the particle-specific part (§4), which is where the hard content lives, has no experiment attached except a one-line Davisson–Germer check. No experiment in B touches boosts or the mass-dependent phase, so Galilean invariance is motivated by nothing observed. The learner will ask "what experiment forces G1–G4?"

2. **"Composition law, seen directly" (§1, line 7) is overstated.** "A sequence of pulses gives the same counts as one pulse of the summed duration" is true of *any* deterministic evolution in a constant Hamiltonian, so it tests nothing; and in Rabi's apparatus it only holds in the rotating frame with the oscillating field phase-continuous across pulses, an idealization B doesn't name. Ramsey's method is specifically two *separated* pulses, and the fringes come from the drift, not from composition.

3. **The figure b-ramsey-fringes is mislabelled.** $P=\cos^2(\Delta T/2)$ is the ideal Ramsey formula for two instantaneous $\pi/2$ pulses with drift time $T$; the caption calls $T$ a "pulse length" and the "two curves" are the same formula plotted twice. It will not show the learner anything.

4. **Rauch 4π (line 9):** "the interference contrast returns only at $4\pi$" — what returns is the *intensity* ($\propto\cos(\phi/2)$); contrast is the fringe amplitude. Minor, but this learner checks words.

## Skipped steps and status problems in §4

5. **G2 is the step the learner asked for and it is sketched, not shown.** "Expanding to second order gives $[K,P]=c\,\mathbb 1$" — the expansion is not performed, and why $c$ must be a multiple of the identity rather than an arbitrary operator is not argued (it comes from the phase $\varphi$ being a number). Then "$\varphi = av\,\mathrm{Im}(c)/\hbar$" with $c=i\hbar M$ gives $\varphi = avM$, which has units of action, not a dimensionless phase; the correct form is $\varphi = Mav/\hbar$. A verifier will flag this.

6. **G4 likewise:** "expanding to first order in $v$ and $t$ gives $[K,H]=i\hbar P$" — no expansion shown. For this learner "every derivation step shown" was a stated requirement.

7. **G1 says boosts are unitary "because probabilities are preserved".** Wigner's theorem allows antiunitary too; continuity in $v$ excludes it. Omitted; the learner will ask.

8. **G3 "$X\equiv K/M$" is labelled "assumption/definition" but is then used as position.** Nothing in B connects this operator to where clicks land. The identification needs $dX/dt = P/M$ (Ehrenfest/Heisenberg equation), which would also justify the final sentence "so $M$ is the inertial mass" — as written that sentence is circular (it reads off $M$ from an equation that was *built* with $M$).

9. **G6 status is muddled.** "The only operators commuting with $X$ are functions of $X$" is labelled assumption, then called "the standard result". It is a theorem for a spinless particle (X generates a maximal abelian algebra); the real assumption is *no internal degrees of freedom*. And the $V(X)$ it yields is forced constant two lines later, so the external potential is still assumed — B says so, correctly, but the heading "Galilean invariance fixes $H=P^2/2M+V(X)$" promises more than is delivered.

10. **"The same theorem in two sizes, not merely related" (§5).** Fair, but the domain issue B itself raised (H defined on a dense set) is exactly what makes the infinite-dimensional case *not* the finite one; the learner distinguishes "same" from "related" and will push here.

## What B does better than candidate-A

- **Step 2's uniqueness proof** of $U=e^{At}$ (via $\frac{d}{dt}(e^{-At}V)=0$) is complete and short; A merely asserts uniqueness.
- **Step 3 proves both directions** (unitary $\Leftrightarrow$ Hermitian); A proves only one and asserts the equivalence.
- **The explicit note that without time-translation invariance $H$ may depend on $t$** is something A buries.
- **The Larmor $2\times2$ worked example** gives the learner a case they can multiply out by hand, and ties $\psi(2\pi/\omega)=-\psi(0)$ to a measured fact (Rauch). A has no finite-dimensional check.
- **The commutator route (G5)** is Ballentine's actual argument and generalizes more cleanly than A's plane-wave matching, which needs the extra reflection-symmetry assumption to kill the $ck$ term and puts $p'=p-mv$ in by hand. B also names $M\ne0$ and Stone–von Neumann, which A omits.
- **B's check-yourself** (drop the $i$) is more diagnostic than A's.

## Net

B is stronger on §3 (the Stone part) and weaker on §4 (the Galilei part), which is the opposite of where this learner's question is hard. A revision of B should perform the G2 and G4 expansions explicitly, fix the $\varphi$ units, add one boost-sensitive experiment (COW's $mg\Delta z\,T/\hbar$ phase is the natural one), and relabel G6.
