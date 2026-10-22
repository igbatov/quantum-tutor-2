# Why a propagator carries $\hbar$ and a vertex carries $1/\hbar$

**You're right: I stated that without deriving it. I also left out two conditions it needs, and one sentence in my caveat was false.** The derivation is a Gaussian integral, done below in one variable and then in many. The two missing conditions: (i) the parameters in $S$ are held fixed and do not depend on $\hbar$; (ii) $\hbar^{L-1}$ counts *amputated* amplitudes, meaning the external propagators are stripped off. The false sentence was "every quantum correction needs loops" (section 4).

## 1. A one-variable model (established: calculus)

Replace the field by a single real variable $x$. Use the action $S(x)=\tfrac12 a x^2+\tfrac{\lambda}{24}x^4$ with $a,\lambda>0$ independent of $\hbar$. To keep the integrals convergent, I use the "Euclidean" weight $e^{-S/\hbar}$; the real-time weight $e^{iS/\hbar}$ case is treated in section 3. Averages are
$$\langle f\rangle=\frac{\int f\,e^{-S/\hbar}\,dx}{\int e^{-S/\hbar}\,dx}.$$

**Propagator.** Set $\lambda=0$ and write $\langle\ \rangle_0$ for averages in this case. The Gaussian integral is $I(a)=\int e^{-ax^2/2\hbar}dx=\sqrt{2\pi\hbar}\,a^{-1/2}$. Differentiating under the integral pulls down one $x^2$: $-2\hbar\,\frac{dI}{da}=\int x^2e^{-ax^2/2\hbar}dx$. Apply this $k$ times to $a^{-1/2}$:
- $k=1$: $(-2\hbar)(-\tfrac12)a^{-3/2}=\hbar\,a^{-3/2}$
- $k=2$: $(-2\hbar)(-\tfrac32)\hbar\,a^{-5/2}=3\hbar^2a^{-5/2}$
- $k=3$: $(-2\hbar)(-\tfrac52)3\hbar^2a^{-7/2}=15\hbar^3a^{-7/2}$

