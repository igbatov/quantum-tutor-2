# Is the Planck time the shortest possible time?

**The premise is wrong.** No experiment and no accepted theory shows that the Planck time, $t_P\approx5.4\times10^{-44}$ s, is the shortest possible time. What is known is narrower. $t_P$ is the time scale you can build from $\hbar$, $G$ and $c$. Near it, the quantum theory of gravity we have stops making predictions, because there it needs infinitely many numbers that it does not contain. That is a limit of our theories. It is not a proven minimum in nature.

## 1. Where $t_P$ comes from (established: dimensional analysis)

We look for powers with $[\hbar^aG^bc^d]=\mathrm{s}$. The units are $[\hbar]=\mathrm{kg\,m^2\,s^{-1}}$, $[G]=\mathrm{m^3\,kg^{-1}\,s^{-2}}$ and $[c]=\mathrm{m\,s^{-1}}$.
- kg: $a-b=0$, so $b=a$.
- m: $2a+3b+d=0$, so $d=-5a$.
- s: $-a-2b-d=1$. Substituting gives $2a=1$, so $a=\tfrac12$.

The result is $t_P=\sqrt{\hbar G/c^5}$. Numerically, $\hbar G=7.039\times10^{-45}$ and $c^5=2.422\times10^{42}$. Their ratio is $2.906\times10^{-87}$, whose square root is $5.39\times10^{-44}$ s. Related scales: $\ell_P=ct_P\approx1.62\times10^{-35}$ m and $E_P=\hbar/t_P=\sqrt{\hbar c^5/G}\approx1.96\times10^9$ J.

- The value is fixed only up to a dimensionless factor. Using $h$ instead of $\hbar$ makes it $\sqrt{2\pi}\approx2.5$ times larger. Using $8\pi G$ gives $\approx2.7\times10^{-43}$ s.
- A unit is not a minimum. $0.01\,t_P$ is a meaningful time. Planck (1899) proposed these units because they do not depend on human conventions. He did not propose them as limits.

## 2. A thought experiment (heuristic)

A signal moving at $c$ crosses a distance $L=c\Delta t$ in time $\Delta t$. So timing to within $\Delta t$ needs a probe localized to roughly $L$. This is relativistic kinematics, and it is an order-of-magnitude estimate.

1. *Quantum step.* Light resolves features about its wavelength in size, so $\lambda\lesssim L$. Its energy is $E=2\pi\hbar c/\lambda\gtrsim2\pi\hbar c/L$.
2. *Classical GR step.* A spherical mass $E/c^2$ inside its Schwarzschild radius $r_s=2GE/c^4$ forms a black hole. For energy that is not spherical, the hoop conjecture says roughly the same, but it is unproven. Here $E$ means the energy in the frame where the total momentum is zero.
3. *Combine.* Setting $\lambda=L$ and $L=r_s$ gives $L^2=4\pi\hbar G/c^3$. So $L\approx3.5\,\ell_P$ and $\Delta t\approx3.5\,t_P$.

This argument joins $E=hc/\lambda$ to a classical horizon in exactly the regime where neither has been tested. It gives a reason to expect new physics there. It does not derive a minimum time.

## 3. The firmer argument: gravity as an effective quantum field theory

**(a) There is only one dimensionless number (established).** Make $GE^\alpha\hbar^\beta c^\gamma$ dimensionless. The kg equation gives $\beta=1-\alpha$, the m equation gives $\gamma=-5$, and the s equation gives $\alpha=2$, $\beta=-1$. So the number is $x\equiv GE^2/\hbar c^5=(E/E_P)^2$.

Now drop $\hbar$ and try $G^\beta E^\alpha c^\gamma$. The equations are kg $\alpha=\beta$, m $3\beta+2\alpha+\gamma=0$ and s $-2\beta-2\alpha-\gamma=0$. Adding the m and s equations gives $\beta=0$, and then $\alpha=\gamma=0$. So in a process whose only scale is $E$, classical GR cannot form any dimensionless correction that depends on $E$, and every such correction contains $\hbar$. For one massless quantum, $E=\hbar ck$ holds exactly (relativistic), so $x=G\hbar k^2/c^3=(\ell_Pk)^2$.

