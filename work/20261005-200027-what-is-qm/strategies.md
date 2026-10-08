# Strategies: "Describe what quantum mechanics is about"

**Situation.** This is the first question of the session, in mode `new-question`, with no previous run. The profile is empty: the level defaults to conceptual and there are no recorded past choices. The question is about as broad as it gets, so every candidate must be a complete answer whatever route it takes:

1. An honest one-sentence answer that includes scope: atoms, electrons and light, and the fact that the theory underlies chemistry and modern technology.
2. One concrete window into the core of the theory, done properly.
3. A zoom-out paragraph saying what quantum mechanics is about, in that candidate's own words rather than a generic list.
4. The one misconception that belongs to its route, defused.
5. One next step and one check question.

At the conceptual level that means no notation, at most one simple relation, roughly 600–700 words and no headings. Since nothing is known about this learner yet, the three candidates should be as different as possible. Which one they pick will tell us whether they learn best from experiments, from pictures, or from explanations of the everyday world.

## 1. Lenses considered

**1. Mechanism-first (fit 3, rejected).** This would state quantum mechanics as a short rulebook and then show what follows, e.g. with a beam splitter. The rules: a system has an amplitude for each possible outcome; the chance of an outcome is the amplitude's size squared; amplitudes for indistinguishable routes add; between measurements, amplitudes change smoothly. It is compact and honest, but a conceptual first-timer will struggle to hold onto rules stated before any phenomenon. Strategies 1 and 2 deliver the same rules, each grounded in an experiment.

**2. Experiment-first (fit 5, chosen as Strategy 1).** Start from what is actually seen when electrons go through two slits one at a time: single dots, random spots, stripes, and stripes destroyed by a which-path record. The amplitude rule then emerges as the only thing that fits. It needs no math. It is the most famous quantum experiment, so it connects to (and can correct) anything they may have heard. It shows lumpiness, chance, interference and measurement in one setting.

**3. Geometric (fit 4, chosen as Strategy 2).** Single photons meet polarizing filters. The state is an arrow of length 1, the chance of passing is the square of its shadow, and Pythagoras explains why chances are squares. Linear polarization needs only a flat 2D arrow (the Bloch sphere would be too much at this level). It leaves the learner a reusable model of superposition, measurement and incompatible questions, since it is exactly a qubit. Fit 4 rather than 5 only because polarization is less familiar, and further from "what the world is made of", than the other two routes.

**4. Classical-contrast (fit 5, chosen as Strategy 3).** Build the planetary atom fairly and let classical physics make its predictions: collapse in about 10⁻¹¹ s, a rainbow smear of light, and atoms of any size. Then show what quantum mechanics puts in its place: allowed amplitude patterns, an energy ladder, sharp colors and a lowest rung. This answers "what is it about" in the most literal sense, because it is the physics of what matter is. It uses everyday hooks (neon signs, sodium street lamps, starlight) and needs only E = hf.

**5. Analogy-led (fit 2, rejected).** Carry one analogy throughout, e.g. "quantum mechanics is probability with waves", via ripples on a pond or noise-cancelling headphones. For a question this broad, one analogy has to stretch across quantization, measurement and interference. It breaks in several places, and that is exactly when analogies mislead. Analogies are used locally instead (noise-cancelling in S1, guitar string in S3), each with its limits stated.

**6. Worked-example-first (fit 2, rejected).** Compute something first, then generalize: e.g. hydrogen's red line from the energy ladder (a 1.89 eV gap gives 656 nm), or the 75% chance that a photon at 30° passes a filter. Starting with a calculation suits an intermediate learner with a narrow question. Here, numbers up front would delay the actual answer. Small worked numbers survive inside S2 (75%/25%) and S3 (656 nm).

**7. Historical (fit 3, rejected).** Tell the 1900–1927 story: glowing hot objects, the photoelectric effect, unstable atoms and sharp spectral lines, electron waves, then the new mechanics. It is engaging and answers "why does this theory exist", but it drifts toward names and dates rather than ideas the learner can reason with. It also invites well-known historical myths. Its central puzzle, the atom, is S3's content, so the two would converge. S3 keeps the strongest puzzle without the chronology.

