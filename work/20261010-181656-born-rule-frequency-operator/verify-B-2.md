VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "squared length $(\lambda-p)^2 + p(1-p)/N$, shortest at $\lambda = p$" | PASS | checks/check_B_01_2.py: exact sympy sum over all $2^N$ strings, N = 1..6, difference 0; argmin = p |
| 2 | "$p = 0.1$: 0.045 at N = 2, 0.0009 at N = 100, 0.000009 at N = $10^4$" | PASS | check_B_01_2.py: 0.045, 9e-4, 9e-6 |
| 3 | "$\langle P^{(k)}\rangle = p$ ... $\langle F_N^2\rangle = p^2 + p(1-p)/N$" | PASS | check_B_01_2.py: symbolic for N = 1..6; $\langle P^{(j)}P^{(k)}\rangle = p^2$ numerically |
| 4 | "$\sum w_m = 1$"; "for N = 4 the five values are 1, 4, 6, 4, 1" | PASS | check_B_03_2.py: w_m from explicit lists equals the binomial formula and sums to 1 (p = 0.1, 0.5, 0.73) |
| 5 | $F_2$ matrix, $P^{(1)}$ diag (0,0,1,1), $P^{(2)}$ diag (0,1,0,1), $P\cdot P = P$ | PASS | check_B_03_2.py |
| 6 | "eigenvalues ... 0, 1/N, ..., 1; eigenvectors ... one and the same m" | PASS | check_B_03_2.py: N = 2, 3, 4, 6, eigenvalue m/N with multiplicity C(N,m) |
| 7 | "not an eigenvector ... at any finite N"; "p = 0.1 is not among" the N = 4 readings | PASS | check_B_03_2.py together with #1: minimum remainder p(1-p)/N > 0 |
| 8 | N = 2, p = 0.1 table: $\Psi_2 = (0.9, 0.3, 0.3, 0.1)$; remainders; 0.055, 0.045, 0.205, 0.855 | PASS | check_B_02_2.py: every entry and squared length matches |
| 9 | "$\sqrt{p(1-p)/N}$ ... 0.05 ... at p = 1/2, 0.03 at p = 0.1" (N = 100) | PASS | check_B_02_2.py |
| 10 | "variance $Np(1-p)$ ... 25 ... sd 5 ... 9 ... sd 3"; zero at p = 0, 1; largest at 1/2; rule-out table (50, 5 / 10, 3 / 100, 0) | PASS | check_B_04_2.py |
| 11 | "a fixed spread of shares across the ions lowers the scatter a little" | PASS | check_B_04_2.py: $\sum p_i(1-p_i) - N\bar p(1-\bar p) \le -0.054$ (never positive) over 2000 random static spreads |
| 12 | "field noise that changes from run to run would raise it" | PASS | check_B_04_2.py: Monte Carlo, N = 100, Rabi-angle jitter shared by the ions: var 31.0 and 49.4 against binomial 25.0; matches $N\langle p(1-p)\rangle + N^2\mathrm{Var}(p)$ |
| 13 | "amplitude ... up has size $\sin(\Omega t/2)$ and for down $\cos(\Omega t/2)$"; "$\sin^2(\Omega t/2)$"; length or detuning sets any p | PASS | check_B_05_2.py: sympy propagator gives (cos, -i sin); a detuning scan at fixed pi pulse covers p from 4e-11 to 1 |
| 14 | "error bars of size $\sqrt{p(1-p)/M}$" | PASS | check_B_04_2.py |
| 15 | Chebyshev chain "$D_\varepsilon(N) \le p(1-p)/(N\varepsilon^2)$" | PASS | check_B_06_2.py: each inequality checked numerically for 9 (N, p) pairs; $\sum w_m(m/N-p)^2 = p(1-p)/N$ |
| 16 | Deviant table: 100/N, 36/N; $2e^{-2N\varepsilon^2}$ = 1.21, 0.0135, 3.9e-22, "below $10^{-2000}$" | PASS | check_B_06_2.py: 1.2131, 0.013476, 3.857e-22, $10^{-2171}$; the exact tail never exceeds any bound |
| 17 | "exponential bound is weaker than Chebyshev's at N = 100" | PASS | check_B_06_2.py: 1.21 > 1 (p = 1/2) and > 0.36 (p = 0.1) |
| 18 | "between N = 400 and 500 at p = 1/2, between 700 and 800 at p = 0.1" | PASS | check_B_06_2.py: among informative values (Chebyshev < 1), Hoeffding first drops below Chebyshev at N = 431 (p = 1/2) and N = 745 (p = 0.1), and stays below for larger N |
| 19 | "exact value at N = 1000 and p = 1/2 is about 0.0014"; "the exact value fastest" | PASS | check_B_06_2.py: 0.001392; the exact/Hoeffding ratio falls from 0.10 to 0.033 |
| 20 | Overlap of product lists "$(c_0c_0' + c_1c_1')^N$" | PASS | check_B_07_2.py: explicit lists for N = 1, 2, 3, 5 |
| 21 | "p = 0.100 against p = 0.111, about 1° apart"; "0.9998477"; "$e^{-15.23} \approx 2.4\times10^{-7}$" | PASS | check_B_07_2.py: 1.026°, cos 1° = 0.9998477, exponent -15.232, value 2.43e-7 |
| 22 | q-size ratio $(N-m)/(m+1)\cdot(c_1/c_0)^q$; $f_q$; table 0.25, 0.10, 0.0357, 0.0122; $1.2649^N$, 1, $0.8854^N$, $0.82^N$ | PASS | check_B_08_2.py: sympy ratio; the q-size peak at N = 2000 sits at $f_q$ (within 1/N); table values match |
| 23 | "Only q = 2 delivers p"; equal amplitudes, "every q gives 1/2" | PASS | check_B_08_2.py: a q scan over [0.5, 6] for p = 0.05, 0.1, 0.3, 0.7 finds only q = 2 |
| 24 | "only the 2-norm is kept fixed by linear maps that move amplitude ... a little at a time" | PASS | check_B_08_2.py: a small rotation keeps the 2-size and changes the 1- and 3-sizes. This is a numerical illustration; the general theorem is the cited Banach–Lamperti result |
| 25 | Many-worlds N = 4 table; "Eleven of the sixteen branches, 69% ... weight 0.0523" | PASS | check_B_09_2.py: 11/16 = 68.75%, weight 0.0523 |
| 26 | "N = 20 the most numerous branches have fraction 1/2 ... most weight ... 0.1" | PASS | check_B_09_2.py: argmax C(20,m) at m = 10; argmax w_m at m = 2 |
| 27 | Everett: additive weight on merging "must be the squared entry" | PASS | check_B_09_2.py: $f(\sqrt{a^2+b^2}) = f(a)+f(b)$ holds for $x^q$ only at q = 2 |
| 28 | Coin/list table lines 2–6: mean p, variance p(1-p)/N, same Chebyshev bound | PASS | check_B_01_2.py, check_B_04_2.py, check_B_06_2.py |
| 29 | Caption numbers: opening minima 0.045, 0.009, 0.0009; N = 4 bars "0.0036 at 3/4 and 0.0001 at 1", spreads 0.25 and 0.15; maxima 0.158, 0.050, 0.0158 | PASS | check_B_10_2.py, check_B_04_2.py |
| 30 | b-model-2 caption: spreads 0.095, 0.030, 0.009; beyond m/N = 0.5 "the largest value, for N = 10, is N × w_6 = 0.0014" | PASS | check_B_10_2.py: 0.00138. The largest values beyond 0.5 for N = 100 and 1000 are 6e-23 and below |
| 31 | b-how-they-relate caption: 0.25, 0.10, 0.036, 0.012; "all q agree at p = 0, 1/2 and 1" | PASS | check_B_10_2.py |
| 32 | Check-yourself answer is well posed (N = 2, $c_1 = 1/\sqrt2$) | PASS | check_B_10_2.py: $\Psi_2$ = (1/2, 1/2, 1/2, 1/2), readings (0, 1/2, 1/2, 1), λ = 1/2, shortest squared length 1/8 |

