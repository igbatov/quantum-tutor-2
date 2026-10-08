# Strategies: "Describe what quantum mechanics is about"

Run 20261005-200107-what-is-qm-teachback. Mode: new-question. Level: conceptual (empty profile, no history, no style preferences recorded yet).

## What this learner needs

This is a very broad first question from someone we know nothing about yet, so we pitch it at the conceptual level: plain words, no formalism, at most one simple relation. A good answer is an honest orientation, not a tour. It needs:

- a core idea the learner can restate, given in the first two sentences;
- one concrete centerpiece that lets them predict a situation they haven't seen;
- a short map of the other big ideas;
- the pop-culture myths most likely to be lurking defused (in two places at once, conscious observers, clumsy measurements);
- a clear line between what is settled and what is still argued about.

We have no record of this learner's taste, so the three candidates should differ as much as possible in style: the story of an experiment, a bounded analogy, and a predict-it-yourself puzzle. Then the learner's choice tells us something.

## Lens survey

1. **Mechanism-first.** Fit 3, rejected as a route. Open with the theory's computing rule in words: every way an event can happen gets an amplitude (an "arrow"); add the arrows for ways nothing tells apart, and square the length to get the probability. A Feynman-style example would be light reflecting off a mirror, where the arrows from far-off paths cancel. It is accurate and powerful, but abstract for a first contact, and the payoff comes late. The rule appears in words inside Strategy 1 and as arrow shadows inside Strategy 3 instead.
2. **Experiment-first.** Fit 5, chosen as Strategy 1. Start from what is literally seen when electrons go through two slits one at a time: single dots that build into stripes, dark spots created by opening a second slit, and stripes erased by a which-slit record. This is the standard demonstration that amplitudes combine, not probabilities. It needs no math and gives a rule the learner can carry to new setups. (I considered the Mach–Zehnder interferometer and rejected it: it teaches the same lesson, so it would produce the same text.)
3. **Geometric.** Fit 2 as a route, rejected; borrowed as a representation. This lens treats states as arrows, measurement as projection, and uses the Bloch sphere. The Bloch sphere ("opposite points are mutually exclusive states") confuses people who don't know linear algebra. The plain picture of polarization as an arrow and a filter as a direction is concrete, though, so Strategy 3 uses it.
4. **Classical-contrast.** Fit 4, rejected as a standalone route. List what classical physics assumes (smooth energies, definite properties read off passively, determinism, particles versus waves) and break each assumption. It suits a broad question, but it turns into a catalogue of claims with no single mechanism to reason with, and every row would borrow another strategy's example. Instead, each chosen strategy builds its own classical expectation before breaking it: balls through one slit, the planetary atom, filters that read labels.
5. **Analogy-led.** Fit 4, chosen as Strategy 2. A guitar string pinned at both ends can sound only certain notes. In the same way, an electron's wave hemmed in by the nucleus can take only certain patterns, which gives fixed energies, each element's color barcode, stable atoms and chemistry. It is concrete and everyday (music, neon signs, fireworks), explains the word "quantum", and retires the planetary-atom picture. The analogy's three limits must be stated as soon as it is introduced.
6. **Worked-example-first.** Fit 3, folded into Strategy 3. The three-filter arithmetic is ½, then ½ of that, then ½ again, which gives ⅛. The numbers are friendly, but leading with a calculation is dry for someone who asked for an overview. It works best as the payoff step inside the puzzle.
7. **Historical.** Fit 2, rejected. The story runs from 1900 to 1927: blackbody radiation, the photoelectric effect, Bohr's atom, de Broglie, Schrödinger and Born. It has story appeal, but it delays the core idea and invites myths: Kelvin's "nothing new to discover" quote is apocryphal, and Planck wasn't responding to the "ultraviolet catastrophe". It also leaves the learner with "energy comes in lumps" rather than the modern amplitude picture. Strategy 2 may use one historical sentence at most.
8. **Question-led.** Fit 4, chosen as Strategy 3. This is a chain of predict-then-see steps with polarizing filters:
   - half the light passes one filter;
   - identically prepared photons pass a tilted filter at random;
   - a 45° photon is not secretly vertical-or-horizontal;
   - crossed filters go dark, but a third filter slipped between them lets light through.

   It is active and low-math, uses something the learner can hold (polarized sunglasses), and covers the parts of QM the other two only mention: randomness, measurement that leaves a new state, and incompatible properties. (I rejected Stern–Gerlach because it needs magnets, spin and the "not literally spinning" caveat, which is too many new things for a first answer.)
