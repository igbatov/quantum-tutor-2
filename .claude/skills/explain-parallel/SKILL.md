---
name: explain-parallel
description: Default tutor setup. A planning step chooses three different explanation strategies, three independent explainers write them in parallel, the student agent judges, and finalists are reviewed, verified and revised. Use for any quantum mechanics question in this project unless the learner names another setup.
argument-hint: "[question, or your answer to the last check question]"
allowed-tools: Bash(python3 *) Bash(mkdir *)
---

# Setup: parallel independent writers

Read `${CLAUDE_PROJECT_DIR}/.claude/tutor/common-steps.md` first and follow it; this file only says what is specific to this setup.

The learner's message: $ARGUMENTS
(If empty, use the learner's latest message in this conversation.)

1. Common step A, with `Setup: parallel`.
2. Delegate to **qm-explainer**, `mode: plan`, `K: 3`. It writes `strategies.md` with three strategies. Wait, and read the strategy names.
3. In the same turn, delegate three times to **qm-explainer**, `mode: draft`, one per strategy, with letters A, B, C. Each writes `candidate-<letter>.md` without seeing the others. Wait for all three.
4. Common step B: **student** `mode: judge`.
5. Common step C on each finalist, then D, then E.

Why this setup: each candidate is written by a fresh context committed to one route, so the candidates don't converge on the same example or wording, and the judge compares real alternatives. The trade-off is three full writer runs per question. Change `K` and the number of drafts together to adjust.
