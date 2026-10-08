# Quantum tutor

This project is a quantum mechanics tutor, not a codebase. The person working here is a learner.

- Route every substantive quantum mechanics question, follow-up, request for "another angle", "simpler" or "more math", and every answer to a "Check yourself" question through a tutor setup. The default is `/explain-parallel`. The learner can name another: `/explain` (baseline, one draft), `/explain-multi`, `/explain-debate`, `/explain-teachback`, or `/explain-bakeoff` (runs several and compares).
- The setups share one team of subagents: qm-explainer, physics-critic, student, math-verifier, learner-modeler. The shared procedure is in `.claude/tutor/common-steps.md`.
- When the student agent can't pick a clear winner among candidate explanations, all finalists are shown and the learner chooses. Record their choice; it shapes future explanations.
- If the learner starts a message with "quick:", answer directly in this conversation using the quantum-explainer skill, without any pipeline.
- `/progress` summarizes what the tutor knows about the learner and suggests what to study next.
- Learner notes live in `learner/profile.md` and `learner/history.md`. The learner may edit them by hand; their edits win.
- Each run's working files live in `work/<run-id>/`.
- Keep your own messages short. The explanation itself is the answer; don't add commentary around it.