9. **Formal derivation.** Fit 1, rejected. Nothing signals linear algebra or calculus, so it is far above this learner's level.
10. **Misconception-first.** Fit 3, rejected as a route. Start from pop myths: in two places at once, a conscious observer creates reality, everything is uncertain, Schrödinger's cat. The profile records no misconceptions, so leading with wrong pictures risks planting them, and it pushes the positive core idea down the page. Instead, each candidate defuses its two or three most relevant myths after the right picture is built.

## The three chosen strategies at a glance

| | Strategy 1 | Strategy 2 | Strategy 3 |
|---|---|---|---|
| Route | experiment-first story | bounded analogy, with a classical-contrast hook | question-led predictions |
| Example | single electrons, two slits | atomic color barcodes, guitar string, quantum dots | polarizing filters, one photon at a time |
| Representation | dot patterns, probability curves | standing-wave shapes, energy ladder | polarization arrows, filter sequences, simple fractions |
| Centerpiece | amplitudes add and cancel; a which-way record erases the stripes | confinement gives discrete energies; the wave gives odds; atoms are stable | only odds are predicted; measurement leaves a new state; superposition is not ignorance; incompatible properties |
| Myths defused | two places at once; conscious observer; detector "kicks" the particle | planetary atom; electron smeared out like fog | filters read labels; superposition means "both" or "don't know"; uncertainty means clumsy instruments |

### Strategy 1: Dots that build stripes

**Plan.** Experiment-first.

1. After the two-sentence core, set up the experiment in plain words: a source turned down so electrons leave one at a time, a barrier with two narrow slits, and a screen that flashes where each electron lands.
2. Build both classical expectations before showing any results. Tiny balls would each go through one slit or the other, so with both slits open you would just get the two one-slit patterns added together: a smooth patch with no stripes. Water ripples would arrive spread over the whole screen at once, not as single flashes.
3. Show what is actually seen. Each electron lands as one dot at an unpredictable spot, and after thousands of dots, bright and dark stripes appear (figure a-buildup).
4. Give the decisive detail. At the middle of a dark stripe, one open slit gives plenty of hits, but two open slits give (ideally) none. Opening a second route made arriving there *less* likely, which is impossible if chances simply add (figure a-compare).
5. Give the rule that explains it, which is what the theory is about. For each way the electron could reach a spot, the theory gives an *amplitude*: a wave-like number with a size and a rhythm, which can be in step or out of step with another. Add the amplitudes for routes that nothing tells apart; the chance is the square of the total's size. In step, they reinforce (bright); out of step, they cancel (dark).
6. Then the which-slit rule. If anything records which slit an electron used (a detector, or even one stray particle of light carrying that information away), the stripes vanish and you get the smooth sum, because routes that can be told apart add their chances, not their amplitudes. What matters is that a record exists, not that a person reads it.
7. Name the result: tiny things arrive whole, like particles, but their odds spread and interfere like waves. The older name for this is wave–particle duality.
8. Close with the map, seen from this experiment:
   - the same kind of amplitudes, hemmed in inside an atom, can form only certain patterns, which gives atoms fixed energies, their colors, their stability and all of chemistry;
   - optionally, the uncertainty principle as a fact about waves: a wave's wavelength is tied to the particle's momentum, and a wave squeezed into a small region must mix many wavelengths;
   - interference has been seen with atoms and with molecules of 60 carbon atoms, but everyday objects are constantly "recorded" by air and light, and their wavelengths are absurdly small.
