VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "(cosθ+sinθ)²/2 = ... = (1+sin 2θ)/2" | PASS | checks/check_C_01_2.py: sympy identity |
| 2 | "θ = 45° or 135° ... a sure bet at D/A" | PASS | check_C_01_2: solutions {π/4, 3π/4}, D chances 1 and 0; sweep of 2·10⁶ angles gives min gap 0.54 |
| 3 | "does not depend on the square ... D shadow ... 0 or ±1" | PASS | check_C_01_2: D shadow takes only {−1, 0, 1} |
| 4 | "QD = (1,i)/√2 = R", "QR = A", "QL = D" | PASS | checks/check_C_02_2.py: exact matrix products |
| 5 | "⟨H\|R⟩=1/√2, ⟨D\|R⟩=(1+i)/2, ⟨A\|R⟩=(1−i)/2, ⟨R\|R⟩=1, ⟨L\|R⟩=0" | PASS | check_C_02_2: all exact |
| 6 | 3×3 table "100/0 ... 50/50" (also the physical Q + 45° splitter R/L sorter) | PASS | check_C_02_2 |
| 7 | "The two exits of any sorter total 1 for every state" | PASS | check_C_02_2: symbolic for H/V, D/A, R/L |
| 8 | "\|s₁−is₂\|² = ... + i s₁s̄₂ − i s̄₁s₂", "\|s₁+is₂\|² = ... − i s₁s̄₂ + i s̄₁s₂"; cross terms cancel | PASS | checks/check_C_03_2.py: both expansions match as written (fixed since round 1), half-sum = \|s₁\|²+\|s₂\|²; ⟨R\|s⟩, ⟨L\|s⟩ as written |
| 9 | "i(x+iy) = −y+ix sends (x,y) to (−y,x)" | PASS | check_C_02_2 |
| 10 | quarter-period delay "multiplies the V component by i" (convention noted) | PASS | checks/check_C_13_2.py: e^{−iω(t−T/4)} = i·e^{−iωt}; −i in the other convention, as the text says |
| 11 | Sphere: real arrows on the H–D–V–A circle; even-bet circles cross only at R, L | PASS | checks/check_C_04_2.py: P = (1+S_k)/2 for 20 000 random states, real arrows have S₃ = 0 |
| 12 | "nine terms, each involving one slit or two"; "I₃ = 0 ... for any three hands" | PASS | checks/check_C_05_2.py: 9 terms, I₃ ≡ 0, and I₄ ≡ 0 too |
| 13 | Power table (p = 1…4; 1.17, −1.66, −12, 36, ...) | PASS | checks/check_C_06_2.py: all 12 entries |
| 14 | "plain size passes at a few special spots": aligned hands and (1,ω,ω²), "I₃ = 0 − 3 + 3 = 0"; "never negative (Hlawka)" | PASS | checks/check_C_07_2.py: the pair sums of (1,ω,ω²) have length 1 and P_ABC = 0. On the screen model for \|x\| ≤ 12 the only zeros of the p=1 leftover are at integers and at thirds (minimum ≥ 0.0079 elsewhere). Random-hand minimum is +5e−7 |
| 15 | "cube and fourth power fail even at the centre"; p=4 products "in which all three hands appear" | PASS | check_C_07_2: 6 and 36; the symbolic p=4 I₃ contains a·ā·b·c̄ terms |
| 16 | Sorkin: "degree p has interference up to order p" | PASS | check_C_07_2: for p=4, I₄ = −12.1 and I₅ = 6e−14 |
| 17 | "N single terms plus N(N−1)/2 pair terms" | PASS | check_C_07_2: N = 3, 4, 5 |
| 18 | Wiggle rule: "f(x)+f(y) = 1 for every θ", f(0)=0, f(1)=1, f(1/√2)=½, "(1−x²)(2x²−1) between −1 and 1/8", f ≥ 0; "1/3 − 2ε/27", "1 − 2ε/9" | PASS | checks/check_C_09_2.py |
| 19 | "f(cos 30°) ... 0.75 + 0.094 ε"; agrees with the square at 0, 1/√2, 1 | PASS | checks/check_C_10_2.py: 3/4 + 3ε/32 (0.09375ε). On [0,1], f = x² only at {0, 1/√2, 1} |
| 20 | Classical wave: detectors "click together at least as often as independent random clicks" | PASS | checks/check_C_16_2.py: α ≥ 1 for 2000 random classical pulse statistics (min 1.19) |
| 21 | Mixture lean "q(1,0,0) + (1−q)(0,0,1)", inside the sphere; pure lean length 1; three leans fix everything | PASS | checks/check_C_15_2.py: ρ = (I + L·σ)/2 rebuilt exactly from the three leans |
| 22 | Quaternions "up to five mutually even-bet sorters" for two exits | PASS | check_C_15_2: 5 anticommuting quaternionic Pauli-type matrices with mutual chances ½. The traceless space has dimension 5 |
| 23 | Wootters count 3, 2, 15 = 3+3+9, 9, 8 = 2+2+4; "4 + 12 = 16", "10" | PASS | checks/check_C_11_2.py: ranks of the operator spans |
| 24 | "6√2 ≈ 8.49" | PASS | check_C_11_2: 8.4853 |
| 25 | Real-QM network bound "at most 7.66" | UNVERIFIABLE | literature value (Renou et al. 2021); the text itself says it is not checkable by hand |
| 26 | Zurek swaps restore "the original state again"; √(2/3), √(1/3) → "2/3 and 1/3" | PASS | checks/check_C_12_2.py: the three sub-branch hands are 1/√3 |
| 27 | Pilot-wave: \|ψ\|² stays so; "\|ψ\| or \|ψ\|⁴ does not in general" | PASS | checks/check_C_14_2.py: two-packet free state, continuity residual 3e−6 (p=2) vs 1.3–4.4 (p=1) and 0.4–0.5 (p=4). For a single Gaussian \|ψ\|⁴ is also kept, so the "in general" is needed |
| 28 | Beth: "per photon of energy hf ... angular momentum ħ" | PASS | check_C_13_2: E/ω = ħ (CODATA) |
| 29 | Grangier et al.: "about a fifth of the independent-click rate" | UNVERIFIABLE | literature value (α ≈ 0.18 in the 1986 paper), not recomputed |
| 30 | Fig c-three-slit-patterns caption: "a weak stripe (about 0.95) between neighbouring tall stripes" | FAIL | checks/check_C_08_2.py: in the plotted window the weak stripes are 0.95 (at ±0.5), 0.62 (±1.5) and 0.22 (±2.5). The figure itself shows this. Correct statement: "Bottom: all three open reaches 9 at the centre; between neighbouring tall stripes there is a weak stripe (about 0.95 next to the centre, smaller further out) with zeros a third and two thirds of the way between them; ..." (the rest of the caption can stay) |
| 31 | Fig c-three-slit-patterns caption, the rest: singles coincide; A+B = B+C, stripes 1 and ½ apart; 4 and 9 at the centre; envelope zero at ±4 with fainter side bands beyond; tall stripes at ±3 ≈ 0.8 < weak stripe at ±½ | PASS | check_C_08_2: the zeros are exact. ABC at ±3 = 0.81 (peak 0.85 at ±2.96). Single-slit side band 0.047 at x ≈ 5.7 |
| 32 | Fig c-three-slit-leftover caption: only p=2 zero; p=1 ≥ 0 with zeros only at stripe centres and 1/3, 2/3; p=3, 4 change sign, 6 and 36 | PASS | check_C_08_2 and check_C_07_2 (zeros checked over \|x\| ≤ 12; envelope zeros at multiples of 4 are integers, so already counted) |
| 33 | Check yourself: no pure state is 50/50 at all three; unpolarized at the centre | PASS | check_C_04_2, check_C_15_2: pure states have \|lean\| = 1; I/2 gives a lean of (0,0,0) and ½ at every sorter |

