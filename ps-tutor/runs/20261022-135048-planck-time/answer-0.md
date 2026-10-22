# Is Planck time the shortest possible time?

**The premise is wrong.** No experiment and no accepted theory shows that the Planck time, $t_P \approx 5.4\times10^{-44}$ s, is the shortest possible time. What can be said is narrower: $t_P$ is the time scale you can build from $\hbar$, $G$ and $c$, and near it our current theories are expected to stop giving reliable predictions. That is a limit of our theories. It is not a proven minimum in nature.

## 1. Where the number comes from (established: arithmetic)

We look for powers $a$, $b$, $d$ such that $\hbar^a G^b c^d$ has the unit of seconds. The units of the three constants are $[\hbar] = \mathrm{kg\,m^2\,s^{-1}}$, $[G] = \mathrm{m^3\,kg^{-1}\,s^{-2}}$ and $[c] = \mathrm{m\,s^{-1}}$. The power of each unit must match on both sides:
- kg: $a - b = 0$, so $b = a$
- m: $2a + 3b + d = 0$. With $b = a$ this gives $5a + d = 0$, so $d = -5a$
- s: $-a - 2b - d = 1$. Substituting gives $-a - 2a + 5a = 2a = 1$, so $a = \tfrac12$

The result is
$$t_P = \sqrt{\frac{\hbar G}{c^5}}, \qquad \ell_P = c\,t_P = \sqrt{\frac{\hbar G}{c^3}}.$$

Putting in the numbers:
- $\hbar G = (1.0546\times10^{-34})(6.674\times10^{-11}) = 7.039\times10^{-45}$
- $c^5 = (2.998\times10^{8})^5 = 2.422\times10^{42}$
- the ratio is $2.906\times10^{-87}$, and its square root is $t_P \approx 5.39\times10^{-44}$ s
- the Planck length is then $\ell_P \approx 1.62\times10^{-35}$ m

Two caveats:
- **The number is only defined up to a dimensionless factor.** If you use $h$ instead of $\hbar$, you get a value $\sqrt{2\pi}\approx2.5$ times larger. If you use $8\pi G$ (the combination that appears in Einstein's equations), you get $\approx 2.7\times10^{-43}$ s. Dimensional analysis fixes the order of magnitude, not a sharp edge.
- **A unit is not a minimum.** In Planck units, $0.01\,t_P$ is a valid number, just as a time of 0.01 s is perfectly meaningful. Planck proposed these units in 1899 because they do not depend on human conventions. He did not propose them as a lower limit on time.

## 2. Why physicists expect new physics near $t_P$

**(a) A thought experiment that mixes two theories (heuristic).** Suppose you want to resolve a time interval $\Delta t$. You need a probe localized within $L = c\,\Delta t$.

1. *Quantum input.* Light resolves features about as small as its wavelength, so you need $\lambda \lesssim L$ (an order-of-magnitude statement). A photon has energy $E = hc/\lambda = 2\pi\hbar c/\lambda$ (established). So $E \gtrsim 2\pi\hbar c/L$.
2. *Gravity input.* In classical general relativity, a spherical mass $M$ inside its Schwarzschild radius $r_s = 2GM/c^2$ forms a black hole (established for the Schwarzschild solution). With $M = E/c^2$ this becomes $r_s = 2GE/c^4$. For energy that is not spherical, the "hoop conjecture" says roughly the same thing, but it is a conjecture. A single photon's energy depends on the observer's frame, so $E$ here has to be the energy in the frame where the total momentum is zero, for example two photons colliding head-on.
3. *Combine.* Take the smallest energy allowed by step 1 ($\lambda = L$) and set $L = r_s$:
   $$L = \frac{2G}{c^4}\cdot\frac{2\pi\hbar c}{L} \;\Rightarrow\; L^2 = \frac{4\pi\hbar G}{c^3} \;\Rightarrow\; L = \sqrt{4\pi}\,\ell_P \approx 3.5\,\ell_P.$$
   Dividing by $c$ gives $\Delta t \approx 3.5\,t_P$.

For shorter $L$, the energy required by step 1 gives $r_s > L$. By this argument, the probe would be inside its own horizon before it could resolve the interval. **But the argument applies classical general relativity and the quantum relation $E = hc/\lambda$ together, in the very regime where neither has been tested and a quantum theory of gravity would be needed.** So it is a reason to expect new physics there, not a derivation of a minimum time.

**(b) Gravity as a low-energy quantum field theory (established within this framework, valid for $E \ll E_P$).** General relativity can be treated as an "effective" quantum field theory. In it, the size of the quantum corrections at energy $E$ is set by the dimensionless number
$$\frac{GE^2}{\hbar c^5} = \left(\frac{E}{E_P}\right)^2, \qquad E_P = \sqrt{\frac{\hbar c^5}{G}} \approx 1.96\times10^{9}\ \text{J}.$$
As a check, $\hbar/E_P = \sqrt{\hbar^2 G/(\hbar c^5)} = \sqrt{\hbar G/c^5} = t_P$. A process on time scale $\Delta t \sim \hbar/E$ therefore has corrections of order $(t_P/\Delta t)^2$. These are tiny for any process we can study, and they reach order 1 near $t_P$. Order 1 means this approximation scheme stops working there. It does not mean time stops being continuous.

## 3. What is actually known

- **Established:** As these theories are formulated, quantum mechanics, quantum field theory and general relativity all treat time (or spacetime) as a continuum. None of them contains a smallest interval.
- **Not verified by me in detail:** The shortest interval timed directly is about $2.5\times10^{-19}$ s: photoemission from H$_2$, Grundmann et al., *Science* 2020. Collider collisions indirectly probe roughly $\hbar/E \sim 10^{-28}$ s (order of magnitude). Both are more than 15 orders of magnitude above $t_P$.
- **Established (not verified by me in detail):** The Fermi telescope found no detectable energy-dependent delay in photon arrival times from gamma-ray burst GRB 090510. Models in which the speed of light changes linearly with photon energy would produce such a delay. For those models, the result puts the energy scale of the effect above roughly $E_P$, under assumptions about when the photons were emitted (Abdo et al. 2009).
- **Contested:** Candidate theories of quantum gravity disagree with one another.
  - In loop quantum gravity, the area and volume operators have discrete spectra. Whether these are physically observable is debated.
  - Some string-theory analyses find that distances below a certain size cannot be resolved, but no lattice of time.
  - Causal set theory postulates discreteness from the start.
  - None of these theories is confirmed by experiment, and none of them predicts a smallest duration exactly equal to $t_P$.

**Bottom line:** $t_P$ marks where our theories are expected to need replacement. Argument (a) is heuristic and argument (b) is the more solid one. Whether a shortest time exists is an open question.

---

**Check yourself:** In argument 2(a), which step uses quantum theory and which uses general relativity? Why does combining them justify only "our theories become unreliable here", not "time is discrete here"?

**Sources:** Zwiebach, *A First Course in String Theory* (2nd ed.), ch. 3 (Planck units); Carroll, *Spacetime and Geometry*, ch. 5 (Schwarzschild solution); Griffiths, *Introduction to Quantum Mechanics*, ch. 3 (uncertainty principle); Rovelli, *Reality Is Not What It Seems* (popular, loop gravity); Hossenfelder, "Minimal Length Scale Scenarios for Quantum Gravity", *Living Rev. Relativ.* 16, 2 (2013); Abdo et al., *Nature* 462, 331 (2009); Planck, *Sitzungsber. Preuss. Akad. Wiss.* (1899), "Über irreversible Strahlungsvorgänge".