9. Finish with the myths and one sentence on what is settled and what is open.

**Example.** Electrons sent one at a time through two slits, with two variations: one slit covered, and a which-slit detector switched on. Say the molecule result came from "similar interference experiments", because it used a grating, not two slits.

**Figures.**

`<!-- FIGURE: a-buildup | Four side-by-side panels of detection dots on a screen for a two-slit experiment with single particles, after N = 10, 100, 1000 and 10000 particles. Sample each dot's horizontal position u (screen position, arbitrary units, range -1.5 to 1.5) from P(u) proportional to [sin(pi u)/(pi u)]^2 * cos^2(4 pi u) (slit separation 4x slit width, giving about seven bright stripes under the central envelope); vertical position uniform random, only for visibility; small black dots on white; title each panel with N. What to notice: every particle lands as one dot at an unpredictable place, and the stripes only emerge statistically after many dots. -->`

`<!-- FIGURE: a-compare | One plot of relative probability (arbitrary units) against screen position u from -1.5 to 1.5, three curves: (1) 'one slit open' = S(u) = [sin(pi u)/(pi u)]^2; (2) 'both slits open, which-slit recorded' = 2 S(u), smooth with no stripes; (3) 'both slits open, nothing recorded' = 4 S(u) cos^2(4 pi u), with stripes whose peaks reach twice curve (2) and zeros in between. Draw a vertical dashed line at the first dark stripe, u = 0.125, with markers showing curve (1) is about 0.95 there while curve (3) is 0. What to notice: opening a second route makes some spots darker because the two routes' amplitudes cancel there; a which-slit record removes the cancellation. -->`

**Opening sentence.** "Quantum mechanics is the physics of light and matter at the scale of atoms and below, and its central idea is this: the theory usually predicts only the odds of each possible result, and it computes those odds from wave-like quantities, called amplitudes, that can add up or cancel out. One experiment shows what that means: fire electrons, one at a time, at a wall with two narrow slits."

**Check yourself (suggested).** "If you cover one of the two slits, will a spot that was in the middle of a dark stripe now get more hits, fewer, or the same?" (Answer: more.)

**Watch-outs.**
- Never say the electron "goes through both slits" or "is in two places". Say the theory assigns an amplitude to each route, and that what the electron "really does" in between is exactly what interpretations disagree about.
- Don't explain the vanishing stripes as the detector kicking the electron; the cause is that a which-slit record exists.
- Use in-step/out-of-step wave language, not arrows or clock hands, so the representation stays distinct from Strategy 3.

### Strategy 2: Atoms that play only certain notes

**Plan.** Analogy-led, with a classical-contrast hook.

1. After the core, show the phenomenon. Heat or electrify a gas and it glows in only a few sharp colors, a barcode that is different for every element: hydrogen's four visible lines, the orange of sodium streetlights, the red of neon signs, the colors of fireworks. A hot solid such as a light-bulb filament glows in every color (figure b-ladder, bottom).
2. Build the classical expectation. Picture the atom as a tiny solar system. An orbiting electron could have any energy, so it should glow in a smear of colors. Worse, classical physics says it would radiate its energy away and spiral into the nucleus in about a hundred-billionth of a second.
3. Introduce the analogy. A guitar string pinned at both ends can vibrate only in patterns that fit a whole number of half-waves between the pegs; each pattern sounds one note, and shorter strings sound higher notes (figure b-fits).
4. State the analogy's limits right away:
   - The electron's wave is not a vibration of any material. Its strength at a place (strictly, its height squared) gives the odds of finding the electron there, and when you look you always find a whole electron at one spot.
   - Unlike a string, it can't be played louder or softer. Its overall size is fixed because it describes exactly one electron, so each allowed pattern comes with exactly one energy. That is why the *energies*, not just the "notes", come in steps.
   - An atom is three-dimensional, and the nucleus's pull, not two pegs, hems the wave in. So the patterns are 3D shapes (orbitals), and their energy spacing is not a guitar's.
