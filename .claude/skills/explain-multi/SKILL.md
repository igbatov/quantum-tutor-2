---
name: explain-multi
description: One explainer writes three deliberately different candidate explanations of a quantum mechanics question after planning the strategies; the student agent judges; finalists are reviewed, verified and revised. Use when the learner asks for the multi-draft or single-writer setup.
argument-hint: "[question, or your answer to the last check question]"
allowed-tools: Bash(python3 *) Bash(mkdir *)
---

# Setup: one writer, several candidates

Read `${CLAUDE_PROJECT_DIR}/.claude/tutor/common-steps.md` first and follow it; this file only says what is specific to this setup.

The learner's message: $ARGUMENTS
(If empty, use the learner's latest message in this conversation.)

1. Common step A, with `Setup: multi`.
2. Delegate to **qm-explainer**, `mode: multi`, `K: 3`. It plans at least six lenses in `strategies.md`, picks the three most different high-fit ones, and writes `candidate-A.md`, `candidate-B.md`, `candidate-C.md`. Wait.
3. Common step B: **student** `mode: judge` over the three candidates.
4. Common step C on each finalist, then D, then E.

Why this setup: one writer sees all three plans at once, so it can keep them genuinely different, and it costs one writer run instead of three. The trade-off is that one context writes all three, so they share the same blind spots. Change `K` in step 2 to get more or fewer candidates.