**8. Question-led (fit 3, rejected).** A chain of small predictions ("what pattern do you expect? now close a slit: more or fewer hits here?"). It is engaging, but in one written answer the predictions are rhetorical, and with any interference example it would duplicate S1. S1 borrows one predict-then-reveal beat, and every candidate's check question keeps the active element.

**9. Formal derivation (fit 1, rejected).** Hilbert space, operators, the Schrödinger equation. The learner has signalled nothing technical and the level is conceptual.

**10. Misconception-first (fit 3, rejected).** Open with popular claims ("in two places at once", "the observer creates reality", "it's only about tiny things") and replace each one. That helps many curious learners, but this profile records no misconceptions. Leading a first answer with wrong pictures puts them in front first and spends the answer on what quantum mechanics is not. Instead, each chosen strategy defuses the one misconception that belongs to its route.

## 2. The three chosen, and how they stay apart

| | Strategy 1 | Strategy 2 | Strategy 3 |
|---|---|---|---|
| Lens | experiment-first | geometric | classical-contrast |
| Example | electrons through two slits, one at a time | single photons through polarizing filters | glowing hydrogen; the atom classical physics says should collapse |
| Representation | dot patterns and chance curves | a length-1 arrow and its shadows | an energy ladder and a "barcode" of spectral lines |
| Idea in the foreground | chances come from amplitudes that add and cancel | states, measurement as a question, incompatible questions | quantized energy; why matter is stable |
| Misconception defused | "goes through both slits / is in two places at once"; the conscious observer | superposition as "secretly one" or "both at once" | the electron as a tiny planet |
| Relation used | none | chance = shadow² | E = hf |
| Next step | decoherence | entanglement | exclusion principle and periodic table |

To stop them converging:
- S1 uses no arrows and no polarization.
- S2 never speaks of interference or cancellation.
- S3 uses neither slits nor polarizers.
- Each zoom-out sums up the subject in its own vocabulary, not a shared generic list: S1 uses lumps, chances, amplitudes and records; S2 uses states, questions, shadows and updates; S3 uses ladders, clouds, patterns and matter.

## 3. Strategies

### Strategy 1: One experiment, the whole story

**First line of the candidate:** `<!-- strategy: experiment-first: the double slit, one electron at a time -->`

**Plan.** Give the one-sentence answer, then go straight into the experiment. There is an electron source, a wall with two narrow slits, and a screen that flashes where each electron lands. The electrons are sent at such a low rate that only one is in the apparatus at a time, so nothing can be blamed on electrons bumping into each other. Invite one quick prediction: tiny balls should pile up in one smooth heap. Then reveal the facts in three beats:
- Each electron arrives whole, as one dot, at a spot nobody can predict.
- After thousands of dots, a striped pattern appears (a-buildup).
- With one slit closed, the stripes vanish into a single smooth hump. Spots that were dark with both slits open now receive electrons, so opening a second way to get somewhere made that place unreachable (a-one-vs-two).

Let the rule emerge as the only thing that fits. Each route to a spot gets an *amplitude*: a quantity that, like the height of a wave, can be positive or negative (a complex number in the full theory). When nothing records which route was taken, the amplitudes for the routes add first, and the chance of landing there is the size of the total, squared. At the dark stripes the two cancel. Use noise-cancelling headphones as the analogy for cancellation, and bound it in the same breath: sound is a wave of air, but an amplitude is not a wave of any stuff, and no detector ever finds part of an electron. Then which-path: if anything records which slit each electron used (a detector, or even one stray photon bouncing off it), the stripes disappear and the plain sum of the two one-slit patterns returns. "Observing" means any physical record, not a mind.

Zoom out, using this experiment as the key to the subject. Quantum mechanics is about:
- things that arrive in whole lumps;
- a theory that predicts chances rather than individual outcomes;
- amplitudes that add and cancel, the engine behind atoms, chemistry, transistors and lasers;
- records that decide what can interfere.