5. Use the analogy to predict:
   - more wiggles means more energy;
   - squeeze the wave into a smaller space and every pattern must wiggle more, so the energies and the gaps between them grow;
   - the lowest pattern is a floor with nothing below it, which is why atoms don't collapse;
   - when the electron changes to a lower pattern, the atom emits one photon carrying exactly the energy difference. $E = hf$ ($E$ is the photon's energy, $f$ its frequency, which we see as color, and $h$ is Planck's constant) turns each difference into one sharp color, one line of the barcode (figure b-ladder, top).
6. Close with the map, seen from atoms:
   - these waves can also add and cancel, which is why single electrons sent through two slits build up stripes, unless something records the slit;
   - an excited atom drops at a random moment and the theory predicts only the average, so QM deals in odds;
   - bonds between atoms are shared wave patterns;
   - lasers, LEDs, computer chips and quantum dots all run on these energy ladders.
7. Finish with the myths and one sentence on what is settled and what is open.

**Example.** Hydrogen's visible lines (656, 486, 434 and 410 nm), with sodium lamps, neon signs and fireworks as everyday instances. Quantum dots are the transfer case: smaller dots glow bluer (Nobel Prize in Chemistry 2023).

**Figures.**

`<!-- FIGURE: b-fits | A string fixed at x = 0 and x = 1 (draw small pegs at both ends). Plot the first three allowed standing-wave shapes y = sin(n pi x) for n = 1, 2, 3, stacked with vertical offsets and labelled 'pattern 1', 'pattern 2', 'pattern 3'; below them a dashed red curve y = sin(2.5 pi x) that ends at height 1 instead of 0 at x = 1, with a red cross at that end and the label 'doesn't fit'. What to notice: only whole numbers of half-waves fit between the pegs; more wiggles means a higher note (for an electron, a higher energy). -->`

`<!-- FIGURE: b-ladder | Top panel: hydrogen's energy ladder, horizontal levels at E_n = -13.6/n^2 eV for n = 1..6 plus a dashed line at 0 labelled 'electron set free'; y-axis labelled 'energy' with no numeric ticks; levels labelled 'pattern 1 (lowest)', 'pattern 2', ...; downward arrows from n = 3, 4, 5, 6 to n = 2, coloured and labelled 656 nm (red), 486 nm (blue-green), 434 nm (violet-blue), 410 nm (violet); small note that drops to pattern 1 give ultraviolet light, which is invisible. Bottom panel: two spectrum strips over 380-700 nm, a continuous rainbow labelled 'glowing hot solid: every color' and a black strip with four bright lines at those wavelengths labelled 'hydrogen gas: only certain colors'. What to notice: each line in the barcode is one drop between allowed energies, and the ladder is not evenly spaced like a guitar's notes. -->`

**Opening sentence.** "Quantum mechanics is the physics of atoms, electrons and light, and it takes its name from its first big discovery: at that scale energy often comes only in certain fixed amounts, or 'quanta'. An electron held inside an atom, for instance, can only have certain energies, for much the same reason that a guitar string can only sound certain notes. Behind this is the theory's central idea: an electron is described by a wave that gives the odds of finding it in each place, and a wave that is hemmed in can only settle into certain shapes."

**Check yourself (suggested).** "Quantum dots are tiny crystals that trap electrons in a very small space: would a smaller dot glow redder or bluer than a bigger one?" (Answer: bluer.)

**Watch-outs.**
- Say the electron "is described by" a wave, never "is" a wave, and don't use de Broglie's picture of a circular orbit with whole wavelengths around it (it fails for real atoms).
- The text must explicitly say that a smaller space means higher energies and bigger gaps, and that bigger energy means bluer light; otherwise the check question can't be answered from the text.
- Describe a quantum jump as changing from one pattern to a lower one while emitting a photon, not as teleporting along a path.
- $E = hf$ is the only equation.

