---
name: explain
description: "Baseline tutor pipeline for a quantum mechanics question: one draft, physics review, student review, computational verification, revision. The cheapest full-quality setup. Use when the learner asks for the baseline or single-draft version."
argument-hint: "[question, or your answer to the last check question]"
allowed-tools: Bash(python3 *) Bash(mkdir *)
---

# Baseline pipeline (one draft)

Read `${CLAUDE_PROJECT_DIR}/.claude/tutor/common-steps.md` first and follow it; this file only says what is specific to this setup.

The learner's message: $ARGUMENTS
(If empty, use the learner's latest message in this conversation.)

1. Common step A, with `Setup: explain`.
2. Delegate to **qm-explainer**, `mode: draft`, no strategy (it picks the best-fitting experiments and models). Output `draft.md`. Wait.
3. Common step C on the single candidate `draft.md`, treating its letter as none: reviews `review-physics.md`, `review-learner.md` (run **student** `mode: review` here, since there is no judge), `verify.md`; revised output `final.md`.
4. Common step D with one finalist, then step E.