Big everyday objects never show stripes because their surroundings record them constantly (decoherence). Defuse "the electron goes through both slits / is in two places at once": the theory says both routes' amplitudes contribute. What the electron "really does" in between is exactly where interpretations differ, while the predictions themselves are not in doubt. No equations. Aim for about 600 words.

**Example.** Electrons fired one at a time at two slits. The concrete hook is the first dark stripe beside the centre. With one slit open, that spot gets nearly as many hits as the centre does. With both open, it gets none.

**Figures.**

```
<!-- FIGURE: a-buildup | Simulated two-slit detection screen, four panels side by side titled "10 electrons", "100 electrons", "1,000 electrons", "10,000 electrons" (cumulative: each panel keeps the previous dots and adds more; fixed random seed). Each electron is one small black dot on a white rectangle. Horizontal position X (in units of the stripe spacing, range -6 to 6) is drawn at random from P(X) proportional to cos^2(pi X) * [sin(pi X/4)/(pi X/4)]^2, i.e. slit separation = 4 x slit width; vertical position uniform at random (the slits are long vertical slots). Shrink the dot size in later panels so 10,000 dots stay readable. No tick numbers; x-axis label "position on screen". The learner should notice: every electron arrives whole, as one dot at an unpredictable place, and the stripes exist only in the pattern of many dots. -->
<!-- FIGURE: a-one-vs-two | Line plot over screen positions X from -6 to 6 (units of the stripe spacing, same set-up as a-buildup). Three curves of relative chance of landing per unit length: (1) "one slit open (either one)": P1(X) = [sin(pi X/4)/(pi X/4)]^2, thin grey; (2) "if each electron simply went through one slit or the other": 2*P1(X), dashed; (3) "both slits open (what is actually seen)": 4*P1(X)*cos^2(pi X), solid and bold. Mark the dark stripes at X = -1.5, -0.5, 0.5, 1.5 with small downward arrows: there curve 3 is exactly zero while curve 1 is clearly above zero (about 0.95 at |X| = 0.5 and 0.62 at |X| = 1.5). y-axis "relative chance of landing here", x-axis "position on screen". The learner should notice: at the dark stripes an electron could land with one slit open, but opening the second slit made those spots unreachable; chances did not add, amplitudes cancelled. -->
```

**Opening sentence.** "Quantum mechanics is the theory of how matter and light behave at the scale of atoms, and the quickest way to see what it is about is one experiment: fire electrons, one at a time, at a wall with two narrow slits, and record where each one lands."

**Guardrails.**
- Never state as fact that the electron "is a wave", "is in two places at once" or "goes through both slits". Say that both routes' amplitudes contribute, and flag what happens in between as a matter of interpretation.
- "Observing" means any physical record of which slit was used (a detector, a stray photon, an air molecule); no minds are involved. Don't present "collapse" as settled physics. One clause saying that what happens during a measurement is still debated is enough.
- Describe the one-slit pattern as a single smooth hump with no stripes, which matches a-one-vs-two, where the screen is far away. Avoid "a band behind each slit".
- The experiment really has been done with electrons arriving one at a time, but don't name experiments or years. If molecules are mentioned, keep it conservative ("molecules of hundreds of atoms").
- On randomness, say that quantum mechanics gives only the chances and nobody can predict the individual spot. Don't claim nature has been proven fundamentally random, and don't bring in Bell's theorem.
- Decoherence explains why big objects show no stripes. It does not by itself settle the measurement problem.
- Describe the amplitude as "like the height of a wave: it can be positive or negative (complex in the full theory)". Don't use arrows, which are Strategy 2's picture.

**Next step and check question.** Next: why baseballs never show stripes (decoherence). Check idea: "**Check yourself:** At a spot where no electrons land when both slits are open, what happens if you close one slit: do electrons start landing there, or does it stay empty?" (Answer: they start landing there.)

### Strategy 2: Arrows and shadows

**First line of the candidate:** `<!-- strategy: geometric: arrows and shadows (photon polarization) -->`

