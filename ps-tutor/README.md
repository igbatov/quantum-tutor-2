# PS tutor

A self-contained Claude Code project: a physicist agent explains at the intermediate level, a "digital twin" of the learner asks the follow-up questions the learner would ask, and an analyst agent updates the twin after every real question so it grows more like the learner.

## Use

```
cd ps-tutor
claude
```

Then:

- `ps: why is the sky blue?` — the loop: professor answers, twin asks up to `MAX_TWIN_QUESTIONS` (see `config.md`, default 6) questions, professor replies to each, then writes one consolidated answer. You see the consolidated answer and the list of questions the twin asked.
- `why is the sky blue?` — the professor answers you directly; the analyst uses your question to update the twin.
- `quick: …` — a direct answer without agents.

The twin's behaviour is in `twin/profile.md`. Edit it by hand if the analyst got something wrong; your edits win. `twin/changelog.md` records every change the analyst made and why.

## Moving to its own repository

This directory needs nothing from the parent repository (it carries its own copy of the quantum-explainer skill). To make it a separate repository, copy the directory or run `git subtree split -P ps-tutor`.
