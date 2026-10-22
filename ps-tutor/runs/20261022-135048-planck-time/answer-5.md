# Why a phase of size $(E/E_P)^2$ can describe classical physics

**You're right: answer-4 contradicted itself.** Its test "classical = finite limit as $\hbar\to0$" applies to *observables* (angles, cross sections), not to phases. Its sentence "At fixed $E$, $GE^2/\hbar c^5$ grows without bound. This signals that the expansion fails. It is not a classical term appearing" was wrong in its second half. The phase $\delta$ is not classical. What is classical is $\hbar\delta$, which is an action, and the deflection angle obtained from its derivative. Both have finite limits as $\hbar\to0$ at fixed $E$ and $b$. "A quantity of size $(E/E_P)^2$ can be classical" should have said exactly that.

## 1. Phases are expected to diverge as $\hbar\to0$ (established)

A free particle with momentum $p$ has $\psi\propto e^{ipx/\hbar}$. At fixed $p$ and $x$, the phase $px/\hbar$ grows without bound as $\hbar\to0$. The observable is $p=\hbar\,\partial(\text{phase})/\partial x$, and it contains no $\hbar$. In general, in the semiclassical (WKB) regime an amplitude goes as $e^{iS_{\rm cl}/\hbar}$, where $S_{\rm cl}$ is the classical action. So answer-4's test has to be applied to $S_{\rm cl}=\hbar\times$phase, or to observables.

## 2. The angle from the phase (stationary phase: established; coefficient $C$: not verified by me)

**Domain:** two massless quanta, each with energy $E$ in the centre-of-mass frame (relativistic, quantum); small angle $\theta\ll1$; impact parameter $b\gg r_g\equiv GE/c^4$. Let $x\equiv(E/E_P)^2=GE^2/\hbar c^5$. In the eikonal approximation,
$$A(\mathbf q)\propto\int d^2b\;e^{-i\mathbf q\cdot\mathbf b}\big[e^{2i\delta(b)}-1\big],\qquad \delta(b)=-C\,x\ln(b/b_0).$$
Here $C$ is a number of order 1 ($C=4$ in the convention of Amati, Ciafaloni and Veneziano), and $b_0$ is an infrared cutoff.

1. Where the total phase $2\delta(b)-\mathbf q\cdot\mathbf b$ changes by many radians across the $b$-plane, neighbouring contributions cancel. What survives comes from points where its gradient is zero: $\mathbf q=2\nabla\delta$.
2. $\delta$ depends only on $b=|\mathbf b|$, so $|\nabla\delta|=|d\delta/db|=Cx/b$. The cutoff $b_0$ drops out.
3. Hence $q=2Cx/b$.
4. The momentum transfer is $\hbar q=2\hbar k\sin(\theta/2)\approx\hbar k\theta$, so $\theta\approx q/k$, with $k=E/\hbar c$.
5. $\theta\approx 2Cx/(kb)$. Now $x/k=\dfrac{GE^2}{\hbar c^5}\cdot\dfrac{\hbar c}{E}=\dfrac{GE}{c^4}=r_g$. So $\theta\approx2C\,r_g/b$.

$\hbar$ cancels. At fixed $E$ and $b$, $\theta$ is a classical observable. With $C=4$ this gives $\theta=8GE/(c^4b)$, which is the classical-GR deflection for this collision (not verified by me in detail). Also, $\hbar\delta=-C\,(GE^2/c^5)\ln(b/b_0)$ has units of $\mathrm{J\,s}$ and contains no $\hbar$: it is a classical action.

**Condition for step 1:** the phase has to vary quickly: $b^2\,|d^2(2\delta)/db^2|=2Cx\gg1$, that is, $E$ well above $E_P$. For $E\ll E_P$ we have $|\delta|\ll1$, so $e^{2i\delta}-1\approx2i\delta$ (single-graviton exchange), and no classical trajectory dominates.