**Plan.** Give the one-sentence answer, then anchor it in something familiar. Light's wiggle has a direction across the beam, called its polarization. A polarizing filter, like the ones in polarized sunglasses, passes light wiggling along its axis and blocks light wiggling across it. Be honest that with bright light this is ordinary wave optics. The quantum part appears when light is dimmed to single photons, because a photon is never split: each one either passes whole or is absorbed, and which happens is unpredictable.

Then build the picture that carries the whole answer:
- The photon's state is an arrow of length 1 pointing along its polarization.
- A filter asks a two-answer question: "along my axis, or across it?"
- The chance of each answer is the square of the arrow's shadow on that direction. The two shadows of a length-1 arrow obey Pythagoras, so the two chances always add to 100% (b-shadow, worked at 30°: 75% pass, 25% blocked).
- After the question, the arrow is replaced by the answer. A photon that passed a vertical filter is now vertical, and it passes a second vertical filter for certain.

The payoff, counted with 100 photons fresh from a vertical filter: a horizontal filter next stops all of them. Slip a 45° filter in between and about 25 get through (b-three-filters). A filter that only sieved photons by a fixed property could never let more through just by being added, so asking the question resets the arrow.

Next, incompatible questions. No arrow lies along both the vertical and the 45° direction, so no photon state has definite answers to both questions, and no preparation can make both certain. This is the simplest version of the trade-off behind the uncertainty principle.

Defuse the superposition myth with a test, not a slogan. A 45° photon is called "a superposition of vertical and horizontal". Suppose each such photon were really a vertical or a horizontal photon that we just didn't know about. Then a 45° filter would pass only half of them. In fact it passes every one. So a superposition is one definite state that has no definite answer to the vertical-or-horizontal question. It is not "secretly one", and it is not "both at once".

Zoom out. Quantum mechanics is about:
- states, which are arrows (in general with many directions and complex numbers);
- measurements as questions with a fixed set of answers;
- chances given by squared shadows;
- states updated by the answer.

This two-direction arrow is exactly a qubit. The same structure, with many more directions, describes electrons in atoms, and through them chemistry, lasers and transistors. The only relation used is chance = shadow². Aim for about 650–700 words. If it runs long, keep the three-filter beat and the superposition test, and cut incompatibility to one sentence.

**Example.** A photon polarized at 30° from a vertical filter's axis passes 75% of the time. Then the three-filter count: 100 photons, then about 50, then about 25.

**Figures.**

```
<!-- FIGURE: b-shadow | Geometric diagram, equal axis scaling, no grid. A vertical dashed line labelled "filter's axis (vertical)" and a horizontal dashed line labelled "across the axis (horizontal)", crossing at the origin. A thick arrow of length 1 from the origin at 30 degrees from vertical, labelled "photon's polarization". Thin dotted lines from the arrow tip perpendicular to each axis. Highlight the shadow on the vertical axis (length cos 30° ≈ 0.87) in blue and the shadow on the horizontal axis (length sin 30° = 0.50) in orange. Annotations: "chance to pass = 0.87² ≈ 0.75", "chance to be blocked = 0.50² = 0.25", "0.75 + 0.25 = 1, because the arrow has length 1 (Pythagoras)". The learner should notice: the squared shadows are the chances, and they automatically add to 100%. -->
<!-- FIGURE: b-three-filters | Two-row step/bar diagram of expected (average) photon counts. Both rows start with 100 photons polarized vertically (fresh from a vertical filter). Row 1 "two filters": bar 100, then a horizontal filter, then bar 0. Row 2 "three filters": bar 100, then a 45° filter, bar 50, then a horizontal filter, bar 25. Above each filter draw a short line segment at the filter's axis angle; print each count on its bar. Title: "Adding a filter lets more light through". The learner should notice: inserting the 45° filter takes the number getting through from 0 to 25, which is impossible if filters only removed photons and left the survivors unchanged. -->
```

