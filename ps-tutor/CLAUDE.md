# PS tutor

A physics tutor with three agents and one learner. Open Claude Code in this directory (`ps-tutor/`) to use it; its rules take precedence over the routing rules in the repository root `CLAUDE.md`.

- **ps-professor**: a professional physicist who explains at the intermediate level, marks the status of every claim, and shows every derivation step.
- **ps-twin**: the learner's digital twin. It asks the follow-up questions the real learner would ask, following `twin/profile.md`.
- **ps-analyst**: reads every real question the learner asks and edits `twin/profile.md` so the twin grows more like the learner.

## Routing

- A message that starts with **`ps:`** runs the `/ps` loop: professor answers, twin asks, professor replies, until the twin has no questions or `MAX_TWIN_QUESTIONS` in `config.md` is reached; then the professor writes one consolidated answer, which is what the learner sees; then the analyst updates the twin from the learner's own message.
- Any other message that is a physics question (no prefix) goes **directly to ps-professor** (`mode: answer`, then show `answer-0.md` in full), and **ps-analyst** uses the learner's message to update the twin. The twin does not run.
- A message that starts with **`quick:`** is answered by the orchestrator directly from the quantum-explainer skill, without agents, and is still logged by the analyst.
- `/progress`-style requests about the twin: show `twin/profile.md` and the last lines of `twin/changelog.md`.

## Files

- `config.md`: limits and level.
- `twin/profile.md`: the twin's behaviour; the learner may edit it by hand, and their edits win.
- `twin/question-log.md`, `twin/changelog.md`: the analyst's records.
- `runs/<id>/`: one folder per learner message: `learner-question.md`, `answer-0.md`, `question-n.md`, `answer-n.md`, `final.md`, `analyst.md`.
- `analysis/`: one-off analyses of the learner's questions.

Keep orchestrator messages short; the professor's text is the answer.
