VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "add to 2, and 2^2 = 4 units ... four times the hits of one slit" | PASS | checks/check_B_01.py: (1+1)^2/1^2 = 4; in the far-field model P2/P1 = 4cos^2(5πu) = 4 at every bright fringe (u→0 limit = 4). Also "+1 and -1 add to 0, 0^2 = 0" verified. |
| 2 | "Over the whole screen, two slits give twice the hits of one" | PASS | checks/check_B_02.py: compared to ONE slit open (the text's unit), as stated. ∫sinc^2 = 1, ∫4 sinc^2 cos^2(5πu) = 2 exactly (sympy; cross term ∫sinc^2 cos(10πu) = 0); numeric ratio on [-200,200] = 2.000000. Two-slit total equals the which-slit (no-interference) total, so "moves them out of the dark stripes into the bright ones" is correct. |
| 3 | "With only the left slit open, electrons do land there" / "Open both ... none" | PASS | checks/check_B_03.py: at dark-fringe centres u = 0.1...0.9, one-slit P = 0.97...0.012 (> 0), two-slit P ≈ 1e-31. |
| 4 | "one smooth hump, which is just the two one-slit patterns added" | PASS | checks/check_B_04.py: |ψL|^2+|ψR|^2 = 2 sinc^2(u) exactly, single maximum in central lobe, no cos^2 fringes; sum of non-negative terms cannot cancel. |
| 5 | "little arrows ... cancel when they point opposite ways" | PASS | checks/check_B_05.py: |1+e^{iθ}|^2 = 0 only at θ = π; ranges 0 to 4. |
| 6 | Figure spec: "sinc^2(u) cos^2(5πu) (slit separation five times the slit width)" | PASS | checks/check_B_06.py: Fraunhofer integral over two slits of width a, separation d = 5a, with u = a sinθ/λ, gives amplitude 2a sinc(u) cos(5πu). |

## Figures
- b-two-slit-buildup: figures/b-two-slit-buildup.png (script checks/fig_b-two-slit-buildup.py, rejection sampling, seed 12345). Panel 1 shows 50 scattered dots, panel 2 clear stripes, panel 3 a single smooth hump with the same overall spread.

## Notes
- The "twice over the whole screen" result is exact here, not approximate: the cross term is the Fourier transform of sinc^2 (a triangle of half-width 1) evaluated at d/a = 5, which is zero. It stays exactly zero for any real double slit in the far field because d ≥ a always.
- The comparison is stated correctly: "twice the hits of one [slit]", alongside "four times the hits of one slit" at a bright spot. Both use the same one-slit baseline; there is no inconsistency.
- In the figure, panels 2 and 3 are not the same 2x scale; each panel shows 5,000 dots, so panel 3 shows the shape only (as the spec asks), not relative brightness.
- Check-yourself (not graded): if half the electrons are randomly tagged, the screen shows the stripes on top of a smooth background, with fringe visibility about 1/2 (check_B_04.py prints ≈0.51 near the centre).
- Conceptual and historical statements (neutrons, molecules, atomic levels, transistors, quantum computers, decoherence of baseballs) were not computed; nothing there conflicts with standard physics.
