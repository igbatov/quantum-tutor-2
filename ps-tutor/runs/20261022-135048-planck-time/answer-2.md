# Why the expansion gives a series in powers of $G$

**You're right: I cited that step and did not show it.** It follows from two counting arguments. (i) If you expand the Einstein–Hilbert action around flat spacetime, every interaction carries a power of a constant $\kappa\propto\sqrt G$, and that power is set by how many lines meet at it. (ii) In a Feynman diagram, each extra loop adds one factor $\kappa^2\propto G$ and one factor $\hbar$. Section 4 also corrects a sentence in answer-1 about logarithms, which was inconsistent.

## 1. Expanding the action (established; shown schematically)

General relativity follows from the action $S=\frac{c^3}{16\pi G}\int d^4x\,\sqrt{-g}\,R$. Here $R$ is the curvature, built from the metric $g$, its inverse $g^{-1}$ and two derivatives. If we drop indices and numerical factors, $\sqrt{-g}\,R\sim g^{-1}\partial\partial g+g^{-1}g^{-1}\partial g\,\partial g$, times further powers of $g$ that come from $\sqrt{-g}$.

Write $g=\eta+\kappa h$. Here $\eta$ is the flat metric, $h$ is the graviton field, and $\kappa$ is a constant we choose below. The inverse is a geometric series:
$$(\eta+\kappa h)^{-1}=\eta^{-1}-\kappa\,\eta^{-1}h\,\eta^{-1}+\kappa^2\,\eta^{-1}h\,\eta^{-1}h\,\eta^{-1}-\dots$$
This series converges only when $\kappa h\ll1$, and that condition is exactly what "nearly flat" means. Curvature is present, because $h$ carries it, but it is small in the region we study. Substituting the series gives a sum of terms. Each term has two derivatives and $n$ factors of $h$:
$$S=\frac{c^3}{16\pi G}\sum_{n\ge2}\kappa^n\!\int(\partial h)^2h^{\,n-2}\quad(\text{schematic}).$$
The sum starts at $n=2$ for two reasons: flat space has $R=0$, and the term linear in $h$ is a total derivative, so it does not contribute to $S$.

Now choose $\kappa^2\propto G$ so that the $n=2$ term, which describes a free graviton, has a coefficient independent of $G$. The standard choice is $\kappa^2=32\pi G$ in units with $c=1$. With this choice the $n$-th term has coefficient $\propto\kappa^{n-2}$. The vertex where three gravitons meet carries $\kappa$, the vertex where four meet carries $\kappa^2$, and so on.

For matter, expanding the matter action to first order in $h$ gives $\frac{\kappa}{2}\int h_{\mu\nu}T^{\mu\nu}$. This term is just the definition of the stress-energy tensor $T$. The term with two gravitons is $\propto\kappa^2$. **Rule:** if matter interacts only through gravity, a vertex where $n$ lines meet in total carries $\kappa^{n-2}$.

## 2. Counting powers of $\kappa$ (established: graph counting)

Take a connected diagram with $V$ vertices, $I$ internal lines, $E$ external lines and $L$ loops. Two facts hold:
- every internal line ends at two vertices and every external line ends at one, so $\sum_v n_v=2I+E$;
- $L=I-V+1$. Example: one line joining two vertices has $I=1$, $V=2$, so $L=0$.

The total power of $\kappa$ is then
$$\sum_v(n_v-2)=2I+E-2V=2(I-V+1)+E-2=E+2L-2.$$
So when the external lines are fixed, an amplitude has the form $\kappa^{E-2}\,[a_0+a_1\kappa^2+a_2\kappa^4+\dots]$. **Each loop adds exactly one $\kappa^2\propto G$.** All tree diagrams ($L=0$) carry the same power.

## 3. Counting powers of $\hbar$ (established, with a caveat)

In quantum theory each history is weighted by $e^{iS/\hbar}$. A propagator is the inverse of the quadratic part of $S/\hbar$, so it is $\propto\hbar$. A vertex comes from $S/\hbar$, so it is $\propto1/\hbar$. A diagram is therefore $\propto\hbar^{I-V}=\hbar^{L-1}$. **Each loop adds one $\hbar$.**

Put the two counts together. Each loop multiplies the amplitude by something $\propto\kappa^2\hbar\propto G\hbar$. The combination $G\hbar/c^3=\ell_P^2$ is an area, so the dimensionless factor needs $k^2$, where $k$ is the process's only wavenumber. That factor is $(\ell_Pk)^2$. Set $k=E/\hbar c$:
$$\ell_P^2k^2=\frac{\hbar G}{c^3}\cdot\frac{E^2}{\hbar^2c^2}=\frac{GE^2}{\hbar c^5}.$$
This is the derivation that the claim in answer-0 §2(b) needed. Note that $\hbar$ sits in the denominator only because we hold $E$ fixed. At fixed $k$, the factor $\ell_P^2k^2\to0$ as $\hbar\to0$, as a quantum correction should.

**Caveat:** the $\hbar$ count holds when masses are written as inverse lengths $mc/\hbar$. Converting back can cancel the $\hbar$. That is why the *classical* term $3G(m_1+m_2)/rc^2$ in answer-1's potential comes from one-loop diagrams (Holstein & Donoghue 2004; not verified by me in detail). "One loop" and "quantum" are related but not identical. Every quantum correction needs loops, but some loop terms are classical.

**Worked example (two masses):**
- *Tree level:* one graviton exchanged between two matter lines. $V=2$, each vertex with $n_v=3$; $E=4$; $I=1$; so $L=0$. The diagram carries $\kappa^2\propto G$, and it gives Newton's $Gm_1m_2/r$ (established).
- *One loop:* two gravitons exchanged. $V=4$, each with $n_v=3$, so $\sum_v n_v=12=2I+4$, which gives $I=4$ and $L=1$. The diagram carries $\kappa^4$.
- *Ratio:* $\kappa^2\hbar$. With $r$ as the only length, this becomes $(\ell_P/r)^2$, which is the form of the $\frac{41}{10\pi}$ term.

## 4. Corrections to answer-1

- **"Logarithms of ratios of energies can also appear" was inconsistent with "only one energy $E$".** A ratio needs two energies. The correct statement is as follows. Loop diagrams in gravity diverge. Absorbing the divergences requires new terms in the action, of the form (curvature)$^2$, whose coefficients general relativity does not fix ('t Hooft & Veltman 1974; established). Defining those coefficients introduces a second scale $\mu$. So corrections contain terms like $(E/E_P)^2\ln(E/\mu)$. The dimensional argument in answer-1 §1 holds only up to such terms.
- At each higher order, more unknown coefficients enter. So the series is predictive only for $E\ll E_P$. Its reaching order 1 near $E_P$ is a **limit of the scheme**, not a prediction about time.

---

**Check yourself:** Mass 1 has a single vertex where two gravitons attach ($n_v=4$). Mass 2 has two vertices with $n_v=3$, joined by a matter propagator. Find $V$, $I$ and $L$, and check that the power of $\kappa$ equals $E+2L-2$.

**Sources:** Zee, *Quantum Field Theory in a Nutshell* (2nd ed.), ch. VIII.1 (gravity as a field theory; ħ and loop counting in part I, section not verified by me); Feynman, Morinigo & Wagner, *Feynman Lectures on Gravitation* (expansion around flat spacetime); Donoghue, *Phys. Rev. D* 50, 3874 (1994); Holstein & Donoghue, *Phys. Rev. Lett.* 93, 201602 (2004); 't Hooft & Veltman, *Ann. Inst. H. Poincaré A* 20, 69 (1974).
