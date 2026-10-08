---
name: explain-bakeoff
description: Run several tutor setups on the same quantum mechanics question and show their results side by side so the learner can pick. Expensive. Use only when the learner explicitly asks to compare setups or asks for the bakeoff.
argument-hint: "[question] [--setups multi,parallel,debate,teachback]"
disable-model-invocation: true
allowed-tools: Bash(python3 *) Bash(mkdir *)
---

# Setup: bakeoff

The learner's message: $ARGUMENTS

This runs several complete setups on one question. Default setups: `multi`, `parallel`, `debate`, `teachback`. If the message ends with `--setups a,b,c`, run only those. Each costs a full pipeline; warn the learner in one sentence about time and usage before starting, then proceed.

1. For each setup, in turn, invoke its skill (`/explain-multi`, `/explain-parallel`, `/explain-debate`, `/explain-teachback`) with the same learner message. Each uses its own run folder. Tell each one, in the invocation, to **skip** common steps D (presenting) and E (learner model) and instead report back its run folder and finalist letters.
2. When all have finished, present the results:
   - For each setup, a heading `## Setup: <name>`, then each finalist in full under `### Explanation <letter>: <strategy>` with the student's note, and the Checked block for that setup.
   - If two setups produced the same strategy, show it once and say which setups chose it.
3. Ask the learner which explanation they prefer, then write `choice.md` in that setup's run folder (common step D) and run the learner-modeler on it (step E) once.