**Worked example:** $E=100\,E_P$, $b=10^3r_g$. Then $x=10^4$ and $kb=(b/r_g)(r_gk)=10^3\times x=10^7$, using $r_gk=x$. So $\theta=2\cdot4\cdot10^4/10^7=8\times10^{-3}=8r_g/b$. Meanwhile $|\delta|\approx4\times10^4\ln(b/b_0)$. Letting $\hbar\to0$ at fixed $E$, $b$ makes $\delta$ larger and leaves $\theta$ unchanged.

## 3. What was wrong in answer-4 §2 (algebra established; diagram identification not verified by me in detail)

Expand $e^{2i\delta}=\sum_n(2i\delta)^n/n!$. The $n=1$ term is tree-level exchange, and the $n$-th term comes from ladder diagrams with $n-1$ loops (eikonal exponentiation). At fixed $E$, each term goes as $x^n\propto\hbar^{-n}$, so each one diverges as $\hbar\to0$. But $|e^{2i\delta}|=1$ for every $\hbar$, and $\theta$ stays finite. So "grows without bound" correctly says that the **power series in $x$ is useless at large $x$**. It does not say the physics is non-classical. Whether a result is classical can be decided for the summed observable, not term by term.

## 4. Corrected statement: three lengths

Let $\bar\lambda=\hbar c/E$ and $r_g=GE/c^4$. Then exactly:
- $\bar\lambda\,r_g=\dfrac{\hbar c}{E}\cdot\dfrac{GE}{c^4}=\dfrac{\hbar G}{c^3}=\ell_P^2$
- $r_g/\bar\lambda=x$ (answer-4), so $r_g/\ell_P=r_g/\sqrt{\bar\lambda r_g}=\sqrt{r_g/\bar\lambda}=E/E_P$

$\ell_P$ is the geometric mean of $\bar\lambda$ and $r_g$, and this gives three regimes:
- **$E\ll E_P$:** $r_g\ll\ell_P\ll\bar\lambda$. Gravity is weak. Loop terms are small relative corrections of size $x$, and they vanish as $\hbar\to0$ at fixed $k$ (answer-2). **Established within the effective theory.**
- **$E\gg E_P$, $b\gg r_g$:** $\bar\lambda\ll\ell_P\ll r_g\ll b$. Classical particle scattering applies; the loop terms are large but sum to a classical phase. **Heuristic, widely held** ('t Hooft; Amati, Ciafaloni and Veneziano). For $b\lesssim r_g$, black-hole formation is expected: **heuristic**.
- **$E\sim E_P$, distances $\sim\ell_P$:** all three lengths are comparable and no ratio is small, so neither expansion applies. **Open.**

The two limits are different. $\hbar\to0$ at fixed $k$ (waves) sends $x\to0$; $\hbar\to0$ at fixed $E$ (particles) sends $x\to\infty$. So "$(E/E_P)^2$ sets the size of quantum corrections" is correct for $E\ll E_P$, as a relative correction to the tree result. It is not a claim about every quantity of that size. For answer-0's question, this sharpens the claim: $t_P=\hbar/E_P$ marks where no small parameter is left (scales near $\ell_P$, $t_P$). It does not mark a failure for every process with $E>E_P$.

---

**Check yourself:** For $E=0.01\,E_P$, put $\bar\lambda$, $\ell_P$ and $r_g$ in order and name the regime. If you then let $\hbar\to0$ at fixed $E$, which regime do you end up in?

**Sources:** Griffiths, *Introduction to Quantum Mechanics*, chapter on the WKB approximation (ch. 8 in 2nd ed.); Feynman & Hibbs, *Quantum Mechanics and Path Integrals*, ch. 2 (classical limit by stationary phase); Sakurai, *Modern Quantum Mechanics*, sec. 2.6 (path integrals; section number not verified by me); Zee, *QFT in a Nutshell*, ch. VIII.1; 't Hooft, *Phys. Lett. B* 198, 61 (1987); Amati, Ciafaloni & Veneziano, *Phys. Lett. B* 197, 81 (1987).
