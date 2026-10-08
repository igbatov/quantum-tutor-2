VERDICT: revise

## Issues
- [major] Figure a-one-vs-two.png legend: "if each electron went through one slit or the other" — The caption was fixed, but the PNG was not redrawn (checks/fig_a-one-vs-two.py lines 12-13 and 18 still carry the round-2 labels). Three labels in the image are still false as written or contradict the caption. (1) This dashed-curve label has no "unaffected by the other slit" condition, so it again rules out the pilot-wave picture that paragraph 28 presents as viable. That was the round-2 major item. (2) "both slits open (what is actually seen)" labels an ideal curve with exact zeros as the observed data, while the caption says real experiments reach only "nearly zero". (3) The annotation "dark stripes, where both slits give zero" has the same unnamed idealization. Fix: regenerate the figure with these labels: dashed "one-slit chances simply added (also an ideal which-slit detector)"; bold "both slits open, nothing recording the slit (ideal set-up)"; annotation "arrows: dark stripes, zero in this ideal calculation; circles: one slit alone (0.95 and 0.62)".
- [minor] "you add chances instead of amplitudes, so nothing cancels" — In context this means the two routes no longer cancel each other, which is true. But the one-slit pattern's own dark gaps (shown in the bottom panel at ±4 and ±8) come from cancellation within a single slit, so the unqualified "nothing" is broader than intended. Fix: "so the two routes no longer cancel each other".

Round-2 items checked:
- "One broad hump": fixed. Text and caption now give a wide central band with fainter side bands, and the zoom panel shows them.
- "Smooth spread": fixed. The text now says "exactly the two one-slit patterns added together, much like the broad spread".
- Unaffected-by-the-other-slit condition: fixed in the text, not in the figure legend (see above).
- Ideal zeros: fixed in the text and caption, not in the figure legend (see above).
- Partial records: fixed ("a fuzzy record only fades them").
- Headphones "silence": fixed ("largely cancel", "much quieter").
- Scope of the opening sentence: fixed.
- The 95% figure: fixed. It is now tied to "the set-up plotted below", which specifies a separation of 4 slit-widths.

Numbers rechecked: sinc²(1/8) ≈ 0.95 and sinc²(3/8) ≈ 0.62. The centre is 4 vs 2 (twice). The totals are exactly equal, because the Fourier support of sinc²(X/4) is |f| ≤ 1/4 and cos(2πX) lies outside it. The first side lobe is 0.047 (about 5%). The zoom factor is 4.6/0.25 ≈ 18. No new false statements were found in the text.

## Sound points worth keeping
- The text now names every idealization: ideal vs real zeros, an ideal which-slit detector, fuzzy vs reliable records, and the set-up behind the 95% figure. The one-slit pattern is described correctly, and the figure shows it.
- Interpretations are handled evenly: "two places at once" is flagged as going beyond the theory, and one pilot-wave-style view and one no-fact view are both given, with identical predictions.
