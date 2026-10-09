# Request
Learner: "Give animation of this process" — the process from the last quick answer: a heavy particle in a two-path superposition, a scatterer starting in |E>, the joint state (|L>|E_L> + |R>|E_R>)/√2, and
P(x) = ½|ψ_L|² + ½|ψ_R|² + Re[ψ_L* ψ_R <E_L|E_R>].
Key point the learner pressed on: ψ_L and ψ_R do NOT change (no kick); only the overlap <E_L|E_R> changes, and the stripes fade because the cross term is multiplied by it.

# Animation spec (b-free, name: decoherence-process)
GIF via matplotlib FuncAnimation + PillowWriter, ~90–120 frames, ~12 fps, < 3 MB, ~800 px wide, plain white style like earlier figures.
Parameter: a scatterer photon with wavelength λ and path separation d; isotropic overlap c(d/λ) = sin(2πd/λ)/(2πd/λ). Animate d/λ from 0 to ~0.5 (c from 1 to 0), hold, then optionally continue to a few scatterers N=1..5 at fixed c=0.6 to show multiplying (c^N), hold. Keep it clear; one phase is fine if two is cluttered.
Panels:
 A. "Particle's path waves (unchanged)": |ψ_L(x)|² and |ψ_R(x)|² — far-screen, ψ_{L,R}= A(x) e^{±iπx/s}, A = one-slit envelope with slit separation 4× width; show they stay identical every frame (maybe also Re ψ_L, Re ψ_R faint).
 B. "Scatterer's two final states": the two unit arrows |E_L>, |E_R> in an abstract plane, angle θ with cosθ = |c| (label "abstract state space, not lab"), plus the number |<E_L|E_R>| shown. Optional small schematic of the photon leaving from the left or right path (labelled schematic).
 C. "What the screen shows": P(x) bold, the two-one-slit-sum dashed (constant), the cross term thin; the text "visibility = |<E_L|E_R>| = …".
Captions must be literally true; name idealizations (heavy particle, no recoil, isotropic emission, far screen, one photon). If c becomes negative past d=λ/2, don't go past λ/2 (or explain the half-spacing shift) — stopping at λ/2 is simpler.
Save figures/decoherence-process.gif, checks/anim_decoherence-process.py, figures/decoherence-process.caption.md, and 3 stills (look at them).

# Second request (learner): "Give animation in the style of https://physics.weber.edu/schroeder/software/QuantumScattering2D.html"
That page (Dan Schroeder's 2D quantum scattering simulation) shows a real 2D Schrödinger-equation simulation: black background, the wavefunction drawn with brightness = |ψ| (or |ψ|²) and hue = phase of ψ, barriers drawn in white/grey, a wave packet moving and scattering in real time.

## Spec: decoherence-2d.gif
- Real simulation: 2D time-dependent Schrödinger equation, split-step Fourier method (numpy FFT), ħ = m = 1, grid ~ 400×400 or 512×512, absorbing boundary (complex absorbing potential or mask) so nothing wraps around. Gaussian packet with momentum toward a wall with two slits (slit separation ≈ 4× slit width, like before). Wall = high potential barrier.
- Separate the branches honestly: evolve the full packet until the transmitted part has just cleared the wall (time t1). Then split the transmitted wave into ψ_L (part on the left-slit side of the symmetry line) and ψ_R (right side) and evolve each on its own afterwards (linearity: ψ_L + ψ_R equals the full transmitted wave at all later times; check this numerically). Discard or dim the reflected part (say so).
- Layout: two simulation panels side by side, same frames in time, plus a "screen" strip below each:
  1. "No record": the full wave ψ_L + ψ_R in Schroeder style (hue = phase, brightness = amplitude). Screen strip: probability |ψ_L+ψ_R|² along a line near the far edge, plus dots (hits) sampled from it accumulating over the animation → stripes.
  2. "Photon scattered at the slits (perfect record, ⟨E_L|E_R⟩ = 0)": at t1 a brief flash/photon wavefront drawn at the slits (schematic, labelled). After t1 the particle has no single wavefunction (it's entangled), so do NOT draw one combined phase-colored wave. Draw the two branches each in Schroeder style but overlaid as two layers, OR draw the density |ψ_L|²+|ψ_R|² in white/grey brightness only with a label "particle alone has no single phase: entangled with the photon". Choose what reads clearest; label it truthfully. Screen strip: |ψ_L|²+|ψ_R|² and accumulating hits → no stripes.
- Optional third panel or a final segment with partial overlap c = 0.5 (P = |ψ_L|²+|ψ_R|²+2c Re ψ_L*ψ_R): only if it doesn't clutter.
- ~120–200 frames, ~15 fps, < 5 MB, ~900 px wide. A small phase colour wheel legend. Title. Text labels short.
- Checks to print: norm conservation before absorption; ‖(ψ_L+ψ_R) − ψ_full‖ small after t1 (evolve the full one too); visibility of screen patterns (≈1 for no record near centre, ≈0 for perfect record).
- Save figures/decoherence-2d.gif, checks/anim_decoherence-2d.py, figures/decoherence-2d.caption.md (true caption, idealizations named: 2D, hard-ish wall, one photon perfect record, recoil neglected, near-field distances of the simulation box, not the far screen), 3 stills you look at.
