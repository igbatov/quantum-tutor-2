<!-- strategy: experiment-first: the double slit, one electron at a time -->

Quantum mechanics is the theory of how matter and light behave at the scale of atoms, and the quickest way to see what it is about is one experiment: fire electrons, one at a time, at a wall with two narrow slits, and record where each one lands.

Behind the slits, a screen flashes wherever an electron hits. The beam is so faint that only one electron is in flight at a time, so nothing can be blamed on electrons bumping into each other. Before reading on, guess what pattern builds up.

If you pictured tiny balls, each going through one slit or the other, you probably expected a smooth spread of hits with no pattern. Here is what real experiments find. Each electron does arrive whole, as one dot, at a spot nobody can predict; quantum mechanics gives only the chances. But as thousands of dots accumulate, stripes appear: bands where many electrons land, separated by bands where almost none do.

<!-- FIGURE: a-buildup | Simulated two-slit detection screen, four panels side by side titled "10 electrons", "100 electrons", "1,000 electrons", "10,000 electrons" (cumulative: each panel keeps the previous dots and adds more; fixed random seed). Each electron is one small black dot on a white rectangle. Horizontal position X (in units of the stripe spacing, range -6 to 6) is drawn at random from P(X) proportional to cos^2(pi X) * [sin(pi X/4)/(pi X/4)]^2, i.e. slit separation = 4 x slit width; vertical position uniform at random (the slits are long vertical slots). Shrink the dot size in later panels so 10,000 dots stay readable. No tick numbers; x-axis label "position on screen". The learner should notice: every electron arrives whole, as one dot at an unpredictable place, and the stripes exist only in the pattern of many dots. -->

Now close one slit. The stripes vanish, leaving one broad hump. Take a spot in the first dark stripe beside the centre. With one slit open, electrons land there nearly as often as at the hump's peak; with both open, essentially never. Opening a second way to get there made the spot unreachable. If each electron simply went through one slit or the other, opening the second slit could only add hits there, never remove them.

<!-- FIGURE: a-one-vs-two | Line plot over screen positions X from -6 to 6 (units of the stripe spacing, same set-up as a-buildup). Three curves of relative chance of landing per unit length: (1) "one slit open (either one)": P1(X) = [sin(pi X/4)/(pi X/4)]^2, thin grey; (2) "if each electron went through one slit or the other (also the result with a which-slit detector)": 2*P1(X), dashed; (3) "both slits open (what is actually seen)": 4*P1(X)*cos^2(pi X), solid and bold. Mark the dark stripes at X = -1.5, -0.5, 0.5, 1.5 with small downward arrows: there curve 3 is exactly zero while curve 1 is clearly above zero (about 0.95 at |X| = 0.5 and 0.62 at |X| = 1.5). y-axis "relative chance of landing here", x-axis "position on screen". The learner should notice: at the dark stripes an electron could land with one slit open, but opening the second slit made those spots unreachable; chances did not add, amplitudes cancelled. Also visible: at the bright stripes the bold curve rises above the dashed one (twice as high at the centre), so the electrons missing from the dark stripes turn up in the bright ones. -->

The rule that fits: quantum mechanics gives each of the two routes to a spot an *amplitude*, a number that, like the height of a wave, can be positive or negative (in the full theory, a complex number). When nothing records which route was taken, you add the two amplitudes first, and squaring the size of that total sets the chance of landing there. Each amplitude depends on the route's length, so at some spots the two are equal and opposite and cancel: the dark stripes. Where they match, they reinforce: the bright stripes. This adding and cancelling is called interference.

Noise-cancelling headphones use the same arithmetic: they play a sound that is high wherever the noise is low, so the two add to silence. But sound is a wave of air; an amplitude is not a wave of any stuff, and no detector ever finds part of an electron.

Last twist: let a detector record which slit each electron uses. The stripes disappear, and you get the two one-slit humps simply added: the smooth spread you first guessed. With a record, you add chances instead of amplitudes, so nothing cancels. Even one stray photon bouncing off the electron is enough if it carries away which-slit information, and nobody ever has to read it. "Observing" here means any physical record, not a mind.

That one experiment shows much of what quantum mechanics is about:

- **Lumps.** Electrons, and light too, are detected only in whole units (quanta, hence the theory's name), even when they build a wave-like pattern.
- **Chances.** The theory predicts the odds of each outcome, not which one happens.
- **Amplitudes.** Odds come from amplitudes that add and cancel. Applied to electrons in atoms, the same rules set atoms' allowed energies and how they bond: the basis of chemistry, transistors and lasers.
- **Records.** Possibilities interfere only until something records which one happened. Air and light bouncing off big objects constantly record where they are, washing out their interference almost instantly; well-isolated molecules of hundreds of atoms still make stripes.

You'll often hear that the electron "goes through both slits" or "is in two places at once". That goes beyond the theory, which says only that both routes' amplitudes shape where the electron lands. Interpretations of the theory disagree about what the electron does in between, and about what measurement does to it. In one, it follows a single definite path, steered by both routes' amplitudes; in another, there is no fact about which slit it used unless something records it. All of them predict the same dots and stripes, exactly as observed.

A good next step is decoherence: how that constant record-keeping hides quantum effects in everyday things, and what it leaves unexplained.

**Check yourself:** At a dark stripe, if you close one slit, do electrons start landing there or does it stay dark, and why?