Divide by $I\propto a^{-1/2}$:
$$\langle x^2\rangle_0=\frac{\hbar}{a},\qquad\langle x^4\rangle_0=3\Big(\frac{\hbar}{a}\Big)^2,\qquad\langle x^6\rangle_0=15\Big(\frac{\hbar}{a}\Big)^3.$$
The quadratic part of $S/\hbar$ is $\tfrac12(a/\hbar)x^2$. Its inverse is $\hbar/a$, and that inverse is the propagator. The numbers 3 and 15 count the ways to split 4 and 6 factors of $x$ into pairs (Wick's theorem). Each pair contributes one propagator $\hbar/a$.

**Vertex.** Expand the interaction part of the weight: $e^{-\lambda x^4/24\hbar}=\sum_n\frac1{n!}\big(-\frac{\lambda}{24\hbar}\big)^nx^{4n}$. Each vertex, i.e. each factor $x^4$, comes with $\lambda/\hbar$, because it comes from $S/\hbar$.

**First correction.** Keep terms to first order in $\lambda$, in both the numerator and the denominator:
$$\langle x^2\rangle=\frac{\langle x^2\rangle_0-\frac{\lambda}{24\hbar}\langle x^6\rangle_0}{1-\frac{\lambda}{24\hbar}\langle x^4\rangle_0}\approx\frac{\hbar}{a}-\frac{\lambda}{24\hbar}(15-3)\frac{\hbar^3}{a^3}=\frac{\hbar}{a}\Big[1-\frac{\lambda\hbar}{2a^2}\Big].$$
The correction is one vertex ($1/\hbar$) times three propagators ($\hbar^3$). Two propagators run to the external points, and the third closes on itself, making one loop. **Relative to the leading term it carries one extra $\hbar$.** The expansion parameter $\lambda\hbar/a^2$ plays the same role as $G\hbar k^2/c^3$ in answer-2.

(The series in $\lambda$ is asymptotic, not convergent. This is established, but each finite order of the counting is exact.)

## 2. From one variable to fields (established)

Take $N$ variables with $S=\tfrac12x^TAx$, where $A$ is a symmetric matrix with positive eigenvalues. Rotate to $x=Oy$, with $O$ orthogonal and $O^TAO=\mathrm{diag}(a_k)$. The integral then factorizes, and by section 1, $\langle y_ky_l\rangle_0=\delta_{kl}\hbar/a_k$. Rotate back:
$$\langle x_ix_j\rangle_0=\sum_kO_{ik}O_{jk}\frac{\hbar}{a_k}=\hbar\,(A^{-1})_{ij}.$$
For a field, the index $i$ becomes a spacetime point and $A$ becomes the differential operator in the quadratic part of $S$. For example, a massless field has propagator $\hbar/k^2$ in momentum space. Treating fields as the $N\to\infty$ limit is the standard perturbative definition; a rigorous construction of interacting 4D path integrals is an open mathematical problem.

**General count.** Consider a connected diagram with $P$ propagators, $V$ vertices and $E$ external points. Treat the external points as end-vertices; then the loop number is $L=P-(V+E)+1$. The diagram is
$$\propto\hbar^{P-V}=\hbar^{L+E-1}.$$
Check against section 1: the leading term has $P=1$, $V=0$, $E=2$, so $L=0$ and $\hbar^1$. The correction has $P=3$, $V=1$, so $L=1$ and $\hbar^2$. Stripping the $E$ external propagators gives $\hbar^{L-1}$, which is answer-2's formula. **At fixed $E$, each loop adds one $\hbar$.**

For gravity, the Einstein–Hilbert action contains no $\hbar$. With answer-2's normalization of $h$, the graviton propagator is $\propto\hbar/k^2$ and each vertex is $\propto\kappa^{n-2}/\hbar$. So each loop brings $\kappa^2\hbar\propto G\hbar$.

## 3. Real time (established)

With the weight $e^{iS/\hbar}$, the Fresnel integral gives $\int e^{iax^2/2\hbar}dx=\sqrt{2\pi i\hbar/a}$, and $\langle x^2\rangle_0=i\hbar/a$. Vertices carry $-i\lambda/\hbar$. Only factors of $i$ change; the powers of $\hbar$ stay the same. The counting holds wherever the theory is defined by $e^{iS/\hbar}$: non-relativistic QM (paths) and relativistic QFT alike.

## 4. Correction, and the one-loop classical term

**"Every quantum correction needs loops" was false.** The correct statement is narrower. At fixed $\hbar$-independent parameters (couplings, wavenumbers, inverse lengths $mc/\hbar$), tree diagrams give the classical field result and loops give powers of $\hbar$. Physical results are usually expressed through masses $m$ and energies $\hbar\omega$, and that conversion moves $\hbar$ between orders, in both directions:
- *A loop term that is classical:* in the loop with massive matter lines, factors $mc/\hbar$ can cancel the loop's $\hbar$. This gives the $3G(m_1+m_2)/rc^2$ term (Holstein & Donoghue 2004; not verified by me in detail). So it is a consequence of rewriting in $m$, not a contradiction of the count.
- *A tree term that is quantum:* tree-level Compton scattering, the Klein–Nishina formula, differs from classical Thomson scattering by terms in $\hbar\omega/mc^2$ (established).

---

**Check yourself:** Using $\langle x^8\rangle_0=105(\hbar/a)^4$, find the order-$\lambda$ term in $\langle x^4\rangle$. What power of $\hbar$ does it carry? Does that match $\hbar^{L+E-1}$ for the connected tree diagram with one vertex?

**Sources:** Zee, *Quantum Field Theory in a Nutshell* (2nd ed.), ch. I.2 (Gaussian integrals, "mattress" to field) and ch. I.7 (the one-variable $x^4$ integral and Feynman diagrams); Peskin & Schroeder, *An Introduction to QFT*, sec. 9.2 (functional quantization) and sec. 5.5 (Compton scattering); loop expansion in $\hbar$: Coleman, *Aspects of Symmetry*, ch. 5 (section not verified by me); Holstein & Donoghue, *Phys. Rev. Lett.* 93, 201602 (2004).