### Strategy 3: The three-filter puzzle

**Plan.** Question-led, with polarization arrows as the representation.

1. After the core, give just enough setup:
   - light's polarization is a direction at right angles to its travel (picture an arrow);
   - a polarizing filter has a direction: it passes light polarized along that direction and blocks light polarized across it;
   - light comes in photons, and a photon either gets through a filter whole or is absorbed whole.
2. Then run four or five short beats, each written as **Predict:** followed by **What happens:**.
   - **Beat 1.** Ordinary light meets a vertical filter. Half gets through, and every photon that made it is now vertical.
   - **Beat 2.** Those vertical photons meet a second filter. If it is vertical, all pass; if horizontal, none; if tilted 45°, half pass, at random. The photons were prepared identically, nothing known about them says which will pass, and the theory predicts the 50% and nothing more.
   - **Beat 3.** Is a 45° photon secretly vertical or horizontal, and we just don't know which? If so, a 45° filter would pass only half of them, as it does for a mix of vertical and horizontal photons. But it passes all of them. So a 45° photon is a definite state of its own, which the theory describes as a particular combination (a *superposition*) of vertical and horizontal. It is not "both at once", and it is not "one or the other, unknown". Optionally, add the arrow-shadow picture: the chance of passing is the square of the length of the arrow's shadow along the filter (figure c-shadow).
   - **Beat 4, the puzzle.** Crossed vertical and horizontal filters let nothing through. Slip a 45° filter between them: does less light get out, or more? More: one-eighth of the original (figure c-filters). Every photon that passes the 45° filter comes out as a 45° photon with no memory of having been vertical, and the horizontal filter then passes half of those. Be honest here: with bright light, ordinary wave optics also predicts the one-eighth. The quantum point is that it still holds one photon at a time: whole photons, random passes, and a fresh state after every filter.
3. Draw the lessons:
   - a measurement is an interaction that leaves the object in a new state, not a passive reading;
   - "vertical or horizontal?" and "45° or 135°?" are incompatible questions: no photon state gives sure answers to both;
   - the same kind of incompatibility is the root of Heisenberg's uncertainty principle for position and momentum; it is a property of the states, not of clumsy filters.
4. Optionally, in at most two sentences: could each photon secretly carry a pre-written answer for every angle? Experiments with pairs of entangled photons (Nobel Prize in Physics 2022) rule out answers that are local, meaning fixed in advance and unaffected by what is done far away. Add that no message can be sent faster than light this way.
5. Close with the map, seen from here: the same rules (amplitudes that combine, odds that are their squares) produce the double-slit stripes, which vanish when anything records which slit, and the fixed energy ladders of atoms behind chemistry, lasers and computer chips.
6. Finish with the myths and one sentence on what is settled and what is open.

**Example.** Polarizing filters, the material in polarized sunglasses and the reason a laptop screen goes dark through tilted sunglasses, at 0°, 45° and 90°, with single photons.

**Figures.**

`<!-- FIGURE: c-filters | Schematic in two rows, light travelling left to right. Row 1, 'two crossed filters': unpolarized light (a few short double-headed arrows at random angles) -> filter drawn as a circle with a vertical line -> vertical double-headed arrows -> circle with a horizontal line -> nothing; under each stage the fraction of the original light: 1, 1/2, 0. Row 2, 'slip a 45-degree filter in between': unpolarized -> vertical filter -> 45-degree filter -> horizontal filter -> horizontal arrows out; fractions 1, 1/2, 1/4, 1/8. Between filters draw the light's polarization arrow along the previous filter's direction. What to notice: adding a filter in the middle lets through light that the two filters alone blocked completely. -->`

Optional, only if the draft uses the shadow rule:

