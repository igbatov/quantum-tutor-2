**Animation: decoherence-process** (`decoherence-process.gif`, about 9 s, loops)

A heavy particle goes through two paths, L and R. A photon scatters off it and ends in |E_L⟩ or |E_R⟩ depending on the path. Nobody looks at the photon. The screen then shows

P(x) = ½|ψ_L|² + ½|ψ_R|² + Re[ψ_L* ψ_R ⟨E_L|E_R⟩].

- **Panel A:** the particle's two path waves, |ψ_L(x)|² (solid) and |ψ_R(x)|² (dashed). They lie on top of each other and stay exactly the same in every frame, because the photon gives the particle no kick.
- **Panel B:** the photon's two possible final states, drawn as unit arrows in an abstract state space (not the lab). The cosine of the angle between them is the overlap |⟨E_L|E_R⟩|. The small box is a lab schematic: the two path positions are a distance d apart, and the red bar is the photon wavelength λ.
- **Panel C:** the screen pattern P(x) (bold), the one-slit sum ½|ψ_L|² + ½|ψ_R|² (dashed), and the cross term (thin).

**Part 1 (one photon).** d/λ grows from 0 to 0.5, so the overlap ⟨E_L|E_R⟩ = sin(2πd/λ)/(2πd/λ) falls from 1 to 0. The cross term is multiplied by this number, so the stripes fade until P(x) equals the one-slit sum. At d/λ = 0 the stripes reach zero. At d/λ = 0.5 there are no two-path stripes left, though the one-slit envelope still has its own small side bands beyond |x| = 4s. The animation stops at d/λ = 0.5. Past that point the overlap turns negative and the stripes would come back shifted by half a spacing.

**Part 2 (several photons).** Each photon has overlap 0.6 (d/λ ≈ 0.26). With N independent photons the overlaps multiply: ⟨E_L|E_R⟩ = 0.6^N, which gives 0.60, 0.36, 0.22, 0.13 and 0.08 for N = 1 to 5. Each weak scattering removes only some of the stripe contrast, but many of them together wash it out.

**Visibility.** In every frame, the stripe contrast of P(x) measured relative to the one-slit sum, (max − min)/(max + min) of P / (½|ψ_L|² + ½|ψ_R|²), equals |⟨E_L|E_R⟩|. The script checks this numerically (error below 1e-15).

**Idealizations:**
- The particle is heavy enough that it does not recoil, so ψ_L and ψ_R are unchanged.
- Each photon leaves from a point at the particle's position in a random direction (isotropic emission).
- The screen is far away. Each path wave is a one-slit envelope times a phase e^{±iπx/s}, with slit separation 4 × slit width.
- There is one photon in Part 1, and N independent photons in Part 2.
- The photon states are pure, and nothing else couples to the paths.
- The x axis is in units of the fringe spacing s. Densities are in units of |ψ_L(0)|².
