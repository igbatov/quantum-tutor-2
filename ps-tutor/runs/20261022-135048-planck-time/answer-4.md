# When $(E/E_P)^2$ measures quantum corrections, and when it does not

**You're right: answer-2 did not settle this.** Its reason was "at fixed $k$ the factor goes to 0 as $\hbar\to0$, as a quantum correction should". That reason depends on holding $k$ fixed, and answer-3 then showed that the verdict depends on which variables you hold fixed. The correct statement has a condition. Suppose the process has no scale except $E$ (or $k$) and dimensionless angles. Then classical general relativity cannot form any dimensionless number, so every $E$-dependent correction contains $\hbar$ whichever variables you use. In that case the loop terms and the quantum corrections are the same thing. If a second scale is present (a mass, or an impact parameter), a term of size $(E/E_P)^2$ can be partly or entirely classical.

## 1. The conversion changes bookkeeping, not the term (established)

For one massless quantum, $E=\hbar ck$ holds exactly (relativistic; $E$ and $k$ measured in the same frame). So
$$\Big(\frac{E}{E_P}\Big)^2=\frac{GE^2}{\hbar c^5}=\frac{G\hbar^2c^2k^2}{\hbar c^5}=\frac{G\hbar k^2}{c^3}=(\ell_Pk)^2 .$$
This is one number written in two sets of variables. Rewriting a term cannot change its physics. A term is **classical** if it tends to a finite nonzero value as $\hbar\to0$ while the quantities of the classical theory are held fixed. The $\hbar$ count of a diagram uses wavenumbers instead. The two classifications can disagree only when the term can be rewritten so that $\hbar$ disappears. That rewriting is what "moves $\hbar$ between orders" meant in answer-3.

## 2. With one scale, $\hbar$ cannot be removed (established: dimensional analysis)

Look for powers making $G^\beta E^\alpha c^\gamma$ dimensionless:
- kg: $-\beta+\alpha=0$
- m: $3\beta+2\alpha+\gamma=0$
- s: $-2\beta-2\alpha-\gamma=0$

Add the m and s equations: $\beta=0$. The kg equation then gives $\alpha=0$, and the m equation gives $\gamma=0$. With $k$ instead of $E$: $[k]=\mathrm{m^{-1}}$ has no kg, so the kg equation alone gives $\beta=0$, and the other two then give $\alpha=\gamma=0$. In both cases only the trivial solution exists.

So classical GR, whose only constants are $G$ and $c$, cannot produce a dimensionless correction that depends on $E$ or $k$ when nothing else sets a scale. Every such correction needs $\hbar$, and by answer-1 §1 it is a function of $(E/E_P)^2$. Neither limit gives a finite classical value:
- At fixed $k$, $(\ell_Pk)^2\to0$.
- At fixed $E$, $GE^2/\hbar c^5$ grows without bound. This signals that the expansion fails. It is not a classical term appearing.

**Physical reading (exact identity).** Let $r_g=GE/c^4$ be the gravitational radius of the energy $E$, a classical length ($r_s=2r_g$). Let $\bar\lambda=1/k=\hbar c/E$ be the reduced wavelength, a quantum length. Then
$$\frac{r_g}{\bar\lambda}=\frac{GE}{c^4}\cdot\frac{E}{\hbar c}=\frac{GE^2}{\hbar c^5}.$$
**Worked example:** for a 1 TeV quantum, $E=1.60\times10^{-7}$ J:
- $r_g=(6.674\times10^{-11})(1.60\times10^{-7})/(8.08\times10^{33})\approx1.32\times10^{-51}$ m
- $\bar\lambda=(1.0546\times10^{-34})(2.998\times10^{8})/(1.60\times10^{-7})\approx1.98\times10^{-19}$ m
- the ratio is $\approx6.7\times10^{-33}$, which agrees with $(1.60\times10^{-7}/1.96\times10^{9})^2$

## 3. Where $\hbar$ cancels: a second scale (algebra established; physics partly not verified)

- **Mass $m$.** Multiply the loop factor by $(mc/\hbar)/k$:
$$\frac{G\hbar k^2}{c^3}\cdot\frac{mc}{\hbar k}=\frac{Gmk}{c^2}\;\xrightarrow{\;k\sim1/r\;}\;\frac{Gm}{rc^2}.$$
Here $\hbar$ has cancelled, which is how answer-3's classical one-loop term $3G(m_1+m_2)/rc^2$ can arise.
- **Impact parameter $b$, massless quanta.**
$$\frac{(\ell_Pk)^2}{kb}=\frac{G\hbar k}{c^3b}=\frac{GE}{c^4b}=\frac{r_g}{b}.$$
This is free of $\hbar$. Small-angle scattering at $kb\gg1$ ('t Hooft 1987; Amati, Ciafaloni, Veneziano 1987; **not verified by me in detail**) has a phase of order $(E/E_P)^2\times\ln b$. Its $b$-dependence gives a classical deflection angle of order $r_g/b$. A phase of order $S/\hbar$ is the classical action counted in units of $\hbar$. So a quantity of size $(E/E_P)^2$ can be classical. **Heuristic, widely held:** for $b\gg r_g$, classical GR is expected to describe such scattering even when $E>E_P$.
- **Infrared.** Loops with massless gravitons contain soft-graviton divergences. They cancel in suitably inclusive cross sections (Weinberg 1965; established), but the detector resolution then enters as a second scale. The single-scale statement holds for quantities in which these effects cancel.

## 4. Corrected statement (for answer-0 §2(b))

Take a process with no masses, angles of order 1, an infrared-safe observable, and $E\ll E_P$. Then the corrections to the classical GR (tree) result are loop terms, they are quantum, and their relative size is $(E/E_P)^2$, up to coefficients and $\ln(E/\mu)$ terms. This is **established within the effective theory**. Answer-0's "they reach order 1 near $t_P$, so the scheme stops working" applies to this single-scale case only. With a second scale, separate the $\hbar$-free part (classical GR) from the rest. Linking $\hbar/E$ to a time $\Delta t$ remains **heuristic**.

---

**Check yourself:** Hold $E$ and $b$ fixed and let $\hbar\to0$. What happens to $(E/E_P)^2$, to $kb$, and to their ratio $r_g/b$? Which of the three is a quantity of classical GR?

**Sources:** Zee, *Quantum Field Theory in a Nutshell* (2nd ed.), ch. VIII.1; Donoghue, "Introduction to the effective field theory description of gravity", arXiv:gr-qc/9512024 (1995); Holstein & Donoghue, *Phys. Rev. Lett.* 93, 201602 (2004); 't Hooft, *Phys. Lett. B* 198, 61 (1987); Amati, Ciafaloni & Veneziano, *Phys. Lett. B* 197, 81 (1987); Weinberg, *Phys. Rev.* 140, B516 (1965).
