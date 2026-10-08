VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | "seven bright stripes under the central envelope and faint ones beyond it" (a-buildup spec) | PASS | checks/check_A_01.py: P(u)=sinc²(u)cos²(4πu) has 7 bright maxima at u=0, ±0.245, ±0.488, ±0.725 (heights 1, 0.81, 0.42, 0.10); the order at u=±1 is missing; beyond it, faint peaks at ±1.26 and ±1.5 (0.033, 0.045) |
| 2 | "one slit open, electrons land there often ... none land there at all"; figure: "curve (1) is about 0.95 there while curve (3) is 0" | PASS | checks/check_A_02.py: S(1/8)=0.9496, 4S·cos²(π/2)=0 exactly; u=0.125 is the first zero of cos(4πu) |
| 3 | "peaks reach twice curve (2)" | PASS | checks/check_A_02.py: 4S/(2S)=2 where cos²=1 |
| 4 | "A second way through made arriving less likely ... impossible if the chances ... simply add" | PASS | checks/check_A_02.py: with chances added, the result is p1+p2 ≥ p1 (both nonnegative), but with amplitudes added it drops from 0.95 to 0 |
| 5 | "add the amplitudes ... chance ... is the size of the total, squared" plus equal routes give bright, half a wavelength gives dark, a whole wavelength gives bright again | PASS | checks/check_A_03.py: \|a+a·e^{2πiΔL/λ}\|² = 4a²cos²(πΔL/λ), equal to 4a², 0 and 4a² at ΔL=0, λ/2 and λ; figure model phase 8πu equals π at u=1/8 (half-wave) |
| 6 | "Routes that can be told apart add their chances, not their amplitudes" | PASS | checks/check_A_04.py: with orthogonal marker states, P = \|ψ1\|²+\|ψ2\|² exactly (difference 0.0) |
| 7 | "records far too gentle for that erase the stripes too" | PASS (model) | checks/check_A_04.py: a which-path marker that leaves the spatial amplitudes untouched (no momentum kick) gives fringe visibility 1.0, 0.52 and 0.03 for marker overlap 1, 0.5 and 0. Visibility depends only on the overlap (the record), not on any disturbance |
| 8 | "wavelength is a tiny length that shrinks as its momentum ... grows" | PASS | checks/check_A_05.py: λ=h/p for electrons is 0.39 nm, 0.12 nm, 39 pm and 5.4 pm at 10 eV, 100 eV, 1 keV and 50 keV, so it decreases monotonically |
| 9 | Everyday objects: "wavelengths far smaller than an atomic nucleus" | PASS | checks/check_A_05.py: 1 g at 1 m/s gives 6.6e-31 m, a baseball 1.1e-34 m, a person 6.8e-36 m, all at least 10^16 times smaller than a 10 fm nucleus |
| 10 | "molecules of 60 carbon atoms" show stripes | UNVERIFIABLE (historical fact) | checks/check_A_05.py only computes λ(C60, 200 m/s)=2.8 pm, which is consistent with Arndt et al. 1999. The experiment itself is not checkable by computation |
| 11 | Atom: "only certain steady patterns fit, each with one fixed energy"; "lowest pattern with nothing below it" | PASS | checks/check_A_06.py: finite-difference hydrogen (l=0) gives discrete levels -13.604, -3.401, -1.512 ... eV, matching -13.606/n² to within 0.01%. The spectrum has a minimum (ground state) |
| 12 | "color fixed by the energy difference ... sharp colors" | PASS | checks/check_A_06.py: H 3→2 ΔE=1.889 eV → 656.47 nm (H-alpha, red); 4→2 486.27 nm; 5→2 434.17 nm |
| 13 | "a wave squeezed into a small region must combine many wavelengths" → momentum spread | PASS | checks/check_A_07.py: Gaussian packets with σx = 4, 1, 0.25 give σk = 0.125, 0.5, 2.0 by FFT; σxσk = 0.5000 each time |
| 14 | Check yourself: covering one slit at a central dark stripe | PASS (consistent) | checks/check_A_02.py: the intended answer, more hits (0 → 0.95 relative units), follows from the text's numbers |

Pass count: 13 PASS, 0 FAIL, 1 UNVERIFIABLE (14 claims).

## Figures
- a-buildup: figures/a-buildup.png (checks/fig_a-buildup.py; inverse-CDF sampling from the specified P(u), N = 10/100/1000/10000, seed 1)
- a-compare: figures/a-compare.png (checks/fig_a-compare.py; three curves told apart by line style as well as color, dashed line at u=0.125, markers at 0.95 and 0)

## Notes
- a-buildup spec: besides the 7 bright stripes, the product also has two tiny sub-peaks at u≈±0.93 (0.2% of the central maximum) on either side of the missing order at u=±1. They are invisible in the figure and don't contradict "seven bright stripes".
- The "faint ones beyond it" (heights 0.03–0.045) are about a third as tall as the outermost bright stripe (0.10), so they are faint but visible at N=10000.
- Claim 7 is verified only as a model (an internal-state marker with zero momentum transfer). That gentle markers erase fringes in real experiments (e.g. Dürr, Nonn, Rempe 1998) is an empirical fact, not something computation can establish.
- "Tiny length" for electrons: at slow lab energies (10–100 eV) λ is about 0.1–0.4 nm, which is atom-sized rather than far smaller. The wording is fine for a conceptual reader.