**Opening sentence.** "Quantum mechanics is the physics of atoms, electrons and light, and at its heart it rewrites two everyday ideas: what it means for something to have a property, and what happens when you measure it."

**Guardrails.**
- With bright light, the filter results (including the three-filter trick) follow from classical wave optics. Say so. The quantum content is that single photons pass whole or not at all, unpredictably, with these chances.
- Use linear polarization only, with one clause saying that the general case (e.g. circular polarization) needs complex numbers.
- The three-filter result shows that filters change photons; they are not pure sieves. It does not rule out hidden variables, so don't claim it does.
- For incompatible questions, likewise, say that no quantum state and no preparation gives definite answers to both. Don't say experiments prove a single photon has no hidden answer: that needs entangled pairs and Bell tests, which is a later topic.
- Counts are averages ("about 25 of 100").
- If a home demo is offered, use two polarized-sunglasses lenses, one rotated 90°, which go dark. Don't promise effects with phone screens.
- Link to the uncertainty principle as "the simplest version of the same kind of trade-off", not as identical to position and momentum.
- Don't speak of interference or cancellation, which belong to Strategy 1.

**Next step and check question.** Next: entanglement, where two photons share one joint state instead of having one arrow each. Check idea: "**Check yourself:** In the three-filter setup, how many of the 100 photons get through if you turn the middle filter to vertical, the same as the first?" (Answer: none.)

### Strategy 3: The atom that shouldn't exist

**First line of the candidate:** `<!-- strategy: classical-contrast: the atom that shouldn't exist -->`

**Plan.** Give the one-sentence answer, then build the classical picture fairly. The atom is a tiny solar system: electrons orbit a nucleus, held by electric attraction. That is exactly where classical physics leads you (Newton's mechanics plus Maxwell's electromagnetism, which work flawlessly for planets, motors and radio). Then let that physics make its predictions. A circling charge gives off light, so the electron should lose energy and spiral into the nucleus in about a hundred-billionth of a second, giving off a smear of all colors on the way. And since orbits could be any size, no two atoms would be alike. Set this against the facts: atoms left alone never collapse, every hydrogen atom is identical, and glowing hydrogen gives off only a few sharp colors rather than a rainbow (c-ladder-spectrum).

Then quantum mechanics' replacement. A bound electron is described by a pattern of amplitudes around the nucleus, and the squared size of that pattern gives the "cloud" of where the electron is likely to be found if you look. Compare a guitar string, which can only vibrate in patterns that fit between its fixed ends. Bound the analogy immediately: nothing is vibrating, the pattern is 3D, the whole electron is always found at a single spot, and hydrogen's rungs crowd together near the top instead of being evenly spaced like a string's notes. Likewise, only certain patterns fit around the nucleus, each with a definite energy. Together they form a ladder of allowed energies.

