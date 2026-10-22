# Why $t_P$ is a limit of our theories, not only of an expansion

**You're right: "no small parameter is left" shows only that the perturbative expansion stops working.** That fact alone does not support answer-0's bottom line, "$t_P$ marks where our theories are expected to need replacement". QCD is a counterexample. Two steps were missing. First, the quantum theory of gravity we actually have is *defined* by this expansion, and the expansion needs a new, undetermined coefficient at every order. Second, near $t_P$ all of these coefficients matter at once. Your possibility, that a theory of the quantized metric is still right there, is open (**contested**, section 4).

## 1. When the expansion fails, the theory can survive (established)

In QCD the expansion parameter is the strong coupling $\alpha_s$. It is dimensionless, and it becomes of order 1 below about 1 GeV, where perturbation theory fails. Even so, QCD keeps the same few parameters (one coupling and the quark masses). Solved numerically on a lattice, it gives light-hadron masses that agree with measurement to a few per cent (Dürr et al. 2008; the precision is not verified by me in detail). So failure of the method is not failure of the theory.

## 2. What is different for gravity (established: power counting)

Take a process whose only scale is a wavenumber $k$ (answer-4's condition). By answers 2 and 3, $L$ loops multiply the tree result by $(\ell_Pk)^{2L}$.

1. Loop integrals diverge. A theorem of perturbative QFT (BPHZ) says the divergent part is *local*, meaning a polynomial in the external wavenumbers. In dimensional regularization no new length enters, so the divergence carries the same factor $\ell_P^{2L}k^{2L}$.
2. The tree term comes from the Einstein–Hilbert action, $R\sim\partial\partial g$, and has two derivatives, so it goes as $k^2$. The $L$-loop divergence therefore goes as $k^{2+2L}$.
3. Cancelling it requires a term in the action with $2+2L$ derivatives, for example $R^{L+1}$ (each $R$ carries two). General relativity has no such term. It has to be added with a coefficient $a_L$ that GR does not fix, so $a_L$ has to be measured.

Checking units: the Einstein–Hilbert density is $\frac{c^3}{16\pi G}R$. A term $a_n\hbar\,\ell_P^{2n-2}R^{n+1}$ has the same units, and the ratio of the two is
$$\frac{a_n\hbar\,\ell_P^{2n-2}R^{n+1}}{(c^3/G)\,R}=a_n\frac{\hbar G}{c^3}\ell_P^{2n-2}R^n=a_n(\ell_P^2R)^n$$
(the $16\pi$ is absorbed into $a_n$). With $R\sim k^2$, the $n$-th term is a relative correction of size $a_n(\ell_Pk)^{2n}$. Pure gravity needs the $R^3$ term at two loops (Goroff & Sagnotti 1986; established). With matter, $R^2$ terms are already needed at one loop ('t Hooft & Veltman 1974).

**Contrast with QCD:** the loop factor is $\alpha_s^L$, with no $k^{2L}$. So the divergences can be absorbed into terms already present, and the number of parameters stays finite. This property is called renormalizability (established).

## 3. What this implies at $t_P$ (established within the effective theory)

- For $k\ll1/\ell_P$, each $a_n$ term is suppressed by $(\ell_Pk)^{2n}$. Measuring finitely many coefficients gives predictions to any required accuracy.
- For $k\sim1/\ell_P$, which means times $\sim t_P$, every term is of size $a_n$. Infinitely many unknown numbers enter on an equal footing. The theory then does not determine the answer. This is not because we cannot calculate: even an exact solution of this action would still need all the $a_n$. It is a statement about what the theory contains, not about the method.

That is the precise sense of "limit of our theories": near $t_P$ they need input that they do not contain.

**Worked example (Fermi's weak-interaction theory).** In units $\hbar=c=1$, $G_F=1.166\times10^{-5}\ \mathrm{GeV^{-2}}$. This has the same unit structure as $G=1/E_P^2$ with $E_P=1.22\times10^{19}$ GeV, so the theory has the same tower of new coefficients. Its expansion parameter is $G_FE^2$:
- $G_FE^2=1$ at $E=1/\sqrt{1.166\times10^{-5}}\ \mathrm{GeV}\approx293$ GeV.
- The theory was in fact replaced by electroweak theory. Its new particle, the W boson, sits at 80.4 GeV, where $G_FE^2=1.166\times10^{-5}\times80.4^2\approx0.075$ (established).

**Heuristic lesson:** a theory of this type has been replaced before, and the new physics appeared *below* the scale where the parameter reaches 1. This does not prove that gravity will follow the same path.

## 4. What remains open (contested)

The coefficients $a_n$ have to come from somewhere outside the present theory:
- **A different theory** (string theory, loop quantum gravity, ...): the metric description is replaced.
- **Asymptotic safety** (Weinberg 1979): the quantized metric stays valid at all energies, because a fixed point of the renormalization flow fixes all but finitely many $a_n$. Renormalization-group calculations in truncated form (Reuter 1998 onward) support it, but it is not proven. This is your scenario.

Either way, something that our current theories do not contain is needed.

**A separate argument, not perturbative:** Penrose's theorem (1965; established) assumes a positive-energy condition and a trapped surface, which forms inside a collapsing star. Under these conditions classical GR predicts light rays that end after a finite affine parameter. So classical GR predicts its own incompleteness. That quantum effects take over where $\ell_P^2R\sim1$ (section 2) is **heuristic**.

**Summary of status:**
- The expansion fails near $t_P$: established.
- Our theories stop making predictions near $t_P$: established within the effective theory.
- The metric description itself fails there: heuristic and widely held; asymptotic safety contests it.
- Time is discrete: open, with no evidence.

---

**Check yourself:** Using step 3 of section 2, how many derivatives does the two-loop counterterm have? Check that $R^3$ has that many.

**Sources:** Zee, *Quantum Field Theory in a Nutshell* (2nd ed.), ch. III.2 (nonrenormalizable interactions, Fermi theory) and ch. VIII.1; Peskin & Schroeder, *An Introduction to QFT*, sec. 10.1 (counting UV divergences); Wald, *General Relativity*, ch. 9 (singularity theorems); Donoghue, *Phys. Rev. D* 50, 3874 (1994); Goroff & Sagnotti, *Nucl. Phys. B* 266, 709 (1986); 't Hooft & Veltman (1974); Weinberg, in *General Relativity: An Einstein Centenary Survey* (1979); Reuter, *Phys. Rev. D* 57, 971 (1998); Dürr et al., *Science* 322, 1224 (2008); Penrose, *Phys. Rev. Lett.* 14, 57 (1965).
