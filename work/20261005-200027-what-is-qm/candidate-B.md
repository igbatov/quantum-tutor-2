<!-- strategy: geometric: arrows and shadows (photon polarization) -->

Quantum mechanics is the physics of atoms, electrons and light; it is the theory underneath chemistry and much of modern technology. At its heart it rewrites two everyday ideas: what it means for something to have a property, and what happens when you measure it.

Bright light behaves as a wave whose electric field wiggles in a direction across the beam: its polarization. A polarizing filter, like those in polarized sunglasses, passes light wiggling along its built-in axis, blocks light wiggling straight across it, and lets slanted light partly through. All of this is ordinary wave optics.

The quantum part shows up when you dim the light to single photons, the indivisible lumps light comes in. A slanted photon can't partly get through: each one passes whole or is blocked, unpredictably. Quantum mechanics predicts only the chance, and its rules fit in one picture:

- The photon's state is described by an arrow of length 1, pointing along its polarization.
- A filter asks the photon a two-answer question: "along my axis (pass) or across it (blocked)?" Nobody needs to watch; the filter does the asking.
- The chance of each answer is the square of the arrow's shadow on that direction: **chance = shadow²**. The shadow is how far the arrow reaches along that direction, like a tilted stick's shadow under an overhead sun.
- After the question, the arrow is replaced by the answer: a photon that passed a vertical filter is now vertical, and passes another vertical filter for certain.

Take a photon polarized at 30° from a vertical filter's axis. Its shadow on the vertical is about 0.866, which squared is 0.75: a 75% chance to pass. Its shadow on the horizontal is 0.5, which squared is 0.25: a 25% chance to be blocked. These always add to 100%: the shadows and the arrow form a right triangle, so by Pythagoras the squared shadows add up to the arrow's length squared, which is 1.

<!-- FIGURE: b-shadow | Geometric diagram, equal axis scaling, no grid. A vertical dashed line labelled "filter's axis (vertical)" and a horizontal dashed line labelled "across the axis (horizontal)", crossing at the origin. A thick arrow of length 1 from the origin, tilted 30 degrees from vertical toward the right, labelled "photon's polarization", with the 30° angle between the arrow and the vertical axis marked. Thin dotted lines from the arrow tip perpendicular to each axis. Highlight the shadow on the vertical axis (from the origin up to cos 30° ≈ 0.866) in blue and the shadow on the horizontal axis (from the origin to sin 30° = 0.5) in orange, each labelled with its length. Annotations: "chance to pass = 0.866² ≈ 0.75", "chance to be blocked = 0.5² = 0.25", "0.75 + 0.25 = 1, because the arrow has length 1 (Pythagoras)". The learner should notice: the squared shadows are the chances, and they automatically add to 100%. -->

Here is the payoff, assuming ideal filters. Send 100 photons that just passed a vertical filter at a horizontal one: a vertical arrow has no horizontal shadow, so none get through. Now slip a 45° filter in between them. About half pass it, roughly 50, each now pointing at 45°; half of those pass the horizontal filter, roughly 25. Adding a filter let more light through! A mere sieve, sorting photons by some fixed property, could never do that. So asking the question changes the photon, resetting its arrow to the answer: measuring is not just looking. (Bright light does this too, as wave optics predicts; what's quantum is that it happens photon by photon, by chance.)

<!-- FIGURE: b-three-filters | Two-row diagram of expected (average) photon counts with ideal filters, read left to right. Row 1, titled "two filters": a vertical filter, a bar labelled 100, a horizontal filter, a bar labelled 0. Row 2, titled "three filters": a vertical filter, a bar labelled 100, a 45° filter, a bar labelled 50, a horizontal filter, a bar labelled 25. Draw each filter as a small square with a line segment through it along the filter's axis (vertical, 45°, horizontal); bar heights proportional to the counts, same scale in both rows. Overall title: "Adding a filter lets more light through". The learner should notice: inserting the 45° filter raises the number getting through from 0 to about 25, which is impossible if filters only removed photons and left the survivors unchanged. -->

A 45° photon is often called "a superposition of vertical and horizontal". Is each one secretly vertical or horizontal, and we just don't know which? Then a 45° filter would pass only half of them, since vertical and horizontal photons each pass it half the time. In fact, it passes every one. Nor is the photon "both at once": it is one arrow pointing one way. "Superposition of vertical and horizontal" only means that this arrow casts a shadow on both. Likewise, a vertical photon is a superposition of the two diagonals, 45° and 135°.

So a 45° photon's answer to a 45° filter is certain, but its answer to a vertical filter is 50/50. That is how quantum mechanics rewrites "having a property": an answer is certain only when the arrow lies right along that answer's direction. No arrow is both vertical-or-horizontal and diagonal, so no way of preparing a photon makes both answers certain. This is the simplest case of the kind of trade-off behind Heisenberg's uncertainty principle.

Zooming out, quantum mechanics is about:

- **states**: arrows, in general with many more directions and with complex numbers in place of ordinary lengths (needed already for light whose wiggle goes round in circles), turning smoothly in time between measurements as the Schrödinger equation describes;
- **questions**: each measurement has a fixed set of possible answers;
- **shadows**: chances are squared shadows;
- **updates**: the answer you get replaces the arrow.

A photon's polarization is exactly what quantum computers call a qubit. With many more directions, the same rules describe electrons in atoms, and through them chemistry, lasers and transistors. The predictions are confirmed to extraordinary precision; what the arrow "really is", and what physically happens when it updates, are still debated.

A natural next step is entanglement: two photons sharing one arrow (in a space with four directions) instead of one each.

**Check yourself:** In the three-filter setup, how many of the 100 photons get through if you turn the middle filter to vertical, the same as the first?
