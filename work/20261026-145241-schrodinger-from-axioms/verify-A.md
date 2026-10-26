VERDICT: ship

| # | Claim (short quote) | Result | Evidence |
|---|---|---|---|
| 1 | Step 1: "dU/dt = A U(t)", A = U'(0) | PASS | checks/check_a-01.py: random 4x4 Hermitian H; finite-difference dU/dt equals U'(0)U(t) within 1e-6 |
| 2 | Step 2: "A^dag + A = 0", H = iħA Hermitian, plus the converse | PASS | check_a-01: max|A+A^dag| = 4e-16; d/dt(U^dag U) = U^dag(A^dag+A)U = 0; a non-anti-Hermitian generator breaks U^dag U = 1 |
| 3 | Step 3: "U(t)=e^{-iHt/ħ}", unique; e^{iHt/ħ}V(t)=1 | PASS | check_a-01: RK4 solution of dV/dt=-(i/ħ)HV agrees with expm to 5e-15; U(s)U(t)=U(s+t), U(0)=1 |
| 4 | "H|E> = E|E> gives e^{-iEt/ħ}|E>" | PASS | check_a-01: eigenvector test |
| 5 | Step 4 theta formula (matching exponents) | PASS | checks/check_a-02.py: sympy, exponents identical for arbitrary omega(k) |
| 6 | Step 5: "omega'(k) - omega'(k-u) = ħu/m", g constant | PASS | check_a-02: derivative identity checked symbolically |
| 7 | "omega = ħk²/2m + ck + omega0" is the unique consistent dispersion | PASS | check_a-02: polynomial ansatz up to degree 6 forces a2 = ħ/2m and a3..a6 = 0; relativistic sqrt(k²+m²) and k⁴-corrected dispersions give a k-dependent theta (d/dk = -0.42 and 7.9) |
| 8 | Completing the square; ck = "seen from a frame moving at -c" | PASS | check_a-02: identity holds; relabelling into a frame at velocity v without the phase gives c = -v |
| 9 | "the bracket is -mv²/2ħ" → theta = -(mvx' + ½mv²t')/ħ | PASS | check_a-02: bracket = mv(2c-v)/2ħ, so -mv²/2ħ at c=0. In 3D (check_a-04) the bracket is -m|v|²/2ħ, independent of k |
| 10 | Boosted psi satisfies the same free SE (G2) | PASS | check_a-02: exact free Gaussian packet; SE residual is 0 with the phase and nonzero without it |
| 11 | "ħω = ½ m v_g²", v_g = ħk/m | PASS | check_a-02 |
| 12 | -iħ∂x has eigenvalue ħk on e^{ikx}; "[K,P]=iħm" | PASS | checks/check_a-04.py: with K = mx - tP (sign is convention-dependent) |
| 13 | Lemma: preserving |psi|² pointwise ⇒ phase function | PASS (finite-dim test) | check_a-04: diagonal phases preserve; a permutation or a small off-diagonal mixing fails |
| 14 | "Real V keeps H Hermitian" | PASS | check_a-04: finite-difference H; complex V breaks Hermiticity |
| 15 | DG: 54 V, Ni, peak "near 50°" close to λ=h/p | PASS | checks/check_a-03.py: λ = 1.669 Å; Ni(111) surface rows d = 2.15 Å give a peak at 50.9°. Bragg planes (d = 0.91 Å) without refraction give a 47.0° scattering angle, so "quantitative once refraction is included" is fair |
| 16 | "λ ∝ 1/√V0"; "sin θ ∝ λ" | PASS | check_a-03 (non-relativistic; the correction at 54 eV is 3e-5) |
| 17 | "T = 10 µs (~2000 m/s over ~2 cm)" | PASS | check_a-03: 0.02/2000 = 1.0e-5 s |
| 18 | COW "about ±16 rad", "roughly five fringes" | PASS | check_a-03: Δφ(30°) = 15.56 rad; 4.95 fringes over -30°..30° (CODATA m_n, g = 9.8) |
| 19 | "ideal phase is ∝ m²" at fixed wavelength; units | PASS | check_a-03: d ln Δφ / d ln m = 2; m g Δz T/ħ is dimensionless |

19/19 PASS.

## Figures
- figures/a-cow-fringes.png. §1 Experiments (requested, line 13). Caption: "Left: the COW interferometer. The beam splits at A, one path runs Δz higher than the other, and the paths recombine at D. Right: model counts vs crystal tilt φ, phase Δφ = m g Δz₀ sin φ T/ħ with Δz₀ = 2 cm and T = 10 µs: ±15.6 rad at ±30°, about 5 fringes. A massless classical wave has no m in its phase, so it would give the flat dotted line."
- figures/a-classical-vs-quantum.png. §2 Classical candidates (extra). Caption: "Toy Davisson–Germer model. A wave scattered by Ni surface rows (d = 2.15 Å) peaks where d sin φ = h/p: 64° at 40 V, 51° at 54 V, 43° at 70 V. Classical particles give a broad spread that does not depend on the voltage (dotted)." The background level and peak widths are illustrative; only the peak positions are computed.
- figures/a-composition-group.png. §3 Model (extra). Caption: "Left: on an energy eigenstate, U(t) = e^{-iEt/ħ} is a rotation in the complex plane, so applying U(t) and then U(s) adds the angles, which is U(s)U(t) = U(s+t). Right: the real and imaginary parts oscillate while |U|² stays 1 (unitarity)."
- figures/a-boost-phase.png. §4 Galilean invariance (requested, line 79). Caption: "The same plane wave at t = 0 seen in the lab (k = 5) and from a frame moving at v = 2 (k' = 3), in units ħ = m = 1. |ψ|² = 1 in both frames. The wavelength changes from 2π/5 to 2π/3 only through the phase factor e^{-imvx/ħ}."
- figures/a-ledger.png. §5 Ledger (extra). Caption: "How the argument is built. Assumptions (dashed boxes) feed the theorems (grey boxes): Stone gives iħ∂tψ = Hψ, and the boost lemma plus Steps 4–5 give ω = ħk²/2m. Together these give the Schrödinger equation. The differentiability of U is assumed, not proved."

## Notes
- The COW figure uses illustrative numbers (Δz₀ = 2 cm, T = 10 µs). The 1975 apparatus enclosed a larger area and gave more fringes, so the caption should not present the 5 fringes as the historical data.
- In the real COW experiment, the intensity also varies with tilt because the crystal bends and because of the Sagnac term. "Tilt-independent for a massless classical wave" holds only in the ideal model, which the text already calls "ideal".
- Step 5 assumes ω is differentiable in k and that v (hence u) ranges over all real numbers. Both are implicit in the text.
- The sign in [K,P] = iħm depends on convention (K = mX - tP here).
- All scripts are in checks/ (check_a-01..04.py and fig_a-*.py). They need no network access and use CODATA constants from scipy.constants.