Pass count: 30/33 (1 FAIL, 2 UNVERIFIABLE).

## Figures
- c-sorter-table: figures/c-sorter-table.png (reused, matches caption)
- c-three-fifty-fifty: figures/c-three-fifty-fifty.png (reused, matches caption)
- c-quarter-wave-hands: figures/c-quarter-wave-hands.png (reused, matches caption)
- c-three-slit-patterns: figures/c-three-slit-patterns.png (reused; the plot is correct, the caption needs the row-30 fix; not widened, because the caption explicitly describes a window inside the central band, −3..3)
- c-three-slit-leftover: figures/c-three-slit-leftover.png (reused, matches the new caption, circles at integers and thirds)
- c-wiggle-rule: figures/c-wiggle-rule.png (reused, matches caption)
- c-swap-step: figures/c-swap-step.png (reused, matches caption)
- c-map: figures/c-map.png (reused, matches caption)

## Notes
- The three round-1 FAILs (cross-term signs, the p=1 "fails elsewhere" wording, the wiggle rule vs Malus) are fixed and now PASS (rows 8, 14, 19).
- Row 14: for general hands the p=1 leftover is also zero whenever the three hands sum to zero (equal or not) or one hand is zero. On the three-slit screen that only happens at the spots the text names, so the statement is true as written.
- Literature values not checked: the 7.66 bound, Grangier's α, Sinha's ~1% bound, the Kauten/Cotter results, Sawant 2014 and the Magaña-Loaiza 2016 leftover.
