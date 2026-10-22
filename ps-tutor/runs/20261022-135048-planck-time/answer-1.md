# Why the dimensionless number is $GE^2/\hbar c^5$

**You're right: I asserted that step without deriving it, and my label "established within this framework" covered more than it should have.** Two parts of 2(b) really are established: (i) $GE^2/\hbar c^5$ is the only dimensionless number you can build from $G$, $\hbar$, $c$ and one energy $E$, and (ii) in the effective field theory of gravity, quantum corrections appear as powers of it. Two parts are heuristic: the translation into "corrections of order $(t_P/\Delta t)^2$", and the claim that it holds for every process. It holds only for processes whose only scale is $E$. The steps follow.

## 1. Only one dimensionless number exists (established: dimensional analysis)

We look for powers $\alpha$, $\beta$, $\gamma$ that make $G\,E^\alpha\hbar^\beta c^\gamma$ dimensionless. The units are $[G]=\mathrm{m^3\,kg^{-1}\,s^{-2}}$, $[E]=\mathrm{kg\,m^2\,s^{-2}}$, $[\hbar]=\mathrm{kg\,m^2\,s^{-1}}$ and $[c]=\mathrm{m\,s^{-1}}$. Each unit's total power must be zero:
- kg: $-1+\alpha+\beta=0$, so $\beta = 1-\alpha$
- m: $3+2\alpha+2\beta+\gamma=0$. Substituting $\beta$ gives $3+2\alpha+2-2\alpha+\gamma=0$, so $\gamma=-5$
- s: $-2-2\alpha-\beta-\gamma=0$. Substituting gives $-2-2\alpha-1+\alpha+5=0$, so $2-\alpha=0$ and $\alpha=2$. Then $\beta=-1$.

So $G E^2/(\hbar c^5)$ is the result. Is there a second dimensionless number that does not involve $G$? Try $E^\alpha\hbar^\beta c^\gamma$. The kg equation gives $\alpha+\beta=0$. The m equation then gives $\gamma=0$. The s equation gives $-2\alpha-\beta=-\alpha=0$. So the only solution is $\alpha=\beta=\gamma=0$, which means no such number exists. **Conclusion:** if a process involves only $G$, $\hbar$, $c$ and one energy $E$, every dimensionless result it has is a function of $GE^2/\hbar c^5=(E/E_P)^2$. (Logarithms of ratios of energies can also appear, but they vary slowly with $E$.)

**Where this stops holding:** if the particles have rest masses $m$, then $Gm^2/\hbar c$ and $GM/rc^2$ are additional dimensionless numbers. The second one, $GM/rc^2$, contains no $\hbar$, so it measures classical relativistic corrections, not quantum ones. My earlier sentence should have said "for a process whose only energy scale is $E$".

## 2. Why the corrections are powers of it (established within the theory)

Dimensional analysis tells you which variable to use. It does not tell you that corrections grow with that variable. That step comes from physics. In the effective field theory, the metric is expanded around flat spacetime, and the result is a series in powers of $G$ (Donoghue 1994). With only $E$ available, step 1 shows that each power of $G$ has to arrive as $G E^2/\hbar c^5$. So, apart from numerical coefficients and logarithms:
$$\text{result} = (\text{leading term})\times\Big[1 + c_1\Big(\tfrac{E}{E_P}\Big)^2 + c_2\Big(\tfrac{E}{E_P}\Big)^4+\dots\Big].$$
Within this framework, quantum mechanics and special relativity are combined consistently (quantum fields on nearly flat spacetime). That is why I called (b) more solid than (a), which glued together $E=hc/\lambda$ and the Schwarzschild horizon. The framework's own domain of validity is $E\ll E_P$.

**Heuristic picture of why $r$ drops out:** take two quanta of energy $E$ a distance $r$ apart. The magnitude of their Newtonian gravitational energy is $G(E/c^2)^2/r = GE^2/(c^4 r)$. The energy needed to localize a quantum within $r$ is about $\hbar c/r$. Their ratio is
$$\frac{GE^2/(c^4 r)}{\hbar c/r}=\frac{GE^2}{\hbar c^5}.$$
This mixes Newtonian gravity with a quantum estimate, so it only illustrates the number. It does not derive it.

## 3. Worked example: quantum correction to Newton's law

**Not verified by me in detail:** Bjerrum-Bohr, Donoghue and Holstein (2003) computed, for one common definition of the potential between two masses,
$$V(r) = -\frac{Gm_1m_2}{r}\Big[1 + 3\frac{G(m_1+m_2)}{rc^2} + \frac{41}{10\pi}\frac{G\hbar}{r^2c^3}\Big].$$
The second term is classical, because it contains no $\hbar$. The third term is quantum. Using $\ell_P^2=\hbar G/c^3$, the third term is $\frac{41}{10\pi}(\ell_P/r)^2 \approx 1.31\,(\ell_P/r)^2$.

To link this to energy, probe distance $r$ with quanta of energy $E\sim\hbar c/r$ (order of magnitude):
$$\Big(\frac{\ell_P}{r}\Big)^2 = \frac{\hbar G}{c^3}\cdot\frac{E^2}{\hbar^2c^2}=\frac{GE^2}{\hbar c^5}.$$
Numbers: at $r=1$ m, $1.31\times(1.62\times10^{-35})^2\approx3.4\times10^{-70}$. At collider scale, $r\sim10^{-18}$ m, it is $\approx3.4\times10^{-34}$. Both are far below anything measurable.

## 4. What remains heuristic

Define $\Delta t\equiv\hbar/E$. Then, exactly, $(E/E_P)^2 = (\hbar/\Delta t)^2/(\hbar/t_P)^2=(t_P/\Delta t)^2$. The heuristic step is calling $\hbar/E$ "the time scale of the process", which is true only as an order of magnitude. The series in section 2 reaching order 1 at $E\sim E_P$ is a **limit of this expansion**. It is not a prediction that time is discrete, and it is not a contradiction.

---

**Check yourself:** Set $E=m_pc^2$ (proton rest energy) in $GE^2/\hbar c^5$. Show that it becomes $Gm_p^2/\hbar c$, and evaluate it. How does it compare with the fine-structure constant $\approx1/137$?

**Sources:** Zee, *Quantum Field Theory in a Nutshell* (2nd ed.), ch. III.2 (nonrenormalizable couplings and dimensional analysis) and ch. VIII.1 (gravity as a field theory); Burgess, "Quantum Gravity in Everyday Life", *Living Rev. Relativ.* 7, 5 (2004); Donoghue, *Phys. Rev. D* 50, 3874 (1994); Bjerrum-Bohr, Donoghue, Holstein, *Phys. Rev. D* 67, 084033 (2003).
