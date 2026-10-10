VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "squared length $(\lambda-p)^2 + p(1-p)/N$, shortest at $\lambda = p$" | PASS | checks/check_B_01.py: exact sympy sum over all $2^N$ strings, N = 1..6, difference 0; argmin = p |
| 2 | "$p = 0.1$: 0.045 at N = 2, 0.0009 at N = 100, 0.000009 at N = $10^4$" | PASS | check_B_01.py: 0.045, 9e-4, 9e-6 |
| 3 | "$\langle P^{(k)}\rangle = p$ ... $\langle F_N^2\rangle = p^2 + p(1-p)/N$" | PASS | check_B_01.py: symbolic, N = 1..6; $\langle P^{(j)}P^{(k)}\rangle = p^2$ numerically |
| 4 | "$\sum w_m = 1$"; "for N = 4 the five values are 1, 4, 6, 4, 1" | PASS | check_B_03.py: w_m from explicit lists equals the binomial formula, sum 1, for p = 0.1, 0.5, 0.73 |
| 5 | $F_2$ matrix, $P^{(1)}$ diag (0,0,1,1), $P^{(2)}$ diag (0,1,0,1), $P\cdot P = P$ | PASS | check_B_03.py |
| 6 | "eigenvalues ... 0, 1/N, ..., 1; eigenvectors ... one and the same m" | PASS | check_B_03.py: N = 2,3,4,6, eigenvalue m/N with multiplicity C(N,m) |
| 7 | "not an eigenvector ... at any finite N"; "p = 0.1 is not among" the N = 4 readings | PASS | check_B_03.py: minimum remainder > 0; with #1, the minimum is p(1-p)/N > 0 for 0 < p < 1 |
| 8 | N = 2, p = 0.1 hand-check: $\Psi_2 = (0.9, 0.3, 0.3, 0.1)$; remainders; 0.055, 0.045, 0.205, 0.855 | PASS | check_B_02.py: every entry and squared length matches |
| 9 | "$\sqrt{p(1-p)/N}$ ... 0.05 ... at p = 1/2, 0.03 at p = 0.1" (N = 100) | PASS | check_B_02.py |
| 10 | Projection noise "variance $Np(1-p)$ ... 25 ... sd 5 ... 9 ... sd 3"; zero at p = 0, 1, largest at 1/2; table of pictures (50, 5 / 10, 3 / 100, 0) | PASS | check_B_04.py: binomial variance 25 and 9; argmax at 0.5 |
| 11 | "slightly different fields, which lowers the scatter a little" | PASS | check_B_04.py: $\sum p_i(1-p_i) \le N\bar p(1-\bar p)$ in 2000 random static spreads (max difference -0.054) |
| 12 | "amplitude of size $\sin(\Omega t/2)$ for up and $\cos(\Omega t/2)$"; "trace $\sin^2(\Omega t/2)$"; length or detuning sets any p in [0,1] | PASS | check_B_05.py: sympy propagator gives (cos, -i sin); a detuning scan at a fixed pi-pulse covers p from 4e-11 to 1 |
| 13 | "error bars of size $\sqrt{p(1-p)/M}$" | PASS | check_B_04.py |
| 14 | Chebyshev chain "$D_\varepsilon(N) \le p(1-p)/(N\varepsilon^2)$" | PASS | check_B_06.py: each inequality checked numerically for 9 (N, p) pairs; $\sum w_m(m/N-p)^2 = p(1-p)/N$ |
| 15 | Deviant table: 100/N, 36/N, $2e^{-2N\varepsilon^2}$ = 1.21, 0.0135, 3.9e-22, below $10^{-2000}$ | PASS | check_B_06.py: 1.2131, 0.013476, 3.857e-22, $10^{-2171}$; the exact tail never exceeds any bound |
| 16 | "sharper bound $2e^{-2N\varepsilon^2}$ (Hoeffding 1963), any p" | FAIL | check_B_06.py: at N = 100 Hoeffding gives 1.21, which is weaker than Chebyshev (1 at p = 1/2, 0.36 at p = 0.1). It is sharper only from roughly N = 500 (p = 1/2) or N = 900 (p = 0.1) on. Correct statement: "exponential bound $2e^{-2N\varepsilon^2}$ (Hoeffding 1963), any p: weaker than Chebyshev at N = 100, far sharper for large N" |
| 17 | "exact value at N = 1000 and p = 1/2 is about 0.0014"; "the exact value fastest" | PASS | check_B_06.py: 0.001392; exact/Hoeffding ratio falls from 0.10 (N = 1000) to 0.033 (N = $10^4$) |
| 18 | Overlap of product lists "$(c_0c_0' + c_1c_1')^N$" | PASS | check_B_07.py: explicit lists for N = 1, 2, 3, 5 |
| 19 | "differ by 1° (p = 0.100 against p = 0.111)"; "0.9998477"; "$e^{-15.23} \approx 2.4\times10^{-7}$" | PASS | check_B_07.py: angle 1.026°, cos 1° = 0.9998477, exponent -15.232, value 2.43e-7 |
| 20 | q-size: ratio $(N-m)/(m+1)\cdot(c_1/c_0)^q$; $f_q = c_1^q/(c_0^q + c_1^q)$; table 0.25, 0.10, 0.0357, 0.0122; totals $1.2649^N$, 1, $0.8854^N$, $0.82^N$ | PASS | check_B_08.py: sympy ratio; the peak of the q-size at N = 2000 sits at $f_q$ (within 1/N); table values match |
| 21 | "Only q = 2 delivers p"; equal amplitudes "every q gives 1/2" | PASS | check_B_08.py: scan of q in [0.5, 6] for p = 0.05, 0.1, 0.3, 0.7 finds only q = 2 |
| 22 | "only the 2-norm is kept fixed by linear maps that move amplitude ... a little at a time" | PASS | check_B_08.py: a small rotation keeps the 2-size at 1 and changes the 1- and 3-sizes (numerical illustration; the general theorem is the cited Banach–Lamperti result) |
| 23 | Many-worlds N = 4 table; "Eleven of the sixteen branches, 69% ... weight 0.0523" | PASS | check_B_09.py: 11/16 = 68.75%, weight 0.0523 |
| 24 | "for N = 20 the most numerous branches have fraction 1/2 ... most weight has fraction 0.1" | PASS | check_B_09.py: argmax C(20,m) at m = 10; argmax w_m at m = 2 |
| 25 | Everett: additive weight on merging "must be the squared entry" | PASS | check_B_09.py: $f(\sqrt{a^2+b^2}) = f(a) + f(b)$ holds for $x^q$ only at q = 2 (the general case follows from Cauchy's equation plus monotonicity) |
| 26 | Model 2 / coin-list table lines 2–6: binomial mean p, variance p(1-p)/N, same Chebyshev bound | PASS | check_B_01.py, check_B_04.py, check_B_06.py |
| 27 | Figure caption numbers: maxima 0.158, 0.050, 0.0158; N = 4 heights; spreads 0.25 and 0.15 | PASS | check_B_04.py, check_B_09.py; figure scripts compute them |

Pass count: 26/27.

## Figures
Requested:
- b-projection-noise: figures/b-projection-noise.png (checks/fig_b-projection-noise.py). Drawn as specified. The curves are distinguished by line style. The certainty ends are marked, and the N = 100 annotation points to p = 1/2 and p = 0.1. The caption is true.
- b-counter-readings: figures/b-counter-readings.png (checks/fig_b-counter-readings.py). It shows the stacked blocks (1, 4, 6, 4, 1), the printed heights, the dashed line at p, and the spread brackets. The caption is true. In the right panel the bracket runs from -0.05 to 0.25 because p - spread < 0. That is expected.

Added, one per section without a figure (proposed captions, each checked against the computation):
- b-opening (opening paragraph): figures/b-opening.png. Proposed caption: "Left: squared length of the remainder $(F_N-\lambda)\Psi_N$ against $\lambda$ for p = 0.1 and N = 2, 10, 100. Each curve is a parabola with its lowest point at $\lambda = p$. Right: that lowest value, p(1-p)/N, falls as 1/N (0.045, 0.0009, 0.000009 at N = 2, 100, $10^4$) but is not zero at any finite N."
- b-what-this-rules-out: figures/b-what-this-rules-out.png. Proposed caption: "Run-to-run counts for 100 ions at p = 1/2 and p = 0.1. Tickets, a biased coin and the quantum rule all give the same binomial histogram (mean 50, spread 5; mean 10, spread 3). The fixed-share glow picture gives the same light in every run (dashed line, true height 1). Only that picture is ruled out by counts."
- b-model-2: figures/b-model-2.png. Proposed caption: "The weights $w_m = C(N,m)p^m(1-p)^{N-m}$ for p = 0.1, scaled by N, against the fraction m/N, for N = 10, 100, 1000. Read them as coin probabilities or as squared lengths: the numbers are the same. They pile up inside the band $|m/N - p| \le 0.05$ as N grows, with spread $\sqrt{p(1-p)/N}$ = 0.095, 0.030, 0.009."
- b-model-3: figures/b-model-3.png. Proposed caption: "N = 20 ions, p = 0.1. Hatched bars show the share of the $2^{20}$ branches with each recorded fraction; this peaks at 1/2 whatever p is. Solid bars show the share of the total weight; this peaks at 0.1. Counting worlds and weighing them pick different 'typical' records."
- b-how-they-relate: figures/b-how-they-relate.png. Proposed caption: "The fraction $f_q$ at which the q-size of the N-copy list concentrates, against $p = |c_1|^2$, for q = 1, 2, 3, 4. Only q = 2 lies on $f = p$; at p = 0.1 the four values are 0.25, 0.10, 0.036, 0.012. All q agree at p = 0, 1/2 and 1, so an equal split cannot reveal the exponent."

I viewed every PNG after the final run.

## Notes
- Row 16 is the only FAIL. It is a wording issue with the label "sharper"; the table's numbers are right. The table itself shows Hoeffding is no sharper at N = 100.
- "Unless the two single-ion states are the same (overlap 1), this goes to zero" is true for the text's real non-negative amplitudes. With general amplitudes, say "the same up to an overall phase (|overlap| = 1)".
- p = 0.100 against 0.111 is a 1.03° separation, not exactly 1°. "For instance" covers this.
- Row 11 assumes a static spread of the pulse across ions. Field noise that changes from shot to shot would raise the scatter instead.
- Conceptual and attribution claims (Squires, Caves–Schack, Gleason, Bell 1966, DGZ equivariance, Gisin, Itano's measured agreement) were not checked by computation and are not counted.