**(b) Each loop brings one factor $G\hbar$ (established, in perturbation theory).** Expand the metric around flat spacetime as $g=\eta+\kappa h$, with $\kappa^2=32\pi G$ in units where $c=1$. In the Einstein–Hilbert action, a vertex where $n$ lines meet then carries $\kappa^{n-2}$. Take a diagram with $V$ vertices, $I$ internal lines, $E_{\rm ext}$ external lines and $L=I-V+1$ loops. Each internal line ends at two vertices and each external line at one, so $\sum_vn_v=2I+E_{\rm ext}$. The total power of $\kappa$ is therefore $2I+E_{\rm ext}-2V=E_{\rm ext}+2L-2$, which means one $\kappa^2\propto G$ per loop.

Now count $\hbar$, with the parameters in $S$ held fixed and independent of $\hbar$. In a one-variable model, $S=\tfrac12ax^2$ and the weight is $e^{-S/\hbar}$. Then $I(a)=\int e^{-ax^2/2\hbar}dx=\sqrt{2\pi\hbar/a}$, and $dI/da=-\frac1{2\hbar}\int x^2e^{-ax^2/2\hbar}dx$. So
$$\langle x^2\rangle=-2\hbar\,\frac{d\ln I}{da}=-2\hbar\Big(-\frac1{2a}\Big)=\frac{\hbar}{a}.$$
So a propagator is $\propto\hbar$. A vertex comes from $S/\hbar$, so it is $\propto1/\hbar$. An amputated diagram (external propagators removed) therefore goes as $\hbar^{I-V}=\hbar^{L-1}$. With the real-time weight $e^{iS/\hbar}$, only factors of $i$ change. Each loop multiplies the result by $G\hbar k^2/c^3=(\ell_Pk)^2$.

**(c) Conditions.** "Loop correction = quantum correction of size $x$" holds for a single-scale, infrared-safe quantity (Weinberg 1965), up to terms $\ln(E/\mu)$ that come from renormalization. With a second scale, $\hbar$ can cancel. Multiply by $(mc/\hbar)/k$: the result is $Gmk/c^2\sim Gm/rc^2$. This is how a classical term, $3G(m_1+m_2)/rc^2$, appears at one loop in the corrected Newton potential (Bjerrum-Bohr, Donoghue, Holstein 2003; not verified by me in detail). The reverse also happens: tree-level Compton scattering contains quantum terms in $\hbar\omega/mc^2$. So "one loop" and "quantum" overlap, but neither implies the other in general.

**(d) What $\hbar\to0$ does depends on what is held fixed.** Let $\bar\lambda=\hbar c/E$ (a quantum length) and $r_g=GE/c^4$ (a classical length). Then, exactly, $\bar\lambda r_g=\ell_P^2$ and $r_g/\bar\lambda=x$.
- At fixed $k$, $\hbar\to0$ sends $x\to0$.
- At fixed $E$, it sends $x\to\infty$.

