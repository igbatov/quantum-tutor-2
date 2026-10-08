---
name: explain-debate
description: Two explainers write rival explanations of a quantum mechanics question from different strategies, critique each other's, revise, and the student agent judges; finalists are verified and revised. Use when the learner asks for the debate setup, or for subtle or contested topics.
argument-hint: "[question, or your answer to the last check question]"
allowed-tools: Bash(python3 *) Bash(mkdir *)
---

# Setup: debate

Read `${CLAUDE_PROJECT_DIR}/.claude/tutor/common-steps.md` first and follow it; this file only says what is specific to this setup.

The learner's message: $ARGUMENTS
(If empty, use the learner's latest message in this conversation.)

1. Common step A, with `Setup: debate`.
2. **qm-explainer**, `mode: plan`, `K: 2`: the two most different high-fit strategies. Wait.
3. Same turn, two **qm-explainer** runs, `mode: draft`, letters A and B. Wait.
4. Same turn, two **qm-explainer** runs, `mode: critique`: one reads its own candidate A and critiques B (`critique-of-B.md`), the other critiques A (`critique-of-A.md`). Wait.
5. Same turn, two **qm-explainer** runs, `mode: revise`, each on its own candidate, reading the critique of it and the rival's candidate. Output `candidate-A.md` and `candidate-B.md` again (overwrite; the originals are kept as `candidate-A-v1.md`, `candidate-B-v1.md`: tell each run to save the original first). Wait.
6. Common step B: **student** `mode: judge` over the revised A and B.
7. Common step C on each finalist (the physics review and verifier still run; peer critique is not a substitute), then D, then E.

Why this setup: a rival with a different route catches omissions and misleading simplifications that a neutral reviewer reads past, and each candidate improves before judging. The trade-off is six writer runs for two candidates, so it is the slowest setup. Best for subtle topics: measurement, Bell's theorem, interpretations, identical particles.
