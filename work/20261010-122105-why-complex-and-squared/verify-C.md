VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "(cosθ+sinθ)²/2 = ... = (1+sin 2θ)/2" | PASS | checks/check_C_01.py: sympy identity holds |
| 2 | "θ = 45° or 135° ... a sure bet at D/A" | PASS | check_C_01: the solutions in [0,π) are {π/4, 3π/4}, and the D chances there are 1 and 0. A 2×10⁶-point sweep finds no θ that is even at both (min gap 0.54) |
| 3 | "does not depend on the square ... D shadow ... is 0 or ±1" | PASS | check_C_01: with \|cos\|=\|sin\|=1/√2 the D shadow takes only the values {−1, 0, 1} |
| 4 | "QD = (1,i)/√2 = R", "QR = A", "QL = D" | PASS | checks/check_C_02.py: exact sympy matrix products |
| 5 | "⟨H\|R⟩=1/√2, ⟨D\|R⟩=(1+i)/2, ⟨A\|R⟩=(1−i)/2, ⟨R\|R⟩=1, ⟨L\|R⟩=0" | PASS | check_C_02: all five overlaps exact |
| 6 | 3×3 table "100/0 ... 50/50" (and the A column in fig c-quarter-wave-hands) | PASS | check_C_02: the full table follows from Model 1. The physical R/L sorter (Q followed by a 45° splitter) gives the same rows, and A gives 50/50, 0/100, 50/50 |
| 7 | "The two exits of any sorter total 1 for every state" | PASS | check_C_02: symbolic, for H/V, D/A and R/L |
| 8 | "the cross terms −i s₁s̄₂ + i s̄₁s₂ and +i s₁s̄₂ − i s̄₁s₂ cancel" | FAIL | checks/check_C_03.py: the cross terms of \|s₁−is₂\|² are **+i s₁s̄₂ − i s̄₁s₂**, and those of \|s₁+is₂\|² are −i s₁s̄₂ + i s̄₁s₂. The two pairs are swapped in the text; the cancellation and the total of 1 are still correct. Correct statement: "the cross terms +i s₁s̄₂ − i s̄₁s₂ (from the first) and −i s₁s̄₂ + i s̄₁s₂ (from the second) cancel" |
| 9 | "i(x+iy) = −y+ix sends (x,y) to (−y,x)" | PASS | check_C_02 |
| 10 | "quarter-period delay ... is exactly the quarter turn" (V × i) | PASS | checks/check_C_13.py: e^{−iω(t−T/4)} = i·e^{−iωt}. This holds in the e^{−iωt} convention; in the other convention the factor is −i, and the text already notes that the handedness label is convention-dependent |
| 11 | Sphere: "real arrows fill one great circle"; "even-bet circles ... cross at R and L, off the real circle" | PASS | checks/check_C_04.py: P = (1+S_k)/2 for 20 000 random states, real arrows have S₃=0, and S₁=S₂=0 on the unit sphere gives (0,0,±1) = R, L. Every pure state has \|S\|=1, so no pure state is 50/50 at all three sorters (this supports the Check-yourself answer) |
| 12 | "\|a+b+c\|² = ... nine terms, each involving one slit or two"; "pairs − singles = P_ABC"; "I₃ = 0 ... for any three hands" | PASS | checks/check_C_05.py: sympy finds 9 terms with at most 2 slits each and I₃ ≡ 0. Also I₄ ≡ 0 for p=2 ("a sum over pairs") |
| 13 | Power table (p = 1…4 for hands (1,1,−1), (1,1,1), (1,i,−1)) | PASS | checks/check_C_06.py: all 12 I₃ entries match, including 1.17 and −1.66 |
| 14 | "The plain size passes where all hands line up ... and fails elsewhere" | FAIL | checks/check_C_07.py: p=1 also gives I₃ = 0 (to 1e−16) for three equal hands 120° apart, (1, ω, ω²). These are exactly the three-slit dark spots at 1/3 and 2/3 of a stripe spacing (also in check_C_08 and the leftover figure). Correct statement: "The plain size passes at a few special spots (where all hands line up, and where three equal hands cancel completely, as at the three-slit dark spots) and fails at most others" |
| 15 | "the cube and the fourth power fail even at the centre"; p=4 contains products "in which all three hands appear" | PASS | check_C_07: at (1,1,1) I₃ = 6 for p=3 and 36 for p=4. The symbolic p=4 I₃ contains terms such as a·ā·b·c̄ |
| 16 | Sorkin: "a rule of degree p has interference up to order p" | PASS | check_C_07: for p=4, I₄ = −10.6 ≠ 0 and I₅ = 1e−13 ≈ 0. For p=2, I₃ ≈ 0. Hlawka: p=1 I₃ ≥ 0 (min over 2·10⁵ random sets of hands is +5e−7) |
| 17 | Wiggle rule: "f(x)+f(y) = 1 for every θ"; "f(0)=0, f(1)=1, f ≥ 0"; "(1−x²)(2x²−1) between −1 and 1/8"; "f = 1/3 − 2ε/27", "total 1 − 2ε/9" | PASS | checks/check_C_09.py: all symbolic or numeric. f(1/√2)=1/2 (the curves cross there). Endpoint totals 0.822 and 1.178 |
| 18 | "with two exits a non-power rule survives everything the sorters measure, up to their error bars" | FAIL | checks/check_C_10.py: f matches cos² only at x² = 0, ½, 1 (the table's entries). A splitter at an intermediate angle (Malus's law) sees a difference of 0.094ε at 30° (0.077 max for ε=0.8), so the data bound ε rather than leave it free. Correct statement: "So with two exits, the rule that the two chances add to 1 cannot rule out a non-power rule: it gives totals of 1 and the same 100/50/50 table (only sorters at intermediate angles, Malus's law, would show it, and they only bound ε)" |
| 19 | Wootters count: 3, 2, 15 = 3+3+9, 9, 8 = 2+2+4 | PASS | checks/check_C_11.py: computed from the dimensions of the spans of the Hermitian / real-symmetric matrices and the rank of the local product operators. Y⊗Y is the parameter that local measurements cannot see in a real pair |
| 20 | "6√2 ≈ 8.49" | PASS | check_C_11: 8.4853 |
| 21 | Real-QM network bound "at most 7.66" | UNVERIFIABLE | literature value (Renou et al. 2021), not recomputed |
| 22 | Zurek swaps restore "the original state again"; unequal hands → "2/3 and 1/3" | PASS | checks/check_C_12.py: tensor-product computation; the three sub-branch hands are all 1/√3 |
| 23 | Beth: "per photon of energy hf ... angular momentum ħ" | PASS | check_C_13: E/ω = ħ (CODATA) |
| 24 | Fig c-three-slit-patterns spec: the singles coincide, A+B = B+C, stripes 1 and ½ unit apart, 4 and 9 at the centre, weak stripe ≈1, zeros at 1/3 and 2/3 | PASS | checks/check_C_08.py: the zeros are exact. The weak stripe near the centre is 0.95 high |
| 25 | Fig c-three-slit-leftover spec: p=2 ≡ 0, p=1 ≥ 0 with isolated zeros, p=3 and p=4 change sign, 6 and 36 at the centre | PASS | check_C_08: max\|I₃\| for p=2 is 6e−15. The p=1 minimum is −2e−16 |