Colors: when the electron drops from one rung to a lower one, the atom emits one photon carrying exactly the energy gap. E = hf (photon energy E, Planck's constant h, frequency f, which the eye sees as color) turns each gap into one color. The drop from rung 3 to rung 2 is hydrogen's red line at 656 nm. Astronomers recognize hydrogen in stars by this same pattern of lines.

Stability: there is a lowest rung, because squeezing the cloud closer to the nucleus raises the electron's energy of motion (a wave confined to a smaller space must wiggle more sharply). The bottom rung balances that cost against the nucleus's pull, and with no rung below it there is nothing to fall to. This is the uncertainty principle at work, a property of waves, not of clumsy measurement.

Defuse the planetary atom: the electron follows no path. In hydrogen's lowest state the cloud is a round ball and there is no orbiting at all, although the electron is not at rest.

Zoom out. Quantum mechanics is about matter coming in allowed states (ladders), chances (clouds) and wave-like patterns of amplitude. Add one more quantum rule, that no two electrons can share a state, and you get the periodic table, chemical bonds, why solids are solid, why copper conducts and silicon makes transistors, and the colors of LEDs and lasers. Add one sentence: these predictions are tested to extraordinary precision, while what the theory "means" is still debated. The only equation is E = hf. Aim for about 650–700 words. If it runs long, cut the guitar-string figure first.

**Example.** Hydrogen's visible lines: red at 656 nm from the rung 3 to rung 2 drop, plus 486, 434 and 410 nm. The yellow of sodium street lamps (589 nm) is an everyday echo. Numbers for checking: rungs at −13.6/n² eV; the 3→2 gap is 1.89 eV, which gives 656 nm with hc ≈ 1240 eV·nm.

**Figures.** c-ladder-spectrum is essential; c-standing-waves is optional and belongs only with the guitar-string analogy.

```
<!-- FIGURE: c-ladder-spectrum | Two panels. Left: hydrogen's energy ladder drawn to scale, horizontal lines at E_n = -13.6/n^2 eV for n = 1 to 6 (-13.6, -3.40, -1.51, -0.85, -0.54, -0.38 eV) labelled "rung 1" ... "rung 6", plus a dashed line at 0 eV labelled "electron set free"; y-axis "energy (eV)". Four downward arrows ending on rung 2, starting on rungs 3, 4, 5, 6, colored by the light they produce and labelled 656 nm (red), 486 nm (blue-green), 434 nm (blue-violet), 410 nm (violet); one grey arrow from rung 2 to rung 1 labelled "ultraviolet, invisible". Right: two horizontal strips over wavelengths 380-700 nm (x-axis "wavelength (nm)"): top strip "hot glowing solid (lamp filament)" filled with a continuous rainbow; bottom strip "glowing hydrogen" black with four thin bright lines at 410, 434, 486 and 656 nm in their colors. The learner should notice: each colored line is one drop between two rungs, so a ladder of separate rungs gives separate colors instead of a smooth rainbow. -->
<!-- FIGURE: c-standing-waves | A string fixed at both ends (black dots at x = 0 and x = 1), four rows. Rows 1-3: the allowed patterns y = sin(n pi x) for n = 1, 2, 3, drawn solid with the mirror image -sin(n pi x) faint, labelled "fits: 1 half-wave", "fits: 2 half-waves", "fits: 3 half-waves". Row 4: y = sin(2.5 pi x) in red, labelled "2.5 half-waves: does not end at the fixed point, not allowed", with a red cross at x = 1. The learner should notice: only whole numbers of half-waves fit between fixed ends, so only certain patterns are possible. -->
```

**Opening sentence.** "Quantum mechanics is the physics that explains what ordinary matter is and why it holds together: why atoms exist at all, why every hydrogen atom in the universe is identical, and why each element glows in its own particular colors."

**Guardrails.**
- The classical collapse estimate for hydrogen is about 1.6 × 10⁻¹¹ s. Say "about a hundred-billionth of a second".
- Excited rungs are not permanent: atoms drop down by emitting light, typically within billionths of a second. Stability is about the bottom rung only.
- The ground-state electron is not at rest (it has energy of motion) and is not orbiting (its angular momentum about the nucleus is zero). Describe the cloud as where you would likely find the electron if you looked, finding the whole electron at one spot each time. Avoid "smeared-out electron", and avoid "the cloud is just our ignorance".
- Don't use absorption by cool hydrogen as an example. Room-temperature hydrogen is H₂ molecules, and ground-state atoms absorb only ultraviolet lines, not the visible ones.
- Lines from stars are shifted by the stars' motion. Say astronomers recognize hydrogen by its pattern of lines, not that the wavelengths are identical.
- The periodic table, bonds and solids need the exclusion principle; call it "one more quantum rule".
- Prefer sodium street lamps or neon signs over fireworks, whose colors partly come from molecules.
- Don't say how long a "quantum jump" takes, or that it is instantaneous.
- Don't claim the atoms in your body have been intact since the Big Bang.
- Don't use slits or polarizers, which belong to Strategies 1 and 2.

**Next step and check question.** Next: how the "no two electrons in the same state" rule builds the periodic table. Check idea: "**Check yourself:** If an atom's ladder had only three rungs, how many different colors of light could it give off as its electron drops down?" (Answer: three.)
