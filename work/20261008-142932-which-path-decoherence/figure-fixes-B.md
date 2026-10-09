# Figure fixes for final-B.md (two figures to redraw)

## 1. b-does-it-explain-the-dot (script: checks/fig_b-does-it-explain-the-dot_2.py)

Change only the many-worlds box text. Replace

    "both dots happen, in two branches that\ncan no longer interfere; we are in one"

with

    "every possible dot happens, each in its\nown branch; the branches can no longer\ninterfere; we are in one"

Keep everything else as drawn: the four identical path/photon/screen drawings (pilot-wave panel keeps its black particle dot), the other three box texts, and the footer "Same predictions for every experiment above; objective collapse differs only by amounts far too small to detect for molecules, growing with the amount of matter." The many-worlds box is now three lines, like the pilot-wave box; make sure it does not overlap "photon state B".

## 2. b-dust-grain (script: checks/fig_b-dust-grain.py)

Move the microwave-background mark from Δx/λ = 0.01 to Δx/λ = 0.019 (on the solid curve; the curve reads about 380 event times there, matching the full Joos–Zeh calculation: ~10 CMB scatterings per second × ~40 s ≈ 380, per-scattering record ≈ 2.6 × 10⁻³). Relabel it

    "microwave\nbackground\n(full calculation:\n≈380 events)"

and reposition the label so it does not sit on the curve (e.g. text at about (0.06, 2500) with the arrow to the mark). Leave the sunlight mark (Δx/λ = 20), the air-molecules arrow, the dashed (λ/Δx)² line, the Δx = λ/2 line, the axes, the title and the legend unchanged. The caption explains why the mark is not at the naive 0.01 for 1-mm waves (shorter waves do most of the scattering, effective λ ≈ 0.7 mm; photons arrive from all directions, doubling each record), so no extra annotation is needed.

## Not required (only if b-rules-out is ever redrawn)

Panel (b) title "seen when one photon is scattered" → "model: one photon scattered"; footnote "whenever the record comes with a recoil" → "for photon scattering". The caption in final-B.md already tells the reader how to read the current labels.