Pass count: 21/25 (3 FAIL, 1 UNVERIFIABLE).

## Figures
- c-sorter-table: figures/c-sorter-table.png
- c-three-slit-patterns: figures/c-three-slit-patterns.png
- c-three-fifty-fifty: figures/c-three-fifty-fifty.png
- c-quarter-wave-hands: figures/c-quarter-wave-hands.png (H and V hands shown in separate complex planes, so that D's two identical hands do not overlap)
- c-three-slit-leftover: figures/c-three-slit-leftover.png (the p=1 zeros are marked; they include the 1/3 and 2/3 dark spots, see row 14)
- c-wiggle-rule: figures/c-wiggle-rule.png
- c-swap-step: figures/c-swap-step.png (frames computed from the actual state vectors)
- c-map: figures/c-map.png

## Notes
- Row 14 also matters for the leftover figure: the p=1 curve touches zero at each tall stripe *and* at the two dark spots between them. The spec's wording "zero only at isolated points" is still true.
- In the patterns figure with d = 4w, the sinc envelope makes the outer "tall" stripes near x = ±3 (≈0.8) lower than the central weak stripe (0.95). The spec says "near the centre", so it is fine, but the text should not call all integer-x stripes "tall".
- The pair stripe peaks are pulled slightly by the envelope (A+B spacing 0.95–0.98). The zeros are exactly 1 apart (A+B) and ½ apart (A+C).
- These literature numbers were not checked: Sinha et al.'s ~1% bound, the Kauten/Cotter results, Beth's half-wave-plate set-up, Grangier et al., and the 2016 Magaña-Loaiza leftover.
- Check-yourself: check_C_04 confirms that no pure state is 50/50 at all three sorters. The "unpolarized light" half needs mixed states (the inside of the sphere), which the text does not set up.
