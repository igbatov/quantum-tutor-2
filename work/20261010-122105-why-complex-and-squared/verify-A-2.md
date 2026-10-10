VERDICT: revise

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "Multiplying by $e^{i\varphi}$ turns a hand by $\varphi$ without changing its length" (expanded algebra) | PASS | checks/check_A_01.py (re-run): product expansion, middle line and $x^2+y^2$ checked symbolically |
| 2 | "Check that $H$ keeps the total chance"; "$H$ is a reflection"; sign-free matrix sends $(1,-1)/\sqrt2$ to $(0,0)$ | PASS | checks/check_A_02.py (re-run) |
| 3 | "Losslessness forces *some* relative turn ... the $i$ convention shifts it by $\pi$" | PASS | checks/check_A_20.py: unitary exactly when the phase sum is $\pi$, and $\frac1{\sqrt2}\begin{pmatrix}1&i\\i&1\end{pmatrix}$ is lossless with no $-1$; checks/check_A_04_2.py: with it, exit 1 gets $\tfrac12-\tfrac12\cos\varphi=\cos^2\frac{\varphi+\pi}{2}$. (Round-1 FAIL is fixed.) |
| 4 | "$H(z,1)/\sqrt2=\tfrac12(z+1,z-1)$", $P_1=\cos^2\frac\varphi2$, $P_2=\sin^2\frac\varphi2$, $PH$, $U=HPH$ | PASS | checks/check_A_03.py (re-run), symbolic |
| 5 | Period one wavelength ($2\pi$); extra-path tick labels | PASS | checks/check_A_03.py |
| 6 | Model 1 table, rows 0° to 180° | PASS | checks/check_A_04.py: all entries within 3-decimal rounding |
| 7 | (c) "100 + 0, 75 + 25, 50 + 50, 25 + 75" | PASS | checks/check_A_04.py: $P_1$ at 0°, 60°, 90°, 120° |
| 8 | (d) arm-1 counter "counts half"; arm 2 blocked, "one quarter" each, independent of tilt | PASS | checks/check_A_05.py: at 97 values of $\varphi$ |
| 9 | Rules-out rows: balls 50/50; chances only "¼ + ¼ = ½ ... at $\varphi=\pi$ it gets nothing" | PASS | checks/check_A_05.py |
| 10 | "$r^2=1$ and $r=+1$ or $-1$", giving 100/0 or 0/100 | PASS | checks/check_A_06.py |
| 11 | Loss in arm 1: exit 1 "between $(1+\sqrt t)^2/4$ and $(1-\sqrt t)^2/4$", exits "sum to $(1+t)/2$"; minimum no longer zero | PASS | checks/check_A_03_2.py: $P_1=\tfrac14(1+t+2\sqrt t\cos\varphi)$, $P_2=\tfrac14(1+t-2\sqrt t\cos\varphi)$ symbolically; max/min at $\varphi=0,\pi$; sum $(1+t)/2$; minimum $>0$ for every $t<1$ (e.g. $2.1\times10^{-2}$ at $t=0.5$) |
| 12 | "98% visibility, which leaves a floor of about 1% of the peak" | PASS | checks/check_A_03_2.py: $(1-V)/(1+V)=0.0101$ |
| 13 | Classical wave "$\alpha$ is at least 1 (exactly 1 for a steady wave, higher for one whose intensity fluctuates)"; ideal single photon $\alpha=0$ | PASS | checks/check_A_06_2.py: steady 1.000, exponential 1.999, uniform 1.333 (Cauchy–Schwarz); Fock state $\lvert1\rangle$ gives 0 |
| 14 | Data: "$\alpha=0.18\pm0.06$", "visibility of 98%", "about 8.09, more than forty standard deviations above 7.66", "about 2000 atoms" | UNVERIFIABLE | checks/check_A_06_2.py, check_A_19.py: experimental values. They match the published values as I recall them, but I could not recompute them |
| 15 | Quaternion amplitudes "pass (a) to (d) just as well"; two plates "could give different counts in the two orders" | PASS | checks/check_A_07_2.py: a unit-quaternion plate gives $\cos^2$, total 1, arm count ½. Plates $AB$ vs $BA$ give exit-1 fractions 0.833 vs 0.383 when the reference arm carries a non-commuting quaternion phase (identical if the reference arm is real; "could" is correct) |
| 16 | 360° reverses the sign, 720° restores it; "counts oscillate smoothly with a period of 720°" | PASS | checks/check_A_09.py (re-run); checks/check_A_08_2.py: $I\propto\lvert1+e^{-i\theta/2}\rvert^2$ has period $4\pi$, not $2\pi$ |
| 17 | Model 2: "$\lvert A_1\rvert=\lvert A_2\rvert=\tfrac12$"; totals 1, 0.707, 0; squared 1, 0.50, 0 | PASS | checks/check_A_07.py (re-run) |
| 18 | $J(x,y)=(-y,x)$, $J^2=-1$; real $4\times4$ rewriting with $J$ is the same theory for one system | PASS | checks/check_A_08.py (re-run): chances agree to $7\times10^{-16}$ |
| 19 | "complex quantum mechanics allows up to $6\sqrt2\approx8.49$" | PASS | checks/check_A_10.py (re-run): explicit network gives 8.485281, and it is the maximum |
| 20 | "real-amplitude theories cannot exceed about 7.66" | UNVERIFIABLE | needs the NPA semidefinite hierarchy; consistent with the literature value 7.6605 |
| 21 | Banach–Lamperti at $2\times2$; "$\lvert a+b\rvert^p<\lvert a\rvert^p+\lvert b\rvert^p$" for $0<p<1$ so mixing loses $p$-total; $p=1$ with non-negative amplitudes allows gradual mixing but no cancelling | PASS | checks/check_A_11.py (re-run); checks/check_A_05_2.py: strict subadditivity on $10^5$ complex pairs for $p=0.2,0.5,0.9$; 6000 random mixing maps all lose $p$-total; stochastic matrices keep the 1-total, and two routes of ¼ still give ½ |
| 22 | $S_p$ table: $p$-total $2^{p-2}$; rows $p=1..4$; "$2\cdot(1/\sqrt2)^p=2^{1-p/2}$ (1.41, 1, 0.71, 0.5)" | PASS | checks/check_A_12.py (re-run) |
| 23 | Binomial step: "$\lvert\alpha+t\gamma\rvert^p=\lvert\alpha\rvert^p+p\lvert\alpha\rvert^{p-1}\mathrm{sgn}(\alpha)\gamma t+\tfrac{p(p-1)}2\lvert\alpha\rvert^{p-2}\gamma^2t^2+\dots$"; the stated $L$ and $Q$ | PASS | checks/check_A_01_2.py: sympy series matches the stated coefficients for $\alpha$ of both signs, two $\gamma$, $p\in\{\tfrac12,1,\tfrac32,2,3,\tfrac52,4\}$; numeric check that the expansion is $\lvert\alpha+t\gamma\rvert^p$ near 0 |
| 24 | $p<2$: "$\lvert t\rvert^p$ has a corner or a cusp at $t=0$ (... for $1<p<2$ its curvature is infinite there)" | FAIL | checks/check_A_01_2.py: for $1<p<2$, $\lvert t\rvert^p$ is differentiable at 0 with slope 0 (slope at $t=10^{-6}$: $1.5\times10^{-3}$ for $p=1.5$), so it has no corner or cusp; only its second derivative blows up ($750$ at $t=10^{-6}$, $p=1.5$). The conclusion is right, and the mixing devices really fail (smallest worst-case mismatch 0.57, 0.34, 0.11 for $p=0.5,1,1.5$). Correct statement: "$\lvert t\rvert^p$ is not smooth at $t=0$: for $p<1$ its slope is infinite there (a cusp), for $p=1$ its slope jumps (a corner), and for $1<p<2$ its curvature is infinite there. A series in whole powers of $t$ is smooth, so it cannot match." |
| 25 | $p>2$: "matching needs $L=0$ and $Q=0$ ... $Q=0$ forces $\gamma=\delta=0$" | PASS | checks/check_A_01_2.py: $Q$ is a positive multiple of a sum of non-negative terms, and its only real zero is $\gamma=\delta=0$. The numerical optimum over mixing devices still misses by 0.065 ($p=3$) and 0.070 ($p=4$) |
| 26 | $p=2$: "$Q=\gamma^2+\delta^2$ must equal 1 and $L$ must be 0 ... a rotation or a reflection" | PASS | checks/check_A_01_2.py: rotation keeps $1+t^2$ exactly; best mismatch over mixing devices $4\times10^{-16}$ |
| 27 | "both inputs landing on the same exit gives a term linear in $t$ ... so the two inputs must land on different exits" | PASS | checks/check_A_01_2.py: for real entries, $\lvert s_1+s_2t\rvert^p=1\pm pt+\dots$ with $s_{1,2}=\pm1$, while $1+\lvert t\rvert^p$ has no $t$ term (see Notes for complex entries) |
| 28 | "a rotation by 15° takes $(1,0)$ to $(0.966,0.259)$ ... 1.225 for $p=1$, exactly 1 for $p=2$ and 0.875 for $p=4$" | PASS | checks/check_A_02_2.py: exact values $\sqrt6/2=1.2247$, 1, $7/8$ |
| 29 | Wiggle rule: two-outcome sum is 1; $f\ge0$ for $\lvert\varepsilon\rvert<1$; three outcomes $1-\tfrac{2\varepsilon}9$; 0.889, "eleven per cent" | PASS | checks/check_A_13.py (re-run) |
| 30 | Renamed amplitudes reproduce counts "but renamed hands no longer add tip to tail" | PASS | checks/check_A_14.py (re-run) |
| 31 | Gleason: squared shadows consistent across groupings, "not the plain size, not a wiggle" | PASS | checks/check_A_15.py (re-run): square and mixed-state rules sum to 1 within $10^{-15}$; plain size off by up to 1.0, wiggle by 0.11 (uniqueness itself is cited) |
| 32 | Pilot wave: squared-length cloud stays so, plain-length cloud does not; real $\psi$ means the particle is at rest | PASS | checks/check_A_16.py (re-run) |
| 33 | Definite energy: hand turns at frequency $E/h$, squared length constant | PASS | checks/check_A_17.py (re-run) |
| 34 | Tilting the plate makes the optical path "grow smoothly" | PASS | checks/check_A_18.py (re-run) |
| 35 | Check yourself: arm 1 turned 90°, arm 2 turned 30°, input $(1,0)$ → exit-1 fraction 0.75 | PASS | checks/check_A_04_2.py: $P_1=3/4$, $P_2=1/4$ exactly (only the 60° difference matters) |
| 36 | Figure captions (all nine) match the drawn figures | PASS | Each PNG inspected against its caption. a-pnorm-circles: "sizes ... trace this same arc" (check_A_21.py, max deviation $3\times10^{-16}$). a-how-they-relate: 1.41 / 0.71 / 0.5 at $\pi/2$ (check_A_12.py). a-model-2: 1, 0.866, 0.707, 0.5, 0. a-interferometer-counts: circles at $0,\pi,2\pi,3\pi$ and the hands at top right, as drawn. a-rules-out: three boxed settings, 1.00 / 2.01 / 0 |

