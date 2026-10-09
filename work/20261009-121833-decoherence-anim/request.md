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
