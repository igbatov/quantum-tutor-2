---
name: explain-teachback
description: "Three independent candidate explanations of a quantum mechanics question are selected by testing, not by reading: a physicist writes a probe exam, a student agent sits it using only one candidate at a time, and the candidate that produced the best answers wins; finalists are reviewed, verified and revised. Use when the learner asks for the teach-back or exam-based setup."
argument-hint: "[question, or your answer to the last check question]"
allowed-tools: Bash(python3 *) Bash(mkdir *)
---

# Setup: teach-back selection

Read `${CLAUDE_PROJECT_DIR}/.claude/tutor/common-steps.md` first and follow it; this file only says what is specific to this setup.

The learner's message: $ARGUMENTS
(If empty, use the learner's latest message in this conversation.)

1. Common step A, with `Setup: teachback`.
2. **qm-explainer**, `mode: plan`, `K: 3`. Wait.
3. Same turn: three **qm-explainer** runs, `mode: draft`, letters A, B, C, and one **physics-critic** run, `mode: exam`, which writes `exam.md` and returns the ANSWER KEY in its reply. Keep the key in your context; it must not go into the run folder. Wait for all four.
4. Same turn: three **student** runs, `mode: examinee`, one per candidate, each told only its candidate file and `exam.md`. They write `exam-answers-<letter>.md`. Wait.
5. **physics-critic**, `mode: grade`, with the answer key and the three answer sheets. It writes `exam-results.md` with `BEST`, `TIE` and `FINALISTS`. Wait.
6. The finalists are the letters in `FINALISTS` (within one point of the best). If there is more than one, also run **student** `mode: judge` on the finalists only, so the learner gets its one-line notes; keep the exam's finalist list even if the judge would narrow it.
7. Common step C on each finalist, then D (mention the exam scores in the Checked block), then E.

Why this setup: it selects by measured transfer, what a learner can do after reading, instead of a judge's impression of the prose. It also finds explanations that read well but don't teach. The trade-off is that the examinee is a model of the learner, not the learner, and the exam adds five runs.