Pass count: 33 PASS, 1 FAIL, 2 UNVERIFIABLE (33/36).

## Figures
- a-setup: figures/a-setup.png (reused; caption matches)
- a-interferometer-counts: figures/a-interferometer-counts.png (reused; caption matches)
- a-rules-out: figures/a-rules-out.png (reused; caption matches)
- a-model-1: figures/a-model-1.png (reused; caption matches)
- a-model-2: figures/a-model-2.png (reused; caption matches)
- a-complex-meaning: figures/a-complex-meaning.png (reused; caption matches)
- a-pnorm-circles: figures/a-pnorm-circles.png (reused; the caption now matches the corrected arc label)
- a-interpretations: figures/a-interpretations.png (reused; caption matches)
- a-how-they-relate: figures/a-how-they-relate.png (reused; caption matches)

None were redrawn.

## Notes
- Row 24 is a wording fix only; the logic of the $p<2$ branch holds. A power series is smooth (infinitely differentiable), and $\lvert t\rvert^p$ is not, for every $p<2$ and also for non-even $p>2$, but the $p>2$ branch rightly uses the size comparison instead.
- "(complex entries go the same way)": this is true in substance, but the last step needs a small change. With complex entries, two inputs on the same exit, for example $(1,0)\to(1,0)$ and $(0,1)\to(i,0)$, give $\lvert1+it\rvert^p=(1+t^2)^{p/2}$, which has no linear term. Feeding $(1,-it)$ instead restores $1+pt+\dots$. If the explainer wants to be exact: "complex entries go the same way, after giving $t$ a suitable phase."
- Row 15: Peres's order test only shows up when the reference arm (or the splitters) carries a quaternion phase that does not commute with the plates. With a purely real reference arm, $\mathrm{Re}(AB)=\mathrm{Re}(BA)$ and both orders give the same counts. The text's "could" is accurate.
- Round-1 items 3 (sign-change wording), 25 (arc label) and the $0<p<1$ note are all resolved in this version.