`<!-- FIGURE: c-shadow | Main panel: an arrow of length 1 at 45 degrees from a vertical dashed line (the filter's direction); highlight its shadow (projection) on the vertical, length 0.71, and annotate 'chance to pass = 0.71 x 0.71 = 0.5'. Two small insets: arrow along the filter (shadow 1, chance 1) and arrow across it (shadow 0, chance 0). What to notice: the chance of passing is the square of the shadow's length, so a 45-degree photon passes a vertical filter half the time. -->`

**Opening sentence.** "Quantum mechanics is the theory of atoms, light and everything made of them, and two surprises sit at its heart: even when you know everything the theory lets you know about something, it usually predicts only the odds of what a measurement will show, and a measurement is not a passive look at a label the thing was already carrying. You can see both with three polarizing filters, the material in polarized sunglasses; try to predict each step before you read on."

**Check yourself (suggested).** "Light leaving a vertical filter passes, in order, a 45° filter, a horizontal filter and another 45° filter: what fraction makes it all the way through?" (Answer: ⅛.)

**Watch-outs.**
- Don't claim the ⅛ itself is uniquely quantum.
- Don't say the theory *never* predicts a result: a vertical photon at a vertical filter passes for certain.
- Avoid the picket-fence picture of a filter (it is backwards for real wire-grid polarizers).
- The filter sequence alone does not prove there are no hidden labels; it only shows measurement isn't passive. Any stronger claim needs Bell, with the locality qualifier.
- Keep "a filter leaves a new state" separate from the uncertainty principle.

## Common to all three

- **Level and length.** Conceptual: plain words, no formalism. Strategy 2 may use $E = hf$ (defined), and Strategy 3 may use simple fractions. Define every term the first time it appears (amplitude, photon, polarization, wave pattern). Aim for about 650–850 words, with no section headings; Strategy 3 may use bold **Predict:** / **What happens:** cues.
- **Core first.** The first two sentences say what QM is about:
  - it is the physics of light and matter at the scale of atoms and below (in principle, of everything);
  - it usually predicts odds, not certainties;
  - the odds come from wave-like amplitudes that can add or cancel;
  - confined things have only certain energies.

  Each opening leads with its own slice of this, and the body supplies the rest. Close the body with a sentence the learner could repeat as "what QM is about".
- **Stand alone (the rest of the map).** After the centerpiece, write three to five sentences from the candidate's own angle that cover what the centerpiece didn't:
  - interference, and how a which-way record erases it;
  - the fixed energy levels of atoms;
  - only odds are predicted;
  - measurement is not passive, and some pairs of properties can't both be sharp (the uncertainty principle is a property of states and waves, not of clumsy instruments);
  - optionally, entanglement, which sends no faster-than-light messages;
  - where QM matters: chemistry, lasers, LEDs, computer chips, MRI;
  - why everyday objects don't show interference: their surroundings constantly record "which way", and their wavelengths are unimaginably small. Don't imply that this settles the deeper puzzle.

  Name the standard terms when the route reaches them (superposition, wave–particle duality, uncertainty principle, entanglement), each with its plain meaning, but don't dump a glossary.
- **Settled versus open.** One or two even-handed sentences. The predictions are among the best tested in science. What is "really" happening between measurements, and what the quantum state is, are debated among interpretations (the measurement problem). Optionally, add that joining QM with gravity is also unsolved.
- **Myths.** Always say that "observation" means any physical interaction that leaves a record, not a mind. Add the strategy's own myths. Never present collapse as settled, never use "in two places at once" literally, never present uncertainty as measurement disturbance, and never invoke consciousness.
- **Ending.** Optionally, one line on what to explore next. Then exactly one **Check yourself:** line: a prediction the reader can work out from that candidate's own text, not a recall question.
- **Figures.** The a-/b-/c- prefixes assume Strategy 1 is A, Strategy 2 is B and Strategy 3 is C; change the prefix if the letter differs. Put each request on its own line where the figure belongs, at most two per candidate.
