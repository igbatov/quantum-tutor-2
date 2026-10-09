**Animation: decoherence-2d** (`decoherence-2d.gif`, 129 frames at 15 fps, about 9 s, with the last frame held 2 s; it loops)

This is a real simulation of the 2D Schrödinger equation (split-step Fourier method, ħ = m = 1, 512 × 512 grid), drawn the way Dan Schroeder's QuantumScattering2D draws waves: black background, hue = phase of ψ, brightness = |ψ|. A wave packet moves down onto a wall (grey bar) with two slits. The slits are 3 wavelengths wide and their centres are 12 wavelengths apart (4 × the width).

- **Before the slits, both panels are identical.** It is the same wave.
- **At time t1** (when the slits have emptied), the wave below the wall is cut along the symmetry line into ψ_L (the left half, mostly from the left slit) and ψ_R (the right half). Each half is then evolved on its own. Because the equation is linear, ψ_L + ψ_R is exactly the wave the uncut evolution gives. About 75 % of the packet bounces back off the wall. That reflected part fades out over the first few frames after t1 and is not shown after that; it never reaches the screen row.
- **Panel 1, "No record":** the wave ψ_L + ψ_R. Where the two beams overlap you can see brightness stripes: interference.
- **Panel 2, "Photon scattered at the slits":** at t1 one photon scatters off the particle just below the slits. The dashed yellow circles are a schematic of the photon leaving from the left or the right slit. They are not computed. The photon's two final states are taken to be orthogonal, ⟨E_L|E_R⟩ = 0 (a perfect which-path record). After that the particle is entangled with the photon and no longer has a wavefunction of its own, so it cannot be drawn with a phase colour. The panel shows only its probability density, |ψ_L|² + |ψ_R|², as white brightness (the square root is drawn, so it uses the same |ψ| scale as panel 1). The two beams pass through each other without two-slit stripes. ψ_L and ψ_R are exactly the same in both panels; only the photon's record differs.
- **Screen strips:** the curve is the density on the dashed "screen row", added up over time. The dots are single detections, drawn at random from that density as it arrives; each dot stands for one repeat of the experiment. On the left the dots build up stripes. On the right they build up a broad, smooth hump with no two-slit stripes. It is really two overlapping one-slit beams, so the top has a shallow 3 % dip in the middle, and there are small wings near the panel edges (about 5 % of the peak).

**Checks (printed by the script):**
- Norm conservation before anything reaches the absorbing edges: drift 8 × 10⁻¹⁰.
- Linearity: ‖(ψ_L + ψ_R) − ψ_transmitted‖ / ‖ψ_transmitted‖ = 4 × 10⁻¹⁴ at all times after t1.
- Cutting at t1 leaves a little wave still inside or above the slits. Compared with the full uncut simulation, the wave below the wall differs by at most 3 % in norm.
- Stripe visibility near the centre of the screen row, (max − min)/(max + min) over about ±1 fringe: 0.93 with no record and 0.015 with a perfect record. A partial record with ⟨E_L|E_R⟩ = 0.5 (not animated) gives 0.47.

The no-record visibility is not exactly 1. The packet contains a spread of wavelengths, which smears the fringes slightly, and away from the centre the two beams arrive with unequal strength.

**Idealizations and display choices:**
- 2D, not 3D. The wall is a finite potential step (height 9 × the packet's energy), so it is "hard-ish", not infinitely hard.
- One photon and a perfect record, ⟨E_L|E_R⟩ = 0. The photon's emission and the particle's recoil are not simulated; recoil is neglected, so ψ_L and ψ_R are not kicked.
- ψ_L and ψ_R are defined by cutting at the symmetry line at t1. A small amount of wave (about 1 % of the probability) is within 5 cells of that line at t1.
- The screen row is only about 41 wavelengths past the slits. That is near-field, well short of the far-screen distance (slit separation² / wavelength ≈ 144 wavelengths). The stripes therefore don't have the textbook far-screen shape.
- The edges of the box absorb the wave (complex absorbing potential), so nothing wraps around. The absorbing layer is hidden.
- Brightness is rescaled from frame to frame, with the same scale in both panels, so the spreading wave stays visible. Values below 5 % of the scale are drawn black. Colours are reduced to a fixed 240-colour palette for the GIF.
