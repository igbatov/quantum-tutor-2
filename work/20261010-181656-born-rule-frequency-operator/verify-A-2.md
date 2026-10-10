VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "after 100 photons ... about 4 percentage points ... 10 000 by about 0.4"; scatter table 0.433 ... 0.00043 | PASS | checks/check_A_01_2.py: sqrt(0.1875/N) = 0.4330, 0.2165, 0.0433, 0.00433, 0.000433 |
| 2 | "For θ = 30° that is 0.75 and 0.25" | PASS | checks/check_A_01_2.py: exact |
| 3 | "differs from run to run by an amount that shrinks as 1/√N" | PASS | checks/check_A_01_2.py: Monte Carlo sd 0.04332 (N=100), 0.004325 (N=10⁴) |
| 4 | "a classical wave ... gives at least 1" | PASS | checks/check_A_02_2.py: α = 1.00 steady, 2.00 thermal, 1.33, 4.34; never below 1 |
| 5 | Grangier, Roger, Aspect "0.18 ± 0.06" | UNVERIFIABLE | literature value; below the classical floor of 1 |
| 6 | Thorn et al. (2004) "found about 0.02" | UNVERIFIABLE | literature value (they report about 0.018); consistent with the wording |
| 7 | "when the two amplitudes are equal in size, every exponent gives ½" | PASS | checks/check_A_03_2.py, check_A_13_2.py |
| 8 | Model 1: binomial mean Np, sd sqrt(Np(1−p)) | PASS | checks/check_A_06_2.py, check_A_01_2.py |
| 9 | N = 1, 2, 3 table (0.866/0.5; 0.75, 0.433, 0.25; 0.650, 0.375, 0.217, 0.125; squares 0.422, 0.141, 0.047, 0.0156) | PASS | checks/check_A_04_2.py |
| 10 | "In each row the squared sizes total 1"; Σ w_m = 1 | PASS | checks/check_A_04_2.py |
| 11 | readings are multiples of 1/N; N=2 diagonal 0, ½, ½, 1; "0.1 is not among them" | PASS | checks/check_A_05_2.py |
| 12 | "Ψ_N is not a sure-bet list at any finite N" | PASS | checks/check_A_05_2.py |
| 13 | F_N = (1/N)ΣP⁽ᵏ⁾, P⁽ᵏ⁾P⁽ᵏ⁾ = P⁽ᵏ⁾, ⟨P⁽ʲ⁾P⁽ᵏ⁾⟩ = p² | PASS | checks/check_A_05_2.py, check_A_06_2.py |
| 14 | "‖(F_N − λ)Ψ_N‖² = (λ − p)² + p(1−p)/N" | PASS | checks/check_A_06_2.py: sympy identity N = 1..8 |
| 15 | "24/256 = 3/32 = 0.09375"; "10/64 = 0.156" = 5/32; "1/8 at N = 2" | PASS | checks/check_A_06_2.py |
| 16 | bound "75/N: above 1 ... for N < 75; 0.075, 0.0075, 7.5×10⁻⁵" | PASS | checks/check_A_07_2.py, check_A_12_2.py (bound ≤ 1 from N = 75) |
| 17 | exact deviant "2.3×10⁻⁴ at N = 10³ and 4.8×10⁻³⁰ at 10⁴", falls exponentially | PASS | checks/check_A_07_2.py: 2.28×10⁻⁴, 4.79×10⁻³⁰; rate −ln(dev)/N → 0.0064 |
| 18 | "at no finite N is the deviant part zero (all-R ... p^N > 0)" | PASS | checks/check_A_07_2.py |
| 19 | "cos 1° = 0.99985 ... (cos 1°)^(10⁵) = e^(−15.2) ≈ 2.4×10⁻⁷" | PASS | checks/check_A_08_2.py: −15.23, 2.43×10⁻⁷ (wording now uses unrounded cos 1°) |
| 20 | f_q table 0.366, 0.250, 0.161, 0.100; totals 1.366^N, 1, 0.775^N, 0.625^N | PASS | checks/check_A_03_2.py, including numeric peak at N = 2×10⁵ |
| 21 | ratio v_{m+1}/v_m formula | PASS | checks/check_A_03_2.py: sympy |
| 22 | totals equal 1 "only at q = 2" | PASS | checks/check_A_03_2.py |
| 23 | "Only for the 2-norm ... continuous ... changes that mix" | PASS | checks/check_A_10_2.py: under rotation the q-norm varies by 0.41, 0.12, 0.11, 0.16 for q = 1, 1.5, 3, 4, and by 10⁻¹⁶ at q = 2 (2D real rotations; the general claim is the cited theorem) |
| 24 | N = 4, p = 0.9: "0.0001 + 0.0036 + 0.0486 = 0.0523"; 0.2916; 0.6561; "11 of the 16 ... 0.6875" | PASS | checks/check_A_09_2.py |
| 25 | "By number of strings, for large N most ... near ½ whatever p is" | PASS | checks/check_A_09_2.py: by count 0.73 (N=100), 0.9986 (N=1000) within 0.05 of ½ |
| 26 | Fig a-overview caption: minimum at λ = 0.25, depths "0.094, 0.019, 0.0019" | PASS | checks/check_A_13_2.py: 0.09375, 0.01875, 0.001875 |
| 27 | Fig a-experiment-1 caption: 0.75/0.25, band ±sqrt(p(1−p)/N), "axis is cut at about 0.7" | PASS | checks/check_A_01_2.py; fig script sets ylim 0 to 0.75 |
| 28 | Fig a-experiment-2 caption: curves through (0,0), (½,½), (1,1); "0.37, 0.25, 0.16 and 0.10"; only q = 2 diagonal | PASS | checks/check_A_13_2.py: 0.366, 0.250, 0.161, 0.100; q ≠ 2 deviate from diagonal by > 0.05 |
| 29 | Fig a-model-1 caption: sd 0.043; "window 0.05 to 0.50 leaves out ... below one in a million" | PASS | checks/check_A_13_2.py: excluded mass 3.9×10⁻⁸ |
| 30 | Fig a-weights-concentrate caption: "weight only 0.42"; spreads 0.217, 0.108, 0.054, 0.027 | PASS | checks/check_A_12_2.py: 0.4219; 0.2165, 0.1083, 0.0541, 0.0271 |
| 31 | Fig a-deviant-length caption (revised): bounds exceed 1 below N = 75 and 19; exact curves zigzag; "10⁻²⁸⁰ and 10⁻¹⁰⁷⁷ at N = 10⁵"; never zero | PASS | checks/check_A_12_2.py: bound ≤ 1 from N = 75 and 19; 272 and 253 upward steps for N in 10..400; log₁₀ = −280.0 and −1077.2 at N = 10⁵. The round-one FAIL is fixed |
| 32 | Fig a-model-3 caption: "0.656 and 0.292"; 11 of 16; N = 100 peaks 0.9 and 0.5, "barely overlap" | PASS | checks/check_A_13_2.py: overlap Σ min(weight, count) = 2.1×10⁻⁶ |
| 33 | Fig a-how-they-relate caption: 1-norm "1.41 at 45°", 3- and 4-norms "0.89 and 0.84"; all 1 at 90° and 180° | PASS | checks/check_A_13_2.py: 1.414, 0.891, 0.841; 1 at 90° and 180° |
| 34 | Check yourself: p = ¾, N = 300 | PASS | checks/check_A_11_2.py: 0.025; halving needs N = 1200 |
| 35 | Born 1926: main text "determines", footnote added in proof "proportional to the square" | UNVERIFIABLE | historical; the revised wording matches the paper as I recall it |

Pass count: 32 PASS, 0 FAIL, 3 UNVERIFIABLE (35 claims).

## Figures
All reused from round one; every caption in final-A.md now matches its figure and script, so I did not redraw any:
- a-overview: figures/a-overview.png
- a-experiment-1: figures/a-experiment-1.png
- a-experiment-2: figures/a-experiment-2.png
- a-classical-candidates: figures/a-classical-candidates.png
- a-model-1: figures/a-model-1.png
- a-weights-concentrate: figures/a-weights-concentrate.png
- a-deviant-length: figures/a-deviant-length.png (zigzag labelled; axis cut at 10⁻³⁰, as the caption says)
- a-model-3: figures/a-model-3.png
- a-how-they-relate: figures/a-how-they-relate.png

## Notes
- The round-one issues are all fixed: the deviant-length caption, the cos 1° rounding, the Born wording, and "Goldstein".
- Row 23 is computed only for real 2D rotations; the general statement rests on the Banach–Lamperti theorem.