Large $x$ need not mean non-classical physics. Consider small-angle scattering of two quanta at impact parameter $b\gg r_g$, with $E\gg E_P$. The eikonal phase is $\delta\approx-Cx\ln(b/b_0)$. It diverges as $\hbar\to0$, as every phase does: compare $e^{ipx/\hbar}$. Classicality is a property of observables. By stationary phase, the momentum transfer is $q=2|d\delta/db|=2Cx/b$. The angle is then $\theta=q/k=2Cx/(kb)=2Cr_g/b$, and $\hbar$ has cancelled ('t Hooft 1987; Amati, Ciafaloni, Veneziano 1987; the value of $C$ is not verified by me). Three regimes follow:
- $E\ll E_P$, so $r_g\ll\ell_P\ll\bar\lambda$: quantum corrections have relative size $x$. **Established within the effective theory.**
- $E\gg E_P$ with $b\gg r_g$: classical GR describes the scattering. **Heuristic, widely held.**
- Distances near $\ell_P$ and times near $t_P$: all three lengths are comparable and no ratio is small. **Open.**

## 4. Why this is a limit of the theory, not only of the method

Losing the small parameter only shows that perturbation theory fails. QCD is the counterexample: at $\alpha_s\sim1$, lattice calculations still reproduce hadron masses (Dürr et al. 2008). Gravity is different (established, power counting):

1. Loop divergences are local (the BPHZ theorem). The $L$-loop divergence goes as $k^2(\ell_Pk)^{2L}$, so it has $2+2L$ derivatives.
2. Cancelling it needs a new term such as $R^{L+1}$, whose coefficient $a_L$ GR does not fix. Pure gravity needs the $R^3$ term at two loops (Goroff & Sagnotti 1986).
3. Check the units. Dividing $a_n\hbar\,\ell_P^{2n-2}R^{n+1}$ by $(c^3/G)R$ gives $a_n(\ell_P^2R)^n$. With $R\sim k^2$, this is a relative correction of size $a_n(\ell_Pk)^{2n}$.

For $k\ll1/\ell_P$, a finite number of measured $a_n$ gives predictions to any required accuracy. For $k\sim1/\ell_P$, every $a_n$ enters at full size, and the theory does not determine the result. Even an exact solution of this action needs all the $a_n$ as input. So near $t_P$, our theories need input that they do not contain.

*Precedent (heuristic lesson only).* Fermi's weak-interaction theory has $G_F=1.166\times10^{-5}\ \mathrm{GeV^{-2}}$. Its parameter $G_FE^2$ reaches 1 at $E=(1.166\times10^{-5})^{-1/2}\approx293$ GeV. It was replaced by electroweak theory, whose W boson sits at 80.4 GeV, where $G_FE^2\approx0.075$.

**Contested:** asymptotic safety (Weinberg 1979; Reuter 1998 onward) proposes that a fixed point fixes all but finitely many $a_n$, which keeps the quantized metric valid at all energies. Truncated calculations support it, but it is unproven. **Established, and a separate argument:** Penrose's theorem (1965) says that, given an energy condition and a trapped surface, classical GR predicts light rays that end after a finite affine parameter. That quantum effects take over where $\ell_P^2R\sim1$ is **heuristic**.

## 5. Experiments and candidate theories

- **Established:** quantum mechanics, QFT and GR, as formulated, all treat time as continuous.
- **Not verified by me in detail:** the shortest interval timed directly is about $2.5\times10^{-19}$ s (Grundmann et al. 2020). Colliders probe about $10^{-28}$ s indirectly (order of magnitude). Both are more than 15 orders of magnitude above $t_P$.
- **Not verified by me in detail:** Fermi saw no energy-dependent arrival delay from GRB 090510. For models in which the speed of light changes linearly with energy, this pushes the energy scale above about $E_P$, under assumptions about emission times (Abdo et al. 2009).
- **Contested:** loop quantum gravity has discrete area and volume spectra (whether they are observable is debated). Some string analyses find a minimum resolvable length. Causal sets postulate discreteness. None is confirmed, and none predicts a shortest duration equal to $t_P$.

**Status summary:** the perturbative expansion fails near $t_P$ (established); the effective theory stops predicting there (established within it); the metric description itself fails there (heuristic, contested by asymptotic safety); time is discrete (open, no evidence).

---

**Check yourself:** Take a single-scale process with $\ell_Pk=0.1$. What is the relative size of the one-loop correction and of the $a_2$ term? Why does $\ell_Pk=1$ change the theory's predictive power and not just the method of calculation?

**Sources:** Zee, *Quantum Field Theory in a Nutshell* (2nd ed.), ch. I.2, I.7, III.2, VIII.1; Griffiths, *Introduction to Quantum Mechanics*, WKB chapter; Feynman & Hibbs, *Quantum Mechanics and Path Integrals*, ch. 2; Carroll, *Spacetime and Geometry*, ch. 5; Wald, *General Relativity*, ch. 9; Peskin & Schroeder, sec. 10.1; Zwiebach, *A First Course in String Theory*, ch. 3; Rovelli, *Reality Is Not What It Seems*; Donoghue, *PRD* 50, 3874 (1994); Bjerrum-Bohr, Donoghue, Holstein, *PRD* 67, 084033 (2003); Goroff & Sagnotti, *NPB* 266, 709 (1986); 't Hooft, *PLB* 198, 61 (1987); Amati, Ciafaloni, Veneziano, *PLB* 197, 81 (1987); Hossenfelder, *Living Rev. Relativ.* 16, 2 (2013); Abdo et al., *Nature* 462, 331 (2009).