Pass count: 32/32.

## Figures
All seven figures were reused from round 1. I viewed each PNG against its new caption, and none needed redrawing.
- b-opening: figures/b-opening.png. It matches the caption: the minima 0.045, 0.009 and 0.0009 are in the legend, and the log–log panel shows 1/N.
- b-projection-noise: figures/b-projection-noise.png. It matches the caption, including the flat grey line at zero for the fixed-share picture.
- b-what-this-rules-out: figures/b-what-this-rules-out.png. It matches the caption: the dashed line is labelled "true height 1, off scale". The p = 0.1 window ends at 30, where the cut-off tail is below 1e-8.
- b-counter-readings: figures/b-counter-readings.png. It matches the caption, and the bars at 0.75 and 1 are labelled.
- b-model-2: figures/b-model-2.png. It matches the caption. The window is 0–0.5, as the caption now states.
- b-model-3: figures/b-model-3.png. It matches the caption.
- b-how-they-relate: figures/b-how-they-relate.png. It matches the caption.

## Notes
- The round-1 FAIL ("sharper" Hoeffding label) is fixed, and the new crossover ranges are correct. For very small N (N ≤ 71 at p = 1/2, N ≤ 19 at p = 0.1), Hoeffding is numerically below Chebyshev, but both exceed 1 there. The phrase "overtakes it only from a few hundred ions on" is true for every informative bound.
- "Field noise ... would raise it" holds for noise shared by the ions in a run (N ≥ 2). If the fluctuations were independent from ion to ion, the variance would stay at $N\bar p(1-\bar p)$ (checked: 25.18 vs 25.00). The text's "field noise" reads naturally as shared, so I marked it PASS.
- Attribution and conceptual claims (Squires, Caves–Schack, Gleason, Busch, DGZ, Goldstein–Struyve, Gisin, Itano's measured agreement) were not checked by computation and are not counted.
